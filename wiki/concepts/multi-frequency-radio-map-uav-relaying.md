---
type: concept
title: "Multi-Frequency Radio-Map UAV Relaying"
tags: [radio-map, uav-relay, device-to-device, terrain-aware-channel, frequency-selection]
related:
  - "[[dong-2026-radio-map-d2d-relay]]"
  - "[[device-to-device-communication]]"
  - "[[terrain-aware-channel-model]]"
  - "[[radio-map-aided-uav-path-planning]]"
  - "[[radio-map-assisted-channel-estimation]]"
created: 2026-07-13
updated: 2026-07-13
---

# Multi-Frequency Radio-Map UAV Relaying

Multi-frequency radio-map UAV relaying uses location- and band-indexed propagation maps to decide which ground gateways connect to which aerial relays, at which frequencies, and where those relays should hover. Lower bands can reach terrain-shadowed users with less attenuation, while wider high-frequency bands offer more throughput in favorable geometry.

[[dong-2026-radio-map-d2d-relay]] constructs Longley-Rice maps from real terrain data, selects one gateway per [[device-to-device-communication|D2D]] subnetwork by map-weighted closeness centrality, and replaces Euclidean k-means with rate-based assignment and grid-position updates. This consumes maps for topology and placement, rather than channel estimation or movement-path feasibility.
