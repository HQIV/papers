# Reproducer scripts — Nucleon binding (Tier-2 #7)

Self-contained bundle for Zenodo upload (`scripts.zip` alongside the paper PDF).
Mirrors the entry scripts and `hqiv_*` dependency closure from the repository
root, plus the `hqiv_lab` package.

**Checksums:** `MANIFEST.sha256` (SHA-256 of every file in this folder).

**Regenerate** (from HQIV-LEAN repository root):

```bash
python3 scripts/bundle_nucleon_binding_scripts.py
```

This refreshes `papers/nucleon_binding/scripts/`, rewrites `MANIFEST.sha256`, and
rebuilds `papers/nucleon_binding/scripts.zip`.

## Entry scripts (paper-cited)

| Script | Reproduces | Output |
| --- | --- | --- |
| `hqiv_isotope_stability_halflife.py` | Free-neutron and isotope half-life readouts; outside $T(\xi)$ + gravity stack | `data/isotope_stability_halflife.json` (when run from repo root) |
| `hqiv_dynamic_beta_isotope.py` | Three-ledger $\beta$ channel chart | `data/dynamic_beta_isotope_chart.json` |
| `hqiv_isotope_pdg_benchmark.py` | Light-panel mass benchmark; curvature imprint control | `data/isotope_pdg_benchmark.json` |
| `hqiv_nuclear_outside_temperature_dynamics.py` | Outside temperature and gravity binding modulator | integrator witness block |
| `hqiv_bond_state_network.py` | Molecular bond-state network; Fano/Hopf bridge | bond-state chart |
| `hqiv_nuclear_caustic_binding.py` | Caustic hierarchy (sphere pair, barbell torus, tetrahedral closure) | caustic witness |
| `hqiv_nuclear_inside_outside_binding.py` | Inside/outside nuclear binding ledger | binding witness |
| `hqiv_dynamic_nucleon_pn.py` | Dynamic p/n mass gap readout | PN witness |
| `hqiv_phase_geometry_density.py` | Condensed-phase $\rho_{\mathrm{curv}}$ bridge via `hqiv_lab` | phase-density witnesses |
| `hqiv_thermodynamic_phase_from_tp.py` | $(T,P)\rightarrow$ derived phase readout | bulk phase witnesses |
| `hqiv_phase_material_response.py` | $n$, $k_{\mathrm{th}}$, $C_p$, $\eta$, $\Delta n$ | material-response chart |
| `hqiv_homogeneous_curvature_feedback.py` | Optional $B_{\mathrm{hom}}+\delta B$ self-consistent demo | chart path |
| `hqiv_bbn_integrator.py` | Faithful BBN integrator witness | `data/bbn_integrator.json` |
| `hqiv_bbn_condition_decay.py` | Condition-dependent decay table | companion to integrator |
| `hqiv_bbn_paper_tables.py` | Paper decomposition / $\eta$ sweep | `data/bbn_paper_tables.json` |
| `hqiv_integrator_lean_audit.py` | Integrator $\leftrightarrow$ Lean audit | `data/integrator_lean_audit.json` |
| `test_hqiv_phase_material_response.py` | H$_2$O ice/liquid response unit checks | `unittest` |
| `hqiv_lab/` | Derived allotropes, unit cells, `hqiv-lab` CLI | install via `pip install -e .` |

Additional `hqiv_*.py` files in this folder are **dependency modules** imported by
the entry scripts above.

**Witness JSON** (frozen outputs under `data/`):

| File | Source script |
| --- | --- |
| `data/isotope_pdg_benchmark.json` | `hqiv_isotope_pdg_benchmark.py` |
| `data/isotope_stability_halflife.json` | `hqiv_isotope_stability_halflife.py` |
| `data/dynamic_beta_isotope_chart.json` | `hqiv_dynamic_beta_isotope.py` |
| `data/nucleon_binding_integrator.json` | `hqiv_nucleon_binding_integrator.py` |
| `data/bbn_integrator.json` | `hqiv_bbn_integrator.py` |
| `data/bbn_paper_tables.json` | `hqiv_bbn_paper_tables.py` |
| `data/integrator_lean_audit.json` | `hqiv_integrator_lean_audit.py` |

## Quick start (from this directory)

```bash
pip install -e .
hqiv-lab H2O
hqiv-lab CH4 --json
python3 hqiv_isotope_pdg_benchmark.py --qualify-em-tipping --lab-temperature-K 300
python3 hqiv_isotope_stability_halflife.py --A 1 --Z 0 \
  --qualify-em-tipping --lab-temperature-K 300 --gravity-stack full
python3 hqiv_dynamic_beta_isotope.py
python3 -m unittest test_hqiv_phase_material_response.py
```

When running from the full repository, use `scripts/` paths instead and write JSON
under `data/` as documented in the paper appendix.

## Lean build target

Machine-checked proofs for this paper build under Lake target
`paper_nucleon_binding` in [HQIV/hqiv-lean](https://github.com/HQIV/hqiv-lean):

```bash
lake build paper_nucleon_binding
```

Regenerate the Lake `globs` list:

```bash
python3 scripts/paper_nucleon_binding_globs.py
```

## Inputs and comparison layer

- Proton lock-in anchor $938.272\,\mathrm{MeV}$ is a lapse-readout comparison target only.
- Tabulated isotope masses and reference half-lives appear in witness JSON as comparison rows, not fit inputs.
- Upstream mass ladder: `hqiv-tuft-sm-lagrangian-paper` (Zenodo [`10.5281/zenodo.20601215`](https://doi.org/10.5281/zenodo.20601215)).

## Citation

Steven Ettinger Jr., *Binding Energy and the Weak Force from HQIV Composite-Trace Weights* (2026). Bib key `hqiv-nucleon-binding-paper` in `papers/references.bib`. Zenodo [`10.5281/zenodo.20711453`](https://doi.org/10.5281/zenodo.20711453); cite the record and this supplementary `scripts.zip` on the same DOI.
