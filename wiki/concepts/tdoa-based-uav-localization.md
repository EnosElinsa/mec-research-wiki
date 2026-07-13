---
type: concept
title: "TDOA-Based UAV Localization"
tags: [localization, tdoa, uav-swarm, least-squares, sensing-geometry]
related:
  - "[[wang-2026-mat-target-tracking]]"
  - "[[zhu-2024-zdrl-uav-tracking]]"
  - "[[geometric-dilution-of-precision]]"
  - "[[uav-trajectory-control]]"
created: 2026-07-13
updated: 2026-07-13
---

# TDOA-Based UAV Localization

Time-difference-of-arrival (TDOA) localization uses relative signal arrival times at spatially separated UAV receivers. Choosing one receiver as reference converts time differences into range-difference equations; Taylor linearization and least-squares iteration estimate the emitter position.

Accuracy depends on timing error and receiver geometry. [[wang-2026-mat-target-tracking]] models Gaussian LoS error and biased higher-variance NLoS error, then controls UAV formation using [[geometric-dilution-of-precision]]. [[zhu-2024-zdrl-uav-tracking]] provides a related active/passive UAV tracking case with learned trajectories and transmit-power control.
