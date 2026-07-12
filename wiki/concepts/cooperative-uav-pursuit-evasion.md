---
type: concept
title: "Cooperative UAV Pursuit-Evasion"
tags: [uav, anti-uav, pursuit-evasion, hierarchical-reinforcement-learning, multi-agent-rl]
related:
  - "[[yang-2025-hcdrl-pursuit-evasion]]"
  - "[[hierarchical-reinforcement-learning]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[autonomous-uav-swarms]]"
  - "[[zhang-2025-cooperative-anti-uav-isac]]"
created: 2026-07-12
updated: 2026-07-12
---

# Cooperative UAV Pursuit-Evasion

Cooperative UAV pursuit-evasion coordinates several counter-UAVs to restrict, surround, and capture an agile target while penalizing inter-vehicle and obstacle conflicts. The control problem combines adversarial motion, formation geometry, collision avoidance objectives, and a finite capture horizon.

[[yang-2025-hcdrl-pursuit-evasion]] uses [[hierarchical-reinforcement-learning]] to select among Approach, Expand, Surround, Enclose, and Capture subtasks, then executes continuous accelerations with lower CTDE policies. This is a physical-interception counterpart to the sensing and beamforming layer in [[zhang-2025-cooperative-anti-uav-isac]]; the pursuit model assumes ideal communication rather than optimizing the supporting wireless network.
