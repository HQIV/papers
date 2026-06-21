# Nucleon Binding (Tier-2 #7)

**Published:** Zenodo v1 — [`10.5281/zenodo.20711453`](https://doi.org/10.5281/zenodo.20711453) (2026-06-16)  
**Bib key:** `hqiv-nucleon-binding-paper`

*Binding Energy and the Weak Force from HQIV Composite-Trace Weights: Lock-In Masses, Three Ledgers, and Zero-Knob Half-Lives*

This note establishes the local-curvature slot equations ($B_{\mathrm{curv}}(\xi)$, three $\beta$ ledgers, slot-wise mass/binding closure, outside-contact primitives) witnessed from nucleon binding through bulk condensed matter. It cites the published TUFT+SM synthesis ([`10.5281/zenodo.20601215`](https://doi.org/10.5281/zenodo.20601215)) and baryogenesis lock-in ([`10.5281/zenodo.20711255`](https://doi.org/10.5281/zenodo.20711255)).

**Referee-facing width stack (v4+):** §`sec:width-assembly` assembles Ledger III in one equation (`G_F`, valley exponent $2(A{-}1){+}1$, interior width-well blend, free-branch $B_{\mathrm{curv}}$ catalysis); §`sec:downstream` states cross-paper consistency with baryogenesis and BBN (coupled $\tau_n(T)$, $^7$Li/H).

## Source and build

| Artifact | Path |
| --- | --- |
| Main source | `hqiv_nucleon_binding_from_composite_trace.tex` |
| PDF | `hqiv_nucleon_binding_from_composite_trace.pdf` |
| Scripts bundle | `scripts.zip` (see `scripts/README.md`, `scripts/MANIFEST.sha256`) |
| Author metadata | `authors.json` |
| Bibliography | `../references.bib` |

Build from this folder:

```bash
cd papers/nucleon_binding
latexmk -pdf hqiv_nucleon_binding_from_composite_trace.tex
```

Regenerate `scripts.zip` from the repository root:

```bash
python3 scripts/bundle_nucleon_binding_scripts.py
```

## Current witness panel (2026-06-08)

| Panel | Metric | Value |
| --- | --- | --- |
| Light isotopes ($A\le 4$) | mean $\|\Delta M\|/M_{\mathrm{ref}}$ | **0.003%** (curvature $G_{\mathrm{eff}}$ spine) |
| Curvature binding @ lock-in | mean $\|\Delta M\|/M_{\mathrm{ref}}$ ($A\le 4$) | **0.003%** (mass ledger; BBN Q) |
| $\mathrm{H_2O}$ ice Ih | $\rho_{\mathrm{solid}}$, $T_{\mathrm{sl}}$, $n$ | 0.920 g/cm³, 272.7 K, 1.30 |
| Condensed panel (4 species) | mean $\|\Delta\rho\|/\rho_{\mathrm{NIST}}$ @ melt $T$ | **0.4%** |
| BBN @ $\eta_{\mathrm{paper}}$ | $Y_p$, $D/H$, $^7\mathrm{Li}/H$ | 0.244, $2.51\times 10^{-5}$, $2.54\times 10^{-10}$ |
| Lab outside (mass chart) | gravity + CMB dipole | **~0.28 ppm** on $M_p$ |

Regenerate JSON witnesses:

```bash
PYTHONPATH=scripts python3 scripts/hqiv_curvature_binding_program.py --json data/curvature_binding_program.json
PYTHONPATH=scripts python3 scripts/hqiv_binding_energy_program.py --json data/binding_energy_program.json
PYTHONPATH=scripts python3 scripts/hqiv_bbn_integrator.py --json data/bbn_integrator.json
PYTHONPATH=scripts python3 scripts/hqiv_bbn_paper_tables.py --json data/bbn_paper_tables.json
PYTHONPATH=scripts python3 scripts/hqiv_condensed_phase_audit.py
PYTHONPATH=scripts python3 scripts/hqiv_isotope_pdg_benchmark.py --json data/isotope_pdg_benchmark.json
PYTHONPATH=scripts python3 scripts/hqiv_nucleon_binding_integrator.py --json data/nucleon_binding_integrator.json
python3 scripts/bundle_nucleon_binding_scripts.py
```

## Lean verification

Machine-checked content builds under the `paper_nucleon_binding` Lake target in [HQIV/hqiv-lean](https://github.com/HQIV/hqiv-lean) ([PR #13](https://github.com/HQIV/hqiv-lean/pull/13)).

```bash
lake build paper_nucleon_binding
```

## Zenodo

| Field | Value |
| --- | --- |
| DOI | [`10.5281/zenodo.20711453`](https://doi.org/10.5281/zenodo.20711453) |
| Community | [HQIV](https://zenodo.org/communities/hqiv) |
| Files on record | PDF, `scripts.zip` |
| License | CC-BY-4.0 |

Downstream papers (`bbn/`, `hep_decay_readout/`) cite this record via `\cite{hqiv-nucleon-binding-paper}` in `../references.bib`.
