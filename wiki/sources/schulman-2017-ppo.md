---
type: source
title: "Proximal Policy Optimization Algorithms"
authors: ["John Schulman", "Filip Wolski", "Prafulla Dhariwal", "Alec Radford", "Oleg Klimov"]
year: 2017
url: ""
venue: ""
tags: [source, drl, policy-gradient, on-policy, ppo, continuous-control, foundational-method]
related:
  - "[[ppo]]"
  - "[[gae]]"
  - "[[j-ppo]]"
  - "[[mappo]]"
  - "[[liu-2026-jppo-en-convntm]]"
  - "[[song-2024-mol-aoi-energy]]"
  - "[[kang-2023-mappo-hierarchical-aerial]]"
  - "[[lee-2024-dho-leo-handover]]"
created: 2026-06-01
updated: 2026-06-09
---

# Proximal Policy Optimization Algorithms

## Citation

Schulman, J., Wolski, F., Dhariwal, P., Radford, A., & Klimov, O. (2017). *Proximal Policy Optimization Algorithms*. **OpenAI**. DOI: not in parse; venue: not in parse. The raw sidecar parse records `arXiv:1707.06347v2 [cs.LG] 28 Aug 2017`.

## TL;DR

The **origin paper for PPO** (Proximal Policy Optimization), the on-policy policy-gradient method that many UAV-MEC and aerial DRL sources in this wiki use as a backbone. PPO keeps the stability of trust-region methods (TRPO) but uses only **first-order optimization**: a **clipped surrogate objective** that forms a pessimistic (lower-bound) estimate of policy performance and discourages updates that move the action-probability ratio too far from 1. This lets the method run **multiple epochs of minibatch SGD** on each batch of sampled data, giving a favorable balance of sample complexity, simplicity, and wall-clock time. This is a **foundational DRL-method** entry rather than an MEC application — it documents the algorithm that the wiki's [[ppo]] concept page and its many downstream variants build on.

## Problem framing

Among neural-network RL methods, deep Q-learning fails on many simple problems and is poorly understood, vanilla policy gradients have poor data efficiency and robustness, and TRPO is comparatively complicated and incompatible with architectures using noise (e.g. dropout) or parameter sharing between the policy and value function. The paper seeks a method that is **scalable, data-efficient, and robust** while using only first-order optimization, attaining TRPO-like reliability without its complexity.

## System model

Not an MEC system. The setting is the standard RL paradigm — an agent interacting with an environment to maximize discounted return — evaluated on simulated robotic locomotion (MuJoCo / OpenAI Gym, and the Roboschool 3D-humanoid tasks) and Atari (Arcade Learning Environment).

## Method

- **Clipped surrogate objective.** With probability ratio $r_t(\theta) = \pi_\theta(a_t|s_t)/\pi_{\theta_\text{old}}(a_t|s_t)$, the objective is $L^{\text{CLIP}}(\theta) = \hat{\mathbb{E}}_t[\min(r_t(\theta)\hat{A}_t,\ \text{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon)\hat{A}_t)]$ — the min of the clipped and unclipped terms removes the incentive to push $r_t$ outside $[1-\epsilon, 1+\epsilon]$ (the paper uses $\epsilon = 0.2$ as a representative value).
- **Adaptive KL-penalty variant.** An alternative that adapts a KL-penalty coefficient $\beta$ toward a target KL each update; the paper reports it performs **worse** than the clipped objective but includes it as a baseline.
- **Combined loss.** With shared policy/value parameters, the per-iteration loss adds a value-function squared-error term and an entropy bonus: $L^{\text{CLIP}+\text{VF}+\text{S}}$.
- **Actor-critic style algorithm.** $N$ parallel actors each collect $T$ timesteps, advantages are computed via a truncated [[gae|generalized advantage estimation]], then the surrogate is optimized with $K$ epochs of minibatch SGD (Adam).

See [[ppo]] for the wiki's concept page and equations.

## Key findings

- On the continuous-control comparison of surrogate objectives, **clipping at $\epsilon = 0.2$ scored best** (average normalized score 0.82), beating no-clipping/penalty (−0.39) and the adaptive/fixed KL variants (Table 1, parse).
- PPO (clipped) **outperforms** TRPO, A2C, A2C+trust-region, CEM, and adaptive vanilla policy gradient on almost all the MuJoCo continuous-control environments (Fig. 3, parse; curves are figure-derived and indicative).
- On 49 Atari games it beat A2C on both scoring metrics and was competitive with ACER (winning more games on the "avg reward over all of training" metric) while being much simpler (Table 2, parse).

## Limitations / future work

The conclusion frames PPO as combining trust-region stability with first-order simplicity and broad applicability; the parse does not enumerate explicit limitations beyond noting the adaptive-KL variant underperforms the clipped objective. Explicit future-work targets are `not in parse`.

## Relation to the corpus

The **method ancestor** of the wiki's large PPO lineage. The [[ppo]] concept page summarizes this algorithm; the hybrid-action variant [[j-ppo]] in [[liu-2026-jppo-en-convntm]] generalizes its probability ratio to mixed continuous/discrete actions, the multi-agent extension [[mappo]] appears in [[kang-2023-mappo-hierarchical-aerial]] and others, the evolutionary multi-objective PPO of [[song-2024-mol-aoi-energy]] and [[sun-2025-emoppo-vlh-aerial-cb]] builds on it, and [[lee-2024-dho-leo-handover]] uses a PPO/IMPALA backbone. Curating the source paper grounds those downstream claims, just as [[fujimoto-2018-td3-actor-critic]] grounds the TD3 line.

## Raw artifacts

- `raw/sources/Proximal Policy Optimization Algorithms/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
