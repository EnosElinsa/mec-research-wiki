---
type: concept
title: "Dynamic Target Prioritization Metric"
tags: [metric, freshness, uav, target-tracking, vehicular-networks]
related:
  - "[[hazarika-2026-dynamo-uav-vehicle-tracking]]"
  - "[[age-of-information]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[uav-enabled-its]]"
  - "[[cramer-rao-bound]]"
  - "[[maddpg]]"
created: 2026-07-10
updated: 2026-07-10
---

# Dynamic Target Prioritization Metric

Dynamic Target Prioritization Metric (DTPM) is the freshness-and-urgency metric in [[hazarika-2026-dynamo-uav-vehicle-tracking]]. It combines elapsed update time, trajectory adherence through Frechet distance, prediction uncertainty, SINR, and distance-aware quality to decide which fast-moving vehicle a UAV team should refresh next.

DTPM is a richer target-tracking complement to [[age-of-information]]. AoI captures how old the last update is, while DTPM also asks whether the predicted trajectory is drifting, how uncertain the prediction is, and whether the communication/sensing link is good enough for a useful update.
