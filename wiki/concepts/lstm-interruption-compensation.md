---
type: concept
title: "LSTM Interruption Compensation"
tags: [lstm, uav-swarm, intermittent-connectivity, prediction, multi-agent-reinforcement-learning]
related:
  - "[[qi-2026-ocma-ddqn-data-collection]]"
  - "[[opportunistic-cooperative-multi-uav-ddqn]]"
  - "[[experience-value-circles]]"
  - "[[attentive-memory-integrated-information-exchange]]"
  - "[[constraint-regimes-in-uav-data-collection]]"
created: 2026-07-14
updated: 2026-07-14
---

# LSTM Interruption Compensation

LSTM interruption compensation predicts a disconnected neighbor's next action from its recent action, position, and local-map sequence. A confidence threshold admits a prediction only when its Softmax score is high enough; otherwise the agent retains the last valid neighbor state.

[[qi-2026-ocma-ddqn-data-collection]] trains this predictor online within each episode to bridge short UAV-to-UAV outages. Reported accuracy remains high for the first two missing steps in the tested grid, but long outages, rapidly changing interference, and prediction errors can make stale inferred state unreliable.
