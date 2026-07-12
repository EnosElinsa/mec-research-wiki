---
type: concept
title: "Radio-Map-Aided UAV Path Planning"
tags: [radio-map, path-planning, cellular-connected-uav, communication-coverage, a-star]
related:
  - "[[radio-map-assisted-channel-estimation]]"
  - "[[cellular-connected-uav]]"
  - "[[air-to-ground-channel-model]]"
  - "[[blockage-aware-channel-model]]"
  - "[[uav-trajectory-control]]"
  - "[[cao-2026-radio-map-cargo-pickup]]"
created: 2026-07-13
updated: 2026-07-13
---

# Radio-Map-Aided UAV Path Planning

Radio-map-aided UAV path planning uses a location-indexed channel or SNR map as a movement-feasibility layer. The planner associates each position with its best terrestrial base station, removes positions whose expected link quality falls below a threshold, and searches the remaining space for a communication-safe path. It therefore consumes a radio map to guide movement rather than using one to estimate the current channel, which is the role captured by [[radio-map-assisted-channel-estimation]].

In [[cao-2026-radio-map-cargo-pickup]], a physical-map-derived expected-SNR grid is thresholded into feasible and infeasible cells. Eight-neighbor A* computes all-pairs warehouse/pickup paths, and the resulting distance matrix feeds a cargo-allocation optimizer. This approach gives deterministic offline paths when the map is accurate; the paper leaves stochastic channel variation, handover delay, the map-resolution/computational-complexity tradeoff, and full 3-D paths for future work.
