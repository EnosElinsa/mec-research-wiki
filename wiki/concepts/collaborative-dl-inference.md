---
type: concept
title: "Collaborative DL Inference"
tags: [distributed-inference, edge-ai, uav-swarm]
related:
  - "[[dnn-model-partition]]"
  - "[[data-partition-parallel-inference]]"
  - "[[pipeline-parallel-inference]]"
  - "[[dispersed-computing]]"
  - "[[sun-2024-asap-uav-swarm]]"
  - "[[zhai-2026-collaborative-inference-uav-mec]]"
created: 2026-05-29
updated: 2026-07-06
---

# Collaborative DL Inference

Distributing a single deep-learning model's **inference** across multiple cooperating devices so they jointly produce one result, instead of running the whole model on one (resource-limited) node or shipping raw data to a remote server. It trades inter-device communication for parallel compute, and is attractive when no single node can hold/run the model and the network/ground link is weak.

In the wiki, [[sun-2024-asap-uav-swarm]] (ASAP) is the anchor for in-swarm collaborative inference: it processes sensory data entirely inside a UAV swarm via [[dnn-model-partition]] across clusters, [[data-partition-parallel-inference]] within clusters, and [[pipeline-parallel-inference]] across clusters. [[zhai-2026-collaborative-inference-uav-mec]] adds a GU-to-UAV split-inference variant: each DNN task is partitioned between the ground user and a serving UAV, then coupled with UAV trajectory and transmit-power control. Collaborative DL inference is the inference-time relative of [[dispersed-computing]] and is positioned against raw-data [[task-offloading]].
