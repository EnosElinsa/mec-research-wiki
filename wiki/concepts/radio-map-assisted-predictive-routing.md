---
type: concept
title: "Radio-Map-Assisted Predictive Routing"
tags: [radio-map, predictive-communication, routing, low-altitude-network]
related:
  - "[[li-2026-radio-map-predictive-routing]]"
  - "[[dynamic-space-time-graph-with-virtual-edges]]"
  - "[[radio-map-assisted-channel-estimation]]"
  - "[[radio-map-aided-uav-path-planning]]"
  - "[[graph-based-resource-management]]"
created: 2026-07-14
updated: 2026-07-14
---

# Radio-Map-Assisted Predictive Routing

Radio-map-assisted predictive routing queries location-indexed large-scale channel and interference statistics along known future node trajectories, then plans how data should move through the resulting time-varying network. The UAV paths are inputs; the optimized object is the data route together with hop timing and transmit resources.

In [[li-2026-radio-map-predictive-routing]], these predictions parameterize interference-weighted edges in a [[dynamic-space-time-graph-with-virtual-edges]]. This differs from [[radio-map-aided-uav-path-planning]], which uses a map to choose the vehicle's own path, and from [[radio-map-assisted-channel-estimation]], which fuses map priors with current channel observations.
