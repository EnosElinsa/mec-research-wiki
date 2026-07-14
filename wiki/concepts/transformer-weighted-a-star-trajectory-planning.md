---
type: concept
title: "Transformer and Weighted A-Star Trajectory Planning"
tags: [transformer, weighted-a-star, uav-trajectory, age-of-information]
related:
  - "[[zhu-2023-aoi-transformer-trajectory]]"
  - "[[generalized-traveling-salesman-problem]]"
  - "[[hovering-disk-data-collection]]"
  - "[[transformer-encoder]]"
  - "[[deadline-constrained-uav-data-collection]]"
  - "[[branch-reduce-and-bound]]"
  - "[[mixed-integer-linear-programming]]"
  - "[[constraint-regimes-in-uav-data-collection]]"
created: 2026-07-14
updated: 2026-07-14
---

# Transformer and Weighted A-Star Trajectory Planning

A learned-and-search decomposition for routing through sets of feasible service points. An autoregressive Transformer chooses the order of service groups; weighted A-star then selects one point from each ordered group on a layered graph.

[[zhu-2023-aoi-transformer-trajectory]] applies this design to AoI-aware UAV collection. Cluster order is learned with REINFORCE and a greedy rollout baseline, while weighted A-star chooses SNR-feasible hover points. The pipeline has no global-optimality or approximation-ratio guarantee in the paper.
