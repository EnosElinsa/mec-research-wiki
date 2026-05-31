---
type: concept
title: "Video Analytics Offloading"
tags: [video, dnn-inference, mec, workload-class]
related:
  - "[[task-offloading]]"
  - "[[video-transcoding-tradeoff]]"
  - "[[qoe-modeling-mec]]"
  - "[[bao-2025-ddpg-video-offloading]]"
  - "[[sun-2024-ues-video-analytics-disaster]]"
created: 2026-05-29
updated: 2026-06-01
---

# Video Analytics Offloading

A workload class in which streaming video must run through DNN inference (object detection, classification, anomaly detection) under tight latency. Distinct from generic task offloading because:

- The data is large (Mb/s of pixels) and **lossy-compressible** — see [[video-transcoding-tradeoff]].
- The DNN's accuracy depends on input quality, so compression isn't free.
- Inference cost grows polynomially with input bit-volume; transcoding to lower bitrate reduces both the transmission and the inference cost.

In the wiki, [[bao-2025-ddpg-video-offloading]] is the canonical entry: video offload split between local UAV inference and HAP inference after transcoding. The QoE objective ([[qoe-modeling-mec]]) explicitly weighs delay against video quality, since pure-delay objectives drive the policy to over-compress. [[sun-2024-ues-video-analytics-disaster]] is the **disaster-rescue** variant: a UAV-mounted edge server offloads smart-camera video analytics under the cameras' **battery constraints**, with the objective being the camera-network lifetime rather than per-task QoE.

Distinct from the **cooperative perception** workload of [[xie-2026-uav-multisource-fusion]], which fuses raw observations from multiple sensors instead of running a per-stream DNN.
