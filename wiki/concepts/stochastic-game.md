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
  - "[[li-2025-stochastic-game-uav-swarm]]"
created: 2026-05-29
updated: 2026-05-29
---

# Stochastic Game (Markov Game)

A multi-state generalization of a repeated game: multiple players act in a shared environment with **state-transition probabilities**, so it is simultaneously a generalization of an MDP (to many agents) and of a one-shot game (to many states). Each agent has its own per-state reward and seeks a policy that is a best response to the others — the solution concept is a [[nash-equilibrium]] (often per stage / Markov-perfect).

In the wiki, [[li-2025-stochastic-game-uav-swarm]] reformulates UAV-swarm energy/clustering/scheduling as **five interconnected stochastic games** (energy replenishment, application placement, trajectory, dynamic clustering, task delegation), proves NE existence via reduction to a multi-period stage game, and solves them with [[multi-agent-q-learning]]. Distinct from the leader-follower [[stackelberg-game]] and the single-controller multi-agent [[ma-pomdp]]; a [[potential-game]] is a special case with convergence guarantees.
