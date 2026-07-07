---
type: concept
title: "Distributional Reinforcement Learning"
tags: [reinforcement-learning, return-distribution, multi-agent-rl]
related:
  - "[[value-decomposition-network]]"
  - "[[multi-agent-q-learning]]"
  - "[[deep-q-network]]"
  - "[[zhu-2024-zdrl-uav-tracking]]"
  - "[[uav-localization-under-jamming]]"
  - "[[zhu-2026-uav-localization-jamming]]"
created: 2026-06-02
updated: 2026-07-07
---

# Distributional Reinforcement Learning

A reinforcement-learning paradigm that learns the full **probability distribution of the return** (the sum of future rewards) instead of only its expected value (the scalar Q/value used by standard RL). Modeling the return distribution gives a richer, more stable learning signal and lets a policy reason about the spread of outcomes, not just the mean.

In [[zhu-2024-zdrl-uav-tracking]], a **Z function decomposition based RL (ZD-RL)** method applies this idea to a cooperative multi-UAV tracking problem: it decomposes a global **Z function** (the return distribution) across agents, in contrast to expectation-based [[value-decomposition-network|value-function decomposition]] (VD-RL). Learning the distribution of the sum of future rewards — rather than its expectation — is credited with more accurate value estimation, better efficiency, and improved training stability, and the method reports up to 39.4% / 64.6% lower positioning error than VD-RL / independent deep RL respectively.

[[zhu-2026-uav-localization-jamming]] applies the same distribution-aware value-estimation logic to [[uav-localization-under-jamming]], approximating individual value-function distributions with mixture Gaussians while the BS switches between GAN-based and TDOA-based positioning.

Contrast with the expectation-based multi-agent methods elsewhere in the corpus ([[value-decomposition-network]], [[multi-agent-q-learning]]).
