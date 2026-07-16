---
type: source
title: "Energy- and Latency-Efficient Resource Allocation for RIS-Assisted UAV-USV Cooperative MEC Network"
authors: ["Yangzhe Liao", "Lin Liu", "Yong Ma"]
year: 2025
url: "https://doi.org/10.1109/TGCN.2025.3545458"
venue: "IEEE Transactions on Green Communications and Networking"
modeling_card: required
tags: [source, maritime-mec, uav-usv, ris, resource-allocation, energy-latency-tradeoff, bidirectional-task, differential-evolution]
related:
  - "[[uav-usv-cooperative-mec]]"
  - "[[maritime-mec]]"
  - "[[intelligent-reflecting-surface]]"
  - "[[uav-mounted-ris]]"
  - "[[differential-evolution]]"
  - "[[matching-theory-for-resource-allocation]]"
  - "[[li-2026-cdto-inland-waterways]]"
  - "[[zeng-2024-usv-fleet-collaborative-offloading]]"
created: 2026-07-07
updated: 2026-07-16
---

# Energy- and Latency-Efficient Resource Allocation for RIS-Assisted UAV-USV Cooperative MEC Network

## Citation

Liao, Y., Liu, L., & Ma, Y. (2025). *Energy- and Latency-Efficient Resource Allocation for RIS-Assisted UAV-USV Cooperative MEC Network*. **IEEE Transactions on Green Communications and Networking**. DOI: 10.1109/TGCN.2025.3545458.

## TL;DR

Introduces a RIS-assisted [[uav-usv-cooperative-mec|UAV-USV cooperative MEC]] architecture for inland waterway communications where USVs have bidirectional tasks with hard time windows. The objective is a weighted sum of UAV energy consumption and USV task-execution latency. The proposed heuristic decomposes the problem into route selection, task-mode/arrival-time selection, and hovering-coordinate/RIS-phase design, solved with enhanced grey wolf optimization (EGWO), integer-constrained-removed augmented Lagrangian (ICRAL), and multi-objective differential evolution (MODE).

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Rotary-wing UAVs carrying passive RIS elements follow a fly-hover-serve pattern to support inland-waterway USVs whose bidirectional tasks combine locally generated input with remote data from a terrestrial base station. Each task must choose local or MEC execution and finish inside a hard service window.

**Problem & objective**: The controller solves $\min_{\boldsymbol\alpha,\boldsymbol\beta,\boldsymbol\tau,\mathbf s,\boldsymbol\theta}F$, where $F=\sum_{j,i,l}\beta_{l,(j,i)}\left(E_{l,(j,i)}^{\mathrm{flight}}+\lambda t_{l,(j,i)}^{\mathrm{total}}\right)$ balances UAV flight energy and task-execution latency.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Task execution mode | $\alpha_i$ | binary | Local USV execution or MEC execution |
| UAV route indicator | $\beta_{l,(j,i)}$ | binary | Whether UAV $l$ flies from service point $j$ to $i$ |
| UAV arrival time | $\tau_{l,i}$ | continuous | Arrival time of UAV $l$ at USV $i$ |
| Hovering coordinate | $\mathbf s_i$ | continuous 3-D coordinate | RIS-UAV service location for USV $i$ |
| RIS phase vector | $\boldsymbol\theta_l$ | continuous phases in $[0,2\pi]$ | Reflection phases used by UAV $l$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Every task selects exactly one of the two execution modes |
| C2 | Route indicators are binary and every UAV leaves and returns to the charging platform |
| C3 | Route-flow conservation holds and each USV is served by exactly one UAV |
| C4 | A UAV cannot begin service before the task's earliest time $X_i$ |
| C5 | Flight, waiting, transmission, and execution finish no later than deadline $Y_i$ |
| C6 | Each RIS element uses a feasible full-reflection phase in $[0,2\pi]$ |

**Algorithm**: The heuristic alternates three coupled solvers at the MEC server. Enhanced grey wolf optimization selects multi-UAV routes, ICRAL relaxes and repairs the execution-mode and arrival-time block, and multi-objective differential evolution updates hovering coordinates and RIS phases while retaining nondominated candidates.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Liao et al. [x] studied RIS-assisted UAV service for inland-waterway USVs with bidirectional tasks and hard time windows. They minimized a weighted sum of UAV flight energy and task latency over execution modes, service routes, arrival times, hovering coordinates, and RIS phases under routing and deadline constraints. Their heuristic couples enhanced grey wolf optimization, an integer-constraint-removed augmented Lagrangian method, and multi-objective differential evolution across the three decision blocks. Simulations reported up to about 46% lower cumulative cost than selected advanced algorithms, with additional reductions as more UAVs or RIS elements were available.

## Problem framing

USV tasks can involve both locally generated data and remotely generated data from the Internet/TBS. That bidirectional data model makes one-way offloading insufficient: the system must decide whether USVs execute locally after receiving remote data or send local data to a terrestrial MEC server, while UAVs with RIS elements provide blocked uplink and downlink paths. The paper optimizes energy-latency tradeoffs under hard service-time windows.

## System model

- A TBS, a set of rotary-wing UAVs, and multiple USVs in an inland-waterway MEC scenario.
- Direct TBS-USV links are severely blocked; UAV-mounted RIS elements assist both downlink and uplink transmissions.
- UAVs follow a fly-hover-serve scheme and dynamically form virtual clusters with the TBS.
- Each USV bidirectional task includes local data, remote input data, required CPU cycles, and a hard time window.
- A task is executed either locally at the USV after remote-data reception or at the MEC server after local-data uplink via RIS-assisted UAV paths.

## Method

The paper decomposes the NP-hard problem into three coupled subproblems:

- **UAV flight-route indicators:** solved by the proposed EGWO algorithm, derived from grey wolf optimization for multi-UAV route selection with time windows.
- **USV task execution mode and UAV arrival time:** solved by the ICRAL algorithm after removing the integer constraint in an augmented-Lagrangian formulation.
- **UAV hovering coordinates and RIS phase shift:** solved with MODE, a multi-objective differential-evolution algorithm.

The full heuristic is implemented at the MEC server and iterates the three subproblem solvers.

## Key findings

- The proposed solution lowers the UAV cumulative cost compared with selected advanced algorithms across different USV counts.
- Increasing the number of RIS reflecting elements reduces cumulative cost because stronger RIS-assisted links reduce transmission time.
- Increasing the number of UAVs reduces cumulative cost by shortening flight routes and service waiting.
- The conclusion reports up to approximately 46% cumulative-cost reduction compared with selected advanced algorithms.

## Limitations / future work

The method is a heuristic for an NP-hard problem; it does not prove global optimality. The paper is simulation-based and assumes a central controller/MEC server with network-state information. The parse does not spell out a concrete future-work list beyond the conclusion heading.

## Relation to the corpus

This source strengthens the maritime track by adding a RIS-assisted UAV-USV cooperative architecture with explicit bidirectional tasks and hard time windows. It complements [[li-2026-cdto-inland-waterways]], where USVs form D2D computation-sharing clusters under UAV cluster heads, and [[zeng-2024-usv-fleet-collaborative-offloading]], where UAVs incentivize USV fleets to compute via reverse auction.

## Raw artifacts

- Parse: `raw/sources/Energy- and Latency-Efficient Resource Allocation for RIS-Assisted UAV-USV Cooperative MEC Network/Energy- and Latency-Efficient Resource Allocation for RIS-Assisted UAV-USV Cooperative MEC Network.md`
- Origin PDF: `raw/sources/Energy- and Latency-Efficient Resource Allocation for RIS-Assisted UAV-USV Cooperative MEC Network/Energy- and Latency-Efficient Resource Allocation for RIS-Assisted UAV-USV Cooperative MEC Network.pdf`
- Figures: `raw/sources/Energy- and Latency-Efficient Resource Allocation for RIS-Assisted UAV-USV Cooperative MEC Network/images/`
