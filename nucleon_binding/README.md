# Nucleon binding (Tier-2 #7)

**Single source:** `hqiv_nucleon_binding_from_composite_trace.tex`

**Title:** *Binding Energy and the Weak Force from HQIV Composite-Trace Weights: Lock-In Masses, Three Ledgers, and Zero-Knob Half-Lives*

**Bib key:** `hqiv-nucleon-binding-paper` in `papers/references.bib`

## Build

```bash
cd papers/nucleon_binding
latexmk -pdf hqiv_nucleon_binding_from_composite_trace.tex
```

Output: `hqiv_nucleon_binding_from_composite_trace.pdf` (27 pages).

## Reproducers

See `scripts/README.md`. Zenodo bundle: `scripts.zip` (self-contained; `MANIFEST.sha256` inside `scripts/`).

Refresh the bundle from repository root:

```bash
python3 scripts/bundle_nucleon_binding_scripts.py
```

Run witness scripts from the repository root (`HQIV/hqiv-lean`) or from `scripts/` inside the extracted zip.

## Lean

Machine-checked modules: `lake build paper_nucleon_binding` in [HQIV/hqiv-lean](https://github.com/HQIV/hqiv-lean).

## Archive

The former working copy `nucleon_binding_beta_decay.tex` (geometric binding + β programme draft) was merged into the canonical note and moved to `papers/archive/nucleon_binding_beta_decay/`.
