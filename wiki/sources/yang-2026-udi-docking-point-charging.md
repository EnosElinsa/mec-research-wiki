---
type: source
title: "An Efficient Docking-Point Deployment and Charging Access Coordination Method for Embodied-Enhanced UAV Networks"
authors: ["Wei Yang", "Jiajie Xu", "Jie Chen", "Xiaolong Xu", "Shucun Fu"]
year: 2026
url: "https://doi.org/10.1109/TCCN.2026.3711108"
venue: "IEEE Transactions on Cognitive Communications and Networking, 12"
modeling_card: required
tags: [source, uav-charging, docking-point-deployment, urban-infrastructure, multi-uav-scheduling, convex-relaxation, queueing]
related:
  - "[[uav-charging-scheduling]]"
  - "[[battery-swapping-uav-mec]]"
  - "[[queueing-theory]]"
  - "[[low-altitude-intelligent-network]]"
  - "[[ma-2025-adrl-si-uav-charging-coverage]]"
created: 2026-11-02
updated: 2026-11-02
---

# An Efficient Docking-Point Deployment and Charging Access Coordination Method for Embodied-Enhanced UAV Networks

## Citation

Yang, W., Xu, J., Chen, J., Xu, X., & Fu, S. (2026). *An Efficient Docking-Point Deployment and Charging Access Coordination Method for Embodied-Enhanced UAV Networks*. **IEEE Transactions on Cognitive Communications and Networking, 12**. DOI: 10.1109/TCCN.2026.3711108.

## TL;DR

Instead of building dedicated stations, the paper retrofits existing urban deployable infrastructure (UDI), such as traffic lights, street lamps, and base stations, into charging-capable UAV docking points. HUDD selects a city-scale docking layout, and CRIR assigns UAVs to docking points with convex relaxation and iterative rounding to balance energy and docking-point load under queueing and residual-energy limits.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A 12 km by 12 km city with $K$ candidate UDI nodes, of which $M$ are retrofitted as docking points $d_i$. UAVs $a_j$ issue charging requests during an observation period, fly to a selected docking point, and may queue there. Each UDI has coordinates and a historical load $L_i$.

**Problem & objective**: Problem (18), a constrained multi-objective assignment: $\min_{\chi\in\Omega}\lambda_1\,\mathrm{norm}(\overline E)+\lambda_2\,\mathrm{norm}(\sigma_L)$, the weighted average UAV energy and docking-point load dispersion.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Docking layout | subset of $\mathcal U=\{u_1,\dots,u_K\}$ | $M$ selected UDIs | Infrastructure retrofitted as docking points |
| Access assignment | $z_{j,i}$ | binary | 1 if UAV $a_j$ charges at docking point $d_i$ |
| Schedule | $\chi$ | element of feasible set $\Omega$ | Charging-access schedule for all UAVs |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Weights $\lambda_1+\lambda_2=1$ with $\lambda_1,\lambda_2>0$. |
| C2 | Energy feasibility, $b^{pre}_jE_{\max}\ge E^{fly}_{j,i}+E^{wait}_{j,i}+b^{safe}E_{\max}$. |
| C3 | Each UAV selects at most one docking point, $\sum_i z_{j,i}\le1$; zero means access failure. |

**Algorithm**: HUDD clusters projected UDI coordinates coarsely, refines within regions using geography and historical load, and selects $M$ docking points. CRIR relaxes the binary access variables, solves the convex relaxation, and iteratively rounds to energy-feasible, congestion-aware assignments.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Yang et al. [x] proposed retrofitting existing urban deployable infrastructure, such as traffic lights, street lamps, and communication base stations, as UAV docking points with charging capability for low-altitude urban services. They jointly modeled docking queues, load, and energy consumption and formulated a multi-objective optimization that balances energy consumption and load under residual-energy safety constraints. To address the NP-hard deployment and scheduling subproblems, they proposed a hierarchical UDI-based docking-point deployment algorithm that generates a scalable docking layout and a charging access coordination algorithm based on convex relaxation and iterative rounding. Simulations on realistic urban datasets from Shanghai Telecom show that the method outperforms baseline schemes in energy consumption, response delay, queueing delay, and load distribution. For example, with 200 UAVs it reduces total energy consumption by about 20.3%, 19.5%, and 6.5% relative to three alternative deployment layouts combined with the same access coordination.

## Problem framing

Dedicated charging stations, battery-swap stations, and mobile chargers are costly and coarse in dense cities. Using UDI gives many heterogeneous candidates, so deployment must scale, and shared docking points create queues, so access must avoid congestion and energy exhaustion.

## System model

- 500 UDI candidates sampled from the Shanghai Telecom dataset.
- Charging requests follow the historical traffic distribution.
- Response delay counts flight time to the docking point plus queueing before charging.

## Method

HUDD combines global spatial clustering with load-aware local selection. CRIR solves a continuous relaxation and rounds iteratively; access failure is recorded when no docking point satisfies the safety margin.

## Key findings

- At $N=200$, HUDD-CRIR lowers response delay by about 10.9%, 6.5%, and 1.5% and queueing delay by about 9.17%, 3.75%, and 0.62% relative to Grid, TopK, and RESP layouts.
- On a fixed layout with $M=65$, CRIR reduces total energy by about 11.1%, 8.0%, and 35.3% and response delay by about 23.7%, 12.9%, and 5.8% relative to NR, MOGS, and ML.

## Limitations / future work

The authors plan to handle time-varying and stochastic demand with adaptive online deployment and scheduling under practical communication and airspace constraints.

## Relation to the corpus

A city-scale infrastructure view of [[uav-charging-scheduling]], distinct from station-based [[battery-swapping-uav-mec]] and from the learned station-return policy in [[ma-2025-adrl-si-uav-charging-coverage]].

## Raw artifacts

- Parse: `raw/sources/An_Efficient_Docking-Point_Deployment_and_Charging_Access_Coordination_Method_for_Embodied-Enhanced_UAV_Networks/An_Efficient_Docking-Point_Deployment_and_Charging_Access_Coordination_Method_for_Embodied-Enhanced_UAV_Networks.md`
- Origin PDF and extracted figures are in the same folder.
