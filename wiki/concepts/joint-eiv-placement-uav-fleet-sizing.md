---
type: concept
title: "Joint EIV Placement and UAV Fleet Sizing"
tags: [uav-scheduling, facility-location, fleet-sizing, deadline, mobile-edge-computing]
related:
  - "[[huang-2026-slim-eiv-uav-fleet]]"
  - "[[edge-intelligent-vehicle]]"
  - "[[two-stage-decomposition]]"
  - "[[energy-latency-tradeoff]]"
  - "[[rotary-wing-propulsion-energy-model]]"
created: 2026-07-14
updated: 2026-07-14
---

# Joint EIV Placement and UAV Fleet Sizing

Joint EIV placement and UAV fleet sizing minimizes ground-hub plus aircraft deployment cost while enforcing task deadlines and UAV energy limits. EIV locations determine route segmentation, communication distance, and where data are processed; each segment then needs a fleet size, common speed, and ordered task schedule.

SLIM+ in [[huang-2026-slim-eiv-uav-fleet]] uses outer dynamic programming over segment boundaries and an inner exact or approximation scheduling solver. The outer recurrence is exact only for the supplied segment costs, while the default scalable inner solver is approximate and speed is searched on a discrete grid; the complete workflow is therefore not a proof of global optimality for the original continuous problem.
