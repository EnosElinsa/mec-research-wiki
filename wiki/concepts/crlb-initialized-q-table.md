---
type: concept
title: "CRLB-Initialized Q-Table"
tags: [reinforcement-learning, q-learning, isac, cramer-rao-bound, prior-knowledge]
related:
  - "[[zhu-2025-green-isac-q-learning]]"
  - "[[improved-fast-base-station-selection]]"
  - "[[multi-agent-q-learning]]"
  - "[[cramer-rao-bound]]"
created: 2026-07-14
updated: 2026-07-14
---

# CRLB-Initialized Q-Table

A CRLB-initialized Q-table injects sensing geometry into tabular communication control before online learning. Actions that associate a selected UAV anchor with a ground terminal receive an initial value proportional to inverse positioning CRLB in the QoS-satisfied state; other entries start at zero.

[[zhu-2025-green-isac-q-learning]] periodically recomputes these priors as the UAV geometry changes, then continues independent [[multi-agent-q-learning]]. The prior can accelerate the tested learning process, but it does not convert the communication reward into a joint sensing-communication optimum or establish convergence of the paper's nonstandard monotone Q update.
