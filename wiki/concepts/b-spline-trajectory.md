---
type: concept
title: "B-Spline Trajectory"
tags: [trajectory, spline, path-planning, uav]
related:
  - "[[uav-trajectory-control]]"
  - "[[peng-2022-cmop-uav-path-planning]]"
  - "[[wu-2026-terrain-aware-uav-mec]]"
created: 2026-05-29
updated: 2026-05-29
---

# B-Spline Trajectory

A smooth UAV flight path defined by a small set of **control points** $\{C P_1, ..., C P_\lambda\}$. The B-spline curve interpolates / approximates these control points, producing a continuously differentiable path with $C^2$ continuity (smooth velocity and acceleration). This is exactly what a UAV's flight controller wants — sharp corners are physically infeasible.

Why this matters for optimization: the trajectory is parameterized by only $3\lambda$ continuous variables (3D coordinates of $\lambda$ control points) instead of arbitrarily many path-point coordinates. A B-spline with $\lambda = 6$ already produces complex paths over hundreds of meters. This shrinks the decision space dramatically — critical for evolutionary trajectory optimization.

Standard in the wiki's evolutionary-trajectory papers: [[peng-2022-cmop-uav-path-planning]] and [[wu-2026-terrain-aware-uav-mec]]. Constraints (turning angle, altitude, terrain clearance) are evaluated at densely-sampled path points $\{B_1, ..., B_J\}$ along the resulting curve.

Contrast with **per-slot trajectory updates** in DRL papers like [[liu-2026-jppo-en-convntm]], which decide a velocity vector each time slot rather than a full path up front.
