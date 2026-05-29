---
type: concept
title: "Multi-Agent TD3 (MATD3)"
tags: [drl, multi-agent, off-policy, ctde]
related:
  - "[[td3]]"
  - "[[masac]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[prioritized-experience-replay]]"
  - "[[shao-2024-drl-antijamming-mec]]"
created: 2026-05-29
updated: 2026-05-29
---

# Multi-Agent TD3 (MATD3)

The multi-agent extension of [[td3]]: each agent runs a TD3 actor-critic (clipped double Q-learning, target policy smoothing, delayed actor updates), trained under [[centralized-training-decentralized-execution]] — critics see joint observations/actions during training while agents act on local observations at execution. This is the deterministic analogue of [[masac]] (which uses stochastic, entropy-regularized policies).

In the wiki, [[shao-2024-drl-antijamming-mec]] uses **PER-MATD3**, combining MATD3 with [[prioritized-experience-replay]], for cooperative resource management (CPU frequency, bandwidth, channel selection) across UAVs under jamming. It argues convergence via clipped double Q-learning even under adversarial interference.
