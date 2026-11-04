---
type: source
modeling_card: required
title: "Joint Task Offloading and Resource Allocation in UAV-Enabled Mobile Edge Computing"
authors: ["Zhe Yu", "Yanmin Gong", "Shimin Gong", "Yuanxiong Guo"]
year: 2020
url: "https://doi.org/10.1109/JIOT.2020.2965898"
venue: "IEEE Internet of Things Journal (IEEE IoT-J)"
tags: [source, uav-mec, computation-offloading, resource-allocation, sca, edge-cloud-collaboration, energy-latency-tradeoff]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[uav-trajectory-control]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[energy-latency-tradeoff]]"
  - "[[binary-vs-partial-offloading]]"
  - "[[zhang-2019-uav-iot-comp-comm]]"
  - "[[liu-2022-miso-uav-mec-trajectory]]"
created: 2026-05-29
updated: 2026-11-03
---

# Joint Task Offloading and Resource Allocation in UAV-Enabled Mobile Edge Computing

## Citation

Yu, Z., Gong, Y., Gong, S., & Guo, Y. (2020). *Joint Task Offloading and Resource Allocation in UAV-Enabled Mobile Edge Computing*. **IEEE Internet of Things Journal**. DOI: 10.1109/JIOT.2020.2965898.

## TL;DR

A UAV-enabled MEC system where a UAV and edge clouds (ECs) **collaboratively** serve stationary IoT devices in regions where ECs are inaccessible due to terrestrial signal blockage/shadowing. The paper minimizes the weighted sum of all devices' service delay and UAV energy consumption by jointly optimizing UAV position, communication and computing resource allocation, and task-splitting decisions, solving the non-convex problem with **successive convex approximation (SCA)**.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Stationary IoT mobile users (MUs) do not compute locally; they offload every task to one UAV over ground-to-air (G2A) links, and the UAV processes a portion onboard and forwards the rest over air-to-ground (A2G) links to terrestrial edge clouds (ECs). The service delay of MU $i$ is $T_i=t_i^{\mathrm{G2A}}+\max_j\{t_i^{\mathrm{UAV}},t_{ij}^{\mathrm{A2G}}+t_{ij}^{\mathrm{EC}}\}$ (13).

**Problem & objective**: Problem (14) minimizes the weighted sum of UAV energy and service delay, $\min\sum_iE_i^{\mathrm{UAV}}+\rho\sum_iT_i$, over UAV position, uplink bandwidth, task partition, and UAV and EC CPU allocation.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV position | $Q^{\mathrm{UAV}}$ | continuous position | Aerial MEC deployment |
| Uplink bandwidth | $B_i^{\mathrm{UL}}$ | continuous, nonnegative | G2A bandwidth for MU $i$ |
| Task partition | $\beta_{i0},\beta_{ij}$ | continuous, $[0,1]$ | Portion of MU $i$'s task processed at the UAV or EC $j$ |
| CPU allocation | $f_i^{\mathrm{UAV}},f_{ij}^{\mathrm{EC}}$ | continuous, nonnegative | UAV and EC computation assigned to MU $i$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| (14b) | Total uplink bandwidth, $\sum_iB_i^{\mathrm{UL}}\leq B^{\mathrm{UL}}$ |
| (14c) | Each task is fully processed, $\beta_{i0}+\sum_j\beta_{ij}=1$ |
| (14d)-(14e) | UAV and EC CPU allocations stay within $F^{\mathrm{UAV}}$ and $F_j^{\mathrm{EC}}$ |
| (14f)-(14i) | Partition variables in $[0,1]$ and nonnegative bandwidth and CPU allocations |

**Algorithm**: Linearize the max term with auxiliary variables $z_i$ to obtain (15), then apply SCA: replace nonconvex terms with convex approximations around the current point, solve the convex problem, update the expansion point, and repeat until the cost converges.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Yu et al. [x] studied joint task offloading and resource allocation in a UAV-enabled mobile edge computing network where a UAV and terrestrial edge clouds serve stationary IoT devices collaboratively. They formulated a weighted service-delay and UAV-energy minimization problem over UAV placement, task splitting, communication resources, and computing resources. Users offload all tasks to the UAV, which splits them between onboard processing and the edge clouds; the constraints enforce complete task partitioning and bandwidth and processor capacities. Their algorithm replaces non-convex terms with tractable local convex approximations and iterates successive convex optimization. Numerical results show lower weighted cost than UAV-only, edge-cloud-only, and fixed UAV-EC schemes, and than a random UAV location.

## Problem framing

Existing MEC fails when users explode in number or facilities are sparse. UAVs improve connectivity for ground IoT via high-altitude LoS. Here the UAV and ECs cooperate (aerial-to-ground links), and the joint position + resource + task-split design is highly non-convex.

## System model

- **Actors.** IoT devices (stationary), one UAV, edge clouds (ECs); the UAV and ECs jointly serve devices.
- **Objective.** Minimize the weighted sum of total device service delay and UAV energy ([[energy-latency-tradeoff]]).
- **Decisions.** UAV position, communication + computing resource allocation, task-splitting ([[binary-vs-partial-offloading]] — splitting).

## Method

- Transform the non-convex problem into an approximated convex form and solve efficiently with an **SCA**-based algorithm ([[alternating-optimization-sdr-sca]]).

## Key findings

- Numerical experiments show the collaborative UAV-EC offloading scheme **largely outperforms baselines that rely solely on UAV or solely on ECs** (the paper's stated headline result).

## Limitations / future work

Stationary IoT devices. Future work: multiple UAVs, and task offloading + UAV swarm placement in multihop MEC scenarios.

## Relation to the corpus

A foundational **UAV-EC collaborative offloading** entry, methodologically close to [[zhang-2019-uav-iot-comp-comm]] (SCA + Lagrangian dual single-UAV) and [[liu-2022-miso-uav-mec-trajectory]] (MISO three-stage). Its UAV+EC cooperation theme foreshadows the hierarchical UAV+HAP track. Reinforces [[alternating-optimization-sdr-sca]] and [[energy-latency-tradeoff]].

## Raw artifacts

- `raw/sources/Joint_Task_Offloading_and_Resource_Allocation_in_UAV-Enabled_Mobile_Edge_Computing/Joint_Task_Offloading_and_Resource_Allocation_in_UAV-Enabled_Mobile_Edge_Computing.md`
- Original PDF and extracted figures in the same folder.
