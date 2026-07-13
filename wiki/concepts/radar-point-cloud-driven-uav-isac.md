---
type: concept
title: "Radar-Point-Cloud-Driven UAV ISAC Control"
tags: [uav-isac, radar-point-cloud, deep-reinforcement-learning, trajectory-control, resource-allocation]
related:
  - "[[chen-2026-pointrl-uav-isac]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[mmwave-radar-sensing]]"
  - "[[uav-trajectory-control]]"
created: 2026-07-14
updated: 2026-07-14
---

# Radar-Point-Cloud-Driven UAV ISAC Control

A control pattern in which 3-D radar returns represent target shape and motion directly rather than supplying only estimated point coordinates. [[chen-2026-pointrl-uav-isac]] encodes vehicle range, velocity, and radar-cross-section points, maps them into separate UAV-motion and power action branches, and uses a sliding-window DQN reward to balance communication capacity, radar capacity, and minimum-user performance.
