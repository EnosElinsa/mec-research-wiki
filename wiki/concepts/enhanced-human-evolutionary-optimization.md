---
type: concept
title: "Enhanced Human Evolutionary Optimization"
tags: [optimization, evolutionary-algorithm, swarm-intelligence, mixed-variable]
related:
  - "[[liu-2026-heterogeneous-sensor-satisfaction]]"
  - "[[sparrow-search-algorithm]]"
  - "[[whale-optimization-algorithm]]"
  - "[[particle-swarm-optimization]]"
created: 2026-07-13
updated: 2026-11-03
---

# Enhanced Human Evolutionary Optimization

An evolutionary search variant that augments human evolutionary optimization with the follower operator of the sparrow search algorithm and the bubble-net (logarithmic spiral) operator of the whale optimizer; leaders also move by Lévy flights. [[liu-2026-heterogeneous-sensor-satisfaction]] uses mixed real/binary individuals for UAV locations and sensor associations, a penalty term with a punishment factor for constraint violations, and a separate Lagrange-dual power update inside candidate evaluation.

The operators broaden exploration and exploitation empirically, but they do not turn the mixed non-convex problem into an exact method. Claims should therefore be tied to the paper's repeated simulation comparisons and exhaustive small-instance check rather than treated as a global convergence guarantee.
