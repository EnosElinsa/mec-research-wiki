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
  - "[[cheng-2026-cnn-mamba-cracks]]"
created: 2026-07-07
updated: 2026-07-13
---

# UAV-Assisted Edge Inference

UAV-assisted edge inference uses a UAV as a mobile relay or edge node for AI inference pipelines whose sensing devices cannot reliably reach a fixed edge server. In [[wen-2026-uav-edge-inference-iscc]], ground devices sense and extract local features, the UAV sequentially visits them to collect quantized feature vectors, and the edge server performs final classification.

The concept connects [[integrated-sensing-computation-communication]] to [[uav-trajectory-control]]: downstream inference accuracy is represented by [[discriminant-gain]], while the UAV access route, hovering locations, sensing power, computation frequency, and transmission parameters determine the end-to-end delay.

[[cheng-2026-cnn-mamba-cracks]] proposes combining UAV/vehicle image acquisition with a compact crack-segmentation network. Its quantitative deployment evidence is limited to an LMC-Belloch/Triton operator benchmark on Jetson AGX Orin; it does not show the model running on the proposed air-ground platform.
