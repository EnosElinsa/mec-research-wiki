---
type: concept
title: "Discriminant Gain"
tags: [edge-ai, inference-accuracy, classification, metric, task-oriented-communication]
related:
  - "[[wen-2024-iscc-edge-ai]]"
  - "[[task-oriented-communication]]"
  - "[[integrated-sensing-computation-communication]]"
  - "[[sum-of-ratios-optimization]]"
created: 2026-06-02
updated: 2026-06-02
---

# Discriminant Gain

A tractable surrogate metric for **classification inference accuracy**, derived from the Kullback-Leibler (KL) divergence. Geometrically, the discriminant gain between two classes is the **distance between their centroids in the Euclidean feature space under normalized feature covariance** — i.e. how separable the two classes are. Larger discriminant gain means the classes are easier to tell apart, which corresponds to higher inference accuracy. For a whole feature vector with independent elements, the per-element discriminant gains sum, and the overall discriminant gain of a classifier is the average over all class pairs.

Discriminant gain matters because true inference accuracy is hard to optimize directly (it has no closed form in the system's physical-layer variables), whereas discriminant gain is an analytically tractable function of sensing noise, quantization distortion, and communication capacity. This makes it a useful **objective** for jointly designing the sensing/computation/communication pipeline of an edge-AI system.

## In this wiki

[[wen-2024-iscc-edge-ai]] adopts discriminant gain as the accuracy surrogate for its multi-device [[integrated-sensing-computation-communication|ISCC]] edge-inference system: it derives a closed-form expression linking sensing noise, quantization distortion, and communication capacity to the discriminant gain, then maximizes it via the [[sum-of-ratios-optimization|sum-of-ratios]] method. The paper validates that inference accuracy rises monotonically with discriminant gain for both SVM and MLP classifiers (with the caveat that accuracy saturates once class centroids are already far apart). It is a building block of the [[task-oriented-communication|task-oriented communication]] view, where the metric of interest is downstream task success rather than throughput.
