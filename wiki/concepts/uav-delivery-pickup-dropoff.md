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
  - "[[jiang-2026-bi-level-uav-delivery-safety]]"
  - "[[target-level-of-safety]]"
  - "[[gao-2026-air-ground-instant-delivery]]"
  - "[[cooperative-uav-taxi-delivery]]"
  - "[[chen-not-in-parse-uav-human-medical-delivery]]"
  - "[[cooperative-uav-human-courier-delivery]]"
  - "[[zhou-2026-multiscale-dt-uav-delivery]]"
  - "[[cao-2026-radio-map-cargo-pickup]]"
  - "[[radio-map-aided-uav-path-planning]]"
created: 2026-07-07
updated: 2026-07-13
---

# UAV Delivery Pickup/Drop-Off Optimization

UAV delivery pickup/drop-off optimization jointly chooses where and when a delivery UAV visits pickup and delivery zones, how it moves in 3-D space, and how it trades mission completion time against propulsion energy. It differs from UAV communication placement because the UAV physically carries payloads: item weight changes propulsion cost, and pickup/drop-off order can dominate the route.

In [[lee-2026-uav-delivery-time-energy]], the problem is formulated with no-fly-zone avoidance, weight restrictions, variable slot lengths, 3-D trajectories, and binary pickup/drop-off indicators. The solver uses SCA plus a penalty convex-concave procedure, and the reported tradeoff is explicit: energy minimization saves more than 20% energy at about 10% longer completion time.

[[jiang-2026-bi-level-uav-delivery-safety]] adds the safety-constrained logistics variant: heterogeneous UAVs receive order assignments through TC-NSGA-III, while RG-FMT* plans delivery paths whose waypoint risk remains below [[target-level-of-safety|TLS]].

[[gao-2026-air-ground-instant-delivery]] adds [[cooperative-uav-taxi-delivery]], where UAV station placement and repositioning fill the time-varying delivery capacity left by crowdsourced taxis, and parcel assignment combines learned courier preferences with generalized assignment.

[[chen-not-in-parse-uav-human-medical-delivery]] adds [[cooperative-uav-human-courier-delivery]] for emergency medical pickup and delivery. It jointly assigns orders and routes a dedicated courier/UAV fleet under soft deadlines, type-specific capacities, and different consolidation rules.

[[cao-2026-radio-map-cargo-pickup]] adds offline expected-SNR-map feasibility, all-pairs A* paths, PSO trip allocation, and payload-dependent speed selection. [[chen-2026-cargo-uav-pickup-lae]] instead learns communication-aware paths from local measurements and adds multi-UAV conflict resolution. In this wiki the concept remains logistics/control infrastructure rather than MEC offloading.
