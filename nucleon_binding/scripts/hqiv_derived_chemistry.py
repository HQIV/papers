#!/usr/bin/env python3
"""
Derived chemistry scalars from the nuclear + condensed spine (no AMU / ρ tables).

  • Atomic mass [amu] from ``cluster_mass_mev`` on the curvature binding ladder
  • Liquid reference density from preferred solid allotrope + motif melt opening
"""

from __future__ import annotations

import math

import hqiv_electronic_valence_shells as evs
import hqiv_lean_physics_primitives as lean
import hqiv_nuclear_curvature_binding as ncb
from fragment_aware_bonded_horizon import FragmentConfig

# CODATA 2018 — unit conversion only (not a chemistry fit).
MEV_PER_AMU = 931.49410242


def derived_atomic_mass_amu(z: int, electrons: int | None = None) -> float:
    """Mass [amu] from nuclear cluster readout at stable A(Z)."""
    e = electrons if electrons is not None else z
    a = ncb.stable_mass_number(z, e)
    m_nuc = ncb.nucleus_curvature_shell(a)
    return ncb.cluster_mass_mev(m_nuc, a) / MEV_PER_AMU


def fragment_mass_amu(frag: FragmentConfig) -> float:
    return derived_atomic_mass_amu(frag.z_nuclear, frag.electrons)


def derived_liquid_density_scale_from_solid(
    rho_solid_g_cm3: float,
    *,
    motif: str,
) -> float:
    """
    Liquid ρ reference at melt from solid allotrope density + motif opening.

    Tetrahedral H-bond nets expand on freeze (ice < water): ρ_liq ≈ ρ_s · (1+α)/φ(3)/6.
    Apolar / pyramidal solids typically relax to sparser liquid: ρ_liq ≈ ρ_s · (1−γ/4).
    """
    if motif == "tetrahedral_hbond":
        return rho_solid_g_cm3 * (1.0 + lean.ALPHA) / lean.PHASE_LIFT_3
    if motif in ("apolar_close_pack", "pyramidal_hbond"):
        return rho_solid_g_cm3 * (1.0 - lean.GAMMA / 4.0)
    if motif == "linear_chain":
        return rho_solid_g_cm3 * (1.0 + lean.GAMMA / 8.0)
    return rho_solid_g_cm3


def derived_liquid_reference_density_g_cm3(
    molecule: str,
    *,
    temperature_k: float = 273.15,
) -> float:
    """Primary solid template density → motif-scaled liquid reference (no ρ table)."""
    from hqiv_lab.coordination import infer_monomer_geometry
    from hqiv_lab.packing import templates_for_motif
    from hqiv_lab.spec import MoleculeSpec
    from hqiv_lab.unit_cell import density_g_cm3, unit_cell_for_allotrope

    spec = MoleculeSpec.from_chart_name(molecule)
    mono = infer_monomer_geometry(spec)
    templates = templates_for_motif(mono.motif)
    if not templates:
        return 1.0
    cell = unit_cell_for_allotrope(spec, templates[0], mono, temperature_k=temperature_k)
    rho_s = density_g_cm3(cell)
    return derived_liquid_density_scale_from_solid(rho_s, motif=mono.motif.value)


def chemistry_compton_triplet_from_z(z: int) -> tuple[int, int, int]:
    """Single-fragment Compton triplet for ion nodes."""
    frag = FragmentConfig("X", z, z)
    return evs.chemistry_compton_triplet((frag,))
