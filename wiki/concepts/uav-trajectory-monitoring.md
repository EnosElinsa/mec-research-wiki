---
type: concept
title: "UAV Trajectory Monitoring"
tags: [isac, uav, target-tracking, trajectory-estimation]
related:
  - "[[yan-2026-uav-trajectory-monitoring]]"
  - "[[yan-not-in-parse-multibs-isac-uav-trajectory]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[networked-isac]]"
created: 2026-07-14
updated: 2026-07-14
---

# UAV Trajectory Monitoring

The sensing-side task of discovering a UAV, associating repeated observations with the correct track, estimating its motion state, and predicting its next position so sensing beams can maintain a complete trajectory history. This is distinct from [[uav-trajectory-control]], where the UAV itself chooses a path.

[[yan-2026-uav-trajectory-monitoring]] implements the task at one three-array ISAC base station through motion-parameter estimation, inter-array coordinate registration, position-and-velocity association, and multiple-model filtering. [[yan-not-in-parse-multibs-isac-uav-trajectory]] extends the monitoring line to asynchronous multi-BS feature fusion and sequential UKF tracking.
