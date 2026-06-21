# HEP decay readout reproducers

**100 Python modules** (stdlib only — no ``pip install``). Imports are **local**
``hqiv_*.py`` files in this folder, closed by import tracing from
``hqiv_hep_readout_pipeline.py``.

## Quick start

```bash
cd scripts   # this directory (or unzip scripts.zip here)
export PYTHONPATH=.

# Regenerate all paper numerics + generated/*.tex (needs full HQIV-LEAN tree for TeX paths)
python3 hqiv_hep_readout_pipeline.py paper --strict

# Or explore one facility / parent
python3 hqiv_hep_readout_pipeline.py run --facility SPS_p_beam_400GeV --parent B_plus
```

## What is reproduced

| Output | Role |
|--------|------|
| ``data/hep_decay_benchmark.json`` | 81 structural passes + 567 readout rows |
| ``data/spine_discharge_law.json`` | Unified spine product registry |
| ``../generated/*.tex`` | Paper tables (branching, EW mass) |
| ``data/hep_readout_pipeline_manifest.json`` | Step log |

**Comparison-only** inputs (never fed into predictions): ``data/hep_decay_observations.json``,
``data/hadron_published_masses.json``.

**Catalog:** ``data/hadron-catalog.js`` (hadron valence content for mass readout).

## PDF

Numerics are reproducible from this folder inside the HQIV-LEAN repository:

```bash
cd ../..   # repository root (contains lakefile.toml)
latexmk -pdf papers/hep_decay_readout/hqiv_hep_decay_readout_from_multichannel.tex
```

Lean certificates: ``lake build HQIVPhysics`` (optional for Python numerics).

## Verify

Fast smoke test (< 30 s, frozen benchmark contract):

```bash
PYTHONPATH=. python3 -m unittest test_hqiv_hep_smoke -q
```

Full regression suite:

```bash
PYTHONPATH=. python3 -m unittest discover -s . -p 'test_hqiv_hep*.py' -q
```

See ``REPRODUCIBILITY.md`` for the one-command paper reproduction.
