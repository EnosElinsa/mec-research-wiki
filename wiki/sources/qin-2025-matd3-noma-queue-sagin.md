---
type: source
title: "Learning-Based NOMA-Enabled Queue-Aware Task Offloading and AAV 3D Trajectory Planning for SAGIN"
authors: ["Peng Qin", "Hongjie Li", "Yang Fu", "Jinhui Hu", "Xue Wu", "Xianchao Zhang"]
year: 2025
url: "https://doi.org/10.1109/TVT.2025.3552807"
venue: "IEEE Transactions on Vehicular Technology (IEEE TVT)"
tags: [source, space-air-ground-integrated-network, noma, task-offloading, aav-trajectory, multi-agent-td3, lyapunov-optimization]
related:
  - "[[space-air-ground-integrated-network]]"
  - "[[noma]]"
  - "[[multi-agent-td3]]"
  - "[[lyapunov-optimization]]"
  - "[[uav-trajectory-control]]"
  - "[[wang-2024-hybrid-oma-noma-sagin]]"
  - "[[hsu-2025-drl-hues-hap-noma]]"
  - "[[fu-2025-otae-inference-lae-batching]]"
created: 2026-05-29
updated: 2026-05-29
---

# Learning-Based NOMA-Enabled Queue-Aware Task Offloading and AAV 3D Trajectory Planning for SAGIN

## Citation

Qin, P., Li, H., Fu, Y., Hu, J., Wu, X., & Zhang, X. (2025). *Learning-Based NOMA-Enabled Queue-Aware Task Offloading and AAV 3D Trajectory Planning for SAGIN*. **IEEE Transactions on Vehicular Technology**. DOI: 10.1109/TVT.2025.3552807.

## TL;DR

A hierarchical **SAGIN** where AAVs provide access and satellites provide backhaul; **NOMA** reuses channels to raise spectrum utilization and throughput. The paper jointly plans AAV 3D trajectory, task offloading, task assignment, and computing-resource allocation to minimize system cost. Because queue-delay constraints couple with decisions, **Lyapunov optimization** splits the problem into three sub-problems solved by MTDTO, a CVX-based method, and GSCRA. The DRL backbone is **MATD3** (per the index terms).

## Problem framing

SAGIN serves users lacking ground base stations: AAVs give massive access, satellites give backhaul. NOMA improves channel reuse, but different AAV trajectories and task assignments yield different delay/energy; queue dynamics add high dynamicity, demanding a queue-aware, learning-based solution.

## System model

- **Hierarchy.** AAVs (access) + satellites (backhaul) cooperatively process offloaded tasks.
- **NOMA.** Channel reuse for spectrum efficiency/throughput.
- **Coupling.** Queue-delay constraints couple with decision-making → handled by [[lyapunov-optimization]].

## Method

- Lyapunov optimization splits into three sub-problems addressed by **MTDTO**, a **CVX-based** method, and **GSCRA** to minimize system cost; trajectory/offloading learning uses **MATD3** ([[multi-agent-td3]]).

## Key findings

- Simulation outcomes show the advantages of the method over baselines (qualitative; specific cost curves in the paper).

## Limitations / future work

Future work: integrate cache resources into the SAGIN network for more efficient service.

## Relation to the corpus

A **NOMA + SAGIN + DRL** entry that pairs with [[wang-2024-hybrid-oma-noma-sagin]] (hybrid OMA/NOMA mode selection) and the HAP-NOMA energy-harvesting scheduler [[hsu-2025-drl-hues-hap-noma]]. Its Lyapunov-decomposition + MATD3 echoes the queue-aware Lyapunov pattern in [[you-2025-uncertain-maritime-hasac]]. Shares authors Peng Qin / Yang Fu with the low-altitude edge-inference paper [[fu-2025-otae-inference-lae-batching]]. Reinforces [[noma]] and [[space-air-ground-integrated-network]].

## Raw artifacts

- `raw/sources/Learning-Based_NOMA-Enabled_Queue-Aware_Task_Offloading_and_AAV_3D_Trajectory_Planning_for_SAGIN/full.md`
- Original PDF and extracted figures in the same folder.
