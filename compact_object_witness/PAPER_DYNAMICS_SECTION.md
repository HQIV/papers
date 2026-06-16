# Paper section: crust MHD equivalence and geometry-first predictions

**Use this file as the outline for the compact-object / pulsar dynamics section.**
It does **not** claim a new magnetic theory. It claims:

> We have a first-principles way to **organize the same Hall-MHD / resistive-MHD physics**
> around **ε-tipping layers** and the **spin axis**, yielding testable predictions for
> **mass/spin dependence** and **surface multipoles**.

Executable bundle: `python3 scripts/hqiv_compact_object_mass.py --paper-dynamics-outline`  
JSON: `data/compact_object_witnesses.json` → `paper_dynamics_section_bundle`

Related: [MHD_EQUIVALENCE_MAP.md](./MHD_EQUIVALENCE_MAP.md), [DYNAMICS_TARGET.md](./DYNAMICS_TARGET.md)

---

## 1. Opening framing (one paragraph for the paper)

Neutron-star magnetism in traditional work is implemented as **resistive and Hall MHD**
in a conducting crust, with conductivity **σ(T, B)**, turbulent **α** effects in proto-neutron
stars, and decades of calibration. HQIV does not replace that stack: it **names the same
equations** in the proved **O-Maxwell** action (`S_O`) plus **modified fluid / plasma closure**
(`HQIVFluidClosureScaffold`), with coefficients **η(ξ, ε)**, **ν_eddy**, and crust stress
discharge tied to the lattice (**α = 3/5**, **γ = 2/5**) and gravitational slot **ε**.
What HQIV adds is **geometry-first organization**: ε-tipping **composition layers**,
**spin-axis latitude belts**, and **τ_mis obliquity** that jointly source **surface multipoles**
without post-hoc offset hotspots. The section proves the **equation-level reduction**, then
states **where geometry adds predictive power** and **where coefficients still require
side-by-side calibration** with literature **σ**, Hall, and ohmic timescales.

---

## 2. Equation-level equivalence (prove the reduction)

Display **standard equations beside HQIV slot names** with explicit coefficient ID.
Suggested LaTeX layout: two-column table in the paper; full rows in
[MHD_EQUIVALENCE_MAP.md](./MHD_EQUIVALENCE_MAP.md).

### 2.1 Maxwell and sources

| Standard | HQIV slot | Lean |
|----------|-----------|------|
| Inhomogeneous Maxwell `∇×F = J` (chart) | `EL_O_general` → `F_divergence_sum − 4πJ_src` | `Hqiv.Physics.Action` |
| φ–field coupling on EM slot | `L_O_phi_coupling = α log(φ+1) ∑ (∇φ)·A` | `Action.L_O_phi_coupling` |

### 2.2 Resistive induction

| Standard | HQIV slot | Coefficient ID |
|----------|-----------|----------------|
| `∂B/∂t = ∇×(v×B) − ∇×(η∇×B)` | `inductionGrowthRateFromLt`; steady `steadyInductionFieldLt` | trad **η** ↔ **η_HQIV(ξ,ε) = γ release(ξ) G_eff(ε)** |
| `E = J/σ` (ohmic) | `ohmicAxialField J σ` | trad **σ(T,B)** ↔ **ξ** ladder + `ohmicAxialField` (`CoronalLongitudinalStress`) |
| `E_eff = E_Ohm + E_long` | `coronalEffectiveAxialField` | HQIV longitudinal channel **not** suppressed at high σ (proved limit) |

Python: `induction_resistivity_eta_from_environment`, `steady_induction_fields_si`.

### 2.3 Momentum and stress

| Standard | HQIV slot | Coefficient ID |
|----------|-----------|----------------|
| `ρ(∂v/∂t + v·∇v) = −∇p + (J×B)/c + ∇·τ` | `ρ f(a,φ) Dv/Dt = RHS`, `f = hqivFluidInertiaFactor` | Modified inertia from **φ** slot |
| `τ = τ_mol + τ_eddy` | `ν_total = ν_mol + hqivEddyViscosity` | F3 plasma closure |
| PNS buoyancy / **α** dynamo driving | `hqivVacuumMomentumSource3`; hot **ξ** → **η**, **ν_eddy** | trad **α** ↔ **ν_eddy + g_vac** (F2 chart) |
| Crust stress → torque | `crustMisalignTorqueFromStressDivergence` | `hqivLongitudinalStressForce3` discharge |

### 2.4 Hall MHD (reduction stated; vector discharge milestone)

| Standard | HQIV correspondence | Status |
|----------|---------------------|--------|
| `∂B/∂t ∋ (σ/2ne) ∇×((∇×B)×B)` | `rapidityNormalized_frozenFirstIndexJet` on EM transport | **Milestone:** explicit Hall benchmark |
| Plastic / elastic crust | Thin-shell `(h/R)²` + variational **σ_ij** extension | **Milestone:** elasticity variational |

**Paper sentence:** “HQIV reduces standard resistive MHD to named action slots; Hall and
plastic terms map to the same transport and stress discharge layers trad codes implement
numerically—we discharge coefficients rather than introduce alternate field dynamics.”

---

## 3. What HQIV adds structurally (geometry-first)

These are **differentiators**—predictions trad work often **bolts on afterward**.

| Structural addition | Mechanism | Witness / command |
|---------------------|-----------|-------------------|
| **ε-tipping layers** (nuclear → charmed → top) | Zone radii `r_top`, `r_charm` move with **ε**; charm retreat on spindown | `gradient_collapse_hypothesis`, `--spindown-charm-audit` |
| **Spin-axis latitude organization** | **ρ_pol**, **ε_spin(θ)**, axial **∇φ**, Coriolis gate **sin²θ\|cosθ\|** | `latitude_torsion_scan`, `surface_multipole_decomposition` |
| **Mid-latitude shear belt** | **ψ_shear**, **χ** peak ~45–70° colatitude → **l=2/l=3** | `--surface-multipole-audit` |
| **τ_mis obliquity** | Longitudinal stress vs **τ_align** (B_eff, B_align, enhanced) | `slip_torque_balance_for_star`, `aligning_torque_enhancement_factor` |
| **m=1 from τ_mis** | Tilted dipole: two longitude-offset spots | `tau_mis_m1_gate`, NICER J0030/J0740 overlay |
| **Spin-dependent multipole transition** | Moderate spin: Coriolis×shear (**l₂**); breakup: equatorial induction (**l₃**) | `high_spin_mass_tail_multipole_grid` |
| **Environment-aware η** | **T_out** with co-spin + CMB Doppler → **ξ** → **η(ξ,ε)** | `compact_object_effective_outside_temperature_K` |

**Paper sentence:** “Layer boundaries, colatitude channels, and obliquity are not separate
fitting parameters—they are discharge slots from the same ε-lattice and spin chart that
trad codes typically impose by hand.”

---

## 4. Where traditional work still has the edge (be honest)

Frame as **coefficient calibration** and **time-dependent vector evolution**, not missing physics.

| Trad strength | HQIV status | Paper framing |
|---------------|-------------|---------------|
| **σ(T, B)**, Hall coefficient, plastic yield, **τ_ohm ~ 10⁴–10⁶ yr** | **η(ξ,ε)** elegant but needs numeric compare across (T, B, ρ) | “Discharging coefficients against crust literature” |
| **3D / 2D axisymmetric** Hall-MHD over **10³–10⁶ yr** | Static / quasi-static multipole projections; **∂_t c_l**, **∂_t m₁** schematic | “Same PDEs; time integration milestone” |
| **Hall term** benchmarked in codes | Map to `rapidityNormalizedJet` sketched, not benchmarked | “Explicit Hall discharge next” |
| **Proto-NS αΩ dynamo** for magnetar **seed B** | Evolution + saturation (pairs at **B_cr**, **ν_eddy**); cold-crust witness seeds **B₀** | “Birth **B** as boundary; HQIV for subsequent geometry” |

Run: `--magnetic-field-gap-audit` for magnetar dex gap and channel fractions.

---

## 5. Differentiating predictions (testable)

Present as **correlations** trad models can fit but rarely predict from one geometry table.

### 5.1 Mass and spin → surface multipoles

- **Prediction:** **l₂/l₀**, **l₃/l₀**, centroid offset, and **m₁** fraction scale with
  **Ω/Ω_break** and mass (equatorial induction competes with Coriolis belt near breakup).
- **Evidence:** `high_spin_mass_tail_multipole_grid`; half-breakup **l₂/l₀ ~ 1.1**,
  breakup **l₃/l₀ ~ 1**, **m₁** weakens at breakup.
- **NICER:** J0030 centroid offset in literature range; J0740 non-antipodal offset >25°.
- **Command:** `--surface-multipole-audit`

### 5.2 Field obliquity (α_eq) vs surface geometry (multipoles)

**Two layers — do not conflate:**

| Layer | Witness field | Meaning |
|-------|---------------|---------|
| **Field–spin balance** | `alpha_equilibrium_aligning_enhanced_deg` | Misalignment between spin and dipole axis from τ_mis / τ_align |
| **Surface brightness** | m=1, centroid, l₂/l₃ | NICER/radio footprint from shear belt + `tau_mis_m1_gate` (tilt uses enhanced α) |

**α_eq regimes (enhanced aligning torque):**

| Regime | α_eq (enhanced) | Note |
|--------|-----------------|------|
| Ms pulsars, **catalog B** | ~90° | Dipole-formula B too weak; τ_mis dominates |
| 1.4 M☉, 640 Hz, **10¹² G** | ~71° | Canonical witness closes |
| 1.98 M☉ **breakup** | ~11° | Aligning torque wins |
| Crab (catalog B ~ 3.8×10¹² G) | ~24° | Rare high-B closure |

The model does **not** predict a fixed three-pole layout (90° + 23°). High α_eq at catalog B plus offset m=1 multipoles can *look* multi-polar observationally.

- **Evidence:** `pulsar_witness_comparison.json` (`closes_with_aligning_enhanced`, `alpha_equilibrium_canonical_b_deg`)
- **Command:** `hqiv_pulsar_witness_benchmark.py --json`

### 5.3 Obliquity ↔ multipole content

- **Prediction:** Higher ψ_shear and τ_mis/τ_align correlate with larger m₁ fraction (not fixed pole angles).
- **Evidence:** `compare_spindown_charm_to_pulsar_dataset`, NICER overlays
- **Command:** `--spindown-charm-pulsar-audit`, `--surface-multipole-audit`

### 5.4 Charm retreat and pair cascade in young, high-mass tail

- **Prediction:** Recent high-spin evolution shows **Δr_charm/R**, pair margin, and
  incremental **B_charm** / **B_pair** (small but correlated with **Ω/Ω_break**).
- **Evidence:** `spindown_charm_retreat_feedback`, breakup **B_charm ~ 3.7%** of **B_total**
- **Command:** `--spindown-charm-audit`, `--breakup-b-audit`

### 5.5 η(ξ,ε) vs literature σ and τ_ohm

- **Prediction:** HQIV η(ξ,ε) occupies the same induction PDE slot as trad η; μ₀σR² at stellar
  radius matches literature τ_ohm ~ 10⁴–10⁶ yr for σ ∈ [10⁷, 10⁹] S/m (order of magnitude).
- **Evidence:** `coefficient_calibration_witness` in `compact_object_witnesses.json`
- **Command:** `--eta-calibration-audit`

---

## 6. Coefficient discharge (implemented witness)

**Goal:** benchmark stars with η_HQIV(ξ,ε), schematic ∂B/∂t, and τ_ohm vs literature σ.

**Status:** `coefficient_calibration_witness()` — grid over (T, ε, σ); stellar-radius
τ_ohm sketch; bundled in `tradsci_mhd_equivalence_bridge`.

Run: `--eta-calibration-audit` or `--mhd-equivalence-audit` (includes calibration summary).

Remaining: match to specific Hall-MHD code output at same a_LT, R (vector milestone).

---

## 7. Recommended section order in the manuscript

1. **Framing** (§1 above)—same MHD, geometry-first organization.
2. **Equation equivalence table** (§2)—prove the reduction.
3. **ε-layers and spin-axis geometry** (§3)—structural additions.
4. **Obliquity and multipoles**—τ_mis, m=1, NICER overlays (figures from audit).
5. **Spin/mass tail**—multipole transition table (high-spin grid).
6. **Coefficient discharge** (§6)—honest calibration vs σ, Hall, τ_ohm.
7. **Predictions** (§5)—bulleted testable correlations.
8. **Limitations** (§4)—proto-NS seed **B**, time-dependent vector Hall-MHD integration.

---

## 8. Figure / table checklist

| Item | Source |
|------|--------|
| Trad ↔ HQIV equation table | §2, `MHD_EQUIVALENCE_MAP.md` |
| Colatitude channel cartoon (pole / belt / equator) | `solar_analogue_multipole_notes`, latitude division |
| NICER J0030 / J0740 comparison table | `--surface-multipole-audit` |
| High-mass spin tail multipole grid | `high_spin_mass_tail_multipole_grid` |
| B-channel fractions at breakup | `--breakup-b-audit` |
| η(ξ,ε) vs σ(T) table | `--eta-calibration-audit`, `coefficient_calibration_witness` |
| α_eq vs catalog B | `pulsar_witness_comparison.json` |
