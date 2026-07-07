---
type: concept
title: "Value Decomposition Network (VDN)"
tags: [drl, multi-agent, cooperative, value-decomposition]
related:
  - "[[ddqn]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[ma-pomdp]]"
  - "[[raivi-2024-jdaco-postdisaster-iot]]"
  - "[[zhu-2026-uav-localization-jamming]]"
created: 2026-06-01
updated: 2026-07-07
---

# Value Decomposition Network (VDN)

A cooperative multi-agent value-based method that learns a **joint** team action-value as the **sum of per-agent value functions**, so the centralized team objective can be trained while each agent still acts greedily on its own local value at execution (a [[centralized-training-decentralized-execution|CTDE]]-compatible factorization). It lets agents share experiences and learn coordinated behavior without a monolithic joint-action value table.

In this wiki, [[raivi-2024-jdaco-postdisaster-iot]] combines VDN with a dueling double DQN ([[ddqn]]) into **VD3QN** for cooperative learning across multiple UAVs in its joint data-aggregation + offloading scheme, where the agents jointly minimize aggregation/offloading cost while maximizing IoT-device coverage.

[[zhu-2026-uav-localization-jamming]] uses VD-RL as an expectation-based comparison point for mixture-Gaussian distributional collaborative RL in UAV localization under jamming.
