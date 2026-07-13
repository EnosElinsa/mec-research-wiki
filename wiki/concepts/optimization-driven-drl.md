---
type: concept
title: "Optimization-Driven Deep Reinforcement Learning"
tags: [deep-reinforcement-learning, optimization, informed-target, hybrid-action, robust-control]
related:
  - "[[ding-2026-optimization-driven-spectrum-sharing]]"
  - "[[heuristic-supervised-drl]]"
  - "[[expert-guided-warm-start-rl]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[hybrid-action-decision-making]]"
created: 2026-07-13
updated: 2026-07-13
---

# Optimization-Driven Deep Reinforcement Learning

Optimization-driven DRL uses a model-based solver to generate actions or return targets that guide a learned policy. The optimizer contributes structured, constraint-aware estimates during training; the neural policy provides lower-cost execution and adaptation after training.

In [[ding-2026-optimization-driven-spectrum-sharing]], a robust alternating SCA/CVX module computes offline lower-bound actions and targets under jammer-CSI uncertainty. A gate substitutes those targets/actions when they exceed the conventional DQN-DDPG estimate. This differs from [[heuristic-supervised-drl]], which learns a supervised bridge to a heuristic, and from a simple replay warm start because optimization targets continue to shape value updates.
