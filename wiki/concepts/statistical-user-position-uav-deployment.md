---
type: concept
title: "Statistical User-Position UAV Deployment"
tags: [uav-deployment, location-uncertainty, user-density, resource-allocation]
related:
  - "[[device-association]]"
  - "[[uav-mobile-relaying]]"
  - "[[chai-2026-random-position-relay-deployment]]"
  - "[[two-regime-aerial-user-association]]"
  - "[[cell-free-uav-predictive-beamforming]]"
  - "[[mobility-asynchrony-and-geometry-in-aerial-coverage]]"
created: 2026-07-14
updated: 2026-07-14
---

# Statistical User-Position UAV Deployment

Planning aerial relay or access-point locations from a probability density over user positions rather than a deterministic coordinate list. Expected rate, delay, or coverage is integrated over the density, allowing deployment before exact users are observed.

[[chai-2026-random-position-relay-deployment]] uses a truncated Gaussian density to score relay-UAV placement and power. Its later association routine nevertheless assumes explicit user coordinates, exposing an important implementation boundary between statistical planning and online assignment.
