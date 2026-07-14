---
type: concept
title: "Energy-Constrained UAV Data-Collection Orienteering"
tags: [uav, data-collection, orienteering, approximation-algorithm, route-planning]
related:
  - "[[li-2023-energy-constrained-uav-data-collection]]"
  - "[[uav-data-collection]]"
  - "[[uav-trajectory-control]]"
  - "[[constraint-regimes-in-uav-data-collection]]"
created: 2026-07-12
updated: 2026-07-14
---

# Energy-Constrained UAV Data-Collection Orienteering

Energy-constrained UAV data-collection orienteering treats useful hover regions as reward-bearing vertices in a depot-returning tour. Edge costs represent flight energy and vertex costs represent hover/transfer energy; the objective chooses a feasible subset whose collected data volume is maximal under one battery budget.

[[li-2023-energy-constrained-uav-data-collection]] applies this structure after discretizing the hovering plane. Full collection gives one reward/cost pair per location, while partial collection expands a location into ordered virtual sojourn increments. For non-overlapping coverage sets, metric-orienteering approximations can carry formal guarantees. When coverage overlaps, rewards become selection-dependent residual data, so the paper switches to greedy marginal-data-per-added-energy heuristics with repeated Christofides tours.

The distinction between non-overlap and overlap is structural: overlapping hover circles destroy fixed independent vertex rewards. Grid resolution and partial-level count also trade solution fidelity against runtime, so discretization parameters are part of the algorithmic design rather than neutral simulation settings.
