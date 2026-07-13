---
type: concept
title: "Multi-Agent Q-Learning"
tags: [drl, multi-agent, value-based, game-theory]
related:
  - "[[nash-equilibrium]]"
  - "[[stochastic-game]]"
  - "[[ddqn]]"
  - "[[li-2025-stochastic-game-uav-swarm]]"
  - "[[ctde-actor-critic-backbones-in-mec]]"
  - "[[zhou-2026-multiscale-dt-uav-delivery]]"
  - "[[cui-2020-marl-uav-resource-allocation]]"
  - "[[zhu-2025-green-isac-q-learning]]"
created: 2026-05-29
updated: 2026-07-14
---

# Multi-Agent Q-Learning

[[cui-2020-marl-uav-resource-allocation]] is an early independent tabular instance: each UAV learns from a binary local QoS state without exchanging actions or rewards, leaving the coupled learning environment non-stationary.

Decentralized / independent-learner Q-learning where multiple agents each maintain their own Q-table or Q-network and learn concurrently, optionally exchanging Q-values to coordinate. Unlike single-agent Q-learning, the environment is non-stationary from any one agent's view (other agents are also learning), so convergence guarantees usually rely on a game-theoretic structure.

In the wiki, [[li-2025-stochastic-game-uav-swarm]]'s **RLDC** algorithm is tabular multi-agent Q-learning with periodic Q-value sharing over a dedicated control channel; the authors prove it converges to a [[nash-equilibrium]] of the underlying [[stochastic-game]] via contraction-mapping arguments. This is distinct from the deep actor-critic backbones ([[ddpg]], [[td3]], [[masac]]) and value-based [[ddqn]] used elsewhere in the corpus — it is closer to classical RL married to equilibrium analysis.

[[zhu-2025-green-isac-q-learning]] is another independent tabular case, distinguished by periodic inverse-CRLB initialization and a nonstandard update that prevents Q values from decreasing; the paper does not prove convergence for that rule.
