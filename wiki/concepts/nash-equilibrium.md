---
type: concept
title: "Nash Equilibrium"
tags: [game-theory, equilibrium, solution-concept]
related:
  - "[[du-2026-hierarchical-coalition-deployment]]"
  - "[[challita-2019-cellular-uav-interference-drl]]"
  - "[[potential-game]]"
  - "[[tang-2026-gat-antijamming]]"
  - "[[stochastic-game]]"
  - "[[stackelberg-game]]"
  - "[[multi-agent-q-learning]]"
  - "[[equilibrium-efficiency-metric]]"
  - "[[chen-2024-ulse-game]]"
  - "[[li-2025-stochastic-game-uav-swarm]]"
  - "[[li-2026-jscfg-uav-grouping]]"
  - "[[joint-switch-coalition-formation-game]]"
  - "[[wang-2023-differentiated-uav-services]]"
  - "[[differentiated-uav-service-market]]"
created: 2026-05-29
updated: 2026-07-13
---

# Nash Equilibrium

The central solution concept of non-cooperative game theory: a strategy profile in which **no player can improve its own payoff by unilaterally deviating**, given the others' strategies. Every player is simultaneously playing a best response. A pure-strategy NE need not exist in general, but special structures guarantee it — e.g. [[potential-game|potential games]] (via the finite improvement property) and the multi-period stage games underlying many [[stochastic-game|stochastic games]].

In the wiki, NE is the target/convergence point of two game-theoretic offloading papers: [[chen-2024-ulse-game]] (proves its LUTO-Game is a potential game with a guaranteed NE, reached by distributed best response) and [[li-2025-stochastic-game-uav-swarm]] (proves NE existence and that its [[multi-agent-q-learning]] RLDC converges to the optimal NE Q-values). Equilibrium efficiency relative to the social optimum is captured by the price of anarchy ([[equilibrium-efficiency-metric]]); contrast the leader-follower equilibrium of the [[stackelberg-game]].
