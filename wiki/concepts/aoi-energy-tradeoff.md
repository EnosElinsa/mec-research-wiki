---
type: concept
title: "AoI-Energy Tradeoff"
tags: [metrics, multi-objective, freshness, energy]
related:
  - "[[age-of-information]]"
  - "[[multi-objective-reinforcement-learning]]"
  - "[[energy-balancing-uav]]"
  - "[[song-2024-mol-aoi-energy]]"
  - "[[shi-2025-aoi-energy-replenishment-multiuav]]"
  - "[[liao-2026-aoi-ris-uav-usv-mec]]"
  - "[[cai-2026-llm-drl-secure-lae-data]]"
  - "[[zhao-2026-adaptive-wdc-wet-lae]]"
created: 2026-05-29
updated: 2026-07-07
---

# AoI-Energy Tradeoff

The conflicting-objective tension (the "AET problem") between minimizing data freshness ([[age-of-information]]) and minimizing UAV energy in aerial data-collection MEC. Collecting from more ground devices and flying longer/faster paths lowers AoI but raises propulsion and compute energy; conserving energy lets AoI grow. Because the objectives genuinely conflict, the right output is a **Pareto set** of policies, not a single fixed-weight compromise.

In the wiki, [[song-2024-mol-aoi-energy]] formalizes this tradeoff and solves it with [[multi-objective-reinforcement-learning]] (MOL-AET) to produce nondominated policies spanning energy-focused (short, cautious paths) to AoI-focused (long, sweeping paths) preferences. [[shi-2025-aoi-energy-replenishment-multiuav]] adds the replenishment version where UAVs spend time and battery on wireless charging, sensor data collection, BS offloading, and charging-station visits. [[liao-2026-aoi-ris-uav-usv-mec]] gives the maritime/RIS version by minimizing a weighted sum of USV average AoI and RUAV flight energy, [[cai-2026-llm-drl-secure-lae-data]] folds AoI and energy into secure LAE data collection, and [[zhao-2026-adaptive-wdc-wet-lae]] replaces UAV-energy cost with energy-device HoE under an adaptive WDC/WET preference. It is the freshness-flavored sibling of the energy-vs-delay and [[energy-balancing-uav]] tradeoffs elsewhere in the corpus.
