---
type: concept
title: "Continuous Omnidirectional Monitoring"
tags: [uav, surveillance-camera, visual-coverage, monitoring-utility, deployment]
related:
  - "[[zhang-2026-omnidirectional-monitoring-deployment]]"
  - "[[path-aware-3d-visual-coverage]]"
  - "[[geometric-disk-cover]]"
  - "[[uav-trajectory-control]]"
created: 2026-07-12
updated: 2026-07-12
---

# Continuous Omnidirectional Monitoring

Continuous omnidirectional monitoring evaluates how long every target is observed from every horizontal viewing direction. For each target-direction pair, its utility unions the monitoring intervals contributed by all selected devices, normalizes by task duration, and then averages over directions and targets, so simultaneous overlapping views are counted once.

[[zhang-2026-omnidirectional-monitoring-deployment]] jointly selects rented fixed-camera strategies and mobile UAV position, orientation, route, and departure time. This couples directional [[path-aware-3d-visual-coverage|visual coverage]] to travel delay, energy, obstacle avoidance, and camera budget rather than treating a covered target as a one-time binary event.

The metric is only as faithful as its visibility model. A sector field of view over a planar projection does not itself capture recognition quality, three-dimensional occlusion, lighting, link latency, or the value of redundant simultaneous observations.
