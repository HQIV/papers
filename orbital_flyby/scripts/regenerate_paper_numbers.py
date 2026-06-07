#!/usr/bin/env python3
"""
Regenerate canonical numbers for hqiv_accelerations_galaxy_evolution.tex.

Run from repo root:
  PYTHONPATH="HQIV_LEAN/scripts:${PWD}" \\
    python HQIV_LEAN/papers/orbital_flyby/scripts/regenerate_paper_numbers.py

Writes:
  papers/orbital_flyby/artifacts/paper_numbers.json
  papers/orbital_flyby/flyby_paper_table.tex
"""

from __future__ import annotations

import json
import sys
from dataclasses import replace, asdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SCRIPTS = ROOT / "HQIV_LEAN" / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import hqiv_orbital_flyby_omaxwell as orb  # noqa: E402
import hqiv_sparc_rotation as sparc  # noqa: E402
from hqiv_flyby_equations import format_paper_table_latex  # noqa: E402
from hqiv_observational_errors import flyby_literature_sigma_mm_s  # noqa: E402
from hqiv_wide_binary import batch_all_chae_systems  # noqa: E402

PAPER_DIR = Path(__file__).resolve().parents[1]
ARTIFACT = PAPER_DIR / "artifacts" / "paper_numbers.json"
TABLE_TEX = PAPER_DIR / "flyby_paper_table.tex"

EARTH_KEYS = ("near_1998", "galileo_1990", "cassini_1999", "rosetta_2005")


def flyby_row(coupling: orb.HQIVOrbitCoupling, key: str) -> dict[str, object]:
    case = orb.FLYBY_CATALOG[key]
    settings = orb.propagation_settings_for(orb.EARTH, case)
    result = orb.compare_classical_vs_hqiv(case, orb.EARTH, coupling, settings)
    classical = result["classical"]
    hqiv = result["hqiv"]
    lit = float(case.reported_anomaly_mm_s or 0.0)
    excess = float(result["hqiv_minus_classical_mm_s"])
    sig = flyby_literature_sigma_mm_s(key, fallback=float("nan"))
    residual = excess - lit
    n_sigma = residual / sig if sig == sig and sig > 0 else None
    return {
        "case_id": key,
        "reported_anomaly_mm_s": lit,
        "literature_sigma_mm_s": sig,
        "classical_delta_v_mm_s": classical["delta_v_mm_s"],
        "hqiv_delta_v_mm_s": hqiv["delta_v_mm_s"],
        "hqiv_minus_classical_mm_s": excess,
        "hqiv_minus_literature_mm_s": residual,
        "residual_n_sigma": n_sigma,
        "r_ca_km": hqiv["r_ca_km"],
        "mean_one_minus_f_out": hqiv.get("mean_one_minus_f_out", hqiv.get("mean_one_minus_f")),
        "asymptote_lat_in_deg": classical["asymptote_lat_in_deg"],
        "asymptote_lat_out_deg": classical["asymptote_lat_out_deg"],
    }


def main() -> int:
    nominal = orb.paper_nominal_coupling()
    flyby_nominal = {k: flyby_row(nominal, k) for k in EARTH_KEYS}

    ablation_specs = [
        ("lit", None),
        ("nominal", nominal),
        ("fixed_lambda_0.5", replace(nominal, lapse_drag_vector_fraction=0.5)),
        ("drop_lt", replace(nominal, lapse_drag_lense_thirring=False)),
        ("drop_colatitude_lt", replace(nominal, lapse_drag_colatitude=False, lapse_drag_lense_thirring=False)),
        ("drop_geodesic", replace(nominal, modified_inertia_geodesic=False)),
        ("drop_spin_lapse", replace(nominal, lapse_drag_phi=False)),
        ("drop_galactic_rindler", replace(nominal, galactic_disk_lapse_phi=False)),
    ]
    ablations: dict[str, dict[str, float]] = {}
    for label, coupling in ablation_specs:
        if coupling is None:
            ablations[label] = {k: flyby_nominal[k]["reported_anomaly_mm_s"] for k in EARTH_KEYS}  # type: ignore[index]
        else:
            ablations[label] = {
                k: round(float(flyby_row(coupling, k)["hqiv_minus_classical_mm_s"]), 4)
                for k in EARTH_KEYS
            }

    near_dt: list[dict[str, float]] = []
    case = orb.FLYBY_CATALOG["near_1998"]
    for dt in (4.0, 2.0, 1.0, 0.5):
        settings = replace(orb.propagation_settings_for(orb.EARTH, case), dt=dt)
        r = orb.compare_classical_vs_hqiv(case, orb.EARTH, nominal, settings)
        near_dt.append(
            {
                "dt_s": dt,
                "classical_delta_v_mm_s": float(r["classical"]["delta_v_mm_s"]),
                "hqiv_delta_v_mm_s": float(r["hqiv"]["delta_v_mm_s"]),
                "excess_mm_s": float(r["hqiv_minus_classical_mm_s"]),
            }
        )

    sparc_opts = sparc.SparcOptions()
    catalog = sparc.load_sparc_catalog()
    selected = sparc.select_galaxies(
        catalog,
        quality_cut=2,
        min_inclination_deg=30.0,
    )
    per_whim = sparc.run_catalog(selected, options=sparc_opts)
    per_floor = sparc.run_catalog(
        selected,
        options=replace(sparc_opts, whim_filament=False),
    )
    sparc_whim_summary = sparc.summarize_catalog(per_whim)
    sparc_floor_summary = sparc.summarize_catalog(per_floor)
    ddo_whim = sparc.evaluate_galaxy(catalog["DDO154"], options=sparc_opts)["summary"]
    ddo_floor = sparc.evaluate_galaxy(
        catalog["DDO154"],
        options=replace(sparc_opts, whim_filament=False),
    )["summary"]

    chae = batch_all_chae_systems(use_rindler_denominator=False)

    payload = {
        "flyby_earth_nominal": flyby_nominal,
        "flyby_ablations_mm_s": ablations,
        "near_dt_convergence": near_dt,
        "sparc_whim_summary": sparc_whim_summary,
        "sparc_cosmic_floor_summary": sparc_floor_summary,
        "ddo154": {
            "chi2_red_whim": ddo_whim["chi2_red_hqiv"],
            "chi2_red_floor": ddo_floor["chi2_red_hqiv"],
        },
        "chae_aggregate": chae["aggregate"],
    }

    ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    table_rows = [flyby_nominal[k] for k in EARTH_KEYS]
    TABLE_TEX.write_text(format_paper_table_latex(table_rows) + "\n", encoding="utf-8")

    print(f"Wrote {ARTIFACT}")
    print(f"Wrote {TABLE_TEX}")
    print("Flyby nominal HQIV-cls [mm/s]:", {k: flyby_nominal[k]["hqiv_minus_classical_mm_s"] for k in EARTH_KEYS})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
