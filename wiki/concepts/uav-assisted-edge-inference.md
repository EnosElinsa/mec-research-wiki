---
type: concept
title: "UAV-Assisted Edge Inference"
tags: [uav, edge-ai, edge-inference, iscc, task-oriented-communication]
related:
  - "[[wen-2026-uav-edge-inference-iscc]]"
  - "[[integrated-sensing-computation-communication]]"
  - "[[discriminant-gain]]"
  - "[[task-oriented-communication]]"
  - "[[uav-trajectory-control]]"
created: 2026-07-07
updated: 2026-07-07
---

# UAV-Assisted Edge Inference

UAV-assisted edge inference uses a UAV as a mobile relay or edge node for AI inference pipelines whose sensing devices cannot reliably reach a fixed edge server. In [[wen-2026-uav-edge-inference-iscc]], ground devices sense and extract local features, the UAV sequentially visits them to collect quantized feature vectors, and the edge server performs final classification.

The concept connects [[integrated-sensing-computation-communication]] to [[uav-trajectory-control]]: downstream inference accuracy is represented by [[discriminant-gain]], while the UAV access route, hovering locations, sensing power, computation frequency, and transmission parameters determine the end-to-end delay.
