---
type: source
modeling_card: required
title: "Joint UAV Placement and Dependent Task Offloading in Multi-UAV MEC Networks: A Graph Attention Enhanced DRL Approach"
authors: ["Cheng Zhan", "Wei Liu", "Kaifeng Song", "Rongfei Fan", "Jun Liu", "Han Hu"]
year: 2026
url: "https://doi.org/10.1109/TMC.2025.3628608"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), vol. 25, no. 4, Apr. 2026"
tags: [source, multi-uav-assisted-mec, dependent-task-offloading, graph-neural-network, dueling-dqn, penalty-dual-decomposition]
related:
  - "[[cheng-zhan]]"
  - "[[kaifeng-song]]"
  - "[[rongfei-fan]]"
  - "[[han-hu]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[interdependent-tasks-dag]]"
  - "[[task-offloading]]"
  - "[[graph-neural-network]]"
  - "[[dueling-dqn]]"
  - "[[penalty-dual-decomposition]]"
  - "[[device-association]]"
created: 2026-07-07
updated: 2026-11-03
---

# Joint UAV Placement and Dependent Task Offloading in Multi-UAV MEC Networks: A Graph Attention Enhanced DRL Approach

## Citation

Zhan, C., Liu, W., Song, K., Fan, R., Liu, J., & Hu, H. (2026). *Joint UAV Placement and Dependent Task Offloading in Multi-UAV MEC Networks: A Graph Attention Enhanced DRL Approach*. **IEEE Transactions on Mobile Computing**, 25(4), 5285-5301. DOI: 10.1109/TMC.2025.3628608.

## TL;DR

Studies multi-UAV MEC where ground users generate application tasks represented as directed acyclic graphs. The paper jointly optimizes UAV placement, UAV-ground-user association, and dependent-task offloading to minimize the final completion time. Its JSPO stage uses successive convex approximation plus penalty dual decomposition for UAV placement and association, while a GAT-enhanced D3QN offloading stage embeds each task DAG before learning binary subtask offloading decisions.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: UAV MEC servers $u_m$ serve ground users (GUs) $s_k$ whose applications are DAGs $G_k$. Start and end subtasks run locally, intermediate subtasks run locally or at the associated UAV, and each subtask starts only when predecessor data and the processor are both available.
**Problem & objective**: Problem (P1) (10)-(15) minimizes the overall end time $TF$ of all GU tasks, $\min_{\{\mathbf q_m\},\{a_{km}\},\mathcal E}TF$, over UAV deployment, user association, and the offloading plan $\mathcal E$.
**Decision variables**:
| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV deployment | $\mathbf q_m$ | continuous 2-D | Position of UAV $u_m$ |
| User association | $a_{km}$ | binary | GU $s_k$ associated with UAV $u_m$ |
| Subtask offloading | $x_i$ in plan $\mathcal E$ | binary | Subtask $i$ at the UAV ($x_i=1$) or locally ($x_i=0$) |
**Constraints**:
| ID | Meaning and key expression |
|---|---|
| (10)-(11) | Binary association with one UAV per GU, $\sum_ma_{km}=1$ |
| (12)-(13) | Binary offloading; start and end subtasks local, $x_l=0$ for $l\in\mathcal L$ |
| (14) | Precedence $S(i)\ge F(j)$ for all $j\in pre(i)$ |
| (15) | End time $TF\ge F(i)$ for every subtask |
**Algorithm**: First assume all intermediate subtasks are offloaded, which reduces P1 to the min-max transmission-time problem P2 over $\{\mathbf q_m\},\{a_{km}\}$; JSPO alternates SCA-based deployment (P4) and PDD-based association (P6)-(P9). Then GATD3QN encodes each DAG with graph attention and a dueling double DQN selects the binary offloading plan, alternating with JSPO until the objective stops decreasing.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zhan et al. [x] studied joint UAV placement and dependent task offloading in multi-UAV MEC networks with DAG applications. They formulated maximum final-completion-time minimization over UAV locations, user associations, and binary subtask execution under single-UAV association, local start and end subtasks, and task-precedence constraints. JSPO combines successive convex approximation with penalty dual decomposition to update placement and association. A graph-attention encoder represents each DAG before a D3QN selects dependent-task offloading actions, and the two stages iterate. Simulations report lower end time for JSPO than K-means and random-deployment placement, and lower end time and faster convergence for GATD3QN than D3QN, DDQN, local computing, and random offloading.

## Problem

Dependent subtasks cannot be offloaded independently: predecessor outputs may need to move between local devices and UAV MEC servers before successors can start. This makes the assignment graph and the computation DAG jointly determine the end time. The paper frames the objective as minimizing the maximum final end time across users while respecting UAV coverage, association, and task-dependency constraints.

## System model

- Multiple UAVs provide MEC service to ground users.
- Each user has one DAG application; start and end subtasks are computed locally, while intermediate subtasks can be local or UAV-executed.
- UAV placement and UAV-ground-user association affect transmission rates and feasible offloading.
- Binary subtask offloading decisions determine where intermediate subtasks execute and whether inter-node intermediate-data transfer is required.

## Method

The proposed JSPO plus DRL loop alternates between infrastructure decisions and dependent-task offloading:

- JSPO optimizes UAV placement and user association with successive convex approximation and penalty dual decomposition.
- The task-offloading problem is modeled as an MDP and solved with a graph-attention-enhanced D3QN.
- The graph attention network encodes task-DAG structure before the D3QN estimates offloading actions; the parse describes this GAT as an unsupervised, plug-and-play state representation.
- JSPO and the DRL offloading stage iterate so placement/association and offloading decisions inform each other.

## Key findings

- The paper reports that GAT-enhanced D3QN reaches a final reward about 12% higher than plain D3QN, and reaches D3QN's final level after roughly 1000 training episodes.
- The GAT and DRL inference time is reported below about 0.1 s with 20 subtasks on an Intel Core i7-10700 test machine.
- The JSPO placement/association stage converges quickly in the reported simulations, with the maximum end time dropping in the first two iterations and then stabilizing.
- The proposed GATD3QN consistently outperforms DDQN, D3QN, local computing, and random offloading baselines in the reported completion-time comparisons.
- Increasing bandwidth improves completion time, but the reported gains diminish as bandwidth grows.

## Limitations / future work

The evaluation is simulation-based. The parse does not report hardware validation, field deployment, or an explicit future-work section -> `not in parse`.

## Relation to the corpus

This page extends the corpus's DAG-aware offloading branch beyond [[huang-2023-mu-aec-task-energy]] and the sequential-task setting in [[teng-2026-gstrl-sequential-offloading]]. It connects [[interdependent-tasks-dag]] to [[graph-neural-network]] representation learning and [[dueling-dqn]] value-based control, while JSPO reinforces [[penalty-dual-decomposition]] as a classical companion to DRL in [[multi-uav-assisted-mec]].

## Raw artifacts

- `raw/sources/Joint_UAV_Placement_and_Dependent_Task_Offloading_in_Multi-UAV_MEC_Networks_A_Graph_Attention_Enhanced_DRL_Approach/Joint_UAV_Placement_and_Dependent_Task_Offloading_in_Multi-UAV_MEC_Networks_A_Graph_Attention_Enhanced_DRL_Approach.md`
- Original PDF and extracted figures (`images/`) in the same folder.
