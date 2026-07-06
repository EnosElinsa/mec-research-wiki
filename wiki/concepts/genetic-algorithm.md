---
type: concept
title: "Genetic Algorithm"
tags: [optimization, evolutionary, metaheuristic, deployment]
related:
  - "[[non-dominated-sorting-genetic-algorithm]]"
  - "[[constrained-multi-objective-evolutionary-algorithm]]"
  - "[[two-stage-decomposition]]"
  - "[[zhao-2026-hcdrl-ga-sagin-sar]]"
created: 2026-07-07
updated: 2026-07-07
---

# Genetic Algorithm

An evolutionary metaheuristic that represents candidate solutions as chromosomes and iteratively applies selection, crossover, mutation, and elitism-style retention to improve a fitness score. In this wiki it is most useful when the decision is combinatorial or deployment-like, and the candidate can be evaluated by a simulator, solver, or learned policy rather than by a closed-form objective.

In [[zhao-2026-hcdrl-ga-sagin-sar]], GA searches UAV takeoff/recovery deployment configurations. Each candidate deployment is evaluated through rollouts of a trained HCDRL/HCSAC policy, so the GA acts as a low-frequency mission-planning layer while DRL handles online trajectory and offloading.

This is related to [[non-dominated-sorting-genetic-algorithm]], which explicitly maintains a Pareto front for multi-objective search. The SAGIN SAR paper uses a normalized weighted-sum fitness for one executable deployment and names Pareto-style evolutionary variants as future work.
