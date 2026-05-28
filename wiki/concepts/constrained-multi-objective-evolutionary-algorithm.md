---
type: concept
title: "Constrained Multi-Objective Evolutionary Algorithm (CMOEA)"
tags: [evolutionary, multi-objective, constrained-optimization, pareto, classical-solver]
related:
  - "[[cmoea-d-cdp]]"
  - "[[infeasible-individual-utilization]]"
  - "[[dual-population-evolutionary-algorithm]]"
  - "[[multi-tasking-evolutionary-algorithm]]"
  - "[[local-search-evolutionary]]"
  - "[[peng-2022-cmop-uav-path-planning]]"
created: 2026-05-29
updated: 2026-05-29
---

# Constrained Multi-Objective Evolutionary Algorithm (CMOEA)

Population-based search for problems with **multiple conflicting objectives** *and* **feasibility constraints**. Output: a set of **non-dominated** solutions approximating the Pareto front, each representing a distinct tradeoff. The decision-maker picks one *after* seeing the front.

Strengths: gradient-free; handles non-differentiable, mixed-integer, non-convex objectives; produces a diverse front in one run rather than one solution per scalarization. Weaknesses: high computational cost (10⁴–10⁵ function evaluations typical); no convergence guarantees; sensitive to genetic-operator choice.

The wiki has an entire **lineage** of CMOEA variants built by the Peng/Huang group on UAV-MEC problems:

- [[peng-2022-cmop-uav-path-planning]] — seed (path planning + offloading, infeasibility utilization).
- [[peng-2024-energy-time-uav-its]] — UAV-ITS energy + completion-time difference.
- [[huang-2023-mu-aec-task-energy]] — multi-UAV interdependent tasks (DAG awareness, [[local-search-evolutionary|local search]]).
- [[huang-2025-cmop-dispersed-computing]] — dispersed computing reliability ([[dual-population-evolutionary-algorithm]]).
- [[wu-2026-terrain-aware-uav-mec]] — terrain-aware urban MEC ([[multi-tasking-evolutionary-algorithm]]).
- [[xie-2026-uav-multisource-fusion]] — V2X cooperative perception (dynamic CMOO).

Different from DRL: CMOEA gives the decision-maker the *whole front*, while DRL outputs a single trained policy. When tradeoffs are open and you want the human in the loop, CMOEA wins; when decisions are real-time and recurring, DRL wins.
