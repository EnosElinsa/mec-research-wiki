---
type: concept
title: "Post-Decision-State Stackelberg Actor-Critic"
tags: [reinforcement-learning, actor-critic, stackelberg-game, leader-follower, post-decision-state]
related:
  - "[[yao-2026-transformer-mean-field-isac-sagin]]"
  - "[[transformer-encoded-mean-field-reinforcement-learning]]"
  - "[[stackelberg-game]]"
  - "[[mean-field-game]]"
created: 2026-07-13
updated: 2026-07-13
---

# Post-Decision-State Stackelberg Actor-Critic

A post-decision-state Stackelberg actor-critic inserts an intermediate state after the leader commits an action but before followers complete their response. The follower policy can condition directly on that committed action, while the leader value update evaluates the downstream follower reaction.

[[yao-2026-transformer-mean-field-isac-sagin]] uses this construction for a satellite leader and UAV followers. The follower population is summarized by [[transformer-encoded-mean-field-reinforcement-learning]], and the post-decision state connects the satellite beamforming decision to UAV trajectory, association, sensing-role, and beamforming responses.

The construction operationalizes sequential dependence in a [[stackelberg-game]] within actor-critic learning. In the cited source it is an algorithmic state representation rather than an equilibrium theorem: empirical reward convergence does not prove existence, uniqueness, or recovery of a Stackelberg equilibrium.
