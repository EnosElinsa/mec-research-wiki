---
type: source
title: "Joint Latency and Charge Cost Minimization for Reliable Task Offloading in Dispersed Computing: A Multi-Objective Optimization Approach"
authors: ["Xumin Huang", "Zexiong Wu", "Chaoda Peng", "Yuan Wu", "Weifeng Zhong", "Jiawen Kang", "Shengli Xie"]
year: 2025
url: ""
venue: "IEEE / preprint (Huang/Peng group, 2025)"
tags: [dispersed-computing, cmop, evolutionary-algorithm, task-redundancy, dual-population, parallel-vs-serial]
related:
  - "[[dispersed-computing]]"
  - "[[task-redundancy-for-reliability]]"
  - "[[parallel-vs-serial-processing]]"
  - "[[constrained-multi-objective-evolutionary-algorithm]]"
  - "[[dual-population-evolutionary-algorithm]]"
  - "[[peng-2022-cmop-uav-path-planning]]"
  - "[[peng-2024-energy-time-uav-its]]"
  - "[[huang-2023-mu-aec-task-energy]]"
created: 2026-05-29
updated: 2026-05-29
---

# Joint Latency and Charge Cost Minimization for Reliable Task Offloading in Dispersed Computing

## Citation

Huang, X., Wu, Z., Peng, C., Wu, Y., Zhong, W., Kang, J., & Xie, S. (2025). *Joint Latency and Charge Cost Minimization for Reliable Task Offloading in Dispersed Computing: A Multi-Objective Optimization Approach*. (Huang/Peng group preprint, 2025.)

## TL;DR

**Dispersed computing** uses a swarm of volunteer IoT devices (IoTDs) to assist an overloaded edge server. Two computing styles coexist:

- **Parallel** on the edge server (simultaneous tasks share CPU frequency).
- **Serial** on each IoTD (queued tasks one at a time).

IoTDs are unreliable — each has a per-task failure probability φ_j. To meet a per-task **reliability requirement R̄_i**, the same task must be redundantly executed on enough IoTDs that 1 − ∏ ρ_{i,j}·φ_j ≥ R̄_i. Both objectives — total latency and total monetary charge — are jointly minimized as a CMOP. The tradeoff is real: more IoTD redundancy improves reliability and parallelism but raises charge.

Solver: a **dual-population CMOEA** with a **repairing constraint-handling technique**.

- Main population maintains feasible solutions and pushes toward Pareto convergence.
- Auxiliary population explores the broader space (including infeasible regions) to keep diversity.
- The repair operator surgically fixes constraint violations rather than deleting infeasible individuals.

## Why this matters

This is another entry in the **Peng/Huang CMOP-evolutionary lineage** (see [[peng-2022-cmop-uav-path-planning]] for the lineage's seed). The novel contributions vs the lineage:

1. **Reliability constraint via redundancy** — first time the lineage models per-IoTD failure probabilities and uses task duplication as a feasibility lever.
2. **Heterogeneous processor model** — the *parallel-vs-serial* asymmetry between edge server and IoTDs is explicitly modeled in the cost function. Most prior MEC papers in the wiki treat all servers as parallel.
3. **Dual-population mechanism** — different from the *single-population infeasibility-allocation* in [[peng-2022-cmop-uav-path-planning]] and the *task-adaptive multi-tasking* in [[wu-2026-terrain-aware-uav-mec]]. A useful design point for the methods comparison.

## Method outline

- **Decision variables.** Binary task-processor assignment ρ_{i,j}; bandwidth allocated to each IoTD b_j; CPU frequency allocated by the edge server to each parallel task.
- **Objectives.**
  - G₁ = Σᵢ T_i (total delay; max-over-IoTD-queue + transmission + parallel-edge time).
  - G₂ = Σᵢ Cost_i (charge: linear in CPU at the edge, energy-compensation per IoTD).
- **Constraints.** Reliability R_i ≥ R̄_i; bandwidth budget; edge CPU budget; per-IoTD energy budget.

## Findings

- Dual-population scheme produces a **better-distributed** Pareto front than single-population baselines.
- Repair-based constraint handling beats "delete-infeasible" baselines in convergence speed because feasible regions are sparse near the Pareto knee.
- Optimal redundancy is **smaller for low-priority tasks** even when extra IoTDs are available — reliability is paid for, not free.

## Limitations

- Static network: IoTDs don't move during the planning window. Real volunteer-IoT systems churn.
- Selfishness modeled only through the charge function (linear); no game-theoretic incentive analysis (contrast [[wang-2025-uav-swarm-stackelberg]], [[bi-2025-sg-mapg]]).
- Task graph is independent — sibling paper [[huang-2023-mu-aec-task-energy]] handles dependent tasks.

## Cross-link with related sources

- **Lineage:** [[peng-2022-cmop-uav-path-planning]] (seed) → this paper (reliability + parallel/serial) and [[huang-2023-mu-aec-task-energy]] (interdependent tasks).
- **Reliability via redundancy** is a new pattern for the wiki — pairs conceptually with the [[fl-poisoning-attacks|FL-poisoning]] tolerance in [[mao-2025-bcsa-frl]] (different mechanism — voting vs duplication — same goal).

## Raw artifacts

- `raw/sources/Joint Latency and Charge Cost Minimization for Reliable Task Offloading in Dispersed Computing A Mu/full.md`
