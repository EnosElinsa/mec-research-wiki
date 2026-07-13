---
type: concept
title: "Mixture-of-Experts DRL"
tags: [drl, multi-task-learning, neural-architecture, generalization]
related:
  - "[[ddpg]]"
  - "[[meta-deep-reinforcement-learning]]"
  - "[[ye-2026-mode-lae-isac]]"
  - "[[ye-2026-meta-deepesc-lae-isac]]"
  - "[[guo-2026-event-triggered-sinr-navigation]]"
created: 2026-07-07
updated: 2026-07-07
---

# Mixture-of-Experts DRL

A DRL architecture that uses a gating network to route states or tasks through shared expert networks and task-specific output layers. In [[ye-2026-mode-lae-isac]], the experts are embedded inside a [[ddpg]] actor-critic controller so multiple objective-preference weights in a low-altitude ISAC problem are trained concurrently. This lets the controller generalize to unseen communication/sensing tradeoff weights without retraining a separate policy from scratch.

[[guo-2026-event-triggered-sinr-navigation]] uses the sparse value-based variant: a Top-1 router activates one expert per D3QN decision after shared map/position encoding. This keeps active parameters and latency nearly constant while retaining a larger total expert capacity.
