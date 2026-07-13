---
type: concept
title: "Memory-Augmented Multi-UAV Navigation"
tags: [multi-uav, navigation, partial-observability, convlstm, multi-agent-reinforcement-learning, data-collection]
related:
  - "[[he-2026-memdrl-uav-navigation]]"
  - "[[ma-pomdp]]"
  - "[[multi-agent-td3]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[prioritized-experience-replay]]"
  - "[[uav-data-collection]]"
  - "[[uav-trajectory-control]]"
  - "[[liu-2021-edivert-mobile-crowdsensing]]"
  - "[[liu-2020-distributed-uav-coverage-navigation]]"
  - "[[ye-2023-graph-uav-coverage]]"
created: 2026-07-13
updated: 2026-07-13
---

# Memory-Augmented Multi-UAV Navigation

Memory-augmented multi-UAV navigation conditions each movement action on a sequence of recent spatial observations rather than one local snapshot. This is useful when limited sensing leaves PoI demand, teammate energy and positions, or prior visits outside the current field of view; obstacles are handled separately through constraints and collision penalties in the cited design.

[[he-2026-memdrl-uav-navigation]] applies ConvLSTM histories to decentralized actors and centralized twin critics. A BeBold-style intrinsic reward promotes first visits to underexplored cells, while fleet-level [[prioritized-experience-replay]] ranks a transition by the sum of UAV TD errors.

Memory does not remove the global-data requirement of [[centralized-training-decentralized-execution|centralized training]], and simulation gains do not by themselves establish flight-dynamics safety. In the cited design, low-level controllers are expected to realize the learned direction-distance waypoints.
