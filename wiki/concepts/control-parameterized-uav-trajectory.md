---
type: concept
title: "Control-Parameterized UAV Trajectory"
tags: [uav-trajectory, control, trajectory-optimization, isac]
related:
  - "[[li-2026-control-based-uav-isac]]"
  - "[[uav-trajectory-control]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[alternating-optimization-sdr-sca]]"
created: 2026-07-10
updated: 2026-07-10
---

# Control-Parameterized UAV Trajectory

Control-parameterized UAV trajectory design represents the UAV path through control inputs in a dynamic state-space model rather than only through discrete waypoint positions. The optimizer chooses parameters for piecewise control functions, then the UAV states and trajectory follow from the dynamics.

In [[li-2026-control-based-uav-isac]], this is used for UAV-enabled [[integrated-sensing-and-communication|ISAC]] trajectory planning. Given beamforming variables, the trajectory subproblem becomes an optimal-control problem; piecewise constant control parameterization and exact penalties transform it into a nonlinear program solved by SQP. The point is practical trackability: a planned ISAC path should satisfy sensing constraints after the UAV dynamics and controller are considered, not only in a kinematic waypoint model.
