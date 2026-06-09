---
type: source
title: "Deep Reinforcement Learning with Double Q-learning"
authors: ["Hado van Hasselt", "Arthur Guez", "David Silver"]
year: 2016
url: ""
venue: "not in parse"
tags: [source, drl, q-learning, value-based, double-dqn, overestimation-bias, foundational-method]
related:
  - "[[ddqn]]"
  - "[[deep-q-network]]"
  - "[[td3]]"
  - "[[fujimoto-2018-td3-actor-critic]]"
  - "[[mao-2025-bcsa-frl]]"
created: 2026-06-02
updated: 2026-06-09
---

# Deep Reinforcement Learning with Double Q-learning

## Citation

van Hasselt, H., Guez, A., & Silver, D. (2016). *Deep Reinforcement Learning with Double Q-learning*. DOI: not in parse; venue: not in parse. The parse carries no DOI, venue, or formal date line.

## TL;DR

The **origin paper for Double DQN**, the value-based DRL algorithm that the wiki's discrete-action MEC offloading sources use to curb Q-learning's over-estimation bias. The paper shows that the over-estimation long known in tabular Q-learning also afflicts the deep DQN agent — substantially, on several Atari 2600 games — and that the **Double Q-learning** idea (decoupling action *selection* from action *evaluation*) generalizes to deep function approximation. The proposed minimal change to DQN, **Double DQN**, reuses the existing target network as the second value estimator: it yields more accurate value estimates and markedly better policies, setting state-of-the-art Atari results. This is a **foundational DRL-method** entry rather than an MEC application — it documents the algorithm the wiki's [[ddqn]] concept page builds on.

## Problem framing

Q-learning includes a maximization over estimated action values, which systematically prefers over-estimated to under-estimated values. The paper unifies prior explanations (inflexible function approximation; environmental noise) by proving that estimation errors of **any** source can induce an upward bias, then asks empirically whether such over-estimations occur for the deep DQN agent, whether they hurt performance, and whether they can be prevented — answering all three affirmatively.

## System model

Not an MEC system. The setting is the standard RL paradigm — learning action values for sequential decision problems to maximize cumulative discounted reward. Evaluated on the Atari 2600 suite via the Arcade Learning Environment, following the DQN experimental protocol (convolutional network, last four frames as input, ~1.5M parameters, 200M training frames per game).

## Method

- **Theorem (lower bound on over-estimation).** If all true optimal action values in a state are equal but the value estimates are unbiased-on-average yet imperfect (mean-squared error $C$), then $\max_a Q_t(s,a) \ge V_*(s) + \sqrt{C/(m-1)}$ for $m$ actions, while the Double-Q estimate's lower bound on absolute error is zero — showing over-estimation arises even with on-average-correct estimates.
- **Double Q-learning target.** Untangle selection from evaluation in the Q-target: select the greedy action with the online weights, but evaluate its value with a second set of weights.
- **Double DQN.** The minimal adaptation of DQN — reuse the **target network** as the second value function. The TD target becomes $Y_t^{\text{DoubleDQN}} = R_{t+1} + \gamma\, Q(S_{t+1}, \arg\max_a Q(S_{t+1},a;\theta_t), \theta_t^{-})$, where $\theta_t$ are the online weights (selection) and $\theta_t^{-}$ the periodically-copied target weights (evaluation). The rest of DQN is unchanged, for a fair comparison at minimal computational overhead.

See [[ddqn]] for the wiki's concept page.

## Key findings

- DQN is consistently, sometimes vastly, over-optimistic about the value of its greedy policy; the over-estimation was observed in **all 49** tested Atari games (in varying amounts), and on Asterix and Wizard of Wor it is extreme enough that rising value estimates coincide with dropping game scores.
- Double DQN produces value estimates much closer to the true discounted returns and **more stable** learning, confirming that DQN's over-estimations were degrading policy quality.
- On 49 games (up to 5 minutes of play), Double DQN improves the normalized score over DQN: **median 93.5% → 114.7%** and **mean 241.1% → 330.3%** (Table 1, parse; DQN numbers cited from Mnih et al. 2015).

## Limitations / future work

The parse notes that over-optimism does not always harm the resulting policy (e.g. DQN plays Pong optimally despite slight over-estimation); the contribution is reducing the cases where it does. Explicit future-work targets beyond extending the decoupling idea are `not in parse`.

## Relation to the corpus

The **method ancestor** of the wiki's Double-Q line. The [[ddqn]] concept page summarizes this algorithm; its decoupled-target idea is the discrete-action analogue of the clipped-double-Q mechanism that [[fujimoto-2018-td3-actor-critic|TD3]] later brings to continuous control, and the [[deep-q-network|DQN]] family it hardens is the discrete-action backbone for MEC offloading decisions (e.g. the per-agent Q-learning in [[mao-2025-bcsa-frl]]). Curating the source paper grounds those downstream claims, alongside [[lillicrap-2016-ddpg-continuous-control]] (DDPG) and [[schulman-2017-ppo]] (PPO).

## Raw artifacts

- `raw/sources/Deep_Reinforcement_Learning_with_Double_Q-learning/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
