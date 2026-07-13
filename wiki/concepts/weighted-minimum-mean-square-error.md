---
type: concept
title: "Weighted Minimum Mean-Square Error"
tags: [optimization, beamforming, mimo, sum-rate, block-coordinate-descent]
related:
  - "[[wan-2026-movable-antenna-multiuav-mimo]]"
  - "[[movable-antenna]]"
  - "[[two-level-movable-antenna]]"
created: 2026-07-13
updated: 2026-07-13
---

# Weighted Minimum Mean-Square Error

Weighted minimum mean-square error (WMMSE) reformulates certain multi-user weighted sum-rate problems as equivalent alternating minimization over receive filters, positive error weights, and transmit variables. For fixed transmit variables, the receiver and weight blocks often have closed-form updates; the remaining transmit or geometry block is then handled by an appropriate constrained solver.

[[wan-2026-movable-antenna-multiuav-mimo]] applies this bridge to a multi-UAV uplink whose variables include precoders, BS combiners, whole-UAV positions, and local [[movable-antenna]] positions. It converts the geometry block into regularized least squares over position dictionaries and uses hierarchical group-sparse pursuit to select macro and micro positions.

The equivalence supports an optimization procedure, not global optimality. In the source, greedy dictionary selection and finite position grids further restrict the continuous feasible set; the monotonic convergence claim concerns transformed objective values.
