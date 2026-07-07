---
type: concept
title: "UAV Delivery Pickup/Drop-Off Optimization"
tags: [uav, delivery, trajectory-optimization, logistics, no-fly-zone]
related:
  - "[[uav-trajectory-control]]"
  - "[[rotary-wing-propulsion-energy-model]]"
  - "[[energy-latency-tradeoff]]"
  - "[[compliance-aware-uav-trajectory]]"
  - "[[lee-2026-uav-delivery-time-energy]]"
  - "[[chen-2026-cargo-uav-pickup-lae]]"
created: 2026-07-07
updated: 2026-07-07
---

# UAV Delivery Pickup/Drop-Off Optimization

UAV delivery pickup/drop-off optimization jointly chooses where and when a delivery UAV visits pickup and delivery zones, how it moves in 3-D space, and how it trades mission completion time against propulsion energy. It differs from UAV communication placement because the UAV physically carries payloads: item weight changes propulsion cost, and pickup/drop-off order can dominate the route.

In [[lee-2026-uav-delivery-time-energy]], the problem is formulated with no-fly-zone avoidance, weight restrictions, variable slot lengths, 3-D trajectories, and binary pickup/drop-off indicators. The solver uses SCA plus a penalty convex-concave procedure, and the reported tradeoff is explicit: energy minimization saves more than 20% energy at about 10% longer completion time.

In this wiki the concept sits near [[chen-2026-cargo-uav-pickup-lae]] and [[compliance-aware-uav-trajectory]], but it is logistics/control infrastructure rather than MEC offloading.
