# Reproducer scripts — BBN paper

These scripts live at the repository root and export the witness JSON cited in the paper.

## Contents

| Script | Reproduces | Notes |
| --- | --- | --- |
| `../../scripts/hqiv_bbn_abundances.py` | Partition readout, epoch sweep, `data/bbn_witnesses.json` | Default run writes witness bundle |
| `../../scripts/hqiv_bbn_epoch_network.py` | Epoch cooling network integration (400-step scaffold) | Feeds integrated $Y_p$ witnesses in Lean |
| `../../scripts/hqiv_dynamic_bulk_bbn.py` | Per-shell $\Omega_b$, dynamic BBN with $B_{\mathrm{curv}}$ + dynamic $C_2$ | `data/dynamic_bulk_bbn_v2.json` |
| `../../scripts/hqiv_integrator_lean_audit.py` | Lean-name ↔ Python integrator audit for paper tables | `data/integrator_lean_audit.json` |
| `../../scripts/test_hqiv_dynamic_c2_bbn.py` | Unit tests for $C_2$ ladder mirrors | `unittest` |

Run from the repository root:

```bash
python3 scripts/hqiv_bbn_abundances.py
python3 scripts/hqiv_bbn_epoch_network.py
python3 scripts/hqiv_dynamic_bulk_bbn.py
python3 scripts/hqiv_integrator_lean_audit.py
python3 -m unittest scripts.test_hqiv_dynamic_c2_bbn
```

## Inputs

- Lock-in $\eta$ from the baryogenesis witness chain (`eta_paper` in Lean; see baryogenesis paper).
- Nucleon masses and binding from `derivedProtonMass`, `derivedDeltaM` (proton lock-in witness).
- Coc et al. semi-analytic fits are **not** HQIV inputs; they appear only in the comparison layer.

## Patch-ontology disclaimer

BBN abundances are discrete-ladder readouts at a cosmological epoch on the temperature shell map. They are not obtained as a continuum-limit refinement of the patch theory.
