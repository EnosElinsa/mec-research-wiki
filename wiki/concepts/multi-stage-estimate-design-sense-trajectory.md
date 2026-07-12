---
type: concept
title: "Multi-Stage Estimate-Design-Sense Trajectory Loop"
tags: [isac, target-localization, uav-trajectory, sequential-design, estimation]
related:
  - "[[jing-2024-isac-trajectory-localization]]"
  - "[[joint-localization-and-communication]]"
  - "[[cramer-rao-bound]]"
  - "[[uav-trajectory-control]]"
  - "[[rotary-wing-propulsion-energy-model]]"
created: 2026-07-13
updated: 2026-07-13
---

# Multi-Stage Estimate-Design-Sense Trajectory Loop

A sequential ISAC control pattern that updates initially uncertain target states from accumulated measurements, redesigns the next UAV trajectory stage around those estimates, executes communication and sensing, and repeats until an energy or mission termination condition is reached.

[[jing-2024-isac-trajectory-localization]] uses coarse target coordinates to initialize the first stage, grid-search MLE to update static target positions, and SCA/CVX trajectory-bandwidth design for later stages. The loop improves formulation accuracy as information accumulates, but it is local, simulation-based, and distinct from validated moving-target tracking.
