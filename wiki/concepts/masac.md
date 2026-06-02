---
type: concept
title: MASAC (Multi-Agent Soft Actor-Critic)
tags: [drl, multi-agent, off-policy]
related:
  - "[[qin-2025-bcuav-masac]]"
  - "[[ctde-actor-critic-backbones-in-mec]]"
created: 2026-05-28
updated: 2026-06-03
---

# MASAC (Multi-Agent Soft Actor-Critic)

The multi-agent extension of [Soft Actor-Critic (SAC)](https://arxiv.org/abs/1801.01290): a maximum-entropy off-policy actor-critic that augments the standard policy objective with an entropy bonus

$$
J(\pi) = \mathbb{E}\Big[\sum_t r(s_t, a_t) + \alpha\, H(\pi(\cdot|s_t))\Big]
$$

The entropy term encourages exploration; $\alpha$ can be auto-tuned to track a target entropy.

In the multi-agent setting, MASAC keeps **decentralized actors** (each agent acts on its own observation) and a **centralized critic** during training (sees all agents' observations + actions to reduce non-stationarity from concurrent learning).

## Why it appears in MEC papers

Compared to **MADDPG** (multi-agent deterministic policies):

- MASAC's stochastic policies handle Pareto-frontier-like multi-objective rewards better.
- The entropy bonus keeps exploration alive in scenarios where agents would otherwise collapse onto suboptimal coordination equilibria.
- Off-policy + replay buffer means sample efficiency is much higher than on-policy alternatives.

In [[qin-2025-bcuav-masac]] the authors specifically pick MASAC over MADDPG and show empirical gains in convergence speed and final sensing rate.

## Trade-offs

- More hyperparameters (entropy target, two Q-nets, target net Polyak rate).
- Centralized critic input dimension grows with agent count — scaling beyond ~10 agents needs attention factorization or value decomposition tricks.
- Off-policy updates can amplify reward-shaping mistakes; reward design needs care.
