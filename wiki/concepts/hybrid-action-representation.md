---
type: concept
title: "Hybrid Action Representation (latent space)"
tags: [drl, hybrid-action, representation-learning, vae]
related:
  - "[[hybrid-action-decision-making]]"
  - "[[td3]]"
  - "[[parameterized-dqn]]"
  - "[[j-ppo]]"
  - "[[hao-2024-clp-multiuav-priority-offloading]]"
created: 2026-05-29
updated: 2026-05-29
---

# Hybrid Action Representation (latent space)

A learned latent-space encoding of a coupled **discrete-continuous** action (e.g. a discrete offloading index plus continuous trajectory/power/compute parameters), following the HyAR approach (Li et al. 2022). A shared learnable **embedding table** maps each discrete action to a continuous vector, and a **conditional VAE** maps the continuous parameters into a Gaussian latent variable conditioned on state and the discrete embedding. Decoding uses nearest-neighbor lookup in the embedding table (discrete) plus the VAE decoder (continuous); a dynamics-prediction head can regularize the latent space.

The point: directly rounding a continuous actor's output to a discrete action (as plain [[ddpg]] would) collapses distinct values onto the same action and degrades performance. Encoding the *whole coupled* action preserves discrete-continuous correlations.

In the wiki, [[hao-2024-clp-multiuav-priority-offloading]]'s CLP combines this representation with [[td3]]. It is one of three ways the corpus handles [[hybrid-action-decision-making]] — alongside [[parameterized-dqn]] (P-DQN) and the dual-head [[j-ppo]].
