---
type: concept
title: "Neural Episodic Control with State Abstraction"
tags: [reinforcement-learning, episodic-control, state-abstraction, intrinsic-reward]
related:
  - "[[xie-2026-uav-irs-eppo]]"
  - "[[ppo]]"
created: 2026-07-13
updated: 2026-07-13
---

# Neural Episodic Control with State Abstraction

An exploration aid that discretizes a continuous state into grid cells, stores an episodic score for each visited cell, and shapes reward using the current abstract-state score relative to the mean score across the episodic table. In [[xie-2026-uav-irs-eppo]], this table augments PPO for UAV trajectory learning rather than replacing the actor-critic policy.

The abstraction can accelerate exploration when nearby continuous states are behaviorally similar, but a `K`-dimensional state with `N` bins per dimension admits `N^K` cells. Its scalability and fidelity therefore depend strongly on dimension, binning, and state normalization.
