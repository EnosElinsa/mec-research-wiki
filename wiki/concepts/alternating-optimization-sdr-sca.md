---
type: concept
title: "Alternating Optimization with SDR and SCA"
tags: [optimization, alternating-optimization, sdr, sca, non-convex, classical-solver]
related:
  - "[[liu-2025-aoi-iscc-five-stage]]"
  - "[[lyu-2023-isac-maneuver-beamforming]]"
  - "[[li-2026-noma-uav-relay-planning]]"
  - "[[deng-2025-covert-isac-trajectory]]"
  - "[[fractional-programming-dinkelbach]]"
  - "[[lyapunov-optimization]]"
  - "[[benaya-2025-aerial-isac-haps]]"
  - "[[mohammadi-2026-star-ris-uav-mec-noma]]"
  - "[[xiao-2025-star-ris-bidirectional-uav-mec]]"
  - "[[wang-2026-secure-lae-uav-scheduling]]"
  - "[[li-2026-isac-vec-beamforming-deployment]]"
  - "[[wu-2026-secure-split-offloading-ci]]"
  - "[[you-2019-rician-uav-data-harvesting]]"
  - "[[lee-2026-uav-delivery-time-energy]]"
  - "[[li-2026-control-based-uav-isac]]"
  - "[[cui-2026-aris-v2x-icac]]"
  - "[[hosseini-2026-aoi-covert-uav]]"
  - "[[liu-2026-spherical-t-ris-bs]]"
  - "[[zhang-2025-cooperative-anti-uav-isac]]"
  - "[[cooperative-isac-transceiver-beamforming]]"
  - "[[fan-2026-hap-uav-iort-oee]]"
  - "[[zhang-2022-uav-relay-substitution]]"
  - "[[meng-2026-uav-isac-corrections]]"
  - "[[ahmed-2026-noma-irs-vehicular]]"
  - "[[fixed-point-irs-passive-beamforming]]"
  - "[[hu-2026-segmented-irs-cpn]]"
  - "[[huroon-2026-bd-ris-rsma-uav]]"
  - "[[fu-2026-uav-fl-user-grouping]]"
  - "[[mihertie-2026-aerial-irs-rsma-ee]]"
  - "[[xie-2023-wireless-powered-short-packet-uav]]"
  - "[[zhang-2026-air-sea-isac-inspection]]"
  - "[[wang-2026-robust-anti-uav-isac]]"
  - "[[wang-2025-cellular-uav-cooperative-detection]]"
  - "[[bi-traveling-salesman-problem-with-neighborhoods]]"
created: 2026-05-29
updated: 2026-07-13
---

# Alternating Optimization with SDR and SCA

A classical recipe for solving non-convex MEC and ISAC problems with multiple coupled blocks (e.g. transmit beamforming, receive beamforming, trajectory, power). The recipe:

1. **Alternating Optimization (AO).** Hold all blocks fixed except one; solve that block; rotate. Repeat until convergence (typically a few iterations).
2. Inside each block, the subproblem is still non-convex. Two go-to relaxations:
   - **Semi-Definite Relaxation (SDR).** Lift a quadratic-form variable into a positive-semidefinite matrix, drop the rank-1 constraint, solve the resulting SDP, then recover a rank-1 solution via Gaussian randomization.
   - **Successive Convex Approximation (SCA).** Replace the non-convex constraint/objective with a convex upper bound at each iteration (e.g. first-order Taylor of a concave term, or DC-programming linearization).

AO converges to a stationary point but not necessarily the global optimum; in practice it's robust enough for ISAC, beamforming, and trajectory problems. See [[benaya-2025-aerial-isac-haps]] for a four-block AO instance.

This stack is the **non-DRL** counterpoint to the j-PPO / DDPG / SAC backbone that dominates the wiki — useful when the problem has clean convex structure within each block.

[[zhang-2025-cooperative-anti-uav-isac]] alternates closed-form receive beamforming with SCA/Dinkelbach transmit updates for [[cooperative-isac-transceiver-beamforming]]. Its distributed counterpart uses primal decomposition to preserve the same modeled KKT target without collecting global CSI centrally.

[[mohammadi-2026-star-ris-uav-mec-noma]] uses the same decomposition style without SDR as the headline: bit allocation, transmit power, STAR-RIS phase shifts, and UAV trajectory are separated into subproblems, then handled with SCA or closed-form MRT-style phase updates inside a BCD loop. [[xiao-2025-star-ris-bidirectional-uav-mec]] uses Dinkelbach plus SCA inside BCD for STAR-RIS bidirectional offloading. [[wang-2026-secure-lae-uav-scheduling]] decomposes secrecy-energy-efficiency maximization into scheduling, power, and trajectory/velocity subproblems, using penalty updates, SCA, and Dinkelbach-driven iteration. [[li-2026-isac-vec-beamforming-deployment]] uses a similar block split for ISAC-enhanced VEC: swarm search handles UAV deployment, while SCA and first-order Taylor expansion handle beamforming. [[li-2026-control-based-uav-isac]] keeps the SCA/SDR beamforming block but replaces waypoint-only trajectory optimization with control-parameterized 3-DoF/6-DoF UAV dynamics. [[hosseini-2026-aoi-covert-uav]] applies the same AO family to covert AoI: LP handles AoI, SCA handles trajectory, and SDR/SCA handles beamforming. [[cui-2026-aris-v2x-icac]] uses BCD plus first-order Taylor convexification for ARIS-aided V2X communication/computation. [[wu-2026-secure-split-offloading-ci]] uses AO with SCA trajectory subproblems and a discrete WOA subproblem for early-exit and DNN-partition choices. [[you-2019-rician-uav-data-harvesting]] applies BCD/SCA to scheduling plus horizontal/vertical trajectory under outage-aware Rician fading, while [[lee-2026-uav-delivery-time-energy]] uses SCA and a penalty convex-concave procedure for pickup/drop-off delivery trajectory optimization.

[[fan-2026-hap-uav-iort-oee]] adds a Dinkelbach/BCD/SCA stack for HAP-UAV IoRT energy efficiency. [[zhang-2022-uav-relay-substitution]] uses block coordinate ascent plus SCA, without SDR, to alternate relay trajectories and powers under overlapping UAV substitution.

[[meng-2026-uav-isac-corrections]] supplies a cautionary SCA case: an omitted auxiliary-variable transformation and first-order logarithmic bound, rather than a claimed negative-definite Hessian, are what make the corrected periodic UAV-ISAC rate subproblem convex.

Three cooperative sensing designs add distinct decompositions: [[zhang-2026-air-sea-isac-inspection]] alternates hover-point beamforming and current-aware USV motion after a discrete route initialization; [[wang-2026-robust-anti-uav-isac]] combines lifted beamformers, robust LMIs, penalty-SCA role assignment, and trajectory convexification; and [[wang-2025-cellular-uav-cooperative-detection]] alternates sensing/communication beamforming with UAV trajectory updates after ground-air state fusion.

The same family covers four energy-efficiency designs with different inner blocks. [[huroon-2026-bd-ris-rsma-uav]] combines BCD/SCA with generalized Benders and Riemannian phase updates; [[fu-2026-uav-fl-user-grouping]] uses two SCA phases around fixed FL participation; [[mihertie-2026-aerial-irs-rsma-ee]] uses SCA plus semidefinite rank-one relaxation; and [[xie-2023-wireless-powered-short-packet-uav]] alternates SCA/fractional location, blocklength, and WPT-power updates without SDR.
