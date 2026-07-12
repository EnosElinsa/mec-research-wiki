---
type: concept
title: "Pretrained-Policy Cooperation Shaping"
tags: [multi-agent-reinforcement-learning, demonstrations, social-dilemma, reward-shaping, cooperation]
related:
  - "[[chen-2026-hammurabi-cooperation]]"
  - "[[expert-guided-warm-start-rl]]"
  - "[[parameter-sharing-marl]]"
  - "[[nash-equilibrium]]"
created: 2026-07-13
updated: 2026-07-13
---

# Pretrained-Policy Cooperation Shaping

A multi-agent training pattern that treats demonstrations as a source of social bias as well as useful behavior. Rule policies are first mapped to relatively cooperative or defect-oriented policy sets, their mixtures are diagnosed with a Markov social dilemma/Schelling diagram, and reward shaping is chosen for the resulting game.

[[chen-2026-hammurabi-cooperation]] classifies its UAV coverage interaction as following a public-goods-game trend and applies inequality-aversion penalties before MARL fine-tuning. This extends [[expert-guided-warm-start-rl]] beyond sample efficiency: a warm start can transmit free-riding behavior or constrain the equilibria reached later.
