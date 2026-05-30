---
type: source
title: "Delay-Aware Cooperative Task Offloading for Multi-UAV Enabled Edge-Cloud Computing"
authors: ["Zhuoyi Bai", "Yifan Lin", "Yang Cao", "Wei Wang"]
year: 2024
url: "https://doi.org/10.1109/TMC.2022.3232375"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, uav-mec, task-offloading, lyapunov-optimization, edge-cloud, load-balancing-uav-mec, post-disaster-mec]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[lyapunov-optimization]]"
  - "[[task-offloading]]"
  - "[[three-tier-cloud-edge-end]]"
  - "[[load-balancing-uav-mec]]"
  - "[[parallel-vs-serial-processing]]"
  - "[[post-disaster-mec]]"
  - "[[yang-2022-stochastic-uav-mec-lyapunov]]"
  - "[[zhu-2025-lycnn-drl-wpt-mec]]"
created: 2026-05-31
updated: 2026-05-31
---

# Delay-Aware Cooperative Task Offloading for Multi-UAV Enabled Edge-Cloud Computing

## Citation

Bai, Z., Lin, Y., Cao, Y., & Wang, W. (2024). *Delay-Aware Cooperative Task Offloading for Multi-UAV Enabled Edge-Cloud Computing*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2022.3232375. (Date of publication 27 December 2022; date of current version 8 January 2024.)

## TL;DR

In weak-infrastructure / post-disaster scenarios, multiple UAVs form an on-site edge cluster and cooperate with a **remote cloud** (via multi-hop UAV relay → ground base station → wired link) to handle real-time tasks. Because tasks are unevenly distributed across UAVs, the most task-heavy UAV bottlenecks the system. The paper formulates a **delay-minimization** problem over **cooperative task offloading** that models network congestion, the air-to-ground channel, and **cooperative parallel computing** (completion delay depends on the slowest edge node). It is non-convex, so **convex approximation** makes it tractable and **Lyapunov optimization** makes the online per-slot offloading decisions. The models are verified on a real UAV-edge platform, and data-driven simulations show near-optimal delay.

## Problem framing

Single-UAV edge computing has limited compute; extending to multiple UAVs plus a cloud forms a multi-UAV edge-cloud system. But UAV compute/load is unevenly distributed, so load balancing is needed. Introducing UAVs adds challenges over ground edge-cloud systems: (i) ubiquitous network congestion when UAVs stream data; (ii) air-to-ground wireless backhaul differs from ground links; (iii) when UAVs cooperate on one mission, the completion-delay model must account for the **slowest** node ([[parallel-vs-serial-processing]]); (iv) strict energy constraints since recharging mid-mission is hard. The authors state this is the **first** use of online task offloading to minimize total service delay in a multi-UAV edge-cloud framework.

## System model

- **Tiers.** UAV on-site edge cluster + remote cloud ([[three-tier-cloud-edge-end]]-style edge-cloud), connected via multi-hop UAV relay → BS → wired link ([[multi-uav-assisted-mec]]).
- **Cooperation.** UAVs with spare capacity take workload from overloaded UAVs ([[load-balancing-uav-mec]]); overflow goes to the cloud.
- **Realistic modeling.** Network congestion, accurate air-to-ground channel, cooperative parallel computing, virtualization-based resource reservation, and stochastic task arrivals.
- **Objective.** Minimize total/service completion delay under energy constraints.

## Method

- **Convex approximation** to make the non-convex problem tractable.
- **Lyapunov optimization** ([[lyapunov-optimization]]) for **online** delay-optimal task-offloading decisions, with mathematical proofs.
- **Platform-guided modeling:** a real-world UAV-enabled edge-computing platform is built to verify model correctness; measurements + real-world datasets drive the simulations.

## Key findings

- The proposed algorithm reaches **near-optimal performance on system delay** (parse contributions + Section 5).
- Real-platform measurements **corroborate the model's correctness**, and data-driven simulations on real-world datasets confirm the algorithm fully utilizes available energy to significantly reduce task completion delay (parse abstract).

## Limitations / future work

Simulation + platform-measurement-driven (not a full field deployment of the algorithm); the parse does not enumerate explicit limitations beyond the modeled assumptions and energy constraints.

## Relation to the corpus

A **Lyapunov-based online optimization** treatment of multi-UAV **edge-cloud** cooperation whose distinguishing feature is the **cooperative-parallel-computing delay model** (slowest-node bottleneck) and explicit load balancing — complementing [[yang-2022-stochastic-uav-mec-lyapunov]]'s stochastic UAV-MEC Lyapunov approach and the Lyapunov-guided DRL of [[zhu-2025-lycnn-drl-wpt-mec]] / [[qin-2025-bcuav-masac]]. Its model verification on a real UAV-edge platform is relatively rare in the corpus (most sources are simulation-only). Reinforces [[load-balancing-uav-mec]] and [[parallel-vs-serial-processing]].

## Raw artifacts

- `raw/sources/Delay-Aware_Cooperative_Task_Offloading_for_Multi-UAV_Enabled_Edge-Cloud_Computing/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
