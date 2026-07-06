---
type: source
title: "QoS-Oriented Task Offloading in NOMA-Based Multi-UAV Cooperative MEC Systems"
authors: ["Peipei Chen", "Lailong Luo", "Deke Guo", "Jiaju Wu", "Kaikai Chi", "Chenggang Yan", "Xudong Dong"]
year: 2026
url: "https://doi.org/10.1109/TWC.2025.3593884"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, uav-mec, noma, task-offloading, task-priority, soft-actor-critic, qos]
related:
  - "[[noma]]"
  - "[[task-priority-in-mec]]"
  - "[[dynamic-qos-constraints]]"
  - "[[soft-actor-critic]]"
  - "[[task-offloading]]"
  - "[[uav-trajectory-control]]"
  - "[[qoe-modeling-mec]]"
created: 2026-07-07
updated: 2026-07-07
---

# QoS-Oriented Task Offloading in NOMA-Based Multi-UAV Cooperative MEC Systems

## Citation

Chen, P., Luo, L., Guo, D., Wu, J., Chi, K., Yan, C., & Dong, X. (2026). *QoS-Oriented Task Offloading in NOMA-Based Multi-UAV Cooperative MEC Systems*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2025.3593884. DOI/venue/year are parse-silent at the top level and verified against a title-matched Crossref/IEEE DOI record.

## TL;DR

Formulates QoS-oriented task offloading for a NOMA-based multi-UAV cooperative MEC system. Tasks carry data size, CPU cycles, deadline, and priority; the objective maximizes average system utility by jointly optimizing UAV 3D trajectories, mobile-user association, offloading ratios, and UAV compute allocation. The proposed ISAC algorithm combines Lagrange duality with an improved [[soft-actor-critic]] loss to improve exploration and avoid local minima.

## Problem

Existing UAV-MEC offloading methods often minimize delay, energy, cost, or throughput without explicitly differentiating high-priority and low-priority tasks. In emergency, navigation, and AR-like applications, missed deadlines have priority-dependent consequences. The paper therefore defines utility functions that penalize high-priority deadline violations sharply while allowing low-priority tasks to degrade more gradually.

## System model

The NMCM system contains multiple mobile users and multiple UAVs over slotted time. Each mobile user generates a task tuple `{D_k(n), C_k(n), omega_k(n), E_k(n)}` for transmitted data size, CPU cycles, maximum delay threshold, and priority level. Users offload via NOMA to UAVs; UAV receivers apply successive interference cancellation. A central controller aggregates beacon information and decides UAV association, trajectories, offloading ratios, and computation resource allocation.

## Method

The paper first applies Lagrange duality to transform the constrained nonconvex problem into an unconstrained dual form. It then proposes ISAC, an improved SAC variant whose Q-network loss includes a perturbation term intended to expand exploration beyond local minima. The reward is tied to system utility while the transformed constraints guide feasible trajectory, association, offloading, and resource decisions.

## Key findings

- ISAC is reported to outperform PPO, SAC, and DDPG on offloading transmission rate at varying bandwidths and task sizes.
- Task completion rate improves as bandwidth increases, but the parse notes that around 50 MHz the offloading rate and completion rate saturate for 1 MB tasks.
- For larger task sizes under fixed 20 MHz bandwidth, offloading performance drops for all methods, but ISAC remains above PPO, SAC, and DDPG in resource-limited settings.
- System utility rises with the number of UAVs, and ISAC is reported to maintain stronger performance as the number of mobile users grows; PPO and DDPG drop sharply when the user count exceeds 40 in the reported experiment.
- The conclusion states that ISAC improves convergence performance, offloading transmission rates, task completion rates, and system utility relative to benchmark algorithms.

## Limitations / future work

The paper does not model high-speed-UAV Doppler effects because of modeling complexity. The conclusion states future research will explore multi-modal learning and aggregation techniques for multi-UAV task offloading.

## Relation to the corpus

This source joins [[task-priority-in-mec]], [[dynamic-qos-constraints]], [[noma]], and [[task-offloading]] in a single multi-UAV formulation. It is close to [[hao-2024-clp-multiuav-priority-offloading]] and [[wang-2026-llm-qos-multiuav-resource]] on priority/QoS-aware UAV-MEC control, but its technical distinction is the Lagrangian-dual plus improved-SAC treatment of constrained NOMA offloading.

## Raw artifacts

- `raw/sources/QoS-Oriented Task Offloading in NOMA-Based Multi-UAV Cooperative MEC Systems/QoS-Oriented Task Offloading in NOMA-Based Multi-UAV Cooperative MEC Systems.md`
- Original PDF and extracted figures (`images/`) in the same folder.
