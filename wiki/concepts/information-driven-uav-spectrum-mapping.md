---
type: concept
title: "Information-Driven UAV Spectrum Mapping"
tags: [spectrum-mapping, uav, informative-path-planning, sparse-bayesian-learning]
related:
  - "[[wang-2026-bayesian-uav-spectrum-mapping]]"
  - "[[temporal-spectrum-cartography]]"
  - "[[radio-map-assisted-channel-estimation]]"
  - "[[spectrum-sensing-channel-selection]]"
  - "[[uav-trajectory-control]]"
  - "[[chakraborty-2026-skyscale-rti-deployment]]"
created: 2026-07-11
updated: 2026-07-14
---

# Information-Driven UAV Spectrum Mapping

Information-driven UAV spectrum mapping treats a UAV as an active sensor for radio environment map construction. The UAV does not merely follow a grid or a preplanned route; it chooses measurements that are expected to reduce map uncertainty under flight, sensing, and obstacle constraints.

In [[wang-2026-bayesian-uav-spectrum-mapping]], the planner is 3DIG-RRT*: an information-gathering RRT* variant that searches feasible 3-D paths with a mutual-information utility. The reconstruction side uses sparse Bayesian dictionary learning plus Gaussian-process shadow-fading refinement, so sampling and inference are coupled around the same uncertainty structure.

This differs from [[temporal-spectrum-cartography]], which emphasizes time-varying RF-map reconstruction from sparse static/mobile sensors, and from [[radio-map-assisted-channel-estimation]], where the map is used as a prior for channel estimation. Here the radio/spectrum map itself is the product being learned.
