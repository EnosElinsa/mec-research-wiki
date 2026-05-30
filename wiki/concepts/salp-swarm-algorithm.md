---
type: concept
title: "Salp Swarm Algorithm (SSA)"
tags: [swarm-intelligence, metaheuristic, multi-objective, evolutionary, optimization]
related:
  - "[[particle-swarm-optimization]]"
  - "[[whale-optimization-algorithm]]"
  - "[[multi-verse-optimizer]]"
  - "[[collaborative-beamforming]]"
  - "[[li-2024-emssa-uav-swarm-vaa]]"
created: 2026-05-31
updated: 2026-05-31
---

# Salp Swarm Algorithm (SSA)

A swarm-intelligence metaheuristic inspired by the chain-formation behavior of salps in the ocean. The population is split into a **leader** (which guides the search toward the current best) and a chain of **followers** (which update relative to the salp ahead of them). The multi-objective variant (MSSA) maintains an **archive** of non-dominated solutions, pruned via a hypercube mechanism to keep diversity along the Pareto front.

## In this wiki

- [[li-2024-emssa-uav-swarm-vaa]] proposes **EMSSA** (enhanced multi-objective SSA), improving the conventional MSSA's **solution initialization**, **solution update**, and **algorithm-parameter update** phases so it can handle the mixed-variable, large-scale, NP-hard MOP arising from joint ground+aerial [[collaborative-beamforming]] (minimizing completion time, eavesdropper signal strength, and UAV energy). It reports outperforming other multi-objective swarm-intelligence baselines.

Sits alongside the corpus's other nature-inspired optimizers — [[particle-swarm-optimization]], [[whale-optimization-algorithm]], [[multi-verse-optimizer]] — as a population-based alternative to DRL for multi-objective UAV problems.
