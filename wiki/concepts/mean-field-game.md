---
type: concept
title: "Mean Field Game"
tags: [game-theory, multi-agent, optimization, uav-mec, energy-harvesting]
related:
  - "[[yao-2026-transformer-mean-field-isac-sagin]]"
  - "[[stochastic-game]]"
  - "[[nash-equilibrium]]"
  - "[[lyapunov-optimization]]"
  - "[[energy-harvesting-mec]]"
  - "[[task-offloading]]"
  - "[[energy-balancing-uav]]"
  - "[[ma-2026-mean-field-green-aec]]"
  - "[[kernel-density-mean-field-marl]]"
  - "[[li-2026-uav-bs-semantic-mfmaddpg-kde]]"
created: 2026-07-07
updated: 2026-07-13
---

# Mean Field Game

A mean field game approximates a large population of interacting agents by replacing direct pairwise coupling with an aggregate population state. Each agent solves a representative control problem against that mean field, and the population state evolves consistently with the agents' policies.

In MEC and aerial edge computing, MFG is useful when hundreds of devices or UAVs interact through shared congestion, energy, or load-balancing effects. It keeps the decision problem scalable without assuming that a central controller can optimize every agent's full joint state.

In [[ma-2026-mean-field-green-aec]], the aggregate state is the UAV population's energy distribution. The MFG decouples large-scale [[task-offloading]] and energy scheduling in a green aerial edge computing system, while [[lyapunov-optimization]] supplies the energy valuation signal that steers long-term balance. The paper reports an epsilon-Nash-equilibrium style approximation with error decreasing as the UAV population grows.

[[li-2026-uav-bs-semantic-mfmaddpg-kde]] is not framed as a formal MFG equilibrium paper, but it uses the adjacent mean-field MARL idea: each UAV-BS approximates neighborhood influence through an aggregate action distribution, refined by [[kernel-density-mean-field-marl|KDE]] for continuous deployment actions.
