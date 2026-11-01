---
type: concept
title: "3GPP UAV LoS Probability Model"
tags: [channel-model, los-probability, cellular-uav, urban-macro, urban-micro]
related:
  - "[[ren-2026-distributed-uav-los]]"
  - "[[air-to-ground-channel-model]]"
  - "[[blockage-aware-channel-model]]"
  - "[[al-hourani-2020-urban-los-probability]]"
  - "[[al-hourani-2024-los-holding-distance-ntn]]"
created: 2026-07-14
updated: 2026-11-02
---

# 3GPP UAV LoS Probability Model

A piecewise statistical model for cellular air-to-ground visibility whose LoS probability changes with horizontal distance, UAV height, and urban macrocell or microcell deployment. [[ren-2026-distributed-uav-los]] uses the 3GPP TR 36.777 form to separate LoS and NLoS serving-distance and capacity behavior; in its Manhattan comparison, this model tracks ray-tracing results more closely than the evaluated ITU alternative.

Geometry-based alternatives appear in [[al-hourani-2020-urban-los-probability]], which derives LoS probability from building statistics for any endpoint heights, and [[al-hourani-2024-los-holding-distance-ntn]], which models LoS state duration along a path.
