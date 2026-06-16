# Lagrangian faithfulness audit (compact-object / pulsar witnesses)

**Purpose:** map each witness formula to its Lean source and label gaps that explain
why pulsar comparison shows misaligning-dominated α_eq while the programme remains
“promising but not quite right.”

Run `python3 scripts/hqiv_lagrangian_faithfulness_audit.py --json` for the machine
readable version (`data/lagrangian_faithfulness_audit.json`).

## Total action spine (proved discrete cell)

From `Hqiv.Physics.Action` and `ContinuumOmaxwellClosure`:

\[
S_{\mathrm{total}} = S_O(J_{\mathrm{src}}, A, \phi) + S_{\mathrm{HQVM\,grav}}(\phi, \rho_m, \rho_r)
\]

- **O-Maxwell:** `L_O_kinetic + 4π J·A + L_O_phi_coupling` with
  `L_O_phi = α log(φ+1) ∑_ν (∇φ)_ν A_{0ν}` (EM channel `a=0` only).
- **Gravity:** `S_HQVM_grav = (3−γ)φ² − 8π G_eff(φ)(ρ_m+ρ_r)`; `S_grav=0` ↔ Friedmann constraint.

**Faithful for:** lattice constants α, γ; φ–gravity coupling in the same action;
inhomogeneous Maxwell with φ source on the abelian slot.

**Not in this action:** rotating-fluid anisotropic stress, crust elasticity, general
relativistic magnetosphere, or Lense–Thirring terms as variational derivatives.

## Variational crust path (2026-06 build-out)

Lean module `Hqiv.Physics.CompactObjectRotatingCrustScaffold` names:

- `crustMisalignTorqueFromStressDivergence` — thin-shell discharge of
  `hqivLongitudinalStressForce3` with shear coupling `χ = a_LT a_∥ / a_grav²`
- `inductionResistivityEta` — `η = γ × release(ξ) × G_eff(ε)` from
  `NuclearOutsideTemperatureDynamics`
- `compactObjectEffectiveOutsideTemperatureK` — spin/CMB Doppler boost on `T_out`
- `steadyInductionFieldLt` / `steadyInductionFieldLong` / `inductionGrowthRateFromLt`

Python mirrors: `crust_misalign_torque_from_stress_div_si`,
`induction_resistivity_eta_from_environment`, `steady_induction_fields_si`,
`compact_object_effective_outside_temperature_K` (spin + CMB Doppler on `T_out`).

**Outside temperature vs spin:** fast rotators book higher `T_out` via co-spin
`β_spin = v/c` and CMB Doppler `√(1+β_combined)/(1−β_combined)` with
`β_combined = β_spin + v_CMB/c` (same additive kinetic slot as the lab dipole).
Near breakup, CMB bathing flux dominates over static photosphere `T_surf`.

## Slot-by-slot witness map

| Witness quantity | Lean / paper slot | Faithfulness | Gap |
|------------------|-------------------|--------------|-----|
| `ε = GM/(Rc²)` | `NuclearOutsideTemperatureDynamics`, outside gravity witness | **Proved readout** | Static spherical exterior; no spin |
| `G_eff mod = 1+γ((1+ε)^α−1)` | `outsideGravityGeffModulator` | **Proved** | Applied as scalar modulator, not full `G_eff(φ)` from `S_grav` with rotating ρ |
| `ψ_shear = atan2(a_LT, a_∥^lin)` | Flyby repartition + `HQIVFluidClosureScaffold` longitudinal tensor | **Hypothesis bridge** | LT split `λ=γ sin²θ ρ_pol` is Python orbit hypothesis; not EL of `S_total` |
| `a_∥^lin = κ_L log(φ+1)|ẑ·∇φ|` | `hqivLongitudinalStressTensor3`, coronal/conductor papers | **Partial** | κ_L stress proved as tensor slot; NS crust + induction not in variational NS action |
| `a_∥^nl` with `log(6 a_grav ε+1)` | `OrbitalFlybyScaffold` + `φ_eff = φ + 6aε` inertia | **Hypothesis** | Boost is inertia-screen bookkeeping, not extra term in `L_O_phi_coupling` |
| `τ_mis ∝ χ sin²θ (h/R)²…` | — | **Witness only** | Crust shell integral with screening; not derived from action |
| `τ_align ∝ B² R⁶ Ω³/c³` | Standard pulsar spindown | **External** | Comparison physics; not HQIV Lagrangian |
| `B_eff = B_surf min(1,δB/B)` | — | **Witness heuristic** | Couples shear to aligning torque; no Lean EL |
| `B_LT = η (a_LT/a_grav) B_surf` | Induction schematic | **Schematic** | `∂B/∂t ~ η a_LT/R` not coupled back into `L_O_kinetic` |
| `B_align`, enhanced τ_align, J×B` | Charm ledger + induction channels | **Hypothesis bridge** | Closes canonical ms at 10¹² G (~71° α_eq); catalog B still → 90° |
| `η vs σ`, τ_ohm ~ μ₀σR²` | `coefficient_calibration_witness` | **Coefficient discharge** | HQIV η dimensionless; trad η_MHD = 1/(μ₀σ) in m²/s |
| `B dipole from P, Ṗ` | Spindown literature | **External** | Catalog comparison only |

## Field obliquity (α_eq) vs NICER surface geometry

- **α_eq** from slip-torque balance = misalignment between **spin and dipole axis** (field ledger).
- **m=1 / centroid** from `tau_mis_m1_gate` = **surface brightness** pattern (uses enhanced α for tilt).
- Catalog ms pulsars: α_eq → 90° at measured B; NICER offsets are not fixed pole angles at 90° and 23°.

## Why pulsar α_eq → 90° is consistent with gaps

1. **Aligning torque** uses dipole B from spindown (~10⁸ G for ms pulsars). Enhanced
   closure (`B_align`, charm ledger, J×B) closes the **canonical** witness at 10¹² G (~71°)
   but not the bulk catalog at measured B.
2. **τ_mis** uses a thin crust layer and χ at mid-latitude — not the same as
   differentiating an anisotropic stress term in `S_total`.
3. **No obliquity angle in the action** — α_eq is a post-hoc balance with standard
   magnetic braking, not a prediction from `δS/δB = 0` on a rotating patch.

## What is still promising

- **Same lattice** (α, γ, `c_rindler_shared = γ/2`) links NS mass ceiling, outside
  `G_eff`, and flyby screens — internally consistent.
- **ψ_shear** peaks at mid-latitude (~0.1–1°) with ms pulsars near half breakup
  (J1748-2446ad, Ω/Ω_break ≈ 0.49) — right morphology for wave driving.
- **Split channels** (ψ_shear vs ψ_long) match distinct Lean slots (fluid LT vs
  φ_eff longitudinal / conductor O-Maxwell).

## Paths to tighten (ordered)

1. **Variational crust slot:** add anisotropic stress `σ_ij` to
   `HQIVFluidClosureScaffold` RANS RHS and derive τ_mis from `∫ r_i (σ_jk ε_jk) dV`
   instead of χ screening.
2. **Unify φ_eff:** either move `6aε` into `L_O_phi_coupling` as explicit
   `φ_eff` in the action, or forbid using it for shear launch (already split in witness).
3. **Magnetospheric B:** derive `B_eff` from induction EL with resistivity η(φ, T)
   from `NuclearOutsideTemperatureDynamics`, not `min(1,δB/B)` alone.
4. **Lean bundle:** extend `OrbitalFlybyScaffold` with rotating-body chart hypotheses
   (currently “Python only” per module header).

## References

Data and catalogs: `papers/references.bib` keys `atnf_psrcat`, `xao_atnf_pulsar_mirror`,
`hqiv-pulsar-witness-data`, `hqiv-compact-object-witness-data`, NICER/Shapiro entries.
