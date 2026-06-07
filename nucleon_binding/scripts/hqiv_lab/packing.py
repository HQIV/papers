"""Crystal packing templates — unit-cell geometry from monomer + motif."""

from __future__ import annotations

import math
from dataclasses import dataclass
from enum import Enum

from hqiv_lab.coordination import IntermolecularMotif, MonomerGeometry

from hqiv_lab._scripts import ensure_scripts_on_path

ensure_scripts_on_path()
import hqiv_lean_physics_primitives as lean  # noqa: E402


class CrystalSystem(str, Enum):
    HEXAGONAL = "hexagonal"
    CUBIC = "cubic"
    ORTHORHOMBIC = "orthorhombic"


@dataclass(frozen=True)
class PackingTemplate:
    """Named allotrope family + how to build lattice constants from monomer."""

    label: str
    crystal: CrystalSystem
    molecules_per_cell: int
    # Geometry multipliers on monomer-derived contact distance r_contact
    a_factor: float
    c_factor: float | None = None
    b_factor: float | None = None
    description: str = ""


def contact_distance_angstrom(mono: MonomerGeometry) -> float:
    """
    Characteristic centre–centre distance in the condensed network.

    H-bond networks: ~2 × r_cov · (1 + α) open channel;
    apolar: ~2.5 × r_cov from tetrahedral vertex span.
    """
    r = mono.mean_bond_length_angstrom
    if mono.motif in (
        IntermolecularMotif.TETRAHEDRAL_HBOND,
        IntermolecularMotif.PYRAMIDAL_HBOND,
        IntermolecularMotif.LINEAR_CHAIN,
    ):
        # H-bond O···O: covalent span + α opening + bent-centre lift on angle
        bend = 0.5 * (1.0 - math.cos(0.5 * mono.bond_angle_rad))
        return 2.0 * r * (1.0 + lean.ALPHA) * (1.0 + lean.C_RINDLER_SHARED * bend)
    if mono.motif == IntermolecularMotif.APOLAR_CLOSE_PACK:
        span = r * math.sqrt(8.0 / 3.0)
        return max(2.5, 2.0 * span)
    return max(2.0, 2.0 * r)


def templates_for_motif(motif: IntermolecularMotif) -> tuple[PackingTemplate, ...]:
    """Candidate packing families implied by the monomer motif."""
    if motif == IntermolecularMotif.TETRAHEDRAL_HBOND:
        return (
            PackingTemplate(
                "Ih",
                CrystalSystem.HEXAGONAL,
                4,
                a_factor=math.sqrt(8.0 / 3.0) * 1.08,
                c_factor=1.628,
                description="Hexagonal ice (tetrahedral H-bond, c/a≈1.63)",
            ),
            PackingTemplate(
                "Ic",
                CrystalSystem.CUBIC,
                2,
                a_factor=math.sqrt(2.0) * 1.02,
                description="Cubic ice (diamond-related H-bond)",
            ),
            PackingTemplate(
                "amorphous",
                CrystalSystem.CUBIC,
                1,
                a_factor=1.15,
                description="Low-density amorphous solid (disordered tetrahedral)",
            ),
        )
    if motif == IntermolecularMotif.PYRAMIDAL_HBOND:
        return (
            PackingTemplate(
                "solid",
                CrystalSystem.ORTHORHOMBIC,
                4,
                a_factor=1.05,
                b_factor=1.05,
                c_factor=1.05,
                description="Molecular orthorhombic (NH3-type)",
            ),
        )
    if motif == IntermolecularMotif.APOLAR_CLOSE_PACK:
        return (
            PackingTemplate(
                "solid_I",
                CrystalSystem.CUBIC,
                4,
                a_factor=math.sqrt(2.0) * 1.12,
                description="Molecular cubic close-packed (CH4-type)",
            ),
        )
    if motif == IntermolecularMotif.LINEAR_CHAIN:
        return (
            PackingTemplate(
                "chain",
                CrystalSystem.ORTHORHOMBIC,
                2,
                a_factor=1.0,
                c_factor=2.0,
                description="Zigzag chain solid",
            ),
        )
    if motif == IntermolecularMotif.DIATOMIC:
        return (
            PackingTemplate(
                "solid",
                CrystalSystem.ORTHORHOMBIC,
                2,
                a_factor=1.0,
                b_factor=1.0,
                c_factor=1.2,
                description="Diatomic orthorhombic",
            ),
        )
    return (
        PackingTemplate(
            "solid",
            CrystalSystem.CUBIC,
            1,
            a_factor=1.2,
            description="Generic cubic molecular cell",
        ),
    )


def lattice_constants_from_template(
    mono: MonomerGeometry,
    template: PackingTemplate,
) -> tuple[float, float, float]:
    """Return (a, b, c) in ångström from monomer contact distance."""
    r = contact_distance_angstrom(mono)
    a = r * template.a_factor
    b = r * (template.b_factor if template.b_factor is not None else template.a_factor)
    c = r * (template.c_factor if template.c_factor is not None else a)
    if template.crystal == CrystalSystem.CUBIC:
        return a, a, a
    if template.crystal == CrystalSystem.HEXAGONAL:
        return a, a, c
    return a, b, c
