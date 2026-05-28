---
type: comparison
title: DDPG vs j-PPO for UAV-MEC
tags: [drl, comparison, action-space]
related:
  - "[[j-ppo]]"
  - "[[hybrid-action-decision-making]]"
  - "[[hybrid-action-beats-pure-drl]]"
  - "[[liu-2026-jppo-en-convntm]]"
created: 2026-05-28
updated: 2026-05-28
---

# DDPG vs j-PPO for UAV-MEC

| Aspect | DDPG | j-PPO |
|---|---|---|
| Action space | Continuous only (deterministic) | Hybrid continuous + discrete |
| Update style | Off-policy, replay buffer | On-policy, clipped surrogate |
| Discrete decisions | Must threshold a continuous output (lossy) | Native discrete head |
| Stability | Sensitive to noise process and target-network lag | Clipped trust region keeps updates bounded |
| Multi-objective reward | Works, but value estimates are noisy | Works, with explicit VF + entropy terms |
| Reported $\Omega$ in [[liu-2026-jppo-en-convntm]] (Fig. 6) | Severe degradation | Highest among all baselines |

## Why this matters in [[multi-uav-assisted-mec]]

Charging is binary. Offloading-ratio quantization is effectively discrete. DDPG's continuous-only action head can't represent these crisply, and the policy lands in a bad local optimum where it almost never charges (energy violation penalty) or always charges (zero data collection).

`j-PPO+EN-ConvNTM` sidesteps this entirely by routing the discrete components through a separate categorical/Bernoulli head — see [[j-ppo]] for the formal probability ratio.

## Caveat

DDPG with a *separate* discrete-action critic (e.g. P-DQN or hybrid TD3 variants) would be a fairer comparison than vanilla DDPG. The paper does not explore those.
