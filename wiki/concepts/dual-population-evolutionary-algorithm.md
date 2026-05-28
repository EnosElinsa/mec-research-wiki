---
type: concept
title: "Dual-Population Evolutionary Algorithm"
tags: [evolutionary, constrained-optimization, exploration-exploitation]
related:
  - "[[constrained-multi-objective-evolutionary-algorithm]]"
  - "[[infeasible-individual-utilization]]"
  - "[[huang-2025-cmop-dispersed-computing]]"
created: 2026-05-29
updated: 2026-05-29
---

# Dual-Population Evolutionary Algorithm

A constrained-MOEA variant that maintains **two co-evolving populations** with complementary roles:

- **Main population** — feasibility-focused; converges toward the Pareto front under a strict constraint-handling rule.
- **Auxiliary population** — diversity-focused; explores broader regions including infeasible space.

The two exchange information periodically (immigration of best-performing individuals), so the auxiliary population keeps the main population from collapsing into a narrow region of the front.

Used in [[huang-2025-cmop-dispersed-computing]] alongside a **repairing** constraint-handling technique: the main population is repaired into feasibility, the auxiliary population stays unrestricted, and crossover between them injects fresh material.

A different design point from the **single-population infeasibility-allocation** scheme of [[peng-2022-cmop-uav-path-planning]] and from the **multi-tasking** scheme of [[wu-2026-terrain-aware-uav-mec]] / [[multi-tasking-evolutionary-algorithm]]. All three solve the exploration-exploitation tension differently.
