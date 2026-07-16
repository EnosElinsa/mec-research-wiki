---
type: source
title: "Decentralized Navigation With Heterogeneous Federated Reinforcement Learning for UAV-Enabled Mobile Edge Computing"
authors: ["Pengfei Wang", "Hao Yang", "Guangjie Han", "Ruiyun Yu", "Leyou Yang", "Geng Sun", "Heng Qi", "Xiaopeng Wei", "Qiang Zhang"]
year: 2024
url: "https://doi.org/10.1109/TMC.2024.3439696"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
modeling_card: required
tags: [source, uav-mec, federated-reinforcement-learning, hierarchical-rl, soft-actor-critic, heterogeneous-uav, energy-efficiency, navigation]
related:
  - "[[mobile-edge-computing]]"
  - "[[federated-reinforcement-learning]]"
  - "[[hierarchical-reinforcement-learning]]"
  - "[[soft-actor-critic]]"
  - "[[heterogeneous-uav-fleet]]"
  - "[[uav-trajectory-control]]"
  - "[[task-offloading]]"
  - "[[mao-2025-bcsa-frl]]"
  - "[[zhang-2025-ssac-mgi-heterogeneous-uav]]"
created: 2026-05-31
updated: 2026-07-16
---

# Decentralized Navigation With Heterogeneous Federated Reinforcement Learning for UAV-Enabled Mobile Edge Computing

## Citation

Wang, P., Yang, H., Han, G., Yu, R., Yang, L., Sun, G., Qi, H., Wei, X., & Zhang, Q. (2024). *Decentralized Navigation With Heterogeneous Federated Reinforcement Learning for UAV-Enabled Mobile Edge Computing*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2024.3439696.

## TL;DR

A **decentralized navigation policy** for UAV-enabled MEC with **heterogeneous** UAVs (differing performance parameters), built from two pieces: a **soft hierarchical deep reinforcement learning network (SHDRLN)** and a **dual-end federated reinforcement learning (DFRL)** algorithm. SHDRLN, a maximum-entropy hierarchical DRL net, abstracts atomic actions into generic **skills** to reduce policy differences across UAVs while maximizing average task-offloading energy efficiency (good UE coverage + minimal offloading wait time). DFRL aggregates policy knowledge at a cloud server and **filters** it at the UAV end so each UAV adopts only the knowledge suited to its own performance parameters.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A swarm of heterogeneous fixed-altitude UAVs navigates disjoint task areas, serves moving UEs, and offloads queued tasks. Each UAV has distinct flight energy, coverage, CPU, and speed parameters and shares policy knowledge through a cloud server.

**Problem & objective**: The navigation objective maximizes energy efficiency $\eta=\sum_j\Lambda_j^*(T)/\sum_je_j(T)$ while meeting waiting-time and coverage requirements.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV trajectory | $\mathbb{J}$ | continuous sequence | Coordinates $[X_j(t),Y_j(t),H]$ over time |
| UAV velocity | $\mathbf V_j(t)$ | continuous, $\|\mathbf V_j\|_2\le V_j^{\max}$ | Motion state of UAV $j$ |
| Atomic acceleration action | $a_t^j$ | discrete, 17 choices | Direction and magnitude used each slot |
| CPU allocation | $f_t$ | continuous, $f_j^{\min}\le f_t\le f_j^{\max}$ | Processing rate for queued tasks |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Area boundary: $0\le X_j(t),Y_j(t)\le L$ |
| C2 | Obstacle avoidance: $[X_j(t),Y_j(t)]\notin\mathbb O_j$ |
| C3 | Speed: $0\le\|\mathbf V_j(t+1)\|_2\le V_j^{\max}$ |
| C4 | Motion directions: $0\le\mathcal U_\alpha,\mathcal U\le2\pi$ |
| C5 | UE queue bounds: $0\le\Lambda_{i_j}(t)\le\Lambda^{\max}$ |
| C6-C7 | CPU range $f_j^{\min}\le f_t\le f_j^{\max}$, waiting time $W_T\le W_T^{\max}$, and coverage $c_T\ge c_T^{\min}$ |

**Algorithm**: SHDRLN uses a maximum-entropy skill policy network with pretrained deep skill networks and actor-critic updates. DFRL aggregates skill-policy parameters at the cloud, computes policy similarity with KL divergence, and filters transferred knowledge separately at each heterogeneous UAV.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Wang et al. [x] formulated decentralized navigation for heterogeneous UAVs that must cover UEs and process queued MEC tasks despite different flight and compute capabilities. The objective maximizes completed task data per joule while constraining map boundaries, obstacles, speed, task buffers, CPU range, waiting time, and coverage. SHDRLN combines pretrained skills with a maximum-entropy hierarchical policy, and DFRL uses cloud-side KL similarity and UAV-side filtering instead of forcing one shared policy. Experiments showed faster early learning and competitive energy efficiency, waiting time, and coverage against SAC, D3QN, random, manual, and FedAvg baselines.

## Problem framing

In UAV-enabled MEC, UAVs have limited battery and heterogeneous performance, so a single centralized navigation policy is impractical (limited communication range, heterogeneity) and naive decentralized knowledge-sharing struggles when UAVs differ. The goal is energy-efficient, stable navigation policy learning that still benefits from shared knowledge, without forcing every UAV onto an identical policy.

## System model

- **Actors.** A swarm of heterogeneous UAVs, each independently training a policy network and sharing knowledge through a cloud server; UAVs provide network access / edge offloading to ground UEs.
- **Objective.** Maximize average **task-offloading energy efficiency** across all UAVs (KB/J), optimizing UE coverage and minimizing offloading waiting time.
- **Ranges.** Each UAV has communication, coverage, and observation ranges; experience is stored locally and aggregated at the cloud.

## Method

- **SHDRLN.** A hierarchical DRL network based on maximum-entropy learning that abstracts atomic actions into reusable skills, reducing inter-UAV policy divergence.
- **DFRL.** A federated-learning algorithm that aggregates skill-policy-network (SPN) parameters at the cloud and **filters** them at each UAV (adaptive selection) so each UAV keeps only navigation knowledge matched to its parameters — contrasted against plain FedAvg, under which all UAVs share one identical policy.

## Key findings

- With DFRL or FedAvg assistance, SHDRLN reaches an average energy efficiency of **2.7 KB/J after 100 (DFRL) / 200 (FedAvg) episodes**, matching the original SHDRLN trained for **300 episodes** — i.e. federated knowledge sharing cuts early-stage random exploration (verbatim figure-read).
- With SAC + DFRL/FedAvg, ~2.4 KB/J is reached after 50 episodes, matching plain SAC at 100 episodes.
- DFRL's final converged energy efficiency **surpasses** the original SHDRLN, whereas FedAvg converges slightly below it — because FedAvg forces one shared policy while DFRL lets each UAV selectively learn a policy tailored to itself. Aggregating very dissimilar policies (as in SAC) degrades performance.
- DFRL gives more stable navigation-policy learning across different heterogeneity levels (G ∈ {5,10,15,20} in the parsed curves).

## Limitations / future work

Simulation-only. Stated future work is to improve policy-model generality, extend SHDRLN/DFRL to multi-task scenarios such as task offloading, edge caching, and load balancing, and use a more comprehensive communication-channel model. Results rest on figure-read energy-efficiency curves (flagged indicative). The approach assumes a cloud aggregator reachable by all UAVs. DOI date of publication 7 Aug 2024 / date of current version 5 Nov 2024 → year 2024.

## Relation to the corpus

A **federated-reinforcement-learning** UAV-MEC entry that, unlike the corpus's other FRL work, targets **heterogeneous** UAVs and adds hierarchical (skill-abstraction) RL. It complements [[mao-2025-bcsa-frl]] (blockchain-enabled cold-start FRL aggregation) by attacking heterogeneity at the aggregation/filtering step, and shares the heterogeneous-fleet framing of [[zhang-2025-ssac-mgi-heterogeneous-uav]] (safe SAC for heterogeneous UAV-MEC). Reinforces [[federated-reinforcement-learning]], [[hierarchical-reinforcement-learning]], [[soft-actor-critic]], and [[heterogeneous-uav-fleet]]. Co-author [[geng-sun]] (Jilin University) recurs across the aerial-MEC cluster.

## Raw artifacts

- `raw/sources/Decentralized_Navigation_With_Heterogeneous_Federated_Reinforcement_Learning_for_UAV-Enabled_Mobile_Edge_Computing/full.md`
- Original PDF and extracted figures in the same folder.
