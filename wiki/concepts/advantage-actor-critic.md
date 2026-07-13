---
type: concept
title: "Advantage Actor-Critic"
tags: [reinforcement-learning, actor-critic, policy-gradient, on-policy]
related:
  - "[[ammar-2026-oran-maritime-slicing]]"
  - "[[ppo]]"
  - "[[hybrid-action-decision-making]]"
created: 2026-07-13
updated: 2026-07-13
---

# Advantage Actor-Critic

Advantage actor-critic (A2C) is an on-policy method that updates a stochastic actor using an advantage estimate while a critic learns the state-value function. Synchronous workers can collect short rollouts and average gradients, trading lower sample reuse for rapid adaptation to current environment dynamics.

[[ammar-2026-oran-maritime-slicing]] compares A2C with [[ppo]] after discretizing VNF, resource, and UAV-movement controls. In that simulation A2C converges faster and adapts better as maritime load grows, but fluctuates more and offers no global-optimality guarantee.
