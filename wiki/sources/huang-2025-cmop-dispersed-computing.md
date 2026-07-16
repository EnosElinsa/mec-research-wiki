---
type: source
title: "Joint Latency and Charge Cost Minimization for Reliable Task Offloading in Dispersed Computing: A Multi-Objective Optimization Approach"
authors: ["Xumin Huang", "Zexiong Wu", "Chaoda Peng", "Yuan Wu", "Weifeng Zhong", "Jiawen Kang", "Shengli Xie"]
year: 2025
url: ""
venue: ""
modeling_card: required
tags: [source, dispersed-computing, cmop, evolutionary-algorithm, task-redundancy, dual-population, parallel-vs-serial]
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
updated: 2026-07-16
---

# Joint Latency and Charge Cost Minimization for Reliable Task Offloading in Dispersed Computing

## Citation

Huang, X., Wu, Z., Peng, C., Wu, Y., Zhong, W., Kang, J., & Xie, S. (2025). *Joint Latency and Charge Cost Minimization for Reliable Task Offloading in Dispersed Computing: A Multi-Objective Optimization Approach*. (Venue / DOI `not in parse`.)

> **Metadata note (2026-05-31 audit):** an earlier version of this page carried the DOI `10.1109/TEVC.2025.3569722` / venue *IEEE Trans. Evolutionary Computation*. That DOI is **not** this paper's — it belongs to **reference [8]** in this paper's own reference list (Wang, Guo, Liu & Wang, *An Adaptive Constraint Violation Evaluation Framework…*, see [[wang-acve-constraint-violation-cmop]]). The misattributed DOI was removed; this paper's own parse contains no `Digital Object Identifier` line, so venue/DOI are `not in parse`.

## TL;DR

**Dispersed computing** uses a swarm of volunteer IoT devices (IoTDs) to assist an overloaded edge server. Two computing styles coexist:

- **Parallel** on the edge server (simultaneous tasks share CPU frequency).
- **Serial** on each IoTD (queued tasks one at a time).

IoTDs are unreliable — each has a per-task failure probability φ_j. To meet a per-task **reliability requirement R̄_i**, the same task must be redundantly executed on enough IoTDs that 1 − ∏ ρ_{i,j}·φ_j ≥ R̄_i. Both objectives — total latency and total monetary charge — are jointly minimized as a CMOP. The tradeoff is real: more IoTD redundancy improves reliability and parallelism but raises charge.

Solver: a **dual-population CMOEA** with a **repairing constraint-handling technique**.

- Main population maintains feasible solutions and pushes toward Pareto convergence.
- Auxiliary population explores the broader space (including infeasible regions) to keep diversity.
- The repair operator surgically fixes constraint violations rather than deleting infeasible individuals.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: An overloaded edge server can execute tasks in parallel or reverse-offload redundant copies to volunteer IoT devices that process their assigned queues serially. IoT devices have heterogeneous bandwidth, charge rates, and failure probabilities, so redundancy improves completion reliability at additional delay and monetary cost.

**Problem & objective**: The constrained multiobjective problem jointly minimizes $\mathbf{G}(\rho,\mathbf{b},\mathbf{f})=\left(G_1,G_2\right)$, where $G_1$ is total task latency and $G_2$ is total processing and communication charge.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Task-processor assignment | $\rho_{i,j}$ | binary | Whether task $i$ is assigned to processor $j$, allowing redundant IoT copies |
| IoT-device bandwidth | $b_j$ | continuous, nonnegative | Communication bandwidth allocated to volunteer device $j$ |
| Edge CPU allocation | $f_i$ | continuous, nonnegative | Edge-server CPU frequency allocated to task $i$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Every task is assigned to at least one processor |
| C2 | A task cannot be executed by the edge server and volunteer IoT devices simultaneously |
| C3 | Redundant IoT execution meets the task reliability target: $P_i\ge\bar R_i$ |
| C4 | Total IoT bandwidth and edge CPU allocations remain within their respective capacities |
| C5 | Bandwidth is allocated only to active IoT processors, and edge CPU is allocated only to edge-executed tasks |
| C6 | Assignment variables are binary and resource allocations stay in their feasible domains |

**Algorithm**: The proposed constrained multiobjective evolutionary algorithm maintains a feasibility-focused main population under the constraint-domination principle and a diversity-focused auxiliary population under an angle-based selection framework. It shares offspring between populations, repairs heterogeneous assignment and resource violations, and returns a Pareto set spanning delay-oriented, charge-oriented, and balanced solutions.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Huang et al. [x] formulated reliable reverse offloading from an overloaded edge server to volunteer IoT devices as constrained multiobjective optimization. They jointly minimized total task delay and monetary charge over redundant task-processor assignment, IoT-device bandwidth, and edge CPU allocation under coverage, exclusivity, per-task reliability, resource-capacity, and activation-coupling constraints. Their evolutionary solver uses a feasibility-focused main population, a diversity-focused auxiliary population, offspring sharing, and a repair operator for heterogeneous constraint violations. On CMOP2, its delay-oriented solution reduced delay by 88.6% and its charge-oriented solution reduced charge by 91.3% relative to CMOEA/D-CDP, while the full dual-population mechanism reduced mean IGD by 77.8%.

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
