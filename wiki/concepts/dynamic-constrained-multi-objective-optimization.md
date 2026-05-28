---
type: concept
title: Dynamic Constrained Multi-Objective Optimization (DCMOO)
tags: [optimization, multi-objective, evolutionary]
related:
  - "[[xie-2026-uav-multisource-fusion]]"
  - "[[lyapunov-optimization]]"
created: 2026-05-28
updated: 2026-05-28
---

# Dynamic Constrained Multi-Objective Optimization (DCMOO)

A class of optimization problems where:

- **Multi-objective:** more than one objective (reliability, latency, energy, fairness) — no scalar argmax; need Pareto-front analysis.
- **Constrained:** explicit feasibility constraints, not just bounds.
- **Dynamic:** objectives, constraints, or both *change over time* — feasible region drifts, optima move.

In MEC, DCMOO arises whenever the underlying environment (vehicle positions, channel conditions, task arrivals) evolves and the controller must maintain Pareto optimality over a moving target.

## Solver families

- **Evolutionary multi-objective optimizers** (NSGA-II, MOEA/D, RVEA) — population-based; naturally produce a Pareto front; restart-warm well across drift cycles. Used in [[xie-2026-uav-multisource-fusion]].
- **Online convex / Lyapunov methods** — turn long-term constraints into per-slot drift-plus-penalty subproblems. Better when each slot is convex; struggles when the Pareto front shifts non-locally. See [[lyapunov-optimization]].
- **DRL-based multi-objective** — trains a policy on a parameterized scalarization; can adapt online but slower to re-converge after drift.

## When to pick which

- **Evolutionary** — drift is fast, problem is non-convex, you need an explicit Pareto front.
- **Lyapunov** — drift is moderate, per-slot subproblem is convex, you need analytical guarantees.
- **DRL** — drift is slow relative to training, you have offline simulation budget.

## In this wiki

[[xie-2026-uav-multisource-fusion]] is the first DCMOO entry — chooses evolutionary because the V-MEC environment shifts faster than DRL can re-train. Most other curated sources sit in the DRL or Lyapunov-DRL families.
