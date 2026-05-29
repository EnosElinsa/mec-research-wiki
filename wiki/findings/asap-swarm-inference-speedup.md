---
type: finding
title: ASAP cuts in-swarm computing latency up to 92.66% vs raw-data offloading (hardware-validated)
source: "[[sun-2024-asap-uav-swarm]]"
confidence: medium
replicated: null
tags: [uav-swarm, distributed-inference, hardware-validated, benchmark]
related:
  - "[[collaborative-dl-inference]]"
  - "[[pipeline-parallel-inference]]"
  - "[[data-partition-parallel-inference]]"
  - "[[elastic-task-scheduling]]"
created: 2026-05-30
updated: 2026-05-30
---

# ASAP cuts in-swarm computing latency up to 92.66% vs raw-data offloading (hardware-validated)

In [[sun-2024-asap-uav-swarm]], the ASAP in-swarm collaborative DL-inference system is evaluated on real hardware, and the parse states the headline directly:

> "ASAP has been deployed on 24 popular airborne computers and 5 real-world quad-rotor UAVs. Experiment results show that the proposed system can decrease the computing latency by up to 92.66% compared with data offloading."

This is one of only two **hardware-validated** sources in the corpus (the other is [[shao-2024-drl-antijamming-mec]]), which makes the result unusually credible relative to the simulation-only majority.

## Mechanism

ASAP keeps inference inside the swarm rather than offloading raw sensory payloads to the ground:

- **Model + data partitioning** splits a DNN across heterogeneous airborne computers ([[dnn-model-partition]], [[data-partition-parallel-inference]]).
- **Pipeline-parallel** execution overlaps stages across UAVs ([[pipeline-parallel-inference]]).
- An **elastic efficient scheduler** (external + internal cluster load balancers + elastic scheduling module) aligns per-cluster inference latency, with an inference-latency predictor (ICLB) computing an aligned time so stragglers do not dominate ([[dl-inference-latency-prediction]], [[elastic-task-scheduling]]).

The 92.66% reduction is measured against the **raw-data-offloading** baseline (offload all sensory data to the resourceful ground), which suffers from the uplink bottleneck ASAP avoids.

## Caveats

- The 92.66% figure is the "up to" best case vs the offloading baseline, not a guaranteed average.
- Hardware-validated but in a controlled experimental setting (24 airborne computers, 5 quad-rotors); generalization to larger swarms or adverse RF conditions is not characterized in the parse.

## Relation to the corpus

The strongest distributed-inference data point in the wiki and the empirical anchor for the [[collaborative-dl-inference]] concept. Distinct workload class from the offloading-decision sources: ASAP optimizes *how to split one model across many UAVs*, not *whether to offload a task*.
