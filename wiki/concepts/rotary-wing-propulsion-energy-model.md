---
type: concept
title: "Rotary-Wing UAV Propulsion Energy Model"
tags: [uav, energy-model, propulsion, trajectory-optimization]
related:
  - "[[uav-trajectory-control]]"
  - "[[energy-latency-tradeoff]]"
  - "[[zeng-2019-rotary-wing-energy-min]]"
  - "[[li-2024-rldc-uav-swarm-clustering]]"
  - "[[lee-2026-uav-delivery-time-energy]]"
  - "[[gong-2026-uav-3d-visual-coverage]]"
  - "[[path-aware-3d-visual-coverage]]"
  - "[[hua-2026-ddrl-content-delivery]]"
  - "[[wang-2026-wutf-fair-communication]]"
  - "[[wireless-powered-uav-fair-service-control]]"
  - "[[tian-2026-joint-localization-communication]]"
  - "[[he-2026-memdrl-uav-navigation]]"
  - "[[zhang-2022-solar-charging-uav-iot]]"
  - "[[huroon-2026-bd-ris-rsma-uav]]"
  - "[[fu-2026-uav-fl-user-grouping]]"
created: 2026-05-31
updated: 2026-07-13
---

# Rotary-Wing UAV Propulsion Energy Model

The closed-form model for a **rotary-wing** UAV's propulsion power as a function of forward speed `V`, with three additive terms — **blade profile**, **induced**, and **parasite**:

`P(V) = P₀(1 + 3V²/U_tip²) + P_i(√(1 + V⁴/4v₀⁴) − V²/2v₀²)^{1/2} + ½ d₀ρsAV³`

where `P₀`, `P_i` are the blade-profile and induced power in hovering, `U_tip` the rotor-blade tip speed, `v₀` the mean rotor induced velocity in hover, `d₀` the fuselage drag ratio, `s` rotor solidity, `ρ` air density, `A` rotor disc area.

Two properties drive UAV trajectory design: hovering power `P_h = P₀ + P_i` is **finite** (rotary-wing UAVs *can* hover, unlike fixed-wing UAVs whose power → ∞ at `V = 0`), and `P(V)` is **neither convex nor concave** — it first decreases then increases with `V`, so hovering is feasible but not the most power-conserving state.

This model originates in [[zeng-2019-rotary-wing-energy-min]] (Zeng, Xu & Zhang, IEEE TWC 2019) and is reused as the propulsion-energy reference across the corpus's UAV-MEC energy formulations — e.g. [[li-2024-rldc-uav-swarm-clustering]] cites it for the leader/follower propulsion terms. It underpins energy-aware [[uav-trajectory-control]] and the [[energy-latency-tradeoff]] in aerial MEC. [[lee-2026-uav-delivery-time-energy]] adapts the same propulsion-energy logic to parcel delivery, where the carried payload weight changes induced power and thus changes the optimal pickup/drop-off order. [[gong-2026-uav-3d-visual-coverage]] uses the same idea in non-MEC [[path-aware-3d-visual-coverage]], where distance-shortest routes can consume more energy than velocity/acceleration-aware paths.

[[hua-2026-ddrl-content-delivery]] uses the same three-term rotary-wing power form to turn served users per consumed energy into an intrinsic reward alongside content-acquisition delay and cache-hit performance.

[[wang-2026-wutf-fair-communication]] resolves slot energy into acceleration, steady flight, deceleration, hovering, and communication terms, then couples that demand to charging-tower proximity inside [[wireless-powered-uav-fair-service-control]].

[[zhang-2022-solar-charging-uav-iot]] combines horizontal, vertical, and hover demand with solar/station charging; [[huroon-2026-bd-ris-rsma-uav]] counts hovering/flying power inside a BD-RIS/RSMA energy-efficiency ratio; and [[fu-2026-uav-fl-user-grouping]] finds that propulsion dominates its grouped UAV-FL energy budget.
