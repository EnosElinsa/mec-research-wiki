---
type: concept
title: "Mixed-Integer Linear Programming"
tags: [optimization, integer-programming, linear-programming]
related:
  - "[[chang-2026-data-offloading-energy-constraints]]"
  - "[[linear-programming]]"
  - "[[mixed-integer-nonlinear-programming]]"
  - "[[transformer-weighted-a-star-trajectory-planning]]"
  - "[[branch-reduce-and-bound]]"
  - "[[opportunistic-cooperative-multi-uav-ddqn]]"
  - "[[constraint-regimes-in-uav-data-collection]]"
created: 2026-07-14
updated: 2026-07-14
---

# Mixed-Integer Linear Programming

Optimization with a linear objective and linear constraints in which some variables are restricted to integer or binary values. MILP can represent routing, assignment, precedence, and logical implications exactly, but general instances are NP-hard and often require branch-and-bound or decomposition.

[[chang-2026-data-offloading-energy-constraints]] formulates UAV pickup/delivery routing and repeated battery-station visits as a MILP using binary route edges, MTZ order variables, and energy-state constraints. Dummy station nodes make repeated visits expressible but enlarge the model substantially.
