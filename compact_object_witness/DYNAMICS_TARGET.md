# Dynamics target before paper finalization

**Purpose:** honest scope boundary between HQIV crust / multipole witnesses and
mature **Hall-MHD + crust-evolution** codes — and how HQIV shows the **same equation
structure** as tradSci (see [MHD_EQUIVALENCE_MAP.md](./MHD_EQUIVALENCE_MAP.md)).

Run the quantitative gap witness:

```bash
python3 scripts/hqiv_compact_object_mass.py --magnetic-field-gap-audit
python3 scripts/hqiv_compact_object_mass.py --mhd-equivalence-audit
```

## HQIV is composite MHD (not a rival model)

Traditional magnetohydrodynamics is **Maxwell + fluid + σ**. HQIV records that stack in
`S_O` + `HQIVFluidClosureScaffold` with proved names for:

- **Ohmic leg:** `E = J/σ` (`CoronalLongitudinalStress.ohmicAxialField`)
- **Resistive induction:** `η(ξ,ε)` and `∂B/∂t ~ η a_LT/R` (`inductionResistivityEta`)
- **MHD momentum:** modified `ρ f Dv/Dt` + `ν_eddy` + Maxwell stress from O-Maxwell EL
- **Crust stress → torque:** `crustMisalignTorqueFromStressDivergence`

Where trad codes “win” numerically, the paper target is **coefficient-identified reduction**
(η ↔ γ release G_eff, σ ↔ ξ ladder, α ↔ ν_eddy + g_vac) on the **same PDEs**, not a
different physics class. See the layer tables in `MHD_EQUIVALENCE_MAP.md`.

Machine-readable: `compact_object_witnesses.json` → `tradsci_mhd_equivalence_bridge`.

## Verdict table (competition landscape)

| Aspect | Traditional (Hall-MHD + dynamo) | HQIV layered + multipole | Status |
|--------|--------------------------------|----------------------------|--------|
| Generating strong initial **B** | Strong (proto-NS convection, αΩ) | Weak (witness seeds **B₀**) | Trad. Sci. leads |
| Non-dipolar / offset geometry | Good but parameter-heavy | Competitive, geometry-first | HQIV competitive |
| Mass / spin dependence | Often post-hoc | Natural from ε, Ω/Ω_break | HQIV advantage |
| Obliquity + multipoles + activity | Fragmented across codes | Unified τ_mis / m=1 / l=2/l=3; **α_eq layer ≠ NICER surface** | HQIV advantage |
| Microphysical rigor (σ, Hall, plastic) | High | Schematic η, effective channels | Trad. Sci. leads |
| First-principles **geometry** (layered ε, poles) | Moderate | Strong (curvature slots) | HQIV advantage |
| Time evolution 10³–10⁶ yr | Mature Hall drift + ohmic + plastic | Not yet coupled back | Trad. Sci. leads |

## Quantitative gap (1.98 M☉ breakup, **B_surf = 10¹² G** witness default)

| Scale | Field (G) | vs witness **B_surf** |
|-------|-----------|------------------------|
| Witness dipole **B₀** | 10¹² | 0 dex (boundary data) |
| Proto-NS dynamo (typical) | 10¹²–10¹³ | 0–1 dex |
| Magnetar surface | 10¹⁴–10¹⁵ | **2–3 dex** above **B₀** |
| Schwinger **B_cr** | ~4×10¹³ | ~1.6 dex above **B₀** |

**Incremental channels at breakup** (fraction of **B_total**):

| Channel | Fraction | Role |
|---------|----------|------|
| **B_eff** (dipole seed) | ~99.99% | Aligning torque, NICER-scale geometry |
| **B_charm** (Λ_c ledger) | ~3.7% of **B_total** | Retreat / weak feedback (not seed) |
| **B_LT** (induction shear) | ~0.12% | Steady **η(a_LT/a_grav)B_surf** |
| **B_pair** (cascade) | ~4×10⁻⁵ | Minor torque lift |

Even at breakup, HQIV **does not** synthesize 10¹⁴–10¹⁵ G from crust induction +
pair + charm channels. The witness **evolves and complexifies** a seeded dipole.

The schematic growth law `∂B/∂t ~ η a_LT/R` is **not** a generation mechanism:
without saturation it would imply absurdly fast growth; the steady closure keeps
**B_LT** at O(10⁻³) **B_surf**. A credible birth field still requires proto-NS
dynamo or observational **B₀** input.

## What the paper should claim

1. **Boundary condition:** **B_surface** from spindown / catalog / NICER (or
   proto-NS dynamo as *external* seed, explicitly labeled).
2. **Geometry evolution:** colatitude division (poles vs Coriolis belt vs equator),
   **ψ_shear**, zonal **l=2/l=3**, **τ_mis m=1** (tilt from enhanced **α_eq**),
   obliquity balance vs catalog and canonical **B**.
3. **Mass / spin linkage:** **Ω/Ω_break**, ε-tipping layers, charm-zone retreat on
   spindown (HEP-grounded Λ_c channel as *perturbation*, not primary **B** source).
4. **Competition:** compare pulse-profile morphology to NICER (J0030, J0740), not
   to naïve centered dipole bags. Position relative to **Hall-MHD crust codes** as
   complementary geometry-first layer.

## What the paper should not claim (yet)

- Magnetar **10¹⁴–10¹⁵ G** **generation** from HQIV crust induction alone.
- Full **10³–10⁶ yr** multipole tracking without Hall + ohmic + plastic coupling.
- Microphysical equivalence to conductivity-resolved plasma models.

## Dynamics milestones before finalization

Ordered by dependency:

1. **Stress → current → B closure (partial):** `B_align`, charm-ledger aligning boost,
   J×B term; feed **B_total** into enhanced τ_align. Catalog B still misaligning-dominated.
2. **Crust diffusion witness:** `coefficient_calibration_witness` vs literature τ_ohm;
   Hall drift timescale vs ohmic (outer crust).
3. **Multipole time evolution:** track **l=2/l=3** and m=1 offset over diffusion
   times; compare to NICER offset evolution hypotheses.
4. **Optional birth slot:** explicit proto-NS αΩ dynamo as **separate** boundary
   layer (hot, convective PNS), not merged with cold-crust induction.
5. **Lean alignment:** variational crust stress discharge → torque (see
   `LAGRANGIAN_FAITHFULNESS_AUDIT.md` paths 1–3).

## Relation to other witnesses

| Witness | File / command | Dynamics role |
|---------|----------------|---------------|
| Multipole + NICER overlay | `--surface-multipole-audit` | Static geometry comparison |
| B channels at breakup | `--breakup-b-audit` | Incremental **B** fractions |
| Spindown → charm retreat | `--spindown-charm-audit` | Mass loss → **B** perturbation |
| η vs σ calibration | `--eta-calibration-audit` | Coefficient discharge table |
| Pulsar α_eq overlay | `hqiv_pulsar_witness_benchmark.py --json` | Field obliquity vs catalog |
| Lagrangian faithfulness | `hqiv_lagrangian_faithfulness_audit.py --json` | Proved vs schematic slots |

## References (traditional baseline)

Hall-MHD crust evolution, ohmic decay, and plastic flow in NS magnetospheres are
the mature comparison class—not uniform magnetized spheres. Cite standard pulsar
magnetic-field reviews and crust conductivity work in `papers/references.bib` when
the dynamics section is written.
