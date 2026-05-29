---
type: source
title: "MOALF-UAV-MEC: Adaptive Multiobjective Optimization for UAV-Assisted Mobile Edge Computing in Dynamic IoT Environments"
authors: ["Ali A. AL-Bakhrani", "Mingchu Li", "Mohammad S. Obaidat", "Gehad Abdullah Amran"]
year: 2025
url: "https://doi.org/10.1109/JIOT.2025.3544624"
venue: "IEEE Internet of Things Journal (IEEE IoT-J)"
tags: [source, uav-mec, multi-objective-reinforcement-learning, model-predictive-control, particle-swarm-optimization, lyapunov-optimization, load-balancing]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[multi-objective-reinforcement-learning]]"
  - "[[lyapunov-optimization]]"
  - "[[load-balancing-uav-mec]]"
  - "[[uav-trajectory-control]]"
  - "[[song-2022-emorl-tcto-uav]]"
  - "[[multi-verse-optimizer]]"
created: 2026-05-29
updated: 2026-05-29
---

# MOALF-UAV-MEC: Adaptive Multiobjective Optimization for UAV-Assisted Mobile Edge Computing in Dynamic IoT Environments

## Citation

AL-Bakhrani, A. A., Li, M., Obaidat, M. S., & Amran, G. A. (2025). *MOALF-UAV-MEC: Adaptive Multiobjective Optimization for UAV-Assisted Mobile Edge Computing in Dynamic IoT Environments*. **IEEE Internet of Things Journal**. DOI: 10.1109/JIOT.2025.3544624.

## TL;DR

A **multiobjective adaptive learning framework (MOALF-UAV-MEC)** for UAV-assisted MEC in dynamic IoT environments that integrates four techniques — **multiobjective RL (MORL)**, **model predictive control (MPC)**, **adaptive particle swarm optimization (APSO)**, and **Lyapunov optimization** — to optimize UAV trajectories, dynamic resource allocation, and system stability. A "burst mode" feature gives UAVs temporary performance boosts under high demand.

## Problem framing

IoT proliferation strains network/compute resources. The paper targets several intertwined challenges at once: multiobjective optimization, adaptive resource allocation, energy efficiency, scalability, and QoS guarantees, in environments where demand fluctuates rapidly.

## System model / method

- Integrates **MORL + MPC + APSO + Lyapunov optimization** into one framework.
- **Burst mode:** UAVs temporarily boost performance in high-demand situations.

## Key findings

The paper reports specific figures (treated as the authors' stated results):
- Task completion rate **94.50%**, with an average of **1890 completed tasks per UAV** and **load-balancing efficiency 96%**.
- A **38% reduction in UAV route optimization** and a **55% increase in task completion** during high-load periods.
- Efficiency of **92.8%** at double-scale deployments and **83.5%** at ten-fold scale.

These are the authors' reported numbers; some are figure/abstract-derived and should be read as indicative of claimed performance rather than independently verified.

## Limitations / future work

The extracted conclusion frames contributions but does not enumerate explicit limitations; the heavy integration of four techniques suggests complexity/tuning costs not quantified in the parse.

## Relation to the corpus

A **multiobjective + multi-technique** UAV-MEC entry that, like [[song-2022-emorl-tcto-uav]], combines multi-objective reinforcement learning with UAV trajectory/offloading — but layers in MPC, APSO, and Lyapunov optimization. Connects to [[load-balancing-uav-mec]], [[multi-objective-reinforcement-learning]], and [[lyapunov-optimization]].

## Raw artifacts

- `raw/sources/MOALF-UAV-MEC_Adaptive_Multiobjective_Optimization_for_UAV-Assisted_Mobile_Edge_Computing_in_Dynamic_IoT_Environments/full.md`
- Original PDF and extracted figures in the same folder.
