#!/usr/bin/env python3
"""
birefringence_calculation.py
============================

Reproducer for Section 7 ("Quantitative test: cosmic birefringence
beta = 0.379 deg") of

    "Kirchhoff's Law of Thermal Emission with Built-In UV/IR Cutoffs
     from HQIV's Discrete Null Lattice"

This script reproduces every line of the paper's "Numerics" paragraph
(equations (12)-(15) and the falsifier paragraph that follows) using
only the standard library.

Inputs (all from the paper)
---------------------------
* T_Pl       = 1.41679e32 K            (Planck temperature)
* T_CMB      = 2.7255 K                (FIRAS, Fixsen 2009)
* t_Pl       = 5.391e-44 s             (Planck time)
* t_wall     = 51.2 Gyr                (HQIV wall-clock age, HQIV-modified
                                        CLASS background output)
* t_apparent = 13.8 Gyr                (HQIV apparent-age fallback used
                                        as the falsifier)
* alpha      = 3 / 5                   (informational monogamy imprint)

Outputs
-------
* m_T            = T_Pl / T_CMB - 1
* N(m_T)         = (m_T + 2)(m_T + 1)
* t_wall / t_Pl
* m_prop         = (t_wall / t_Pl) / N(m_T)
* beta_HQIV in radians and degrees
* residual to PR4 in sigma units (Eskilt-Komatsu 2022)
* falsifier: same chain with t_apparent, residual at -2.55 sigma

Usage
-----
    python birefringence_calculation.py             # human-readable report
    python birefringence_calculation.py --json      # machine-readable JSON

Patch-ontology disclaimer: degrees, kelvin, and SI units are
calculation-approximation translations of patch quantities
(integer cycle indices, shell ladders, normalised readouts).  The
discrete patch layer is the ontology; this script is an
interoperability tool, not a continuum-limit refinement.
"""

from __future__ import annotations

import argparse
import json
import math
from typing import Any

T_PL = 1.41679e32
T_CMB = 2.7255
T_PL_TIME = 5.391e-44
GYR_TO_S = 3.155693e16
T_WALL_GYR = 51.2
T_APPARENT_GYR = 13.8
ALPHA = 3.0 / 5.0

BETA_PR4_DEG = 0.342
BETA_PR4_ERR_DEG = 0.094


def shell_index_from_temperature(T_obs_K: float) -> float:
    return T_PL / T_obs_K - 1.0


def lattice_simplex_count(m: float) -> float:
    return (m + 2.0) * (m + 1.0)


def m_prop(t_age_gyr: float, m_T_value: float) -> float:
    t_age_s = t_age_gyr * GYR_TO_S
    return (t_age_s / T_PL_TIME) / lattice_simplex_count(m_T_value)


def beta_near_pole(m_prop_value: float) -> float:
    return ALPHA * math.log1p(m_prop_value)


def chain_for_age(label: str, t_age_gyr: float, m_T_value: float) -> dict[str, Any]:
    mp = m_prop(t_age_gyr, m_T_value)
    beta_rad = beta_near_pole(mp)
    beta_deg = math.degrees(beta_rad)
    residual_sigma = (beta_deg - BETA_PR4_DEG) / BETA_PR4_ERR_DEG
    return {
        "label": label,
        "t_age_Gyr": t_age_gyr,
        "t_age_over_t_Pl": t_age_gyr * GYR_TO_S / T_PL_TIME,
        "m_prop": mp,
        "beta_rad": beta_rad,
        "beta_deg": beta_deg,
        "residual_sigma_vs_PR4": residual_sigma,
    }


def compute() -> dict[str, Any]:
    m_T_value = shell_index_from_temperature(T_CMB)
    N_mT = lattice_simplex_count(m_T_value)

    wall = chain_for_age("wall_clock", T_WALL_GYR, m_T_value)
    apparent = chain_for_age("apparent", T_APPARENT_GYR, m_T_value)

    return {
        "inputs": {
            "T_Pl_K": T_PL,
            "T_CMB_K": T_CMB,
            "t_Pl_s": T_PL_TIME,
            "alpha": ALPHA,
            "t_wall_Gyr": T_WALL_GYR,
            "t_apparent_Gyr": T_APPARENT_GYR,
            "PR4_beta_deg": BETA_PR4_DEG,
            "PR4_beta_err_deg": BETA_PR4_ERR_DEG,
        },
        "shared": {
            "m_T": m_T_value,
            "N_mT": N_mT,
        },
        "wall_clock": wall,
        "apparent_age_falsifier": apparent,
    }


def emit_report(d: dict[str, Any]) -> str:
    s = d["shared"]
    w = d["wall_clock"]
    a = d["apparent_age_falsifier"]
    return "\n".join(
        [
            "Cosmic birefringence prediction (HQIV finite-mode Kirchhoff paper, S7)",
            "=======================================================================",
            "",
            "Shared chain",
            "------------",
            "  m_T               = T_Pl / T_CMB - 1   = {:.3e}".format(s["m_T"]),
            "  N(m_T)            = (m_T+2)(m_T+1)     = {:.3e}".format(s["N_mT"]),
            "",
            "Wall-clock prediction (paper's prediction)",
            "------------------------------------------",
            "  t_wall / t_Pl     = {:.3e}".format(w["t_age_over_t_Pl"]),
            "  m_prop            = (t_wall/t_Pl) / N(m_T) = {:.3e}".format(w["m_prop"]),
            "  beta_HQIV (rad)   = {:.4e}".format(w["beta_rad"]),
            "  beta_HQIV (deg)   = {:.4f}".format(w["beta_deg"]),
            "  residual vs PR4   = {:+.2f} sigma".format(w["residual_sigma_vs_PR4"]),
            "",
            "Falsifier: substitute apparent age",
            "-----------------------------------",
            "  m_prop (apparent) = {:.3e}".format(a["m_prop"]),
            "  beta (apparent)   = {:.4f} deg".format(a["beta_deg"]),
            "  residual vs PR4   = {:+.2f} sigma".format(a["residual_sigma_vs_PR4"]),
            "",
            "Verdict",
            "-------",
            "  Wall-clock chain reproduces the paper's boxed value 0.3792 deg",
            "  and lies within the PR4 1-sigma envelope.  The apparent-age",
            "  substitution fails by more than 2 sigma, providing the internal",
            "  discriminator described in S7 of the paper.",
        ]
    )


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
