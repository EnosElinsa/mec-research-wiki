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
updated: 2026-07-16
---

# Deep Reinforcement Learning-Based Task Offloading With Collaborative Inference in UAV-Assisted Mobile Edge Computing Networks

## Citation

Zhai, X. B., Fu, S., Yi, C., Liu, Z., Dong, C., & Tan, C. W. (2026). *Deep Reinforcement Learning-Based Task Offloading With Collaborative Inference in UAV-Assisted Mobile Edge Computing Networks*. **IEEE Transactions on Intelligent Transportation Systems**, 27(1), 472-482. DOI: 10.1109/TITS.2025.3629117.

## TL;DR

A multi-UAV MEC framework for DNN inference tasks where each ground user's DNN can be split between the user device and a UAV server. The proposed DPDTS method combines optimal DNN partition-point selection, fairness-aware GU-UAV matching / resource allocation, and TD3-based UAV trajectory plus user transmit-power control to reduce delay and energy.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Multiple fixed-altitude UAV MEC servers execute the later layers of ground-user DNN inference tasks after users compute earlier layers locally. Partition-dependent feature size couples GU-UAV association, compute sharing, transmit power, trajectory, delay, and energy.

**Problem & objective**: A non-convex mixed control problem minimizes weighted energy and end-to-end inference delay, $\min \omega_E E_{\mathrm{tot}}+\omega_T T_{\mathrm{avg}}$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| DNN partition point | $l_m$ | integer layer index | Last locally executed layer for user $m$ |
| GU-UAV association | $x_{m,k}$ | binary | UAV $k$ serving ground user $m$ |
| Compute ratio | $f_{m,k}$ | continuous, nonnegative | UAV computation allocated to user $m$ |
| UAV velocity | $\mathbf v_k(t)$ | continuous bounded vector | Trajectory action of UAV $k$ |
| GU transmit power | $p_m(t)$ | continuous, bounded | Intermediate-feature uplink power |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Each user selects one valid DNN partition and at most one UAV |
| C2 | Associated users lie inside UAV coverage radius |
| C3 | Per-UAV user count and computation allocation remain within capacity |
| C4 | Ground-user transmit powers stay within limits |
| C5 | UAV speed, region, and battery consumption remain feasible |

**Algorithm**: Search feasible DNN partition points with OPPS → rank GU-UAV pairs by weighted delay-energy improvement → match users and allocate UAV compute with fairness weights → let TD3 choose UAV velocities and user transmit powers → evaluate the joint cost and boundary penalties → repeat across slots.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zhai et al. [x] studied task offloading with collaborative DNN inference in multi-UAV mobile edge computing networks. They formulated weighted energy and delay minimization over DNN partition points, GU-UAV association, computing-resource ratios, UAV trajectories, and user transmit powers. DPDTS applies OPPS to select layer partitions and uses fairness-aware matching to associate users and allocate UAV compute. A TD3 controller then selects UAV velocity vectors and user transmit powers under coverage, capacity, power, battery, and movement constraints. Simulations report lower energy and average inference delay than the evaluated DTS, RAT, EE-PPO, and DPRT baselines.

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
