---
type: concept
title: "Multi-Exit DNN"
tags: [distributed-inference, edge-ai, early-exit, dnn]
related:
  - "[[collaborative-dl-inference]]"
  - "[[dnn-model-partition]]"
  - "[[dl-inference-latency-prediction]]"
  - "[[wu-2026-secure-split-offloading-ci]]"
created: 2026-07-07
updated: 2026-07-07
---

# Multi-Exit DNN

A deep neural network with intermediate classifier exits, so inference can stop before the final layer when a shallower exit provides enough accuracy. In MEC, this creates an accuracy/latency/energy control variable: early exits reduce computation and transmission pressure, while deeper exits usually improve accuracy.

In [[wu-2026-secure-split-offloading-ci]], multi-exit inference is combined with [[dnn-model-partition]] and secure split offloading. Devices process initial layers, upload intermediate feature data, and the UAV server chooses both the partition point and the early-exit point under delay, secure-rate, and accuracy constraints.
