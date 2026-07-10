---
type: concept
title: "Multi-Scale U-Net Pathloss Prediction"
tags: [channel-model, pathloss-prediction, deep-learning, uav-communications]
related:
  - "[[hussain-2026-unet-uav-mmwave-pathloss]]"
  - "[[air-to-ground-channel-model]]"
  - "[[blockage-aware-channel-model]]"
  - "[[radio-map-assisted-channel-estimation]]"
  - "[[low-altitude-intelligent-network]]"
created: 2026-07-10
updated: 2026-07-10
---

# Multi-Scale U-Net Pathloss Prediction

Multi-scale U-Net pathloss prediction uses spatial input maps and encoder-decoder convolutions to estimate radio pathloss over a grid. [[hussain-2026-unet-uav-mmwave-pathloss]] uses log-distance, LoS mask, and building-mask channels, then combines multi-scale convolution branches with an ASPP bottleneck.

Within the wiki this concept belongs to the data-driven branch of [[air-to-ground-channel-model]] and [[blockage-aware-channel-model]]. It is adjacent to [[radio-map-assisted-channel-estimation]], but it predicts pathloss maps from geometry-derived features rather than completing CSI from a route-indexed radio map.
