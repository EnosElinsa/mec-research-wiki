---
type: source
title: "Distributionally Robust Computation Offloading and Trajectory Optimization in Low-Altitude Wireless Networks"
authors: ["Ziye Jia", "Guanwang Jiang", "Lijun He", "Yian Zhu", "Qihui Wu", "Chau Yuen", "Zhu Han"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3688525"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, low-altitude-wireless-network, distributionally-robust-optimization, uav-hap, task-offloading, trajectory-optimization, benders-decomposition, successive-convex-approximation]
related:
  - "[[distributionally-robust-optimization]]"
  - "[[uav-trajectory-safety-guarantee-ladder]]"
  - "[[robust-offloading]]"
  - "[[low-altitude-intelligent-network]]"
  - "[[high-altitude-platform-station]]"
  - "[[uav-trajectory-control]]"
  - "[[task-offloading]]"
  - "[[jia-2025-dro-uav-hap-mec]]"
  - "[[ziye-jia]]"
  - "[[qihui-wu]]"
  - "[[zhu-han]]"
created: 2026-07-06
updated: 2026-07-16
modeling_card: required
---

# Distributionally Robust Computation Offloading and Trajectory Optimization in Low-Altitude Wireless Networks

## Citation

Jia, Z., Jiang, G., He, L., Zhu, Y., Wu, Q., Yuen, C., & Han, Z. (2026). *Distributionally Robust Computation Offloading and Trajectory Optimization in Low-Altitude Wireless Networks*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2026.3688525.

## TL;DR

Studies a **low-altitude wireless network (LAWN)** where ground users offload tasks to UAVs and a HAP under uncertain task-size distributions. The paper formulates a distributionally robust computation-offloading and trajectory-optimization problem, using uncertainty sets built with L1, L-infinity, and Fortet-Mourier metrics. The proposed DRCOTO algorithm combines outer distributional optimization with Benders decomposition and successive convex approximation for the mixed-integer offloading and UAV-trajectory decisions.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Ground users with uncertain task-size distributions offload data to cruising UAVs for local aerial computation or relay to a hovering HAP.

**Problem & objective**: Jointly choose binary collection, UAV-compute, and HAP-relay decisions with UAV trajectories to minimize worst-case expected total delay, $\min_{x,y,z,q}\max_{\mathbb P_i\in\mathcal D_i}\sum_{i,n}\mathbb E_{\mathbb P_i}[T_{i,n}]$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
| --- | --- | --- | --- |
| GU-UAV collection | $x_{i,j,n}$ | binary | Collect task part $i$ with UAV $j$ in slot $n$ |
| UAV computation | $y_{i,j,n}$ | binary | Compute collected data on UAV $j$ |
| HAP relay | $z_{i,j,n}$ | binary | Relay collected data from UAV $j$ to the HAP |
| UAV trajectory | $q_{j,n}^{u}$ | continuous 3-D positions | UAV position at slot $n$ |
| Ambiguous task distribution | $\mathbb P_i\in\mathcal D_i$ | probability distribution | Worst-case task-size law within the chosen metric ball |

**Constraints**:

| ID | Meaning and key expression |
| --- | --- |
| C1 | Each task part is assigned to at most one collecting UAV and follows a valid local, UAV, or HAP route |
| C2 | UAV positions remain inside the operating area and obey per-slot speed limits |
| C3 | Distinct UAVs maintain the minimum safety distance |
| C4 | Data collection, computation, and relay choices satisfy server capacities and communication feasibility |
| C5 | The worst-case delay objective is evaluated over the declared L1, L-infinity, or Fortet-Mourier ambiguity set |

**Algorithm**: Alternate distributionally robust updates with Benders decomposition, solve continuous offloading and trajectories by SCA, and update the integer master decisions with cuts in the DRCOTO procedure.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Jia et al. [x] coupled UAV trajectory planning with computation offloading for a low-altitude network whose task-size distributions are uncertain. They minimize worst-case expected delay over binary GU collection, UAV computation, HAP relaying, and continuous UAV positions under area, speed, collision, capacity, and distributional ambiguity constraints. DRCOTO combines distributionally robust optimization with Benders decomposition and SCA, separating an integer offloading master from continuous trajectory and resource updates. Across the reported comparisons, its delay approaches branch-and-bound at lower large-scale runtime, while the Fortet-Mourier ambiguity set gives the smallest delay and standard deviation among the tested uncertainty metrics.

## Problem

Low-altitude MEC decisions depend on task sizes that are not known exactly in advance. Optimizing only for a nominal task-size distribution can reduce delay in the average case but degrade badly when the realized distribution shifts. The paper therefore asks how to jointly choose offloading decisions and UAV trajectories while minimizing worst-case expected delay over a distributional ambiguity set.

## System model

- **Architecture.** Multiple UAVs and one HAP serve ground users. A ground user can compute locally, send tasks to a UAV, or have UAV-collected tasks relayed to the HAP.
- **Uncertainty.** Task sizes follow an unknown distribution near a historical reference distribution. The paper constructs ambiguity sets with L1 norm, L-infinity norm, and Fortet-Mourier metrics.
- **Objective.** Minimize worst-case expected delay by jointly optimizing offloading choices and UAV trajectories.

## Method

DRCOTO solves the distributionally robust problem with a layered decomposition. The outer layer searches over the worst-case probability distribution within the ambiguity set. The inner layer handles offloading and trajectory decisions using Benders decomposition for the binary/continuous split and successive convex approximation for nonconvex trajectory structure.

## Key findings

- Optimized UAV trajectories move toward denser ground-user regions, reducing transmission delay in the reported maps.
- Compared with deterministic and stochastic optimization variants, robust optimization is more conservative, while the Fortet-Mourier ambiguity set produces the smallest reported standard deviation and the best stability among the three DRO variants.
- MAPPO can achieve lower delay in some experiments, but the paper notes its extensive offline-training requirement and higher energy consumption.
- Increasing the uncertainty radius increases delay and energy. Among the tested ambiguity sets, Fortet-Mourier has the smallest delay/energy, followed by L1 and then L-infinity.
- In the 15-ground-user / 3-UAV setting, the UAV task quota has a turning point around 5: below that value more tasks must be relayed to the HAP; after that value, marginal delay reduction slows.
- The proposed algorithm is reported close to exact branch-and-bound in delay while having lower running time growth than exact methods and better scalability than several decomposition/metaheuristic baselines.

## Limitations / future work

The conclusion proposes extending the model to adaptive task segmentation and real-time trajectory replanning.

## Relation to the corpus

This is a second DRO anchor for the HAP/UAV low-altitude line after [[jia-2025-dro-uav-hap-mec]], but the uncertainty object changes from CSI-error moments to **task-size distributions**, and the control surface expands to UAV trajectory. It links [[distributionally-robust-optimization]], [[robust-offloading]], [[uav-trajectory-control]], and [[high-altitude-platform-station]] into the low-altitude wireless-network track.

## Comparison boundary

The ladder treats this as distributional robustness of expected computation delay over declared ambiguity sets, not as a collision or flight-safety certificate. See [[uav-trajectory-safety-guarantee-ladder]] for the boundary against bounded-error and intervention-based mechanisms.

## Raw artifacts

- `raw/sources/Distributionally_Robust_Computation_Offloading_and_Trajectory_Optimization_in_Low-Altitude_Wireless_Networks/Distributionally_Robust_Computation_Offloading_and_Trajectory_Optimization_in_Low-Altitude_Wireless_Networks.md`
- Original PDF and extracted figures (`images/`) in the same folder.
