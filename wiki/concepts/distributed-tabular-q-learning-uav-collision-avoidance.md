---
type: concept
title: "Distributed Tabular Q-Learning for UAV Collision Avoidance"
tags: [q-learning, collision-avoidance, decentralized-control, uav]
related:
  - "[[hsu-2022-collision-avoidance-trajectory]]"
  - "[[safe-reinforcement-learning]]"
  - "[[uav-trajectory-control]]"
  - "[[autonomous-uav-swarms]]"
created: 2026-07-14
updated: 2026-07-14
---

# Distributed Tabular Q-Learning for UAV Collision Avoidance

Distributed tabular Q-learning for UAV collision avoidance lets each aircraft choose a heading adjustment from quantized local relative observations without knowing other trajectories in advance. Offline learning produces a state-action table used for online lookup, while planned mission routes remain a separate input.

[[hsu-2022-collision-avoidance-trajectory]] represents at most two nearby UAVs in each state and falls back to an identifier-based altitude change for denser encounters. Its simulated collision avoidance is not a formal safety guarantee, so it remains adjacent to [[safe-reinforcement-learning]] rather than an instance of certified safe control.
