---
type: source
title: "Learning-Based Over-the-Air Integrated Sensing, Communication and Computation in UAV Swarm-Enabled Intelligent Transportation Systems"
authors: ["Peng Hou", "Hongbin Zhu", "Zhihui Lu", "Shin-Chia Huang", "Yang Yang", "Hongfeng Chai"]
year: 2025
url: "https://doi.org/10.1109/TGCN.2024.3492028"
venue: "IEEE Transactions on Green Communications and Networking (IEEE TGCN), 9(3), 2025"
modeling_card: required
tags: [source, integrated-sensing-computation-communication, uav-enabled-its, multi-uav, ppo, deep-reinforcement-learning, resource-allocation]
related:
  - "[[integrated-sensing-computation-communication]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[uav-enabled-its]]"
  - "[[ppo]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[device-association]]"
  - "[[qin-2025-urllc-noma-uav-iscc]]"
  - "[[zhao-2026-mappo-jscc-aec]]"
created: 2026-07-07
updated: 2026-07-16
---

# Learning-Based Over-the-Air Integrated Sensing, Communication and Computation in UAV Swarm-Enabled Intelligent Transportation Systems

## Citation

Hou, P., Zhu, H., Lu, Z., Huang, S.-C., Yang, Y., & Chai, H. (2025). *Learning-Based Over-the-Air Integrated Sensing, Communication and Computation in UAV Swarm-Enabled Intelligent Transportation Systems*. **IEEE Transactions on Green Communications and Networking**, 9(3), 1414-1428. DOI: 10.1109/TGCN.2024.3492028. (The parse gives DOI, publication date 5 Nov 2024, and current version 21 Aug 2025; volume/issue/pages/venue verified against the title-matched Crossref/IEEE DOI record.)

## TL;DR

Introduces an Air-ISCC framework for UAV-swarm-enabled ITS where UAVs sense the environment, communicate with IoTDs, and compute offloaded tasks. The paper jointly optimizes time-slot scheduling, sensing/communication power, computing-resource allocation, and service association to maximize service success while minimizing UAV energy. PBIA, a PPO-based DRL algorithm with parallel training, learns UAV-swarm service policies.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A UAV swarm provides sensing, over-the-air communication, and edge computation to mobile IoT devices in an ITS region. Each slot is split into sensing and service phases, and a control UAV coordinates the participating UAVs under finite power and compute resources.

**Problem & objective**: Jointly maximize task-service success and minimize system energy, $\max_{\boldsymbol\alpha,\mathbf p,\boldsymbol\varepsilon,\mathcal C}N^{-1}\sum_t\{-\mathcal E[t],\mathcal O[t]\}$, over scheduling, sensing power, compute shares, and service associations.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Slot scheduling share | $\alpha_j[t]$ | continuous, $(0,1]$ | Sensing and service time assigned to UAV $j$ |
| UAV sensing power | $p_j[t]$ | continuous, $(0,p_{\max}]$ | Radar or sensing transmit power |
| Service association | $c_{i,j}[t]$ | binary, one-hot | UAV selected by IoT device $i$ |
| Compute-resource share | $\varepsilon_{i,j}[t]$ | continuous, $[0,1]$ | Fraction of UAV $j$'s compute assigned to device $i$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | IoT devices remain inside the UAV swarm's service region. |
| C2 | Scheduling shares and sensing powers remain within their allowed bounds. |
| C3 | Each IoT device associates with exactly one UAV. |
| C4 | Compute shares are nonnegative and sum to at most one at each UAV. |
| C5 | Sensing quality meets the target condition. |
| C6 | Communication and computation finish each successful task within its service deadline. |

**Algorithm**: Convert the multiobjective design to an MDP whose reward is completed-service reward minus weighted UAV and device energy. Use a PPO actor to emit the mixed scheduling, power, resource, and association action, map association scores to one-hot choices, update actor and critic with clipped objectives and generalized advantage estimation, and accelerate training with asynchronous parallel workers before deploying the policy on the control UAV.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Hou et al. [x] formulated UAV-swarm over-the-air sensing, communication, and computation as joint scheduling, sensing-power, compute-allocation, and device-association control. They maximized service success while minimizing UAV and device energy under service-region, power, one-UAV association, compute-capacity, sensing-quality, and delay constraints. PBIA maps the problem to a mixed-action MDP and trains a PPO actor-critic with clipped updates, generalized advantage estimation, and asynchronous parallel workers. Across 100 tests, PBIA reported 97.58% average success, reward 279.527, and load-balance metric 0.863, with success gains from 16.32% to 61.44% over the baselines.

## Problem framing

ITS emergency and traffic scenarios need sensing, communication, and computation at the same time. A single UAV has limited sensing range, communication rate, computing capacity, and energy, while a UAV swarm has to coordinate multidimensional resources and avoid inefficient competition among IoTDs. The paper turns this coupled Air-ISCC design into a sequential decision-making problem.

## System model

- The network has a UAV swarm and terrestrial IoTDs in a Manhattan-style ITS area.
- Communication/sensing links between IoTDs and the master eNodeB can be blocked by terrain or traffic accidents.
- UAVs carry antenna arrays, radar sensing units, computing resources, and storage.
- Each time slot is split by TDM: the first sub-slot senses environment/target information, and the second provides communication and computation service for offloaded IoTD tasks.
- Service decisions include sensing time, sensing power, UAV-IoTD association, and CPU-resource allocation.

## Method

The optimization target combines service success and UAV energy consumption. The paper models state, action, and reward for an MDP and proposes PBIA, a Proximal Policy Optimization based Air-ISCC algorithm. A parallel DRL training scheme lets multiple workers collect experience from Air-ISCC environments and send updates through a server-side PPO training loop before deployment on the control UAV.

## Key findings

- PBIA learns a stable service policy and converges faster than the DDPG and REINFORCE baselines in the reported reward curves.
- In 100 testing episodes, Table III reports PBIA average success rate 97.58% +/- 6.47%, average reward 279.527 +/- 19.716, and the best load-balance metric, 0.863 +/- 0.439.
- Across varying IoTD counts, the paper reports PBIA success-rate gains of 16.32% to 61.44% over baselines, and load-balancing improvements of 50.09% to 72.23%.
- PBIA remains effective as IoTD speeds, UAV counts, and energy-weighting factors vary, although the parse notes reduced stability as IoTD movement speed increases.

## Limitations / future work

The conclusion states that the study restricts UAV mobility; multi-UAV trajectory optimization in dynamic ITS environments is identified as future work.

## Relation to the corpus

This source expands [[integrated-sensing-computation-communication]] from single-UAV/FEEL and HAP-assisted AEC settings into a UAV-swarm ITS service system. It is closer to [[uav-enabled-its]] than to generic vehicular offloading: UAVs provide sensing, communication, and compute services for moving IoTDs in emergency/traffic scenes. Methodologically, PBIA reinforces the [[ppo]] lineage and complements [[zhao-2026-mappo-jscc-aec]] and [[qin-2025-urllc-noma-uav-iscc]] as ISCC/ISAC-MEC control entries.

## Raw artifacts

- `raw/sources/Learning-Based Over-the-Air Integrated Sensing- Communication and Computation in UAV Swarm-Enabled Intelligent Transportation Systems/Learning-Based Over-the-Air Integrated Sensing- Communication and Computation in UAV Swarm-Enabled Intelligent Transportation Systems.md`
- Original PDF and extracted figures (`images/`) in the same folder.
