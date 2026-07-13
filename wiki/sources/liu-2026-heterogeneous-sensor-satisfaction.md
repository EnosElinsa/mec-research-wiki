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
updated: 2026-07-13
---

# Joint Deployment, User Association, and Power Allocation for Data Collection in UAV-Assisted Wireless Sensor Networks

## Citation

Liu, Y., Zhang, K., Fang, X., Xiao, M., Song, F., Xue, Q., Cui, Y., & Ding, C. (2026). *Joint Deployment, User Association, and Power Allocation for Data Collection in UAV-Assisted Wireless Sensor Networks*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2026.3694771.

## TL;DR

Models delay-sensitive, energy-sensitive, and dual-sensitive sensors with separate sigmoid satisfaction functions, then jointly selects static 3-D UAV placements, sensor associations, and sensor transmit powers. ELGHEOA combines an enhanced human evolutionary optimizer for the mixed deployment/association variables with a Lagrange-dual power update.

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
