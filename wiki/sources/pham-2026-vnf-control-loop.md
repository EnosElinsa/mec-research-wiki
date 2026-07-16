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
updated: 2026-07-16
---

# Dynamic VNF Orchestration for UAV-Aided Emergency Networks: A Learning and Optimization Control Loop Framework

## Citation

Pham, C., & Nguyen, K. K. (2026). *Dynamic VNF Orchestration for UAV-Aided Emergency Networks: A Learning and Optimization Control Loop Framework*. **IEEE Transactions on Mobile Computing**, 1-15. DOI: 10.1109/TMC.2026.3682014.

## TL;DR

Couples fast distributed multipath routing with slower centralized VNF scaling in UAV-aided emergency networks. MADDPG actors allocate service-function-chain traffic from local observations, while an event-triggered BSUM orchestrator changes VNF replicas and placement when routing constraints remain infeasible.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A UAV-aided emergency network is represented as a graph of UAV and terrestrial base stations, edge/cloud compute nodes, routers, and wired or wireless links. User sessions request latency-bounded service function chains, traffic can split over candidate paths, and virtual network functions may be replicated and placed across compute nodes under changing topology, load, battery, and link conditions.

**Problem & objective**: A two-timescale constrained control loop minimizes fast routing latency and slow VNF running/scaling cost, represented by $\min J_{\mathrm{route}}$ for path traffic and $\min J_{\mathrm{scale}}=C_{\mathrm{run}}+C_{\mathrm{change}}$ for replica placement and rates.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Path traffic split | $x_{s,p}(t)$ | continuous, $[0,1]$ | Fraction of session $s$ routed over candidate path $p$ |
| BS/user association | $a_{u,b}(t)$ | binary | Base station serving user $u$ in the slot |
| VNF replica count | $n_{v,j}$ | nonnegative integer | Instances of function $v$ hosted at node $j$ |
| VNF placement/rate | $z_{v,j},r_{v,j}$ | binary or relaxed placement; continuous rate | Location and processed traffic of each virtual function |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| R1 | Path fractions conserve every admitted session's traffic and meet its minimum rate |
| R2 | Link capacity, node buffer, battery, and energy limits are respected |
| R3 | End-to-end SFC delay includes path, handoff, rerouting, and path-splitting terms and remains bounded |
| S1 | VNF placement, replica count, compute capacity, and survival-throughput constraints remain feasible |
| S2 | Virtual-link traffic, scaling energy, and SFC latency constraints hold after orchestration |

**Algorithm**: Train distributed routing actors with centralized MADDPG critics → execute local multipath routing each slot → detect persistent routing infeasibility → relax and block the VNF scaling/placement problem → apply proximal BSUM with convexified rate terms → round placement decisions and feed the new infrastructure state back to routing.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Pham and Nguyen [x] studied dynamic virtual network function orchestration for UAV-aided emergency networks through a learning and optimization control loop. They formulated fast multipath service-function-chain routing under link, rate, buffer, battery, energy, and latency constraints and a slower VNF scaling problem under compute, replica, throughput, link, and energy constraints. Distributed routing agents are trained with MADDPG under centralized training and decentralized execution. Persistent routing infeasibility triggers a centralized orchestrator that relaxes placement variables, applies proximal block successive upper-bound minimization, and rounds the resulting placement. Simulations report 65.9 ms average end-to-end delay for MADDPG-BSUM, 212.5 average VNF instances, and 32 scaling events across 717 routing decisions in the stated experiment.

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
