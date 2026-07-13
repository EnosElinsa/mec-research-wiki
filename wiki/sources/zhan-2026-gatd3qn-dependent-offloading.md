---
type: source
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
updated: 2026-07-14
---

# Joint UAV Placement and Dependent Task Offloading in Multi-UAV MEC Networks: A Graph Attention Enhanced DRL Approach

## Citation

Zhan, C., Liu, W., Song, K., Fan, R., Liu, J., & Hu, H. (2026). *Joint UAV Placement and Dependent Task Offloading in Multi-UAV MEC Networks: A Graph Attention Enhanced DRL Approach*. **IEEE Transactions on Mobile Computing**, 25(4), 5285-5301. DOI: 10.1109/TMC.2025.3628608.

## TL;DR

Studies multi-UAV MEC where ground users generate application tasks represented as directed acyclic graphs. The paper jointly optimizes UAV placement, UAV-ground-user association, and dependent-task offloading to minimize the final completion time. Its JSPO stage uses successive convex approximation plus penalty dual decomposition for UAV placement and association, while a GAT-enhanced D3QN offloading stage embeds each task DAG before learning binary subtask offloading decisions.

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

- `raw/sources/Joint UAV Placement and Dependent Task Offloading in Multi-UAV MEC Networks A Graph Attention Enhanced DRL Approach/Joint UAV Placement and Dependent Task Offloading in Multi-UAV MEC Networks A Graph Attention Enhanced DRL Approach.md`
- Original PDF and extracted figures (`images/`) in the same folder.
