---
type: source
title: "Joint Resource Management for Energy-Efficient UAV-Assisted SWIPT-MEC: A Deep Reinforcement Learning Approach"
authors: ["Yue Chen", "Hui Kang", "Jiahui Li", "Geng Sun", "Boxiong Wang", "Jiacheng Wang", "Cong Liang", "Shuang Liang", "Dusit Niyato"]
year: 2025
url: "https://doi.org/10.1109/JIOT.2025.3574332"
venue: "IEEE Internet of Things Journal (IEEE IoT-J)"
tags: [source, uav-mec, swipt, wireless-power-transfer, soft-actor-critic, energy-efficiency, drl]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[wireless-power-transfer]]"
  - "[[rf-energy-harvesting]]"
  - "[[masac]]"
  - "[[hybrid-action-decision-making]]"
  - "[[uav-charging-scheduling]]"
  - "[[zhu-2025-lycnn-drl-wpt-mec]]"
  - "[[hsu-2025-drl-hues-hap-noma]]"
created: 2026-05-29
updated: 2026-05-29
---

# Joint Resource Management for Energy-Efficient UAV-Assisted SWIPT-MEC: A Deep Reinforcement Learning Approach

## Citation

Chen, Y., Kang, H., Li, J., Sun, G., Wang, B., Wang, J., Liang, C., Liang, S., & Niyato, D. (2025). *Joint Resource Management for Energy-Efficient UAV-Assisted SWIPT-MEC: A Deep Reinforcement Learning Approach*. **IEEE Internet of Things Journal**. DOI: 10.1109/JIOT.2025.3574332.

## TL;DR

A directional-antenna-enhanced UAV that acts as both base station and MEC server, providing **simultaneous wireless information and power transfer (SWIPT)** plus computation to energy-constrained ground IoT terminals in infrastructure-free areas. The paper formulates a **bi-objective** problem (minimize system energy consumption; maximize terminal battery energy) with charging fairness, reformulates it as an MDP with a hybrid solution space, and solves it with an improved **soft actor-critic** (SAC-SK) featuring an action-simplification mechanism plus boundary-penalty and charging-reward designs.

## Problem framing

In remote/disaster areas without ground infrastructure, SWIPT-enabled UAV-MEC must balance UAV energy, terminal battery levels, and compute allocation under limited UAV battery, nonlinear energy-harvesting characteristics, and dynamic task arrivals — competing objectives needing multiple trade-off policies.

## System model

- **UAV roles.** Base station + MEC server with directional antennas; supplies charging ([[wireless-power-transfer]] / [[rf-energy-harvesting]]) and computation offloading to ground terminals.
- **Objective.** Bi-objective: minimize system energy consumption and maximize terminal battery energy, ensuring charging fairness.
- **Reformulation.** MDP with a hybrid (discrete + continuous) solution space.

## Method

- **SAC-SK:** improved soft actor-critic with an **action-simplification mechanism** for convergence/generalization, learning a maximum-entropy policy that schedules offloading decisions and UAV trajectory; **boundary-penalty** and **charging-reward** mechanisms aid learning ([[masac]]/[[hybrid-action-decision-making]]).

## Key findings

- SAC-SK significantly outperforms baselines across multiple metrics and shows robust generalization across diverse scenarios, particularly in complex environments (qualitative; specific curves in the paper).

## Limitations / future work

The authors explicitly note: static ground terminals may not capture real mobility; the energy model ignores signal interference in dense deployments; and although SAC-SK reduces training time/compute, it still has costs. Future work would address these.

## Relation to the corpus

An **energy-efficiency + WPT** entry that complements [[zhu-2025-lycnn-drl-wpt-mec]] (Lyapunov-guided DRL for WPT-MEC) and the energy-harvesting HAP-NOMA scheduling of [[hsu-2025-drl-hues-hap-noma]]. Its hybrid-action SAC connects to the hybrid-action DRL family ([[ma-2025-pdqn-vehicular-mec]], [[liu-2026-jppo-en-convntm]]). Reinforces [[wireless-power-transfer]], [[masac]], and [[uav-charging-scheduling]]. Shares the Geng Sun / Jiahui Li / Dusit Niyato cluster with several aerial sources.

## Raw artifacts

- `raw/sources/Joint_Resource_Management_for_Energy-Efficient_UAV-Assisted_SWIPT-MEC_A_Deep_Reinforcement_Learning_Approach/full.md`
- Original PDF and extracted figures in the same folder.
