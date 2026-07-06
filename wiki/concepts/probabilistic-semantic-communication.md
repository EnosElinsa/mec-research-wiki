---
type: concept
title: "Probabilistic Semantic Communication"
tags: [semantic-communication, knowledge-graph, compression, sagin, energy-efficiency]
related:
  - "[[semantic-communication]]"
  - "[[task-oriented-communication]]"
  - "[[space-air-ground-integrated-network]]"
  - "[[zhao-2025-probabilistic-semantic-sagin]]"
  - "[[zheng-2024-semcom-sec-offloading]]"
  - "[[sun-2024-mfris-semantic-antijamming]]"
created: 2026-07-07
updated: 2026-07-07
---

# Probabilistic Semantic Communication

Probabilistic semantic communication (PSCom) compresses semantic triplets by using a shared probabilistic graph as a common knowledge base. If the receiver can infer an omitted relation from graph probabilities, the transmitter sends a smaller semantic representation and spends extra computation to perform the compression/recovery logic.

The important MEC tradeoff is communication energy versus semantic-computation energy. Lower semantic compression ratios reduce transmitted data but require higher-dimensional conditional probabilities and larger computation overhead. In [[zhao-2025-probabilistic-semantic-sagin]], that overhead is modeled as a piecewise function of compression ratio and optimized across satellite and UAV compute resources in a [[space-air-ground-integrated-network]].

This is a narrower concept than [[semantic-communication]] in general: it is specifically graph-probability-driven semantic compression, not any semantic encoder or task-oriented feature transmission.
