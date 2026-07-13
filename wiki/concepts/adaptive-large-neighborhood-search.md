---
type: concept
title: "Adaptive Large Neighborhood Search"
tags: [optimization, metaheuristic, routing, destroy-repair]
related:
  - "[[zhang-2026-msialns-air-ground-inspection]]"
  - "[[vehicle-uav-collaborative-inspection]]"
  - "[[genetic-algorithm]]"
created: 2026-07-13
updated: 2026-07-13
---

# Adaptive Large Neighborhood Search

Adaptive large neighborhood search repeatedly destroys part of a feasible solution and repairs it with one of several operators, updating operator preferences from observed search performance. It is useful for routing and scheduling problems whose coupled constraints make exact optimization difficult.

[[zhang-2026-msialns-air-ground-inspection]] specializes this pattern to a bi-layer vehicle-UAV schedule. Its operators remove congested ground nodes, similar task regions, expensive components, or dependent UAV task chains, then reconstruct schedules with greedy, regret, or randomized insertion while preserving launch/recovery feasibility.
