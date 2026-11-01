---
type: concept
title: "Battery Swapping in UAV-MEC"
tags: [uav, energy, mec, battery-swapping]
related:
  - "[[uav-trajectory-control]]"
  - "[[task-offloading]]"
  - "[[uav-charging-scheduling]]"
  - "[[rotary-wing-propulsion-energy-model]]"
  - "[[ye-2026-flight-speed-battery-swapping]]"
  - "[[in-flight-uav-energy-replenishment]]"
  - "[[li-2026-battery-mule-uav-swarm-scheduling]]"
  - "[[li-2026-two-timescale-uav-replacement-hap]]"
created: 2026-07-07
updated: 2026-11-02
---

# Battery Swapping in UAV-MEC

Battery swapping treats UAV energy replenishment as a discrete infrastructure decision: the UAV returns to a station, replaces its battery, and resumes the mission with a new energy state. This differs from [[uav-charging-scheduling]], energy harvesting, or wireless power transfer because the decision has route, delay, replacement-cost, and battery-mass consequences.

In [[ye-2026-flight-speed-battery-swapping]], battery swaps are optimized together with flight-speed scheduling and [[task-offloading]]. The key modeling point is that a heavier or more capable battery can reduce total operational cost when it avoids enough swap overhead, while a lighter battery may force extra station visits even if the airframe consumes less propulsion energy per segment.

Airborne alternatives avoid the return flight: [[li-2026-battery-mule-uav-swarm-scheduling]] uses battery mules that swap batteries in the air, one branch of [[in-flight-uav-energy-replenishment]]. [[li-2026-two-timescale-uav-replacement-hap]] keeps station-based replacement but lets a substituting UAV or the HAP absorb the replaced UAV's devices, decided on a slow timescale by a stochastic game.
