---
type: source
title: "Optimizing Energy Efficiency for Federated Learning in Rotary-Wing UAV Air-to-Ground Communications"
authors: ["Xuan-Toan Dang", "Quynh-Suong Nguyen", "Oh-Soon Shin"]
year: 2026
url: "https://doi.org/10.1109/TGCN.2025.3599309"
venue: "IEEE Transactions on Green Communications and Networking (IEEE TGCN), vol. 10, pp. 829-843"
tags: [source, federated-learning, uav, energy-efficiency, air-to-ground, alternating-optimization]
related:
  - "[[simultaneous-interference-uav-federated-learning]]"
  - "[[federated-learning]]"
  - "[[air-to-ground-channel-model]]"
  - "[[uav-trajectory-control]]"
created: 2026-07-14
updated: 2026-07-14
---

# Optimizing Energy Efficiency for Federated Learning in Rotary-Wing UAV Air-to-Ground Communications

## Citation

Dang, X.-T., Nguyen, Q.-S., & Shin, O.-S. (2026). *Optimizing Energy Efficiency for Federated Learning in Rotary-Wing UAV Air-to-Ground Communications*. **IEEE Transactions on Green Communications and Networking, 10**, 829-843. DOI: 10.1109/TGCN.2025.3599309.

## TL;DR

Minimizes user computation-plus-communication energy in UAV-coordinated federated learning by jointly controlling simultaneous uplink powers, local accuracy and CPU resources, and the rotary-wing UAV's 3-D placement and velocity under mixed LoS/NLoS propagation and a flight-energy return constraint.

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

## Raw artifacts

- Parse: `raw/sources/Optimizing_Energy_Efficiency_for_Federated_Learning_in_Rotary-Wing_UAV_Air-to-Ground_Communications/Optimizing_Energy_Efficiency_for_Federated_Learning_in_Rotary-Wing_UAV_Air-to-Ground_Communications.md`
- Origin PDF and extracted figures (`images/`) are in the same folder.
