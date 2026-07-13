---
type: concept
title: "Primal-Dual Constrained MARL"
tags: [multi-agent-reinforcement-learning, constrained-reinforcement-learning, primal-dual, lagrangian]
related:
  - "[[li-2026-credit-aware-uav-irs-secrecy]]"
  - "[[safe-reinforcement-learning]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[masac]]"
  - "[[shapley-value-marl-credit-assignment]]"
created: 2026-07-14
updated: 2026-07-14
---

# Primal-Dual Constrained MARL

Primal-dual constrained MARL optimizes agent policies while learning a Lagrange multiplier for an expected-cost constraint. Policy parameters form the primal variables; the dual variable raises the penalty when learned behavior exceeds the allowed cost and relaxes it when the constraint is satisfied.

In [[li-2026-credit-aware-uav-irs-secrecy]], each UAV-IRS has reward critics, constraint critics, and a multiplier. A binary cost represents non-cooperative coalition behavior, while a decreasing allowance progressively tightens the cooperation constraint around the individualized rewards from [[shapley-value-marl-credit-assignment]].

This mechanism enforces a learned expectation, not a hard per-step safety guarantee. Constraint satisfaction depends on critic accuracy, multiplier dynamics, cost definition, and training coverage; the supporting study reports simulation-based local policies rather than formal feasibility under distribution shift.
