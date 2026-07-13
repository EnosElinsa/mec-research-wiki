---
type: concept
title: PPO (Proximal Policy Optimization)
tags: [drl, policy-gradient, on-policy]
related:
  - "[[wang-2026-ikpp-vehicular-uav]]"
  - "[[xie-2026-uav-irs-eppo]]"
  - "[[j-ppo]]"
  - "[[gae]]"
  - "[[liu-2026-jppo-en-convntm]]"
  - "[[schulman-2017-ppo]]"
  - "[[wang-2025-ppo-uav-positioning-offloading]]"
  - "[[wu-2026-model-based-ppo-ris-uav-mec]]"
  - "[[beishenalieva-2026-secrecy-aware-uav-path-planning]]"
  - "[[hua-2026-ddrl-content-delivery]]"
created: 2026-05-28
updated: 2026-07-13
---

# PPO (Proximal Policy Optimization)

Schulman et al.'s on-policy actor-critic algorithm that constrains each update to remain "proximal" to the previous policy via a clipped surrogate objective (origin paper curated as [[schulman-2017-ppo]]). Standard form:

$$
L_n^{\text{CLIP}}(\theta) = \mathbb{E}_n\big[\min(g_n(\theta) A_n,\; \text{clip}(g_n(\theta), 1-\varepsilon, 1+\varepsilon) A_n)\big]
$$

with $g_n(\theta) = \pi_\theta(\mathbf{a}_n|\mathbf{h}_n) / \pi_{\theta_\text{old}}(\mathbf{a}_n|\mathbf{h}_n)$ and $A_n$ a [[gae|GAE]] estimate.

When the policy and value heads share parameters, the loss is augmented:

$$
L_n^{\text{CLIP}+\text{VF}+\text{S}} = \mathbb{E}_n[L_n^{\text{CLIP}} - c_1 L_n^{\text{VF}} + c_2 S[\pi_\theta]]
$$

## Convergence properties (cited in [[liu-2026-jppo-en-convntm]])

- Smooth reward + compact policy space → sublinear bound $\mathbb{E}[\|\theta_k - \theta^*\|^2] \le F/k$ (Zhong & Zhang, NeurIPS 2023).
- Linear-MDP complexity bound: $O(d_{sa}^2 N_h^3 / \varepsilon^2)$.

## Adaptation in this project

The vanilla form assumes a single action distribution. The work in [[liu-2026-jppo-en-convntm]] generalizes the probability ratio to a hybrid of continuous and discrete components — see [[j-ppo]].

[[wang-2025-ppo-uav-positioning-offloading]] uses PPO for joint UAV positioning and partial task offloading in multi-UAV MEC, while [[wu-2026-model-based-ppo-ris-uav-mec]] embeds PPO in a decentralized model-based MARL loop with local dynamics rollouts for RIS-assisted urban UAV-MEC. [[beishenalieva-2026-secrecy-aware-uav-path-planning]] uses PPO-style policy-gradient control for secrecy-aware UAV path, power, and mode decisions before PSO slot allocation.

[[hua-2026-ddrl-content-delivery]] uses clipped PPO in a CNN-GRU dual-phase loop: online UAV movement and transmission decisions populate a buffer, while offline GAE-based updates retrain and redistribute the policy for multi-BS content delivery.

## Reference implementation

The hyperparameters and code structure follow [Kostrikov's PyTorch PPO](https://github.com/ikostrikov/pytorch-a2c-ppo-acktr-gail) (cited as [35]).
