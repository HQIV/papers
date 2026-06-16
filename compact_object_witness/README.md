# Compact-object and pulsar witness data (conjectural)

Witness scripts compare HQIV curvature slots, slip-torque balance, surface
multipoles, and pulsar-catalog spindown parameters. **Not** a published Tier paper;
bundles are cited from nucleon-binding and orbital-flyby notes as comparison-layer
readouts.

**Paper:** `hqiv_compact_object_crust_mhd_equivalence.tex` — composite MHD equivalence
(same equations as trad Hall-MHD), geometry-first multipoles, honest scope.

## Quick reproduce (paper data)

```bash
papers/compact_object_witness/regenerate_data.sh
```

Or step by step:

```bash
python3 scripts/hqiv_compact_object_mass.py --json
python3 scripts/hqiv_pulsar_witness_benchmark.py --json
python3 scripts/hqiv_lagrangian_faithfulness_audit.py --json
```

Build PDF:

```bash
cd papers/compact_object_witness && pdflatex hqiv_compact_object_crust_mhd_equivalence.tex
```

## Data bundles (repo root)

| File | Generator | Description |
|------|-----------|-------------|
| `data/compact_object_witnesses.json` | `hqiv_compact_object_mass.py --json` | Mass ceiling, slip torque, MHD bridge, η calibration, NICER multipoles |
| `data/pulsar_catalog.json` | `hqiv_pulsar_witness_benchmark.py --refresh-catalog` | ATNF spindown subset (XAO mirror CSV) |
| `data/pulsar_mass_measurements.json` | hand-curated | NICER + Shapiro-delay masses |
| `data/pulsar_witness_comparison.json` | `hqiv_pulsar_witness_benchmark.py --json` | Per-pulsar α_eq (B_eff + aligning enhanced) |
| `data/lagrangian_faithfulness_audit.json` | `hqiv_lagrangian_faithfulness_audit.py --json` | Lean ↔ Python slot alignment |

## Lean modules

| Module | Role |
|--------|------|
| `Hqiv.Physics.CompactObjectRotatingCrustScaffold` | Variational τ_mis, η(ξ,ε), induction discharges |
| `Hqiv.Physics.CompactObjectMhdEquivalenceScaffold` | Trad MHD ↔ HQIV reduction + honesty ledger |

## CLI audits (paper sections)

| Command | Paper section |
|---------|----------------|
| `--paper-dynamics-outline` | Full bundle + NICER summary |
| `--mhd-equivalence-audit` | Equation correspondence table |
| `--eta-calibration-audit` | η(ξ,ε) vs literature σ, τ_ohm sketch |
| `--magnetic-field-gap-audit` | Magnetar B gap, channel fractions |
| `--surface-multipole-audit` | l=2/l=3, m=1, J0030/J0740 overlays |
| `--breakup-b-audit` | B_charm / B_pair fractions at breakup |
| `--spindown-charm-audit` | Charm retreat feedback |
| `--spindown-charm-pulsar-audit` | Catalog overlay |

## What we claim (current witness)

1. **Same MHD stack** — resistive induction, ohmic leg, modified momentum; proved naming in Lean.
2. **Geometry-first** — ε layers, colatitude belts, τ_mis → multipoles, m=1 tilt.
3. **Coefficient discharge** — `coefficient_calibration_witness` maps η(ξ,ε) and μ₀σR² to literature τ_ohm band.
4. **Aligning torque** — `B_align`, charm-ledger boost, minimal J×B; `alpha_equilibrium_aligning_enhanced_deg`.

## What we do **not** claim

- Magnetar 10¹⁴–10¹⁵ G **generation** from cold crust alone (**B₀** is boundary data).
- Stable three-pole geometry (90° + 23°); high α_eq at catalog B is **field–spin misalignment**, separate from NICER surface brightness pattern.
- Full 10³–10⁶ yr vector Hall-MHD integration (milestone).

### Obliquity readout (important)

| Layer | Quantity | Typical ms (catalog B) |
|-------|----------|------------------------|
| **Field torque balance** | `alpha_equilibrium_aligning_enhanced_deg` | → 90° (τ_mis wins) |
| **Canonical witness B** | 1.4 M☉, 640 Hz, 10¹² G | ~71° |
| **Breakup** | 1.98 M☉, Ω/Ω_break → 1 | ~11° (aligning wins) |
| **NICER geometry** | m=1, centroid offset | `tau_mis_m1_gate` + enhanced α tilt |

## Manuscript outlines

| Doc | Content |
|-----|---------|
| [PAPER_DYNAMICS_SECTION.md](./PAPER_DYNAMICS_SECTION.md) | Section order, tables, predictions |
| [MHD_EQUIVALENCE_MAP.md](./MHD_EQUIVALENCE_MAP.md) | Trad ↔ HQIV equation map |
| [DYNAMICS_TARGET.md](./DYNAMICS_TARGET.md) | Competition verdict, milestones |
| [LAGRANGIAN_FAITHFULNESS_AUDIT.md](./LAGRANGIAN_FAITHFULNESS_AUDIT.md) | Proved vs hypothesis slots |

## External catalogs (`papers/references.bib`)

- ATNF Pulsar Catalogue — `atnf_psrcat`
- XAO IVOA mirror — `xao_atnf_pulsar_mirror`
- NICER — `nicer_psr0030_miller2019`, `nicer_psr0740_riley2021`, `rutherford2024_msp_masses`
- Shapiro masses — `freire2012_shapiro`, `antoniadis2013_ns_max`, `crombie2020_j0740`
