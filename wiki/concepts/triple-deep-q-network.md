---
type: concept
title: "Triple Deep Q-Network (TDQN)"
tags: [drl, q-learning, value-based, overestimation]
related:
  - "[[deep-q-network]]"
  - "[[ddqn]]"
  - "[[dueling-dqn]]"
  - "[[lin-2025-energy-effective-ris-multiuav-coverage]]"
created: 2026-07-11
updated: 2026-07-11
---

# Triple Deep Q-Network (TDQN)

A DQN-family variant that adds an auxiliary target network to the usual online/target-network setup, with asynchronous target updates and expectation-style target estimation intended to reduce bootstrap and max-estimation overestimation.

In [[lin-2025-energy-effective-ris-multiuav-coverage]], TDQN controls RIS-assisted UAV movement and GT scheduling. It is compared with DQN, [[ddqn|DDQN]], and [[dueling-dqn|Dueling DQN]] under the same RIS/DBSCAN/fair setting, and reports the highest average energy efficiency among those value-based baselines before the K-DBSCAN clustering upgrade. The concept is useful as a narrow DQN-family entry, not a general replacement for actor-critic methods in continuous control.
