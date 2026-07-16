---
type: source
title: "DDPG-Attention-based Resource Allocation and Trajectory Optimization in Hierarchical MEC"
authors: ["Ying Chen", "Zhihao Hu", "Zhuoyue Chen", "Jiwei Huang", "Lian Zhao"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3676417"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
modeling_card: required
tags: [source, hierarchical-aerial-mec, hap, uav-mec, noma, wireless-power-transfer, lyapunov-optimization, ddpg, attention, fairness]
related: ["[[hierarchical-aerial-mec]]", "[[high-altitude-platform-station]]", "[[noma]]", "[[wireless-power-transfer]]", "[[lyapunov-optimization]]", "[[ddpg]]", "[[fairness-metrics-in-mec]]", "[[uav-trajectory-control]]", "[[chen-2023-dotora-air-ground-online]]", "[[jia-2025-dro-uav-hap-mec]]", "[[hsu-2025-drl-hues-hap-noma]]", "[[kang-2023-mappo-hierarchical-aerial]]"]
created: 2026-07-06
updated: 2026-07-16
---

# DDPG-Attention-based Resource Allocation and Trajectory Optimization in Hierarchical MEC

## Citation

Chen, Y., Hu, Z., Chen, Z., Huang, J., & Zhao, L. (2026). *DDPG-Attention-based Resource Allocation and Trajectory Optimization in Hierarchical MEC*. **IEEE Transactions on Mobile Computing**, 1-17. DOI: 10.1109/TMC.2026.3676417.

## TL;DR

A HAP-UAV-MEC system where IoT devices can compute locally, offload to a UAV, or reach a HAP through the UAV; the UAV can compute tasks itself or forward overflow to the HAP. The system uses NOMA for many IoT uplinks and WPT from the HAP to support the UAV's energy queue. DART combines Lyapunov optimization with DDPG plus attention: Lyapunov turns the multi-stage MINLP into per-slot deterministic subproblems, DDPG-attention handles coupled trajectory / offloading decisions, and convex optimization handles resource allocation.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Multiple IoT devices maintain local and offloading queues, one mobile UAV provides computation and relaying, and a high-altitude platform (HAP) provides additional computation and wireless power transfer. IoT-UAV access uses NOMA with successive interference cancellation, and the UAV can execute tasks or forward them to the HAP.

**Problem & objective**: The long-term problem $P_1$ minimizes the fairness-weighted average cost $\lim_{T\to\infty}\frac{1}{T}\sum_{t=1}^{T}\frac{E_{\mathrm{total}}(t)}{f_a(t)}$ while keeping task and energy queues stable through joint trajectory, offloading, and resource decisions.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Offloading decision | $I_i(t)$ | binary, $\{0,1\}$ | Whether IoT device $i$ offloads to the UAV |
| IoT CPU frequency | $f_{i,l}(t)$ | continuous, $[0,f_{i,l}^{\max}]$ | Local computing frequency |
| IoT-to-UAV offload | $D_{i,o}(t)$ | continuous, nonnegative | Data sent from IoT device $i$ to the UAV |
| UAV-to-HAP offload | $S_{i,o}(t)$ | continuous, nonnegative | UAV data forwarded to the HAP |
| UAV motion | $(v(t),\theta(t))$ | continuous, bounded | UAV speed and flight angle |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Offloading decisions are binary: $I_i(t)\in\{0,1\}$. |
| C2 | Local CPU frequency is bounded: $0\le f_{i,l}(t)\le f_{i,l}^{\max}$. |
| C3 | Local computation cannot exceed the local queue: $D_{i,l}(t)\le Q_{i,l}(t)$. |
| C4 | IoT offloading cannot exceed radio capacity or queue: $0\le D_{i,o}(t)\le R_i(t)\iota$ and $D_{i,o}(t)\le Q_{i,o}(t)$. |
| C5 | UAV forwarding is bounded by its link capacity: $0\le S_{i,o}(t)\le R_s(t)\iota$. |
| C6 | UAV execution and forwarding cannot exceed its task queue: $S_{i,o}(t)+D_{i,u}(t)\le H_i(t)$. |
| C7 | UAV energy queue is bounded: $0\le X(t)\le E^{\max}$. |
| C8 | Long-term queues are stable: $\lim_{T\to\infty}\frac{1}{T}\sum_{t=1}^{T}\mathbb E[Q_{\mathrm{total}}(t)]<\infty$. |

**Algorithm**: Apply Lyapunov drift-plus-penalty to obtain a deterministic per-slot problem, solve independent offloading and local-frequency subproblems analytically, use a knapsack allocation for UAV forwarding, and train an attention-enhanced DDPG policy for coupled UAV trajectory and offloading; convex optimization supplies the remaining bandwidth and resource allocations.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Chen et al. [x] studied hierarchical HAP-UAV MEC with NOMA uplinks, wireless power transfer, multi-tier task offloading, and fairness-aware service of IoT devices. They formulated a long-term cost minimization over UAV trajectory, binary offloading decisions, local CPU frequency, IoT-to-UAV data, and UAV-to-HAP forwarding subject to queue, energy, capacity, and fairness constraints. DART combines Lyapunov decomposition, attention-enhanced DDPG for the coupled trajectory and offloading control, and analytical or convex solutions for the remaining resource subproblems. In simulations, DART reduced energy cost and queue length relative to GTGO, GATO, DDPG, DQN, and random baselines while remaining near exhaustive-search solutions in small instances.

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
