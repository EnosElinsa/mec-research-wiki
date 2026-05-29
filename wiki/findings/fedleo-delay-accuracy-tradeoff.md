---
type: finding
title: FedLEO cuts decentralized-FL delay up to 41% and lifts accuracy up to 9.39%
source: "[[zhai-2023-fedleo-decentralized-fl]]"
confidence: medium
replicated: null
tags: [leo-satellite, federated-learning, offloading, benchmark]
related:
  - "[[decentralized-federated-learning]]"
  - "[[leo-satellite-edge-computing]]"
  - "[[adaptive-inter-layer-data-offloading]]"
  - "[[sagin-satellite-offloading-landscape]]"
created: 2026-05-30
updated: 2026-05-30
---

# FedLEO cuts decentralized-FL delay up to 41% and lifts accuracy up to 9.39%

In [[zhai-2023-fedleo-decentralized-fl]], the FedLEO server-free decentralized FL framework with offloading-aided straggler mitigation reports, explicitly in the abstract and contributions list:

> "reduce the system delay by up to 41% on average and improve the global model accuracy by up to 9.39% compared with benchmark policies."

## Grounding detail (per-dataset)

The 41% / 9.39% headline is an aggregate. The parse's scalability experiment (varying the accuracy-vs-delay weight κ) breaks it down:

- **MNIST:** delay-only optimization reduces delay up to 31.7% vs local computation; adding accuracy optimization improves accuracy up to 3.643% with very small delay increase.
- **CIFAR-10:** maximum delay optimization of 45.05% and accuracy optimization of 9.39%.

So the 9.39% accuracy figure is the CIFAR-10 best case; the 41% average-delay figure is the headline across the realistic-dataset experiments.

## Mechanism

- **Decentralized aggregation** exploits the LEO constellation's ring topology (Ring-Allreduce-style intra-orbit + inter-orbit synchronization) so no central satellite is needed.
- A **satellite-centric threshold-based offloading strategy** plus a **system-wide greedy iterative offloading decision algorithm** trade compute among satellites to mitigate the straggler effect and statistical heterogeneity, optimizing delay and accuracy under compute/communication power constraints.

## Caveats

- Single-paper result, simulation only (MNIST / CIFAR-10 on realistic constellation models) — `confidence: medium`.
- "Benchmark policies" are alternative FL/offloading baselines; the margin depends on the accuracy-vs-delay weight κ.

## Relation to the corpus

The plain-FL / decentralized-FL anchor in the [[sagin-satellite-offloading-landscape]] synthesis. Contrasts with the blockchain-secured federated thread ([[mao-2025-bcsa-frl]]) and the SAGIN-FL-with-handover thread ([[han-2024-sagin-fl-handover]]).
