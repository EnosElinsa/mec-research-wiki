---
type: concept
title: "Alternating Optimization with SDR and SCA"
tags: [optimization, alternating-optimization, sdr, sca, non-convex, classical-solver]
related:
  - "[[fractional-programming-dinkelbach]]"
  - "[[lyapunov-optimization]]"
  - "[[benaya-2025-aerial-isac-haps]]"
  - "[[mohammadi-2026-star-ris-uav-mec-noma]]"
  - "[[xiao-2025-star-ris-bidirectional-uav-mec]]"
  - "[[wang-2026-secure-lae-uav-scheduling]]"
created: 2026-05-29
updated: 2026-07-07
---

# Alternating Optimization with SDR and SCA

A classical recipe for solving non-convex MEC and ISAC problems with multiple coupled blocks (e.g. transmit beamforming, receive beamforming, trajectory, power). The recipe:

1. **Alternating Optimization (AO).** Hold all blocks fixed except one; solve that block; rotate. Repeat until convergence (typically a few iterations).
2. Inside each block, the subproblem is still non-convex. Two go-to relaxations:
   - **Semi-Definite Relaxation (SDR).** Lift a quadratic-form variable into a positive-semidefinite matrix, drop the rank-1 constraint, solve the resulting SDP, then recover a rank-1 solution via Gaussian randomization.
   - **Successive Convex Approximation (SCA).** Replace the non-convex constraint/objective with a convex upper bound at each iteration (e.g. first-order Taylor of a concave term, or DC-programming linearization).

AO converges to a stationary point but not necessarily the global optimum; in practice it's robust enough for ISAC, beamforming, and trajectory problems. See [[benaya-2025-aerial-isac-haps]] for a four-block AO instance.

This stack is the **non-DRL** counterpoint to the j-PPO / DDPG / SAC backbone that dominates the wiki — useful when the problem has clean convex structure within each block.

[[mohammadi-2026-star-ris-uav-mec-noma]] uses the same decomposition style without SDR as the headline: bit allocation, transmit power, STAR-RIS phase shifts, and UAV trajectory are separated into subproblems, then handled with SCA or closed-form MRT-style phase updates inside a BCD loop. [[xiao-2025-star-ris-bidirectional-uav-mec]] uses Dinkelbach plus SCA inside BCD for STAR-RIS bidirectional offloading. [[wang-2026-secure-lae-uav-scheduling]] decomposes secrecy-energy-efficiency maximization into scheduling, power, and trajectory/velocity subproblems, using penalty updates, SCA, and Dinkelbach-driven iteration.
