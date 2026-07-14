---
type: concept
title: "Dynamic-Programming Battery-Station Insertion"
tags: [dynamic-programming, battery-swapping, uav-routing, energy-constraints]
related:
  - "[[chang-2026-data-offloading-energy-constraints]]"
  - "[[battery-swapping-uav-mec]]"
  - "[[many-to-one-pickup-and-delivery]]"
  - "[[samir-2020-time-constrained-data-collection]]"
  - "[[deadline-constrained-uav-data-collection]]"
  - "[[branch-reduce-and-bound]]"
  - "[[constraint-regimes-in-uav-data-collection]]"
created: 2026-07-14
updated: 2026-07-14
---

# Dynamic-Programming Battery-Station Insertion

Given a fixed service order, this method selects replenishment-station identities and insertion positions so each route segment fits within battery capacity while added travel and replacement delay are minimized. The dynamic program optimizes station placement for that order, not the underlying service order.

[[chang-2026-data-offloading-energy-constraints]] applies the method after constructing a pickup-before-delivery route, then iterates route refinement and station reinsertion. Its model resets the UAV to full energy after a constant replacement delay.
