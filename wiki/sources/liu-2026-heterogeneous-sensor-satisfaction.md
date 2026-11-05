---
type: source
title: "Joint Deployment, User Association, and Power Allocation for Data Collection in UAV-Assisted Wireless Sensor Networks"
authors: ["Yanping Liu", "Kunkun Zhang", "Xuming Fang", "Ming Xiao", "Fuhong Song", "Qing Xue", "Yaping Cui", "Changfeng Ding"]
year: 2026
url: "https://doi.org/10.1109/TWC.2026.3694771"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, multi-uav, wireless-sensor-network, deployment, user-association, power-control, evolutionary-optimization]
related:
  - "[[enhanced-human-evolutionary-optimization]]"
  - "[[air-to-ground-channel-model]]"
  - "[[device-association]]"
  - "[[yanping-liu]]"
  - "[[xuming-fang]]"
  - "[[fuhong-song]]"
created: 2026-07-13
updated: 2026-11-03
modeling_card: required
---

# Joint Deployment, User Association, and Power Allocation for Data Collection in UAV-Assisted Wireless Sensor Networks

## Citation

Liu, Y., Zhang, K., Fang, X., Xiao, M., Song, F., Xue, Q., Cui, Y., & Ding, C. (2026). *Joint Deployment, User Association, and Power Allocation for Data Collection in UAV-Assisted Wireless Sensor Networks*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2026.3694771.

## TL;DR

Models delay-sensitive, energy-sensitive, and dual-sensitive sensors with separate sigmoid satisfaction functions, then jointly selects static 3-D UAV placements, sensor associations, and sensor transmit powers. ELGHEOA combines an enhanced human evolutionary optimizer for the mixed deployment/association variables with a Lagrange-dual power update.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: $M$ statically deployed UAVs collect uplink data from heterogeneous ground sensors $u\in\mathcal U$. Delay-sensitive, energy-sensitive, and dual-sensitive sensors have class-specific sigmoid satisfaction $S_u\in(0,1)$ over probabilistic LoS/NLoS air-to-ground links with mutual interference.
**Problem & objective**: P1 (12) maximizes total sensor satisfaction, $\max_{\{x_m,y_m,h_m,a_{u,m},p_u\}}\sum_{u\in\mathcal U}S_u$ s.t. C1–C7, a mixed-integer nonlinear program; the power subproblem P2 (29) maximizes $\sum_uS_u$ over $\{p_u\}$ s.t. power and rate limits.
**Decision variables**:
| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV placement | $(x_m,y_m,h_m)$ | continuous 3-D position | Static location of UAV $m$ |
| Sensor association | $a_{u,m}$ | binary | Sensor $u$ is served by UAV $m$ |
| Sensor transmit power | $p_u$ | continuous, $\le p_u^{th}$ | Uplink power of sensor $u$ |
**Constraints**:
| ID | Meaning and key expression |
|---|---|
| C1 (12) | Binary association: $a_{u,m}\in\{0,1\}$ |
| C2 (12) | Each UAV serves at most $M^{th}$ sensors |
| C3 (12) | Each sensor associates with exactly one UAV: $\sum_ma_{u,m}=1$ |
| C4 (12) | Sensor power limit: $p_u\le p_u^{th}$ |
| C5 (12) | Minimum rate: $r_u\ge r_u^{th}$ |
| C6 (12) | UAV altitude limit: $h_m\le h_m^{th}$ |
| C7 (12) | Inter-UAV safety distance: $d^m_{m_1,m_2}\ge d^{th}$ |
**Algorithm**: ELGHEOA decomposes P1: EHEOA (human evolutionary optimization with Lévy-flight leaders, a WOA-inspired spiral step, and Sparrow-Search-style explorers, handling real and binary variables) searches deployment and association, and a Lagrangian/gradient-descent method solves P2; the two blocks alternate until satisfaction stabilizes.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Liu et al. [x] studied joint UAV deployment, sensor association, and power allocation for data collection from heterogeneous wireless sensors. They formulated a mixed discrete-continuous optimization that maximizes the sum of class-specific sigmoid satisfaction utilities for delay-sensitive, energy-sensitive, and dual-sensitive sensors. The decision variables include static 3-D UAV positions, sensor-UAV associations, and sensor transmit powers under capacity, QoS, deployment, and separation constraints. They proposed ELGHEOA, an enhanced human evolutionary optimizer that borrows Sparrow-Search followers and a whale-optimization spiral step, and solved the power block with Lagrange duality and gradient descent. Simulations report higher aggregate satisfaction than the compared metaheuristics, a 13.83% gain over the best fixed-power EHEOA result, and, with 2 UAVs, the optimum for 4 or 6 sensors but 2.8% below exhaustive association at 10 sensors.

## System and objective

- Multiple statically deployed UAVs collect uplink data from known ground sensors under probabilistic LoS/NLoS path loss and mutual interference.
- Sensor classes differ in whether delay, energy, or both determine satisfaction; urgency and class-specific thresholds parameterize the sigmoid utility.
- The objective sums sensor satisfaction subject to association, per-UAV capacity, power, QoS, deployment-bound, and UAV-separation constraints.

## Method

The enhanced human evolutionary optimization algorithm adds salp-swarm follower and whale-optimization bubble operators to the base population search, with mixed real/binary encoding and penalty handling. For each deployment/association candidate, the power block is updated by Lagrange duality and gradient descent. The combined ELGHEOA is a heuristic decomposition: the paper reports empirical convergence but no global-optimality guarantee.

## Key findings

- Under fixed placement and association, optimized power improves overall satisfaction by **13.83%** over the best reported fixed-power EHEOA setting.
- In the two-UAV exhaustive-association check, ELGHEOA matches the exhaustive result for four and six sensors and is **2.8%** lower for ten sensors.
- The main evolutionary comparison uses 100 population members, 300 iterations, and 20 independent runs against WOA, SSA, BOA, SMA, PSO, HEOA, and EHEOA.

## Limitations / interpretation

The study is simulation-only and optimizes static deployment rather than flight trajectories. Sensor positions and demands are known; UAV propulsion, repositioning energy, and control overhead are absent. Satisfaction is a model-specific utility whose value can rise when thresholds are relaxed, not a universal QoS measure. The parse labels one threshold as `15 joules` under a rate-like symbol, and the explanation of threshold effects around Figs. 14-15 is mathematically unclear; neither should be used as clean quantitative evidence.

## Relation to the corpus

This source extends deployment and association work with explicitly heterogeneous service utilities. Its solver belongs to the corpus's swarm/evolutionary family, while its separate dual power update is a discrete-continuous decomposition rather than end-to-end learning.

## Raw artifacts

- `raw/sources/Joint_Deployment_User_Association_and_Power_Allocation_for_Data_Collection_in_UAV-Assisted_Wireless_Sensor_Networks/Joint_Deployment_User_Association_and_Power_Allocation_for_Data_Collection_in_UAV-Assisted_Wireless_Sensor_Networks.md`
- Origin PDF and extracted figures (`images/`) in the same folder.
