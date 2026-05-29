---
type: concept
title: "Pipeline-Parallel Inference"
tags: [distributed-inference, pipeline, latency]
related:
  - "[[collaborative-dl-inference]]"
  - "[[dnn-model-partition]]"
  - "[[parallel-vs-serial-processing]]"
  - "[[makespan-minimization]]"
  - "[[sun-2024-asap-uav-swarm]]"
created: 2026-05-29
updated: 2026-05-29
---

# Pipeline-Parallel Inference

Executing per-stage submodels as a **pipeline**: once a stage (here, a UAV cluster) finishes its submodel on one task, it immediately starts the next task while downstream stages process the previous one. With a steady stream of tasks, the average per-task latency becomes the **bottleneck-stage** latency rather than the sum over all stages — so balancing stage latencies is what matters.

In the wiki, [[sun-2024-asap-uav-swarm]] runs its cluster-level [[dnn-model-partition|submodels]] in this pipelined fashion, which is why its load-balancer (ECLB) targets equal per-cluster latency. It is the pipelined case of [[parallel-vs-serial-processing]] and motivates a [[makespan-minimization]]-style objective in [[collaborative-dl-inference]].
