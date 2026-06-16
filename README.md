# HQIV Papers

This repository collects the LaTeX sources, build artifacts, and bibliographies for the HQIV (Horizon-Quantized Informational Vacuum) paper series. It is consumed as a git submodule by [HQIV/hqiv-lean](https://github.com/HQIV/hqiv-lean).

All publications go to the [Zenodo HQIV community](https://zenodo.org/communities/hqiv).

## Publication order

The series is published in tiers so that each later paper can cite the earlier ones by their minted DOIs. Tier~0, all four Tier-1 foundation-extension records, Tier-2 #5 (TUFT+SM synthesis), and Tier-2 #6 (baryogenesis lock-in) are on Zenodo; remaining Tier-2+ entries are unpublished drafts queued in the order below.

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
| 4 | `thermodynamics_arrow/` | `hqiv_thermodynamics_and_arrow_of_time.tex` | [`10.5281/zenodo.20478826`](https://doi.org/10.5281/zenodo.20478826) | 2026-05-31 | `hqiv-thermo-arrow-paper` |

### Tier 2 — Standard Model and mass closure (combined foundation)

#### Published on Zenodo

| # | Folder | Source `.tex` | DOI (version) | Date | Bib key |
|---|---|---|---|---|---|
| 5 | `tuft_sm_lagrangian/` | `hqiv_tuft_sm_lagrangian_synthesis.tex` | [`10.5281/zenodo.20601215`](https://doi.org/10.5281/zenodo.20601215) | 2026-06-08 | `hqiv-tuft-sm-lagrangian-paper` |
| 6 | `baryogenesis_lockin/` | `hqiv_baryogenesis_curvature_lockin.tex` | [`10.5281/zenodo.20711255`](https://doi.org/10.5281/zenodo.20711255) | 2026-06-16 | `hqiv-baryogenesis-paper` |

**Patch gauge consistency (2026-06):** the TUFT+SM synthesis records **proved** finite SM anomaly-trace cancellation, topological-sector discharge, fibre-torsion subleading sector zeta, light-cone \(\mathfrak{so}(8)\) holonomy with weak/colour non-abelian charts, **full four-edge SO(8) Wilson plaquettes** (`Hqiv/Physics/SO8PlaquetteHolonomy.lean`), shell-to-harmonic limits, **rapidity-phase Lorentz closure** (`Hqiv/Geometry/RapidityLorentzClosure.lean`), and **spatial-rotation Lorentz closure** for flyby/CMB/fluid directional readouts (`Hqiv/Geometry/SpatialRotationLorentzClosure.lean`). **Partial / open:** Haar measure on rotated charts; general flat HQVM kinetic invariance under `boostDiscretePotential41` (`Hqiv/Physics/DiscreteActionStrongPoincareBridge.lean`); continuum Wightman Poincaré — see `hqiv_tuft_sm_lagrangian_synthesis.tex` and `papers/include/patch_theory_messaging.tex`. **Discharged on partial slice:** Wilson–kinetic equivalence (`ActionHolonomyGlue.wilsonKineticPlaquetteEquivalence_discharged`); `fullActionStrongPoincare_discharged`.

#### Queued (unpublished)

| # | Folder | Bib key | Role |
|---|---|---|---|
| 7 | `nucleon_binding/` | `hqiv-nucleon-binding-paper` | Binding energy and the weak force: single source `hqiv_nucleon_binding_from_composite_trace.tex` ($8\times8$ composite-trace nucleon masses through $A=4$; three-ledger $\beta$ tipping; lab agreement). Cites #5 and #6. **Next in Tier-2 queue.** |
| 8 | `bbn/` | `hqiv-bbn-paper` | BBN light elements from network weights + faithful stoichiometric integrator ($Y_p$, $D/H$, $^3$He/H, $^7$Li/H at $\eta_{\mathrm{paper}}$). Consumes lock-in $\eta$ (#6) and nucleon binding (#7). |
| — | `gluon_curvature_artifact/` | `hqiv-gluon-curvature-note` | Tier-2 closure: the gluon is the curvature artifact of the inner-Casimir trapping on the strong octonion channels; identical in form and scale to the composite-trace binding and the inner trapped-Casimir heavy gap. Cites the combined TUFT+SM synthesis (#5), the nucleon-binding note, and the Tier-1 record. |
| 9 | `hep_decay_readout/` | `hqiv-hep-decay-paper` | Heavy-flavour three-ledger decay readout: discrete multichannel rules, quarkonium EM contact $39/10$, branching without partial-width inputs; $87/87$ comparison discharge. Extends nucleon-binding $\beta$ tipping. |

### Lean formal proof notes

| Folder | Source `.tex` | Role |
|---|---|---|
| `factor_search_formalization/` | `hqiv_factor_search_formalization.tex` | Formal audit note for the factor-search drivers, certificate soundness, and cost scaffolding. |
| `goldbach_so4_so2_delta/` | `goldbach_so4_so2_delta.tex` | Working Lean-backed reduction note for the `SO(4)` tangent carrier, selected `SO(2)+Δ` Goldbach parity channel, and threshold split into finite verification plus eventual selected-channel positivity. |
| `s3_zeta_so4_projection/` | `hqiv_s3_zeta_so4_projection_closed_form.tex` | S³ / SO(4) synthesis: harmonic--Δ closure, 45° quaternion projections, regional `ζ(s)` closed forms, polar decoupling and log edge, sector-zeta vs classical-ζ dictionary, HEP integration bridge (`sec:hep-zeta-bridge`); uses `readout_dictionary_messaging.tex` (not full patch contract). RH = proved equivalences with zero slack, not discharge. |

### Tier 3 — Applied phenomenology

| # | Folder | Bib key | Role |
|---|---|---|---|
| 10 | `longitudinal_em_force/` | `ettinger2026longitudinal` | Axial wire force from the O-Maxwell phase-gradient term. |
| 11 | `coronal_heating/` | `hqiv-coronal-paper` | Direct application of #10 to coronal flux tubes; back-to-back companion. |
| 12 | `omaxwell_fluid_chart/` | `hqiv-fluid-chart-paper` | F2 fluid-closure chart companion to `Action.lean` / `ModifiedMaxwell.lean`. |
| 13 | `orbital_flyby/` | `hqiv-flyby-paper` | HQIV acceleration readouts: flybys, SPARC+WHIM disks, filament cross-match, long-term galaxy–filament evolution. |
| 14 | `complex_time_stokes_bridge/` | `hqiv-complex-time-stokes-paper` | Lattice time angle / lapse / zeta phase; Wick bridge to Stokes factors; **functional PDE identity** with TUFT Beltrami--NS on finite Hopf modes (not Millennium smoothness). |

### Witness data (not Zenodo tier papers)

| Folder | Bib keys | Role |
|---|---|---|
| `compact_object_witness/` | `hqiv-compact-object-witness-data`, `hqiv-pulsar-witness-data`, `hqiv-lagrangian-faithfulness-audit`, `atnf_psrcat`, `xao_atnf_pulsar_mirror`, NICER/Shapiro keys | MHD equivalence paper + witness JSON; run `compact_object_witness/regenerate_data.sh`. |

### Archived (not republished)

- `archive/lean_to_mass_spectrum/` — early internal working draft; content merged into the combined TUFT+SM synthesis (`hqiv-tuft-sm-lagrangian-paper`).
- `archive/sm_lagrangian/` and `archive/tuft_hqiv_dynamic_mass_spectrum/` — two internal working drafts (one on the Lagrangian sector projections, one on the TUFT/Hopf mass spectrum) that were consolidated into the single combined paper in `tuft_sm_lagrangian/` before any release. They were never preprinted or deposited.
- `archive/nucleon_binding_beta_decay/` — geometric binding + β-programme working copy; merged into `nucleon_binding/hqiv_nucleon_binding_from_composite_trace.tex`.
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
| `thermodynamics_arrow/` | `hqiv-thermo-arrow-paper` (Zenodo [`10.5281/zenodo.20478826`](https://doi.org/10.5281/zenodo.20478826), v1 2026-05-31) |
| `tuft_sm_lagrangian/` | `hqiv-tuft-sm-lagrangian-paper` (Zenodo [`10.5281/zenodo.20601215`](https://doi.org/10.5281/zenodo.20601215), v2 2026-06-08) |
| `baryogenesis_lockin/` | `hqiv-baryogenesis-paper` (Zenodo [`10.5281/zenodo.20711255`](https://doi.org/10.5281/zenodo.20711255), v1 2026-06-16) |
| `nucleon_binding/` | `hqiv-nucleon-binding-paper` |
| `bbn/` | `hqiv-bbn-paper` |
| `gluon_curvature_artifact/` | `hqiv-gluon-curvature-note` |
| `hep_decay_readout/` | `hqiv-hep-decay-paper` |
| `longitudinal_em_force/` | `ettinger2026longitudinal` |
| `coronal_heating/` | `hqiv-coronal-paper` |
| `omaxwell_fluid_chart/` | `hqiv-fluid-chart-paper` |
| `orbital_flyby/` | `hqiv-flyby-paper` |
| `s3_zeta_so4_projection/` | `hqiv-s3-zeta-so4-paper` |
| Lean library (GitHub) | `hqiv-lean` |
| Brodie quantised-inertia | `brodie2026` |
| Compact-object witness data | `hqiv-compact-object-witness-data`, `hqiv-pulsar-witness-data`, `hqiv-lagrangian-faithfulness-audit` |
| Pulsar catalogs / masses | `atnf_psrcat`, `xao_atnf_pulsar_mirror`, `lorimer2004handbook`, `miller2019_j0030`, `riley2021_j0740`, `rutherford2024_msp_masses`, `freire2012_shapiro`, `antoniadis2013_ns_max`, `crombie2020_j0740` |

**Standard chemistry / material-response references** (used in `nucleon_binding/` condensed-phase slots; not HQIV-specific): `nistwebbook_h2o`, `crc2023handbook`, `petrenko2002ice`, `goerigk2017gmtkn55`, `gillespie1970vsepr`, `hecht2017optics`, `jackson1999`, `ashcroft1976ssp`, `atkins2018pchem`, `eyring1936viscosity`, `grimme2011d3`, `santra2013ice`, `brandenburg2016jctc`, `reilly2013mbd`, `gillan2016perspective`.

## Working checklist

### Current focus — Nucleon binding (`nucleon_binding/`)

Tier-2 #7; cites published TUFT+SM synthesis (`hqiv-tuft-sm-lagrangian-paper`, DOI [`10.5281/zenodo.20601215`](https://doi.org/10.5281/zenodo.20601215)) and published baryogenesis lock-in (`hqiv-baryogenesis-paper`, DOI [`10.5281/zenodo.20711255`](https://doi.org/10.5281/zenodo.20711255)).

- [x] Title and bib key aligned: *Binding Energy and the Weak Force from HQIV Composite-Trace Weights* (`hqiv-nucleon-binding-paper`).
- [x] Publication-chain abstract matches Tier-2 \#7 (after baryogenesis, before BBN).
- [x] Reproducer index at `nucleon_binding/scripts/README.md`; `authors.json` present.
- [x] Self-contained `nucleon_binding/scripts.zip` + `scripts/MANIFEST.sha256` (refresh: `python3 scripts/bundle_nucleon_binding_scripts.py`).
- [x] Lean support: `lake build paper_nucleon_binding` in [hqiv-lean](https://github.com/HQIV/hqiv-lean) ([PR #13](https://github.com/HQIV/hqiv-lean/pull/13)).
- [ ] Reader-first pass on body Lean identifiers (intro + scope improved; appendix index remains canonical).
- [x] Rebuild PDF locally (`latexmk -pdf hqiv_nucleon_binding_from_composite_trace.tex`; see `nucleon_binding/README.md`).
- [ ] Deposit on Zenodo (nucleon binding is **next** in Tier-2 queue).

### Queued — Lightcone v3 tightening (`lightcone_to_oshoracle/`)

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
- [x] Tier 1 #4: `thermodynamics_arrow/` published on Zenodo ([`10.5281/zenodo.20478826`](https://doi.org/10.5281/zenodo.20478826), 2026-05-31; `scripts.zip` on record). **Tier-1 quartet complete.**
- [x] Tier 2 #5 (combined): `tuft_sm_lagrangian/` published on Zenodo ([`10.5281/zenodo.20601215`](https://doi.org/10.5281/zenodo.20601215), v2 2026-06-08; `scripts.zip` on record). Lean support: [hqiv-lean PR #12](https://github.com/HQIV/hqiv-lean/pull/12) (`paper_tuft_sm_lagrangian` target).
- [x] Tier 2 #6: `baryogenesis_lockin/` published on Zenodo ([`10.5281/zenodo.20711255`](https://doi.org/10.5281/zenodo.20711255), v1 2026-06-16; `scripts.zip` on record).
- [ ] Tier 2 #7: publish `nucleon_binding/` (*Binding Energy and the Weak Force*; cites #5 and #6).
- [ ] Move `rapidity_so8_closure/` into `archive/`.
- [ ] Tier 2 remainder: `nucleon_binding/` → `bbn/`.
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
| `factor_search_formalization/`  | `hqiv_factor_search_formalization.tex`          | Lean formal proof note |
| `goldbach_so4_so2_delta/`       | `goldbach_so4_so2_delta.tex`                    | Lean formal proof note |
| `thermodynamics_arrow/`         | `hqiv_thermodynamics_and_arrow_of_time.tex`         | 1.4 (Zenodo) |
| `tuft_sm_lagrangian/`           | `hqiv_tuft_sm_lagrangian_synthesis.tex`             | 2.5 (Zenodo) |
| `baryogenesis_lockin/`          | `hqiv_baryogenesis_curvature_lockin.tex`            | 2.6 (Zenodo) |
| `nucleon_binding/`              | `hqiv_nucleon_binding_from_composite_trace.tex`     | 2.8  |
| `bbn/`                          | `hqiv_bbn_light_elements_from_network_weights.tex`  | 2.9  |
| `longitudinal_em_force/`        | `longitudinal_em_force_hqiv.tex`                    | 3.10 |
| `coronal_heating/`              | `hqiv_coronal_longitudinal_heating.tex`             | 3.11 |
| `omaxwell_fluid_chart/`         | `HQIV_OMaxwell_fluid_chart.tex`                     | 3.12 |
| `orbital_flyby/`                | `hqiv_accelerations_galaxy_evolution.tex` (+ `flyby_paper_table.tex`) | 3.13 |
| `tuft_topology_hqiv_bridge/`    | `hqiv_tuft_topology_discrete_continuous_bridge.tex` | working draft (Tier-2 topology companion) |
| `archive/lean_to_mass_spectrum/`| `hqiv_lean_from_combinatorics_to_mass_spectrum.tex` | archive (superseded by TUFT synthesis) |
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
- `\input{../include/shell_ontology_messaging.tex}` (TUFT hadron / mass-spectrum papers — **not** cosmology-only drafts)
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
