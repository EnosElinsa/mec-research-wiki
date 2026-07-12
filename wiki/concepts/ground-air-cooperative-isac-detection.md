---
type: concept
title: "Ground-Air Cooperative ISAC Detection"
tags: [isac, cellular-connected-uav, cooperative-sensing, data-fusion, target-detection]
related:
  - "[[wang-2025-cellular-uav-cooperative-detection]]"
  - "[[cellular-connected-uav]]"
  - "[[multi-source-data-fusion]]"
  - "[[networked-isac]]"
  - "[[integrated-sensing-and-communication]]"
created: 2026-07-13
updated: 2026-07-13
---

# Ground-Air Cooperative ISAC Detection

An asymmetric cooperative-sensing architecture in which a terrestrial base station and a cellular-connected UAV observe the same aerial targets, associate their target-level measurements, and centrally fuse target state before adapting communication and mobility.

In [[wang-2025-cellular-uav-cooperative-detection]], the BS supplies strong fixed infrastructure while the UAV supplies mobile LoS geometry. Normalized position/motion distance associates observations, an EKF performs [[multi-source-data-fusion]], and the fused state guides alternating beamforming and trajectory updates. This differs from multi-BS [[networked-isac]] and from fixed anti-UAV transceiver cooperation.
