# Baryogenesis Lock-In (Tier-2 #6)

**Published:** Zenodo v1 — [`10.5281/zenodo.20711255`](https://doi.org/10.5281/zenodo.20711255) (2026-06-16)  
**Bib key:** `hqiv-baryogenesis-paper`

*Curvature-Ratio Lock-In for Baryon Asymmetry: Demonstrated on the HQIV Discrete Spine (Lean Formalisation)*

Cites the published TUFT+SM synthesis ([`10.5281/zenodo.20601215`](https://doi.org/10.5281/zenodo.20601215)).

## Programme position

**This note is a capability demonstration, not the programme goal.** It is the seventh HQIV preprint and functions as a doorway to the shared discrete curvature-ratio spine. Baryon-asymmetry bookkeeping is one application of that spine (null-lattice curvature ratios, $G_2\cup\{\Delta\}\Rightarrow\mathfrak{so}(8)$, inner–outer Casimir balance, binding/contact networks). The primary artefacts are the Lean formalisation and the reproduction bundle.

**On-ramps:** [disregardfiat.tech](https://disregardfiat.tech) (plain-language tour, clickable Lean anchors) · [github.com/HQIV/hqiv-lean](https://github.com/HQIV/hqiv-lean) (formal library) · companion BBN note (`hqiv-bbn-paper`).

**Lock-in at $m=4$.** `referenceM = 4` is the first shell on the discrete ladder with enough octonion-mode budget to host the full sector spine ($N_{\mathrm{new}}(4)=40$ in `OctonionicLightCone.lean`; $G_2\cup\{\Delta\}\Rightarrow\mathfrak{so}(8)$ in `SO8ClosureAbstract.lean`). Baryogenesis $\Omega_k$ and $\eta$ normalisation are read at this same proton-lock-in row ($\xi_{\mathrm{lock}}=5$).

## Source and build

| Artifact | Path |
| --- | --- |
| Main source | `hqiv_baryogenesis_curvature_lockin.tex` |
| PDF | `hqiv_baryogenesis_curvature_lockin.pdf` |
| Scripts bundle | `scripts.zip` (see `scripts/README.md`, `scripts/MANIFEST.sha256`) |
| Author metadata | `authors.json` |
| Bibliography | `../references.bib` |

Build from this folder:

```bash
cd papers/baryogenesis_lockin
latexmk -pdf hqiv_baryogenesis_curvature_lockin.tex
```

Regenerate `scripts.zip` from the repository root:

```bash
python3 scripts/bundle_baryogenesis_scripts.py
```

## Current witness panel

| Panel | Metric | Value |
| --- | --- | --- |
| Lean lock-in anchor | $\eta_{10}$ | **6.10** (quarantined `eta_paper`) |
| Dynamic bulk (comparison) | $\eta_{10}$, $\Omega_b$ | **6.20**, **0.0499** |
| Dynamic $\eta$ at lock-in (dimless binding feedback) | $\eta_{10}$ | **$\approx 7.0$** ($\eta_{\mathrm{paper}}\times(1+\delta_{\mathrm{bind}})$) |
| Faithful BBN @ $\eta_{\mathrm{paper}}$ | $Y_p$, $D/H$ | **0.244**, **$2.51\times 10^{-5}$** |
| Faithful BBN @ $\eta_{\mathrm{paper}}$ | $^3\mathrm{He}/H$, $^7\mathrm{Li}/H$ | **$1.01\times 10^{-5}$**, **$2.54\times 10^{-10}$** (pre-depletion) |
| Coc semi-analytic @ same $\eta$ | $^7\mathrm{Li}/H$ | **$\approx 4.65\times 10^{-10}$** (comparison, not HQIV output) |
| $D/H$ vs Coc 2015 | $z$-score | **$\approx -0.45$** |

Regenerate JSON witnesses:

```bash
python3 scripts/hqiv_dynamic_bulk_bbn.py
python3 scripts/hqiv_bbn_integrator.py --json data/bbn_integrator.json
python3 scripts/hqiv_integrator_lean_audit.py
python3 scripts/bundle_baryogenesis_scripts.py
```

## Zenodo record

| Field | Value |
| --- | --- |
| DOI | [`10.5281/zenodo.20711255`](https://doi.org/10.5281/zenodo.20711255) |
| Community | [HQIV](https://zenodo.org/communities/hqiv) |
| Files on record | PDF, `scripts.zip` |
| License | CC-BY-4.0 |

Downstream papers (`nucleon_binding/`, `bbn/`) cite this record via `\cite{hqiv-baryogenesis-paper}` in `../references.bib`.
