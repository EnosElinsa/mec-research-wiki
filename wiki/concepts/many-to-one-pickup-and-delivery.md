---
type: concept
title: "Many-to-One Pickup-and-Delivery Routing"
tags: [routing, precedence-constraints, data-collection, edge-server]
related:
  - "[[chang-2026-data-offloading-energy-constraints]]"
  - "[[uav-data-collection]]"
  - "[[dynamic-programming-battery-station-insertion]]"
  - "[[generalized-traveling-salesman-problem]]"
  - "[[samir-2020-time-constrained-data-collection]]"
  - "[[deadline-constrained-uav-data-collection]]"
  - "[[constraint-regimes-in-uav-data-collection]]"
created: 2026-07-14
updated: 2026-07-14
---

# Many-to-One Pickup-and-Delivery Routing

A precedence-constrained route in which several pickup nodes map to one designated delivery node and every pickup in that group must be visited before its delivery. Multiple groups create overlapping routing choices even when assignments are fixed.

[[chang-2026-data-offloading-energy-constraints]] uses IoT devices as pickup nodes and predetermined edge servers as delivery nodes. The UAV must collect every device's data before visiting its server, while battery-station detours add a second route-feasibility layer.
