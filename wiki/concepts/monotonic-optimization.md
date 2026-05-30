---
type: concept
title: "Monotonic Optimization"
tags: [optimization, global-optimum, non-convex, branch-and-bound, robust-optimization]
related:
  - "[[alternating-optimization-sdr-sca]]"
  - "[[mixed-integer-nonlinear-programming]]"
  - "[[csi-estimation-error]]"
  - "[[sun-2024-mfris-semantic-antijamming]]"
created: 2026-05-31
updated: 2026-05-31
---

# Monotonic Optimization

A global-optimization framework for problems whose objective/constraints can be expressed in terms of **monotonic (increasing) functions** over a normal/co-normal feasible set. By exploiting monotonicity, sequential **partitioning / polyblock**-style procedures can converge to the **global optimum** of otherwise non-convex problems, often with fewer feasibility evaluations than generic global solvers.

## In this wiki

- [[sun-2024-mfris-semantic-antijamming]] develops a fast-converging monotonic optimization algorithm combined with **decoupling second-order cone programming (MO-DSOCP)** to globally solve a semantic-computation-rate maximization whose objective is quasi-convex and whose constraints are [[mixed-integer-nonlinear-programming|MINLP]]. It complements the more common [[alternating-optimization-sdr-sca|AO+SDR+SCA]] pipeline, which targets stationary (not necessarily global) points.
