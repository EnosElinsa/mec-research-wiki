---
type: source
title: "FedLEO: An Offloading-Assisted Decentralized Federated Learning Framework for Low Earth Orbit Satellite Networks"
authors: ["Zhiwei Zhai", "Qiong Wu", "Shuai Yu", "Rui Li", "Fei Zhang", "Xu Chen"]
year: 2023
url: "https://doi.org/10.1109/TMC.2023.3304988"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, leo-satellite-edge-computing, federated-learning, decentralized-fl, computation-offloading, straggler-effect]
related:
  - "[[leo-satellite-edge-computing]]"
  - "[[federated-learning]]"
  - "[[decentralized-federated-learning]]"
  - "[[task-offloading]]"
  - "[[walker-star-constellation]]"
  - "[[mao-2025-bcsa-frl]]"
  - "[[han-2024-sagin-fl-handover]]"
created: 2026-05-29
updated: 2026-05-29
---

# FedLEO: An Offloading-Assisted Decentralized Federated Learning Framework for Low Earth Orbit Satellite Networks

## Citation

Zhai, Z., Wu, Q., Yu, S., Li, R., Zhang, F., & Chen, X. (2023). *FedLEO: An Offloading-Assisted Decentralized Federated Learning Framework for Low Earth Orbit Satellite Networks*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2023.3304988.

## TL;DR

A **decentralized federated learning** framework for LEO satellite constellations that trains ML models on satellite-generated Earth imagery without shipping raw data to ground. Because a single central aggregation satellite is impractical, FedLEO exploits the constellation's topology to aggregate model parameters **without a central server**. To fight the straggler effect and statistical heterogeneity, it adds an **offloading** framework with a satellite-centric threshold-based offloading strategy and a system-wide greedy iterative offloading-decision algorithm. Reported gains: up to **41% lower system delay** on average and up to **9.39% higher global-model accuracy** versus benchmarks.

## Problem framing

LEO satellites do complex Earth-observation ML but face restricted downlink bandwidth and spotty connectivity, so transmitting all imagery to ground for centralized training is infeasible. FL exchanges only parameters, but classic FL's central aggregator is hard to realize in a distributed constellation; satellites also differ in compute/comm capability (stragglers) and data distribution (statistical heterogeneity).

## System model

- **Network.** LEO satellite constellation with characteristic topology; satellites collaborate for resource sharing ([[walker-star-constellation]]-style coverage).
- **Heterogeneity.** Unbalanced compute/comm capabilities (straggler effect) and non-IID data across satellites.

## Method

- **Decentralized aggregation** leveraging the constellation topology — no central server, avoiding its reliability/bandwidth bottlenecks.
- **Offloading for collaboration:** a satellite-centric **threshold-based offloading strategy** (also reducing weight divergence vs. centralized ML) plus a **system-wide greedy iterative algorithm** that jointly optimizes delay and training accuracy under compute/comm power constraints; theoretical analysis included.

## Key findings

- On realistic datasets, FedLEO reduces system delay by **up to 41% on average** and improves global-model accuracy by **up to 9.39%** versus benchmark policies (the paper's stated headline numbers), and adapts to tasks with diverse accuracy/delay requirements.

## Limitations / future work

Experiments use realistic datasets in simulation. The parse's conclusion does not enumerate explicit limitations beyond the modeled constraints.

## Relation to the corpus

Strengthens the **LEO-satellite + federation** thread alongside [[mao-2025-bcsa-frl]] (blockchain-aggregated FRL in zero-trust LEO) and [[han-2024-sagin-fl-handover]] (FL over SAGIN with handover) — FedLEO's distinguishing move is *server-free* decentralized aggregation plus offloading to handle stragglers. Reinforces [[leo-satellite-edge-computing]], [[federated-learning]], and introduces [[decentralized-federated-learning]].

## Raw artifacts

- `raw/sources/FedLEO_An_Offloading-Assisted_Decentralized_Federated_Learning_Framework_for_Low_Earth_Orbit_Satellite_Networks/full.md`
- Original PDF and extracted figures in the same folder.
