---
type: concept
title: "Convex-TSP UAV Data Collection"
tags: [trajectory-planning, data-collection, traveling-salesman-problem, convex-optimization]
related:
  - "[[hsu-2022-collision-avoidance-trajectory]]"
  - "[[uav-data-collection]]"
  - "[[uav-trajectory-control]]"
  - "[[bi-traveling-salesman-problem-with-neighborhoods]]"
created: 2026-07-14
updated: 2026-07-14
---

# Convex-TSP UAV Data Collection

Convex-TSP UAV data collection plans a route between distinct fixed endpoints that must enter heterogeneous communication neighborhoods around assigned devices. An auxiliary no-return traveling-salesman problem fixes the device order, convex subproblems place each contact point inside its disk, and iterative local refinement shortens the resulting piecewise-linear path.

In [[hsu-2022-collision-avoidance-trajectory]], the route covers a UAV's return leg after cargo delivery. It is distinct from [[bi-traveling-salesman-problem-with-neighborhoods]], which couples two coordinated tours, and it does not jointly optimize device association or online collision avoidance.
