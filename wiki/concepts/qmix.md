---
type: concept
title: "QMIX"
tags: [marl, qmix, value-decomposition, ctde, cooperative]
related:
  - "[[value-decomposition-network]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[ma-pomdp]]"
  - "[[ensemble-qmix]]"
  - "[[multi-agent-q-learning]]"
  - "[[shi-2025-aoi-energy-replenishment-multiuav]]"
  - "[[zhang-2026-ensemble-marl-uav-target-search]]"
created: 2026-07-11
updated: 2026-07-11
---

# QMIX

QMIX is a cooperative multi-agent value-decomposition method. It learns per-agent action-value functions and combines them through a monotonic mixing network, so maximizing each local value remains consistent with maximizing the joint team value. This makes it a [[centralized-training-decentralized-execution|CTDE]] method: centralized training can use global information, while each agent executes from its local observation.

In this wiki, [[shi-2025-aoi-energy-replenishment-multiuav]] uses QMIX beside [[value-decomposition-network|VDN]] for AoI-aware multi-UAV data collection and energy replenishment. [[zhang-2026-ensemble-marl-uav-target-search]] builds the specialized [[ensemble-qmix]] variant, where multiple independently trained QMIX networks vote on actions for heterogeneous UAV target search.
