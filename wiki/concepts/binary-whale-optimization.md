---
type: concept
title: "Binary Whale Optimization Algorithm (BWOA)"
tags: [metaheuristic, binary-optimization, swarm-intelligence, integer-programming]
related:
  - "[[multi-verse-optimizer]]"
  - "[[matching-theory-for-resource-allocation]]"
  - "[[jia-2025-dro-uav-hap-mec]]"
created: 2026-05-29
updated: 2026-05-29
---

# Binary Whale Optimization Algorithm (BWOA)

A binary-variable adaptation of the whale optimization algorithm (WOA), itself inspired by humpback whale bubble-net feeding behavior. Original WOA is a continuous metaheuristic with three operators: *encircling prey*, *bubble-net spiral attack*, and *prey search*. BWOA discretizes by mapping the continuous position update through a sigmoid (S-shape) or tanh (V-shape) and thresholding.

Used in [[jia-2025-dro-uav-hap-mec]] for the binary task-offloading subproblem (which task goes to which UAV vs the HAP) after primal decomposition reduces the original MISOCP. Justified empirically against greedy and pure-GA baselines.

Sits in the same family as [[multi-verse-optimizer]] (used in [[liu-2025-haps-uav-maritime-iot]]) — different swarm metaphors, similar role: cheap binary search when the structure doesn't yield to convex relaxation.
