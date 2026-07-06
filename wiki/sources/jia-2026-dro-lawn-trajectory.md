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
updated: 2026-07-06
---

# Distributionally Robust Computation Offloading and Trajectory Optimization in Low-Altitude Wireless Networks

## Citation

Jia, Z., Jiang, G., He, L., Zhu, Y., Wu, Q., Yuen, C., & Han, Z. (2026). *Distributionally Robust Computation Offloading and Trajectory Optimization in Low-Altitude Wireless Networks*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2026.3688525.

## TL;DR

Studies a **low-altitude wireless network (LAWN)** where ground users offload tasks to UAVs and a HAP under uncertain task-size distributions. The paper formulates a distributionally robust computation-offloading and trajectory-optimization problem, using uncertainty sets built with L1, L-infinity, and Fortet-Mourier metrics. The proposed DRCOTO algorithm combines outer distributional optimization with Benders decomposition and successive convex approximation for the mixed-integer offloading and UAV-trajectory decisions.

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

## Raw artifacts

- `raw/sources/Distributionally Robust Computation Offloading and Trajectory Optimization in Low-Altitude Wireless Networks/Distributionally Robust Computation Offloading and Trajectory Optimization in Low-Altitude Wireless Networks.md`
- Original PDF and extracted figures (`images/`) in the same folder.
