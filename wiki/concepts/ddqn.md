---
type: concept
title: Double DQN (DDQN)
tags: [drl, q-learning, value-based]
related:
  - "[[federated-reinforcement-learning]]"
  - "[[mao-2025-bcsa-frl]]"
created: 2026-05-28
updated: 2026-05-28
---

# Double DQN (DDQN)

A modification of DQN (van Hasselt et al., 2016) that decouples action *selection* from action *evaluation* using two networks — an online network for selection and a target network for evaluation — to mitigate the systematic over-estimation bias of vanilla Q-learning.

## TD target

$$
y_n = r_n + \gamma\, Q_{\text{target}}\big(s_{n+1},\, \arg\max_a Q_{\text{online}}(s_{n+1}, a)\big)
$$

Compare to vanilla DQN, which uses $\arg\max_a Q_{\text{target}}$ — DDQN cuts the correlation that drives value over-estimation.

## Why it appears in MEC papers

The discrete-action subset of MEC offloading decisions (which satellite / which edge / which queue) is naturally Q-learning territory. DDQN is a low-variance, drop-in upgrade over DQN that adds little engineering cost. Used as the per-agent backbone in [[mao-2025-bcsa-frl]] for [[federated-reinforcement-learning|FRL]]-based offloading.

## Comparison with continuous-action methods

For pure-continuous problems (e.g. UAV trajectory increments), continuous-action methods like DDPG / TD3 / [[ppo|PPO]] are preferred. For pure-discrete or quantized-action problems, DQN family (DQN / DDQN / Dueling-DQN / Rainbow) remains the default choice.
