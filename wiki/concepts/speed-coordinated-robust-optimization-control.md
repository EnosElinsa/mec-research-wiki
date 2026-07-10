---
type: concept
title: "Speed-Coordinated Robust Optimization Control"
tags: [its, cav, robust-optimization, emergency-vehicle-priority, pso]
related:
  - "[[zang-2026-uav-ev-priority-cav-speed]]"
  - "[[uav-enabled-its]]"
  - "[[uav-data-collection]]"
  - "[[particle-swarm-optimization]]"
  - "[[vehicular-mec]]"
created: 2026-07-10
updated: 2026-07-10
---

# Speed-Coordinated Robust Optimization Control

An ITS coordination pattern where connected vehicles adjust speed to create usable gaps for uncertain human-driven vehicles. In [[zang-2026-uav-ev-priority-cav-speed]], UAVs provide sensing and relaying, but the decisive control action is CAV speed adjustment around an emergency vehicle.

The robust part comes from human uncertainty. Lane-change timing and duration are not fixed, so the controller searches over worst-case human responses while choosing which objective-lane CAV should slow or recover and when the evacuation-lane CAV should adjust. The paper solves this min-max structure with a dual-layer [[particle-swarm-optimization]] procedure and recomputes it in a rolling horizon after lane changes occur.

This concept is adjacent to [[vehicular-mec]] and [[uav-enabled-its]], but it is not an offloading mechanism. It uses UAV infrastructure as a traffic-state collector and coordinator for emergency-vehicle priority.
