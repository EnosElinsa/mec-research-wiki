---
type: concept
title: "Action-Masked Hierarchical DRL"
tags: [drl, hierarchical, action-masking, constraints, ddqn]
related:
  - "[[bayessa-not-in-parse-uav-isac-secure-content-hdrl]]"
  - "[[hierarchical-reinforcement-learning]]"
  - "[[ddqn]]"
  - "[[two-timescale-optimization]]"
  - "[[service-caching-mec]]"
  - "[[cramer-rao-bound]]"
created: 2026-07-11
updated: 2026-07-11
---

# Action-Masked Hierarchical DRL

Action-masked hierarchical DRL decomposes a constrained control problem into levels or timescales, then removes infeasible actions from the policy's candidate set before action selection. The hierarchy keeps slow decisions from being relearned every slot, while the mask protects the learner from wasting updates on choices that violate hard constraints.

In [[bayessa-not-in-parse-uav-isac-secure-content-hdrl]], the hierarchy separates long-timescale content caching from short-timescale user association, UAV deployment, communication beamforming, and sensing beamforming. The long-timescale layer uses DDQN for caching. The short-timescale layer uses attention-based DDQN with an action mask so infeasible association/deployment/beamforming combinations are omitted before Q-value evaluation.

The pattern is narrower than general [[hierarchical-reinforcement-learning]]: it is not mainly about learned options or reusable skills. Its role is engineering decomposition for a mixed-timescale, mixed-discrete constrained wireless-control problem.
