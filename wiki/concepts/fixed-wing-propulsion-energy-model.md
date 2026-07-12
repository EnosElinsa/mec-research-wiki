---
type: concept
title: "Fixed-Wing UAV Propulsion Energy Model"
tags: [uav, energy-model, propulsion, trajectory-optimization, fixed-wing]
related:
  - "[[rotary-wing-propulsion-energy-model]]"
  - "[[uav-trajectory-control]]"
  - "[[energy-latency-tradeoff]]"
  - "[[zeng-2017-energy-efficient-uav-trajectory]]"
  - "[[liu-2026-usp-nfrp-emergency-communication]]"
  - "[[persistent-emergency-uav-swarm-service]]"
  - "[[zhu-2026-fixed-wing-fd-af-wind]]"
created: 2026-06-01
updated: 2026-07-13
---

# Fixed-Wing UAV Propulsion Energy Model

The closed-form model for a **fixed-wing** UAV's propulsion energy as a function of its flight **velocity (speed and direction)** and **acceleration**, derived for straight-and-level (constant-altitude) flight. It starts from the aerodynamic drag

`D = c₁V² + c₂κ²/V²`

where the first term is **parasitic drag** (grows with speed²), the second is **lift-induced drag** (grows as 1/speed²), `κ = L/W` is the load factor, and `c₁ = ½ρC_D₀S`, `c₂ = 2W²/(πe₀A_R ρS)` are constants of air density, drag coefficient, wing area, weight, Oswald efficiency, and aspect ratio. Minimum drag `D_min = 2√(c₁c₂)` occurs at the drag-minimum speed `V_dm = (c₂/c₁)^{1/4}`.

The defining property versus the [[rotary-wing-propulsion-energy-model]]: fixed-wing propulsion power **diverges as `V → 0`** — a fixed-wing UAV **cannot hover**, so energy-efficient designs must keep it moving (e.g., orbiting a ground terminal). Fixed-wing UAVs typically carry larger payloads and fly faster than rotary-wing counterparts.

This model originates in [[zeng-2017-energy-efficient-uav-trajectory]] (Zeng & Zhang, IEEE TWC 2017), which the authors state is the first to relate UAV propulsion energy to **both velocity and acceleration** (prior models used speed only). It underpins energy-efficient (bits/Joule) [[uav-trajectory-control]] and the [[energy-latency-tradeoff]] in aerial communications. The companion model for hovering-capable UAVs is the [[rotary-wing-propulsion-energy-model]] from [[zeng-2019-rotary-wing-energy-min]].

[[liu-2026-usp-nfrp-emergency-communication]] applies the fixed-wing endurance logic to [[persistent-emergency-uav-swarm-service]]: aircraft fly at constant speed, approximate hovering with small circles, and must retain enough energy to return to the charging station before another UAV takes over.

[[zhu-2026-fixed-wing-fd-af-wind]] extends straight-level-flight power accounting to constant 3-D wind. The wind triangle separates air speed from ground speed and derives pitch/crab compensation; under its model, vertical wind changes engine power directly, while horizontal wind changes ground speed, relay geometry, and delivered data. The design optimizes propulsion only on a fixed route and does not establish a general wind-aware trajectory model.
