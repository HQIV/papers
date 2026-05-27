# Reproducer scripts — Finite-Mode Kirchhoff paper

This directory contains the small, dependency-light scripts that
reproduce every quantitative claim in

> **Kirchhoff's Law of Thermal Emission with Built-In UV/IR Cutoffs
> from HQIV's Discrete Null Lattice.**

The bundle is intentionally self-contained so it can be uploaded as
a Zenodo supplementary file alongside the paper PDF and share the
same DOI.

## Contents

| File | Reproduces | Notes |
| --- | --- | --- |
| `birefringence_calculation.py` | Section 7 numerics paragraph (eqs. (12)–(15)) and the apparent-age falsifier | Inputs are the paper's `T_Pl`, FIRAS `T_CMB`, the wall-clock age `t_wall = 51.2 Gyr`, and `alpha = 3/5`. No fit parameters. |
| `kirchhoff_finite_mode.py` | Section 5 (Theorem 5.4 finiteness/positivity/monotonicity) and the hockey-stick cumulative-count identity (eq. (3)) | Computes the truncated blackbody energy density at FIRAS `T_CMB` for several `(m_UV, m_IR)` windows; verifies the closed-form hockey-stick sum vs the iterative sum. |
| `friedmann_recovery.py` | Section 8 (Theorem 8.1, Friedmann recovery) | Reports `t_H_HQIV = t_Pl · N(m_T)` versus the textbook radiation-era `t_H = M_Pl / T^2` at CMB today, recombination, and BBN onset. |
| `README.md` | this file | how-to-run, contents, patch-ontology disclaimer, citation block |

## Requirements

* Python 3.10 or newer.
* No third-party packages required — everything runs against the
  standard library.

## How to run

```bash
# 1. Birefringence prediction (Section 7)
python birefringence_calculation.py            # human-readable report
python birefringence_calculation.py --json     # machine-readable JSON

# 2. Finite-mode Kirchhoff law (Section 5)
python kirchhoff_finite_mode.py                # human-readable report
python kirchhoff_finite_mode.py --json         # machine-readable JSON

# 3. Friedmann recovery (Section 8)
python friedmann_recovery.py                   # human-readable report
python friedmann_recovery.py --json            # machine-readable JSON
```

All three scripts are fully deterministic and run in well under a
second on any modern laptop.

## Regenerating scripts.zip

From the paper directory (`papers/finite_mode_kirchhoff`):

```bash
cd /home/jr/Repos/HQIV_LEAN/papers/finite_mode_kirchhoff
zip -r scripts.zip scripts/ -x "*.pyc" "__pycache__/*"
```

## Provenance and versioning

* The constants used (`T_Pl`, `t_Pl`, `alpha = 3/5`, the wall-clock
  age `51.2 Gyr`, the apparent age `13.8 Gyr`, and the FIRAS
  `T_CMB = 2.7255 K`) come straight from the paper text.  No fit
  parameters are tuned.
* The PR4 reference value `0.342° ± 0.094°` is from
  Eskilt & Komatsu, *Phys. Rev. D* **106** (2022) 063503 — the same
  paper cited in the manuscript.
* The closed-form hockey-stick cumulative count is the integer
  identity proved in
  `Hqiv/Geometry/OctonionicLightCone.lean::cumLatticeSimplexCount_hockey_stick`
  (and `cumLatticeSimplexCount_closed`); the script confirms it
  numerically for several `n`.

## Patch-ontology disclaimer

The numerical outputs are calculation-approximation translations
of patch quantities (integer cycle indices, shell ladders,
normalised readouts) into degrees, kelvins, and SI seconds.
They are **not** a continuum-limit refinement of the patch theory.
The discrete patch layer is the ontology (see the patch-theory
reader contract embedded in the paper); these scripts are
interoperability tools for cross-citation only.

## Citation

If you use this bundle, please cite the paper and the HQIV-LEAN
repository:

* Steven Ettinger Jr., *Kirchhoff's Law of Thermal Emission with
  Built-In UV/IR Cutoffs from HQIV's Discrete Null Lattice*
  (2026).  \url{https://doi.org/10.5281/zenodo.20416564} (this
  script bundle is filed on the same Zenodo record).
* HQIV Lean 4 formalization (slimmed public mirror), 2026,
  <https://github.com/HQIV/hqiv-lean>.
