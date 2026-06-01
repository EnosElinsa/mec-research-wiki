---
type: concept
title: "Dueling DQN"
tags: [drl, q-learning, value-based]
related:
  - "[[deep-q-network]]"
  - "[[ddqn]]"
  - "[[wu-2024-satellite-maritime-spectrum-sharing]]"
  - "[[pomdp]]"
created: 2026-06-02
updated: 2026-06-02
---

# Dueling DQN

A value-based DRL architecture that splits the Q-network into two streams — a **state-value** stream $V(s)$ and an **advantage** stream $A(s,a)$ — and recombines them into $Q(s,a)$. Decoupling "how good is this state" from "how much better is each action" lets the network learn the value of states without having to estimate the effect of every action, which improves policy evaluation when many actions have similar value.

It is orthogonal to, and commonly combined with, [[ddqn|Double DQN]] (which decouples action selection from evaluation to curb over-estimation): the two together form a "Double Dueling DQN" used to stabilize learning and speed convergence over a plain [[deep-q-network]].

In the corpus, the Dueling + Double DQN combination is the backbone of the **SCA-D3QN** spectrum-sharing agent in [[wu-2024-satellite-maritime-spectrum-sharing]], where the satellite cannot fully observe channel states (a [[pomdp]]) and the architecture is reported to mitigate action-value over-estimation and accelerate convergence while evaluating channel-allocation actions.
