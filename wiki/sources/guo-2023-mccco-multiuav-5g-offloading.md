---
type: source
title: "Multi-UAV Cooperative Task Offloading and Resource Allocation in 5G Advanced and Beyond"
authors: ["Hongzhi Guo", "Yutao Wang", "Jiajia Liu", "Chang Liu"]
year: 2023
url: "https://doi.org/10.1109/TWC.2023.3277801"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, multi-uav-assisted-mec, task-offloading, resource-allocation, partial-offloading, software-defined-networking, load-balancing]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[interdependent-tasks-dag]]"
  - "[[binary-vs-partial-offloading]]"
  - "[[load-balancing-uav-mec]]"
  - "[[network-slicing]]"
  - "[[hao-2024-clp-multiuav-priority-offloading]]"
  - "[[huang-2023-mu-aec-task-energy]]"
created: 2026-05-29
updated: 2026-11-03
modeling_card: required
---

# Multi-UAV Cooperative Task Offloading and Resource Allocation in 5G Advanced and Beyond

## Citation

Guo, H., Wang, Y., Liu, J., & Liu, C. (2023). *Multi-UAV Cooperative Task Offloading and Resource Allocation in 5G Advanced and Beyond*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2023.3277801.

## TL;DR

A **software-defined-networking-enhanced cooperative multiple-UAV-enabled aerial computing (MUEAC)** system. Cooperation among UAVs overcomes single-UAV limits (small coverage, scarce resources) and balances load; for divisible, data-dependent tasks, **partial offloading** makes scheduling more flexible than binary. The authors minimize the processing delay of divisible tasks under task-data-dependency and UAV-energy constraints, proposing the **MCCCO** (multi-UAV cooperative communication and computing optimization) scheme.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Ground devices generate interdependent subtask flows that can be partially offloaded to cooperating UAVs through aerial links and ground D2D relays.

**Problem & objective**: Problem P1 jointly chooses subtask placement and D2D association to minimize total processing delay, $T=\min_{X,Y}\sum_{i=1}^{n}t(w(i))$; UAV energy enters only through the thresholds in C5 and C6.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
| --- | --- | --- | --- |
| Subtask offloading | $x_{w(i),s(j)}^{v}$ | binary | Assign subtask $s(j)$ of flow $w(i)$ to UAV $v$ |
| D2D association | $y_{w(i)}^{k}$ | binary | Select the ground relay or associated device for flow $w(i)$ |
| Offloading strategy | $X$ | binary decision matrix | Collection of subtask-to-UAV assignments |
| Association strategy | $Y$ | binary decision matrix | Collection of ground D2D associations |

**Constraints**:

| ID | Meaning and key expression |
| --- | --- |
| C1 | Subtask offloading is binary, $x_{w(i),s(j)}^{v}\in\{0,1\}$ |
| C2 | Ground D2D association is binary, $y_{w(i)}^{k}\in\{0,1\}$, $k\in N_v$ |
| C3 | Each subtask runs on exactly one computing UAV, $\sum_{v=1}^{\lvert V\rvert}x_{w(i),s(j)}^{v}=1$ |
| C4 | A device transmits its task to exactly one device covered by the same UAV, $\sum_{k\in A[i]}y_{w(i)}^{k}=1$ |
| C5 | UAV manager energy, $e^{M}\leq e_0$ |
| C6 | Computing-UAV energy, $e_v^{\mathcal C}\leq e_0$ for all $v\in V$ |
| C7 | G2A distance, $d_{k,v}\leq R_{G2A}$ |
| C8 | D2D distance, $d_{k,k'}\leq R_{D2D}$ |

**Algorithm**: Decompose delay into D2D uplink and aerial offloading terms, solve the association subproblem with a near-optimal convex relaxation, and update task placement with a two-layer game-theoretic approximation until the offloading decisions stabilize.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Guo et al. [x] studied cooperative multi-UAV execution of interdependent subtask flows with ground D2D relaying and aerial communication. They minimized total processing delay over binary ground-device association and subtask-to-UAV placement under unique-assignment, coverage-range, and UAV energy constraints. MCCCO relaxes the D2D association for CVX and applies a two-layer game to update subtask and flow offloading decisions until a Nash equilibrium is reached. In small-scale tests, MCCCO reached near-optimal delay compared with the enumeration method at lower running time, with slightly higher UAV energy from A2A cooperation; it also gave lower delay than RDOA and than MCCCO without multi-UAV cooperation or without ground D2D association, while using less than 5% more energy than RDOA.

## Problem framing

5G-Advanced/beyond IoT apps (autonomous driving, face detection) are compute-intensive and latency-sensitive; remote areas lack terrestrial infrastructure. Single UAV-enabled aerial computing (SUEAC) is limited, so multiple UAVs (MUEAC) cooperate to use resources fully and balance load. Divisible tasks with data dependencies favor partial offloading.

## System model

- **Actors.** Multiple cooperating UAVs (SDN-enhanced) serving ground devices; models D2D communication, A2A communication, and task interdependency, with a detailed task-execution process from ground devices to UAVs ([[interdependent-tasks-dag]]).
- **Objective.** Minimize task processing delay under task-data-dependency and UAV-energy constraints; achieve load balancing on UAV energy.
- **Offloading.** Partial ([[binary-vs-partial-offloading]]).

## Method

- **MCCCO** scheme optimizing the ground D2D association strategy and computation-task offloading strategy to minimize processing delay and balance UAV energy load.

## Key findings

- Experiments show MCCCO achieves better task-processing-delay reduction and load balancing on UAV energy than traditional multi-UAV schemes (qualitative; specific curves in the paper).

## Limitations / future work

The parse's conclusion does not enumerate explicit future work beyond the established scheme.

## Relation to the corpus

A **cooperative multi-UAV partial-offloading** entry emphasizing task interdependency (DAG) and load balancing, complementing the priority-aware cooperative work [[hao-2024-clp-multiuav-priority-offloading]] and the energy-balancing multi-objective study [[huang-2023-mu-aec-task-energy]]. Reinforces [[interdependent-tasks-dag]], [[binary-vs-partial-offloading]], and [[load-balancing-uav-mec]]; introduces [[network-slicing]]/SDN-enhanced framing.

## Raw artifacts

- `raw/sources/Multi-UAV_Cooperative_Task_Offloading_and_Resource_Allocation_in_5G_Advanced_and_Beyond/Multi-UAV_Cooperative_Task_Offloading_and_Resource_Allocation_in_5G_Advanced_and_Beyond.md`
- Original PDF and extracted figures in the same folder.
