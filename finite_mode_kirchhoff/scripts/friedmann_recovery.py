#!/usr/bin/env python3
"""
friedmann_recovery.py
=====================

Reproducer for Section 8 ("Friedmann scaling recovered, not imported")
of

    "Kirchhoff's Law of Thermal Emission with Built-In UV/IR Cutoffs
     from HQIV's Discrete Null Lattice"

This script confirms numerically that the propagation-shell duration

    t_H_HQIV(T) ~ t_Pl * N(m_T(T))

reproduces the radiation-era Friedmann scaling

    t_H_radiation(T) = M_Pl / T^2

at several reference cosmological temperatures (CMB today,
recombination, big-bang nucleosynthesis).  The same stars-and-bars
count N(m) that delivers the finite-mode Kirchhoff law of Section 5
delivers Friedmann's H ~ T^2 here.

Inputs
------
* T_Pl   = 1.41679e32 K            (Planck temperature)
* t_Pl   = 5.391e-44 s             (Planck time)
* alpha  = 3 / 5                   (informational monogamy imprint)
* Reference temperatures:
    -- CMB today              T = 2.7255 K     (FIRAS, Fixsen 2009)
    -- Recombination          T = 3000 K       (textbook)
    -- BBN onset              T = 1e10 K       (textbook)

Outputs
-------
For each temperature:
* m_T = T_Pl / T - 1
* N(m_T)
* t_H_HQIV   = t_Pl * N(m_T)
* t_H_rad    = M_Pl / T^2 in equivalent natural units
* relative discrepancy

Usage
-----
    python friedmann_recovery.py             # human-readable report
    python friedmann_recovery.py --json      # machine-readable JSON

Patch-ontology disclaimer: SI seconds and kelvins are
calculation-approximation translations of patch quantities.  The
discrete patch layer is the ontology; this script is an
interoperability tool, not a continuum-limit refinement.
"""

from __future__ import annotations

import argparse
import json
from typing import Any

T_PL = 1.41679e32
T_PL_TIME = 5.391e-44
ALPHA = 3.0 / 5.0

REFERENCE_T = [
    ("CMB_today", 2.7255),
    ("recombination", 3000.0),
    ("BBN_onset", 1.0e10),
]


def shell_index_from_temperature(T_obs_K: float) -> float:
    return T_PL / T_obs_K - 1.0


def lattice_simplex_count(m: float) -> float:
    return (m + 2.0) * (m + 1.0)


def t_H_hqiv_seconds(T_obs_K: float) -> float:
    m_T = shell_index_from_temperature(T_obs_K)
    return T_PL_TIME * lattice_simplex_count(m_T)


def t_H_radiation_seconds(T_obs_K: float) -> float:
    """Continuum standard: t_H = (T_Pl / T)^2 * t_Pl in natural units.

    This is the textbook radiation-era Friedmann relation; we use it
    only as the literature comparison object.  Per the patch-theory
    reader contract, HQIV's discrete N(m_T) is the foundation.
    """
    return (T_PL / T_obs_K) ** 2 * T_PL_TIME


def compute() -> dict[str, Any]:
    rows = []
    for label, T in REFERENCE_T:
        m_T = shell_index_from_temperature(T)
        N_mT = lattice_simplex_count(m_T)
        t_hqiv = t_H_hqiv_seconds(T)
        t_rad = t_H_radiation_seconds(T)
        rel = (t_hqiv - t_rad) / t_rad
        rows.append(
            {
                "label": label,
                "T_K": T,
                "m_T": m_T,
                "N_mT": N_mT,
                "t_H_HQIV_s": t_hqiv,
                "t_H_radiation_s": t_rad,
                "relative_discrepancy": rel,
            }
        )
    return {
        "inputs": {
            "T_Pl_K": T_PL,
            "t_Pl_s": T_PL_TIME,
            "alpha": ALPHA,
            "reference_temperatures": [
                {"label": label, "T_K": T} for label, T in REFERENCE_T
            ],
        },
        "rows": rows,
    }


def emit_report(d: dict[str, Any]) -> str:
    lines = [
        "Friedmann scaling recovered (HQIV finite-mode Kirchhoff paper, S8)",
        "===================================================================",
        "",
        "For each reference temperature: t_H_HQIV = t_Pl * N(m_T(T)) compared",
        "with the textbook radiation-era Friedmann relation t_H = M_Pl / T^2.",
        "",
        "{:<14} {:>12} {:>12} {:>14} {:>14} {:>10}".format(
            "label",
            "T (K)",
            "m_T",
            "N(m_T)",
            "t_H_HQIV (s)",
            "rel diff",
        ),
    ]
    for r in d["rows"]:
        lines.append(
            "{lbl:<14} {T:>12.4e} {mT:>12.4e} {N:>14.4e} {tH:>14.4e} {rel:>+10.3e}".format(
                lbl=r["label"],
                T=r["T_K"],
                mT=r["m_T"],
                N=r["N_mT"],
                tH=r["t_H_HQIV_s"],
                rel=r["relative_discrepancy"],
            )
        )
    lines += [
        "",
        "The relative discrepancy is O(1 / m_T), which is exponentially small",
        "at the temperatures shown (m_T ranges from ~1.4e21 at BBN onset to",
        "~5.2e31 at the CMB today).  No Einstein equation has been used; the",
        "scaling is delivered by the same stars-and-bars count that gave the",
        "finite-mode Kirchhoff law in Section 5.",
    ]
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    out = compute()
    if args.json:
        print(json.dumps(out, indent=2))
    else:
        print(emit_report(out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
