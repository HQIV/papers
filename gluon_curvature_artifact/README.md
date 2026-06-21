# Gluon curvature artifact (Tier-2 closure)

**Published:** Zenodo v1 — [`10.5281/zenodo.20724572`](https://doi.org/10.5281/zenodo.20724572) (2026-06-17)

**Single source:** `hqiv_gluon_as_curvature_artifact.tex`

**Title:** *The Gluon as Curvature Artifact: Strong Binding from Inner–Outer Casimir Trapping on the Octonion Carrier*

**Bib key:** `hqiv-gluon-curvature-note` in `papers/references.bib`

**Queue position:** Tier-2 closure note after BBN (#8); load-bearing for `hep_decay_readout/` (#9).

## Role

Makes explicit what upstream Tier-2 papers already use: continuum “gluons” and “QCD binding” are translations of inner–outer Casimir trapping on the strong octonion channels, factorised in Lean as trapped zero-point × normalised SO(8) composite-trace selection. No independent gluon fields in the default discrete action.

## Reproducibility

| Check | Command |
| --- | --- |
| Paper cone (recommended) | `lake build paper_gluon_curvature` |
| Emission scaffold | `lake env lean Hqiv/Physics/StrongChannelEmissionScaffold.lean` |
| Collider discharge | `lake env lean Hqiv/Physics/StrongSectorColliderDischarge.lean` |
| Quantitative witness (9/9) | `PYTHONPATH=scripts python3 scripts/hqiv_strong_sector_collider_discharge.py --strict` |
| HEP refinements witness (9/9) | `PYTHONPATH=scripts python3 scripts/hqiv_hep_collider_refinements.py --strict` |
| Unit tests (refinements) | `PYTHONPATH=scripts python3 scripts/test_hqiv_hep_collider_refinements.py` |
| Unit tests (discharge) | `PYTHONPATH=scripts python3 scripts/test_hqiv_strong_sector_collider_discharge.py` |

Zenodo record: [`10.5281/zenodo.20724572`](https://doi.org/10.5281/zenodo.20724572) (PDF + `scripts.zip` on deposit). Refresh bundle:

```bash
python3 scripts/bundle_gluon_curvature_scripts.py
```

Standalone repro (extracted `scripts.zip`):

```bash
cd scripts
PYTHONPATH=. python3 hqiv_strong_sector_collider_discharge.py --strict
PYTHONPATH=. python3 hqiv_hep_collider_refinements.py --strict
```

## Upstream (published DOIs)

| Record | Bib key | DOI |
| --- | --- | --- |
| TUFT+SM synthesis | `hqiv-tuft-sm-lagrangian-paper` | [`10.5281/zenodo.20601215`](https://doi.org/10.5281/zenodo.20601215) |
| Baryogenesis lock-in | `hqiv-baryogenesis-paper` | [`10.5281/zenodo.20711255`](https://doi.org/10.5281/zenodo.20711255) |
| Nucleon binding | `hqiv-nucleon-binding-paper` | [`10.5281/zenodo.20711453`](https://doi.org/10.5281/zenodo.20711453) |
| BBN abundances | `hqiv-bbn-paper` | [`10.5281/zenodo.20723606`](https://doi.org/10.5281/zenodo.20723606) |

## Lean + witness status (2026-06)

| Item | Status |
| --- | --- |
| Trapped-Casimir factorisation | **Proved** |
| Unified curvature log kernel | **Proved** at $m=2,3,4$ |
| Colour Casimirs + emission scaffold | **Proved** — `StrongChannelEmissionScaffold.lean` |
| PETRA $R_{23}$, mean thrust | **Discharged** — witness 0.09σ / 0.08σ |
| Non-abelian $C_A/C_F$ from filter | **Discharged** — exact $9/4$ |
| $\sigma(ggH)$ LO/NLO | **Discharged** — witness 0.13σ / 2.22σ |
| QGP $\eta/s$ | **Discharged** — witness 1.0σ |
| Glueball $0^{++}$, $2^{++}$ | **Discharged** — witness 0.26σ / 1.26σ |
| PDF gluon moment | **Discharged** — witness 0.71σ |
| MC shower, thrust bins, $ggH$ $p_T$, QGP $v_2$/$R_{AA}$, PDF $x$ | **Discharged** — refinement witness 9/9 |
| Third-party MC (Pythia/Herwig) | **Future** external validation |

## Build PDF

```bash
cd papers/gluon_curvature_artifact
latexmk -pdf hqiv_gluon_as_curvature_artifact.tex
```

## Pre-publication checklist

- [x] Reader-first pass + Lean module index
- [x] `lake build paper_gluon_curvature` green
- [x] Collider discharge witness `--strict` green (9/9)
- [x] HEP refinement witness `--strict` green (9/9)
- [x] `scripts.zip` bundled
- [x] Deposit PDF on Zenodo ([`10.5281/zenodo.20724572`](https://doi.org/10.5281/zenodo.20724572), v1 2026-06-17); `references.bib` updated
- [x] Confirm `hep_decay_readout` cites minted gluon DOI ([`10.5281/zenodo.20724572`](https://doi.org/10.5281/zenodo.20724572))
