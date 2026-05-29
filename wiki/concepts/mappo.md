---
type: concept
title: "MAPPO (Multi-Agent PPO)"
tags: [drl, multi-agent, on-policy]
related:
  - "[[kang-2023-mappo-hierarchical-aerial]]"
  - "[[ppo]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[masac]]"
created: 2026-05-29
updated: 2026-05-29
---

# MAPPO (Multi-Agent PPO)

The multi-agent extension of [[ppo|Proximal Policy Optimization]]: each agent runs a clipped-objective on-policy actor, typically with a **centralized critic** during training under [[centralized-training-decentralized-execution|CTDE]], so agents act on local observations at execution time. MAPPO inherits PPO's training stability (trust-region-style clipping) and is a common choice when on-policy stability is preferred over the sample efficiency of off-policy methods like [[masac]].

In [[kang-2023-mappo-hierarchical-aerial]] MAPPO solves the joint GD-association, resource-allocation, and UAV→HAP offloading POMDP in a hierarchical aerial computing system, with state normalization and action masking to speed training.
