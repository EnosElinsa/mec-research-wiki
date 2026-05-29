---
type: concept
title: "ProbSparse Self-Attention Prediction (Informer-style)"
tags: [time-series, transformer, prediction, efficiency]
related:
  - "[[informer-trajectory-prediction]]"
  - "[[traffic-aware-offloading]]"
  - "[[chen-2024-thoas-traffic-aware-sagin]]"
created: 2026-05-29
updated: 2026-05-29
---

# ProbSparse Self-Attention Prediction (Informer-style)

An efficient long-sequence time-series forecaster based on the Informer architecture's **ProbSparse self-attention**, which attends only to the dominant query-key pairs to cut self-attention cost from $O(L^2)$ to $O(L \log L)$ per query, plus inter-layer **self-attention distillation** (Conv1d + ELU + MaxPool between encoder layers) to shrink the sequence. A decoder + MLP head emits the forecast.

In the wiki, [[chen-2024-thoas-traffic-aware-sagin]] uses it to predict future cellular traffic for adaptive slice sizing in SAGIN. It is the traffic-forecasting cousin of [[informer-trajectory-prediction]] (used for vehicle trajectory in [[zhang-2025-mcma-task-migration]]) — same Informer lineage, different prediction target — and the prediction engine behind [[traffic-aware-offloading]].
