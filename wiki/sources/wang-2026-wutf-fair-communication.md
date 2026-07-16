---
type: source
title: "DRL-Based Wireless-Powered UAVs Trajectories Planning for Fair Communication"
authors: ["Peixiang Wang", "Xiaoyu Wang", "He Huang", "Haipeng Dai"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3664292"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, uav, wireless-power-transfer, fairness, mappo, ctde, trajectory-control]
related:
  - "[[wireless-powered-uav-fair-service-control]]"
  - "[[wireless-power-transfer]]"
  - "[[jains-fairness-index]]"
  - "[[ma-pomdp]]"
  - "[[mappo]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[sequential-multi-agent-policy-generation]]"
  - "[[rotary-wing-propulsion-energy-model]]"
  - "[[uav-trajectory-control]]"
created: 2026-07-12
updated: 2026-07-16
modeling_card: required
---

# DRL-Based Wireless-Powered UAVs Trajectories Planning for Fair Communication

## Citation

Wang, P., Wang, X., Huang, H., & Dai, H. (2026). *DRL-Based Wireless-Powered UAVs Trajectories Planning for Fair Communication*. **IEEE Transactions on Mobile Computing**, 25(7), 10317-10334. DOI: 10.1109/TMC.2026.3664292.

## TL;DR

WUTF coordinates wireless-powered UAV base stations through centralized training and decentralized execution. Each UAV selects speed and yaw from local observations, while a shared critic and sequential PPO-style actor updates optimize a reward that combines underserved-user communication value, Jain fairness, propulsion/communication energy, and safety penalties.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Wireless-powered UAV base stations fly at fixed altitude to serve stationary ground users and recharge while hovering near wireless charging towers. The controller must balance cumulative throughput, geographical fairness, propulsion and communication energy, and long-duration operation.

**Problem & objective**: Problem P1 maximizes communication efficiency, $\max_{\mathbf v,\boldsymbol\psi,\mathbf b}\frac{P_TF_T}{\sum_{t,i}E_{t,\mathrm{out}}^{f_i}}$, where $P_T$ is total throughput, $F_T$ is Jain fairness, and the denominator is total UAV energy.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV speed | $v_{f_i}^t$ | continuous, $[0,v_{\max}]$ | Per-slot UAV flight speed |
| UAV yaw | $\psi_{f_i}^t$ | continuous, $[0,2\pi]$ | Flight direction in slot $t$ |
| User association | $b_{f_i,u_j}^t$ | binary | Indicates whether UAV $f_i$ serves user $u_j$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| 23a | UAV battery remains positive and below capacity, $0<B_t^{f_i}\leq B_{\max}$ |
| 23b | User association is binary |
| 23c | Each user is served by at most one UAV, $\sum_i b_{f_i,u_j}^t\leq1$ |
| 23d | UAV speed satisfies $0\leq v_{f_i}^t\leq v_{\max}$ |
| 23e | UAV yaw satisfies $0\leq\psi_{f_i}^t\leq2\pi$ |
| 23f-23g | UAV coordinates remain inside the square task area |

**Algorithm**: WUTF casts the problem as a multi-agent POMDP in which each UAV actor selects speed and yaw from local observations. CNN and GRU layers encode spatial and temporal information, a centralized critic supports training, and randomized sequential PPO-style actor updates reduce conflicts between changing agent policies before decentralized execution.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Wang et al. [x] studied long-duration fair communication by wireless-powered UAV base stations that can recharge near fixed charging towers. They maximized total throughput multiplied by Jain fairness per unit UAV energy over speed, yaw, and user-association decisions subject to battery, association, mobility, and area constraints. WUTF uses CNN-GRU actors, a centralized critic, and sequential PPO-style policy updates within a multi-agent partially observable model. For four UAVs, the reported Jain fairness was 0.748 compared with 0.529 for modified LTCC-UDUA, corresponding to a 41.4% improvement. The authors also reported higher communication efficiency than all listed learning and heuristic baselines across the examined charging ranges. A separate Shanghai-map simulation with 378 users demonstrated the learned two-UAV trajectories over a one-hour mission.

## Problem

Multiple battery-limited UAV base stations must serve geographically distributed users while periodically recharging from wireless charging towers. Trajectories determine coverage, throughput, propulsion demand, and charging opportunity at the same time, so maximizing only aggregate rate can repeatedly favor easy-to-reach users and shortening routes can leave service regions uncovered.

## System model

- Fixed-altitude rotary-wing UAVs serve fixed ground users over probabilistic LoS/NLoS air-ground links and OFDMA. A user associates with at most one UAV in a slot and must meet an SINR threshold.
- Each slot has movement and hovering/service phases. Charging towers transfer additive distance-dependent power while a UAV hovers, subject to UAV input and tower output caps.
- UAV energy includes acceleration, steady flight, deceleration, hovering, and communication; the state tracks UAV/user/tower positions, accumulated user throughput, and UAV batteries.
- The formal mixed-integer nonlinear problem maximizes total throughput times Jain fairness divided by total UAV energy, subject to battery, association, speed, yaw, and area constraints.

## Method

WUTF casts online control as a multi-agent POMDP. Each actor observes its own position and battery plus all user/tower positions and accumulated user throughput, but not other UAV positions or batteries. Its continuous action is speed and yaw; service follows the resulting coverage and association model.

The actor uses CNN spatial features, layer normalization, and a GRU. A centralized critic sees the global state during training. Rollouts feed GAE, then actors are updated in randomized sequence with a clipped PPO-style objective that uses already-updated predecessor policies to reduce joint-policy conflict. The critic is updated last and discarded for decentralized execution. The reward multiplies Jain fairness by an underserved-user communication value, divides by weighted energy, and penalizes battery depletion or obstacle collision; those penalties are learned-control safeguards rather than explicit constraints in the stated optimization problem.

## Key findings

- For four UAVs, WUTF reaches Jain fairness `0.748` versus `0.529` for modified LTCC-UDUA, a reported `41.4%` improvement.
- Across the tested charging ranges, the prose reports average fairness gains of `3.54%`, `32.01%`, `18.69%`, `78.21%`, `61.44%`, and `174.22%` over MAPPO, LTCC-UDUA, MADDPG, QMIX, KM-GA, and Random, respectively.
- The communication-efficiency sentence reports gains of `5.97%`, `22.23%`, `21.41%`, `123.62%`, `150.99%`, and `693.93%` over MAPPO, LTCC-UDUA, MADDPG, QMIX, `GA`, and Random. The baseline definition names the fifth method KM-GA, so `GA` appears to be shorthand in this result sentence.
- With 400 users and two UAVs, the reported fairness and communication efficiency are `0.78` and `0.45`. A separate real-map simulation places 378 users in Shanghai and plans two UAVs over a one-hour, 60-slot mission.

## Limitations / parse caveats

The study remains simulation-based. Its main model fixes user locations and UAV altitude, allows charging only while hovering, adds tower powers without wave-interference modeling, uses probabilistic rather than map-exact LoS, and gives deployed actors no other-UAV state or communication. Wind, detailed fading, charging budgets, and adaptive altitude are not part of the evaluated controller. The WCT-outage response below 10% battery is a separate emergency rule rather than the base policy. Several extracted equations and table cells are damaged, so figure-only values and OCR-truncated parameters are not transcribed. The parse omits publication metadata; an exact-title Crossref record supplies the 2026 TMC citation. Technical claims come only from the parse.

## Relation to the corpus

[[wireless-powered-uav-fair-service-control]] connects [[wireless-power-transfer]] to fairness-aware multi-UAV communication rather than device-side harvest-then-offload. It combines [[jains-fairness-index|Jain fairness]], detailed [[rotary-wing-propulsion-energy-model|rotary-wing energy]], and WUTF's sequential PPO-style multi-agent updates under [[centralized-training-decentralized-execution|CTDE]].

## Raw artifacts

- Parse: `raw/sources/DRL-Based_Wireless-Powered_UAVs_Trajectories_Planning_for_Fair_Communication/DRL-Based_Wireless-Powered_UAVs_Trajectories_Planning_for_Fair_Communication.md`
- Origin PDF: `raw/sources/DRL-Based_Wireless-Powered_UAVs_Trajectories_Planning_for_Fair_Communication/DRL-Based_Wireless-Powered_UAVs_Trajectories_Planning_for_Fair_Communication.pdf`
- Figures: `raw/sources/DRL-Based_Wireless-Powered_UAVs_Trajectories_Planning_for_Fair_Communication/images/`
