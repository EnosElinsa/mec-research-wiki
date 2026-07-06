---
type: concept
title: "Regret-Minimization Learning"
tags: [game-theory, reinforcement-learning, multi-agent, channel-allocation]
related:
  - "[[stochastic-game]]"
  - "[[multi-agent-q-learning]]"
  - "[[fan-2026-parallel-caching-uav-mec]]"
created: 2026-07-07
updated: 2026-07-07
---

# Regret-Minimization Learning

A multi-agent learning pattern where agents update policies based on the regret of not having chosen alternative actions. In [[fan-2026-parallel-caching-uav-mec]], the upper-layer channel-allocation problem is modeled as a [[stochastic-game]], and regret minimization is used to approach a correlated-equilibrium channel profile across UAV agents after lower-layer DQN selects local caching/offloading decisions.
