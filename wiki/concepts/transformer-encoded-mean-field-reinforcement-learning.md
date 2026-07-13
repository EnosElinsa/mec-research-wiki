---
type: concept
title: "Transformer-Encoded Mean-Field Reinforcement Learning"
tags: [reinforcement-learning, multi-agent, mean-field, transformer, attention, uav-swarm]
related:
  - "[[yao-2026-transformer-mean-field-isac-sagin]]"
  - "[[post-decision-state-stackelberg-actor-critic]]"
  - "[[mean-field-game]]"
  - "[[transformer-encoder]]"
  - "[[integrated-sensing-and-communication]]"
created: 2026-07-13
updated: 2026-07-13
---

# Transformer-Encoded Mean-Field Reinforcement Learning

Transformer-encoded mean-field reinforcement learning represents a population of interacting agents through attention over agent state-action tokens. It retains the mean-field goal of avoiding an explicit full joint-action model, while letting the aggregate representation depend on heterogeneous pairwise relationships rather than only an arithmetic mean.

In [[yao-2026-transformer-mean-field-isac-sagin]], a Transformer encoder processes the unordered UAV-follower tokens inside a leader-follower actor-critic for interference management. The encoded population state is coupled to [[post-decision-state-stackelberg-actor-critic|post-decision leader-follower updates]] across trajectories, beamforming, user association, and sensing-role choices.

This is narrower than [[transformer-encoder]] and adjacent to [[mean-field-game]]. It describes a learned mean-field representation, not a proof that the agents converge to a mean-field or Stackelberg equilibrium. Self-attention also has quadratic token complexity, so reducing the explicit joint-action dimension does not by itself establish sublinear scaling in the number of agents.
