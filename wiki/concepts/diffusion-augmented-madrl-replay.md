---
type: concept
title: "Diffusion-Augmented MADRL Replay"
tags: [multi-agent-reinforcement-learning, diffusion, experience-replay, data-augmentation]
related:
  - "[[wu-2026-sensing-error-uav-scheduling]]"
  - "[[generative-diffusion-model]]"
  - "[[deep-q-network]]"
  - "[[sensing-error-aware-communication-rate]]"
created: 2026-07-14
updated: 2026-07-14
---

# Diffusion-Augmented MADRL Replay

Experience-replay augmentation in which a diffusion model learns the distribution of complete multi-agent transition tuples and generates additional transitions for policy or value-network training. Real and synthetic samples are mixed at a controlled ratio so the learner can encounter a broader set of modeled disturbances without making diffusion the action-selection policy.

[[wu-2026-sensing-error-uav-scheduling]] trains a fully connected [[generative-diffusion-model]] on `(state, action, reward, next state)` tuples containing sensing-error effects. Each MADQN minibatch combines generated and real replay samples, while epsilon-greedy [[deep-q-network|DQN]] agents still select UAV scheduling actions. This differs from a diffusion policy or a diffusion model used directly as an optimizer.

Generated transitions need feasibility and consistency controls when actions are constrained. The source calls its generated tuples valid but does not define a filter for binary association, bandwidth, motion, QoS, sensing constraints, or reward-channel consistency; it also does not explain how its stated continuous position and bandwidth actions are represented by DQN.
