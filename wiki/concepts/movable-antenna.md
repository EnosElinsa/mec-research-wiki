---
type: concept
title: "Movable Antenna"
tags: [antenna, mimo, channel-modeling, low-altitude-economy]
related:
  - "[[zeng-2026-movable-antenna-u2u-channel]]"
  - "[[lu-2026-uav-swarm-two-level-ma]]"
  - "[[two-level-movable-antenna]]"
  - "[[extremely-large-scale-mimo]]"
  - "[[near-field-communications]]"
  - "[[low-altitude-intelligent-network]]"
  - "[[mozaffari-2019-drone-antenna-array]]"
created: 2026-07-07
updated: 2026-07-07
---

# Movable Antenna

A movable antenna places each radiating element on a mechanically adjustable position within a bounded region, so the array can exploit local spatial channel variation rather than being fixed to one geometry. The same idea is also discussed in the literature as a fluid-antenna-style reconfigurable antenna system.

In [[zeng-2026-movable-antenna-u2u-channel]], movable antennas are applied to UAV-to-UAV MIMO wideband channels for low-altitude economy networks. The paper derives closed-form channel-correlation statistics and then optimizes antenna positions by maximizing the log-determinant of spatial correlation matrices under movement-region and minimum-spacing constraints.

[[lu-2026-uav-swarm-two-level-ma]] extends the idea into [[two-level-movable-antenna]] design: UAV positions form a swarm-level movable array, while each UAV also carries locally movable elements. Together these sources connect reconfigurable physical-layer hardware to [[low-altitude-intelligent-network]], [[extremely-large-scale-mimo]], and [[near-field-communications]], while remaining distinct from drone-swarm virtual arrays such as [[mozaffari-2019-drone-antenna-array]].
