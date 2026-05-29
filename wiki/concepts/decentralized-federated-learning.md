---
type: concept
title: "Decentralized Federated Learning"
tags: [federated-learning, distributed-training, satellite]
related:
  - "[[zhai-2023-fedleo-decentralized-fl]]"
  - "[[federated-learning]]"
  - "[[leo-satellite-edge-computing]]"
  - "[[blockchain-for-fl-aggregation]]"
created: 2026-05-29
updated: 2026-05-29
---

# Decentralized Federated Learning

A variant of [[federated-learning]] that removes the central aggregation server: nodes exchange and aggregate model parameters directly (peer-to-peer or topology-driven), avoiding the central server's reliability and bandwidth bottlenecks. It is attractive when no single node is a natural, reliable aggregator.

In [[zhai-2023-fedleo-decentralized-fl]] (FedLEO), the LEO satellite constellation's topology drives server-free aggregation, combined with an offloading framework to mitigate the straggler effect and statistical (non-IID) heterogeneity. This contrasts with the blockchain-mediated aggregation of [[mao-2025-bcsa-frl]] and the SAGIN-handover FL of [[han-2024-sagin-fl-handover]].
