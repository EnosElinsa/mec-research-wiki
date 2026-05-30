---
type: source
title: "Addressing Function Approximation Error in Actor-Critic Methods"
authors: ["Scott Fujimoto", "Herke van Hoof", "David Meger"]
year: 2018
url: ""
venue: "Proceedings of the 35th International Conference on Machine Learning (ICML), PMLR 80"
tags: [source, drl, actor-critic, td3, continuous-control, overestimation-bias, foundational-method]
related:
  - "[[td3]]"
  - "[[ddpg]]"
  - "[[ddqn]]"
  - "[[multi-agent-td3]]"
  - "[[hao-2024-clp-multiuav-priority-offloading]]"
  - "[[shao-2024-drl-antijamming-mec]]"
  - "[[zhao-2022-matd3-multiuav-ec-offloading]]"
created: 2026-05-31
updated: 2026-05-31
---

# Addressing Function Approximation Error in Actor-Critic Methods

## Citation

Fujimoto, S., van Hoof, H., & Meger, D. (2018). *Addressing Function Approximation Error in Actor-Critic Methods*. **Proceedings of the 35th International Conference on Machine Learning (ICML)**, Stockholm, Sweden, PMLR 80. DOI: not in parse. (Open-source code linked in the parse: `https://github.com/sfujim/TD3`.)

## TL;DR

The **origin paper for TD3** (Twin Delayed Deep Deterministic policy gradient). It shows that the overestimation bias well known in discrete-action [[deep-q-network|Q-learning]] also afflicts actor-critic continuous-control methods, and proposes three mechanisms to fix it. Built on top of [[ddpg]], the result outperforms the prior state of the art across the OpenAI Gym continuous-control suite. This is a **foundational DRL-method** entry rather than an MEC application — it documents the algorithm that many UAV-MEC sources in this wiki build on.

## Problem framing

In value-based RL, maximizing a noisy value estimate causes consistent overestimation; temporal-difference bootstrapping accumulates that error. The authors establish that deterministic policy gradients in continuous control inherit the same problem, and that the discrete-action fix (Double DQN) is ineffective in actor-critic settings because the slowly-changing policy keeps current and target value estimates too similar.

## System model

Not an MEC system. The setting is the standard RL paradigm: an agent interacting with an environment, choosing actions per a policy to maximize the discounted return, evaluated on seven continuous-control domains from OpenAI Gym.

## Method

TD3 augments DDPG with three techniques:

- **Clipped double Q-learning** — a pair of independently trained critics; the TD target uses the **minimum** of the two to upper-bound (and thus curb) overestimation, favoring underestimation that does not propagate.
- **Delayed policy updates** — the actor and target networks update less frequently than the critics, so the value estimate converges before it drives policy updates, reducing per-update error.
- **Target policy smoothing** — a SARSA-style regularizer that bootstraps similar action estimates (clipped noise on the target action) to reduce variance.

See [[td3]] for the wiki's concept page.

## Key findings

- Overestimation bias and error accumulation are demonstrably present in actor-critic continuous control, not just discrete Q-learning.
- TD3 outperforms the state of the art "in every environment tested" / "by a wide margin" (the parse's wording), with ablations isolating each contribution and experiments run across many seeds for reproducibility.

## Limitations / future work

The parse does not enumerate explicit limitations or future work beyond the reproducibility framing.

## Relation to the corpus

The **method ancestor** of the wiki's large TD3 lineage. [[td3]] (concept) names it as the hardened successor to [[ddpg]]; the multi-agent extension [[multi-agent-td3]] (MATD3) appears in [[shao-2024-drl-antijamming-mec]] and [[zhao-2022-matd3-multiuav-ec-offloading]], and the hybrid-action latent variant CLP in [[hao-2024-clp-multiuav-priority-offloading]] builds directly on TD3. Curating the source paper grounds those downstream claims. Its clipped-double-Q idea also descends from the [[ddqn|Double Q-learning]] line.

## Raw artifacts

- `raw/sources/Addressing Function Approximation Error in Actor-Critic Methods/full.md`
- Original PDF and extracted figures in the same folder.
