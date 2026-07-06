---
type: concept
title: "Energy-Latency Tradeoff"
tags: [metrics, objective, scalarization, mec]
related:
  - "[[aoi-energy-tradeoff]]"
  - "[[energy-balancing-uav]]"
  - "[[qoe-modeling-mec]]"
  - "[[shao-2024-drl-antijamming-mec]]"
  - "[[li-2025-energy-latency-uav-vec]]"
  - "[[yang-2025-generalizable-pareto-offloading]]"
created: 2026-05-29
updated: 2026-07-07
---

# Energy-Latency Tradeoff

The most common scalarized MEC objective: a **weighted sum of latency and energy**, $\Omega = \xi \cdot T + (1-\xi) \cdot E$, with a tunable weight $\xi \in [0,1]$. Raising $\xi$ prioritizes responsiveness; lowering it prioritizes battery life. It collapses two conflicting goals into a single reward/cost that DRL agents and classical solvers can optimize directly.

In the wiki, [[shao-2024-drl-antijamming-mec]] uses exactly this cost (finding $\xi = 0.5$ balances best), and the same weighted-sum pattern recurs across the corpus as the default offloading objective. Contrast with the *vectorial* treatment that keeps objectives separate — the [[aoi-energy-tradeoff]] solved by multi-objective learning — when fixed weights are undesirable.

[[li-2025-energy-latency-uav-vec]] uses the weighted-sum form for UAV-assisted vehicular FL participant selection and resource allocation. [[yang-2025-generalizable-pareto-offloading]] is the explicit contrast case: it keeps delay and energy as vector rewards and conditions the policy on the current preference weight.
