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
  - "[[guo-2026-event-triggered-sinr-navigation]]"
  - "[[uncertainty-triggered-radio-map-update]]"
  - "[[chakraborty-2026-skyscale-rti-deployment]]"
  - "[[handoff-aware-uav-trajectory-planning]]"
  - "[[peng-2025-cargo-uav-energy-outage-tradeoff]]"
  - "[[deng-2024-radio-map-uav-pickup-delivery]]"
  - "[[huang-2026-hgadrl-cargo-uav-pickup-delivery]]"
created: 2026-07-13
updated: 2026-11-02
---

# Radio-Map-Aided UAV Path Planning

Radio-map-aided UAV path planning uses a location-indexed channel or SNR map as a movement-feasibility layer. The planner associates each position with its best terrestrial base station, removes positions whose expected link quality falls below a threshold, and searches the remaining space for a communication-safe path. It therefore consumes a radio map to guide movement rather than using one to estimate the current channel, which is the role captured by [[radio-map-assisted-channel-estimation]].

In [[cao-2026-radio-map-cargo-pickup]], a physical-map-derived expected-SNR grid is thresholded into feasible and infeasible cells. Eight-neighbor A* computes all-pairs warehouse/pickup paths, and the resulting distance matrix feeds a cargo-allocation optimizer. This approach gives deterministic offline paths when the map is accurate; the paper leaves stochastic channel variation, handover delay, the map-resolution/computational-complexity tradeoff, and full 3-D paths for future work.

[[guo-2026-event-triggered-sinr-navigation]] adds online map maintenance and learned navigation. Its [[uncertainty-triggered-radio-map-update]] refreshes coarse/global and fine/local SINR grids only when MC-dropout variance crosses a threshold, exposing a freshness-versus-downlink-traffic tradeoff.

[[deng-2024-radio-map-uav-pickup-delivery]] uses a Dijkstra variant that adds interruption time to edge weights, so the all-pairs matrix behind its pickup-and-delivery genetic algorithm already favors reliable links. [[peng-2025-cargo-uav-energy-outage-tradeoff]] and [[huang-2026-hgadrl-cargo-uav-pickup-delivery]] instead train dueling DDQN agents on outage-probability maps: the first weights expected outage time in the objective, while the second imposes a per-position outage threshold. When the cost is the number of cell changes rather than map quality, the design becomes [[handoff-aware-uav-trajectory-planning]].
