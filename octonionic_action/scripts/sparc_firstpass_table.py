#!/usr/bin/env python3
"""
sparc_firstpass_table.py
========================

Reproducer for Table 2 (``tab:sparc-firstpass``) of

    "Octonionic Action from the HQIV-LEAN Variational Layer:
     Derivation, Holonomy Alignment, and a Tiered Uniqueness Thesis"

This script runs the HQIV galaxy-rotation calculator on the six built-in
exponential-disk presets (M33, NGC 2403, NGC 3198, NGC 6503, DDO 154, UGC 2885)
with **no fit parameters**, **no halo**, and the angular Rindler denominator on
by default. Inputs are the literature stellar mass and disk scale length; the
HQIV inertia factor is the same f(a, phi) = a / (a + phi/6) used by the flyby
calculator. The output is the per-row baryonic / HQIV / observed circular
speeds at the reference radius, in km/s.

Usage
-----
    python sparc_firstpass_table.py            # JSON to stdout
    python sparc_firstpass_table.py --markdown # GitHub-flavoured Markdown
    python sparc_firstpass_table.py --latex    # LaTeX tabular fragment

Provenance
----------
The implementation in ``hqiv_galaxy_rotation.py`` (snapshot bundled alongside
this script) is the exact module used by the HQIV-Orbital companion harness
(https://github.com/HQIV/HQIV_Orbital, see also the orbital-flyby paper). No
modifications are applied here. Re-running this script with the same Python
interpreter must yield the values listed in Table 2 to the displayed
precision.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from typing import Any

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import hqiv_galaxy_rotation as g  # noqa: E402

PRESET_ORDER = ["m33", "ngc2403", "ngc3198", "ngc6503", "ddo154", "ugc2885"]


def compute_rows() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for name in PRESET_ORDER:
        payload = g.preset_payload(
            name, n=40, projection=1.0, use_rindler_denominator=True
        )
        ref = payload["reference_model"]
        disk = payload["disk"]
        rows.append(
            {
                "name": name,
                "label": disk["name"],
                "note": payload["note"],
                "disk_mass_msun": disk["disk_mass_kg"] / g.M_SUN_KG,
                "scale_kpc": disk["scale_length_m"] / g.KPC,
                "r_ref_kpc": payload["reference_radius_kpc"],
                "v_baryonic_km_s": ref["baryonic_speed_km_s"],
                "v_hqiv_km_s": ref["hqiv_speed_km_s"],
                "v_observed_km_s": payload["observed_flat_km_s"],
                "inertia_factor_full": ref["inertia_factor_full"],
                "epsilon_doppler": ref["epsilon_doppler"],
                "residual_pct": (
                    100.0
                    * (ref["hqiv_speed_km_s"] - payload["observed_flat_km_s"])
                    / payload["observed_flat_km_s"]
                ),
            }
        )
    return rows


def emit_json(rows: list[dict[str, Any]]) -> str:
    return json.dumps(rows, indent=2)


def emit_markdown(rows: list[dict[str, Any]]) -> str:
    out = [
        "| Galaxy | M_disk (Msun) | R_d (kpc) | r_ref (kpc) | v_bary (km/s) "
        "| v_HQIV (km/s) | v_obs (km/s) | residual (%) |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for r in rows:
        out.append(
            "| {label} | {m:.2g} | {rd:.2f} | {rr:.0f} | {vb:.1f} | {vh:.1f} "
            "| {vo:.0f} | {res:+.1f} |".format(
                label=r["label"],
                m=r["disk_mass_msun"],
                rd=r["scale_kpc"],
                rr=r["r_ref_kpc"],
                vb=r["v_baryonic_km_s"],
                vh=r["v_hqiv_km_s"],
                vo=r["v_observed_km_s"],
                res=r["residual_pct"],
            )
        )
    return "\n".join(out)


def emit_latex(rows: list[dict[str, Any]]) -> str:
    out = [
        "\\begin{tabular}{lcccccc}",
        "\\hline",
        "Galaxy & $M_\\mathrm{disk}$ ($M_\\odot$) & $R_d$ (kpc) & "
        "$r_{\\mathrm{ref}}$ (kpc) & $v_\\mathrm{bary}$ (km/s) & "
        "$v_\\mathrm{HQIV}$ (km/s) & $v_\\mathrm{obs}$ (km/s) \\\\",
        "\\hline",
    ]
    for r in rows:
        out.append(
            "{label} & ${m:.0e}$ & {rd:.1f} & {rr:.0f} & {vb:.1f} & "
            "{vh:.1f} & {vo:.0f} \\\\".format(
                label=r["label"],
                m=r["disk_mass_msun"],
                rd=r["scale_kpc"],
                rr=r["r_ref_kpc"],
                vb=r["v_baryonic_km_s"],
                vh=r["v_hqiv_km_s"],
                vo=r["v_observed_km_s"],
            )
        )
    out += ["\\hline", "\\end{tabular}"]
    return "\n".join(out)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    fmt = parser.add_mutually_exclusive_group()
    fmt.add_argument("--markdown", action="store_true")
    fmt.add_argument("--latex", action="store_true")
    args = parser.parse_args(argv)

    rows = compute_rows()
    if args.markdown:
        print(emit_markdown(rows))
    elif args.latex:
        print(emit_latex(rows))
    else:
        print(emit_json(rows))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
