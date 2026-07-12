---
type: concept
title: "Path-Aware 3-D Visual Coverage"
tags: [uav, visual-coverage, viewpoint-planning, trajectory-optimization, energy-model]
related:
  - "[[gong-2026-uav-3d-visual-coverage]]"
  - "[[uav-trajectory-control]]"
  - "[[b-spline-trajectory]]"
  - "[[rotary-wing-propulsion-energy-model]]"
  - "[[energy-latency-tradeoff]]"
  - "[[zhang-2026-omnidirectional-monitoring-deployment]]"
  - "[[zhou-2026-gl-ahg-coverage-planning]]"
created: 2026-07-10
updated: 2026-07-13
---

# Path-Aware 3-D Visual Coverage

A UAV sensing-planning pattern where viewpoint selection and flight-path energy are optimized together. The planner cannot choose viewpoints greedily and route them afterward, because a visually complete viewpoint set can still force an expensive or dynamically awkward path.

[[gong-2026-uav-3d-visual-coverage]] is the corpus anchor. It combines overlapping-field-of-view viewpoint generation with energy-aware routing, B-spline SE(3) smoothing, and propulsion-energy minimization. The useful distinction is between distance-optimal and energy-optimal paths: a shorter path is not necessarily cheaper when rotary-wing speed, acceleration, and flight time all affect propulsion energy.

[[zhou-2026-gl-ahg-coverage-planning]] pushes the coupling upstream: an energy proxy weights candidate terrain waypoints before a game-learning weighted-vertex-cover step, and an alternating hierarchical [[genetic-algorithm]] then trades path length against that energy proxy. Its B-spline represents terrain rather than the UAV trajectory, and its linear distance/angle energy model is less physically detailed than a propulsion model.

This concept is adjacent to [[uav-trajectory-control]] rather than MEC offloading. It is relevant when UAV sensing papers need complete coverage of a physical object, and when [[rotary-wing-propulsion-energy-model]] assumptions change the interpretation of "optimal" trajectory.
