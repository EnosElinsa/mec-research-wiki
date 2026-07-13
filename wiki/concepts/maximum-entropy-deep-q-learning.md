---
type: concept
title: "Maximum-Entropy Deep Q-Learning"
tags: [reinforcement-learning, q-learning, entropy, discrete-action, stochastic-policy]
related:
  - "[[ye-2023-graph-uav-coverage]]"
  - "[[deep-q-network]]"
  - "[[soft-actor-critic]]"
  - "[[memory-augmented-multi-uav-navigation]]"
created: 2026-07-13
updated: 2026-07-13
---

# Maximum-Entropy Deep Q-Learning

Maximum-entropy deep Q-learning augments expected return with policy entropy. For a discrete action set, Q-values can define a temperature-softmax distribution from which actions are sampled, while a soft Bellman target accounts for both value and entropy. This keeps value-based discrete control but avoids a purely greedy deterministic policy.

[[ye-2023-graph-uav-coverage]] uses this pattern in SDRGN after graph attention and GRU memory. It is distinct from [[soft-actor-critic]]: the controller has no separate stochastic actor or twin Q critics.
