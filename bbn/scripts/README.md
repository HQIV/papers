# Reproducer scripts — BBN paper

These scripts live at the repository root and export the witness JSON cited in the paper.

## Contents

| Script | Reproduces | Notes |
| --- | --- | --- |
| `../../scripts/hqiv_bbn_integrator.py` | **Primary** faithful BBN readout | `data/bbn_integrator.json`; synthesis-window D/H + tail gate, coupled inventory |
| `../../scripts/hqiv_bbn_paper_tables.py` | Paper tables (decomposition, η sweep, sensitivity) | `data/bbn_paper_tables.json` |
| `../../scripts/hqiv_bbn_abundances.py` | Partition readout, epoch sweep, `data/bbn_witnesses.json` | Lock-in partition + epoch scaffold |
| `../../scripts/hqiv_bbn_epoch_network.py` | Epoch cooling network integration (400-step scaffold) | Feeds integrated $Y_p$ witnesses in Lean |
| `../../scripts/hqiv_dynamic_bulk_bbn.py` | Per-shell $\Omega_b$, legacy dynamic BBN with $B_{\mathrm{curv}}$ + dynamic $C_2$ | `data/dynamic_bulk_bbn_v2.json`; legacy row in audit |
| `../../scripts/hqiv_integrator_lean_audit.py` | Lean-name ↔ Python integrator audit for paper tables | `data/integrator_lean_audit.json` |
| `../../scripts/test_hqiv_bbn_integrator.py` | Unit tests for faithful integrator | `unittest` |
| `../../scripts/test_hqiv_dynamic_c2_bbn.py` | Unit tests for $C_2$ ladder mirrors | `unittest` |

Run from the repository root:

```bash
PYTHONPATH=scripts python3 scripts/hqiv_bbn_integrator.py
PYTHONPATH=scripts python3 scripts/hqiv_bbn_paper_tables.py
python3 scripts/hqiv_bbn_abundances.py
python3 scripts/hqiv_bbn_epoch_network.py
python3 scripts/hqiv_dynamic_bulk_bbn.py
python3 scripts/hqiv_integrator_lean_audit.py
PYTHONPATH=scripts python3 -m unittest scripts.test_hqiv_bbn_integrator
python3 -m unittest scripts.test_hqiv_dynamic_c2_bbn
```

## Inputs

- Lock-in $\eta$ from the baryogenesis witness chain (`eta_paper` in Lean; see [`hqiv-baryogenesis-paper`](https://doi.org/10.5281/zenodo.20711255)).
- Nucleon masses and binding from `derivedProtonMass`, `derivedDeltaM` (proton lock-in witness).
- Coc et al. semi-analytic fits are **not** HQIV inputs; they appear only in the comparison layer.

## Primary witness (June 2026)

At $\eta_{\mathrm{paper}} = 6.10\times 10^{-10}$ the faithful integrator exports:

| Quantity | Model | Observation anchor |
| --- | --- | --- |
| $Y_p$ | $\approx 0.244$ | $0.244$ |
| $D/H$ | $\approx 2.51\times 10^{-5}$ ($z\approx -0.5$) | $(2.53\pm 0.04)\times 10^{-5}$ |
| $^3\mathrm{He}/H$ | $\approx 1.0\times 10^{-5}$ | $\sim 10^{-5}$ |
| $^7\mathrm{Li}/H$ | $\approx 2.54\times 10^{-10}$ (HQIV pre-depletion) | Coc semi-analytic $\approx 4.65\times 10^{-10}$; Spite band $(1.6$--$4.5)\times 10^{-10}$ |

## Patch-ontology disclaimer

BBN abundances are discrete-ladder readouts at a cosmological epoch on the temperature shell map. They are not obtained as a continuum-limit refinement of the patch theory.
