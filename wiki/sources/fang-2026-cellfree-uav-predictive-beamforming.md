---
type: source
title: "Predictive Beamforming and Resource Allocation for High-Mobility Cell-Free UAV Networks"
authors: ["Chao Fang", "Cheng Zhang", "Wen Wang", "Pengguang Du", "Wei Zhang", "Yongming Huang"]
year: 2026
url: "https://doi.org/10.1109/TWC.2026.3695091"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), vol. 25, pp. 18039-18056"
modeling_card: required
tags: [source, cell-free-massive-mimo, predictive-beamforming, uav-tracking, resource-allocation, ekf, covariance-intersection]
related:
  - "[[cell-free-uav-predictive-beamforming]]"
  - "[[covariance-intersection-state-fusion]]"
  - "[[pcrb-guided-pilot-length-optimization]]"
  - "[[cellular-connected-uav]]"
  - "[[cramer-rao-bound]]"
  - "[[device-association]]"
  - "[[multi-source-data-fusion]]"
  - "[[wang-2026-6dara-cellfree]]"
  - "[[beam-delay-alignment-transmission]]"
  - "[[shi-2026-vhetnet-comp-coverage]]"
  - "[[mobility-asynchrony-and-geometry-in-aerial-coverage]]"
  - "[[yongming-huang]]"
created: 2026-07-14
updated: 2026-07-16
---

# Predictive Beamforming and Resource Allocation for High-Mobility Cell-Free UAV Networks

## Citation

Fang, C., Zhang, C., Wang, W., Du, P., Zhang, W., & Huang, Y. (2026). *Predictive Beamforming and Resource Allocation for High-Mobility Cell-Free UAV Networks*. **IEEE Transactions on Wireless Communications, 25**, 18039-18056. DOI: 10.1109/TWC.2026.3695091.

## TL;DR

Uses distributed EKF tracking and covariance-intersection fusion to predict high-mobility UAV channels after one pilot-bearing slot, then jointly chooses pilot length, ground-AP association, and downlink power from a tracking-accuracy bound.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Distributed ground APs serve high-mobility UAVs in a cell-free downlink. Only the first slot of each frame carries orthogonal uplink pilots; local EKFs and covariance-intersection fusion predict later LoS channels, while NLoS components are handled statistically.

**Problem & objective**: Maximize training-adjusted effective sum spectral efficiency, $\max_{\mathbf U,\mathbf P,L}R(\mathbf U,\mathbf P,L)$, over pilot length, sparse AP-UAV association, and downlink power while enforcing a posterior tracking-accuracy bound.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Pilot length | $L$ | integer, $K\leq L\leq N_s$ | Training symbols in the first slot of a frame |
| AP-UAV association | $u_{m,k}$ | binary | Whether AP $m$ serves UAV $k$ |
| Downlink power | $p_{m,k}$ | continuous, nonnegative | Power allocated by AP $m$ to UAV $k$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Position-tracking bound meets the target: $\Omega(L)\leq\zeta$. |
| C2 | Pilot length is integer and satisfies $K\leq L\leq N_s$. |
| C3 | AP association is binary and each AP serves at most $U_{\max}$ UAVs. |
| C4 | Every AP respects its downlink budget: $\sum_k p_{m,k}\leq P_{\max}$. |
| C5 | Unassociated links receive zero power through the association-power coupling. |

**Algorithm**: Run local EKFs from delay, Doppler, azimuth, and elevation estimates and fuse their states by covariance intersection. Select the shortest feasible pilot length by integer bisection on the PCRB, replace binary association with a reweighted L1 sparse-power surrogate, and alternate fractional or quadratic-transform power updates with dual-variable bisection until effective sum spectral efficiency stabilizes.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Fang et al. [x] developed predictive beamforming for high-mobility cell-free UAV networks using distributed EKF tracking and covariance-intersection fusion. They maximized effective sum spectral efficiency over integer pilot length, binary AP-UAV association, and downlink power under PCRB accuracy, pilot-length, AP-user capacity, and per-AP power constraints. Their solution chooses the shortest feasible pilot by bisection, approximates sparse association with reweighted L1 power variables, and alternates fractional-programming and dual updates. At frame length 20, the reported design achieved effective sum SE 57.2, 31% above the training-every-slot equal-allocation baseline, while using 95% less fronthaul overhead.

## Problem and system model

Multiple ground access points with planar arrays serve single-antenna UAVs through a central processing unit. Repeated full CSI training would consume a large fraction of each short high-mobility coherence interval. The proposed frame therefore collects orthogonal uplink pilots only in its first slot and relies on state prediction for later downlink slots.

Each AP estimates delay, Doppler, azimuth, and elevation, runs a local EKF, reconstructs the LoS channel, and forms a zero-forcing predictive beam. The downlink is noncoherent across APs, with binary AP-UAV association and per-link power. Effective spectral efficiency subtracts the initial training duration rather than treating prediction as overhead-free.

## Method

[[cell-free-uav-predictive-beamforming]] sends local state estimates and covariance matrices, rather than full CSI, to the CPU. [[covariance-intersection-state-fusion]] combines them without requiring known cross-correlations. A posterior CRB connects predicted position uncertainty to training length; [[pcrb-guided-pilot-length-optimization]] then uses integer bisection for pilots, reweighted L1 sparsity for association, and Lagrangian-dual/quadratic transforms for power allocation.

The multipath extension tracks only the deterministic LoS component and treats NLoS statistically through a use-and-then-forget bound.

## Key findings

- Across the evaluated frame lengths, the paper reports 90% lower training overhead with 22% better positioning accuracy, 95% lower overhead with 3% worse accuracy, and 98% lower overhead with 56% worse accuracy.
- At a 20-slot frame, fusion reduces reported position sum-RMSE from 51.5 m to 26.5 m, while effective sum spectral efficiency is 57.2 versus 43.5 for tracking with fixed pilots and equal allocation.
- Against fused tracking/joint-allocation baselines, the method gives comparable spectral efficiency with 78%-88% less training and 95% less fronthaul overhead.
- At 20 slots, effective sum spectral efficiency is 8% below the ideal-CSI, training-free upper bound (57.2 versus 62.4).
- Performance degrades as the Rician factor falls from 20 to 5 dB, consistent with the beamformer predicting only the LoS component.

## Limitations

Evidence is analytical and Monte Carlo simulation only. The PCRB/fused-covariance relation depends on first-order EKF linearization and local linear-Gaussian assumptions, which can be optimistic at low SNR or under aggressive maneuvers. Equal covariance-intersection weights are used because AP reliability is unknown. Reweighted-L1 association is a local approximation to the mixed-integer problem, and the cited microsecond-to-submillisecond fronthaul latency is an expectation rather than a measurement.

## Relation to the corpus

This source is a ground-AP-to-UAV cell-free architecture, distinct from [[aerial-terrestrial-cell-free-massive-mimo]], where aerial APs serve ground users. It extends predictive beam control from a single link into distributed tracking, state fusion, and resource allocation.

## Raw artifacts

- Parse: `raw/sources/Predictive_Beamforming_and_Resource_Allocation_for_High-Mobility_Cell-Free_UAV_Networks/Predictive_Beamforming_and_Resource_Allocation_for_High-Mobility_Cell-Free_UAV_Networks.md`
- Origin PDF and extracted figures (`images/`) are in the same folder.
