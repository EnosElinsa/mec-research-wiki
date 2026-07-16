---
type: source
title: "Optimizing Energy Efficiency for Federated Learning in Rotary-Wing UAV Air-to-Ground Communications"
authors: ["Xuan-Toan Dang", "Quynh-Suong Nguyen", "Oh-Soon Shin"]
year: 2026
url: "https://doi.org/10.1109/TGCN.2025.3599309"
venue: "IEEE Transactions on Green Communications and Networking (IEEE TGCN), vol. 10, pp. 829-843"
modeling_card: required
tags: [source, federated-learning, uav, energy-efficiency, air-to-ground, alternating-optimization]
related:
  - "[[aerial-federated-aggregation-design-space]]"
  - "[[zhong-2026-hierarchical-ota-fl]]"
  - "[[li-2026-clp-uav-hpfl]]"
  - "[[hierarchical-over-the-air-federated-learning]]"
  - "[[gradient-correlation-aware-aggregation-mse]]"
  - "[[critical-learning-period]]"
  - "[[simultaneous-interference-uav-federated-learning]]"
  - "[[federated-learning]]"
  - "[[air-to-ground-channel-model]]"
  - "[[uav-trajectory-control]]"
created: 2026-07-14
updated: 2026-07-16
---

# Optimizing Energy Efficiency for Federated Learning in Rotary-Wing UAV Air-to-Ground Communications

## Citation

Dang, X.-T., Nguyen, Q.-S., & Shin, O.-S. (2026). *Optimizing Energy Efficiency for Federated Learning in Rotary-Wing UAV Air-to-Ground Communications*. **IEEE Transactions on Green Communications and Networking, 10**, 829-843. DOI: 10.1109/TGCN.2025.3599309.

## TL;DR

Minimizes user computation-plus-communication energy in UAV-coordinated federated learning by jointly controlling simultaneous uplink powers, local accuracy and CPU resources, and the rotary-wing UAV's 3-D placement and velocity under mixed LoS/NLoS propagation and a flight-energy return constraint.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A rotary-wing UAV acts as the federated-learning server for $K$ ground users. Users upload local models simultaneously on one uplink resource under mutual interference, and the UAV placement follows a mixed LoS/NLoS air-to-ground model while movement, hovering, and downlink communication consume UAV energy.

**Problem & objective**: The design minimizes all users' computation-plus-communication energy across the required global rounds, $\min_{\mathbf w,\mathbf u,\mathbf f,\eta,T_u^{\mathrm{com}},T_{\mathrm{cmp}}}G(\eta)E(\mathbf w,\mathbf u,\mathbf f,\eta)$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Uplink power coefficient | $w_k$ | continuous, $0\leq w_k\leq1$ | Fractional uplink power used by user $k$ |
| UAV location | $\mathbf u=(x_u,y_u,z_u)$ | continuous, $0\leq x_u,y_u\leq L$, $h_{\min}\leq z_u\leq h_{\max}$ | Three-dimensional server placement |
| User CPU frequency | $f_k$ | continuous, $f_{\min}\leq f_k\leq f_{\max}$ | Local computing frequency of user $k$ |
| Local training accuracy | $\eta$ | continuous, $0\leq\eta\leq1$ | Accuracy target controlling local and global iterations |
| Uplink synchronization time | $T_u^{\mathrm{com}}$ | continuous, nonnegative | Common upper bound on user upload time |
| Local computation time | $T_{\mathrm{cmp}}$ | continuous, nonnegative | Common upper bound on one local computation round |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| 16b-16d | User power and UAV horizontal and vertical placement remain within their prescribed bounds |
| 16e | The full training process meets its deadline, $G(\eta)T(\eta,T_u^{\mathrm{com}},T_{\mathrm{cmp}})\leq t_{\mathrm{limit}}$ |
| 16f-16h | Uplink, downlink, and local computation finish within their synchronized time bounds |
| 16i-16j | CPU frequency and local accuracy remain feasible, $f_{\min}\leq f_k\leq f_{\max}$ and $0\leq\eta\leq1$ |
| 16k-16l | UAV speed is bounded and movement energy supports a safe return, $0\leq v_{\mathrm{uav}}\leq v_{\max}$ and $E_{\mathrm{uav}}^{\mathrm{mov}}\leq E_{\mathrm{fly}}$ |

**Algorithm**: An inner-approximation alternating method first fixes $\eta$ and convexifies the coupled placement, uplink power, CPU, and timing block. With placement and power fixed, a second convexified block updates local accuracy and the remaining computation and communication resources; the blocks repeat to a local stationary solution.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Dang et al. [x] optimized federated learning coordinated by a rotary-wing UAV when users upload simultaneously under interference and the air-to-ground channel mixes LoS and NLoS propagation. Their formulation minimizes aggregate user computation and communication energy over uplink power, local accuracy, CPU frequency, synchronization times, and three-dimensional UAV placement, subject to training deadlines and a safe-return flight-energy budget. An inner-approximation alternating algorithm convexifies the placement and resource blocks and converges to a local stationary point. Simulations place the UAV at 30.12 m under pure LoS and 50.04 m under mixed propagation, reach 95% of terminal performance within ten iterations, and show lower user energy than the restricted-variable benchmarks.

## Problem and system model

A single-antenna rotary-wing UAV coordinates `K` single-antenna user equipments as the FL server. All users upload local models simultaneously on the same time-frequency resource, so each user's rate includes inter-user interference. The A2G model averages fast fading and combines distance loss with elevation-dependent LoS/NLoS probabilities.

The objective is total UE energy over the FL process, including local computation and model communication. Constraints cover user powers and CPU frequencies, local accuracy, synchronous completion, an overall training deadline, 3-D UAV bounds and speed, and enough UAV movement energy to return safely. The optimization is performed offline at a ground controller rather than onboard the UAV.

## Method

The [[simultaneous-interference-uav-federated-learning]] formulation alternates between two non-convex blocks. With local accuracy fixed, inner approximation convexifies placement, velocity, power, and timing constraints; with UAV location and power fixed, a second convexified block updates accuracy and computation/communication resources. The paper establishes stationary-point/KKT convergence for the inner programs and local convergence for the alternating procedure, not global optimality.

## Key findings

- Simulated optimal altitude is 30.12 m under pure LoS and 50.04 m under the mixed LoS/NLoS setting, illustrating the blockage-versus-distance trade-off.
- In the reported 12-user setting, increasing the UAV flight budget beyond 5,000 J no longer changes the reached placement; below that level, velocity optimization materially affects UE energy.
- The iterative method reaches 95% of its reported terminal performance within ten iterations. Idealized OMA has the lowest plotted UE energy because it assumes perfect interference cancellation; the proposed simultaneous method remains close to OMA and outperforms the restricted-variable benchmarks across bandwidth and model-size sweeps.
- Simultaneous interference remains explicit rather than being removed through orthogonal scheduling or perfect SIC.

## Limitations

Evidence is simulation-only. The optimization is centralized and offline, assumes available CSI and user locations, averages out fast fading, uses one UAV, and reaches a local stationary solution. It optimizes one placement transition rather than an online mobile trajectory, and its tractability claim does not constitute an onboard runtime demonstration.

## Relation to the corpus

This source extends [[federated-learning]] with a communication layer that keeps inter-user interference, realistic [[air-to-ground-channel-model|LoS/NLoS A2G propagation]], and rotary-wing movement energy in the same optimization. It complements learning-based UAV-FL controllers by using deterministic inner approximations and explicit deadline and return-energy constraints.

In [[aerial-federated-aggregation-design-space]], [[zhong-2026-hierarchical-ota-fl]] and [[hierarchical-over-the-air-federated-learning]] provide the direct physical-layer contrast: their superposition computes analog partial gradients, whereas this paper decodes simultaneous user uploads under interference. Its UE-energy objective is distinct from [[gradient-correlation-aware-aggregation-mse]] and its learning-stationarity bridge. [[li-2026-clp-uav-hpfl]] and [[critical-learning-period]] add a second contrast, between this offline constraint-driven placement/resource design and learning-state-triggered visits and aggregation periods.

## Raw artifacts

- Parse: `raw/sources/Optimizing_Energy_Efficiency_for_Federated_Learning_in_Rotary-Wing_UAV_Air-to-Ground_Communications/Optimizing_Energy_Efficiency_for_Federated_Learning_in_Rotary-Wing_UAV_Air-to-Ground_Communications.md`
- Origin PDF and extracted figures (`images/`) are in the same folder.
