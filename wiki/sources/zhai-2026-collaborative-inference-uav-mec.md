---
type: source
modeling_card: required
title: "Deep Reinforcement Learning-Based Task Offloading With Collaborative Inference in UAV-Assisted Mobile Edge Computing Networks"
authors: ["Xiangping Bryce Zhai", "Shuang Fu", "Changyan Yi", "Zhiquan Liu", "Chao Dong", "Chee Wei Tan"]
year: 2026
url: "https://doi.org/10.1109/TITS.2025.3629117"
venue: "IEEE Transactions on Intelligent Transportation Systems (IEEE T-ITS)"
tags: [source, uav-assisted-mec, multi-uav, collaborative-inference, dnn-partition, task-offloading, td3, trajectory-optimization]
related:
  - "[[collaborative-dl-inference]]"
  - "[[dnn-model-partition]]"
  - "[[task-offloading]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[uav-trajectory-control]]"
  - "[[td3]]"
  - "[[sun-2024-asap-uav-swarm]]"
  - "[[niazmand-2025-jopa-dnn-pruning-iiot]]"
created: 2026-07-06
updated: 2026-11-03
---

# Deep Reinforcement Learning-Based Task Offloading With Collaborative Inference in UAV-Assisted Mobile Edge Computing Networks

## Citation

Zhai, X. B., Fu, S., Yi, C., Liu, Z., Dong, C., & Tan, C. W. (2026). *Deep Reinforcement Learning-Based Task Offloading With Collaborative Inference in UAV-Assisted Mobile Edge Computing Networks*. **IEEE Transactions on Intelligent Transportation Systems**, 27(1), 472-482. DOI: 10.1109/TITS.2025.3629117.

## TL;DR

A multi-UAV MEC framework for DNN inference tasks where each ground user's DNN can be split between the user device and a UAV server. The proposed DPDTS method combines optimal DNN partition-point selection, fairness-aware GU-UAV matching / resource allocation, and TD3-based UAV trajectory plus user transmit-power control to reduce delay and energy.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Multiple fixed-altitude UAV MEC servers $j\in\mathcal K$ serve ground users (GUs) $i\in\mathcal M$ that run DNN inference. A GU executes the layers up to a partition point locally and offloads the intermediate features to one UAV, which runs the remaining layers.
**Problem & objective**: Problem (15) minimizes the weighted cost $e(n)=\sum_j\sum_i(\eta E_{i,j}^{part}(n)+(1-\eta)T_{i,j}^{part}(n))w_i$ (14) over partition points, UAV trajectories, compute allocation, GU power, and offloading. The parse garbles the expression of (15), so check the published paper.
**Decision variables**:
| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Partition point | $l_i^*(n)$ | integer, up to the DNN depth | Last layer GU $i$ executes locally |
| UAV trajectory | $\{X_j(n),Y_j(n),V_j(n)\}$ | continuous | Horizontal position and speed of UAV $j$ |
| Compute allocation | $b_{i,j}(n)$ | continuous ratio | Share of UAV $j$ computing given to GU $i$ |
| GU transmit power | $P_i^{off}(n)$ | continuous, $\le P_i^{\max}$ | Feature-upload power |
| Offloading decision | $\alpha_i(n)$ | binary | Local-only processing or partial offloading to a UAV |
**Constraints**:
| ID | Meaning and key expression |
|---|---|
| C2 | GU within UAV coverage radius $d_{\max}$ |
| C3-C4 | UAV activity area $D_{\max}$ and speed $V^{\max}$ |
| C5 | GU transmit power $\le P_i^{\max}$ |
| C6 | Partition point within the number of DNN layers |
| C7 | UAV energy within battery capacity $E_{UAV}^{\max}$ over the service period |
| C8-C9 | Each task fully local or partially offloaded; each UAV serves at most $Z$ GUs |
| C10-C11 | Bounds on the compute-allocation ratios (C1 is not described in the parse) |
**Algorithm**: Alternating optimization over three subproblems: OPPS selects each task's optimal partition point, a fairness-factor matching associates GUs with UAVs and allocates compute, and a TD3 agent in an MDP with negative cost as reward chooses UAV trajectories and GU transmit powers.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zhai et al. [x] studied task offloading with collaborative DNN inference in multi-UAV mobile edge computing networks. They formulated weighted energy and delay minimization over DNN partition points, GU-UAV association, computing-resource ratios, UAV trajectories, user transmit powers, and offloading decisions. DPDTS applies OPPS to select layer partitions and uses fairness-aware matching to associate users and allocate UAV compute. A TD3 controller then selects UAV velocity vectors and user transmit powers under coverage, capacity, power, battery, and movement constraints. Simulations report lower energy and average inference delay than the evaluated DTS, RAT, EE-PPO, and DPRT baselines.

## Problem

Conventional multi-UAV MEC offloading models often treat tasks as generic data-plus-CPU jobs. This paper targets DNN inference, where intermediate feature sizes and layer compute vary sharply across partition points, making binary offloading inefficient. The optimization jointly chooses DNN split points, GU-UAV associations, UAV computing-resource ratios, UAV trajectories, and user transmit powers to minimize a weighted energy-delay cost.

## System model

- **Network:** K UAVs with edge servers serve M ground users over time slots while flying at a fixed altitude.
- **Tasks:** each ground user generates DNN inference tasks; task types are modeled by layer count, per-layer CPU cycles, and per-layer output size.
- **Split inference:** the first part of a DNN task executes locally, intermediate data are transmitted to the UAV, and the remaining layers execute on the UAV; a partition at layer 0 means full offload and a partition at the final layer means local execution.
- **Constraints:** UAV coverage radius, flight speed, transmit-power limit, UAV battery capacity, one UAV per GU per slot, and per-UAV user capacity.

## Method

DPDTS decomposes the non-convex problem into three pieces. OPPS searches DNN partition points for each task type and UAV coverage set. A matching algorithm ranks user-UAV pairs by weighted energy/delay improvement and allocates UAV compute according to a fairness weight. A [[td3]] actor-critic controller then optimizes UAV velocity vectors and GU transmit powers, using the negative energy-delay objective plus boundary penalties as the reward.

## Key findings

- With coverage radius 50 m, DPDTS consumes **1536.9 J**, which the parse reports as **22.6%**, **35.5%**, **17.6%**, and **54.2%** lower than DTS, RAT, EE-PPO, and DPRT, respectively.
- Under the same coverage setting, DPDTS reports **253.7 ms** average processing delay per user, faster than the four baselines by **24.8%**, **36.8%**, **19.26%**, and **49.1%**.
- When the number of ground users increases, DPDTS keeps the lowest energy and end-to-end delay among the compared schemes; for 70 GUs it reports **2209.0 J** energy, and for 80 GUs it reports **389 ms** average processing delay.
- Across bandwidth settings, DPDTS reduces energy by **35.1%**, **49.2%**, **23.9%**, and **66.4%** on average versus the four baselines, and reduces average delay by **27.5%**, **31.7%**, **18.2%**, and **57.1%**.

## Limitations / future work

The conclusion states that algorithm scalability is insufficient and that a gap remains between simulation experiments and actual scenarios. The paper does not report hardware or real-flight validation for DPDTS.

## Relation to the corpus

This source connects [[collaborative-dl-inference]] with mainstream UAV-MEC [[task-offloading]]. Compared with [[sun-2024-asap-uav-swarm]], which partitions inference inside a UAV swarm, this paper partitions DNN tasks between each GU and its serving UAV while also optimizing multi-UAV trajectories. It is also a useful DNN-task counterpart to [[niazmand-2025-jopa-dnn-pruning-iiot]], which treats model pruning / offloading in IIoT rather than UAV trajectory control.

## Raw artifacts

- `raw/sources/Deep_Reinforcement_Learning-Based_Task_Offloading_With_Collaborative_Inference_in_UAV-Assisted_Mobile_Edge_Computing_Networks/Deep_Reinforcement_Learning-Based_Task_Offloading_With_Collaborative_Inference_in_UAV-Assisted_Mobile_Edge_Computing_Networks.md`
- Original PDF and extracted figures (`images/`) in the same folder.
