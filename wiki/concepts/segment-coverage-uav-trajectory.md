---
type: concept
title: "Segment-Coverage UAV Trajectory"
tags: [uav, trajectory-planning, set-cover, radio-tomography, measurement-design]
related:
  - "[[chakraborty-2026-skyscale-rti-deployment]]"
  - "[[radio-tomographic-attenuation-mapping]]"
  - "[[rank-saturation-rem-updates]]"
  - "[[uav-trajectory-control]]"
  - "[[information-driven-uav-spectrum-mapping]]"
created: 2026-07-14
updated: 2026-07-14
---

# Segment-Coverage UAV Trajectory

A segment-coverage UAV trajectory chooses measurement locations to expose as many previously unseen terrain segments as possible within a flight-distance budget. A distance-weighted greedy set-cover rule values new ray-segment intersections while penalizing travel from the current position, turning flight planning into measurement design for radio tomography.

[[chakraborty-2026-skyscale-rti-deployment]] calibrates a minimum movement distance from terrain statistics and uses the trajectory to support [[radio-tomographic-attenuation-mapping]]. The greedy route has no global optimality guarantee, and its coverage objective does not directly model flight dynamics, propulsion energy, occlusion uncertainty, or the final radio-map error.
