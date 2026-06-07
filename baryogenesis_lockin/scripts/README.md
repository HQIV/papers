# Baryogenesis witness scripts

Tables in `hqiv_baryogenesis_curvature_lockin.tex` (dynamic bulk + BBN dynamic-$C_2$)
are regenerated from the HQIV-LEAN repo root:

```bash
python3 scripts/hqiv_dynamic_bulk_bbn.py
python3 scripts/hqiv_integrator_lean_audit.py
python3 -m unittest scripts.test_hqiv_dynamic_c2_bbn
```

Outputs:

| File | Role |
| --- | --- |
| `data/dynamic_bulk_bbn_v2.json` | Per-shell $\Omega_b$, dynamic BBN, `bbn_dynamic_C2_ladder` |
| `data/integrator_lean_audit.json` | Paper citation row + Lean-name audit |

Lean anchors: `Hqiv.Physics.DynamicBBNBaryogenesis` (`bbnDynamicC2OpportunitySuppression`,
`bbnShellReactionOpportunity_dynamic_integrator`) and
`Hqiv.Physics.HopfShellBeltramiMassBridge` (`tuftLapseConcentrationAtXi`).

Early dynamic-baryogenesis demo (Table row “early dynamic baryogenesis”):

```bash
python3 scripts/hqiv_dynamic_bbn_baryogenesis.py
```

Output: `data/bbn_witnesses_dynamic.json`.
