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
  - "[[miao-2022-gaglpp-drone-swarm-iiot]]"
created: 2026-05-29
updated: 2026-11-03
---

# UAV-Assisted Task Offloading in Edge Computing

## Citation

Zhang, J., Zhang, G., Wang, X., Zhao, X., Yuan, P., & Jin, H. (2024). *UAV-Assisted Task Offloading in Edge Computing*. **IEEE Internet of Things Journal**. DOI: 10.1109/JIOT.2024.3488210.

## TL;DR

A UAV-assisted task-offloading mechanism (**UTOM**) that deploys UAVs as mobile edge servers in complex terrains (forest, desert) to avoid large-scale fixed-server deployment. It minimizes the weighted sum of latency and energy consumption by jointly optimizing resource allocation, offloading decisions, and UAV trajectory, decomposing the non-convex problem into three sub-problems solved by convex optimization (resource), an **improved particle swarm optimization (IPSO)** (offloading), and **DDPG** (trajectory).

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: IoT devices in an infrastructure-poor area offload latency-sensitive tasks to one UAV edge server over $N$ slots. In each slot at most one device offloads, and the UAV position sets the air-to-ground rate.
**Problem & objective**: Problem P1 minimizes the weighted cost $\mathbb C=(1-\omega)\mathcal T+\omega E$ (1) over resource allocation $\Phi=\{p_u^{up},f_u^{uav}\}$, offloading decisions $X$, and UAV trajectory $\Theta$.
**Decision variables**:
| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Offloading decision | $X_u^{uav}(n)$ | binary | IoT device $u$ offloads to the UAV in slot $n$ |
| Device transmit power | $p_u^{up}$ | continuous, $[p_{\min},p_{\max}]$ | Uplink power of device $u$ |
| UAV CPU frequency | $f_u^{uav}$ | continuous, $[f_{\min},f_{\max}]$ | UAV computing for device $u$ |
| UAV trajectory | $\Theta$ | continuous | UAV path over the slots |
**Constraints**:
| ID | Meaning and key expression |
|---|---|
| C1-C2 | At most one device offloads per slot, $\sum_uX_u^{uav}(n)\le1$, with binary $X_u^{uav}(n)$ |
| C3 | Offloaded ratio $0\le\lambda_u(n)\le1$ |
| C4 | Devices and UAV move within the $X\times Y$ area |
| C5 | UAV speed $v_{\min}\le\lVert v(n)\rVert\le v_{\max}$ |
| C6-C7 | Power and CPU ranges $[p_{\min},p_{\max}]$ and $[f_{\min},f_{\max}]$ |
| C8 (2) | Offloaded tasks finish within the slot, $X_u^{uav}(n)(t_u^{trans}(n)+t_u^{uav}(n))\le\delta$ |
**Algorithm**: UTOM decomposes P1: for fixed offloading and position, resource allocation P2-P3 is solved by Lagrange multipliers and KKT conditions in closed form; improved particle swarm optimization selects offloading decisions; and DDPG controls the UAV trajectory.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zhang et al. [x] studied UAV-assisted task offloading in edge computing for infrastructure-poor environments. They formulated weighted latency and energy minimization over resource allocation, task-offloading decisions, and UAV trajectory under single-offload, offloading-ratio, area, speed, power, CPU, and slot-latency constraints. UTOM solves the resource block through Lagrange multipliers and KKT conditions. Improved particle swarm optimization selects offloading decisions, and DDPG controls the UAV trajectory. Simulations report about 14.23% and 6% lower cost than DQN and OTDDPG, better convergence than DQN, AC, and OTDDPG, and gains of IPSO over PSO.

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

- `raw/sources/UAV-Assisted_Task_Offloading_in_Edge_Computing/UAV-Assisted_Task_Offloading_in_Edge_Computing.md`
- Original PDF and extracted figures in the same folder.
