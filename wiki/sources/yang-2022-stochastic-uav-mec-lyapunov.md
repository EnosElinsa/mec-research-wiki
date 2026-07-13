---
type: source
title: "Online Trajectory and Resource Optimization for Stochastic UAV-Enabled MEC Systems"
authors: ["Zheyuan Yang", "Suzhi Bi", "Ying-Jun Angela Zhang"]
year: 2022
url: "https://doi.org/10.1109/TWC.2022.3142365"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, uav-mec, lyapunov-optimization, online-algorithm, trajectory-optimization, stochastic-optimization, user-mobility]
related:
  - "[[ying-jun-angela-zhang]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[lyapunov-optimization]]"
  - "[[uav-trajectory-control]]"
  - "[[two-stage-decomposition]]"
  - "[[energy-latency-tradeoff]]"
  - "[[yu-2020-uav-ec-collaborative-offloading]]"
  - "[[zhu-2025-lycnn-drl-wpt-mec]]"
created: 2026-05-29
updated: 2026-07-14
---

# Online Trajectory and Resource Optimization for Stochastic UAV-Enabled MEC Systems

## Citation

Yang, Z., Bi, S., & Zhang, Y.-J. A. (2022). *Online Trajectory and Resource Optimization for Stochastic UAV-Enabled MEC Systems*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2022.3142365.

## TL;DR

A UAV-enabled MEC platform serving multiple mobile ground users with **random movements and task arrivals**. The goal is to minimize the average weighted energy of all users subject to average UAV-energy and data-queue-stability constraints. Formulated as a multi-stage stochastic optimization and converted via **Lyapunov optimization** into per-slot deterministic problems; two reduced-complexity methods solve resource allocation and UAV movement either **sequentially (two-stage)** or **jointly (one-step)**.

## Problem framing

UAV-MEC must serve users out of terrestrial coverage despite random user mobility and stochastic task arrivals. The long-term objective (average user energy) under UAV-energy and queue-stability constraints needs an online algorithm that doesn't require future knowledge.

## System model

- **Actors.** One UAV-MEC platform; multiple mobile ground users with random movement + task arrivals.
- **Objective.** Minimize average weighted user energy subject to average UAV energy and data-queue stability.
- **Tool.** [[lyapunov-optimization]] converts the multi-stage stochastic problem into per-slot deterministic problems with fewer variables.

## Method

- Two reduced-complexity methods for the non-convex per-slot sub-problem:
  - **Two-stage:** sequentially solve user resource allocation, then UAV movement ([[two-stage-decomposition]]).
  - **Joint:** solve resource allocation and UAV movement together.
- Both satisfy the average UAV-energy and queue-stability constraints and trade off user energy vs. queue-backlog length (the O(1/V), O(V) Lyapunov trade-off).

## Key findings

- Both methods significantly outperform benchmarks (including a learning-based method) in reducing ground-user energy; the **joint method outperforms the two-stage method at the cost of higher computational complexity** (the paper's stated trade-off).

## Limitations / future work

The parse's conclusion does not enumerate explicit future work beyond the established framework.

## Relation to the corpus

A clean **Lyapunov-based online UAV-MEC** entry whose explicit two-stage-vs-joint comparison directly informs the wiki's [[two-stage-decomposition]] thread (cf. the discrete-then-continuous decompositions in [[wang-2026-aerial-marine-msar]], [[nabi-2025-jour-hierarchical-aerial]]). Shares the Lyapunov backbone with [[zhu-2025-lycnn-drl-wpt-mec]] and [[qin-2025-bcuav-masac]]; shares the UAV-EC offloading lineage with [[yu-2020-uav-ec-collaborative-offloading]]. Reinforces [[lyapunov-optimization]].

## Raw artifacts

- `raw/sources/Online_Trajectory_and_Resource_Optimization_for_Stochastic_UAV-Enabled_MEC_Systems/full.md`
- Original PDF and extracted figures in the same folder.
