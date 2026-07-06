---
type: concept
title: "LEO Satellite Coverage Time"
tags: [leo-satellite, constraint, mobility, geometry]
related:
  - "[[leo-satellite-edge-computing]]"
  - "[[walker-star-constellation]]"
  - "[[seamless-handover]]"
  - "[[chen-2024-ulse-game]]"
  - "[[chen-2026-pddqn-sagin-mec]]"
created: 2026-05-29
updated: 2026-07-07
---

# LEO Satellite Coverage Time

The bounded, per-device communication window during which a moving LEO satellite remains reachable by a given ground device. Because LEO satellites orbit fast, this window is short and differs per device; it is derived geometrically from orbit altitude, Earth radius, minimum elevation angle, and satellite velocity. It enters offloading problems as a **hard constraint**: any task offloaded to a satellite must complete (upload + compute) within the device's coverage time.

In the wiki, [[chen-2024-ulse-game]] derives a per-MUD maximum communication time `T_i^L` and enforces `T_i^LEO ≤ T_i^L` on every satellite-offloading decision. It is the per-device, geometric counterpart to the constellation-level coverage modeling in [[walker-star-constellation]], and the same scarcity that motivates [[seamless-handover]] in LEO-based federated learning.

[[chen-2026-pddqn-sagin-mec]] uses the same kind of moving-LEO coverage window in a hybrid-action SAGIN control problem, where IoT devices can split tasks across local, UAV, and LEO execution only when the satellite coverage duration can support the offloaded workload.
