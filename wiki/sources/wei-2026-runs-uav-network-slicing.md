---
type: source
title: "RUNs: Fast and Robust Network Slicing for UAV-Assisted Wireless Networks Under Imperfect CSI and Node Mobility"
authors: ["Fengsheng Wei", "Gang Feng", "Haokang Lou", "Shuang Qin", "Wei Jiang"]
year: 2026
url: "https://doi.org/10.1109/TWC.2026.3667217"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), vol. 25, pp. 12770-12786"
tags: [source, network-slicing, uav-assisted-wireless-network, robust-optimization, imperfect-csi, mixed-integer-optimization, augmented-lagrangian, block-coordinate-descent]
related:
  - "[[robust-uav-network-slicing]]"
  - "[[gang-feng]]"
  - "[[shuang-qin]]"
  - "[[network-slicing]]"
  - "[[chance-constraint]]"
  - "[[csi-estimation-error]]"
  - "[[mixed-integer-nonlinear-programming]]"
  - "[[dynamic-qos-constraints]]"
  - "[[cheng-2025-dos-satellite-edge-computing]]"
  - "[[ammar-2026-oran-maritime-slicing]]"
created: 2026-07-14
updated: 2026-07-14
---

# RUNs: Fast and Robust Network Slicing for UAV-Assisted Wireless Networks Under Imperfect CSI and Node Mobility

## Citation

Wei, F., Feng, G., Lou, H., Qin, S., & Jiang, W. (2026). *RUNs: Fast and Robust Network Slicing for UAV-Assisted Wireless Networks Under Imperfect CSI and Node Mobility*. **IEEE Transactions on Wireless Communications, 25**, 12770-12786. DOI: 10.1109/TWC.2026.3667217.

## TL;DR

RUNs is a robust optimization framework for joint UAV deployment, integer channel allocation, and continuous power allocation across heterogeneous radio slices. It converts bounded demand and location uncertainty plus Gaussian CSI error into deterministic constraints, decomposes altitude from resource allocation, solves a continuous relaxation with augmented Lagrangian and two-block coordinate descent, and restores integer channel counts through knapsack rounding.

## Problem and system model

A single-antenna UAV serves users assigned to heterogeneous [[network-slicing|network slices]] in a circular cell. Slice-specific channel bandwidths represent different service granularities. The decisions are the UAV deployment, integer channels per user, and per-channel transmit powers; constraints cover total bandwidth and power, movement and coverage, per-slot energy, uncertain demand, and per-channel service rates.

Demand lies in bounded intervals, user positions lie in uncertainty disks, and [[csi-estimation-error]] follows a zero-mean complex Gaussian model. Each channel has a slice-specific rate [[chance-constraint]], making the robust slicing formulation a nonlinear, nonconvex [[mixed-integer-nonlinear-programming|mixed-integer problem]].

## Method

[[robust-uav-network-slicing]] replaces demand by its upper bound and user distance by the farthest point in its location uncertainty region. The Gaussian CSI chance constraint is converted into a deterministic minimum-rate condition using the inverse Gaussian Q-function.

The deterministic problem is projected into a channel/power main problem and a univariate altitude subproblem. The altitude is selected in closed form as the smallest value satisfying coverage, mobility, and altitude bounds. Integer channel counts are then relaxed; an augmented-Lagrangian outer loop and two-block coordinate-descent inner loop alternate convex channel and power subproblems. A two-dimensional 0-1 knapsack step rounds each relaxed channel count up or down. An optional outer Bayesian-optimization procedure selects horizontal position by repeatedly evaluating RUNs.

The convergence analysis establishes stationary points for the inner problem and AKKT/KKT conditions for the relaxed main problem under stated assumptions. It does not establish global optimality of the original mixed-integer problem.

## Key findings

- Table III reports RUNs runtimes of 0.067, 0.089, 0.128, 0.234, and 0.303 s for 20, 40, 60, 80, and 100 users, versus 0.442, 1.300, 2.104, 4.248, and 6.601 s for SQP. The authors summarize RUNs as nearly 20 times faster with about a 0.9% objective gap; the exact row-wise ratios vary.
- For 60 users, figure-based comparisons report RUNs close to SQP and at least 25% above SCA, GBO, and SHIO as UAV power or bandwidth varies. With user count varied, it is described as about 15% above all benchmarks except SQP.
- The four-cell horizontal-deployment illustration reports Bayesian optimization converging in about 12 objective evaluations. This is scenario-specific and figure-derived.
- The conclusion reports approximately 500 ms convergence for large-scale problems on the stated laptop, not on UAV hardware.
- The robustness results are internally inconsistent. The nominal total rate is stated as 1443 Mbps; the paper says robustness costs about 6 Mbps and also 0.07%, but `6 / 1443` is approximately 0.416%, not 0.07%. The conclusion repeats a 99% service guarantee with 0.07% degradation, so the absolute and relative claims cannot all be treated as mutually validating.

## Limitations

Evidence is simulation-only and uses a laptop implementation, with no UAV runtime, radio testbed, flight experiment, or measured uncertainty trace. The main model has one omnidirectional single-antenna UAV and one cell; multi-cell reuse is an extension, while collaborative multi-UAV service and adaptive beamforming remain future work.

The robust counterpart depends on known demand intervals, location disks, and Gaussian CSI errors, but RUNs does not estimate those uncertainty models or test misspecification. The theoretical result concerns stationary conditions for the relaxed problem, and the paper explicitly allows poor local optima. Knapsack recovery has pseudo-polynomial dependence on residual resources, while the stated log-linear complexity retains tolerance-dependent iteration counts whose practical behavior is established empirically.

## Relation to the corpus

RUNs connects [[dynamic-qos-constraints]] with uncertainty-aware aerial radio resource allocation. It complements the slicing settings in [[ammar-2026-oran-maritime-slicing]] and the recurring authors' optimization work represented by [[cheng-2025-dos-satellite-edge-computing]], while focusing on robust radio slicing rather than computation offloading.

## Raw artifacts

- Parse: `raw/sources/RUNs_Fast_and_Robust_Network_Slicing_for_UAV-Assisted_Wireless_Networks_Under_Imperfect_CSI_and_Node_Mobility/RUNs_Fast_and_Robust_Network_Slicing_for_UAV-Assisted_Wireless_Networks_Under_Imperfect_CSI_and_Node_Mobility.md`
- Origin PDF and extracted figures (`images/`) are in the same folder.
