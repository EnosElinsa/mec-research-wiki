---
type: concept
title: "Multi-Agent Transformer"
tags: [multi-agent-reinforcement-learning, transformer, autoregressive-policy, attention]
related:
  - "[[wang-2026-mat-target-tracking]]"
  - "[[transformer-encoder]]"
  - "[[sequential-multi-agent-policy-generation]]"
  - "[[ma-pomdp]]"
  - "[[ppo]]"
created: 2026-07-13
updated: 2026-07-13
---

# Multi-Agent Transformer

A Multi-Agent Transformer (MAT) represents a cooperative joint policy with an encoder-decoder Transformer. Self-attention contextualizes all agents' observations; a masked autoregressive decoder then generates an ordered action sequence, conditioning each later action on preceding actions. Multi-agent advantage decomposition and a PPO-style clipped objective provide the learning target.

In [[wang-2026-mat-target-tracking]], MAT controls UAV velocity changes after Hungarian assignment to virtual sensing points around a TDOA target estimate. The design combines [[transformer-encoder]] context with [[sequential-multi-agent-policy-generation]], but its joint observation and autoregressive action dependencies should not be described as communication-free decentralized execution.
