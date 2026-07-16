---
type: source
title: "Two-Hop Partial Task Offloading and Resource Allocation in Air-Ground Integrated Mobile Edge Computing Network: A DRL-Based Method"
authors: ["Shichao Li", "Bingji Lu", "Laha Ale", "Hongbin Chen", "Fangqing Tan", "Jingyue Huang"]
year: 2025
url: "https://doi.org/10.1109/JIOT.2025.3548088"
venue: "IEEE Internet of Things Journal (IEEE IoT-J)"
tags: [source, air-ground-integrated-network, partial-offloading, resource-allocation, maddpg, ippo, prioritized-experience-replay, hap, uav]
related:
  - "[[air-ground-integrated-network]]"
  - "[[high-altitude-platform-station]]"
  - "[[binary-vs-partial-offloading]]"
  - "[[multi-agent-td3]]"
  - "[[ppo]]"
  - "[[prioritized-experience-replay]]"
  - "[[uav-trajectory-control]]"
  - "[[wang-2024-hybrid-oma-noma-sagin]]"
  - "[[kang-2023-mappo-hierarchical-aerial]]"
created: 2026-05-29
updated: 2026-07-16
modeling_card: required
---

# Two-Hop Partial Task Offloading and Resource Allocation in Air-Ground Integrated Mobile Edge Computing Network: A DRL-Based Method

## Citation

Li, S., Lu, B., Ale, L., Chen, H., Tan, F., & Huang, J. (2025). *Two-Hop Partial Task Offloading and Resource Allocation in Air-Ground Integrated Mobile Edge Computing Network: A DRL-Based Method*. **IEEE Internet of Things Journal**. DOI: 10.1109/JIOT.2025.3548088.

## TL;DR

A joint partial-task-offloading, resource-allocation, and UAV-trajectory-design problem in an **air-ground integrated MEC** network for Internet of Remote Things (IoRT), where UAVs and HAPs execute tasks. The objective is to minimize total offloading delay across all IoRT devices. The non-convex problem is cast as an MDP, decomposed into two sub-problems solved with **MADDPG** (trajectory + power control) and **IPPO** (offloading + resource allocation), enhanced with **prioritized experience replay** and a noise value, yielding MADDPG-IPER, NV-IPPO, and the overall JPTORAUTD algorithm.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: IoRT devices offload partial tasks through UAV relays to HAP edge servers in a two-hop air-ground integrated MEC network over a slotted horizon.

**Problem & objective**: Jointly control UAV trajectories and powers, task split ratios, UAV and HAP CPU allocations, and minimize total task offloading delay, $\min\sum_{n,m,k_m}T_{k_m}(n)$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
| --- | --- | --- | --- |
| IoRT transmit power | $p_{k_m}(n)$ | continuous in $[0,P_{k_m}^{\max}]$ | Uplink power from device $k_m$ |
| UAV trajectory | $\mathbf q_m(n)$ | continuous 2-D position | UAV relay movement over slots |
| UAV transmit power | $p_m(n)$ | continuous in $[0,P_m^{\max}]$ | UAV-to-HAP transmit power |
| Partial offloading ratio | $\alpha_{k_m}(n)$ | continuous in $[0,1]$ | Fraction of task sent to the UAV path |
| UAV CPU allocation | $f_{m,k_m}(n)$ | continuous, bounded | CPU cycles allocated by UAV $m$ |
| HAP CPU allocation | $f_{h,k_m}(n)$ | continuous, bounded | CPU cycles allocated by the HAP |

**Constraints**:

| ID | Meaning and key expression |
| --- | --- |
| C1 | UAV and HAP CPU allocations remain within their maximum aggregate capacities. |
| C2 | IoRT and UAV transmit powers stay within power limits, with UAV energy budgets respected. |
| C3 | Partial offloading ratios satisfy $0\leq\alpha_{k_m}(n)\leq1$. |
| C4 | Each task's total two-hop execution delay meets its tolerance deadline. |
| C5 | UAV trajectories obey per-slot speed, return-to-start, and minimum separation constraints. |

**Algorithm**: Decompose the MDP into trajectory and IoRT-power control solved by MADDPG-IPER and partial offloading/resource allocation solved by noise-value IPPO, then combine both policies as JPTORAUTD.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Li et al. [x] studied partial task offloading in a two-hop air-ground integrated MEC network linking IoRT devices, UAV relays, and HAP servers. They minimized total offloading delay over UAV trajectories and powers, device powers, task split ratios, and UAV and HAP CPU allocations under energy, mobility, separation, capacity, and deadline constraints. Their JPTORAUTD decomposition uses MADDPG-IPER for trajectory and power control and noise-value IPPO for offloading and resource allocation. Simulations report consistently lower total delay than JFAM, JIAM, and JHAM baselines as HAP or UAV bandwidth and the flight period vary.

## Problem framing

MEC + air-ground integrated networks give widespread coverage for IoRT, with UAVs and HAPs executing tasks two hops away. As IoRT-device and UAV counts grow, the MDP's complexity grows, motivating problem decomposition and convergence-improving tricks.

## System model

- **Tiers.** IoRT devices → UAVs → HAPs (two-hop execution) ([[high-altitude-platform-station]]).
- **Offloading.** Partial ([[binary-vs-partial-offloading]]).
- **Objective.** Minimize total task-offloading delay of all IoRT devices → MDP.

## Method

- Decompose into:
  - **UAV trajectory + IoRT power control:** based on **MADDPG**, improved with enhanced prioritized experience replay → **MADDPG-IPER** ([[multi-agent-td3]], [[prioritized-experience-replay]]).
  - **Partial offloading + resource allocation:** based on **independent PPO (IPPO)**, with a noise value → **NV-IPPO** ([[ppo]]).
- Combine into the **JPTORAUTD** algorithm.

## Key findings

- Simulations show JPTORAUTD reduces total offloading delay versus benchmark algorithms (qualitative; specific curves in the paper).

## Limitations / future work

The parse's conclusion does not enumerate explicit future work beyond the established method.

## Relation to the corpus

A **two-hop air-ground DRL offloading** entry that combines MADDPG + IPPO across decomposed sub-problems, alongside the MAPPO hierarchical work [[kang-2023-mappo-hierarchical-aerial]] and the SCA+DQN SAGIN work [[wang-2024-hybrid-oma-noma-sagin]] (shared co-authors Hongbin Chen / Fangqing Tan). Reinforces [[air-ground-integrated-network]], [[prioritized-experience-replay]], and the partial-offloading framing.

## Raw artifacts

- `raw/sources/Two-Hop_Partial_Task_Offloading_and_Resource_Allocation_in_AirGround_Integrated_Mobile_Edge_Computing_Network_A_DRL-Based_Method/full.md`
- Original PDF and extracted figures in the same folder.
