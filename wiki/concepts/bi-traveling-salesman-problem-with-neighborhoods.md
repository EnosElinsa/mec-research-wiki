---
type: concept
title: "Bi-Traveling Salesman Problem With Neighborhoods"
tags: [trajectory-optimization, uav-usv, maritime, routing, energy-efficiency]
related:
  - "[[zhang-2026-air-sea-isac-inspection]]"
  - "[[successive-hover-and-fly-trajectory]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[uav-usv-cooperative-mec]]"
  - "[[alternating-optimization-sdr-sca]]"
created: 2026-07-13
updated: 2026-07-13
---

# Bi-Traveling Salesman Problem With Neighborhoods

A heterogeneous two-vehicle routing problem in which the number, positions, visit order, and dwell times of feasible service neighborhoods are jointly selected. In [[zhang-2026-air-sea-isac-inspection]], sensing radii and UAV-USV communication distance define the neighborhoods, while each directed edge carries a joint aerial/marine energy cost that depends on UAV motion and position-dependent water current.

The paper solves this Bi-TSPN approximately through target clustering, an open-loop hybrid-cost TSP, and continuous SCA refinement. It differs from an ordinary TSPN because both vehicles must remain coupled and arrive together despite different dynamics and energy models.
