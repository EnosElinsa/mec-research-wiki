---
type: concept
title: "Deep Q-Network (DQN)"
tags: [drl, value-based, discrete-action, off-policy, replay-buffer]
related:
  - "[[zhang-2021-safe-dqn-emergency]]"
  - "[[chai-2026-random-position-relay-deployment]]"
  - "[[wu-2026-sensing-error-uav-scheduling]]"
  - "[[wang-2023-drl-irs-uav-trajectory]]"
  - "[[ddqn]]"
  - "[[parameterized-dqn]]"
  - "[[ddpg]]"
  - "[[gao-2024-sagin-perception-offloading]]"
  - "[[zhao-2026-adaptive-wdc-wet-lae]]"
  - "[[triple-deep-q-network]]"
  - "[[zhao-2026-dt-ddqn-bisd-deployment]]"
  - "[[zhang-2026-distributed-jscc-uav-video]]"
  - "[[ding-2026-optimization-driven-spectrum-sharing]]"
created: 2026-05-29
updated: 2026-07-14
---

# Deep Q-Network (DQN)

[[wu-2026-sensing-error-uav-scheduling]] uses a multi-agent DQN backbone for UAV position, association, and bandwidth decisions, but describes those action components as continuous without specifying discretization or a hybrid-action parameterization. That unresolved mismatch is a concrete instance of DQN's discrete-action limitation.

The foundational value-based DRL algorithm: a deep neural network approximates the action-value function $Q(s,a)$, trained with TD targets bootstrapped from a periodically-synced target network and sampled from an experience replay buffer. Action selection is greedy / ε-greedy over the discrete action set.

Strengths: simple, sample-efficient (off-policy + replay), and effective for **discrete** decisions. Weaknesses: only handles discrete/low-cardinality action spaces, suffers Q-overestimation (addressed by [[ddqn|Double DQN]]), and does not extend natively to continuous control (where [[ddpg]]/[[td3]] are used instead).

In the wiki, [[gao-2024-sagin-perception-offloading]] uses a plain DQN to solve the discrete UAV-BS association subproblem (a 0/1 MINLP), pairing it with [[ddpg]] for continuous offloading control. [[zhao-2026-adaptive-wdc-wet-lae]] uses DQN in the second tier of MA2HDRL for discrete WDC subslot scheduling, while SAC handles continuous trajectory/WET control. The corpus also contains [[ddqn]] and [[parameterized-dqn]] variants as specializations.

[[lin-2025-energy-effective-ris-multiuav-coverage]] adds [[triple-deep-q-network|TDQN]], a DQN-family variant with an auxiliary target network for RIS-assisted UAV trajectory and GT scheduling.
