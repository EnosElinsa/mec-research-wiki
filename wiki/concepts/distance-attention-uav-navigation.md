---
type: concept
title: "Distance-Attention UAV Navigation"
tags: [uav-navigation, attention, lidar, multi-agent-reinforcement-learning, collision-avoidance]
related:
  - "[[zhang-2026-distance-attention-uav-navigation]]"
  - "[[ma-pomdp]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[maddpg]]"
  - "[[autonomous-uav-swarms]]"
  - "[[uav-trajectory-control]]"
created: 2026-07-13
updated: 2026-07-13
---

# Distance-Attention UAV Navigation

Distance-attention UAV navigation weights range-sensor layers according to their current distances and recent temporal context before selecting a motion action. It lets a policy emphasize the vertical portions of a local obstacle profile that matter to the current maneuver instead of flattening every LiDAR ray with equal importance.

[[zhang-2026-distance-attention-uav-navigation]] applies Softmax attention across three vertical LiDAR layers using projected range features and the prior LSTM hidden state. A separate historical-feature-flow critic fuses current global observation-action features with queued global observations during [[centralized-training-decentralized-execution|centralized training]], while each actor executes from local input.

Attention improves feature selection but does not impose a safety guarantee. Fixed-ray sensor coverage, delayed or lost neighbor messages, larger or heterogeneous swarms, and the absence of physical validation remain limitations; reward penalties do not guarantee collision avoidance or connectivity.
