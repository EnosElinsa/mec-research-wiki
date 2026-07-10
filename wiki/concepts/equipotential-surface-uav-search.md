---
type: concept
title: "Equipotential-Surface UAV Search"
tags: [uav, trajectory-optimization, channel-estimation, line-of-sight, low-altitude-economy]
related:
  - "[[zheng-2026-active-search-low-altitude-uav]]"
  - "[[drone-cell-3d-placement]]"
  - "[[radio-map-assisted-channel-estimation]]"
  - "[[air-to-ground-channel-model]]"
  - "[[uav-trajectory-control]]"
  - "[[wireless-backhaul]]"
created: 2026-07-10
updated: 2026-07-10
---

# Equipotential-Surface UAV Search

Equipotential-surface UAV search is an online placement pattern where the UAV constrains its exploration to positions that balance access-link service and backhaul quality. Instead of sweeping the full 3-D volume, the UAV follows a lower-dimensional surface and uses local channel measurements to decide where the surface can be followed safely.

In [[zheng-2026-active-search-low-altitude-uav]], the surface balances BS-UAV and UAV-user objectives under unknown user locations and unknown urban propagation. The UAV builds local LoS channel estimates while flying, so the concept sits between [[drone-cell-3d-placement]], [[radio-map-assisted-channel-estimation]], and [[uav-trajectory-control]].
