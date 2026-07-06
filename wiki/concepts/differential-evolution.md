---
type: concept
title: "Differential Evolution (DE)"
tags: [optimization, evolutionary-algorithm, metaheuristic]
related:
  - "[[wang-2019-todetas-deployment-scheduling]]"
  - "[[constrained-multi-objective-evolutionary-algorithm]]"
  - "[[particle-swarm-optimization]]"
  - "[[liao-2025-ris-uav-usv-resource-allocation]]"
created: 2026-05-29
updated: 2026-07-07
---

# Differential Evolution (DE)

A population-based evolutionary optimizer that generates trial solutions by adding scaled differences between population members (mutation), recombining them (crossover), and selecting greedily. It is effective for continuous, non-convex problems and easy to hybridize with problem-specific operators.

In [[wang-2019-todetas-deployment-scheduling]], DE is the upper-layer search engine for UAV deployment: each individual encodes a UAV location, the population an entire deployment, and an **elimination operator** adaptively reduces the number of UAVs until tasks can no longer meet delay constraints. DE belongs to the same evolutionary-computation family as the CMOP methods ([[constrained-multi-objective-evolutionary-algorithm]]) and metaheuristics like [[particle-swarm-optimization]].

[[liao-2025-ris-uav-usv-resource-allocation]] uses multi-objective differential evolution (MODE) for the continuous subproblem that jointly chooses UAV hovering coordinates and RIS phase shifts in a RIS-assisted UAV-USV cooperative MEC architecture.
