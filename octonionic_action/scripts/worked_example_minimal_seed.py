#!/usr/bin/env python3
"""
worked_example_minimal_seed.py
==============================

Reproducer for Subsection 4.2 ("Worked numerical example: minimal seed at
m_ref = 4") of

    "Octonionic Action from the HQIV-LEAN Variational Layer:
     Derivation, Holonomy Alignment, and a Tiered Uniqueness Thesis"

Inputs (all from the paper's text)
----------------------------------
* sign pattern        s = (+1, +1, -1, -1)            (cyclic, sums to 0)
* unit vector         v on (e_1, e_7) plane, theta = pi/4
* calibration shell   m_ref = 4   ->   phi = 2 * (m_ref + 1) = 10
* curvature imprint   alpha = 3 / 5
* readout increment   delta_R = 1e-2  (small, illustrative only)

Outputs
-------
* omega          = alpha * log(phi + 1) * delta_R
* A profile       (vertex potential per non-zero channel)
* sum F^2         (full antisymmetric F = A_nu - A_mu, summed)
* L_kin           = -(1/4) * (1/2) * sum F^2  =  -2 * omega^2
* Wilson bracket  -(1/2) * 4 omega^2  <=  L_kin  <=  -(1/4) * 4 omega^2
* EL covector     to confirm omega = 0 is the only stationary point
                  (the seed parameterises off-shell variational geometry)

Usage
-----
    python worked_example_minimal_seed.py            # human-readable report
    python worked_example_minimal_seed.py --json     # machine-readable

The script depends only on the Python standard library.
"""

from __future__ import annotations

import argparse
import json
import math
from typing import Any

ALPHA = 3.0 / 5.0
M_REF = 4
PHI = 2.0 * (M_REF + 1)
DELTA_R = 1.0e-2
THETA = math.pi / 4.0
SIGNS = (+1, +1, -1, -1)


def compute() -> dict[str, Any]:
    log11 = math.log(PHI + 1.0)
    omega = ALPHA * log11 * DELTA_R
    v1 = math.cos(THETA)
    v7 = math.sin(THETA)

    assert sum(SIGNS) == 0, "cyclic seed must sum to zero (Stokes compatibility)"

    A = [0.0]
    for s in SIGNS[:-1]:
        A.append(A[-1] + s * omega)
    A_close = A[0] + sum(s * omega for s in SIGNS)
    assert math.isclose(A_close, A[0], abs_tol=1e-15), "cyclic closure failed"

    sum_F_sq_per_channel = 0.0
    for mu in range(4):
        for nu in range(4):
            if mu == nu:
                continue
            F = A[nu] - A[mu]
            sum_F_sq_per_channel += F * F

    sum_F_sq = (v1 * v1 + v7 * v7) * sum_F_sq_per_channel
    L_kin = -0.25 * 0.5 * sum_F_sq

    cyclic_edge_sq = sum((s * omega) ** 2 for s in SIGNS) * (v1 * v1 + v7 * v7)
    wilson_lower = -0.5 * cyclic_edge_sq
    wilson_upper = -0.25 * cyclic_edge_sq

    sum_A_per_channel = sum(A)
    EL = [4.0 * A_nu - sum_A_per_channel for A_nu in A]

    return {
        "inputs": {
            "alpha": ALPHA,
            "m_ref": M_REF,
            "phi": PHI,
            "delta_R": DELTA_R,
            "theta_rad": THETA,
            "signs": list(SIGNS),
        },
        "log_phi_plus_1": log11,
        "omega": omega,
        "v_components": {"v1": v1, "v7": v7},
        "A_per_channel": A,
        "sum_F_squared_total": sum_F_sq,
        "sum_F_squared_per_channel": sum_F_sq_per_channel,
        "L_kin": L_kin,
        "L_kin_check_minus_2_omega_sq": -2.0 * omega * omega,
        "wilson_bound_lower": wilson_lower,
        "wilson_bound_upper": wilson_upper,
        "wilson_lower_saturated": math.isclose(L_kin, wilson_lower, rel_tol=1e-12),
        "EL_per_channel": EL,
        "stationarity_holds_only_if": "omega == 0",
    }


def emit_report(d: dict[str, Any]) -> str:
    lines = [
        "Worked numerical example: minimal seed at m_ref = 4",
        "===================================================",
        "",
        "Inputs:",
        "  alpha            = {a:.10f}".format(a=d["inputs"]["alpha"]),
        "  m_ref            = {m}".format(m=d["inputs"]["m_ref"]),
        "  phi(m_ref)       = {p:.1f}".format(p=d["inputs"]["phi"]),
        "  delta_R          = {dr:.2e}".format(dr=d["inputs"]["delta_R"]),
        "  log(phi + 1)     = {l:.14f}".format(l=d["log_phi_plus_1"]),
        "",
        "Phase increment:",
        "  omega = alpha * log(11) * delta_R",
        "        = {o:.14e}".format(o=d["omega"]),
        "",
        "Unit vector on (e_1, e_7) plane:",
        "  v1 = v7 = cos(pi/4) = {v:.6f}".format(v=d["v_components"]["v1"]),
        "",
        "A vertex potential (per non-zero channel, before v scaling):",
        "  A = " + ", ".join("{:.6e}".format(a) for a in d["A_per_channel"]),
        "",
        "Full antisymmetric F^2 sum (over all ordered pairs, both channels):",
        "  sum F^2     = {s:.6e}".format(s=d["sum_F_squared_total"]),
        "",
        "Kinetic aggregate:",
        "  L_kin       = -(1/4)(1/2) sum F^2 = {Lk:.6e}".format(Lk=d["L_kin"]),
        "  cross-check -2 omega^2            = {Lk2:.6e}".format(
            Lk2=d["L_kin_check_minus_2_omega_sq"]
        ),
        "",
        "Two-sided Wilson bound:",
        "  lower = -(1/2) * 4 omega^2 = {lo:.6e}".format(d=d, lo=d["wilson_bound_lower"]),
        "  upper = -(1/4) * 4 omega^2 = {up:.6e}".format(up=d["wilson_bound_upper"]),
        "  L_kin saturates lower bound: {sat}".format(sat=d["wilson_lower_saturated"]),
        "",
        "EL covector (sum_mu F^a_{mu nu}) per channel and vertex:",
        "  EL = " + ", ".join("{:+.6e}".format(e) for e in d["EL_per_channel"]),
        "  -> EL identity demands EL = 0 at every vertex; only omega = 0 satisfies",
        "     this, so the seed parameterises off-shell variational geometry, not",
        "     a stationary point of the action (consistent with paper text).",
    ]
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    parser.add_argument(
        "--json",
        action="store_true",
        help="emit machine-readable JSON instead of the human report",
    )
    args = parser.parse_args(argv)

    result = compute()
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(emit_report(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
