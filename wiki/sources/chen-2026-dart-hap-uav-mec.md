---
type: source
title: "DDPG-Attention-based Resource Allocation and Trajectory Optimization in Hierarchical MEC"
authors: ["Ying Chen", "Zhihao Hu", "Zhuoyue Chen", "Jiwei Huang", "Lian Zhao"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3676417"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, hierarchical-aerial-mec, hap, uav-mec, noma, wireless-power-transfer, lyapunov-optimization, ddpg, attention, fairness]
related: ["[[hierarchical-aerial-mec]]", "[[high-altitude-platform-station]]", "[[noma]]", "[[wireless-power-transfer]]", "[[lyapunov-optimization]]", "[[ddpg]]", "[[fairness-metrics-in-mec]]", "[[uav-trajectory-control]]", "[[chen-2023-dotora-air-ground-online]]", "[[jia-2025-dro-uav-hap-mec]]", "[[hsu-2025-drl-hues-hap-noma]]", "[[kang-2023-mappo-hierarchical-aerial]]"]
created: 2026-07-06
updated: 2026-07-06
---

# DDPG-Attention-based Resource Allocation and Trajectory Optimization in Hierarchical MEC

## Citation

Chen, Y., Hu, Z., Chen, Z., Huang, J., & Zhao, L. (2026). *DDPG-Attention-based Resource Allocation and Trajectory Optimization in Hierarchical MEC*. **IEEE Transactions on Mobile Computing**, 1-17. DOI: 10.1109/TMC.2026.3676417.

## TL;DR

A HAP-UAV-MEC system where IoT devices can compute locally, offload to a UAV, or reach a HAP through the UAV; the UAV can compute tasks itself or forward overflow to the HAP. The system uses NOMA for many IoT uplinks and WPT from the HAP to support the UAV's energy queue. DART combines Lyapunov optimization with DDPG plus attention: Lyapunov turns the multi-stage MINLP into per-slot deterministic subproblems, DDPG-attention handles coupled trajectory / offloading decisions, and convex optimization handles resource allocation.

## Problem

Ground-only MEC can fail in complex terrain or disasters, while UAV-only MEC is battery- and compute-limited. HAPs add stable upper-tier compute, but the resulting HAP-UAV-IoT system couples trajectory, NOMA access, task queues, energy queues, offloading, WPT, fairness, and compute / communication resource allocation. The objective is to minimize IoT-device and UAV energy cost while maintaining queue stability and service performance.

## System model

- **Tiers:** multiple IoT devices, one UAV with compute / task / energy queues, and one HAP with high-performance compute and stable energy.
- **Offloading:** IoT tasks can be local or offloaded to the UAV; the UAV can execute tasks or offload remaining work to the HAP.
- **Communications:** NOMA with SIC for IoT-UAV access; UAV-HAP channel includes LoS / NLoS considerations.
- **Energy:** HAP WPT supplies UAV energy; the objective counts IoT and UAV energy cost, while HAP energy is treated as sufficient.
- **Fairness:** a service-count-based fairness constraint encourages the UAV to serve IoT devices more evenly rather than staying near a subset.

## Method

DART defines a Lyapunov drift-plus-penalty upper bound and decomposes the original multi-stage MINLP into four parallel subproblems. The most coupled subproblem - UAV trajectory and offloading decisions - is solved with DDPG-A, a DDPG variant using an attention mechanism over state features. The resource-allocation subproblems are solved by convex optimization or analytical methods.

## Key findings

- The experiments report that DART reduces total cost while keeping queue behavior stable across task-arrival rates.
- The fairness constraint matters: without it, the UAV tends to favor a subset of IoT devices, leading to longer queues and higher energy costs in the reported comparison.
- DART outperforms Random, DQN, DDPG, and the listed trajectory/offloading baselines in energy cost and queue performance; the attention-enhanced DDPG is slightly better than plain DDPG in the reported figures.
- A small-scale exhaustive-search comparison using the Melbourne CBD IoT-device dataset shows DART near the optimal queue and energy-cost behavior in the reported setting.

## Limitations / future work

The evaluation is simulation-based. The paper models one UAV and one HAP; multi-UAV collaborative MEC is named as future work. Imperfect CSI and MIMO extensions are also left outside the reported formulation. The HAP has sufficient energy and the WPT link is modeled rather than experimentally validated.

## Relation to the corpus

This strengthens the [[hierarchical-aerial-mec]] track by combining UAV+HAP offloading with [[noma]], [[wireless-power-transfer]], fairness, and Lyapunov-guided DRL. It is closest architecturally to [[jia-2025-dro-uav-hap-mec]] and [[kang-2023-mappo-hierarchical-aerial]], but differs by using [[ddpg]]-attention under a Lyapunov decomposition rather than DRO or MAPPO. It also continues ying-chen's online/game-theoretic air-ground MEC line from [[chen-2023-dotora-air-ground-online]], now in a HAP-UAV-MEC setting.

## Raw artifacts

- `raw/sources/DDPG-Attention-based Resource Allocation and Trajectory Optimization in Hierarchical MEC/DDPG-Attention-based Resource Allocation and Trajectory Optimization in Hierarchical MEC.md`
- Original PDF and extracted figures (`images/`) in the same folder.
