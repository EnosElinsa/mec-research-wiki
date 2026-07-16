---
type: source
modeling_card: not_applicable
title: "Human-level control through deep reinforcement learning"
authors: ["Volodymyr Mnih", "Koray Kavukcuoglu", "David Silver", "Andrei A. Rusu", "Joel Veness", "Marc G. Bellemare", "Alex Graves", "Martin Riedmiller", "Andreas K. Fidjeland", "Georg Ostrovski", "Stig Petersen", "Charles Beattie", "Amir Sadik", "Ioannis Antonoglou", "Helen King", "Dharshan Kumaran", "Daan Wierstra", "Shane Legg", "Demis Hassabis"]
year: 2015
url: ""
venue: "Nature"
tags: [source, deep-q-network, deep-reinforcement-learning, experience-replay, atari, foundational-drl]
related:
  - "[[van-hasselt-2016-double-dqn]]"
  - "[[lillicrap-2016-ddpg-continuous-control]]"
  - "[[fujimoto-2018-td3-actor-critic]]"
created: 2026-06-04
updated: 2026-07-16
---

# Human-level control through deep reinforcement learning

## Citation

Mnih, V., Kavukcuoglu, K., Silver, D., et al. (2015). *Human-level control through deep reinforcement learning*. **Nature**, 518, 529–533. DOI: not in parse. (Received 10 July 2014; accepted 16 January 2015.)

## TL;DR

Introduces the **Deep Q-Network (DQN)** — a deep convolutional Q-learning agent that learns control policies directly from raw pixel inputs using two stabilizing mechanisms: **experience replay** (randomizes over stored (s, a, r, s') tuples to break observation correlations) and **target networks** (periodically updated Q-network copy used to generate stable training targets). Tested on 49 Atari 2600 games with the same architecture and hyperparameters, DQN surpasses all previous RL algorithms on 43 of 49 games and matches professional human game-tester performance on more than half (29 games). The first artificial agent to learn a wide range of competencies from high-dimensional sensory inputs in an end-to-end fashion.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Mnih et al. [x] introduced the deep Q-network for learning control policies directly from high-dimensional visual observations. The method approximates the optimal action-value function with a convolutional neural network and selects discrete actions through Q-learning. It stores transitions in an experience replay memory, samples randomized minibatches, and evaluates Bellman targets with a periodically updated target network. The same architecture and hyperparameters were evaluated across 49 Atari 2600 games. The reported results exceed the evaluated previous reinforcement-learning algorithms on 43 games and reach the paper's human-level threshold on 29 games.

## Problem framing

RL with nonlinear function approximators (neural networks) is unstable or diverges due to three problems: (i) correlated sequential observations violate the i.i.d. assumption; (ii) small policy updates dramatically shift the data distribution; (iii) Q-values and target values are correlated (the target moves with the network). Prior RL successes required handcrafted features or low-dimensional state spaces. DQN addresses all three instabilities while operating directly on 84×84×4 stacked-frame pixel inputs.

## System model

- **Input:** 84×84×4 preprocessed/stacked Atari frames (greyscale, 60 Hz → 15 Hz subsampled).
- **Architecture:** three convolutional layers + two fully connected layers; single output head with one Q-value per legal action.
- **Experience replay buffer:** stores (s_t, a_t, r_t, s_{t+1}) tuples; mini-batches sampled uniformly at random.
- **Target network θ^−:** separate copy of Q-network, updated to match current Q-network parameters every C steps; held fixed between updates.
- **Loss:** E[(r + γ max_{a'} Q(s', a'; θ^−) − Q(s, a; θ))^2] minimized by SGD.
- **Evaluation:** 49 Atari 2600 games, same algorithm/hyperparameters throughout; scores normalized relative to human tester and random play.

## Key findings

- DQN outperforms all prior RL algorithms on **43 of 49 Atari games** with the same network and hyperparameters (parse text).
- Achieves human-level performance (>75% of human score) on **more than half** (29) of the 49 games (parse text).
- Experience replay and target networks are individually necessary; ablation shows both components contribute to stability (parse Methods / Supplementary).
- First demonstration of end-to-end RL learning from high-dimensional visual input without domain-specific feature engineering (parse Abstract, Introduction).

## Limitations / future work

DQN uses a single (s,a)→Q value output; it cannot handle continuous action spaces directly. Overestimates Q-values due to max operator in target — addressed by [[van-hasselt-2016-double-dqn]] (Double DQN). Fully-online experience replay does not handle non-stationary distributions optimally.

## Relation to the corpus

The foundational DQN paper that anchors the deep-Q-learning lineage in the corpus. Directly generalized by [[van-hasselt-2016-double-dqn]] (Double DQN), extended to continuous actions by [[lillicrap-2016-ddpg-continuous-control]] (DDPG), and used as conceptual backbone for DQN-based MEC sources ([[xie-2025-stin-delay-offloading]], [[mou-2025-adm-dt-migration]], and others). Experience replay and target networks are standard components in virtually every DQN-derived corpus source.

## Raw artifacts

- `raw/sources/Human-Level_Control_through_Deep_Reinforcement_Learning/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
