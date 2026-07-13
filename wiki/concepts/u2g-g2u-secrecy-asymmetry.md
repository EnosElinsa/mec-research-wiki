---
type: concept
title: "U2G-G2U Secrecy Asymmetry"
tags: [physical-layer-security, uav, channel-geometry, trajectory-optimization]
related:
  - "[[zhang-2019-secure-uav-trajectory-power]]"
  - "[[physical-layer-security]]"
  - "[[uav-trajectory-control]]"
  - "[[micro-macro-mobility-security]]"
created: 2026-07-14
updated: 2026-07-14
---

# U2G-G2U Secrecy Asymmetry

The direction-dependent effect of UAV motion on a secrecy link. In UAV-to-ground transmission, moving the UAV can change both the legitimate air-ground channel and the UAV-to-eavesdropper channel. In ground-to-UAV transmission with a fixed ground eavesdropper, the same motion changes only the legitimate ground-air channel because the ground-to-ground eavesdropper link is independent of UAV position.

[[zhang-2019-secure-uav-trajectory-power]] makes this asymmetry explicit. Its U2G design uses trajectory and UAV transmit power to shape both rate terms, whereas its G2U design uses trajectory to improve the legitimate link and ground-node power to manage both rate terms. Under the paper's model, trajectory therefore has less secrecy leverage in G2U, and the optimized path can coincide with a best-effort path toward the legitimate ground node.

This is a channel-model result, not a universal property of uplink secrecy. It depends on a fixed ground eavesdropper, a trajectory-independent ground-ground channel, known locations, fixed altitude, and the paper's LoS/fading assumptions. It complements the broader macro-mobility treatment in [[micro-macro-mobility-security]] rather than duplicating that general use of UAV motion.
