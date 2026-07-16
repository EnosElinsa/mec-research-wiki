---
type: source
modeling_card: required
title: "Joint Trajectory Design and Resource Allocation for Energy-Efficient Multi-UAV Assisted Vehicular Networks: An IKPP Approach"
authors: ["Jing Wang", "Xiaotian Zhou", "Haixia Zhang", "Daojun Liang", "Dongfeng Yuan"]
year: 2026
url: "https://doi.org/10.1109/TWC.2025.3595138"
venue: "IEEE Transactions on Wireless Communications (TWC)"
tags: [source, vehicular-network, multi-uav, energy-efficiency, proximal-policy-optimization]
related:
  - "[[ppo]]"
  - "[[ikpp-action-reconstruction]]"
  - "[[device-association]]"
  - "[[uav-trajectory-control]]"
  - "[[rotary-wing-propulsion-energy-model]]"
  - "[[xiaotian-zhou]]"
  - "[[haixia-zhang]]"
created: 2026-07-13
updated: 2026-07-16
---

# Joint Trajectory Design and Resource Allocation for Energy-Efficient Multi-UAV Assisted Vehicular Networks: An IKPP Approach

## Citation

Wang, J., Zhou, X., Zhang, H., Liang, D., & Yuan, D. (2026). Joint trajectory design and resource allocation for energy-efficient multi-UAV assisted vehicular networks: An IKPP approach. *IEEE Transactions on Wireless Communications, 25*, 2150-2166. https://doi.org/10.1109/TWC.2025.3595138

## TL;DR

Multiple fixed-altitude UAV base stations collect OFDMA uplink traffic from moving vehicles while reusing subcarriers across UAVs. IKPP combines PPO-clip trajectory/power/carrier scores with nearest-UAV load balancing and discrete action reconstruction to maximize simulated throughput per UAV propulsion power.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Multiple fixed-altitude UAV base stations collect OFDMA uplink traffic from road-constrained moving vehicles. Subcarriers are orthogonal within a UAV and reused across UAVs, creating co-channel interference, while UAV propulsion power depends on flight speed.

**Problem & objective**: A constrained fractional mixed-action problem maximizes horizon energy efficiency, $\max \sum_t\frac{\sum_k R_k(t)}{\sum_m P_m^{\mathrm{fly}}(t)}$, through UAV motion, association, vehicle power, and carrier assignment.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV speed and heading | $v_m(t),\theta_m(t)$ | continuous, bounded | Trajectory-control action of UAV $m$ |
| Vehicle association | $x_{k,m}(t)$ | binary | UAV serving vehicle $k$ |
| Vehicle transmit power | $p_k(t)$ | continuous, bounded | Uplink power of vehicle $k$ |
| Subcarrier assignment | $a_{k,n}(t)$ | binary | Carrier $n$ allocated to vehicle $k$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Each vehicle associates with one UAV and receives one feasible carrier |
| C2 | A UAV serves no more vehicles than its available subcarriers |
| C3 | Vehicle rates satisfy QoS and powers remain within their limits |
| C4 | UAVs remain inside the service region, meet endpoint conditions, and obey speed limits |
| C5 | Pairwise UAV separation remains above the collision threshold |

**Algorithm**: Let PPO-clip output motion, power, and carrier scores → associate each vehicle with its nearest proposed UAV → move excess vehicles to other UAVs until carrier capacities hold → reconstruct binary carrier assignments from the scores → apply QoS, boundary, and collision penalties and update the policy.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Wang et al. [x] studied joint trajectory design and resource allocation for energy-efficient multi-UAV vehicular networks. They formulated horizon throughput-to-propulsion-power maximization over UAV speed and heading, vehicle association, uplink power, and OFDMA carrier assignment under QoS, capacity, boundary, endpoint, and collision constraints. IKPP uses PPO-clip to generate continuous motion, power, and carrier scores. A nearest-UAV load-balancing procedure enforces service capacity, and discrete action reconstruction converts the carrier scores into assignments. Simulations report higher reward and energy efficiency than the evaluated PPO, DDPG, static, and ablation baselines, with policy inference below the simulated slot duration.

## Problem and system model

The system jointly chooses per-slot UAV speed/heading, vehicle power, vehicle-UAV association, and subcarrier assignment. It models probabilistic LoS channels, cross-UAV co-channel interference, vehicle QoS, UAV collision separation, service boundaries, start/end positions, and speed limits.

The centralized state contains every current vehicle coordinate and previous UAV coordinate, assuming slot-start GPS broadcasts. The objective sums, across time slots, the ratio of aggregate vehicle throughput to aggregate UAV propulsion power in each slot.

## Method

PPO-clip emits continuous motion, power, and per-UAV carrier scores. The so-called improved k-means step assigns every vehicle to its nearest proposed UAV, then moves excess members to other UAVs by distance until carrier-capacity limits hold; it does not update cluster centroids. [[ikpp-action-reconstruction]] selects the required number of low-scored carriers for each UAV and assigns them sequentially to its vehicles.

QoS, boundary, and collision requirements enter the reward as fixed penalties. This does not guarantee feasibility of the original constrained fractional program, and neither the heuristic association nor PPO has a global-optimality guarantee.

## Key findings

- The tested policy reports mean inference time of **0.0017-0.0035 s** and all sampled decisions below **0.005 s** versus a one-second slot; offline training and system overhead are excluded.
- IKPP reports the highest reward and energy efficiency among its ablations, IKDDPG, and direct-PPO association across tested configurations, without a headline percentage.
- Trajectory-enabled policies concentrate speed near 12 m/s and modeled propulsion near 120 W; the static-hover case is modeled at 168.5 W.
- Moderate injected speed errors retain similar rewards in five tests, while a +5 m/s error degrades reward.

## Limitations

Evidence is simulation-only. The model assumes exact global GPS state, fixed UAV altitude, quasi-static one-second slots, known channel statistics, centralized control, and predictable road-constrained motion. Action reconstruction does not optimize vehicle-carrier pairing within a UAV. The real-time claim covers policy inference on the test computer, not training, radio/control latency, safety certification, or end-to-end deployment.

## Relation to the corpus

This source adds a hybrid heuristic/[[ppo]] controller to the multi-UAV vehicular resource-management thread. It differs from generic [[device-association]] policies by deriving association from proposed UAV motion and enforcing per-UAV service load before reconstructing carrier assignments.

## Raw artifacts

- Parse: `raw/sources/Joint_Trajectory_Design_and_Resource_Allocation_for_Energy-Efficient_Multi-UAV_Assisted_Vehicular_Networks_An_IKPP_Approach/Joint_Trajectory_Design_and_Resource_Allocation_for_Energy-Efficient_Multi-UAV_Assisted_Vehicular_Networks_An_IKPP_Approach.md`
- Origin PDF and extracted figures (`images/`) are in the same folder.
