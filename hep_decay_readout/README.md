# HEP decay readout (Tier-2 extension / decay-calculator layer)

**Single source:** `hqiv_hep_decay_readout_from_multichannel.tex`

**Title:** *Heavy-Flavour Decay Chains from HQIV Three-Ledger Readout: Discrete Multichannel Rules, Quarkonium Contact, and Branching without Partial-Width Inputs*

**Bib key:** `hqiv-hep-decay-paper` in `papers/references.bib`

## Build

```bash
cd papers/hep_decay_readout
latexmk -pdf hqiv_hep_decay_readout_from_multichannel.tex
```

Output: `hqiv_hep_decay_readout_from_multichannel.pdf`.

## Reproducers

See `scripts/README.md`. Entry scripts live at the repository root under `scripts/hqiv_hep_*.py` and `scripts/hqiv_decay_calculator.py`.

Strict benchmark discharge (87/87 at last refresh):

```bash
python3 scripts/hqiv_hep_decay_benchmark.py --strict
```

## Lean

Machine-checked module: `Hqiv/Physics/HepDecayReadout.lean` (imported by `HQIVPhysics.lean`).

```bash
lake env lean Hqiv/Physics/HepDecayReadout.lean
```

## Upstream

Consumes the published TUFT+SM synthesis (`hqiv-tuft-sm-lagrangian-paper`, DOI [`10.5281/zenodo.20601215`](https://doi.org/10.5281/zenodo.20601215)) and the nucleon-binding three-ledger programme (`hqiv-nucleon-binding-paper`).
