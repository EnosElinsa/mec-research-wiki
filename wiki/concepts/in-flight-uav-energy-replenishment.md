---
type: concept
title: "In-Flight UAV Energy Replenishment"
tags: [uav, energy, wireless-power-transfer, battery-swapping, service-continuity]
related:
  - "[[uav-charging-scheduling]]"
  - "[[battery-swapping-uav-mec]]"
  - "[[wireless-power-transfer]]"
  - "[[simultaneous-wireless-information-and-power-transfer]]"
  - "[[zhu-2022-aerial-refueling-uav-charging]]"
  - "[[yan-2025-in-flight-uav-charging-distance]]"
  - "[[li-2026-battery-mule-uav-swarm-scheduling]]"
created: 2026-11-02
updated: 2026-11-02
---

# In-Flight UAV Energy Replenishment

Replenishing a working UAV's energy from another aircraft while it stays airborne, so that the mission or service does not pause for a return to a ground station. A dedicated supply UAV either transfers energy wirelessly to the working UAV or physically swaps its battery. The supply UAV's own energy budget, the distance between the two aircraft, and the order in which working UAVs are served determine how much service time is gained.

## In this wiki

- **Wireless charging by charging UAVs.** [[zhu-2022-aerial-refueling-uav-charging]] splits a fleet into charging UAVs and mission UAVs and learns charging routes and targets with DDPG and MADDPG to minimize data-collection completion time. [[yan-2025-in-flight-uav-charging-distance]] studies the link itself: with a fixed transmitter energy budget and a minimum communication rate, received energy peaks at a distance inside the Fresnel zone, for both aligned and fly-by charging.
- **Airborne battery swapping by mules.** [[li-2026-battery-mule-uav-swarm-scheduling]] assigns recipients to several battery mules with load balancing and schedules each mule with a time-constrained TSP to maximize the swarm's continuous service ratio.

The concept differs from ground-based [[uav-charging-scheduling]] and station-based [[battery-swapping-uav-mec]], where the working UAV leaves its position and a replacement or service gap must be planned.
