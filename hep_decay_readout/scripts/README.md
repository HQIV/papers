# Reproducer scripts — HEP decay readout

This folder is a self-contained, source-only import closure for the paper-cited
HQIV-LEAN scripts. Run from the repository root when working in HQIV-LEAN, or put
this folder on `PYTHONPATH` when using the paper repo by itself.

For paper reproducibility, the scripts, comparison data, and generated table are
also bundled in `papers/hep_decay_readout/scripts.zip`; checksums are in
`papers/hep_decay_readout/scripts/MANIFEST.sha256`.

## Entry scripts (paper-cited)

| Script | Reproduces | Output |
| --- | --- | --- |
| `hqiv_hep_decay_readout.py` | Mass gaps, CKM slots, EM contact factor, OZI weights | inline / import |
| `hqiv_hep_decay_chain.py` | Unified HEP decay graph; quarkonium hadronic pooling | `data/decay_chain_readout.json` |
| `hqiv_hep_multichannel_expansion.py` | Programmatic charm/bottom channel expansion | channel lists |
| `hqiv_hep_production_readout.py` | Facility kinematics and production-rate proxies | inline |
| `hqiv_hep_decay_sigma.py` | Monte Carlo $\sigma$ propagation on benchmark rows | sigma fields in JSON |
| `hqiv_hep_decay_benchmark.py` | Lean-aligned calculator vs comparison layer | `data/hep_decay_benchmark.json` |
| `hqiv_spine_gap_closure_terms.py` | Exact spine-derived candidate terms for residual gaps | `data/spine_gap_closure_terms.json` |
| `export_hep_branching_table.py` | LaTeX table for paper (Table branch. comparison) | `papers/hep_decay_readout/generated/branching_comparison.tex` |
| `hqiv_decay_calculator.py` | CLI: `hep`, `nuclear`, `benchmark`, `discharge` | terminal + JSON |

## Unit tests

```bash
python3 scripts/test_hqiv_hep_decay_readout.py
python3 scripts/test_hqiv_hep_decay_chain.py
python3 scripts/test_hqiv_hep_multichannel_expansion.py
python3 scripts/test_hqiv_hep_decay_benchmark.py
python3 scripts/test_hqiv_decay_calculator.py
```

## Quick start

```bash
python3 scripts/hqiv_hep_decay_benchmark.py --json-out data/hep_decay_benchmark.json
python3 scripts/hqiv_spine_gap_closure_terms.py
PYTHONPATH=scripts python3 scripts/export_hep_branching_table.py
cd papers/hep_decay_readout && pdflatex hqiv_hep_decay_readout_from_multichannel.tex
```

## Inputs and comparison layer

- Proton lock-in anchor $938.272\,\mathrm{MeV}$ is a lapse-readout comparison target only.
- PDG / facility reference branching, masses, and production fractions appear in `data/hep_decay_observations.json` as **comparison rows only**---never as HQIV prediction inputs.
- Open-flavour topology seeds are unit weighted (`openFlavourTopologySeedWeight = 1`); no relative template priors are bundled.
- Gap-closure candidates in `spine_gap_closure_terms.json` are exact Lean-spine
  factors, not applied benchmark weights.
- Upstream mass ladder: `hqiv-tuft-sm-lagrangian-paper` (Zenodo [`10.5281/zenodo.20601215`](https://doi.org/10.5281/zenodo.20601215)).

## Citation

Steven Ettinger Jr., *Heavy-Flavour Decay Chains from HQIV Three-Ledger Readout* (2026). Bib key `hqiv-hep-decay-paper` in `papers/references.bib`.
