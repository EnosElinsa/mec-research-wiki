---
type: concept
title: "Task-Oriented Communication"
tags: [edge-ai, semantics, inference-accuracy, resource-allocation, integrated-sensing-and-communication]
related:
  - "[[wen-2024-iscc-edge-ai]]"
  - "[[discriminant-gain]]"
  - "[[integrated-sensing-computation-communication]]"
  - "[[semantic-communication]]"
  - "[[over-the-air-computation]]"
created: 2026-06-02
updated: 2026-06-02
---

# Task-Oriented Communication

A design principle where the system optimizes for the **success of a downstream task** (e.g. inference accuracy and latency) rather than for a generic communication metric such as throughput or bit error rate. In an edge-AI inference pipeline, the bits that matter are the ones that improve the final decision, so resources (power, bandwidth, time, quantization budget) should be allocated to maximize a task-relevant quality measure — not to maximize raw data rate.

This reframing changes the objective: when sensing, computation, and communication compete for the same radio resources, a task-oriented design jointly tunes them against an accuracy surrogate (see [[discriminant-gain]]) under latency and on-device-energy constraints. It is closely related to [[semantic-communication]] (transmit meaning, not symbols) and is a natural fit for [[integrated-sensing-computation-communication|ISCC]] systems where the "payload" is a feature vector feeding a model.

## In this wiki

[[wen-2024-iscc-edge-ai]] is the corpus's explicit task-oriented design: its split-inference edge-AI system treats inference accuracy (via [[discriminant-gain]]), not throughput, as the performance metric, and argues that the full benefit of split inference is only unlocked by a joint sensing-computation-communication design under this task-oriented principle. The view connects to [[over-the-air-computation]] (compute the function, not every signal) and to the broader [[semantic-communication]] thread.
