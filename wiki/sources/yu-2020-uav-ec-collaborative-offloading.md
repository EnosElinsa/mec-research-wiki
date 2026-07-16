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
updated: 2026-07-16
---

# Joint Task Offloading and Resource Allocation in UAV-Enabled Mobile Edge Computing

## Citation

Yu, Z., Gong, Y., Gong, S., & Guo, Y. (2020). *Joint Task Offloading and Resource Allocation in UAV-Enabled Mobile Edge Computing*. **IEEE Internet of Things Journal**. DOI: 10.1109/JIOT.2020.2965898.

## TL;DR

A UAV-enabled MEC system where a UAV and edge clouds (ECs) **collaboratively** serve stationary IoT devices in regions where ECs are inaccessible due to terrestrial signal blockage/shadowing. The paper minimizes the weighted sum of all devices' service delay and UAV energy consumption by jointly optimizing UAV position, communication and computing resource allocation, and task-splitting decisions, solving the non-convex problem with **successive convex approximation (SCA)**.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Stationary IoT devices split tasks among local computation, one UAV MEC server, and terrestrial edge clouds that may be blocked from direct access. UAV placement couples ground-to-air communication, UAV-edge-cloud cooperation, computing delay, and aerial energy.

**Problem & objective**: A non-convex joint offloading problem minimizes weighted service delay and UAV energy, $\min \omega_T\sum_k T_k+\omega_E E_{\mathrm U}$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV position | $\mathbf q$ | continuous 3-D position | Aerial MEC deployment |
| Task split | $\alpha_{k,j}$ | continuous, $[0,1]$ | Fraction of device $k$'s task sent to execution tier $j$ |
| Communication allocation | $b_k,p_k$ | continuous, bounded | Bandwidth and power used by device $k$ |
| Computing allocation | $f_{k,j}$ | continuous, nonnegative | CPU resource assigned at UAV or edge cloud $j$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Task fractions sum to one for each device |
| C2 | Radio bandwidth and power allocations stay within budgets |
| C3 | UAV and edge-cloud CPU allocations do not exceed capacity |
| C4 | Local, UAV, and cloud execution and transmission satisfy task timing conditions |
| C5 | UAV placement and energy consumption remain feasible |

**Algorithm**: Express communication, computation, and task-splitting costs in one non-convex program → introduce auxiliary variables and first-order convex lower bounds → solve the resulting convex approximation → update the expansion point → repeat SCA until the delay-energy objective converges.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Yu et al. [x] studied joint task offloading and resource allocation in a UAV-enabled mobile edge computing network where a UAV and terrestrial edge clouds serve stationary IoT devices collaboratively. They formulated a weighted service-delay and UAV-energy minimization problem over UAV placement, task splitting, communication resources, and computing resources. The constraints enforce complete task partitioning, radio and processor capacities, service timing, and UAV operation. Their algorithm replaces non-convex terms with tractable local convex approximations and iterates successive convex optimization. Numerical results show lower weighted cost than the evaluated UAV-only and edge-cloud-only service schemes.

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

- `raw/sources/Joint_Task_Offloading_and_Resource_Allocation_in_UAV-Enabled_Mobile_Edge_Computing/full.md`
- Original PDF and extracted figures in the same folder.
