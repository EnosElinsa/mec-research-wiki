---
type: concept
title: "Bernstein Safe Approximation"
tags: [optimization, chance-constraint, probability, robust-optimization, convex-approximation]
related:
  - "[[li-2026-full-duplex-noma-uav-relay]]"
  - "[[chance-constraint]]"
  - "[[robust-uav-position-power-optimization]]"
  - "[[zhang-2021-safe-dqn-emergency]]"
  - "[[distributed-tabular-q-learning-uav-collision-avoidance]]"
  - "[[uav-trajectory-safety-guarantee-ladder]]"
created: 2026-07-14
updated: 2026-07-14
---

# Bernstein Safe Approximation

A Bernstein safe approximation replaces a Gaussian quadratic [[chance-constraint]] with deterministic convex inequalities derived from a Bernstein-type concentration bound. Feasibility of the replacement is sufficient for the requested probability guarantee, but the reverse need not hold, so the approximation can reserve more margin than necessary.

[[li-2026-full-duplex-noma-uav-relay]] applies this device to rate and relay-ordering constraints under Gaussian UAV-position error, then solves the resulting position and power blocks with SCA. Its numerical reliability margins show scenario-specific conservatism rather than equivalence to the original chance-constrained feasible set.
