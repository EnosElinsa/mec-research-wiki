---
type: concept
title: "Reservation-Based Density-Aware 4-D UAV Planning"
tags: [urban-air-mobility, trajectory-planning, air-traffic-management, chance-constraint, robust-mpc]
related:
  - "[[vitale-2026-density-aware-4d-trajectory]]"
  - "[[urban-air-mobility]]"
  - "[[uav-trajectory-control]]"
  - "[[chance-constraint]]"
  - "[[target-level-of-safety]]"
  - "[[compliance-aware-uav-trajectory]]"
created: 2026-07-12
updated: 2026-07-12
---

# Reservation-Based Density-Aware 4-D UAV Planning

Reservation-based density-aware 4-D UAV planning assigns a spatial route and occupancy times through capacity-limited airspace. In [[vitale-2026-density-aware-4d-trajectory]], the strategic ICPP schedules departure, route, and arrival-time QoS under cube-capacity constraints, while a separate intra-cube MPC layer handles pairwise collision risk during execution.

[[vitale-2026-density-aware-4d-trajectory]] uses a centralized reverse-time graph search to reserve cube-time slots and a distributed robust-MPC layer to execute each reservation. The local controller exchanges predicted Gaussian trajectories and conservatively transforms pairwise separation [[chance-constraint|chance constraints]] into deterministic distance constraints.

The pattern depends on the spatial and temporal discretization, reservation-duration model, and reliability of local state exchange. Its capacity setting and probabilistic guarantee do not transfer unchanged to a new airspace geometry or disturbance model; positive safety slack also indicates that the strict risk target is temporarily infeasible.
