---
type: concept
title: "CMOEA/D-CDP"
tags: [evolutionary, multi-objective, decomposition, constraint-handling]
related:
  - "[[constrained-multi-objective-evolutionary-algorithm]]"
  - "[[peng-2024-energy-time-uav-its]]"
  - "[[huang-2023-mu-aec-task-energy]]"
created: 2026-05-29
updated: 2026-05-29
---

# CMOEA/D-CDP

A constrained-multi-objective evolutionary algorithm based on **decomposition** with the **constrained domination principle (CDP)** for constraint handling. The decomposition part (MOEA/D) splits the multi-objective problem into many scalarized single-objective subproblems via weight vectors, evolved together so neighboring weights share information. CDP defines a custom dominance: feasible-over-infeasible, then constraint-violation magnitude, then standard Pareto domination.

Why it's the wiki's go-to evolutionary backbone: decomposition naturally produces a diverse front, and CDP gives a clean rule for handling infeasibility. The Peng/Huang lineage builds on top of it with:

- **Infeasibility-utilization** ([[peng-2022-cmop-uav-path-planning]]) — keep useful infeasible individuals.
- **Repair** ([[peng-2024-energy-time-uav-its]], [[huang-2025-cmop-dispersed-computing]]) — surgically fix violations.
- **Local search** ([[huang-2023-mu-aec-task-energy]]) — accelerate convergence.
- **Multi-tasking** ([[wu-2026-terrain-aware-uav-mec]]) — co-evolve related subtasks.

Each variant is a different answer to "how do you make CMOEA/D-CDP find a wider, better-converged front faster on UAV-MEC problems."
