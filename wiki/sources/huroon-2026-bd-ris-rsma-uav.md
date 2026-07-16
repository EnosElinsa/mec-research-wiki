---
type: source
title: "Energy-Efficient Transmission Strategy for UAV-RIS 2.0 Assisted Communications Using Rate Splitting Multiple Access"
authors: ["Aamer Mohamed Huroon", "Yu-Chih Huang", "Li-Chun Wang"]
year: 2026
url: "https://doi.org/10.1109/TWC.2025.3617169"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), vol. 25, pp. 5246-5261"
modeling_card: required
tags: [source, beyond-diagonal-ris, rate-splitting-multiple-access, multi-uav, energy-efficiency, generalized-benders-decomposition, riemannian-optimization, trajectory-control]
related:
  - "[[beyond-diagonal-ris]]"
  - "[[rate-splitting-multiple-access]]"
  - "[[intelligent-reflecting-surface]]"
  - "[[mixed-integer-nonlinear-programming]]"
  - "[[fractional-programming-dinkelbach]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[uav-trajectory-control]]"
  - "[[rotary-wing-propulsion-energy-model]]"
  - "[[qin-2023-ris-uav-mec-ee]]"
  - "[[lin-2025-energy-effective-ris-multiuav-coverage]]"
created: 2026-07-13
updated: 2026-07-16
---

# Energy-Efficient Transmission Strategy for UAV-RIS 2.0 Assisted Communications Using Rate Splitting Multiple Access

## Citation

Huroon, A. M., Huang, Y.-C., & Wang, L.-C. (2026). *Energy-Efficient Transmission Strategy for UAV-RIS 2.0 Assisted Communications Using Rate Splitting Multiple Access*. **IEEE Transactions on Wireless Communications**, 25, 5246-5261. DOI: 10.1109/TWC.2025.3617169.

## TL;DR

Combines group-connected [[beyond-diagonal-ris|BD-RIS]] hardware with intra-group [[rate-splitting-multiple-access|RSMA]] in a multi-UAV downlink. An augmented GBD framework assigns RIS clusters, while BCD, SCA, and Riemannian updates optimize common rates, precoders, UAV motion, and non-diagonal scattering matrices for rate-per-total-power efficiency.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Multiple multi-antenna UAVs each serve one ground-user group through a building-mounted group-connected beyond-diagonal RIS. Orthogonal subcarrier portions separate UAV groups, while users within a group use one-layer rate-splitting multiple access. Direct and RIS-assisted links follow Rician channel models, and each assisted group is assigned one BD-RIS cluster.

**Problem & objective**: Problem (28) is a mixed-integer nonlinear fractional program that maximizes system energy efficiency, $\max \eta=R_{overall}/P_T$, over RIS-cluster assignment, RSMA transmission, BD-RIS scattering, and UAV motion.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| RIS-cluster assignment | $\mathcal T$ | integer or binary assignment | Allocate BD-RIS clusters to UAV groups |
| UAV precoders | $\mathbf W_g$ | complex continuous matrices | Common and private RSMA beamforming |
| Common-rate allocation | $\mathbf r_g$ | continuous, nonnegative | Split the decodable common rate among users |
| UAV trajectories | $\mathbf Q$ | continuous positions | Time-slotted multi-UAV paths |
| BD-RIS scattering | $\mathbf\Phi_g$ | complex manifold matrix | Non-diagonal cluster phase rotation and coupling |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1-C3 | BD-RIS clusters are assigned consistently to UAV groups |
| C4 | Every user can decode the group's common RSMA stream |
| C5 | Each user's common plus private rate meets its QoS target |
| C6 | Per-UAV transmit power remains within its limit |
| C7 | Each BD-RIS scattering block satisfies the group-connected hardware manifold |
| C8-C9 | UAV paths satisfy initial-return and maximum-displacement constraints |

**Algorithm**: Apply a quadratic transform to the rate-over-power objective, use generalized Benders decomposition to separate discrete cluster assignment in a MILP master from continuous primal variables, decompose the primal problem with block coordinate descent, update precoders, rates, and trajectories by SCA and scattering matrices by Riemannian conjugate gradient, then add Benders cuts and iterate the bounds until convergence.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Huroon et al. [x] studied energy-efficient transmission in a multi-UAV downlink that combines group-connected beyond-diagonal RIS hardware with rate-splitting multiple access. They formulated a mixed-integer nonlinear fractional program that maximizes aggregate rate per total transmit, UAV, and RIS power by jointly optimizing RIS-cluster allocation, common rates, precoders, UAV trajectories, and non-diagonal scattering matrices. A quadratic transform handles the fractional objective, and generalized Benders decomposition separates discrete cluster assignment from the continuous primal design. Within the primal loop, block coordinate descent and successive convex approximation update RSMA and trajectory variables, while Riemannian conjugate gradient updates the BD-RIS scattering matrices. Simulations report higher energy efficiency for BD-RIS with RSMA than the evaluated conventional-RIS, NOMA, fixed-UAV, and no-BD-RIS configurations.

## Problem

The discrete assignment of BD-RIS clusters to UAV groups is coupled with continuous beamforming, common-rate allocation, RIS configuration, and UAV trajectories. The paper seeks an energy-efficient design without treating the surface, mobility, or RSMA interference management as independent layers.

## System model

- Each multi-antenna UAV serves one ground-user group. Groups receive orthogonal subcarrier shares, while users within a group share the downlink through one-layer RSMA.
- A passive group-connected BD-RIS is fixed to a building facade. Its cells are partitioned into clusters; each assisted UAV group receives one cluster, while unassisted groups use direct links.
- Direct and RIS-assisted channels use Rician models. The negotiation and optimization assume perfect channel estimation and synchronization.
- Energy efficiency divides aggregate rate by transmit, UAV hovering/flying, and RIS controller/circuit power. Group-connected hardware uses more inter-cell circuit elements than a diagonal surface.

## Method

A quadratic transform handles the fractional objective. Generalized Benders decomposition keeps RIS-cluster assignment in a MILP master and continuous variables in a primal problem. Inside the primal loop, SCA updates RSMA precoders/common rates and trajectories, while Riemannian conjugate gradient updates the BD-RIS scattering matrices. A separate two-stage approximation first constructs a user-directed UAV path and then optimizes the surface for that fixed path.

## Key findings

- Across the fixed-UAV comparisons, BD-RIS with RSMA has the highest reported sum rate and energy efficiency; conventional RIS with RSMA, conventional RIS with NOMA, and RSMA without RIS follow in that order.
- The prose attributes a `4.2 bits/s/Hz` sum-rate gain to BD-RIS plus RSMA over RSMA without RIS, but its figure caption and discussion disagree on whether the sweep varies antenna count or BD-RIS cells.
- At eight UAV antennas, the paper reports SDMA reaching about `94%` of RSMA performance; RSMA remains highest across the antenna sweep.
- Joint UAV flight and optimized BD-RIS configuration outperform fixed-UAV and no-BD-RIS variants qualitatively in the trajectory experiments.

## Limitations / parse caveats

The study is simulation-only and assumes perfect CSI/synchronization, fixed user grouping, orthogonal inter-group spectrum, passive surface hardware, and fixed RIS and ground-user locations. Detailed mobility optimization and the two-stage route focus on UAV 1 rather than demonstrating full multi-UAV scalability. The parse corrupts several SINR and power equations, overloads `F`, alternates between complex-circle and Stiefel terminology, and labels a section global optimality before describing only a local result. It also contains editorial residue, a caption/prose conflict for Fig. 6, and a complexity envelope of `M <= 64` despite simulations at `M=80` and `100`.

## Relation to the corpus

The ground-mounted non-diagonal surface distinguishes this source from [[uav-mounted-ris]] studies. It extends the fixed-building RIS energy-efficiency line in [[qin-2023-ris-uav-mec-ee]] with cluster assignment, coupled scattering, and RSMA, while [[lin-2025-energy-effective-ris-multiuav-coverage]] provides a diagonal facade-RIS multi-UAV comparison.

## Raw artifacts

- Parse: `raw/sources/Energy-Efficient_Transmission_Strategy_for_UAV-RIS_2_0_Assisted_Communications_Using_Rate_Splitting_Multiple_Access/Energy-Efficient_Transmission_Strategy_for_UAV-RIS_2_0_Assisted_Communications_Using_Rate_Splitting_Multiple_Access.md`
- Origin PDF: `raw/sources/Energy-Efficient_Transmission_Strategy_for_UAV-RIS_2_0_Assisted_Communications_Using_Rate_Splitting_Multiple_Access/Energy-Efficient_Transmission_Strategy_for_UAV-RIS_2_0_Assisted_Communications_Using_Rate_Splitting_Multiple_Access.pdf`
- Figures: `raw/sources/Energy-Efficient_Transmission_Strategy_for_UAV-RIS_2_0_Assisted_Communications_Using_Rate_Splitting_Multiple_Access/images/`
