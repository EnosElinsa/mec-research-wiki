---
type: concept
title: "Parameterized DQN (P-DQN)"
tags: [drl, dqn, hybrid-action, continuous-action, value-based]
related:
  - "[[ddqn]]"
  - "[[hybrid-action-decision-making]]"
  - "[[j-ppo]]"
  - "[[ma-2025-pdqn-vehicular-mec]]"
created: 2026-05-29
updated: 2026-05-29
---

# Parameterized DQN (P-DQN)

A DRL variant for **hybrid action spaces** — finitely many discrete options, each parameterized by a continuous vector. Architecture:

- **Actor head per discrete option** outputs the continuous parameter vector $x_k$ for each discrete action $k$.
- **Critic** Q(s, k, $x_k$) estimates value for the (state, discrete, continuous) tuple.
- Training: Q-network is updated with TD-target like DQN; actor heads are trained to maximize the critic, like DDPG.

P-DQN sidesteps two clumsy alternatives: discretizing the continuous action (loses precision) or relaxing the discrete action to a softmax (loses integrality). It naturally fits offloading problems where the agent picks **which server** (discrete) and **how much transmit power** (continuous) — see [[ma-2025-pdqn-vehicular-mec]] for a vehicular-MEC instance.

Compared with [[j-ppo]] (on-policy, stochastic, hybrid head), P-DQN is off-policy and value-based, so sample efficient via replay but more prone to Q-overestimation. Pick P-DQN when the discrete choice is small (≤10 options) and you want sample efficiency; pick j-PPO when you want stable on-policy updates.
