---
type: concept
title: "Goal-Oriented Semantic Twinning"
tags: [digital-twin, semantic-communication, state-inference, satellite-edge, task-oriented]
related:
  - "[[liao-2026-semantic-twinning-tracking]]"
  - "[[digital-twin]]"
  - "[[semantic-communication]]"
  - "[[age-of-information]]"
  - "[[edge-intelligence]]"
created: 2026-07-13
updated: 2026-07-13
---

# Goal-Oriented Semantic Twinning

Goal-oriented semantic twinning maintains only the virtual state, precision, and update frequency needed by a current task. Instead of transmitting a full digital twin at every cycle, it treats variables that can infer others as significant, samples those variables frequently, and sparsely resamples reconstructed variables for validation.

[[liao-2026-semantic-twinning-tracking]] combines ARIMA, KF/UIF, GAT, and causal inference for missing satellite-UAV tracking state, then uses the reconstructed twin for radio scheduling and cluster control. This extends [[semantic-communication]] from content selection to the structure and synchronization policy of the [[digital-twin]] itself.
