---
type: concept
title: "Gravitational Search Algorithm (GSA)"
tags: [metaheuristic, optimization, multi-objective, swarm-intelligence]
related:
  - "[[multi-verse-optimizer]]"
  - "[[salp-swarm-algorithm]]"
  - "[[whale-optimization-algorithm]]"
  - "[[constrained-multi-objective-evolutionary-algorithm]]"
  - "[[mixed-integer-nonlinear-programming]]"
  - "[[collaborative-beamforming]]"
  - "[[zheng-2024-recmop-uav-cb]]"
  - "[[swarm-metaheuristics-in-uav-mec]]"
created: 2026-06-01
updated: 2026-06-03
---

# Gravitational Search Algorithm (GSA)

A population-based **metaheuristic** in which candidate solutions are treated as **agents (masses)** that attract one another by a simulated law of gravity: the force on an agent is a randomly-weighted sum of the gravitational pull of the others, so heavier (better-fitness) masses move slowly and pull lighter ones toward promising regions. The gravitational "constant" decays over iterations to shift from exploration to exploitation. Because each agent's motion integrates contributions from many others rather than tracking only a global/individual best, GSA is argued to be **less prone to premature local-optimum trapping** and to need **few control parameters**.

## In this wiki

- [[zheng-2024-recmop-uav-cb]] selects GSA as the base framework for its **improved multi-objective GSA (IMOGSA)**, motivated explicitly against the alternatives: unlike DRL it needs no costly model training (UAVs run the solver), and unlike convex optimization it does not transform/distort the original solution space. To handle the NP-hard, large-scale, **mixed continuous/discrete** RECMOP (UAV locations + excitation weights), IMOGSA adds three designs — **quasi-opposition based learning** (better initial solutions), a **discrete solution update strategy** (discrete dimensions), and an **NSGA-II-style archive optimization method** (crossover/mutation to refine the Pareto archive).

GSA sits alongside the corpus's other mixed-variable metaheuristics for aerial multi-objective problems — the [[multi-verse-optimizer]] (used for the hovering-vs-motion-energy CB problem), the [[salp-swarm-algorithm]] (secure/data-collection CB), and the [[whale-optimization-algorithm]] — all chosen to emit a one-run Pareto set for NP-hard [[mixed-integer-nonlinear-programming]] formulations.
