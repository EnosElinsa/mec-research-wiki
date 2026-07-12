---
type: concept
title: "Dual-Network Sequential AoI Control"
tags: [aoi, uav, wireless-power-transfer, multi-agent-drl, value-factorization]
related:
  - "[[wang-2026-glint-aoi-wireless-powered-edge]]"
  - "[[age-of-information]]"
  - "[[wireless-power-transfer]]"
  - "[[rf-energy-harvesting]]"
  - "[[uav-data-collection]]"
  - "[[uav-trajectory-control]]"
  - "[[device-association]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[maddpg]]"
created: 2026-07-12
updated: 2026-07-12
---

# Dual-Network Sequential AoI Control

Dual-network sequential AoI control decomposes a large mixed UAV freshness problem into ordered policies whose outputs constrain the next decision stage. Mobility and association are resolved first; wireless-power time and sensor transmission scheduling then operate on the resulting coverage and energy state.

In [[wang-2026-glint-aoi-wireless-powered-edge]], each UAV runs two actors. The first chooses 3D position and delegates binary [[device-association]] to path-loss matching. The second chooses discretized WPT time and sensor transmissions. Local critics are combined by a monotonic mixer during centralized training, while execution uses only local observations and the two actors in sequence.

The decomposition reduces the binary action explosion, but it is approximate: the first stage uses prior-slot WPT allocation and candidate-sensor indicators rather than the exact downstream AoI objective. Its benefit is tractable multi-UAV control, not a proof of global optimality for the original MINLP.
