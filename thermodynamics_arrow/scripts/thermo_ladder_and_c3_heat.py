#!/usr/bin/env python3
"""Reproduce ladder thermodynamics and C3 heat dissipation signs from the thermodynamics paper.

Standard library only. Deterministic.
"""

from __future__ import annotations

import argparse
import json
import math


def T_ladder(m: int) -> float:
    return 1.0 / (m + 1)


def laplacian_cycle3(u: list[float]) -> list[float]:
    n = 3
    return [u[(i + 1) % n] + u[(i - 1) % n] - 2.0 * u[i] for i in range(n)]


def entropy_production_proxy(u: list[float]) -> float:
    lap = laplacian_cycle3(u)
    return -sum(ui * li for ui, li in zip(u, lap))


def euler_heat_step(u: list[float], nu: float, dt: float) -> list[float]:
    lap = laplacian_cycle3(u)
    return [ui + dt * nu * li for ui, li in zip(u, lap)]


def energy(u: list[float]) -> float:
    return sum(ui * ui for ui in u)


# --- Finite blackbody comparison (for paper table) ---

def new_modes(m: int) -> float:
    """Multiplicity of new modes at shell m (from OctonionicLightCone)."""
    if m == 0:
        return 8.0
    else:
        return 8.0 * (m + 1)


def shell_omega(m: int) -> float:
    """Dimensionless frequency tag at shell m (natural Planck units)."""
    return 1.0 / (m + 1)


def n_bose(omega: float, T: float) -> float:
    """Bose--Einstein occupation (Planck mean energy / omega)."""
    if omega <= 0 or T <= 0:
        return 0.0
    x = omega / T
    # guard against overflow / underflow
    if x > 700:
        return 0.0
    return 1.0 / (math.exp(x) - 1.0)


def finite_blackbody_U(T: float, m_UV: int, m_IR: int) -> float:
    """Truncated energy density U(T; m_UV, m_IR) in natural units."""
    total = 0.0
    for m in range(m_UV, m_IR + 1):
        Nm = new_modes(m)
        om = shell_omega(m)
        total += Nm * om * n_bose(om, T)
    return total


def finite_blackbody_entropy_density(T: float, m_UV: int, m_IR: int) -> float:
    """s = (4/3) U / T for the truncated sum (massless radiation)."""
    U = finite_blackbody_U(T, m_UV, m_IR)
    return (4.0 / 3.0) * U / T if T > 0 else 0.0


def blackbody_comparison_table(T: float = 0.05, large_IR: int = 5000) -> dict:
    """Return dict with ratios and values for selected cutoffs vs large-IR proxy."""
    cutoffs = [10, 50, 100, 200, 500, 1000, 2000, large_IR]
    U_large = finite_blackbody_U(T, 0, large_IR)
    s_large = finite_blackbody_entropy_density(T, 0, large_IR)
    rows = []
    for M in cutoffs:
        U = finite_blackbody_U(T, 0, M)
        s = finite_blackbody_entropy_density(T, 0, M)
        ratio_U = U / U_large if U_large > 0 else 0.0
        ratio_s = s / s_large if s_large > 0 else 0.0
        rows.append({
            "m_IR": M,
            "U": round(U, 8),
            "s": round(s, 8),
            "U_ratio_to_large": round(ratio_U, 6),
            "s_ratio_to_large": round(ratio_s, 6),
        })
    return {
        "T": T,
        "large_IR_proxy": large_IR,
        "U_large": round(U_large, 8),
        "s_large": round(s_large, 8),
        "rows": rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="emit JSON")
    args = parser.parse_args()

    ladder = {m: T_ladder(m) for m in range(8)}
    u = [1.0, -0.5, 0.25]
    sigma = entropy_production_proxy(u)
    nu, dt = 0.4, 0.5
    e0, e1 = energy(u), energy(euler_heat_step(u, nu, dt))
    cfl_ok = 3 * nu * dt <= 2

    bb = blackbody_comparison_table(T=0.05, large_IR=5000)

    out = {
        "ladder_T_m": ladder,
        "third_law_m_for_eps_1e-3": next(m for m in range(10000) if T_ladder(m) < 1e-3),
        "C3_u": u,
        "entropy_production_proxy": sigma,
        "entropy_production_nonneg": sigma >= -1e-15,
        "euler_nu": nu,
        "euler_dt": dt,
        "cfl_3_nu_dt_le_2": cfl_ok,
        "energy_before": e0,
        "energy_after_euler": e1,
        "euler_energy_nonincreasing": e1 <= e0 + 1e-15,
        "blackbody_comparison": bb,
    }

    if args.json:
        print(json.dumps(out, indent=2))
        return

    print("HQIV thermodynamics ladder + C3 heat checks")
    print("=" * 48)
    print("Shell ladder T(m)=1/(m+1):")
    for m, t in ladder.items():
        print(f"  m={m}: T={t:.6f}")
    print(f"  m with T<1e-3: {out['third_law_m_for_eps_1e-3']}")
    print()
    print(f"C3 state u={u}")
    print(f"  entropy production proxy Sigma(u) = {sigma:.6f}  (>=0: {out['entropy_production_nonneg']})")
    print(f"  Euler step nu={nu}, dt={dt}, CFL ok: {cfl_ok}")
    print(f"  ||u||^2 before {e0:.6f}, after {e1:.6f}  (non-increasing: {out['euler_energy_nonincreasing']})")

    # Blackbody finite-vs-large-cutoff comparison (paper table data)
    bb = out["blackbody_comparison"]
    print()
    print("Finite blackbody (T=0.05 natural units; UV=0)")
    print("  m_IR     U            s            U/U_large    s/s_large")
    print("  " + "-" * 58)
    for r in bb["rows"]:
        print(f"  {r['m_IR']:>6}  {r['U']:12.8f} {r['s']:12.8f} "
              f"{r['U_ratio_to_large']:>10.6f} {r['s_ratio_to_large']:>10.6f}")
    print(f"  (large-IR proxy = {bb['large_IR_proxy']}; U_large ≈ {bb['U_large']:.8f})")
    print("  Note: as m_IR grows (many shells occupied) the ratios approach the")
    print("  continuum Stefan--Boltzmann limit (T^4 scaling recovered in the Kirchhoff companion).")


if __name__ == "__main__":
    main()
