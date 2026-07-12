---
type: concept
title: "Optimal Transport Theory"
tags: [optimization, assignment, resource-allocation, association]
related:
  - "[[device-association]]"
  - "[[matching-theory-for-resource-allocation]]"
  - "[[generalized-assignment-problem]]"
  - "[[gao-2026-fmad3qn-uav-gd-association]]"
  - "[[mozaffari-not-in-parse-3d-drone-cellular-network]]"
created: 2026-07-07
updated: 2026-07-11
---

# Optimal Transport Theory

An optimization framework for moving mass from one distribution to another at minimum cost. In resource-allocation language, it can turn many association or assignment problems into structured transport problems, often revealing integrality or closed-form properties that are hidden in a direct combinatorial formulation.

In [[gao-2026-fmad3qn-uav-gd-association]], optimal transport theory is used with Lagrangian duality to derive a closed-form ground-device association rule for multi-UAV MEC. That rule replaces exhaustive association search inside a federated dueling-DDQN 3D deployment controller, reducing association complexity from exponential in the number of devices to O(KU) under the paper's model.

[[mozaffari-not-in-parse-3d-drone-cellular-network]] uses optimal transport for a non-MEC aerial-cellular association problem: drone-UE mass is partitioned among drone-BS cells to minimize transmission, backhaul, and computation latency rather than only maximize SINR.

It is adjacent to [[matching-theory-for-resource-allocation]] and [[generalized-assignment-problem]], but the emphasis is different: matching pages usually model stable or preference-based pairings, while optimal transport emphasizes minimum-cost mass movement and dual potentials.
