---
type: concept
title: "Selective Uniform-Cost Search"
tags: [graph-search, trajectory-planning, branch-and-bound, cellular-connected-uav]
related:
  - "[[ren-2026-movable-antenna-uav-trajectory]]"
  - "[[cellular-connected-uav]]"
  - "[[uav-trajectory-control]]"
  - "[[movable-antenna]]"
created: 2026-07-13
updated: 2026-07-13
---

# Selective Uniform-Cost Search

Selective uniform-cost search (SUCS) is the grid-path method used in [[ren-2026-movable-antenna-uav-trajectory]]. A node's priority combines accumulated mission time with a lower bound on the remaining flight time. Expansion also carries communication state: movable-array positions, serving-BS choice, and feasibility under a lower bound on expected SINR.

The selective part prunes candidate histories according to progress and a bounded retention parameter, limiting the growth caused by multiple antenna/association states reaching the same grid point. At each retained state, MMSE combining and a local feasible-direction antenna update determine whether the Jensen lower bound on expected SINR keeps onward edges feasible.

Its optimality proposition depends on the remaining-time term being a valid lower bound. In practical use, grid discretization, state pruning, and locally optimized antenna positions make SUCS a controlled-complexity trajectory heuristic rather than a global solver for the original continuous problem.
