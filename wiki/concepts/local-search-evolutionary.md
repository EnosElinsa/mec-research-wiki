---
type: concept
title: "Local Search in Evolutionary Algorithms"
tags: [evolutionary, memetic, local-search, hybrid]
related:
  - "[[constrained-multi-objective-evolutionary-algorithm]]"
  - "[[huang-2023-mu-aec-task-energy]]"
created: 2026-05-29
updated: 2026-05-29
---

# Local Search in Evolutionary Algorithms

A hybrid technique (often called "memetic algorithm") that augments the global search of an evolutionary algorithm with a **local refinement** step on selected individuals. The local search uses problem-specific information — gradients, neighborhood moves, or objective-aware heuristics — to push individuals toward nearby local optima before the next generation.

Used in [[huang-2023-mu-aec-task-energy]] for multi-UAV interdependent task scheduling. The local-search step there exploits the DAG structure: rather than mutating any task assignment, it swaps tasks between UAVs in ways that respect predecessor ordering and reduce the makespan locally.

Trade-off: local search per individual is computationally expensive, so it's typically applied only to a subset (best-by-objective, or random fraction) per generation. When the global search is **slow to converge** in a large feasible region with sparse Pareto front (typical for DAG scheduling), the speedup pays for itself.
