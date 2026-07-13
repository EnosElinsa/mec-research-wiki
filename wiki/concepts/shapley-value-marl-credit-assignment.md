---
type: concept
title: "Shapley-Value MARL Credit Assignment"
tags: [multi-agent-reinforcement-learning, credit-assignment, cooperative-game-theory, shapley-value]
related:
  - "[[li-2026-credit-aware-uav-irs-secrecy]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[masac]]"
  - "[[soft-actor-critic]]"
  - "[[primal-dual-constrained-marl]]"
created: 2026-07-14
updated: 2026-07-14
---

# Shapley-Value MARL Credit Assignment

Shapley-value MARL credit assignment converts a shared team outcome into agent-specific rewards by averaging each agent's marginal contribution over coalitions. The resulting credits satisfy an efficiency property: their sum equals the value assigned to the full coalition.

[[li-2026-credit-aware-uav-irs-secrecy]] uses exact coalition values to reward UAV-IRS agents inside a [[centralized-training-decentralized-execution]] [[masac|MASAC]] learner. The individualized signal is intended to expose each UAV-IRS's contribution when trajectories and phase shifts jointly determine secrecy performance.

The credit is only as meaningful as the chosen coalition-value function, and it attributes reward rather than guaranteeing cooperation or causal responsibility. Exact enumeration grows factorially with agent count; the supporting method therefore pairs it with [[primal-dual-constrained-marl]] and evaluates only relatively small UAV teams.
