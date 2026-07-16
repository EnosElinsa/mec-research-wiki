---
type: source
title: "Cooperative Federated Learning Over Ground-to-Satellite Integrated Networks: Joint Local Computation and Data Offloading"
authors: ["Dong-Jun Han", "Seyyedali Hosseinalipour", "David J. Love", "Mung Chiang", "Christopher G. Brinton"]
year: 2024
url: "https://doi.org/10.1109/JSAC.2024.3365901"
venue: "IEEE Journal on Selected Areas in Communications (IEEE JSAC)"
modeling_card: required
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
updated: 2026-07-16
---

# Cooperative Federated Learning Over Ground-to-Satellite Integrated Networks: Joint Local Computation and Data Offloading

## Citation

Han, D.-J., Hosseinalipour, S., Love, D. J., Chiang, M., & Brinton, C. G. (2024). *Cooperative Federated Learning Over Ground-to-Satellite Integrated Networks: Joint Local Computation and Data Offloading*. **IEEE Journal on Selected Areas in Communications**. DOI: 10.1109/JSAC.2024.3365901.

## TL;DR

A **ground-to-satellite cooperative [[federated-learning|FL]]** methodology for remote regions that lack terrestrial infrastructure. LEO satellite constellations play three simultaneous roles during FL: (i) edge-computing units that process **data offloaded** from ground devices, (ii) intra-cluster model aggregators, and (iii) relays that pass models/data to neighboring satellites over inter-satellite links (ISLs). Because each satellite covers a region only briefly, the trained model and acquired data are handed to the next incoming satellite so FL continues. The paper proves convergence and builds a training-latency minimizer over per-satellite data-offloading amounts and computation speeds.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Geographically separated clusters of ground clients have no terrestrial infrastructure and are served by moving solar-powered LEO satellites. Clients retain privacy-sensitive samples, may offload non-sensitive samples, and communicate with satellites using allocated bandwidth, while inter-satellite links hand models and data to incoming satellites when coverage expires; no named multiple-access scheme is specified.

**Problem & objective**: Network problem (35) minimizes the maximum per-cluster FL-round latency, $\min_{\bar\alpha,\bar\gamma,\bar f_S,\bar b}\tau^{\mathrm{round}}$, jointly over data offloading, client processing, satellite CPU, and client bandwidth.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Client offloading portion | $\alpha_k$ | continuous, $0\leq\alpha_k\leq\alpha_k^{\max}$ | Fraction of client $k$'s dataset offloaded to its satellite |
| Client processing portion | $\gamma_k$ | continuous, $0\leq\gamma_k\leq1-\alpha_k$ | Fraction processed locally during a global round |
| Satellite CPU frequency | $f_{S,j}$ | continuous, $0\leq f_{S,j}\leq f_S^{\max}$ | Computation rate assigned at the satellite serving cluster $j$ |
| Client bandwidth | $b_k$ | continuous, $b_k\geq0$ | Ground-to-satellite bandwidth allocated to client $k$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| 35b-35c | Only non-sensitive data may be offloaded and local processing cannot exceed the retained portion |
| 35d-35e | Satellite CPU is bounded and $\sum_{k\in G_j}b_k\leq B_j$ |
| 35f-35h | Client energy and sun-facing or non-sun-facing satellite battery limits are satisfied |
| 35i-35j | The convergence-bound target holds and cluster offloading obeys $\sum_{k\in G_j}\alpha_k\lvert D_k\rvert\leq A_j^{\max}$ |

**Algorithm**: Set $\gamma_k=1-\alpha_k$ to process every retained sample and tighten the convergence bound; initialize the offloading, satellite-CPU, and bandwidth blocks; alternately optimize the blocks by block-coordinate descent; within the offloading block, use nested bisection to balance the slowest client-side completion time against repeated satellite-side computation; repeat until the block updates stabilize.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Han et al. [x] studied cooperative federated learning over ground-to-satellite networks serving remote client clusters without terrestrial infrastructure. They formulated FL-round latency minimization over client data-offloading fractions, local processing fractions, satellite CPU frequencies, and bandwidth allocations under privacy, energy, convergence, and communication-load constraints. Their method uses satellites as edge processors, cluster aggregators, and inter-satellite relays, and solves the nonconvex resource problem with block-coordinate updates and nested bisection. Experiments on MNIST, FMNIST, and CIFAR-10 reported faster time to target accuracy than fixed offloading and terrestrial-only baselines, with optimized mean offloading portions of 56.89, 55.23, and 67.23 percent.

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
