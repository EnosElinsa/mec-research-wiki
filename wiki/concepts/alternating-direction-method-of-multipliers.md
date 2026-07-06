---
type: concept
title: Alternating Direction Method of Multipliers (ADMM)
tags: [optimization, convex-optimization, distributed-optimization, decomposition]
related:
  - "[[two-stage-decomposition]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[penalty-dual-decomposition]]"
  - "[[lyapunov-optimization]]"
  - "[[zeng-2024-usv-fleet-collaborative-offloading]]"
  - "[[zhang-2026-dwell-time-aerial-vec]]"
created: 2026-05-31
updated: 2026-07-06
---

# Alternating Direction Method of Multipliers (ADMM)

A first-order optimization method that solves problems with **separable structure** by splitting the variables into blocks, forming an **augmented Lagrangian**, and alternately minimizing over each block before updating the dual (multiplier) variables. Because the per-block updates can run in parallel, ADMM scales to large problems and converges under standard convexity/closedness conditions, often with a penalty parameter that trades off primal vs dual feasibility.

## Why MEC research reaches for it

- Offloading/resource-allocation problems frequently separate into per-node or per-decision blocks (e.g. subtask allocation vs computation-capacity allocation), which is exactly ADMM's sweet spot.
- Its parallel structure reduces computational complexity versus solving the coupled problem directly, and the dynamic-penalty variants improve convergence speed.

## In this wiki

- [[zeng-2024-usv-fleet-collaborative-offloading]] decomposes its energy-minimization problem via **Block Coordinate Descent** into two subproblems, each solved by an **ADMM improved with dynamic penalty coefficients**, exploiting ADMM's parallelism to cut complexity and guarantee convergence of the inner loop.
- [[zhang-2026-dwell-time-aerial-vec]] uses an ADMM-style resource-allocation component inside a BCD solution for dwell-time-constrained aerial VEC.

It complements the corpus's other decomposition/convex-pipeline tools — [[two-stage-decomposition]], [[alternating-optimization-sdr-sca]], and [[penalty-dual-decomposition]] — and is often paired with [[lyapunov-optimization]] as a per-slot solver.
