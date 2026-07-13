---
type: source
title: "Joint Beamforming, Power Control, and Trajectory Planning for NOMA-Based UAV Relaying System"
authors: ["Xiazhao Li", "Laixian Peng", "Haichao Wang", "Xingyue Yu", "Wendong Zhao", "Hai Wang"]
year: 2026
url: "https://doi.org/10.1109/TGCN.2026.3673110"
venue: "IEEE Transactions on Green Communications and Networking"
tags: [source, noma, uav-relay, amplify-and-forward, beamforming, power-control, trajectory-optimization, max-min-fairness, successive-convex-approximation]
related:
  - "[[noma-af-uav-relaying]]"
  - "[[imperfect-sic-residual-interference]]"
  - "[[noma]]"
  - "[[uav-mobile-relaying]]"
  - "[[uav-trajectory-control]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[fairness-metrics-in-mec]]"
  - "[[zeng-2016-throughput-relaying]]"
created: 2026-07-13
updated: 2026-07-13
---

# Joint Beamforming, Power Control, and Trajectory Planning for NOMA-Based UAV Relaying System

## Citation

Li, X., Peng, L., Wang, H., Yu, X., Zhao, W., & Wang, H. (2026). *Joint Beamforming, Power Control, and Trajectory Planning for NOMA-Based UAV Relaying System*. **IEEE Transactions on Green Communications and Networking**. DOI: 10.1109/TGCN.2026.3673110.

## TL;DR

Studies a two-hop downlink in which a multi-antenna UAV amplify-and-forward relay connects a base station to clustered NOMA users with no direct base-station-to-user link. It maximizes the minimum accumulated user rate by alternating communication-variable and trajectory subproblems, using SCA and semidefinite relaxation. The method converges monotonically for its surrogate updates but does not guarantee a global optimum or rank-one recovery.

## Problem

UAV relaying can improve blocked or distant downlinks, but trajectory, beamforming, NOMA power allocation, relay amplification, and residual SIC interference jointly determine each user's end-to-end rate. The paper targets max-min fairness over a finite flight horizon under mobility, airspace, QoS, NOMA-ordering, and average base-station/UAV power constraints.

## System model

- A base station with $N_T$ antennas communicates with $K$ users only through one $N_A$-antenna UAV amplify-and-forward relay; the direct links are unavailable.
- Users are grouped into $M$ spatial NOMA clusters by their proximity to randomly generated unitary directions.
- Air-to-ground links follow an elevation-dependent Rician model. The optimization assumes complete CSI and full Doppler compensation.
- [[imperfect-sic-residual-interference]] is represented by a fixed residual coefficient after cancellation.
- The decision variables are the finite-horizon UAV trajectory, transmit/receive beamforming, per-cluster NOMA power coefficients, UAV amplification power, and a max-min-rate epigraph variable.

## Method

The solver alternates between two blocks:

1. With trajectory fixed, optimize beamforming, NOMA power, and relay amplification using logarithmic slack variables, first-order convex surrogates, SCA, and semidefinite relaxation.
2. With communication variables fixed, optimize the UAV trajectory through local convex approximations while freezing the small-scale fading at the previous trajectory iterate.

The dropped rank-one constraints are handled by eigenvector extraction or Gaussian randomization. Consequently, the returned feasible point can depend on rank recovery. The paper establishes bounded monotonic behavior for the constructed surrogate sequence, not global optimality of the original joint problem.

## Key findings

- The proposed alternating procedure converges within about 40 iterations in the reported default simulation.
- Comparisons include fixed trajectory, zero-forcing, OMA/SDMA, MRC/MRT, fixed NOMA power coefficients, and relaxed-SDR variants. The figures report the joint design as the strongest max-min-rate method across the tested settings.
- Increasing base-station or relay power improves the minimum accumulated rate before interference and other constraints limit the gains; optimized movement places the UAV to balance the relay's two hops and disadvantaged users.
- The parse's Table II contains exact numerical entries, but its OCR does not preserve a reliable mapping between values, methods, and user counts. Those numbers are not reproduced as labeled results.

The default setup uses six users in three clusters, a 40 s horizon, 8 base-station antennas, 6 UAV antennas, 40 dBm base-station power, 37 dBm UAV power, and a residual-SIC coefficient of 0.01. Users lie within a 250 m-radius region centered at $[600,0,0]$.

## Limitations

The study uses one relay UAV, static users, no direct link, perfect CSI, and full Doppler compensation. Small-scale fading is frozen during each trajectory update, and the model omits UAV propulsion energy. Rank relaxation and Gaussian randomization do not ensure recovery of the original non-convex optimum. Results are simulation-based, and the broken table extraction prevents independent use of several tabulated values.

## Relation to the corpus

[[noma-af-uav-relaying]] specializes [[uav-mobile-relaying]] to a two-hop AF architecture whose user side uses [[noma]]. The source extends trajectory-power coupling beyond the decode/store/forward structure of [[zeng-2016-throughput-relaying]] by jointly controlling multi-antenna beamforming, relay gain, and NOMA coefficients. Its max-min objective connects to [[fairness-metrics-in-mec]], while its solver is an instance of [[alternating-optimization-sdr-sca]].

## Raw artifacts

- Parse: `raw/sources/Joint_Beamforming_Power_Control_and_Trajectory_Planning_for_NOMA-Based_UAV_Relaying_System/Joint_Beamforming_Power_Control_and_Trajectory_Planning_for_NOMA-Based_UAV_Relaying_System.md`
- Origin PDF: `raw/sources/Joint_Beamforming_Power_Control_and_Trajectory_Planning_for_NOMA-Based_UAV_Relaying_System/Joint_Beamforming_Power_Control_and_Trajectory_Planning_for_NOMA-Based_UAV_Relaying_System.pdf`
- Figures: `raw/sources/Joint_Beamforming_Power_Control_and_Trajectory_Planning_for_NOMA-Based_UAV_Relaying_System/images/`
