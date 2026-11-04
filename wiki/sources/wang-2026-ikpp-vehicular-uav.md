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
updated: 2026-11-03
---

# Joint Trajectory Design and Resource Allocation for Energy-Efficient Multi-UAV Assisted Vehicular Networks: An IKPP Approach

## Citation

Wang, J., Zhou, X., Zhang, H., Liang, D., & Yuan, D. (2026). Joint trajectory design and resource allocation for energy-efficient multi-UAV assisted vehicular networks: An IKPP approach. *IEEE Transactions on Wireless Communications, 25*, 2150-2166. https://doi.org/10.1109/TWC.2025.3595138

## TL;DR

Multiple fixed-altitude UAV base stations collect OFDMA uplink traffic from moving vehicles while reusing subcarriers across UAVs. IKPP combines PPO-clip trajectory/power/carrier scores with nearest-UAV load balancing and discrete action reconstruction to maximize simulated throughput per UAV propulsion power.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Multiple fixed-altitude UAV base stations collect OFDMA uplink traffic from road-constrained moving vehicles. Sub-carriers are orthogonal within a UAV and reused across UAVs, creating co-channel interference, while UAV propulsion power depends on flight speed. In the paper's notation $j$ indexes UAVs and $m$ indexes vehicles.

**Problem & objective**: Problem (21) is a mixed-integer non-convex fractional program that maximizes long-term energy efficiency, $\max_{\{\boldsymbol\Lambda,\boldsymbol\Omega,\mathbf P,\mathbf Q\}}\sum_n\frac{\sum_m\sum_j\sum_c\beta_{j,m}[n]\omega_m^c[n]R_{j,m}^c[n]}{\sum_jP_j^{fl}[n]}$, the per-slot sum rate divided by UAV propulsion power, summed over slots.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Vehicle-UAV association | $\beta_{j,m}[n]\in\boldsymbol\Lambda$ | binary | Vehicle $m$ is served by UAV $j$ |
| Sub-carrier assignment | $\omega_m^c[n]\in\boldsymbol\Omega$ | binary | Vehicle $m$ uses sub-carrier $c$ |
| Vehicle transmit power | $p_m[n]\in\mathbf P$ | continuous, $[0,P_m^{max}]$ | Uplink power of vehicle $m$ |
| UAV trajectory | $\mathbf q_j[n]\in\mathbf Q$ | continuous 2-D position | Position of UAV $j$, updated by its velocity |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| QoS | Each vehicle's rate is at least $R_m^{QoS}$ |
| 21b | $0\le p_m[n]\le P_m^{max}$ |
| 21c | Each vehicle associates with at most one UAV |
| 21e-21f | Each vehicle uses at most one sub-carrier, and each sub-carrier at a UAV serves at most one vehicle; association and sub-carrier variables are binary |
| 21g | UAVs stay inside the $s_x\times s_y$ service region |
| 21h, 21k | Per-slot UAV displacement is at most $D_{\max}$, with $\mathbf q_j[n]=\mathbf q_j[n-1]+\mathbf v_j[n]\tau_t$ |
| 21j | UAV separation is at least $S_{\min}$ |
| 21l-21m | Vehicle speed bounds and road-following movement model |

The paper's text numbers these constraints one step off from the parsed tags; the IDs above follow the parsed equation tags.

**Algorithm**: Let PPO-clip output motion, power, and carrier scores → associate each vehicle with its nearest proposed UAV → move excess vehicles to other UAVs until carrier capacities hold → reconstruct binary carrier assignments from the scores → apply QoS, boundary, and collision penalties and update the policy.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Wang et al. [x] studied joint trajectory design and resource allocation for energy-efficient multi-UAV vehicular networks. They formulated horizon throughput-to-propulsion-power maximization over UAV speed and heading, vehicle association, uplink power, and OFDMA carrier assignment under QoS, power, association, sub-carrier, boundary, movement, and collision constraints. IKPP uses PPO-clip to generate continuous motion, power, and carrier scores. A nearest-UAV load-balancing procedure enforces service capacity, and discrete action reconstruction converts the carrier scores into assignments. Simulations report the highest reward and system energy efficiency against schemes that optimize only part of the variables and against a variant without the action-space reduction of Algorithm 1, with per-slot execution time below 0.005 s.

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
