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
updated: 2026-07-16
modeling_card: required
---

# Joint Deployment, User Association, and Power Allocation for Data Collection in UAV-Assisted Wireless Sensor Networks

## Citation

Liu, Y., Zhang, K., Fang, X., Xiao, M., Song, F., Xue, Q., Cui, Y., & Ding, C. (2026). *Joint Deployment, User Association, and Power Allocation for Data Collection in UAV-Assisted Wireless Sensor Networks*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2026.3694771.

## TL;DR

Models delay-sensitive, energy-sensitive, and dual-sensitive sensors with separate sigmoid satisfaction functions, then jointly selects static 3-D UAV placements, sensor associations, and sensor transmit powers. ELGHEOA combines an enhanced human evolutionary optimizer for the mixed deployment/association variables with a Lagrange-dual power update.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Multiple statically deployed UAVs collect uplink data from heterogeneous ground sensors. Delay-sensitive, energy-sensitive, and dual-sensitive sensors use class-specific sigmoid satisfaction functions over probabilistic-LoS/NLoS air-to-ground links with mutual interference.

**Problem & objective**: Joint deployment, association, and power-control optimization, a mixed discrete-continuous non-convex problem, maximizes aggregate sensor satisfaction, $\max_{\mathbf q,\mathbf x,\mathbf p}\sum_n U_n(\mathrm{delay}_n,\mathrm{energy}_n)$, subject to association, capacity, power, QoS, deployment, and separation constraints.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV placement | $\mathbf q_u$ | continuous 3-D position | Static location of UAV $u$ |
| Sensor association | $x_{u,n}$ | binary | Sensor $n$ is collected by UAV $u$ |
| Sensor transmit power | $p_n$ | continuous, bounded | Uplink power of sensor $n$ |
| Satisfaction utility | $U_n$ | continuous sigmoid value | Class-specific delay/energy satisfaction |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Each sensor associates with at most one UAV and each UAV respects its service capacity |
| C2 | Sensor powers satisfy per-device bounds and link QoS requirements |
| C3 | UAV placements lie in the permitted 3-D region |
| C4 | Inter-UAV separation and mutual-interference constraints hold |
| C5 | Class-specific delay and energy satisfaction inputs use the modeled sigmoid thresholds |

**Algorithm**: Encode placement and association in ELGHEOA with mixed real/binary individuals → apply salp-swarm and whale-optimization operators with penalty handling → update the power block by Lagrange duality and gradient descent → iterate until aggregate satisfaction stabilizes.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Liu et al. [x] studied joint UAV deployment, sensor association, and power allocation for data collection from heterogeneous wireless sensors. They formulated a mixed discrete-continuous optimization that maximizes the sum of class-specific sigmoid satisfaction utilities for delay-sensitive, energy-sensitive, and dual-sensitive sensors. The decision variables include static 3-D UAV positions, sensor-UAV associations, and sensor transmit powers under capacity, QoS, deployment, and separation constraints. They proposed ELGHEOA, an enhanced human evolutionary optimizer with salp-swarm and whale-optimization operators, and solved the power block with Lagrange duality and gradient descent. Simulations report improved aggregate satisfaction and close agreement with exhaustive association for the tested small cases.

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
