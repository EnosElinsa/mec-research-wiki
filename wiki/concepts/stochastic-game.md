---
type: concept
title: "Stochastic Game (Markov Game)"
tags: [game-theory, multi-agent, mdp]
related:
  - "[[nash-equilibrium]]"
  - "[[potential-game]]"
  - "[[stackelberg-game]]"
  - "[[multi-agent-q-learning]]"
  - "[[ma-pomdp]]"
  - "[[regret-minimization-learning]]"
  - "[[li-2025-stochastic-game-uav-swarm]]"
  - "[[ning-2023-uav-mec-offloading-deployment]]"
  - "[[fan-2026-parallel-caching-uav-mec]]"
  - "[[wang-2023-differentiated-uav-services]]"
  - "[[differentiated-uav-service-market]]"
  - "[[multi-agent-imitation-learning]]"
  - "[[cui-2020-marl-uav-resource-allocation]]"
created: 2026-05-29
updated: 2026-07-13
---

# Stochastic Game (Markov Game)

A multi-state generalization of a repeated game: multiple players act in a shared environment with **state-transition probabilities**, so it is simultaneously a generalization of an MDP (to many agents) and of a one-shot game (to many states). Each agent has its own per-state reward and seeks a policy that is a best response to the others — the solution concept is a [[nash-equilibrium]] (often per stage / Markov-perfect).

[[cui-2020-marl-uav-resource-allocation]] models UAV base stations as selfish stochastic-game players choosing a user, subchannel, and power level through independent tabular Q-learning.

In the wiki, [[li-2025-stochastic-game-uav-swarm]] reformulates UAV-swarm energy/clustering/scheduling as **five interconnected stochastic games** (energy replenishment, application placement, trajectory, dynamic clustering, task delegation), proves NE existence via reduction to a multi-period stage game, and solves them with [[multi-agent-q-learning]]. Distinct from the leader-follower [[stackelberg-game]] and the single-controller multi-agent [[ma-pomdp]]; a [[potential-game]] is a special case with convergence guarantees.

[[ning-2023-uav-mec-offloading-deployment]] uses stochastic games differently: it decomposes UAV-enabled MEC into a UE computation-offloading game and a UAV location-selection game, then uses probability-based learning plus a chess-like alternating update to seek pure-strategy Nash equilibria under dynamic task generation.

[[fan-2026-parallel-caching-uav-mec]] uses a stochastic-game layer for inter-UAV channel allocation, solved with [[regret-minimization-learning]] toward correlated-equilibrium channel profiles while lower-layer DQN handles each UAV's caching/offloading choices.
