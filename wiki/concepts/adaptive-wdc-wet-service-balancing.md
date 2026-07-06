---
type: concept
title: "Adaptive WDC/WET Service Balancing"
tags: [low-altitude-economy, wireless-data-collection, wireless-energy-transfer, multi-objective-optimization]
related:
  - "[[zhao-2026-adaptive-wdc-wet-lae]]"
  - "[[uav-data-collection]]"
  - "[[wireless-power-transfer]]"
  - "[[age-of-information]]"
  - "[[aoi-energy-tradeoff]]"
  - "[[low-altitude-intelligent-network]]"
created: 2026-07-07
updated: 2026-07-07
---

# Adaptive WDC/WET Service Balancing

Joint control of UAV-provided wireless data collection and wireless energy transfer when the two services compete for the same UAV mobility, energy, and scheduling budget. In [[zhao-2026-adaptive-wdc-wet-lae]], I-devices need freshness-oriented WDC and E-devices need RF energy replenishment, so the optimizer minimizes [[age-of-information|AoI]] and hungry-level-of-energy together rather than treating data collection and charging as separate missions.

The distinctive feature is **adaptive scalarization**. Instead of choosing a fixed WDC-vs-WET objective weight by trial and error, the paper learns the reward preference through a central controller and lets local UAV agents optimize trajectory, WET, and WDC policies under that preference.
