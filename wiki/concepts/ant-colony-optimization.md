---
type: concept
title: "Ant Colony Optimization (ACO)"
tags: [optimization, swarm-intelligence, metaheuristic, routing]
related:
  - "[[mao-2024-ntn-hierarchical-caching-cav]]"
  - "[[particle-swarm-optimization]]"
  - "[[swarm-metaheuristics-in-uav-mec]]"
created: 2026-05-29
updated: 2026-06-03
---

# Ant Colony Optimization (ACO)

A swarm-intelligence metaheuristic inspired by ants depositing pheromone along paths: good (short/low-cost) paths accumulate more pheromone and are reinforced, biasing the colony toward high-quality solutions over time. ACO is well suited to combinatorial problems with a graph/path structure (routing, selection, assignment).

In [[mao-2024-ntn-hierarchical-caching-cav]], a **Delay-Motivated ACO (DM-ACO)** selects which LEO satellites should cache content so as to minimize system propagation delay (avoiding the duplication/interference of caching on every satellite). ACO belongs to the same swarm-metaheuristic family as [[particle-swarm-optimization]].
