---
type: concept
title: "Parameter Sharing in Multi-Agent Reinforcement Learning"
tags: [multi-agent-reinforcement-learning, parameter-sharing, scalability, homogeneous-agents, ctde]
related:
  - "[[chen-2026-hammurabi-cooperation]]"
  - "[[wang-2026-robust-multiuav-jtcra]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[pretrained-policy-cooperation-shaping]]"
created: 2026-07-13
updated: 2026-07-13
---

# Parameter Sharing in Multi-Agent Reinforcement Learning

Parameter sharing trains one actor or value function for multiple homogeneous agents while allowing their observations to produce different actions. It reduces model count, pools experience, and supports fleet-size changes when agents have compatible observation and action spaces.

[[chen-2026-hammurabi-cooperation]] shares a UAV coverage policy before game-diagnosed reward shaping. [[wang-2026-robust-multiuav-jtcra]] separates heterogeneous trajectory and communication roles, then shares parameters only within each homogeneous role. The pattern improves scalability but does not remove partial observability or guarantee that all agents converge to a socially desirable equilibrium.
