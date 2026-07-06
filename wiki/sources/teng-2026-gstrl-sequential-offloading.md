---
type: source
title: "Graph-Based Spatiotemporal RL Framework for Sequential Task Offloading in Multi-UAV Systems"
authors: ["Meiyan Teng", "Xin Li", "Xuyun Zhang", "Jianqiu Xu", "Kun Zhu"]
year: 2026
url: "https://doi.org/10.1109/TMC.2025.3635085"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, multi-uav, task-offloading, sequential-task-offloading, graph-neural-network, ppo]
related:
  - "[[sequential-task-offloading]]"
  - "[[task-offloading]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[graph-neural-network]]"
  - "[[ppo]]"
  - "[[interdependent-tasks-dag]]"
created: 2026-07-07
updated: 2026-07-07
---

# Graph-Based Spatiotemporal RL Framework for Sequential Task Offloading in Multi-UAV Systems

## Citation

Teng, M., Li, X., Zhang, X., Xu, J., & Zhu, K. (2026). *Graph-Based Spatiotemporal RL Framework for Sequential Task Offloading in Multi-UAV Systems*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2025.3635085.

## TL;DR

Models multi-UAV cooperative offloading as a sequential task offloading problem (sTOP) where jobs contain ordered subtasks and UAV topology changes over time. GSTRL represents UAVs, requesting tasks, and offloaded tasks as a heterogeneous graph, extracts spatial features with HGNN, tracks temporal dependencies with LSTM, and uses masked PPO to keep offloading actions feasible. The reported gains come from jointly modeling network topology and task order rather than treating tasks as independent one-shot jobs.

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
