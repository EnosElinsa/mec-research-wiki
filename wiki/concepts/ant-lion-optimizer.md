---
type: concept
title: "Ant Lion Optimizer (ALO)"
tags: [swarm-intelligence, metaheuristic, multi-objective, evolutionary, optimization]
related:
  - "[[sun-2021-temcmop-uav-cb]]"
  - "[[particle-swarm-optimization]]"
  - "[[salp-swarm-algorithm]]"
  - "[[multi-verse-optimizer]]"
  - "[[whale-optimization-algorithm]]"
  - "[[collaborative-beamforming]]"
  - "[[swarm-metaheuristics-in-uav-mec]]"
created: 2026-06-02
updated: 2026-06-03
---

# Ant Lion Optimizer (ALO)

A swarm-intelligence metaheuristic that mimics the hunting behavior of **antlions** and their prey (ants). Candidate solutions ("ants") perform random walks while "antlions" build traps that bias the walks toward promising regions; elitism keeps the best antlion influencing the population. The multi-objective variant (**MOALO**) maintains an archive of non-dominated solutions to approximate the Pareto front in a single run, the way other multi-objective swarm methods do.

ALO, like the corpus's other nature-inspired optimizers, is attractive for **mixed-variable, large-scale, NP-hard** problems where it returns a Pareto set in one run (a decision-maker picks a trade-off afterward) and does not require gradients or convexity — but standard MOALO struggles when the solution space mixes continuous and discrete dimensions.

## In this wiki

[[sun-2021-temcmop-uav-cb]] proposes **IMOALO** (improved multi-objective ALO) to solve the time/VAA-time/energy multi-objective problem of UAV [[collaborative-beamforming]]. It adds two improvements over conventional MOALO: **chaos + opposition-based-learning (chaos-OBL)** initialization to raise initial-solution quality, and a **hybrid solution-update operator** to handle the mixed continuous (positions, speeds, weights) + discrete (base-station serving order) solution space. It reports the overall best performance across the three objectives versus baselines including MOPSO, NSGA-II, and conventional MOALO. ALO sits alongside the [[salp-swarm-algorithm]], [[multi-verse-optimizer]], [[whale-optimization-algorithm]], and [[particle-swarm-optimization]] as a population-based alternative to DRL for multi-objective UAV beamforming.
