---
type: source
modeling_card: required
title: "UAV-Relay-Aided Secure Maritime Networks Coexisting With Satellite Networks: Robust Beamforming and Trajectory Optimization"
authors: ["Yu Yao", "Wenqi Xiao", "Pu Miao", "Gaojie Chen", "Haitao Yang", "Chan-Byoung Chae", "Kai-Kit Wong"]
year: 2026
url: "https://doi.org/10.1109/TWC.2025.3596136"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), 25, 2342-2358"
tags: [source, maritime-communications, physical-layer-security, satellite-uav-terrestrial-network, robust-beamforming, trajectory-optimization]
related:
  - "[[physical-layer-security]]"
  - "[[norm-bounded-csi-robust-optimization]]"
  - "[[s-procedure-for-csi-uncertainty]]"
  - "[[csi-estimation-error]]"
  - "[[uav-mobile-relaying]]"
  - "[[information-causality-constraint]]"
  - "[[uav-trajectory-control]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[lu-2023-uav-relay-secure-maritime-mec]]"
  - "[[wu-2024-satellite-maritime-spectrum-sharing]]"
  - "[[chan-byoung-chae]]"
  - "[[kai-kit-wong]]"
created: 2026-07-14
updated: 2026-07-16
---

# UAV-Relay-Aided Secure Maritime Networks Coexisting With Satellite Networks: Robust Beamforming and Trajectory Optimization

## Citation

Yao, Y., Xiao, W., Miao, P., Chen, G., Yang, H., Chae, C.-B., & Wong, K.-K. (2026). *UAV-Relay-Aided Secure Maritime Networks Coexisting With Satellite Networks: Robust Beamforming and Trajectory Optimization*. **IEEE Transactions on Wireless Communications**, 25, 2342-2358. DOI: 10.1109/TWC.2025.3596136.

The article was published online in August 2025 and assigned to the final 2026 volume; the canonical citation year follows that volume record.

## TL;DR

Jointly designs TBS, decode-and-forward UAV-relay, and satellite beamformers with the UAV trajectory in a spectrum-sharing maritime satellite-UAV-terrestrial network. The method applies alternating optimization, semidefinite reformulation, the S-procedure, and successive convex approximation to a worst-case secrecy objective under deterministic norm-bounded CSI errors.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A terrestrial base station sends confidential maritime traffic through a multi-antenna decode-and-forward UAV relay while a cochannel LEO satellite serves satellite users and an eavesdropper listens to the maritime link. The TBS, UAV, and satellite share spectrum, and satellite-related and eavesdropping channels have deterministic norm-bounded CSI errors.

**Problem & objective**: Problem (13) maximizes worst-case weighted average secrecy rate, $\max_{\mathbf W[n],\mathbf q[n]}\min_{\Delta\mathbf h[n]}\frac{1}{N}\sum_{n=1}^{N}\sum_{k=1}^{K}\omega_k\big(r_{U,k}[n]-r_{E,k}[n]\big)$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| TBS beamforming | $\mathbf w_{T,k}[n]$ | complex continuous | Backhaul beam from the TBS for maritime-user stream $k$ |
| UAV beamforming | $\mathbf w_{U,k}[n]$ | complex continuous | Relay access beam from the UAV to maritime user $k$ |
| Satellite beamforming | $\mathbf w_{S,m}[n]$ | complex continuous | Downlink beam for satellite user $m$ |
| UAV trajectory | $\mathbf q[n]$ | continuous, 3-D trajectory | Slotwise UAV relay position |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| 1a-1c | UAV endpoints, speed, and altitude satisfy the prescribed flight envelope |
| 11 | Robust relay causality requires the TBS-UAV rate to cover the aggregate UAV-MU forwarding rate |
| 12 | Every satellite user meets its worst-case minimum rate $\Gamma_{S,m}^{\min}$ |
| 13b-13d | TBS, UAV, and satellite beamforming obey their per-slot power budgets |
| Uncertainty sets | Satellite and eavesdropping CSI errors remain inside declared Euclidean or Frobenius norm balls |

**Algorithm**: Alternating optimization fixes the trajectory while updating collaborative TBS, UAV, and satellite beamforming, then fixes the beams while updating the UAV path. Auxiliary variables, sign-definiteness and S-procedure LMIs treat semi-infinite CSI constraints, while Cauchy-Schwarz bounds, SCA, and a shrinking trust region yield convex local subproblems.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Yao et al. [x] studied robust secure maritime communication in a spectrum-sharing satellite-UAV-terrestrial network with a decode-and-forward UAV relay and imperfect CSI. They maximized worst-case weighted average secrecy rate over TBS, UAV, and satellite beamformers and the UAV trajectory while enforcing power, flight, relay-backhaul, and satellite-user rate constraints. Their alternating method uses auxiliary variables, the S-procedure, sign-definiteness reformulations, successive convex approximation, and trust-region trajectory updates. The plotted outer objective converges after roughly seven iterations for the examined satellite-user rate thresholds. Simulations report about 150 percent higher average secrecy rate than random beamforming in the flight-duration comparison and show that the robust joint design remains stronger than the compared schemes as bounded CSI error increases.

## Problem

A terrestrial base station must send confidential traffic to maritime users through a multi-antenna UAV relay while a cochannel LEO satellite serves satellite users and an eavesdropper attempts to intercept maritime traffic. Beamforming and UAV motion jointly affect the relay backhaul, maritime access links, satellite-user QoS, cross-tier interference, and information leakage, while satellite-related and eavesdropping CSI is outdated or uncertain.

## System model

- The TBS, UAV, and satellite share spectrum. The UAV decodes and forwards TBS traffic to maritime users, while the satellite transmits to satellite users.
- CSI errors on the UAV-eavesdropper, satellite-UAV, satellite-user, and satellite-eavesdropper channels lie in specified Euclidean/Frobenius norm balls around channel estimates.
- The objective maximizes a worst-case weighted time-average sum of maritime-user rate minus eavesdropper rate. The parsed objective does not visibly apply a positive-part operator, so it should not be read as a fully clipped secrecy-capacity expression.
- Constraints include per-slot TBS/UAV/satellite power budgets, prescribed UAV endpoints and mobility limits, a per-slot relay/backhaul rate condition, and worst-case minimum rates for satellite users.

## Method

The algorithm alternates between collaborative beamforming at fixed trajectory and trajectory design at fixed beamforming. In the beamforming block, auxiliary variables, first-order bounds, Schur-complement LMIs, general sign-definiteness, and the [[s-procedure-for-csi-uncertainty|S-procedure]] convert semi-infinite quadratic constraints under [[norm-bounded-csi-robust-optimization|norm-bounded CSI uncertainty]] into a finite SDP solved with CVX. In the trajectory block, inequality bounds, first-order Taylor approximations, and a shrinking trust region yield a convex local subproblem.

The resulting iterations address the stated uncertainty sets, but they do not establish global optimality for the original coupled non-convex problem. The paper states convexity of each reformulated local subproblem and trust-region convergence conditions for trajectory updates; plotted objective convergence and non-decreasing accepted updates support local iterative improvement, not a global secrecy guarantee or robustness to arbitrary model mismatch.

## Key findings

- In the reported simulations over 50 channel realizations, the outer objective converges after roughly seven iterations for the plotted satellite-user rate thresholds.
- Increasing the satellite-user minimum-rate threshold from 0.5 to 0.8 bps/Hz lowers secure performance in the tested setup because the coupled requirements leave less UAV power available.
- For flight durations of 7, 10, and 20 seconds, longer missions let the optimized path spend more time near a favorable secrecy region and away from the modeled eavesdropper. The paper reports about 150% higher average secrecy rate than random beamforming in that comparison.
- Imperfect CSI reduces secrecy performance, with a sharper decline in the plotted uncertainty-radius sweep beyond 0.2. These observations are simulation-specific and are not analytical worst-case performance bounds.
- Removing satellite interference gives a modest gain in the tested regimes, while the proposed design exceeds MRT by up to about 2 bps/Hz in the plotted comparison.

## Limitations / parse caveats

The evidence is simulation-only, with one modeled eavesdropper, known geometry, deterministic bounded CSI errors, fixed antenna and power budgets, and specific Rician/LoS/satellite channel models. Several LMIs, obstacle equations, and altitude symbols are OCR-damaged or internally inconsistent, so exact algebraic and altitude-control claims require checking the PDF. The explicit satellite-user QoS constraint also conflicts with introductory wording that refers to maritime-user QoS. No field trial, global-optimality result, or guarantee outside the declared uncertainty balls is provided.

## Relation to the corpus

This source combines [[physical-layer-security]], [[uav-mobile-relaying]], and [[uav-trajectory-control]] in a satellite-terrestrial spectrum-sharing setting. It extends the secure maritime relay theme of [[lu-2023-uav-relay-secure-maritime-mec]] and the coexistence problem in [[wu-2024-satellite-maritime-spectrum-sharing]] with coordinated TBS/UAV/satellite beamforming. Its per-slot relay-rate condition is closely related to [[information-causality-constraint|information causality]], while its deterministic CSI treatment grounds [[norm-bounded-csi-robust-optimization]] and [[s-procedure-for-csi-uncertainty]].

## Raw artifacts

- Parse: `raw/sources/UAV-Relay-Aided_Secure_Maritime_Networks_Coexisting_With_Satellite_Networks_Robust_Beamforming_and_Trajectory_Optimization/UAV-Relay-Aided_Secure_Maritime_Networks_Coexisting_With_Satellite_Networks_Robust_Beamforming_and_Trajectory_Optimization.md`
- Origin PDF: `raw/sources/UAV-Relay-Aided_Secure_Maritime_Networks_Coexisting_With_Satellite_Networks_Robust_Beamforming_and_Trajectory_Optimization/UAV-Relay-Aided_Secure_Maritime_Networks_Coexisting_With_Satellite_Networks_Robust_Beamforming_and_Trajectory_Optimization.pdf`
- Figures: `raw/sources/UAV-Relay-Aided_Secure_Maritime_Networks_Coexisting_With_Satellite_Networks_Robust_Beamforming_and_Trajectory_Optimization/images/`
