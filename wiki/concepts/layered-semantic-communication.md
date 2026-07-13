---
type: concept
title: "Layered Semantic Communication"
tags: [semantic-communication, joint-source-channel-coding, uav, position-adaptation]
related:
  - "[[lin-2026-layered-semantic-uav-aggregation]]"
  - "[[semantic-communication]]"
  - "[[semantic-reference-signal-matching]]"
  - "[[noma]]"
  - "[[uav-data-collection]]"
created: 2026-07-14
updated: 2026-07-14
---

# Layered Semantic Communication

A semantic communication architecture that separates reusable feature extraction and reconstruction from adaptation to the current channel or deployment geometry. A base joint source-channel codec is trained under a reference condition and frozen; a second layer adjusts transmitted and received semantic signals, and optionally infrastructure position, without retraining the codec for every geometry.

[[lin-2026-layered-semantic-uav-aggregation]] applies this separation to multi-user image uploads over OFDM-[[noma|NOMA]] to a hovering UAV. Its semantic-feature-extraction layer supplies the frozen encoders and decoder, while the position-and-processing-coordination layer either uses learned channel-aware signal processors or alternating signal-scaling and UAV-position optimization. Both variants use [[semantic-reference-signal-matching]] to align changed-channel observations with the frozen decoder's reference input.

Layering reduces the need to store or retrain a codec for each UAV-user distance, but it does not remove adaptation cost or channel assumptions. The source requires perfect real-time CSI at users and the UAV, fixes user grouping and altitude in the main design, and evaluates only simulated CIFAR-10 reconstruction.
