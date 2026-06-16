# Baryogenesis witness scripts

Standalone reproduction bundle for `hqiv_baryogenesis_curvature_lockin.tex`.
Regenerate the bundle from the HQIV-LEAN repository root:

```bash
python3 scripts/bundle_baryogenesis_scripts.py
```

## Regenerate paper tables (repository root)

```bash
python3 scripts/hqiv_dynamic_bulk_bbn.py
python3 scripts/hqiv_bbn_integrator.py --json data/bbn_integrator.json
python3 scripts/hqiv_integrator_lean_audit.py
python3 -m unittest scripts.test_hqiv_dynamic_c2_bbn scripts.test_hqiv_bbn_integrator
```

## Run from this folder only (extracted `scripts.zip`)

```bash
cd papers/baryogenesis_lockin/scripts
PYTHONPATH=. python3 hqiv_dynamic_bulk_bbn.py
PYTHONPATH=. python3 hqiv_bbn_integrator.py --json data/bbn_integrator.json
PYTHONPATH=. python3 hqiv_integrator_lean_audit.py
python3 -m unittest test_hqiv_dynamic_c2_bbn test_hqiv_bbn_integrator
```

No Lean build is required for the Python witnesses.

## Entry scripts

| Script | Output | Paper role |
| --- | --- | --- |
| `hqiv_dynamic_bulk_bbn.py` | `data/dynamic_bulk_bbn_v2.json` | Per-shell $\Omega_b$, dynamic $\eta_{10}$, $C_2$ ladder |
| `hqiv_bbn_integrator.py` | `data/bbn_integrator.json` | Faithful BBN at $\eta_{\mathrm{paper}}$ (primary abundance row) |
| `hqiv_integrator_lean_audit.py` | `data/integrator_lean_audit.json` | Paper citation row + Lean-name audit |
| `hqiv_dynamic_bbn_baryogenesis.py` | `data/bbn_witnesses_dynamic.json` | Early dynamic-baryogenesis demo |
| `hqiv_bbn_paper_tables.py` | `data/bbn_paper_tables.json` | LaTeX-ready BBN table fragments |

## Mirrored data

| File | Role |
| --- | --- |
| `data/dynamic_bulk_bbn_v2.json` | Bulk integrator + BBN scaffold |
| `data/bbn_integrator.json` | Faithful stoichiometric integrator payload |
| `data/integrator_lean_audit.json` | Recommended citation row for Tables 1--2 |
| `data/bbn_paper_tables.json` | Companion BBN table export |
| `data/bbn_witnesses_dynamic.json` | Legacy dynamic demo |
| `data/hqiv_witnesses.json` | Scale witness / derived proton mass |

## Lean anchors

- `Hqiv.Physics.BaryogenesisCore`, `BaryogenesisEtaPaper`, `BaryogenesisWitness`
- `Hqiv.Physics.DynamicBBNBaryogenesis` (`bbnDynamicC2OpportunitySuppression`,
  `bbnShellReactionOpportunity_dynamic_integrator`)
- `Hqiv.Physics.HopfShellBeltramiMassBridge` (`tuftLapseConcentrationAtXi`)
- `Hqiv.Physics.BBNStoichiometricIntegrator` (faithful integrator mirror)

Verify checksums: `sha256sum -c MANIFEST.sha256` (from this directory).
