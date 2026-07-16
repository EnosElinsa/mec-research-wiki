---
type: source
modeling_card: required
title: "Multi-Agent Deep Reinforcement Learning for Task Offloading in UAV-Assisted Mobile Edge Computing"
authors: ["Nan Zhao", "Zhiyang Ye", "Yiyang Pei", "Ying-Chang Liang", "Dusit Niyato"]
year: 2022
url: "https://doi.org/10.1109/TWC.2022.3153316"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, multi-uav-assisted-mec, multi-agent-drl, matd3, task-offloading, trajectory-design, edge-cloud-collaboration]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[multi-agent-td3]]"
  - "[[td3]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[uav-trajectory-control]]"
  - "[[energy-latency-tradeoff]]"
  - "[[he-2023-fairness-3d-multiuav-maddpg]]"
  - "[[chang-2022-marl-multiuav-trajectory]]"
created: 2026-05-29
updated: 2026-07-16
---

# Multi-Agent Deep Reinforcement Learning for Task Offloading in UAV-Assisted Mobile Edge Computing

## Citation

Zhao, N., Ye, Z., Pei, Y., Liang, Y.-C., & Niyato, D. (2022). *Multi-Agent Deep Reinforcement Learning for Task Offloading in UAV-Assisted Mobile Edge Computing*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2022.3153316.

## TL;DR

A collaborative MEC system with **multiple UAVs and multiple edge clouds (ECs)** offloading user-equipment (UE) tasks. The goal is to minimize the sum of execution delays and energy consumptions by jointly designing UAV trajectories, computation-task allocation, and communication-resource management. Formulated as an MDP and solved with a cooperative **multi-agent DRL** framework; given the high-dimensional continuous action space, the **twin delayed DDPG (MATD3)** algorithm is used.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Multiple UAVs act as assisted edge clouds and cooperate with terrestrial edge servers for mobile UE tasks. Dynamic UE state, UAV positions, radio resources, and heterogeneous computation jointly determine execution delay and energy.

**Problem & objective**: A cooperative continuous-action MDP minimizes total system cost, $\min\mathbb E[\sum_t\gamma^t(D_{\mathrm{sum}}(t)+\lambda_EE_{\mathrm{sum}}(t))]$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV trajectory action | $\Delta\mathbf q_m(t)$ | continuous bounded vector | Movement of UAV $m$ |
| Task allocation | $\alpha_{k,j}(t)$ | continuous/discrete | Fraction or destination for UE task $k$ |
| Communication resource | $b_k(t),p_k(t)$ | continuous, bounded | Bandwidth and power allocated to UE $k$ |
| Computing resource | $f_{k,j}(t)$ | continuous, nonnegative | CPU allocated at UAV or edge cloud $j$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Each UE workload is fully allocated among feasible execution nodes |
| C2 | Radio and computing allocations remain within node capacities |
| C3 | UE tasks meet execution-delay requirements |
| C4 | UAV movement and coverage remain feasible |
| C5 | UE, UAV, and edge-cloud energy budgets are respected |

**Algorithm**: Observe local UAV, UE, task, and resource state → let each MATD3 actor output movement, task, and resource actions → train centralized twin critics on joint state/action → use the smaller target value, delayed actor updates, policy smoothing, and replay → execute decentralized UAV policies.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zhao et al. [x] studied task offloading in collaborative multi-UAV and multi-edge-cloud mobile edge computing. They formulated a cooperative MDP that minimizes execution delay and energy over UAV trajectories, computation-task allocation, and communication-resource management under workload, capacity, delay, mobility, coverage, and energy constraints. Each UAV executes a local continuous actor while centralized twin critics train on joint state and actions. MATD3 uses clipped double targets, delayed actor updates, target-policy smoothing, and replay to stabilize the high-dimensional policy. Simulations report lower total system cost than the evaluated optimization and multi-agent learning baselines under changing users and resources.

## Problem framing

UAVs serve as assisted edge clouds for large-scale, sparsely-distributed UEs, but have limited compute/energy. With multiple UAVs and ECs cooperating, the joint trajectory + task-allocation + resource-management problem is non-convex and high-dimensional.

## System model

- **Actors.** Multiple UAVs (assisted ECs) + multiple ECs serving UEs collaboratively.
- **Objective.** Minimize sum of execution delays + energy consumptions ([[energy-latency-tradeoff]]).
- **Decisions.** UAV trajectories, computation-task allocation, communication-resource management → MDP.

## Method

- A cooperative **multi-agent DRL** framework under CTDE; **MATD3** (twin delayed DDPG) handles the high-dimensional continuous action space ([[multi-agent-td3]], [[td3]]).

## Key findings

- The multi-UAV multi-EC offloading method adapts to UE mobility and changing communication/computation resources and task dynamics, and significantly reduces total system cost versus other optimization approaches (qualitative; specific curves in the paper).

## Limitations / future work

The parse's conclusion does not enumerate explicit future work beyond the established framework.

## Relation to the corpus

A core **MATD3 cooperative multi-UAV MEC** entry that sits with [[he-2023-fairness-3d-multiuav-maddpg]] (MADDPG, fairness) and [[chang-2022-marl-multiuav-trajectory]] (MARL trajectory/resource) in the multi-agent UAV-trajectory family, and shares the UAV+EC collaboration theme with [[yu-2020-uav-ec-collaborative-offloading]]. Reinforces [[multi-agent-td3]] and [[centralized-training-decentralized-execution]].

## Raw artifacts

- `raw/sources/Multi-Agent_Deep_Reinforcement_Learning_for_Task_Offloading_in_UAV-Assisted_Mobile_Edge_Computing/full.md`
- Original PDF and extracted figures in the same folder.
