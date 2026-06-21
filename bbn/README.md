# BBN Light Elements (Tier-2 #8)

**Published:** Zenodo v1 — [`10.5281/zenodo.20723606`](https://doi.org/10.5281/zenodo.20723606) (2026-06-16)

**Bib key:** `hqiv-bbn-paper`

*Big-Bang Nucleosynthesis from HQIV Network Weights: Lock-In η, Epoch Ladder, and Integrated Witnesses in the Lean Library*

Consumes published upstream records: TUFT+SM ([`10.5281/zenodo.20601215`](https://doi.org/10.5281/zenodo.20601215)), baryogenesis lock-in ([`10.5281/zenodo.20711255`](https://doi.org/10.5281/zenodo.20711255)), nucleon binding ([`10.5281/zenodo.20711453`](https://doi.org/10.5281/zenodo.20711453)).

**On-ramps:** [disregardfiat.tech](https://disregardfiat.tech) · [github.com/HQIV/hqiv-lean](https://github.com/HQIV/hqiv-lean) (formal library)

## Source and build

| Artifact | Path |
| --- | --- |
| Main source | `hqiv_bbn_light_elements_from_network_weights.tex` |
| Scripts bundle | `scripts.zip` (see `scripts/README.md`, `scripts/MANIFEST.sha256`) |
| Bibliography | `../references.bib` |

```bash
cd papers/bbn
latexmk -pdf hqiv_bbn_light_elements_from_network_weights.tex
```

Regenerate `scripts.zip` from the repository root:

```bash
python3 scripts/bundle_bbn_scripts.py
```

## Zenodo record

| Field | Value |
| --- | --- |
| DOI | [`10.5281/zenodo.20723606`](https://doi.org/10.5281/zenodo.20723606) |
| Community | [HQIV](https://zenodo.org/communities/hqiv) |
| Files | `hqiv_bbn_light_elements_from_network_weights.pdf`, `scripts.zip` |

Downstream papers cite this record via `\cite{hqiv-bbn-paper}` in `../references.bib`.
