---
type: source
title: "Mobile-Edge Computing in SAGINs: A Hybrid Action Space P-DDQN Algorithm for Joint Offloading and Resource Allocation"
authors: ["Haosheng Chen", "Haixia Cui", "Peng Cao", "Yejun He", "Jun Li", "Ivan Wang-Hei Ho", "Victor C. M. Leung"]
year: 2026
url: "https://doi.org/10.1109/TWC.2026.3706356"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), 25, 2026"
tags: [source, sagin, leo-satellite-edge-computing, uav-mec, task-offloading, hybrid-action, parameterized-dqn, ddqn, ddpg]
related:
  - "[[space-air-ground-integrated-network]]"
  - "[[leo-satellite-edge-computing]]"
  - "[[leo-satellite-coverage-time]]"
  - "[[hybrid-action-decision-making]]"
  - "[[parameterized-dqn]]"
  - "[[ddqn]]"
  - "[[ddpg]]"
  - "[[task-offloading]]"
  - "[[uav-trajectory-control]]"
  - "[[device-association]]"
  - "[[victor-c-m-leung]]"
created: 2026-07-07
updated: 2026-07-07
---

# Mobile-Edge Computing in SAGINs: A Hybrid Action Space P-DDQN Algorithm for Joint Offloading and Resource Allocation

## Citation

Chen, H., Cui, H., Cao, P., He, Y., Li, J., Ho, I. W.-H., & Leung, V. C. M. (2026). *Mobile-Edge Computing in SAGINs: A Hybrid Action Space P-DDQN Algorithm for Joint Offloading and Resource Allocation*. **IEEE Transactions on Wireless Communications**, 25, 19115-19130. DOI: 10.1109/TWC.2026.3706356. (DOI/venue/year verified against the title-matched Crossref/IEEE DOI record; the parse header itself does not print the DOI.)

## TL;DR

Proposes a MEC-enabled SAGIN for remote areas where IoT devices can compute locally, offload to a UAV edge server, or offload to LEO satellite edge servers. The optimization minimizes weighted energy plus latency under satellite coverage-time and partial-offloading constraints. Because device association and satellite selection are discrete while transmit power, task ratios, and trajectory variables are continuous, the paper uses a parameterized DDQN (P-DDQN) that combines DDQN for discrete actions with DDPG for continuous parameters.

## Problem framing

Remote and underdeveloped regions lack terrestrial base-station support, while UAV-only MEC is constrained by coverage and energy. LEO satellites add wide-area coverage and stronger compute, but their moving coverage windows restrict feasible satellite offloading. The resulting resource-allocation problem couples UAV 3D trajectory, IoT-device association, transmit power, satellite association, and partial task assignment.

## System model

- **Layers.** Ground IoT devices, one UAV MEC server, and multiple LEO satellites with MEC servers.
- **Coverage.** UAV coverage depends on its 3D position; LEO service is constrained by remaining satellite coverage time derived from orbital geometry and minimum elevation angle.
- **Tasks.** Each IoT task can be partitioned for local execution, UAV execution, and LEO execution.
- **Objective.** Minimize a weighted sum of delay and energy while respecting UAV battery, communication, compute, and partial-offloading constraints.

## Method

The paper formulates a long-term sequential optimization problem with a hybrid action space. P-DDQN parameterizes each discrete action with continuous variables: DDQN selects discrete decisions such as user scheduling and satellite association, while a DDPG-style policy network generates continuous parameters such as task-offloading ratios and transmit powers. The double-DQN target is used to reduce Q-value overestimation relative to P-DQN.

## Key findings

- P-DDQN reaches the highest reward among P-DQN, PPO, DDPG, and DDQN baselines in the reported training comparison, converging around the reported reward level after roughly 500 episodes.
- System cost rises with task CPU-cycle demand and IoT-device count; P-DDQN remains below the baseline costs, with larger advantage when task complexity exceeds 1 Gcycle.
- System cost decreases as the number of LEO satellites increases because higher satellite density improves access probability, elevation, and coverage duration.
- Ablations show fixed transmit power and fixed UAV altitude increase system cost; the per-slot comparison reports P-DDQN around 2.30 system cost, fixed altitude around 2.65, and fixed power as the most unstable/higher-cost case.
- Optimized UAV altitude adapts to IoT-device distribution, flying higher for dispersed devices and lower for dense devices to reduce energy when long-range coverage is less necessary.

## Limitations / future work

The conclusion proposes extending the framework to more complex SAGIN scenarios with multi-UAV cooperative optimization, and exploring multi-agent hybrid-action algorithms based on soft actor-critic for broader evaluations.

## Relation to the corpus

This source strengthens the [[space-air-ground-integrated-network]] / [[leo-satellite-edge-computing]] offloading track with a native hybrid-action DRL formulation. It is close to [[chen-2024-ulse-game]] in using UAV-LEO cooperation and coverage-time constraints, but solves a joint offloading/resource/trajectory problem with P-DDQN rather than a game-theoretic distributed best-response. Methodologically it extends [[parameterized-dqn]] beyond vehicular MEC and connects [[ddqn]], [[ddpg]], [[hybrid-action-decision-making]], and [[leo-satellite-coverage-time]]. Co-author [[victor-c-m-leung]] links it to the wiki's recurring senior-collaborator roster.

## Raw artifacts

- `raw/sources/Mobile-Edge Computing in SAGINs A Hybrid Action Space P-DDQN Algorithm for Joint Offloading and Resource Allocation/Mobile-Edge Computing in SAGINs A Hybrid Action Space P-DDQN Algorithm for Joint Offloading and Resource Allocation.md`
- Original PDF and extracted figures (`images/`) in the same folder.
