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
created: 2026-05-29
updated: 2026-05-29
---

# Collaborative DL Inference

Distributing a single deep-learning model's **inference** across multiple cooperating devices so they jointly produce one result, instead of running the whole model on one (resource-limited) node or shipping raw data to a remote server. It trades inter-device communication for parallel compute, and is attractive when no single node can hold/run the model and the network/ground link is weak.

In the wiki, [[sun-2024-asap-uav-swarm]] (ASAP) is the anchor: it processes sensory data entirely inside a UAV swarm via [[dnn-model-partition]] across clusters, [[data-partition-parallel-inference]] within clusters, and [[pipeline-parallel-inference]] across clusters. It is the inference-time relative of [[dispersed-computing]] (distributing general computation across aerial nodes), and is positioned against raw-data [[task-offloading]].
