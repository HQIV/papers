# Traditional MHD ↔ HQIV equation correspondence

**Thesis:** HQIV is not a rival phenomenology beside magnetohydrodynamics. It is a **composite
MHD stack** — inhomogeneous **O-Maxwell** (`S_O`) plus **modified fluid / plasma closure**
(`HQIVFluidClosureScaffold`) on the same lattice (α, γ, ε, ξ). Where traditional Hall-MHD
codes “win” today, the target is to show the **same PDE structure** with HQIV coefficients
and geometry slots filling the closure table — not to replace σ(T, B) with a single η fudge.

Paper chart: `papers/omaxwell_fluid_chart/HQIV_OMaxwell_fluid_chart.tex`  
Roadmap: `AGENTS/FLUID_OMAXWELL_ROADMAP.md`  
Executable map: `python3 scripts/hqiv_compact_object_mass.py --mhd-equivalence-audit`

## Layer 0 — Total action spine (what MHD is built on)

| Traditional | HQIV (proved naming) | Lean |
|-------------|----------------------|------|
| Maxwell + sources | `S_O(J, A, φ)` + `L_O_phi_coupling` | `Hqiv.Physics.Action` |
| Gravity / lapse | `S_HQVM_grav(φ, ρ)` | `Action`, `HQVMetric` |
| Inhomogeneous Maxwell RHS | `EL_O_general` → `∑ F − 4πJ` | `Action`, `ModifiedMaxwell` |

MHD in tradSci is **derived** from Maxwell + fluid + conductivity. HQIV records the same
derivation order explicitly (F3 milestone in `FLUID_OMAXWELL_ROADMAP.md`).

## Layer 1 — Resistive MHD (ideal + η)

| Traditional equation | HQIV slot | Status |
|----------------------|-----------|--------|
| `∂B/∂t = ∇×(v×B) − ∇×(η∇×B)` (resistive induction) | `inductionGrowthRateFromLt`: `∂B/∂t ~ η a_LT/R`; steady `B_LT = η(a_LT/a_grav)B_surf` | **Named** (`CompactObjectRotatingCrustScaffold`); full `∇×` vector PDE = **chart discharge** |
| `E + v×B = η∇×B` (or `J = σ(E + v×B)`) | `ohmicAxialField J σ = J/σ`; `coronalEffectiveAxialField = E_Ohm + E_HQIV` | **Proved** classical limit (`CoronalLongitudinalStress`) |
| `η` resistivity / `σ` conductivity | `inductionResistivityEta(ξ, ε) = γ release(ξ) G_eff(ε)` | **Proved** nonneg (`CompactObjectRotatingCrustScaffold`); ξ from `T_out`, ε from gravity |
| Frozen-in flux / ideal MHD | `frozenFirstIndexJet`, `rapidityNormalized_frozenFirstIndexJet` | **Chart transport** (`CovariantSolution`, `ContinuumOmaxwellClosure`) |

**Interpretation:** trad **`η`** and **`σ(T)`** are the **environment modulators** HQIV already
indexes through outside temperature **ξ** and gravitational slot **ε** (`NuclearOutsideTemperatureDynamics`).
The NS witness uses `induction_resistivity_eta_from_environment` (spin + CMB Doppler on `T_out`).

## Layer 2 — Momentum + Maxwell stress

| Traditional | HQIV | Status |
|-------------|------|--------|
| `ρ(∂v/∂t + v·∇v) = −∇p + (J×B)/c + ∇·τ_visc` | `ρ f(a,φ) Dv/Dt = RHS` with `f = a/(a+φ/6)` | **Defined** (`hqivFluidInertiaFactor`) |
| Turbulent / eddy stress | `τ = τ_mol + τ_eddy`, `ν_total = ν_mol + ν_eddy` | **F3 bookkeeping** (`PlasmaFluidClosureAssumptions`) |
| `ν_eddy` from turbulence | `hqivEddyViscosity(Θ, |δ̇θ′|, ℓ_coh, C)` | **Defined**; `ℓ_coh ↔ λ_D` bookkeeping |
| Buoyancy / driving (PNS convection) | `hqivVacuumMomentumSource3 = −(γ/6)∇(φ ∇δ̇θ′)` | **F2 chart hypothesis** (`OMaxwellFluidChartHypothesis`) |
| Longitudinal crust stress | `hqivLongitudinalStressTensor3`, `hqivLongitudinalStressForce3` | **Tensor slot**; torque discharge `crustMisalignTorqueFromStressDivergence` |

**Interpretation:** trad **Maxwell stress** sits in O-Maxwell EL; trad **viscous / turbulent**
terms map to F3 split. Proto-NS **convective driving** is the same slot family as
`g_vac` + hot **`ξ`** (high `η`, high `ν_eddy`) — not a separate ad hoc dynamo.

## Layer 3 — Hall MHD + crust elasticity (tradSci mature; HQIV discharge path)

| Traditional (NS crust codes) | HQIV correspondence | Milestone |
|------------------------------|---------------------|-----------|
| `∂B/∂t = ∇×(v×B − η∇×B) + (σ/2ne)∇×((∇×B)×B)` (Hall) | Hall drift as **rapid transport** on frozen jet: `rapidityNormalizedJet` scales discrete `∂F` packaging | Extend chart vector induction; match Hall term in `CovariantSolution` limit |
| `∂B/∂t` with **plastic / elastic** crust | `crustMisalignTorqueFromStressDivergence` + thin-shell `(h/R)²` screen | Couple crust elasticity `σ_ij` from variational shell (LAGRANGIAN_FAITHFULNESS path 1) |
| Ohmic decay `τ_ohm ~ 10⁴–10⁶ yr` | Same **`J/σ`** leg; `σ` from `ξ(T)` ladder + layered ε | **`coefficient_calibration_witness`** vs μ₀σR² (stellar radius) |
| Multipole diffusion / Hall drift competition | `surface_multipole_decomposition` + future `∂_t c_l` tied to `η` and Hall scale | `DYNAMICS_TARGET` milestone 2–3 |

HQIV does not deny Hall-MHD; it **defers the vector PDE** to the same slots trad codes fill
with σ, η, and elasticity — with **γ/α geometry** fixing the coefficient algebra.

## Layer 4 — Dynamo / strong initial B

| Traditional | HQIV same-dynamics view | Gap type |
|-------------|-------------------------|----------|
| αΩ turbulent dynamo (PNS) | Hot **`ξ`**, large **`ν_eddy`**, **`g_vac`**, **`J_O_plasma`** coherence → amplify **`B`** through induction loop | **Coefficient / calibration** (need PNS `T`, velocity, saturation) |
| Magnetar 10¹⁴–10¹⁵ G | Schwinger scale `B_cr ~ 4×10¹³ G` in witness; pair cascade at `B > B_cr` | **Seed + saturation** not missing Maxwell leg |
| Flux freezing in collapse | Ideal induction + rapidity-normalized transport | **Implementation** of vector `∇×` on crust chart |

Trad “wins” on **magnetar magnitude** because mature codes **tune α, turbulence, and σ(T,B)**
over decades. HQIV wins on **which slots must appear** (all are present) and **how they link**
to mass, spin, ε-layers, and NICER geometry.

## Unification table (paper-facing)

| Phenomenon | TradSci primary equation | HQIV primary slot | Same dynamics? |
|------------|--------------------------|-------------------|----------------|
| Coronal heating | `q̇ = nq E v_∥` | `coronalHeatingRateDensity` | **Yes** (proved limits) |
| Ohmic suppression at high σ | `E → J/σ → 0` | `ohmicAxialField_classical_limit` | **Yes** |
| LT / shear launch | MHD body force | `a_LT`, `compactObjectShearCoupling` | **Yes** (witness) |
| Induction from shear | `∂B/∂t ~ ∇×(v×B)` | `inductionGrowthRateFromLt` | **Same structure** (scalar discharge) |
| Obliquity torque | `τ ∝ B² R⁶ Ω³` (braking) vs crust stress | `τ_mis` vs `τ_align` (+ `B_align`, enhanced, J×B) | **Unified** in slip row |
| NICER multipoles | Hall-MHD + offset dipole fits | `surface_multipole_decomposition`, `τ_mis m=1` | **Competitive geometry** |
| Spindown → mass → charm | (usually ignored) | `quantify_spindown_charm_retreat_feedback` | **HQIV extra coupling** |

## What to claim in the paper

1. **HQIV ⊃ trad MHD structure** at the level of O-Maxwell + resistive closure + modified
   momentum (cite this map + `HQIV_OMaxwell_fluid_chart.tex`).
2. **Numerical competition** is against **Hall-MHD crust codes**, with HQIV supplying
   **ε( r )**, **Ω/Ω_break**, pole vs belt geometry, and **η(ξ, ε)** instead of free dipole offsets.
3. **Dynamics section goal:** display trad PDEs side-by-side with HQIV slot names; run
   coefficient-identified reduction (η ↔ γ release G_eff, σ ↔ ξ ladder) on one NS benchmark.

## Implementation checklist (before final draft)

- [x] `σ(ξ, ε)` / τ_ohm numeric compare — `coefficient_calibration_witness`, `--eta-calibration-audit`
- [ ] Vector induction discharge: `∇×(v×B − η∇×B)` on oblate crust chart (Python + Lean names).
- [ ] Hall term: explicit `τ_H(σ,B)` witness ↔ `rapidityNormalizedJet` coefficient.
- [ ] `∂_t B_l` / `∂_t m_1` tied to `dB_growth` and crust diffusion times.
- [ ] PNS birth boundary: high-`ξ` convective cell as **initial condition** on same PDEs.
