---
type: concept
title: "Attention-Based UAV Target Search"
tags: [uav-swarm, target-search, attention, mappo, computation-offloading]
related:
  - "[[zhu-2026-hab-mappo-target-search]]"
  - "[[mappo]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[beta-policy-drl]]"
  - "[[task-offloading]]"
  - "[[uav-trajectory-control]]"
  - "[[uav-charging-scheduling]]"
  - "[[zhang-2026-ensemble-marl-uav-target-search]]"
  - "[[ensemble-qmix]]"
created: 2026-07-07
updated: 2026-07-11
---

# Attention-Based UAV Target Search

[[zhang-2026-ensemble-marl-uav-target-search]] is the non-offloading counterpart: it keeps the focus on heterogeneous fixed-wing/multirotor target search and adds [[ensemble-qmix]] for robust value-decomposition MARL decisions.

A cooperative-search control pattern where UAVs use attention over neighboring agents and environment state to search with a dynamically sized swarm. [[zhu-2026-hab-mappo-target-search]] uses attention inside a MAPPO actor/critic architecture so a UAV can focus on relevant neighbor information, while the critic compresses variable agent features into a fixed-size representation for cross-scale transfer.

The target-search workload couples sensing and computation: each UAV must decide where to fly, whether to charge, and whether each segmented image should be processed locally or offloaded to a BS. This places the concept between [[uav-trajectory-control]], [[task-offloading]], and [[uav-charging-scheduling]] rather than pure path planning.
