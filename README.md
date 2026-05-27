# HQIV Papers

This repository collects the LaTeX sources, build artifacts, and bibliographies for the HQIV (Horizon-Quantized Informational Vacuum) paper series. It is consumed as a git submodule by [HQIV/hqiv-lean](https://github.com/HQIV/hqiv-lean).

All publications go to the [Zenodo HQIV community](https://zenodo.org/communities/hqiv).

## Publication order

The series is published in tiers so that each later paper can cite the earlier ones by their minted DOIs. Tier 0 and Tier-1 records #1–3 (`3d_causal_growth`, `octonionic_action`, `finite_mode_kirchhoff`) are on Zenodo; remaining Tier-1–3 entries are unpublished drafts queued in the order below.

### Tier 0 — Already published on Zenodo (frozen)

| # | Folder | Source `.tex` | DOI (latest version) | Concept DOI | Date | Bib key |
|---|---|---|---|---|---|---|
| 0a | (top-level main paper) | `main.tex` | `10.5281/zenodo.18899939` | `10.5281/zenodo.18794889` | 2026-03-07 | `ettinger2026hqiv` |
| 0b | `lightcone_to_oshoracle/` | `octonion_lightcone_to_oshoracle.tex` | `10.5281/zenodo.19336553` | `10.5281/zenodo.19227897` | 2026-03-30 | `hqiv-lightcone-paper` |
| 0c | `closure/` | `closure.tex` (+ `so8_closure_full_appendix.tex`) | `10.5281/zenodo.20214211` | `10.5281/zenodo.20214210` | 2026-05-15 | `hqiv-so8-paper` |

The lightcone record is scheduled for a v3 update (see "Working checklist" below). New versions reuse the same concept DOI and only mint a fresh version DOI; companion drafts cite the **concept DOI** so they keep resolving across versions (where a concept DOI exists).

### Tier 1 — Foundation extension quartet (sequence-strict)

Each paper here is a direct mathematical/variational sequel to `closure` and must publish before the next so that companion `\cite{...}` keys resolve to live DOIs.

#### Published on Zenodo

| # | Folder | Source `.tex` | DOI (version) | Date | Bib key |
|---|---|---|---|---|---|
| 1 | `3d_causal_growth/` | `hqiv_3d_causal_growth_octonionic_gauge.tex` | [`10.5281/zenodo.20415586`](https://doi.org/10.5281/zenodo.20415586) | 2026-05-27 | `hqiv-3d-growth-paper` |
| 2 | `octonionic_action/` | `hqiv_octonionic_action_and_uniqueness.tex` | [`10.5281/zenodo.20416085`](https://doi.org/10.5281/zenodo.20416085) | 2026-05-27 | `hqiv-oct-action-paper` |
| 3 | `finite_mode_kirchhoff/` | `hqiv_finite_mode_kirchhoff_from_lattice_simplex.tex` | [`10.5281/zenodo.20416564`](https://doi.org/10.5281/zenodo.20416564) | 2026-05-27 | `hqiv-kirchhoff-paper` |

#### In queue (pre-DOI)

| # | Folder | Bib key | Role |
|---|---|---|---|
| 4 | `thermodynamics_arrow/` | `hqiv-thermo-arrow-paper` | Thermodynamic laws 0–3 on the shell ladder; finite blackbody entropy; arrow from causal monogamy + discrete dissipation signs. Sequel to Kirchhoff. |

### Tier 2 — Standard Model and mass closure

| # | Folder | Bib key | Role |
|---|---|---|---|
| 5 | `lean_to_mass_spectrum/` | `hqiv-mass-spectrum-paper` | Electroweak scale + fermion ladder from lock-in `v` and outer-horizon `S(m)`. Cross-links lightcone's projected complex carrier. |
| 6 | `sm_lagrangian/` | `hqiv-sm-lagrangian-paper` | Full SM Lagrangian as sectorial projection of the discrete action. |
| 7 | `baryogenesis_lockin/` | `hqiv-baryogenesis-paper` | Baryon asymmetry as curvature-ratio lock-in. Cites all of Tier 1. |
| 8 | `nucleon_binding/` | `hqiv-nucleon-binding-paper` | Nucleon masses from $8\times8$ composite-trace binding at lock-in; bonded vs free neutron scaffold. β-decay lifetimes marked future work. |
| 9 | `bbn/` | `hqiv-bbn-paper` | BBN light elements from network weights + epoch ladder; integrated $Y_p$ witnesses. Consumes lock-in $\eta$ (#7) and nucleon binding (#8). |

### Tier 3 — Applied phenomenology

| # | Folder | Bib key | Role |
|---|---|---|---|
| 10 | `longitudinal_em_force/` | `ettinger2026longitudinal` | Axial wire force from the O-Maxwell phase-gradient term. |
| 11 | `coronal_heating/` | `hqiv-coronal-paper` | Direct application of #10 to coronal flux tubes; back-to-back companion. |
| 12 | `omaxwell_fluid_chart/` | `hqiv-fluid-chart-paper` | F2 fluid-closure chart companion to `Action.lean` / `ModifiedMaxwell.lean`. |
| 13 | `orbital_flyby/` | `hqiv-flyby-paper` | Flyby anomalies + galaxy rotation from inertia screen and Lense–Thirring release fraction. |

### Archived (not republished)

- `rapidity_so8_closure/` → moves into `archive/` next pass. Its own abstract identifies it as the long-form workspace draft of `closure.tex`; the published `closure` record (`10.5281/zenodo.20214211`) is the canonical version.

## Cross-citation bib keys

When drafting any companion, use these keys when citing earlier work in the chain. They are the canonical keys carried in `references.bib`:

| Folder | Bib key in `references.bib` |
|---|---|
| HQIV main (Zenodo only) | `ettinger2026hqiv` |
| `closure/` | `hqiv-so8-paper` |
| `lightcone_to_oshoracle/` | `hqiv-lightcone-paper` |
| `3d_causal_growth/` | `hqiv-3d-growth-paper` (Zenodo [`10.5281/zenodo.20415586`](https://doi.org/10.5281/zenodo.20415586), v1 2026-05-27) |
| `octonionic_action/` | `hqiv-oct-action-paper` (Zenodo [`10.5281/zenodo.20416085`](https://doi.org/10.5281/zenodo.20416085), v1 2026-05-27) |
| `finite_mode_kirchhoff/` | `hqiv-kirchhoff-paper` (Zenodo [`10.5281/zenodo.20416564`](https://doi.org/10.5281/zenodo.20416564), v1 2026-05-27) |
| `thermodynamics_arrow/` | `hqiv-thermo-arrow-paper` |
| `lean_to_mass_spectrum/` | `hqiv-mass-spectrum-paper` |
| `sm_lagrangian/` | `hqiv-sm-lagrangian-paper` |
| `baryogenesis_lockin/` | `hqiv-baryogenesis-paper` |
| `nucleon_binding/` | `hqiv-nucleon-binding-paper` |
| `bbn/` | `hqiv-bbn-paper` |
| `longitudinal_em_force/` | `ettinger2026longitudinal` |
| `coronal_heating/` | `hqiv-coronal-paper` |
| `omaxwell_fluid_chart/` | `hqiv-fluid-chart-paper` |
| `orbital_flyby/` | `hqiv-flyby-paper` |
| Lean library (GitHub) | `hqiv-lean` |
| Brodie quantised-inertia | `brodie2026` |

## Working checklist

### Current focus — Lightcone v3 tightening (`lightcone_to_oshoracle/`)

The DOI is already minted (concept `10.5281/zenodo.19227897`); a tightened v3 will publish under the same concept DOI.

- [ ] Compress the megaparagraph abstract to ~150–200 words; keep result statements (R⁸ carrier, lossless QM bookkeeping, sparse update, α=3/5 / γ=2/5 forced, β consistency check, pilot-wave stance).
- [ ] Trim the "four-layer reader guide" to defer patch-QFT plumbing to `include/patch_theory_messaging.tex` (already `\input`-ed at line 84).
- [ ] Adopt `include/release_archive_macros.tex` for companion-code/DOI references currently hand-written near the top.
- [ ] Apply the **reader-first writing convention** (see "Writing conventions" below): pull every `\lean{Hqiv/...}` and `\texttt{snake\_case}` Lean identifier out of the body and abstract; replace each with a reader-friendly name `\hyperref`-linked to a single Lean module-index appendix.
- [ ] Add closure (`10.5281/zenodo.20214211`) and lightcone-self (`10.5281/zenodo.19336553`) records to `references.bib` as `hqiv-so8-paper` and `hqiv-lightcone-paper`. (Both are referenced by Tier 1+ drafts already.)
- [ ] Rebuild the PDF, push v3 to Zenodo on the existing concept DOI.

### Next sessions (queued, not started)

- [x] Tier 1 #1: `3d_causal_growth/` published on Zenodo ([`10.5281/zenodo.20415586`](https://doi.org/10.5281/zenodo.20415586), 2026-05-27).
- [x] Tier 1 #2: `octonionic_action/` published on Zenodo ([`10.5281/zenodo.20416085`](https://doi.org/10.5281/zenodo.20416085), 2026-05-27; `scripts.zip` on record).
- [x] Tier 1 #3: `finite_mode_kirchhoff/` published on Zenodo ([`10.5281/zenodo.20416564`](https://doi.org/10.5281/zenodo.20416564), 2026-05-27; `scripts.zip` on record).
- [ ] Tier 1 remainder: tighten `thermodynamics_arrow/` against shared `include/` and live upstream DOIs; publish in the listed order.
- [ ] Move `rapidity_so8_closure/` into `archive/`.
- [ ] Tier 2: `lean_to_mass_spectrum/` → `sm_lagrangian/` → `baryogenesis_lockin/` → `nucleon_binding/` → `bbn/`.
- [x] Tier 3 (start): `longitudinal_em_force/` + `coronal_heating/` (back-to-back).
- [x] Tier 3: `orbital_flyby/` (SPARC map + Rosetta boundary-channel note).
- [ ] Tier 3 (remainder): `omaxwell_fluid_chart/`.

## Writing conventions

**Reader first, not a Lean walkthrough.** The paper body is for physicists and mathematicians. Lean is the audit layer — load-bearing, but it lives in an appendix, not in every other sentence.

### Rule

- **Body:** prose uses reader-friendly names for every concept ("the lattice $\alpha$-ratio identity", "the curvature norm", "the shell-imprint factor"). No `\path{Hqiv/...}` and no `\texttt{snake\_case\_lemma\_names}` inline.
- **Appendix:** every Lean reference (module path + theorem/definition name) appears in a single appendix section that the body links to. The appendix is the *only* place a reader has to look at file paths.
- **Cross-link:** the reader-friendly name in the body is a clickable `hyperref` to its appendix entry; the appendix entry itself shows the Lean module + identifier.

### Pattern

```latex
% In the body — reader-friendly, clickable
The lattice ratio at every truncation equals
\(\alpha = 3/5\) (\hyperref[lean:latticeAlphaRatio]{lattice $\alpha$-ratio identity}).

% In the back matter — single Lean index
\appendix
\section{Lean module index}\label{app:lean-index}

\begin{description}
\item[\phantomsection\label{lean:latticeAlphaRatio}Lattice $\alpha$-ratio identity.]
  \path{Hqiv/Geometry/OctonionicLightCone.lean},
  theorem \texttt{latticeAlphaRatio\_eq\_alpha}.

\item[\phantomsection\label{lean:gammaForced}Forced $\gamma = 2/5$.]
  \path{Hqiv/Geometry/AlphaGammaForcedByLattice.lean},
  theorem \texttt{gamma\_eq\_2\_5} (paired with
  \texttt{alpha\_gamma\_forced\_pair}).
\end{description}
```

`\hypersetup{linkcolor=blue}` (or similar) is encouraged so the body links are visibly clickable in the PDF.

### Allowed exceptions

- Module names may appear in the body of a *Lean status* paragraph that is itself flagged as such (e.g. "Status of the formal cone:") — but at most one such paragraph per section.
- Theorems being *stated* as the paper's own contribution may carry their Lean identifier on the same line as the theorem statement (one identifier, in `\texttt{...}`), since the identifier *is* the contribution.
- Standalone "audit certificate" papers (like the published `closure`) may keep more inline Lean references because the certificate *is* the paper. New drafts should not adopt that style.

### Retroactive cleanup target

The lightcone v3 pass is the first paper to be brought into compliance (see the lightcone checklist above — it is currently the worst offender, with dozens of `\lean{...}` calls and `\texttt{module\_name}` references in the body and abstract). Tier 1+ drafts must ship with this convention from day one.

## Layout

```
papers/
├── README.md
├── references.bib          ← single shared bibliography
├── include/                ← shared LaTeX fragments (cited via ../include/...)
│   ├── patch_theory_messaging.tex
│   └── release_archive_macros.tex
├── <paper_short_name>/     ← one folder per paper
│   ├── <paper>.tex
│   ├── <paper>.pdf         (rebuilt locally; .gitignored auxiliaries excluded)
│   └── authors.json
└── archive/                ← superseded / historical drafts
    ├── mainold/
    └── MHD/
```

### Paper folders (alphabetical)

| Folder                          | Source `.tex`                                       | Tier |
| ------------------------------- | --------------------------------------------------- | ---- |
| `closure/`                      | `closure.tex` (+ bundled `so8_closure_full_appendix.tex`) | 0c   |
| `lightcone_to_oshoracle/`       | `octonion_lightcone_to_oshoracle.tex`               | 0b   |
| `3d_causal_growth/`             | `hqiv_3d_causal_growth_octonionic_gauge.tex`        | 1.1 (Zenodo) |
| `octonionic_action/`            | `hqiv_octonionic_action_and_uniqueness.tex`         | 1.2 (Zenodo) |
| `finite_mode_kirchhoff/`        | `hqiv_finite_mode_kirchhoff_from_lattice_simplex.tex` | 1.3 (Zenodo) |
| `thermodynamics_arrow/`         | `hqiv_thermodynamics_and_arrow_of_time.tex`         | 1.4  |
| `lean_to_mass_spectrum/`        | `hqiv_lean_from_combinatorics_to_mass_spectrum.tex` | 2.5  |
| `sm_lagrangian/`                | `hqiv_sm_lagrangian_from_discrete_action.tex`       | 2.6  |
| `baryogenesis_lockin/`          | `hqiv_baryogenesis_curvature_lockin.tex`            | 2.7  |
| `nucleon_binding/`              | `hqiv_nucleon_binding_from_composite_trace.tex`     | 2.8  |
| `bbn/`                          | `hqiv_bbn_light_elements_from_network_weights.tex`  | 2.9  |
| `longitudinal_em_force/`        | `longitudinal_em_force_hqiv.tex`                    | 3.10 |
| `coronal_heating/`              | `hqiv_coronal_longitudinal_heating.tex`             | 3.11 |
| `omaxwell_fluid_chart/`         | `HQIV_OMaxwell_fluid_chart.tex`                     | 3.12 |
| `orbital_flyby/`                | `hqiv_orbital_flyby_anomaly.tex` (+ `flyby_paper_table.tex`) | 3.13 |
| `rapidity_so8_closure/`         | `hqiv_rapidity_manifold_so8_closure.tex`            | archive (pending move) |
| `archive/mainold/`              | `mainold.tex` (legacy monolithic draft)             | archive |
| `archive/MHD/`                  | `mhd.tex`                                           | archive |

## Building

Each paper is self-contained from its own folder:

```bash
cd <paper_short_name>/
latexmk -pdf <paper>.tex
```

Paths in the sources reference the shared bibliography and includes relatively:

- `\input{../include/patch_theory_messaging.tex}`
- `\input{../include/release_archive_macros.tex}` (Tier 0/1 papers that ship a companion-code archive)
- `\bibliography{../references}`

(Archive papers nested one level deeper use `../../` accordingly.)

## Authors

Every paper folder has an `authors.json` with the schema:

```json
{
  "paper": "<paper_short_name>",
  "authors": [
    {
      "name":        "Steven Ettinger Jr",
      "email":       "steven@disregardfiat.tech",
      "affiliation": "Independent Researcher",
      "orcid":       "0009-0004-9940-3666",
      "github":      "disregardfiat"
    }
  ]
}
```

The single sole-author ORCID `0009-0004-9940-3666` is now propagated to every paper (see commit history if a folder is missing it). Add new co-authors by appending to the `authors` array; only fill in `orcid` once the new author has a real iD (use `null` until then, never the placeholder zeros).
