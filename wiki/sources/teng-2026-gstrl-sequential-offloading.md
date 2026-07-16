---
type: source
title: "Graph-Based Spatiotemporal RL Framework for Sequential Task Offloading in Multi-UAV Systems"
authors: ["Meiyan Teng", "Xin Li", "Xuyun Zhang", "Jianqiu Xu", "Kun Zhu"]
year: 2026
url: "https://doi.org/10.1109/TMC.2025.3635085"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
modeling_card: required
tags: [source, multi-uav, task-offloading, sequential-task-offloading, graph-neural-network, ppo]
related:
  - "[[sequential-task-offloading]]"
  - "[[task-offloading]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[graph-neural-network]]"
  - "[[ppo]]"
  - "[[interdependent-tasks-dag]]"
created: 2026-07-07
updated: 2026-07-16
---

# Graph-Based Spatiotemporal RL Framework for Sequential Task Offloading in Multi-UAV Systems

## Citation

Teng, M., Li, X., Zhang, X., Xu, J., & Zhu, K. (2026). *Graph-Based Spatiotemporal RL Framework for Sequential Task Offloading in Multi-UAV Systems*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2025.3635085.

## TL;DR

Models multi-UAV cooperative offloading as a sequential task offloading problem (sTOP) where jobs contain ordered subtasks and UAV topology changes over time. GSTRL represents UAVs, requesting tasks, and offloaded tasks as a heterogeneous graph, extracts spatial features with HGNN, tracks temporal dependencies with LSTM, and uses masked PPO to keep offloading actions feasible. The reported gains come from jointly modeling network topology and task order rather than treating tasks as independent one-shot jobs.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Devices generate jobs composed of ordered tasks, and heterogeneous UAVs execute or forward one task at a time over a time-varying inter-UAV graph. Each task incurs transmission, queueing, and computation delay, while every UAV has finite energy and a single processing core.

**Problem & objective**: The sequential task offloading problem in (11) maximizes $\mathcal Q^{time}+\mathcal Q^{load}$ by assigning every task to an eligible UAV while reducing deadline violations and workload imbalance.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Task offloading UAV | $O_{j,k}$ | categorical, $O_{j,k}\in\mathbf U$ | UAV selected to execute task $k$ of job $j$ |
| Requesting UAV | $R_{j,k}$ | predecessor-determined category | UAV that holds the output required by the current task |
| Masked policy action | $A_t$ | categorical feasible UAV | RL action selecting the next offloading destination |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 / 11a | Job response time satisfies $T_j\leq T_j^{\max}$ |
| C2 | Sequential consistency requires $R_{j,k}=O_{j,k-1}$ |
| C3 / 11b | The requesting and selected UAVs must be connected in slot $t$ |
| C4 / 11d | Each UAV respects cumulative energy capacity $\sum_tE_{u,t}\leq E_u^{\max}$ |
| C5 / 11e | Every offloading destination belongs to the available UAV set |

**Algorithm**: GSTRL constructs a heterogeneous graph with UAV, requesting-task, and offloaded-task nodes. An HGNN encodes spatial topology, an LSTM encodes task-order history, and the combined state feeds masked PPO so disconnected or otherwise infeasible UAV actions are removed before sampling and policy updates.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Teng et al. [x] formulated sequential task offloading in a dynamic collaborative multi-UAV system with time-varying connectivity, heterogeneous computing resources, and queueing delay. Their objective combines job response quality and inter-UAV load balance under deadline, predecessor, connectivity, battery, and destination-feasibility constraints. GSTRL represents UAVs and task states as a heterogeneous graph, combines HGNN spatial features with LSTM temporal features, and applies masked PPO to select feasible offloading destinations. Simulations report lower execution time and higher success rate and operational efficiency than the evaluated RL and heuristic methods. Experiments using public UAV trajectories and Seattle building data retained the highest reported success rates in both suburban and dense-urban settings, including about 90% for 50 requests and about 70% for 150 requests in the suburban case.

## Problem framing

Multi-UAV systems can share computation through inter-UAV offloading, but real jobs in disaster relief, inspection, and surveillance often have predecessor-successor dependencies. UAV mobility also changes U2U links and resource availability. The resulting offloading problem is NP-hard and cannot be captured well by static single-slot offloading or independent-task abstractions.

## System model

The system contains a cloud server, UAVs, and devices. Devices generate Poisson job requests made of linear task sequences. Each UAV has one computing core, finite energy, a location, transmission power, queue state, and current requests; UAV-to-UAV communication depends on dynamic connectivity and LoS/NLoS conditions. A task's execution time includes transmission, waiting, and computing time, and the objective balances response quality and load quality under deadline, predecessor, connectivity, energy, and offloading constraints.

## Method

GSTRL builds a dynamic heterogeneous graph whose node types include UAVs, offloaded tasks, and requesting tasks, with U2U, task-to-UAV, and UAV-to-task edges. Its spatiotemporal module combines:

- an HGNN/GAT-style spatial encoder for heterogeneous topology and task-resource relations;
- an LSTM for temporal dependencies across sequential subtasks;
- original system features such as UAV energy, queue state, location, and task attributes.

The extracted representation feeds a masked PPO policy, implemented as G-MPPO, so invalid actions are excluded before policy sampling and update.

## Key findings

- The abstract reports about 25% higher average reward than DRL and heuristic baselines, 30-50% higher task success rate and OER, and up to 40% lower execution time in complex multi-UAV systems.
- In the 100-device simulations, G-MPPO keeps task success above 90% in most tested UAV-count cases, while UCB-MAB and random offloading remain below 40%.
- The real-world-style evaluation uses public UAV trajectory datasets and Seattle building-distribution data; with nine UAVs, G-MPPO achieves about 90% success in the small suburban case and close to 70% in the large suburban case.
- The method is reported to converge more stably than PPO, RGNN, DQN, and DDQN under multiple random seeds.

## Limitations / future work

The paper models each job as a linear task sequence. It states that DAG-structured tasks are a future extension, even though DAGs can sometimes be transformed into equivalent sequences at the cost of abstraction.

## Relation to the corpus

This source adds an explicit [[sequential-task-offloading]] anchor to the broader [[task-offloading]] corpus. It connects the two-part graph-resource-management survey lineage through [[graph-neural-network]], and it complements [[interdependent-tasks-dag]] by focusing on sequence-structured UAV jobs rather than general DAG scheduling.

## Raw artifacts

- `raw/sources/Graph-Based Spatiotemporal RL Framework for Sequential Task Offloading in Multi-UAV Systems/Graph-Based Spatiotemporal RL Framework for Sequential Task Offloading in Multi-UAV Systems.md`
- Original PDF and extracted figures (`images/`) in the same folder.
