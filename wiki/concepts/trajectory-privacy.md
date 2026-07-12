---
type: concept
title: "Trajectory Privacy"
tags: [uav, privacy, trajectory, low-altitude-economy]
related:
  - "[[uav-trajectory-control]]"
  - "[[low-altitude-intelligent-network]]"
  - "[[privacy-sensitive-data-partitioning]]"
  - "[[compliance-aware-uav-trajectory]]"
  - "[[wu-2026-service-oriented-segmented-trajectory]]"
  - "[[wu-2026-parallel-cooperative-charging]]"
  - "[[parallel-cooperative-uav-charging]]"
created: 2026-07-07
updated: 2026-07-12
---

# Trajectory Privacy

A trajectory-design constraint that treats where a UAV flies and what it can visually expose as part of the privacy model. In facade-adjacent or dense urban settings, a route can be efficient for energy and communication while still violating privacy if it crosses windows or public-sensitive regions.

In [[wu-2026-service-oriented-segmented-trajectory]], the metric is the trajectory privacy preservation level, based on how many privacy-sensitive smart windows are crossed by UAV routes. TRA and SOS-TRA refine service paths to avoid those crossings, turning privacy from an after-the-fact policy concern into a route-feasibility and utility term. It is adjacent to [[compliance-aware-uav-trajectory]], but narrower: trajectory privacy focuses on visual exposure, while compliance-aware planning also includes no-fly zones, obstacles, speed limits, and landing constraints.

[[wu-2026-parallel-cooperative-charging]] adds an adjacent privacy mechanism rather than a trajectory constraint: its Section VI extension requires each nonempty charging group to contain at least `K` UAVs so station observations do not isolate one UAV's path or target. The paper assumes anonymity already exists on station entry, so this group-size rule is narrower than full trajectory privacy.
