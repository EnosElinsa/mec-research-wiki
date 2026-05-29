---
type: concept
title: "Self-Adaptive Global-Best Harmony Search (SGHS)"
tags: [optimization, metaheuristic, resource-allocation]
related:
  - "[[whale-optimization-algorithm]]"
  - "[[multi-verse-optimizer]]"
  - "[[gao-2024-sagin-perception-offloading]]"
created: 2026-05-29
updated: 2026-05-29
---

# Self-Adaptive Global-Best Harmony Search (SGHS)

A music-inspired metaheuristic (a variant of Harmony Search) that improvises new candidate solutions ("harmonies") by drawing from a harmony memory, with a **self-adaptive** distance bandwidth and **normally-distributed** harmony-memory-considering rate (HMCR) and pitch-adjusting rate (PAR). The "global-best" element biases new harmonies toward the best-so-far solution to speed convergence.

In the wiki, [[gao-2024-sagin-perception-offloading]] uses SGHS (Algorithm 1) to solve the base-station compute-resource-allocation subproblem (P3) inside its DRL-plus-Lyapunov pipeline, reporting robust convergence across HMCR∈{0.4,0.9} / PAR∈{0.1,0.4} (HMCR=0.9 fastest). It is one of several metaheuristics in the corpus's optimization track, alongside the [[whale-optimization-algorithm]], [[binary-whale-optimization]], and [[multi-verse-optimizer]].
