---
type: source
title: "Continuous Control with Deep Reinforcement Learning"
authors: ["Timothy P. Lillicrap", "Jonathan J. Hunt", "Alexander Pritzel", "Nicolas Heess", "Tom Erez", "Yuval Tassa", "David Silver", "Daan Wierstra"]
year: 2016
url: ""
venue: "International Conference on Learning Representations (ICLR)"
modeling_card: not_applicable
tags: [source, drl, actor-critic, ddpg, continuous-control, off-policy, foundational-method]
related:
  - "[[ddpg]]"
  - "[[deep-q-network]]"
  - "[[td3]]"
  - "[[fujimoto-2018-td3-actor-critic]]"
  - "[[bao-2025-ddpg-video-offloading]]"
  - "[[zhang-2024-uav-task-offloading-ddpg]]"
  - "[[maddpg]]"
created: 2026-06-02
updated: 2026-07-16
---

# Continuous Control with Deep Reinforcement Learning

## Citation

Lillicrap, T. P., Hunt, J. J., Pritzel, A., Heess, N., Erez, T., Tassa, Y., Silver, D., & Wierstra, D. (2016). *Continuous Control with Deep Reinforcement Learning*. Presented at ICLR 2016. Also published as arXiv:1509.02971. DOI: not in parse.

## TL;DR

The **origin paper for DDPG** (Deep Deterministic Policy Gradient), the off-policy actor-critic algorithm that many UAV-MEC and aerial DRL sources in this wiki use as a continuous-control backbone. It adapts the ideas behind Deep Q-Learning to continuous action spaces: a [[deep-q-network|DQN]]-style critic (replay buffer + target network) is combined with a **deterministic policy gradient** actor, so the method avoids the per-step action maximization that makes plain Q-learning intractable in continuous domains. Using one set of hyperparameters and network architecture, DDPG robustly solves more than 20 simulated physics tasks (cartpole swing-up, dexterous manipulation, legged locomotion, car driving), in many cases learning end-to-end directly from raw pixels. This is a **foundational DRL-method** entry rather than an MEC application; it documents the algorithm that [[ddpg]] and its downstream variants build on.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Lillicrap et al. [x] introduced Deep Deterministic Policy Gradient as a model-free off-policy actor-critic method for continuous action spaces. DDPG trains a deterministic actor through the critic's action gradient and stabilizes temporal-difference learning with replay, slowly updated actor and critic targets, and batch normalization. Temporally correlated exploration noise separates behavior exploration from the learned deterministic policy. Using one architecture and hyperparameter set, the method learned policies for more than 20 simulated control tasks from low-dimensional states and, in many cases, directly from pixels. The ablation study found target networks crucial, while normalized evaluations showed that some runs exceeded a model-based planner with access to the simulator dynamics.

## Problem framing

DQN handles high-dimensional observations but only **discrete, low-dimensional action spaces**, because it relies on finding the action that maximizes the action-value function — an iterative optimization at every step in continuous domains. Naively discretizing a continuous action space suffers the curse of dimensionality (a 7-DoF system with a 3-level-per-joint discretization already gives 3^7 = 2187 actions) and discards the structure of the action domain. The paper seeks a model-free, off-policy method that learns policies directly in high-dimensional, continuous action spaces, while remaining stable with neural-network function approximators.

## System model

Not an MEC system. The setting is the standard RL paradigm — an agent interacting with an environment in discrete timesteps to maximize discounted return, modeled as an MDP with a continuous action space $\mathcal{A} = \mathbb{R}^N$. Evaluated on simulated physical-control tasks in MuJoCo (and the TORCS driving simulator), using both low-dimensional state descriptors (joint angles/positions) and high-dimensional pixel renderings.

## Method

DDPG builds on the deterministic policy gradient (DPG) algorithm and imports DQN's stabilizing ingredients:

- **Deterministic actor** $\mu(s\mid\theta^\mu)$ trained by the policy gradient $\nabla_{\theta^\mu} J \approx \mathbb{E}[\nabla_a Q(s,a\mid\theta^Q)\,\nabla_{\theta^\mu}\mu(s\mid\theta^\mu)]$ (chain rule through the critic).
- **Q-critic** $Q(s,a\mid\theta^Q)$ trained with TD targets, bootstrapped from target networks.
- **Replay buffer** to decorrelate the sequentially-sampled transitions and enable minibatch learning.
- **Soft target updates** $\theta' \leftarrow \tau\theta + (1-\tau)\theta'$ with $\tau \ll 1$ for both actor and critic target networks — found to be required for stable, non-diverging training (a key difference from the original DPG).
- **Batch normalization** on the state input and network layers, so a single set of hyperparameters generalizes across tasks with differing observation units/scales.
- **Ornstein-Uhlenbeck exploration noise** added to the actor's actions during training (off-policy exploration treated separately from learning).

See [[ddpg]] for the wiki's concept page.

## Key findings

- With identical network structure and hyperparameters, DDPG learns competitive policies across more than 20 simulated physics tasks from low-dimensional observations, and good policies directly from pixels in many cases (the parse's wording).
- Normalizing scores so a random agent scores 0 and a model-based planner (iLQG, full access to the dynamics) scores 1, DDPG reaches good policies on many tasks and in several runs **exceeds the planner** even when learning from pixels (Table 1, parse).
- Ablations show **target networks are crucial** — learning without them (as in the original DPG) is very poor in many environments; batch normalization is also needed for cross-task generalization (Fig. 2, parse; curves are figure-derived and indicative).
- DDPG's Q-estimates are accurate without systematic bias on simple tasks and degrade on harder ones, while still yielding competent policies (Fig. 3, parse). The paper notes Q-learning's known tendency to overestimate values — the issue that [[van-hasselt-2016-double-dqn|Double DQN]] and later [[fujimoto-2018-td3-actor-critic|TD3]] target directly.

## Limitations / future work

The parse notes DDPG can require a large number of training episodes to find solutions (the typical sample-complexity caveat of model-free RL) and that, like other RL methods, it provides no convergence guarantee with non-linear function approximators. Explicit future-work targets beyond scaling to harder problems are `not in parse`.

## Relation to the corpus

The **method ancestor** of the wiki's large DDPG lineage. The [[ddpg]] concept page summarizes this algorithm; vanilla DDPG drives the continuous controllers in [[bao-2025-ddpg-video-offloading]] (offloading-ratio + transcoding + HAP-resource control) and [[zhang-2024-uav-task-offloading-ddpg]] (UAV trajectory), the multi-agent extension [[maddpg]] descends from it, and [[fujimoto-2018-td3-actor-critic|TD3]] is its overestimation-hardened successor. This source paper grounds those downstream claims, just as [[schulman-2017-ppo]] grounds the PPO line and [[van-hasselt-2016-double-dqn]] grounds the Double-Q line.

## Raw artifacts

- `raw/sources/Continuous control with deep reinforcement learning/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
