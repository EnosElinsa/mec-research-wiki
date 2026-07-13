---
type: concept
title: "Dual-Objective Multi-UAV ISAC Optimization"
tags: [isac, multi-uav, multi-objective, pareto, trajectory-optimization]
related:
  - "[[guo-2026-dual-objective-multiuav-isac]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[constrained-multi-objective-evolutionary-algorithm]]"
  - "[[cramer-rao-bound]]"
  - "[[uav-trajectory-control]]"
created: 2026-07-13
updated: 2026-07-13
---

# Dual-Objective Multi-UAV ISAC Optimization

Dual-objective multi-UAV ISAC optimization keeps communication utility and sensing accuracy as separate objectives while jointly controlling aerial mobility and radio/sensing assignments. The result is a Pareto set rather than one fixed-weight solution, allowing an operator to inspect how added communication rate increases target-estimation error or vice versa.

In [[guo-2026-dual-objective-multiuav-isac]], the objectives are average user sum rate and aggregate target-location [[cramer-rao-bound|CRB]]. Trajectories, powers, user associations, and target associations are mixed variables, and an archive-guided [[constrained-multi-objective-evolutionary-algorithm]] approximates the feasible non-dominated front under mobility, collision, rate, and sensing-frequency constraints.
