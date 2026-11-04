---
type: source
modeling_card: required
title: "Dynamic VNF Orchestration for UAV-Aided Emergency Networks: A Learning and Optimization Control Loop Framework"
authors: ["Chuan Pham", "Kim Khoa Nguyen"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3682014"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), pp. 1-15"
tags: [source, vnf, service-function-chaining, emergency-network, maddpg, bsum, centralized-training-decentralized-execution]
related:
  - "[[routing-vnf-scaling-control-loop]]"
  - "[[network-function-virtualization]]"
  - "[[service-function-chaining]]"
  - "[[maddpg]]"
  - "[[block-successive-upper-bound-minimization]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[post-disaster-mec]]"
  - "[[persistent-emergency-uav-swarm-service]]"
  - "[[zhang-2025-vnf-sgin-dql]]"
  - "[[du-2023-maddpg-service-placement-agin]]"
created: 2026-07-13
updated: 2026-11-03
---

# Dynamic VNF Orchestration for UAV-Aided Emergency Networks: A Learning and Optimization Control Loop Framework

## Citation

Pham, C., & Nguyen, K. K. (2026). *Dynamic VNF Orchestration for UAV-Aided Emergency Networks: A Learning and Optimization Control Loop Framework*. **IEEE Transactions on Mobile Computing**, 1-15. DOI: 10.1109/TMC.2026.3682014.

## TL;DR

Couples fast distributed multipath routing with slower centralized VNF scaling in UAV-aided emergency networks. MADDPG actors allocate service-function-chain traffic from local observations, while an event-triggered BSUM orchestrator changes VNF replicas and placement when routing constraints remain infeasible.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A UAV-aided emergency network (UAVs, terrestrial nodes, wired and wireless links) serves user sessions through service function chains (SFCs) under a hybrid O-RAN architecture. Wireless link capacity $B_e(t)$ depends on SNR and LoS probability, UAV batteries drain with operation and computing, and flows may split over candidate paths $\mathcal P_i$.

**Problem & objective**: Two coupled problems run at different time scales. P1 in (8)–(9) chooses path rates to minimize $\sum_t\mathbb L(t)$, where $\mathbb L(t)$ in (7) weights the worst-path latency of each critical SFC, a handoff/rerouting latency, and a path-splitting penalty. P2 in (22) chooses VNF instances and virtual-link rates to minimize $\sum_t\zeta(t)$, with $\zeta(t)$ in (20) the instance cost plus a penalty on scaling events.

**Decision variables**:
| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Path rate (P1) | $w_{ij}(t)$ | continuous, nonnegative | Data rate of flow $i$ on path $j$ |
| VNF instances (P2) | $x_{nv}^c(t)$ | integer | Instances of the $n$-th VNF of chain $c$ on node $v$ |
| Virtual-link rate (P2) | $r_{n\to(vv')}^c(t)$ | continuous | Rate of the $n$-th virtual link of chain $c$ on physical link $(v,v')$ |

**Constraints**:
| ID | Meaning and key expression |
|---|---|
| (1) | P1 link capacity: $\sum w_{ij}(t)a_{e,j}\le B_e(t)$ |
| (2) | P1 minimum flow rate: $\sum_jw_{ij}(t)\ge\bar w_i$ |
| (3) | P1 node backlog within buffer $\epsilon_v(t)$ |
| (4)–(5) | P1 UAV energy per slot and minimum battery $E_v(t)\ge E_{\min}$ |
| (6) | P1 mission-critical latency: $\max_jL_j(t)\phi(w_{ij}(t))\le\bar L_i$ |
| (10) | P2 node compute: $\sum_{c,n}x_{nv}^c(t)p_n\le\kappa_vp_v$ (battery-scaled) |
| (11) | P2 minimum instances: $\sum_vx_{nv}^c(t)\ge I_n^c(t)$ |
| (12)–(13) | P2 SFC demand from P1 and survival throughput $\ge\varrho^c\lambda^c(t)$ |
| (14) | P2 link capacity for virtual-link rates |
| (17) | P2 end-to-end SFC latency including processing (15)–(16), propagation, and migration latency |
| (18)–(19) | P2 UAV energy and minimum battery |
| (21) | P2 big-$M$ coupling of placement and traffic |

**Algorithm**: Distributed MADDPG routing agents (centralized training, decentralized execution) solve P1 each slot; persistent infeasibility triggers the orchestrator, which relaxes $x_{nv}^c$, solves P2 by proximal BSUM, rounds the placement, and feeds the new state back to routing.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Pham and Nguyen [x] studied dynamic virtual network function orchestration for UAV-aided emergency networks through a learning and optimization control loop. They formulated fast multipath service-function-chain routing under link, rate, buffer, battery, energy, and latency constraints and a slower VNF scaling problem under compute, replica, throughput, link, and energy constraints. Distributed routing agents are trained with MADDPG under centralized training and decentralized execution. Persistent routing infeasibility triggers a centralized orchestrator that relaxes placement variables, applies proximal block successive upper-bound minimization, and rounds the resulting placement. Simulations report 65.9 ms average end-to-end delay for MADDPG-BSUM, close to but slightly worse than A2C in the varying setting, and 212.5 average VNF instances (2.6% fewer than Best-fit), while A2C-SFC reaches a lower scaling cost (33.78 versus 36.12); scaling occurred 32 times across 717 routing decisions.

## Problem

Emergency areas may lose terrestrial coverage while mission-critical calling, video, and monitoring services still require low-latency [[service-function-chaining|service function chains]]. Virtualized RAN/core functions can run on UAVs, terrestrial base stations, edge nodes, or cloud nodes, but topology, bursty traffic, compute, links, payload, and batteries change faster than static VNF placement can follow.

## System model

- A graph contains UAV/terrestrial base stations, edge/cloud compute nodes, routers, and wired/wireless links. Nodes can host gNB, gateway, AMF, UPF, SMF, and other virtual network functions.
- User sessions request SFCs with minimum rates and latency bounds. One base station serves each user per slot, but a flow may be split over candidate paths.
- Routing latency includes selected-path delay, handoff/rerouting overhead, and a path-splitting penalty under link, rate, buffer, battery, energy, and end-to-end delay constraints.
- VNF scaling chooses integer instance counts and virtual-link traffic rates, balancing running and scaling costs under compute, replica, survival-throughput, link, latency, and energy constraints.

## Method

The [[routing-vnf-scaling-control-loop]] has two timescales. Each base station runs a routing agent every slot. The routing problem is a partially observable Markov game: local actors see connected users and local paths, while centralized critics use global state and all agents' actions during MADDPG training.

Persistent routing infeasibility triggers a centralized VNF-scaling problem. The orchestrator relaxes integer placements, divides placement/rate variables into blocks, applies proximal [[block-successive-upper-bound-minimization|BSUM]] with convexified rate terms, and rounds the resulting placement back to integers. Placement changes alter subsequent routing; observed routing loads inform later scaling.

## Key findings

- Across 534 sessions and 1000 slots, average end-to-end delay is `62.5 ms` for an ideal centralized A2C-SFC baseline, `65.9 ms` for MADDPG-BSUM, and `79.2 ms` for offline MEC.
- At peak load, delay composition is reported as `56%` propagation, `34%` processing, `9.8%` handoff, and `0.19%` migration.
- BSUM averages `212.5` VNF instances versus `218.1` for Best-fit, a stated `2.6%` reduction; average scaling costs are `33.78/36.12/39.25` for A2C-SFC/BSUM/Best-fit.
- BSUM uses `37.9%` of active-link bandwidth versus `43.6%` for Best-fit. The loop performs 32 scaling events and 717 routing decisions, about one scaling event per 22 routing decisions.
- With `20%` random link drops at peak load, latency rises by about `10%`; the paper explicitly limits this result to simulation.

## Limitations / parse caveats

The evaluation uses synthetic traffic on a modified CORONET topology, not measured emergency traffic or hardware. The ideal full-information A2C-SFC implementation is not directly comparable to the original baseline system. Node totals conflict (`72` stated versus `44 + 38` in the table), request-lifetime/data-size settings conflict, and A2C-SFC acceptance is `9.4` in the table but `9.7` in prose. The channel study mixes static average path loss with random slot degradation, and the authors leave stochastic channels, empirical batteries, and hardware-in-the-loop tests to future work. Several equations, tables, and one latency-violation sentence are OCR-damaged.

## Relation to the corpus

Unlike [[zhang-2025-vnf-sgin-dql]], which learns VNF selection/chaining in a satellite-ground network, this source separates local emergency routing from event-triggered VNF replication and placement. It also differs from task-offloading controllers: the controlled objects are SFC traffic and VNF instances across a virtualized emergency infrastructure.

## Raw artifacts

- Parse: `raw/sources/Dynamic_VNF_Orchestration_for_UAV-Aided_Emergency_Networks_A_Learning_and_Optimization_Control_Loop_Framework/Dynamic_VNF_Orchestration_for_UAV-Aided_Emergency_Networks_A_Learning_and_Optimization_Control_Loop_Framework.md`
- Origin PDF: `raw/sources/Dynamic_VNF_Orchestration_for_UAV-Aided_Emergency_Networks_A_Learning_and_Optimization_Control_Loop_Framework/Dynamic_VNF_Orchestration_for_UAV-Aided_Emergency_Networks_A_Learning_and_Optimization_Control_Loop_Framework.pdf`
- Figures: `raw/sources/Dynamic_VNF_Orchestration_for_UAV-Aided_Emergency_Networks_A_Learning_and_Optimization_Control_Loop_Framework/images/`
