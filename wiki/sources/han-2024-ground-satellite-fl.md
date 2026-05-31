---
type: source
title: "Cooperative Federated Learning Over Ground-to-Satellite Integrated Networks: Joint Local Computation and Data Offloading"
authors: ["Dong-Jun Han", "Seyyedali Hosseinalipour", "David J. Love", "Mung Chiang", "Christopher G. Brinton"]
year: 2024
url: "https://doi.org/10.1109/JSAC.2024.3365901"
venue: "IEEE Journal on Selected Areas in Communications (IEEE JSAC)"
tags: [source, federated-learning, leo-satellite, ground-to-satellite, data-offloading, convergence-analysis, latency-minimization]
related:
  - "[[federated-learning]]"
  - "[[leo-satellite-edge-computing]]"
  - "[[privacy-sensitive-data-partitioning]]"
  - "[[leo-satellite-coverage-time]]"
  - "[[makespan-minimization]]"
  - "[[han-2024-sagin-fl-handover]]"
  - "[[zhai-2023-fedleo-decentralized-fl]]"
  - "[[mao-2025-bcsa-frl]]"
created: 2026-05-31
updated: 2026-05-31
---

# Cooperative Federated Learning Over Ground-to-Satellite Integrated Networks: Joint Local Computation and Data Offloading

## Citation

Han, D.-J., Hosseinalipour, S., Love, D. J., Chiang, M., & Brinton, C. G. (2024). *Cooperative Federated Learning Over Ground-to-Satellite Integrated Networks: Joint Local Computation and Data Offloading*. **IEEE Journal on Selected Areas in Communications**. DOI: 10.1109/JSAC.2024.3365901.

## TL;DR

A **ground-to-satellite cooperative [[federated-learning|FL]]** methodology for remote regions that lack terrestrial infrastructure. LEO satellite constellations play three simultaneous roles during FL: (i) edge-computing units that process **data offloaded** from ground devices, (ii) intra-cluster model aggregators, and (iii) relays that pass models/data to neighboring satellites over inter-satellite links (ISLs). Because each satellite covers a region only briefly, the trained model and acquired data are handed to the next incoming satellite so FL continues. The paper proves convergence and builds a training-latency minimizer over per-satellite data-offloading amounts and computation speeds.

## Problem framing

Many devices in rural/maritime/mountain regions are unconnected to terrestrial networks, so neither cloud nor edge servers are reachable for conventional FL aggregation, and the devices themselves are low-powered. The authors exploit the dense, wide-coverage LEO layer to aggregate models and offload computation. Key questions: what roles should satellites play, how much data should each ground device offload, how to handle satellite battery limits and the limited coverage time of LEO satellites, and how to guarantee convergence while minimizing training time. The paper positions itself among the first to address FL over ground-to-satellite integrated networks with theoretical guarantees and optimized design.

## System model

- **Topology.** J geographically separated clusters of K ground clients (example J = 3, K = 9); LEO satellites move along orbits, one covering a given region at a time, relaying via ISLs.
- **Data split.** Each client's dataset splits into privacy-sensitive samples (kept local) and non-sensitive samples (offloadable), with offloading portion α_k ∈ [0, α_k^max] — see [[privacy-sensitive-data-partitioning]].
- **Solar-powered satellites.** Clusters facing the sun let covering satellites recharge (looser energy constraints); other clusters face strict battery limits, so more data can be offloaded / processed when facing the sun.
- **Latency.** Per-round latency combines client-side compute, ground-to-satellite offloading, satellite-side compute, intra-cluster aggregation, and ISL model/data handover when a satellite's [[leo-satellite-coverage-time|coverage window]] expires.

## Method

- **Procedure.** A one-time preprocessing step offloads a non-sensitive data subset to the covering satellite; then each global round runs parallel local updates at clients and satellites, ISL handover of model+data to the incoming satellite, intra-cluster aggregation into cluster models, and a final global aggregation (FedAvg-style, weighted by data portions).
- **Convergence analysis.** Under standard non-convex assumptions, proves convergence of the time-averaged squared gradient norm to zero (a stationary point), establishing the algorithm is sound under the adaptive offloading.
- **Network optimization.** Minimizes training latency over the amount of data offloaded from each ground user to each satellite and the satellites' computation powers, subject to solar-powered battery constraints.

## Key findings

- Across three benchmark datasets (the abstract names three; the parse experiment section discusses MNIST/FMNIST/CIFAR-10), the methodology **significantly speeds up FL convergence** compared with terrestrial-only and other satellite baselines.
- Strategically using satellite resources — especially offloading more when the cluster faces the sun (recharging) — is the main lever for the speedup; the paper gives insights into how offloading should depend on sun-facing status.

## Limitations / future work

Simulation-only (benchmark-dataset experiments, no real-satellite testbed). Relies on a known offloadable non-sensitive fraction and estimable coverage windows, FedAvg aggregation, and standard FL convergence assumptions. The parse does not enumerate explicit future work. DOI date of publication 13 Feb 2024 / date of current version 9 May 2024 → year 2024.

## Relation to the corpus

A **satellite-FL** entry that frames satellites as edge-computing units + aggregators + relays, complementing [[zhai-2023-fedleo-decentralized-fl]] (server-free decentralized FL over LEO constellations) and [[mao-2025-bcsa-frl]] (blockchain-enabled cold-start FRL). It is by the same Purdue group ([[dong-jun-han]], [[christopher-brinton]]) as the SAGIN-FL paper [[han-2024-sagin-fl-handover]] and is **distinct** from it: this work targets a two-tier ground-to-satellite network with solar-battery-aware offloading and a convergence proof, whereas [[han-2024-sagin-fl-handover]] adds a UAV/air tier and an explicit seamless-handover offloading optimizer. Reinforces [[leo-satellite-edge-computing]], [[privacy-sensitive-data-partitioning]], and [[leo-satellite-coverage-time]].

## Raw artifacts

- `raw/sources/Cooperative_Federated_Learning_Over_Ground-to-Satellite_Integrated_Networks_Joint_Local_Computation_and_Data_Offloading/full.md`
- Original PDF and extracted figures in the same folder.
