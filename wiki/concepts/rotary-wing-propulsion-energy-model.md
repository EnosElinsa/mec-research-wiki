---
type: concept
title: "Rotary-Wing UAV Propulsion Energy Model"
tags: [uav, energy-model, propulsion, trajectory-optimization]
related:
  - "[[uav-trajectory-control]]"
  - "[[energy-latency-tradeoff]]"
  - "[[zeng-2019-rotary-wing-energy-min]]"
  - "[[li-2024-rldc-uav-swarm-clustering]]"
created: 2026-05-31
updated: 2026-05-31
---

# Rotary-Wing UAV Propulsion Energy Model

The closed-form model for a **rotary-wing** UAV's propulsion power as a function of forward speed `V`, with three additive terms — **blade profile**, **induced**, and **parasite**:

`P(V) = P₀(1 + 3V²/U_tip²) + P_i(√(1 + V⁴/4v₀⁴) − V²/2v₀²)^{1/2} + ½ d₀ρsAV³`

where `P₀`, `P_i` are the blade-profile and induced power in hovering, `U_tip` the rotor-blade tip speed, `v₀` the mean rotor induced velocity in hover, `d₀` the fuselage drag ratio, `s` rotor solidity, `ρ` air density, `A` rotor disc area.

Two properties drive UAV trajectory design: hovering power `P_h = P₀ + P_i` is **finite** (rotary-wing UAVs *can* hover, unlike fixed-wing UAVs whose power → ∞ at `V = 0`), and `P(V)` is **neither convex nor concave** — it first decreases then increases with `V`, so hovering is feasible but not the most power-conserving state.

This model originates in [[zeng-2019-rotary-wing-energy-min]] (Zeng, Xu & Zhang, IEEE TWC 2019) and is reused as the propulsion-energy reference across the corpus's UAV-MEC energy formulations — e.g. [[li-2024-rldc-uav-swarm-clustering]] cites it for the leader/follower propulsion terms. It underpins energy-aware [[uav-trajectory-control]] and the [[energy-latency-tradeoff]] in aerial MEC.
