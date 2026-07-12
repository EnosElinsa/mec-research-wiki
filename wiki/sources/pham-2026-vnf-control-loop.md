---
type: source
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
updated: 2026-07-13
---

# Dynamic VNF Orchestration for UAV-Aided Emergency Networks: A Learning and Optimization Control Loop Framework

## Citation

Pham, C., & Nguyen, K. K. (2026). *Dynamic VNF Orchestration for UAV-Aided Emergency Networks: A Learning and Optimization Control Loop Framework*. **IEEE Transactions on Mobile Computing**, 1-15. DOI: 10.1109/TMC.2026.3682014.

## TL;DR

Couples fast distributed multipath routing with slower centralized VNF scaling in UAV-aided emergency networks. MADDPG actors allocate service-function-chain traffic from local observations, while an event-triggered BSUM orchestrator changes VNF replicas and placement when routing constraints remain infeasible.

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
