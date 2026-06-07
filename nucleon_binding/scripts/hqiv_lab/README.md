# HQIV Lab — chemistry and materials from inputs

Derives **allotropes**, **unit cells**, and **material response** from molecular
inputs (fragments + bonds, or GMTKN55 names). No fitted intermolecular potentials.

Requires the HQIV Lean repo layout: `scripts/` for physics mirrors.

## Install (editable)

```bash
cd /path/to/HQIV_LEAN
pip install -e .
```

## Usage

```python
from hqiv_lab import MaterialsLab

lab = MaterialsLab()
spec = lab.spec_from_name("H2O")

for cand in lab.derive_allotropes(spec):
    print(cand.label, cand.density_g_cm3, cand.score)

best = lab.preferred_allotrope(spec)
print(best.unit_cell.a_angstrom, best.unit_cell.c_angstrom)

witness = lab.readout(spec)
```

CLI:

```bash
hqiv-lab H2O
hqiv-lab CH4 --json
hqiv-lab NH3 --allotropes-only
```

## Pipeline

```
MoleculeSpec (bonds, fragments)
  → MonomerGeometry (VSEPR, motif, n_contacts)
  → PackingTemplate candidates (Ih, Ic, fcc, …)
  → PhaseUnitCell (a,b,c,Z) from contact distance
  → rank @ (T,P) via thermodynamic spine
  → material_response (n, k_th, C_p, …)
```

## Lean

`Hqiv.QuantumChemistry.PhaseAllotropeDerivation` — structural mirror.
