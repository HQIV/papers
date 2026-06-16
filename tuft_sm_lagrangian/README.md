# TUFT + SM Lagrangian Synthesis (Tier-2 Opener)

**Published:** Zenodo v2 — [`10.5281/zenodo.20601215`](https://doi.org/10.5281/zenodo.20601215) (2026-06-08)  
**Bib key:** `hqiv-tuft-sm-lagrangian-paper`

This directory contains the HQIV paper that realizes Nielsen's TUFT synthesis on the complex Hopf fibration inside the discrete octonion-carrier framework.

Nielsen's Topological Unified Field Theory (TUFT) supplies the topological tool: the complex Hopf fibration as classifying space for charge-quantised U(1) theories, the nested Hopf shells, and the vision of a single-scale synthesis in which the entire fermion mass spectrum descends from contact Beltrami spectra on those shells.

This work supplies the dynamic realization: the three Hopf-shell structures emerge on the discrete octonion carrier fixed by the HQIV light-cone axiom; the inner--outer Casimir balance on those shells (derived from the informational-energy/monogamy axiom) produces an explicit temperature-dependent scale and the factor $\kappa_6(\xi,\Phi,t)$. From this scale the full set of ground and excited-state masses is read, and every sector of the Standard Model Lagrangian is recovered as a direct projection of the proved discrete octonion O-Maxwell action.

The result is a parameter-free bridge (one consistent now-slice on the temperature ladder) from the two HQIV axioms to the entire effective $\mathcal{L}_{\rm SM}$, including all masses and Yukawa couplings. The construction yields HQIV-specific predictions, most notably longitudinal electromagnetic forces arising from the phase-gradient term in the O-Maxwell dynamics — signatures without direct counterparts in the pure continuum TUFT/SO(10) setting.

**Core thesis**  
A single now-slice $(\xi, \Phi, t)$ together with the lattice rationals fixed by the HQIV axioms ($\alpha = 3/5$, $\gamma = 2/5$, $\alpha_{\rm GUT} = 1/42$) determines the complete effective $\mathcal{L}_{\rm SM}$ at that epoch. PDG values are comparison targets only.

## Source and build

| Artifact | Path |
| --- | --- |
| Main source | `hqiv_tuft_sm_lagrangian_synthesis.tex` |
| PDF | `hqiv_tuft_sm_lagrangian_synthesis.pdf` |
| Scripts bundle | `scripts.zip` (49 Python files; see `scripts/README.md`) |
| Author metadata | `authors.json` |
| Bibliography | `../references.bib` |
| Shell ontology appendix | `../include/shell_ontology_messaging.tex` |

Build from this folder:

```bash
cd papers/tuft_sm_lagrangian
latexmk -pdf hqiv_tuft_sm_lagrangian_synthesis.tex
```

Regenerate `scripts.zip` after refreshing scripts from the repo root — see `scripts/README.md`.

## Paper structure (high level)

**§1** (Introduction): executive summary, pipeline figure, claim-status table, symbol table, scope box; **§1.1--1.2**: background and the two axioms. **§3**: inner--outer Casimir flowchart, $C_2(\xi)$ plot, Rindler proof sketch, error budget. **§6**: full SM-Lagrangian bridge (discrete O-Maxwell cell, five-sector theorem, parameter table). **§7**: falsifiability channels and longitudinal-EM estimates.

**Appendices:**
- `app:lean-catalog` — reader-friendly Lean module index (135-module import closure)
- `app:shell-ontology` — shell index ontology messaging
- `app:lean-witnesses` — plain-English theorem witness table

## Lean verification

Machine-checked content builds under the `paper_tuft_sm_lagrangian` Lake target in [HQIV/hqiv-lean](https://github.com/HQIV/hqiv-lean) ([PR #12](https://github.com/HQIV/hqiv-lean/pull/12)).

```bash
cd hqiv-lean
lake build paper_tuft_sm_lagrangian
```

## Zenodo record

| Field | Value |
| --- | --- |
| DOI | [`10.5281/zenodo.20601215`](https://doi.org/10.5281/zenodo.20601215) |
| Community | [HQIV](https://zenodo.org/communities/hqiv) |
| Files on record | PDF, `scripts.zip` |
| License | CC-BY-4.0 |

Downstream Tier-2 papers (`nucleon_binding/`, `bbn/`, `gluon_curvature_artifact/`) cite the TUFT+SM record via `\cite{hqiv-tuft-sm-lagrangian-paper}`; baryogenesis lock-in is published at [`10.5281/zenodo.20711255`](https://doi.org/10.5281/zenodo.20711255) (`hqiv-baryogenesis-paper`).
