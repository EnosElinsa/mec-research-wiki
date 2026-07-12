---
type: source
title: "Energy-Efficient Transmission Strategy for UAV-RIS 2.0 Assisted Communications Using Rate Splitting Multiple Access"
authors: ["Aamer Mohamed Huroon", "Yu-Chih Huang", "Li-Chun Wang"]
year: 2026
url: "https://doi.org/10.1109/TWC.2025.3617169"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), vol. 25, pp. 5246-5261"
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
updated: 2026-07-13
---

# Energy-Efficient Transmission Strategy for UAV-RIS 2.0 Assisted Communications Using Rate Splitting Multiple Access

## Citation

Huroon, A. M., Huang, Y.-C., & Wang, L.-C. (2026). *Energy-Efficient Transmission Strategy for UAV-RIS 2.0 Assisted Communications Using Rate Splitting Multiple Access*. **IEEE Transactions on Wireless Communications**, 25, 5246-5261. DOI: 10.1109/TWC.2025.3617169.

## TL;DR

Combines group-connected [[beyond-diagonal-ris|BD-RIS]] hardware with intra-group [[rate-splitting-multiple-access|RSMA]] in a multi-UAV downlink. An augmented GBD framework assigns RIS clusters, while BCD, SCA, and Riemannian updates optimize common rates, precoders, UAV motion, and non-diagonal scattering matrices for rate-per-total-power efficiency.

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
