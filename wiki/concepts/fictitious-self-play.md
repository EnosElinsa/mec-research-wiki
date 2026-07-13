---
type: concept
title: "Fictitious Self-Play"
tags: [game-theory, equilibrium-learning, multi-agent-learning]
related:
  - "[[stochastic-game]]"
  - "[[potential-game]]"
  - "[[nash-equilibrium]]"
  - "[[multi-agent-q-learning]]"
  - "[[communication-constrained-marl]]"
  - "[[jia-2026-ufsp-rail-inspection]]"
  - "[[yin-2026-uav-antijamming-nfsp]]"
created: 2026-07-06
updated: 2026-07-14
---

# Fictitious Self-Play

Fictitious self-play is a decentralized equilibrium-learning pattern where each agent alternates between learning a best response to its current belief about other agents and updating an averaged policy from empirical play. It is useful when agents interact repeatedly but do not have complete, current global state.

In this wiki, [[jia-2026-ufsp-rail-inspection]] adapts the pattern to multi-UAV rail-line inspection under imperfect information. Each UAV uses local observations plus lightweight aggregate feedback, learns a Q-learning best response against its belief, and averages strategies over time. The paper proves the rail-inspection game is an exact [[potential-game]] and uses the FSP-style process to drive the system toward a [[nash-equilibrium]].

This is different from standard [[centralized-training-decentralized-execution]] MARL: U-FSP is explicitly designed around private UAV state, delayed / stale peer information, and belief updates rather than a central critic with full training-time state.

[[yin-2026-uav-antijamming-nfsp]] combines neural fictitious self-play with recurrent dueling double Q-learning for [[implicit-opponent-modeling]] between a communicating UAV and an adaptive mobile jammer.
