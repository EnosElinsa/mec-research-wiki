---
type: source
modeling_card: required
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
updated: 2026-11-03
---

# FedLEO: An Offloading-Assisted Decentralized Federated Learning Framework for Low Earth Orbit Satellite Networks

## Citation

Zhai, Z., Wu, Q., Yu, S., Li, R., Zhang, F., & Chen, X. (2023). *FedLEO: An Offloading-Assisted Decentralized Federated Learning Framework for Low Earth Orbit Satellite Networks*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2023.3304988.

## TL;DR

A **decentralized federated learning** framework for LEO satellite constellations that trains ML models on satellite-generated Earth imagery without shipping raw data to ground. Because a single central aggregation satellite is impractical, FedLEO exploits the constellation's topology to aggregate model parameters **without a central server**. To fight the straggler effect and statistical heterogeneity, it adds an **offloading** framework with a satellite-centric threshold-based offloading strategy and a system-wide greedy iterative offloading-decision algorithm. Reported gains: up to **41% lower system delay** on average and up to **9.39% higher global-model accuracy** versus benchmarks.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Heterogeneous LEO satellites train a shared model on non-IID Earth-observation data and aggregate parameters along constellation links without a central server. A slow satellite $v_a$ can offload $I_{ab}$ samples to an adjacent satellite $v_b$ over multi-hop flows to reduce the straggler delay.
**Problem & objective**: P1 (15) trades system delay against weight divergence, $\min_{I_{ab},p_a^o,p_a^u,\mathbf w_{m\tau}^{(a)},\mathbf w_{m\tau}^{(f)}}\max_p\sum_{a'\in\mathcal L(p)}t_{a'}^o+M\max_{a\in\mathcal N}t_a^u+Mt_\omega+\kappa\lVert\mathbf w_{m\tau}^{(f)}-\mathbf w_{m\tau}^{(c)}\rVert$, where $\kappa$ weights accuracy against delay.
**Decision variables**:
| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Offloaded data size | $I_{ab}$ | continuous, $[0,D_a]$ | Samples moved from satellite $v_a$ to neighbor $v_b\in\mathcal B(a)$ |
| Communication power | $p_a^o$ | continuous, $[0,p_a^{omax}]$ | Transmit power for data offloading |
| Computation power | $p_a^u$ | continuous, $[0,p_a^{umax}]$ | Power for local model training |
| Model parameters | $\mathbf w_{m\tau}^{(a)},\mathbf w_{m\tau}^{(f)}$ | continuous | Local and FedLEO-aggregated models compared with centralized $\mathbf w_{m\tau}^{(c)}$ |
**Constraints**:
| ID | Meaning and key expression |
|---|---|
| C1 | Communication power $0\leq p_a^o\leq p_a^{omax}$ |
| C2 | Computation power $0\leq p_a^u\leq p_a^{umax}$ |
| C3 | Offloaded data $0\leq I_{ab}\leq D_a$ |
| C4 | Delay after offloading does not exceed the no-offloading delay: $T^o+T^u\leq\max_a\{M\tau CD_a\sqrt{\zeta_a/p_a^u}\}+Mt_\omega$ |
| C5 | Divergence does not grow: $\lVert\mathbf w_{m\tau}^{(f)}-\mathbf w_{m\tau}^{(c)}\rVert\leq\lVert\mathbf w_{m\tau}^{(l)}-\mathbf w_{m\tau}^{(c)}\rVert$ |
**Algorithm**: P1 is transformed into round-by-round local problems P2 (20) for the slowest satellite $v_a$, with D1-D6 mirroring C1-C5. Power subproblems (26)-(27) and the data-size problem (28)-(P5) give a satellite-centric threshold rule with thresholds $\Gamma_l,\Gamma_h$ (Algorithm 2). Algorithm 3 greedily selects the receiving neighbor by a weighted delay and data-distribution score, updates virtual datasets by (21)-(22), and repeats until no offloading decision improves; its approximation ratio is $2\Upsilon$.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zhai et al. [x] studied offloading-assisted decentralized federated learning in low-Earth-orbit satellite networks. FedLEO exploits constellation topology to aggregate model parameters without a central server and uses task offloading to reduce straggler delay under heterogeneous computation, communication, and data distributions. A satellite-centric threshold strategy identifies useful transfers, while a system-wide greedy iterative algorithm selects offloading decisions that trade training delay against model accuracy. The formulation bounds communication power, computation power, and offloaded data size, and requires that offloading neither increases delay nor enlarges weight divergence. Experiments report up to 41% lower average system delay and up to 9.39% higher global-model accuracy than benchmark policies, including FedAvg, FedProx, and FedNova.

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

- `raw/sources/FedLEO_An_Offloading-Assisted_Decentralized_Federated_Learning_Framework_for_Low_Earth_Orbit_Satellite_Networks/FedLEO_An_Offloading-Assisted_Decentralized_Federated_Learning_Framework_for_Low_Earth_Orbit_Satellite_Networks.md`
- Original PDF and extracted figures in the same folder.
