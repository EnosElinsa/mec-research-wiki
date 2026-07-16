---
type: source
title: "Joint Energy and Completion Time Difference Minimization for UAV-Enabled Intelligent Transportation Systems: A Constrained Multi-Objective Optimization Approach"
authors: ["Chaoda Peng", "Zexiong Wu", "Xumin Huang", "Yuan Wu", "Jiawen Kang", "Qiong Huang", "Shengli Xie"]
year: 2024
url: "https://doi.org/10.1109/TITS.2024.3395993"
venue: "IEEE Transactions on Intelligent Transportation Systems"
tags: [source, uav, its, multi-source-fusion, cmop, evolutionary-algorithm, time-balancing, service-caching]
related:
  - "[[uav-enabled-its]]"
  - "[[multi-source-data-fusion]]"
  - "[[constrained-multi-objective-evolutionary-algorithm]]"
  - "[[completion-time-difference]]"
  - "[[service-caching-mec]]"
  - "[[cmoea-d-cdp]]"
  - "[[peng-2022-cmop-uav-path-planning]]"
  - "[[huang-2025-cmop-dispersed-computing]]"
  - "[[huang-2023-mu-aec-task-energy]]"
created: 2026-05-29
updated: 2026-07-16
modeling_card: required
---

# Joint Energy and Completion Time Difference Minimization for UAV-Enabled Intelligent Transportation Systems

## Citation

Peng, C., Wu, Z., Huang, X., Wu, Y., Kang, J., Huang, Q., & Xie, S. (2024). *Joint Energy and Completion Time Difference Minimization for UAV-Enabled Intelligent Transportation Systems: A Constrained Multi-Objective Optimization Approach*. **IEEE Transactions on Intelligent Transportation Systems**. DOI: 10.1109/TITS.2024.3395993.

## TL;DR

A control center dispatches multiple UAVs to monitor traffic at distinct ground locations. Each UAV gathers surveillance data and either processes it locally or offloads to an edge server. The **fusion** of all UAVs' processing results at the control center is sensitive to **temporal misalignment** — if UAVs finish at very different times, the fusion is degraded.

So the CMOP balances:

- **G₁:** total UAV energy consumption.
- **G₂:** total **pairwise completion-time difference** among employed UAVs (a synchronization objective, not a makespan).

Solved with the **CMOEA/D-CDP** framework plus an **improved genetic operator** (data-type aware) and a **repairing constraint-handling technique**.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A control center dispatches $I$ standby UAVs to $J$ monitoring locations with $I\ge J$. Each selected UAV collects data, then either processes locally or offloads to an edge server whose service programs may be cached.

**Problem & objective**: Minimize $G_1(\mathbf x)=\sum_{i,j}y_{i,j}[(1-x_i)E_{i,j}^{L}+x_iE_{i,j}^{O}]$ and the completion-time imbalance $G_2(\mathbf x)=\sum_{i\in\mathcal S}|\tau_i-\hat\tau|/\vartheta$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Offloading mode | $x_i$ | binary (encoded in $[0,1]$) | Local processing or edge offloading |
| UAV-task association | $y_{i,j}$ | binary (encoded in $[0,1]$) | UAV $i$ is assigned to monitoring task $j$ |
| UAV bandwidth | $b_i$ | continuous, nonnegative | Bandwidth allocated to UAV $i$ |
| Edge CPU allocation | $f_i^O$ | continuous, nonnegative | Edge computing capability for offloaded task |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | At most one task per UAV: $\sum_{j=1}^{J}y_{i,j}\le1$ for every $i$ |
| C2 | Every monitoring task is assigned: $\sum_{i=1}^{I}y_{i,j}=1$ for every $j$ |
| C3 | Total selected-UAV bandwidth: $\sum_{i,j}y_{i,j}b_i\le B$ |
| C4 | Edge CPU budget: $\sum_{i,j}y_{i,j}x_if_i^O\le F$ |
| C5 | Edge storage budget: $\sum_{i,j}y_{i,j}(\beta_j+x_i\alpha_i)\le S$ |
| C6 | Domain constraints: $x_i,y_{i,j}\in[0,1]$ and $b_i,f_i^O\ge0$ |

**Algorithm**: Encode each solution as mixed integer and continuous parts, decompose the CMOP with CMOEA/D-CDP weight vectors, apply data-type-aware differential and mutation operators, repair violated assignment, bandwidth, CPU, and storage constraints, and retain non-dominated feasible solutions.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Peng et al. [x] formulate a multi-UAV intelligent transportation system problem that balances total energy with completion-time differences important for multi-source fusion. Binary task association and local-versus-edge processing decisions are coupled with UAV bandwidth and edge CPU allocations, while service caching changes the processing delay. The proposed CMOEA/D-CDP uses data-type-aware evolutionary operators and a repairing constraint handler to search the resulting mixed-variable Pareto problem. Experiments on three monitoring-task instances report improved inverted-generational-distance and hypervolume performance over the compared constrained multi-objective algorithms.

## Why this matters

The completion-time-difference objective is the original contribution. Most prior wiki sources optimize **mean** or **max** delay; this paper argues that for **multi-source fusion** the **variance** of completion times matters more. That observation is very portable:

- Federated learning round synchronization ([[mao-2025-bcsa-frl]]).
- Multi-vehicle cooperative perception ([[xie-2026-uav-multisource-fusion]]).
- Multi-UAV interdependent task scheduling ([[huang-2023-mu-aec-task-energy]]).

In all those settings, "everyone finish around the same time" is a hidden constraint that's worth pulling explicit.

This paper is also a **lineage** entry in the Peng/Huang group's **CMOP-evolutionary** thread — see [[peng-2022-cmop-uav-path-planning]] for the seed.

## Method outline

- **Decision variables.** Binary task association y_{i,j} (UAV i ↔ task j); binary offloading x_i (local vs edge); UAV computing speeds f_i^L; edge CPU allocation f_i^O; UAV flight speed v_i.
- **Service caching.** Tasks may need a service program. If cached on the edge server (γ_j = 1), retrieval is fast; else fetched from the cloud (extra time r_ES). This is a wiki-first **service-caching** modeling.
- **Genetic operator.** Distinguishes binary, integer, and continuous variables, applying the right crossover/mutation per type.
- **Constraint repair.** Infeasible offspring are surgically repaired (rather than simply discarded).

## Findings

- The repair-CHT + data-type-aware operator beats stock CMOEA/D-CDP baselines on inverted-generational distance and hypervolume.
- Time-difference reduction comes mostly from **balancing offloading** (slow local UAVs offload; fast UAVs run local) — *not* from balancing flight time.
- Energy and time-difference do conflict: pushing all UAVs to offload reduces variance but spikes edge-server energy.

## Limitations

- Static UAV start positions; no trajectory replanning during the mission.
- Synchronization objective uses pairwise differences; could be reformulated as variance for cleaner gradient information (open methodological question).
- I ≥ J assumption — more UAVs than tasks. The reverse case is the interesting one for crowded-deployment scenarios and isn't addressed.

## Cross-link with related sources

- **Lineage:** [[peng-2022-cmop-uav-path-planning]] (seed) → this paper (multi-UAV + time difference) → [[huang-2025-cmop-dispersed-computing]] (reliability via redundancy) → [[wu-2026-terrain-aware-uav-mec]] (terrain awareness) → [[huang-2023-mu-aec-task-energy]] (interdependent tasks).
- **Synchronization-as-objective** is a recurring pattern: see also [[mao-2025-bcsa-frl]]'s round-synchronization in BCSA-FRL.
- **Service caching** is introduced here for the wiki — could be revisited in any future ground-MEC source with caching.

## Raw artifacts

- Parse: `raw/sources/Joint_Energy_and_Completion_Time_Difference_Minimization_for_UAV-Enabled_Intelligent_Transportation_Systems_A_Constrained_Multi-Objective_Optimization_Approach/full.md`
- Origin PDF: `raw/sources/Joint_Energy_and_Completion_Time_Difference_Minimization_for_UAV-Enabled_Intelligent_Transportation_Systems_A_Constrained_Multi-Objective_Optimization_Approach/9aeb297b-5e89-4774-8eb4-cf560799765b_origin.pdf`
- Figures: `raw/sources/Joint_Energy_and_Completion_Time_Difference_Minimization_for_UAV-Enabled_Intelligent_Transportation_Systems_A_Constrained_Multi-Objective_Optimization_Approach/images/`
