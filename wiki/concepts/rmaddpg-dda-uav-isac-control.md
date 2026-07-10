---
type: concept
title: "RMADDPG-DDA UAV-ISAC Control"
tags: [marl, maddpg, isac, uav, vehicular-networks, exploration]
related:
  - "[[wang-2026-rmaddpg-dda-uav-isac-vehicular]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[maddpg]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[multi-objective-reinforcement-learning]]"
  - "[[uav-enabled-its]]"
  - "[[cramer-rao-bound]]"
created: 2026-07-10
updated: 2026-07-10
---

# RMADDPG-DDA UAV-ISAC Control

RMADDPG-DDA is the MARL controller proposed in [[wang-2026-rmaddpg-dda-uav-isac-vehicular]] for UAV-enabled vehicular [[integrated-sensing-and-communication]]. It keeps the [[maddpg]] / [[centralized-training-decentralized-execution]] backbone, then adds random-network-distillation novelty rewards, parameter sharing, and dynamic data augmentation by permuting UAV and user identifiers.

Its role in the corpus is a concrete exploration-and-generalization variant of MADDPG for moving-vehicle ISAC. The reward is multi-objective: served vehicles, effective mutual information, and energy saving are optimized while QoS, upload-capacity, and collision constraints remain active.
