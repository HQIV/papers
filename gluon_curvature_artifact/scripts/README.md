# Reproducer scripts — gluon curvature artifact

Minimal import closure for `papers/gluon_curvature_artifact/` (Zenodo bundle).
Zenodo record: [`10.5281/zenodo.20724572`](https://doi.org/10.5281/zenodo.20724572).
Comparison JSON lives in `data/` beside these scripts (never HQIV inputs).

## Entry scripts

| Script | Role |
| --- | --- |
| `hqiv_strong_sector_collider_discharge.py` | Leading-order collider discharge (9 cases) |
| `hqiv_hep_collider_refinements.py` | HEP refinements: shower MC, thrust bins, ggH pT, QGP, PDF x |
| `test_hqiv_strong_sector_collider_discharge.py` | Unit tests for discharge witness |
| `test_hqiv_hep_collider_refinements.py` | Unit tests for refinement witness |

## Quick start (standalone, from extracted `scripts/`)

```bash
cd scripts
PYTHONPATH=. python3 hqiv_strong_sector_collider_discharge.py --strict
PYTHONPATH=. python3 hqiv_hep_collider_refinements.py --strict
python3 test_hqiv_strong_sector_collider_discharge.py
python3 test_hqiv_hep_collider_refinements.py
```

## Quick start (HQIV-LEAN repository root)

```bash
PYTHONPATH=scripts python3 scripts/hqiv_strong_sector_collider_discharge.py --strict
PYTHONPATH=scripts python3 scripts/hqiv_hep_collider_refinements.py --strict
```

Lean (full checkout only): `lake build paper_gluon_curvature`

Dependencies: Python 3.10+ stdlib only.
