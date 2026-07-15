---
type: concept
title: "Compliance-Aware UAV Trajectory Planning"
tags: [uav, trajectory-control, safety, compliance, low-altitude-economy]
related:
  - "[[low-altitude-intelligent-network]]"
  - "[[uav-trajectory-control]]"
  - "[[safe-reinforcement-learning]]"
  - "[[soft-actor-critic]]"
  - "[[llm-assisted-resource-allocation]]"
  - "[[gong-2026-safe-economic-lae-trajectory]]"
  - "[[target-level-of-safety]]"
  - "[[jiang-2026-bi-level-uav-delivery-safety]]"
  - "[[vitale-2026-density-aware-4d-trajectory]]"
  - "[[uav-trajectory-safety-guarantee-ladder]]"
created: 2026-07-07
updated: 2026-07-14
---

# Compliance-Aware UAV Trajectory Planning

Compliance-aware trajectory planning treats airspace rules as part of the control problem, not as an after-the-fact filter. The trajectory must satisfy physical safety constraints such as collision and no-fly-zone avoidance, and regulatory constraints such as speed limits in residential zones.

[[gong-2026-safe-economic-lae-trajectory]] grounds this concept for low-altitude data collection. Its POMDP includes obstacle avoidance, no-fly zones, residential-zone speed limits, landing, and energy constraints; a hybrid SAC-LLM training loop uses LLM reasoning only when nearby obstacles or constrained regions make safety and compliance salient.

[[jiang-2026-bi-level-uav-delivery-safety]] adds an explicit risk-threshold variant for delivery: every planned path segment must satisfy a [[target-level-of-safety]] constraint, so risk remains a hard feasibility condition rather than only a weighted objective term.
