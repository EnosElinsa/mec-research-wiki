---
type: concept
title: "Aerial Active-RIS Backhaul"
tags: [active-ris, wireless-backhaul, uav-bs, aerial-base-station]
related:
  - "[[jeon-2026-ampli-flection-aerial-backhaul]]"
  - "[[active-ris]]"
  - "[[wireless-backhaul]]"
  - "[[drone-cell-3d-placement]]"
  - "[[intelligent-reflecting-surface]]"
created: 2026-07-11
updated: 2026-07-11
---

# Aerial Active-RIS Backhaul

Aerial active-RIS backhaul places an amplifying reconfigurable surface on a high-altitude aerial platform so blocked ground infrastructure can reach UAV base stations through a controllable reflected path. The active-RIS elements add gain to fight the multiplicative fading of a long source-RIS-destination cascade, while also consuming power and injecting dynamic noise.

In [[jeon-2026-ampli-flection-aerial-backhaul]], the backhaul source serves multiple UAV-BSs through an aerial active RIS when the direct path is blocked. The key design variables are the aerial platform location, RIS array partitioning, phase alignment point, and equal amplification gain. Unlike [[drone-cell-3d-placement]], which chooses where UAV-BSs serve ground users, this concept controls the upper-tier [[wireless-backhaul]] that keeps those UAV-BSs connected.

The useful distinction from passive [[intelligent-reflecting-surface|RIS]] backhaul is the power tradeoff: amplification can cut transmit power, but the surface's active hardware, reflection power, and dynamic noise must be included before calling the design energy-efficient.
