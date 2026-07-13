---
type: concept
title: "Multi-Location Hovering"
tags: [uav-trajectory, wireless-power-transfer, lagrange-duality, fairness]
related:
  - "[[xie-2021-uav-wpt-tutorial]]"
  - "[[xu-2018-uav-wpt-trajectory]]"
  - "[[successive-hover-and-fly-trajectory]]"
  - "[[uav-trajectory-control]]"
created: 2026-07-14
updated: 2026-07-14
---

# Multi-Location Hovering

A speed-relaxed UAV trajectory structure represented by a finite set of service locations and optimized dwell times. Lagrange duality and a linear program can recover an optimum for time-sharing formulations such as max-min wireless power delivery, WPCN throughput, or simplified wireless-powered MEC.

Because travel time is removed, the result is generally an upper bound rather than a feasible finite-speed route. [[xie-2021-uav-wpt-tutorial]] uses it as the structural starting point for [[successive-hover-and-fly-trajectory|successive hover-and-fly]], which connects the hover points at maximum speed and reallocates the remaining mission time to dwell periods.
