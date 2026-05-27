# Reproducer scripts — Octonionic Action paper

This directory contains the small, dependency-light scripts that reproduce
the explicit numerical results in

> **Octonionic Action from the HQIV-LEAN Variational Layer:
> Derivation, Holonomy Alignment, and a Tiered Uniqueness Thesis.**

The bundle is intentionally self-contained so it can be uploaded as a Zenodo
supplementary file alongside the paper PDF and share the same DOI.

## Contents

| File | Reproduces | Notes |
| --- | --- | --- |
| `hqiv_galaxy_rotation.py` | underlying HQIV galaxy-rotation calculator (snapshot) | Identical to `HQIV_LEAN/scripts/hqiv_galaxy_rotation.py` and the upstream module in the [HQIV-Orbital](https://github.com/HQIV/HQIV_Orbital) companion harness; same `f(a,phi)=a/(a+phi/6)` and angular Rindler denominator used by the flyby paper. |
| `sparc_firstpass_table.py` | Table 2 (SPARC-style first-pass sanity check) | Six exponential-disk presets, no fits, no halo, default angular Rindler denominator. |
| `worked_example_minimal_seed.py` | Subsection 4.2 (worked numerical example at `m_ref = 4`) | Pure standard-library Python; verifies `omega`, `A` profile, `L_kin = -2 omega^2`, two-sided Wilson bound, and that the EL identity forces `omega = 0` (so the seed parameterises off-shell variational geometry, not a stationary point of the action). |

## Requirements

* Python 3.10 or newer.
* No third-party packages required — everything runs against the standard
  library.

## How to run

```bash
# 1. SPARC first-pass table (Table 2)
python sparc_firstpass_table.py            # JSON to stdout (default)
python sparc_firstpass_table.py --markdown # Markdown table
python sparc_firstpass_table.py --latex    # LaTeX tabular fragment

# 2. Worked numerical example (Subsection 4.2)
python worked_example_minimal_seed.py            # human-readable report
python worked_example_minimal_seed.py --json     # machine-readable JSON
```

Both scripts are fully deterministic and depend only on the snapshot of
`hqiv_galaxy_rotation.py` shipped here. They take well under one second on
any modern laptop.

## Provenance and versioning

* The galaxy-rotation calculator snapshot is taken from the HQIV-LEAN tree
  at the same commit that produced the paper PDF. The upstream module is
  the one used by the orbital-flyby calculator and the
  [HQIV-Orbital](https://github.com/HQIV/HQIV_Orbital) companion harness;
  it is **not** modified here.
* No fit parameters are tuned; the only inputs to the SPARC presets are
  the literature stellar mass and disk scale length recorded inside
  `hqiv_galaxy_rotation.py` (`GALAXY_PRESETS` dict).
* `worked_example_minimal_seed.py` uses the natural logarithm with the
  explicit decimal value `log 11 = 2.39789527279837...` (Python `math.log`),
  matching the disclosure in the worked-example paragraph.

## Patch-ontology disclaimer

The numerical outputs are calculation-approximation translations of patch
quantities into kilometre-per-second / dimensionless circular-speed
coordinates. They are **not** a continuum-limit refinement of the patch
theory. The discrete patch layer is the ontology (see the patch-theory
reader contract in the paper); these scripts are interoperability tools
for cross-citation only.

## Citation

If you use this bundle, please cite the paper and the HQIV-LEAN repository:

* Steven Ettinger Jr., *Octonionic Action from the HQIV-LEAN Variational
  Layer: Derivation, Holonomy Alignment, and a Tiered Uniqueness Thesis*
  (Preprint v3, 2026). DOI to be minted on Zenodo deposit; this script
  bundle shares that DOI.
* HQIV Lean 4 formalization (slimmed public mirror), 2026,
  <https://github.com/HQIV/hqiv-lean>.
