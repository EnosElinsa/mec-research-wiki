---
type: concept
title: "Fractional Power Control"
tags: [power-control, cellular-uplink, interference-management, uav]
related:
  - "[[azari-2020-uav-to-uav-cellular]]"
  - "[[channel-inversion-power-control]]"
  - "[[uav-to-uav-communication]]"
created: 2026-07-14
updated: 2026-07-14
---

# Fractional Power Control

An uplink power rule that compensates only a fraction of large-scale path loss, usually through an exponent between zero and one and a maximum transmit-power cap. Zero compensation keeps power nearly constant; full compensation approaches channel inversion until the cap binds.

In [[azari-2020-uav-to-uav-cellular]], the compensation factor controls the U2U reliability versus ground-uplink interference tradeoff. Shorter aerial links need less power and can improve both tiers, while aggressive compensation eventually saturates as UAV transmitters reach their cap.
