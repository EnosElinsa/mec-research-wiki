---
type: concept
title: "Dueling DQN"
tags: [drl, q-learning, value-based]
related:
  - "[[guo-2026-event-triggered-sinr-navigation]]"
  - "[[deep-q-network]]"
  - "[[ddqn]]"
  - "[[wu-2024-satellite-maritime-spectrum-sharing]]"
  - "[[pomdp]]"
  - "[[gao-2026-fmad3qn-uav-gd-association]]"
  - "[[zhan-2026-gatd3qn-dependent-offloading]]"
  - "[[lin-2025-energy-effective-ris-multiuav-coverage]]"
created: 2026-06-02
updated: 2026-07-13
---

# Dueling DQN

A value-based DRL architecture that splits the Q-network into two streams — a **state-value** stream $V(s)$ and an **advantage** stream $A(s,a)$ — and recombines them into $Q(s,a)$. Decoupling "how good is this state" from "how much better is each action" lets the network learn the value of states without having to estimate the effect of every action, which improves policy evaluation when many actions have similar value.

It is orthogonal to, and commonly combined with, [[ddqn|Double DQN]] (which decouples action selection from evaluation to curb over-estimation): the two together form a "Double Dueling DQN" used to stabilize learning and speed convergence over a plain [[deep-q-network]].

In the corpus, the Dueling + Double DQN combination is the backbone of the **SCA-D3QN** spectrum-sharing agent in [[wu-2024-satellite-maritime-spectrum-sharing]], where the satellite cannot fully observe channel states (a [[pomdp]]) and the architecture is reported to mitigate action-value over-estimation and accelerate convergence while evaluating channel-allocation actions.

[[gao-2026-fmad3qn-uav-gd-association]] uses the same value/advantage split inside a federated multi-agent DDQN controller for UAV 3D deployment, with a closed-form device-association subroutine supplying the reward signal. [[zhan-2026-gatd3qn-dependent-offloading]] combines D3QN with graph-attention task-DAG embeddings for dependent-task offloading.

[[lin-2025-energy-effective-ris-multiuav-coverage]] uses Dueling DQN as a RIS-assisted UAV coverage baseline and reports [[triple-deep-q-network|TDQN]] above it in average energy efficiency.
