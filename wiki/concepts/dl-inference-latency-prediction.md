---
type: concept
title: "DL Inference Latency Prediction"
tags: [edge-ai, latency-prediction, scheduling]
related:
  - "[[collaborative-dl-inference]]"
  - "[[pipeline-parallel-inference]]"
  - "[[elastic-task-scheduling]]"
  - "[[sun-2024-asap-uav-swarm]]"
created: 2026-05-29
updated: 2026-05-29
---

# DL Inference Latency Prediction

Predicting how long a deep-learning model (or submodel) will take to run on a given device, so a scheduler can partition and balance work. Naive FLOPs-based estimates are inaccurate because real latency depends on operator types, memory access, and framework **operator fusion**.

In the wiki, [[sun-2024-asap-uav-swarm]] uses a lightweight two-part predictor: (1) operator-level prediction (config-pattern models for conv-like operators, FLOPs-linear for element-wise ones), and (2) a tiny learned **latency-fusion fine-tuner** that captures TensorRT fusion rules. It is millisecond-fast (vs nn-Meter's seconds-to-minutes) and far more accurate than a FLOPs baseline. The predictor is what feeds ASAP's load balancers (ICLB/ECLB) and [[elastic-task-scheduling]] for [[collaborative-dl-inference]].
