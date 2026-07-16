---
type: source
modeling_card: required
title: "UAV-Assisted Task Offloading in Edge Computing"
authors: ["Junna Zhang", "Guoxian Zhang", "Xinxin Wang", "Xiaoyan Zhao", "Peiyan Yuan", "Hu Jin"]
year: 2024
url: "https://doi.org/10.1109/JIOT.2024.3488210"
venue: "IEEE Internet of Things Journal (IEEE IoT-J)"
tags: [source, uav-mec, task-offloading, resource-allocation, particle-swarm-optimization, ddpg, trajectory-optimization]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[uav-trajectory-control]]"
  - "[[ddpg]]"
  - "[[particle-swarm-optimization]]"
  - "[[energy-latency-tradeoff]]"
  - "[[binary-vs-partial-offloading]]"
  - "[[zhang-2019-uav-iot-comp-comm]]"
  - "[[yu-2020-uav-ec-collaborative-offloading]]"
created: 2026-05-29
updated: 2026-07-16
---

# UAV-Assisted Task Offloading in Edge Computing

## Citation

Zhang, J., Zhang, G., Wang, X., Zhao, X., Yuan, P., & Jin, H. (2024). *UAV-Assisted Task Offloading in Edge Computing*. **IEEE Internet of Things Journal**. DOI: 10.1109/JIOT.2024.3488210.

## TL;DR

A UAV-assisted task-offloading mechanism (**UTOM**) that deploys UAVs as mobile edge servers in complex terrains (forest, desert) to avoid large-scale fixed-server deployment. It minimizes the weighted sum of latency and energy consumption by jointly optimizing resource allocation, offloading decisions, and UAV trajectory, decomposing the non-convex problem into three sub-problems solved by convex optimization (resource), an **improved particle swarm optimization (IPSO)** (offloading), and **DDPG** (trajectory).

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: IoT devices in infrastructure-poor terrain offload tasks to a UAV mobile edge server. UAV position affects air-to-ground rates, while execution choice and resource allocation determine device and UAV delay and energy.

**Problem & objective**: UTOM solves a non-convex joint problem minimizing weighted latency and energy, $\min \omega_T T_{\mathrm{tot}}+\omega_E E_{\mathrm{tot}}$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Offloading decision | $x_k$ | binary | Local or UAV execution for task $k$ |
| Computing allocation | $f_k$ | continuous, nonnegative | UAV CPU assigned to task $k$ |
| Communication resource | $b_k,p_k$ | continuous, bounded | Bandwidth and power for offloading |
| UAV trajectory | $\mathbf q(t)$ | continuous position | Mobile edge-server path |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Each task selects one execution mode |
| C2 | Communication and computation allocations remain within capacity |
| C3 | Task transmission and execution meet latency requirements |
| C4 | Device and UAV energy budgets are respected |
| C5 | UAV trajectory satisfies region and mobility limits |

**Algorithm**: Fix offloading and trajectory and solve resource allocation by Lagrange/KKT conditions → update binary offloading with improved particle swarm optimization → update UAV trajectory with DDPG → evaluate the joint delay-energy cost → alternate the three subproblems.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zhang et al. [x] studied UAV-assisted task offloading in edge computing for infrastructure-poor environments. They formulated weighted latency and energy minimization over resource allocation, task-offloading decisions, and UAV trajectory under execution, resource, delay, energy, and mobility constraints. UTOM solves the resource block through Lagrange multipliers and KKT conditions. Improved particle swarm optimization selects offloading decisions, and DDPG controls the UAV trajectory. Simulations report lower weighted latency-energy cost than the evaluated offloading and trajectory baselines.

## Problem framing

Task offloading frees resource-constrained IoT devices, but fixed base-station edge servers have limited range and high deployment cost. UAVs as mobile edge servers cover complex terrains; the joint resource + offloading + trajectory design is non-convex.

## System model

- **Actors.** UAV(s) as mobile edge servers; IoT devices offloading tasks.
- **Objective.** Minimize weighted sum of latency + energy consumption ([[energy-latency-tradeoff]]).
- **Decisions.** Resource allocation, offloading decision, UAV trajectory.

## Method

- Decompose into three sub-problems:
  1. **Resource allocation:** Lagrange multiplier method + KKT conditions (convex).
  2. **Offloading decision:** improved particle swarm optimization (IPSO) ([[particle-swarm-optimization]]).
  3. **UAV trajectory:** **DDPG** ([[ddpg]]).

## Key findings

- Simulation experiments show UTOM efficiently reduces the weighted sum of latency and energy consumption (qualitative; specific curves in the paper).

## Limitations / future work

The authors flag: extend to **multi-UAV** systems for many IoT devices (a single UAV may not meet demand), and jointly use UAVs + edge servers to improve overall performance.

## Relation to the corpus

A **hybrid convex + IPSO + DDPG** single-UAV offloading entry that combines classical optimization, swarm optimization, and DRL across decomposed sub-problems — a methodological middle ground between the pure-optimization [[zhang-2019-uav-iot-comp-comm]] / [[yu-2020-uav-ec-collaborative-offloading]] and the pure-DRL multi-UAV works. Reinforces [[ddpg]], [[particle-swarm-optimization]], and [[uav-trajectory-control]].

## Raw artifacts

- `raw/sources/UAV-Assisted_Task_Offloading_in_Edge_Computing/full.md`
- Original PDF and extracted figures in the same folder.
