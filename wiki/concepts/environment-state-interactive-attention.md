---
type: concept
title: "Environment-State Interactive Attention"
tags: [attention, state-representation, uav-trajectory, aerial-ris]
related:
  - "[[feng-2026-aerial-ris-secure]]"
  - "[[uav-trajectory-control]]"
  - "[[phase-aware-relativistic-adaptive-descent]]"
  - "[[td3]]"
created: 2026-07-14
updated: 2026-07-14
---

# Environment-State Interactive Attention

Environment-State Interactive Attention (ESIA) builds a trajectory-control representation by querying environment features with the current UAV position. CSI, user positions, and UAV velocity form attention keys, while those features plus the previous UAV position form values.

In [[feng-2026-aerial-ris-secure]], ESIA feeds the trajectory-specialist TD3 agent and complements [[phase-aware-relativistic-adaptive-descent]] in the beamforming specialist. The paper attributes improved simulated GPS-noise robustness to this fusion, but it does not establish a general noise-filtering guarantee.
