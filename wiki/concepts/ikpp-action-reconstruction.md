---
type: concept
title: "IKPP Action Reconstruction"
tags: [reinforcement-learning, resource-allocation, vehicle-association]
related:
  - "[[wang-2026-ikpp-vehicular-uav]]"
  - "[[ppo]]"
  - "[[device-association]]"
created: 2026-07-13
updated: 2026-07-13
---

# IKPP Action Reconstruction

A hybrid action pipeline that turns a continuous policy output into mixed continuous/discrete network controls. PPO proposes UAV motion, vehicle powers, and per-UAV carrier scores; a load-constrained nearest-UAV heuristic derives association; carrier scores are then converted into binary assignments.

In [[wang-2026-ikpp-vehicular-uav]], the association step is called improved k-means but does not update centroids. The reconstruction enforces service-load and carrier-count structure, while QoS, boundary, and collision requirements remain reward penalties rather than hard feasibility guarantees.
