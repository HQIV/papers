# HEP decay readout (Tier-2 extension / decay-calculator layer)

**Single source:** `hqiv_hep_decay_readout_from_multichannel.tex`

**Reproducibility:** [`REPRODUCIBILITY.md`](REPRODUCIBILITY.md) — one-command numerics + fast smoke test.

**Title:** *Heavy-Flavour Branching Ratios Derived from Discrete Three-Ledger Rules on the HQIV Null-Lattice Carrier*

**Bib key:** `hqiv-hep-decay-paper` in `papers/references.bib`

**Queue position:** Tier-2 #10 (successor to [gluon curvature closure](https://doi.org/10.5281/zenodo.20724572)); extends nucleon-binding three-ledger $\beta$ tipping to open and hidden heavy flavour.

**Fresh vs.\ upstream gluon note:** EM contact $37/10$ ($39/10$ legacy certificate), multichannel readout, CKM ledger normalization, collider environment dressing, unified spine discharge product $W=\prod_k g_k^{e_k}$, factorization uniqueness (Lean `SpineDischargeUniqueness.lean`), heavy-flavour spine reconciliation (`SpineDischargeWeight.lean`).

## Build

```bash
cd papers/hep_decay_readout
latexmk -pdf hqiv_hep_decay_readout_from_multichannel.tex
```

Output: `hqiv_hep_decay_readout_from_multichannel.pdf`.

## Reproducers

**Canonical data layout:** the pipeline writes to **repo-root** `data/` and `papers/hep_decay_readout/generated/`. The bundled copy under `papers/hep_decay_readout/data/` mirrors the same schema for Zenodo/scripts.zip.

**Unified pipeline** (recommended — collider input → discharge tables → paper artifacts):

```bash
# From repo root (recommended)
export PYTHONPATH=papers/hep_decay_readout/scripts
python3 papers/hep_decay_readout/scripts/hqiv_hep_readout_pipeline.py paper --strict

# From paper directory
cd papers/hep_decay_readout
PYTHONPATH=scripts python3 scripts/hqiv_hep_readout_pipeline.py paper --strict

# General: facility + environment + parent branching snapshot
PYTHONPATH=scripts python3 scripts/hqiv_hep_readout_pipeline.py run \
  --facility LHC_pp_13TeV --env collider_hadron --parent B_plus --parent phi

# Bottle / beam-dump mix on a custom beam
PYTHONPATH=scripts python3 scripts/hqiv_hep_readout_pipeline.py run \
  --beam p --beam-energy 24 --beam-mix 'p:0.85,pi+:12@0.15' --env ucn_bottle --chain

PYTHONPATH=scripts python3 scripts/hqiv_hep_readout_pipeline.py list facilities
PYTHONPATH=scripts python3 scripts/hqiv_hep_readout_pipeline.py list envs
```

Bundled archive: `papers/hep_decay_readout/scripts.zip`
(refresh from repo root: `python3 scripts/bundle_hep_decay_scripts.py`).

Individual entry points (also invoked by `paper` subcommand):

```bash
PYTHONPATH=scripts python3 scripts/hqiv_hep_decay_benchmark.py --strict
PYTHONPATH=scripts python3 scripts/hqiv_strong_sector_collider_discharge.py --strict
PYTHONPATH=scripts python3 scripts/hqiv_hep_collider_refinements.py --strict
PYTHONPATH=scripts python3 scripts/hqiv_spine_discharge_export.py
PYTHONPATH=scripts python3 scripts/export_excited_mass_table.py
PYTHONPATH=scripts python3 scripts/export_hep_branching_table.py
```

### Test status

**Fast smoke test** (< 30 s, frozen JSON contract):

```bash
cd papers/hep_decay_readout/scripts
PYTHONPATH=. python3 -m unittest test_hqiv_hep_smoke -q
```

**Full suite** (strict `paper --strict` runs this internally):

```bash
cd papers/hep_decay_readout/scripts
PYTHONPATH=. python3 -m unittest discover -s . -p 'test_hqiv_hep*.py' -q
```

At last refresh the structural benchmark reported **81 pass / 0 fail** in `data/hep_decay_benchmark.json`; check `data/hep_readout_pipeline_manifest.json` for the unittest step status.

## Lean

**Decay spine** (`lake build HQIVPhysics`):

- `Hqiv/Physics/HepDecayReadout.lean` (decay ledger, gauge readout, $f_{\mathrm{EM}}=37/10$)
- `Hqiv/Physics/HepDecayChannelRouting.lean` (routing predicates, gauge-curvature row lemmas)
- `Hqiv/Physics/SpineDischargeWeight.lean` (unified product law, heavy-flavour reconciliation)
- `Hqiv/Physics/SpineDischargeUniqueness.lean` (factorization uniqueness)
- `Hqiv/Physics/ElectroweakMassObservation.lean` (facility dressing chart)
- `Hqiv/Physics/AcceleratorOutsideDressing.lean` (spectroscopy facility dressing)
- `Hqiv/Physics/ExcitedMassPanelReadout.lean` / `ExcitedMassComparisonHonesty.lean` (excited panel + $\sigma$ honesty)
- `Hqiv/Physics/HepAnomalyDischarge.lean` (nine-class discharge capstone)

**Collider bundle** (`lake build paper_gluon_curvature`):

- `Hqiv/Physics/StrongSectorColliderDischarge.lean` (leading collider discharge)
- `Hqiv/Physics/HepColliderRefinements.lean` (MC shower, differential slots)

```bash
# Aggregate decay spine
lake build HQIVPhysics

# Collider discharge (upstream gluon note)
lake build paper_gluon_curvature

# Optional direct checks outside default import cones
lake env lean Hqiv/Physics/ShellIndexRiemannZetaBridge.lean
lake env lean Hqiv/Physics/StandardModelLagrangianFromDiscreteAction.lean
```

## Upstream (published Tier-2 chain)

This note consumes the full published spine through gluon closure; comparison data never enter the prediction path.

| Record | Bib key | DOI | Role in this note |
| --- | --- | --- | --- |
| Nielsen TUFT | `NielsenTUFT2026` | [PhilArchive NIETTU](https://philarchive.org/rec/NIETTU) | Nested Hopf shells, Beltrami contact spectrum, intrinsic mass scales |
| TUFT+SM synthesis | `hqiv-tuft-sm-lagrangian-paper` | [`10.5281/zenodo.20601215`](https://doi.org/10.5281/zenodo.20601215) | Quark meta-resonance mass panel; chiral factors; electroweak slots |
| Baryogenesis lock-in | `hqiv-baryogenesis-paper` | [`10.5281/zenodo.20711255`](https://doi.org/10.5281/zenodo.20711255) | Lock-in shell / $\eta$ normalisation (no new decay inputs) |
| Nucleon binding | `hqiv-nucleon-binding-paper` | [`10.5281/zenodo.20711453`](https://doi.org/10.5281/zenodo.20711453) | Three-ledger prototype; $G_F$; $\beta$ tipping |
| BBN abundances | `hqiv-bbn-paper` | [`10.5281/zenodo.20723606`](https://doi.org/10.5281/zenodo.20723606) | Network-from-weights multichannel discipline |
| Gluon curvature closure | `hqiv-gluon-curvature-note` | [`10.5281/zenodo.20724572`](https://doi.org/10.5281/zenodo.20724572) | Strong-sector trapping; OZI overlap; collider witnesses |

Tier 0–1 spine (`ettinger2026hqiv`, `hqiv-lightcone-paper`, `hqiv-so8-paper`, `hqiv-3d-growth-paper`, `hqiv-oct-action-paper`, `hqiv-kirchhoff-paper`, `hqiv-thermo-arrow-paper`) is cited in the paper introduction.

## Pre-publication checklist

- [x] Scope and upstream inputs section (`§\ref{sec:scope}`)
- [x] `referenceM=4` programme pin (`papers/include/referenceM_programme_pin.tex`)
- [x] Neutral-spectator contact wired for $B^0\to D^0\pi^0$ ($\approx 15.6\%$ vs.\ $16\%$)
- [x] Rebuild PDF after upstream citation pass
- [x] Refresh `scripts.zip`; run benchmark `--strict`
- [x] Structural pass count aligned to artifact (`81 pass / 0 fail`)
- [ ] Deposit on Zenodo; update `references.bib` with version DOI
