---
type: concept
title: "Sensing-Feasible UAV Reachability"
tags: [isac, feasibility, uav-trajectory, graph-reachability, semidefinite-programming]
related:
  - "[[lyu-2023-isac-maneuver-beamforming]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[uav-trajectory-control]]"
created: 2026-07-13
updated: 2026-07-13
---

# Sensing-Feasible UAV Reachability

A two-step mission-feasibility construction for UAV-ISAC. First, a sensing-only semidefinite program marks candidate UAV locations where a transmit covariance can satisfy all illumination constraints under the power budget. Second, a graph connects feasible locations that are within one-slot movement distance, allowing endpoint reachability to be tested before communication-rate optimization.

[[lyu-2023-isac-maneuver-beamforming]] uses depth-first search on this graph. Connectivity is necessary for a feasible maneuver, but the paper's argument does not explicitly prove that the connecting path fits the finite number of mission slots; graph reachability and time-budget feasibility should therefore remain distinct claims.
