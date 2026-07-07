---
type: concept
title: "Angle-Dependent Rician Fading"
tags: [channel-model, rician-fading, uav, trajectory-optimization, outage]
related:
  - "[[air-to-ground-channel-model]]"
  - "[[uav-data-collection]]"
  - "[[uav-trajectory-control]]"
  - "[[you-2019-rician-uav-data-harvesting]]"
created: 2026-07-07
updated: 2026-07-07
---

# Angle-Dependent Rician Fading

Angle-dependent Rician fading models the UAV-ground channel as a Rician channel whose Rician factor changes with the UAV-ground elevation angle. As elevation increases, the LoS component usually becomes stronger and the scattered component weaker, but the UAV also moves farther from the ground node if it climbs. Trajectory design therefore faces a distance-versus-angle tradeoff rather than a simple "lower is better" or "higher is better" rule.

In [[you-2019-rician-uav-data-harvesting]], this channel model drives 3-D UAV data-harvesting trajectories. The paper maps elevation angle to effective fading power under an outage constraint, approximates that relation with a logistic function, and uses it inside a BCD/SCA trajectory-and-scheduling solver.

This concept complements the broader [[air-to-ground-channel-model]] page, which covers LoS/NLoS probability and other statistical or geometric UAV channel models.
