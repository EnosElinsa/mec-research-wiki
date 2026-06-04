---
type: source
title: "Space/Aerial-Assisted Computing Offloading for IoT Applications: A Learning-Based Approach"
authors: ["Nan Cheng", "Feng Lyu", "Wei Quan", "Conghao Zhou", "Hongli He", "Weisen Shi", "Xuemin Shen"]
year: 2019
url: "https://doi.org/10.1109/JSAC.2019.2906789"
venue: "IEEE Journal on Selected Areas in Communications (IEEE JSAC)"
tags: [source, sagin, iot, task-offloading, reinforcement-learning, edge-computing, satellite, uav-mec, early-sagin]
related:
  - "[[task-offloading]]"
  - "[[xuemin-shen]]"
  - "[[ullah-2026-mec-drl-ntn-survey]]"
  - "[[liu-2023-sagecn-online-offloading]]"
  - "[[three-tier-cloud-edge-end]]"
created: 2026-06-04
updated: 2026-06-04
---

# Space/Aerial-Assisted Computing Offloading for IoT Applications: A Learning-Based Approach

## Citation

Cheng, N., Lyu, F., Quan, W., Zhou, C., He, H., Shi, W., & Shen, X. (2019). *Space/Aerial-Assisted Computing Offloading for IoT Applications: A Learning-Based Approach*. **IEEE Journal on Selected Areas in Communications**, 37(5). DOI: 10.1109/JSAC.2019.2906789. (Received 10 October 2018; accepted 13 March 2019; published 21 March 2019; current version 16 April 2019.)

## TL;DR

One of the **first papers to study computing offloading in a SAGIN** (Space-Air-Ground Integrated Network). UAVs serve as flying edge servers (low-latency local offloading); satellites provide always-on cloud computing (higher delay but unlimited compute). Formulates the SAG-IoT offloading problem as a **Markov Decision Process (MDP)** and solves it with an **actor-critic RL** algorithm (policy gradient + value network) to learn the optimal offloading policy on-the-fly. A separate heuristic handles the **VM resource allocation and task scheduling** on UAV edge servers. Demonstrates near-optimal VM allocation and fast-converging RL offloading with lower total cost than baselines.

## Problem framing

Remote IoT devices in rural/suburban areas lack terrestrial edge infrastructure. SAGIN integrates: (i) UAVs as flying edge servers (near-user, low-delay but UAV mobility causes dynamic availability); (ii) satellites for cloud access (high-delay but ubiquitous). Designing an offloading policy that exploits both tiers while adapting to UAV mobility, varying channel conditions, and heterogeneous IoT task demands is a multi-dimensional, non-stationary optimization problem. Standard convex optimization cannot handle the non-stationarity; RL learns from experience without a system model.

## System model

- **M IoT users**, each with N applications. Three offloading options per task: (i) local execution; (ii) offload to UAV edge VM; (iii) offload to satellite/cloud.
- **UAV edge servers:** VMs virtualize compute resources for parallel execution; joint VM resource allocation + task scheduling solved as a mixed-integer program (heuristic approximation).
- **SAGIN channel:** UAV-ground and satellite-ground links; dynamic due to UAV mobility.
- **MDP formulation:** state = remaining task queue + channel states + VM availability; action = offloading decision matrix; reward = negative weighted sum of delay, energy consumption, and server usage cost.
- **Actor-critic RL:** policy gradient for large action space + critic (value function) to accelerate learning.

## Key findings

- Proposed VM allocation heuristic achieves **near-optimal performance** with much lower computational complexity than exact mixed-integer programming (parse Section IV / results).
- Actor-critic RL offloading algorithm **converges fast** and achieves **lower total cost** (weighted delay + energy + usage cost) than baselines: cloud-only, edge-only, random offloading (parse Section VI).
- Claimed to be the **first work to study computing offloading in SAGIN**, establishing the feasibility of SAGIN supporting computation-intensive IoT applications (parse Section I contributions).

## Limitations / future work

Pre-DRL era (early RL + actor-critic; not deep actor-critic with neural network approximation). Fixed UAV trajectories (not jointly optimized with offloading). Single satellite/cloud tier. The parse does not give specific numerical gains in the results section (deferred to figures).

## Relation to the corpus

Xuemin Shen ([[xuemin-shen]]) is a co-author. The **earliest SAGIN computing-offloading paper** in the corpus — prior to and conceptually foundational for [[liu-2023-sagecn-online-offloading]], [[cheng-2025-dos-satellite-edge-computing]], [[zhang-2023-three-tier-satellite-offloading]], and the [[ullah-2026-mec-drl-ntn-survey]] which surveys this line of work. The [[three-tier-cloud-edge-end]] concept is explicitly instantiated as satellite cloud + UAV edge + local.

## Raw artifacts

- `raw/sources/Space_Aerial-Assisted_Computing_Offloading_for_IoT_Applications_A_Learning-Based_Approach/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
