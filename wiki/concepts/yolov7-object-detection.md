---
type: concept
title: "YOLOv7 Object Detection"
tags: [perception, computer-vision, object-detection]
related:
  - "[[mmwave-radar-sensing]]"
  - "[[multi-source-data-fusion]]"
  - "[[perception-aided-offloading]]"
  - "[[gao-2024-sagin-perception-offloading]]"
  - "[[du-2024-yolo-semcom-digital-twin]]"
created: 2026-05-29
updated: 2026-06-02
---

# YOLOv7 Object Detection

A real-time single-stage convolutional object detector from the YOLO ("You Only Look Once") family. It classifies and localizes objects in a single forward pass, making it suitable for onboard, latency-sensitive perception.

In the wiki, [[gao-2024-sagin-perception-offloading]] uses YOLOv7 for vision-based recognition of ground-device/object **type** and behavior, which is fused ([[multi-source-data-fusion]]) with [[mmwave-radar-sensing]] range/velocity/angle estimates and injected into the DRL state for [[perception-aided-offloading]]. The wiki treats YOLOv7 as a perception building block; the paper assumes its recognition is effective and does not model detection error as a degrading factor.

[[du-2024-yolo-semcom-digital-twin]] instead **modifies** the detector: it slims YOLOv7-X with an ELAN-H module (HorNet recursive gated convolution) and a parameter-free SimAM 3-D attention module ("YOLOv7-HS") to fit edge devices, and uses the detector's per-object **confidence** as the importance signal driving [[semantic-communication]] power allocation.
