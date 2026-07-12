---
type: concept
title: Hybrid Continuous–Discrete Action Decision-Making
tags: [drl, action-space]
related:
  - "[[j-ppo]]"
  - "[[ppo]]"
  - "[[chen-2026-pddqn-sagin-mec]]"
  - "[[liu-2026-jppo-en-convntm]]"
  - "[[hybrid-action-beats-pure-drl]]"
  - "[[qin-2023-symmetry-augmented-uav-isac]]"
created: 2026-05-28
updated: 2026-07-12
---

# Hybrid Continuous–Discrete Action Decision-Making

A class of control problems where the action vector at each step contains both real-valued and categorical components. In UAV-MEC:

| Component | Type | Distribution |
|---|---|---|
| UAV position increment $\Delta Q_{u,n}$ | continuous | Gaussian |
| Offload ratio $\lambda_{u,d,n}$ | continuous on $[0,1]$ | beta or clipped Gaussian |
| Charging indicator $\xi_{u,n}$ | binary | Bernoulli |

Most off-the-shelf DRL algorithms target one side or the other:

- DDPG / TD3 / SAC — continuous-only via deterministic or stochastic Gaussian policies
- DQN — discrete-only via Q-values
- A2C / PPO — formally support either, but a single shared policy network must be set up carefully

The cleanest empirical fix in [[liu-2026-jppo-en-convntm]] is [[j-ppo]]: keep a unified actor-critic, but split the probability ratio between the two action types and weight them with $c_3$. See [[hybrid-action-beats-pure-drl]].

[[chen-2026-pddqn-sagin-mec]] adds a SAGIN instance: discrete scheduling/satellite-association actions are paired with continuous offloading-ratio and transmit-power parameters, handled by a P-DDQN design that combines DDQN and DDPG.
