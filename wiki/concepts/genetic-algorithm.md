---
type: concept
title: "Genetic Algorithm"
tags: [optimization, evolutionary, metaheuristic, deployment]
related:
  - "[[zhao-2026-uav-irs-data-collection]]"
  - "[[guo-2026-uav-wsn-completion-time]]"
  - "[[shah-2026-cellfree-mimo-fap-control]]"
  - "[[guo-2026-dual-objective-multiuav-isac]]"
  - "[[non-dominated-sorting-genetic-algorithm]]"
  - "[[constrained-multi-objective-evolutionary-algorithm]]"
  - "[[two-stage-decomposition]]"
  - "[[zhao-2026-hcdrl-ga-sagin-sar]]"
  - "[[zhou-2026-gl-ahg-coverage-planning]]"
  - "[[zhang-2026-msialns-air-ground-inspection]]"
  - "[[kanani-2026-haps-uav-isac]]"
created: 2026-07-07
updated: 2026-07-14
---

# Genetic Algorithm

An evolutionary metaheuristic that represents candidate solutions as chromosomes and iteratively applies selection, crossover, mutation, and elitism-style retention to improve a fitness score. In this wiki it is most useful when the decision is combinatorial or deployment-like, and the candidate can be evaluated by a simulator, solver, or learned policy rather than by a closed-form objective.

In [[zhao-2026-hcdrl-ga-sagin-sar]], GA searches UAV takeoff/recovery deployment configurations. Each candidate deployment is evaluated through rollouts of a trained HCDRL/HCSAC policy, so the GA acts as a low-frequency mission-planning layer while DRL handles online trajectory and offloading.

This is related to [[non-dominated-sorting-genetic-algorithm]], which explicitly maintains a Pareto front for multi-objective search. The SAGIN SAR paper uses a normalized weighted-sum fitness for one executable deployment and names Pareto-style evolutionary variants as future work.

[[zhou-2026-gl-ahg-coverage-planning]] uses an alternating hierarchical GA for terrain coverage paths. It switches between distance-heavy and energy-heavy fitness every 100 generations, retains a non-dominated archive, and periodically injects archive elites. The method is multi-objective in its search state even though a normalized weighted score selects one final route.

[[kanani-2026-haps-uav-isac]] uses canonical GA for a weighted sensing/communication objective and compares it with a PPO scalarization and a Pareto-preserving NSGA-II formulation.
