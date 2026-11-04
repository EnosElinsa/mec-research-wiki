---
type: source
modeling_card: required
title: "QoS Aware Virtual Network Embedding in Space-Air-Ground-Ocean Integrated Network"
authors: ["Yi Zhang", "Peiying Zhang", "Chunxiao Jiang", "Shangguang Wang", "Hongxia Zhang", "Chunming Rong"]
year: 2024
url: "https://doi.org/10.1109/TSC.2024.3357707"
venue: "IEEE Transactions on Services Computing (IEEE TSC)"
tags: [source, space-air-ground-ocean-integrated-network, virtual-network-embedding, network-function-virtualization, network-slicing, dynamic-qos-constraints, non-terrestrial-network]
related:
  - "[[space-air-ground-ocean-integrated-network]]"
  - "[[virtual-network-embedding]]"
  - "[[network-function-virtualization]]"
  - "[[network-slicing]]"
  - "[[service-function-chaining]]"
  - "[[dynamic-qos-constraints]]"
  - "[[space-air-ground-integrated-network]]"
  - "[[non-terrestrial-network]]"
  - "[[zhang-2025-vnf-sgin-dql]]"
  - "[[du-2023-maddpg-service-placement-agin]]"
created: 2026-06-02
updated: 2026-11-03
---

# QoS Aware Virtual Network Embedding in Space-Air-Ground-Ocean Integrated Network

## Citation

Zhang, Y., Zhang, P., Jiang, C., Wang, S., Zhang, H., & Rong, C. (2024). *QoS Aware Virtual Network Embedding in Space-Air-Ground-Ocean Integrated Network*. **IEEE Transactions on Services Computing**. DOI: 10.1109/TSC.2024.3357707. (Manuscript received 29 June 2023; revised 30 October 2023; accepted 17 January 2024; date of publication 24 January 2024; date of current version 8 August 2024 → year 2024.)

## TL;DR

Abstracts the **space-air-ground-ocean integrated network (SAGOI-Net)** as a **three-layer heterogeneous physical substrate** (satellite / air / ground-ocean) under an SDN + network-virtualization architecture, and proposes a **QoS-aware multi-domain virtual network embedding (VNE)** algorithm. Virtual network requests (VNRs) are first **classified by K-means** into one of three QoS categories (compute / bandwidth / delay), and the **reward function is switched accordingly**; a **reinforcement-learning agent** (a four-layer policy network: input → convolution → softmax → output) then maps virtual nodes onto physical nodes, with link mapping via **k-shortest-path**. Simulations report gains in delay, acceptance rate, and revenue.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: An SDN controller embeds virtual network requests (VNRs) $G^V$ into a space-air-ground-ocean substrate network with time-varying topology. Virtual nodes demand CPU, virtual links demand bandwidth and delay, and infrastructure providers do not disclose all physical information.
**Problem & objective**: The paper states no single optimization problem. It evaluates long-term average revenue (8) and revenue-cost ratio $LRC=\lim_{T\to\infty}\sum_tR(G^V,t)/\sum_tCost(G^V,t)$ (9), plus embedding delay (10) and acceptance rate, and trains with reward $r_{r/c}=R/Cost$ (21) or $r_{delay}=\beta\sum BW/Delay(G^V,t)$ (22) chosen by QoS category.
**Decision variables**:
| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Node mapping | $n^v\uparrow n^s$ | discrete | Physical node hosting each virtual node, sampled from the softmax policy (20) |
| Link mapping | $(n_i^s,n_j^s)\uparrow(n_m^v,n_n^v)$ | discrete path | Substrate path for each virtual link, chosen by k-shortest paths |
**Constraints**:
| ID | Meaning and key expression |
|---|---|
| (2) | Node CPU: $CPU_{n^s}\geq CPU_{n^v}$ if $n^v\uparrow n^s$ |
| (3) | Link bandwidth: $BW_{(n_i^s,n_j^s)}\geq BW_{(n_m^v,n_n^v)}$ for mapped links |
| (4) | Link delay: $D_{(n_i^s,n_j^s)}\leq D_{(n_m^v,n_n^v)}$ for mapped links |
| (5) | One substrate node per virtual node: $Num_{\max}(n^v)=1$ |
**Algorithm**: K-means (11)-(12) classifies each VNR into three QoS categories; compute- and bandwidth-dominant requests use $r_{r/c}$ and delay-dominant requests use $r_{delay}$. A policy network with a convolutional layer takes the five-feature node matrix $M_f$ (13)-(17) as state and outputs node-embedding probabilities; links are embedded by k-shortest paths, the policy is updated by reward-scaled gradients (25), and VNR subgraphs that fail after topology changes are re-embedded.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zhang et al. [x] studied QoS-aware virtual network embedding in a space-air-ground-ocean integrated network. They modeled node CPU and delay, link bandwidth and delay, time-varying topology, and limited multi-domain information sharing. K-means classifies requests as compute-, bandwidth-, or delay-dominant, and the corresponding reward guides a convolutional policy that places virtual nodes. Virtual links use k-shortest paths, and failed request subgraphs are re-embedded after topology changes. Simulations report lower embedding delay and higher acceptance rate and long-term average revenue than SA-RL-VNE, RL-VNE, and a baseline embedding algorithm.

## Problem framing

SAGOI-Net promises comprehensive, low-delay coverage for global ITS/vehicle communications, but as a multi-tier heterogeneous architecture it cannot efficiently use network resources or guarantee differentiated QoS. The paper identifies three gaps in prior work: heuristic VNE algorithms fall into local optima; multi-domain VNE research is mostly terrestrial (little on heterogeneous, hierarchical multi-domain networks); and existing studies do not specifically model the physical resources of the three network segments. It therefore models SAGOI-Net hierarchically (over an SDN architecture) and proposes an RL-assisted, QoS-aware multi-domain VNE that **re-embeds failed VNR subgraphs** to stabilize QoS under topology change.

## System model

- **Substrate network.** Weighted undirected graph `G^S = {N^S, L^S, A^S}` with node sets for satellite (`N^S_S`), air (`N^S_A`), and ground-ocean (`N^S_{G&O}`) segments, intra- and inter-domain links, and attributes of CPU, link bandwidth, and link delay.
- **VNR.** Weighted undirected graph `G^V` with per-node CPU + computation-delay requirements and per-link bandwidth + delay requirements. Constraints: physical CPU ≥ virtual CPU, link bandwidth ≥ requirement, physical link delay ≤ virtual delay requirement, and one physical node per virtual node.
- **Time-varying topology.** Node working probability is modeled (Eq. 1) as a function of the number of VNRs carried; the topology at horizon `T` is sliced into consecutive `Δt` windows to handle satellite/platform movement and handover.
- **Privacy.** Each infrastructure provider (InP) uploads only limited topology/resource info to the SDN controller, reflecting the multi-domain privacy/overhead concern.
- **Metrics.** Revenue `R(G^v,t)`, cost (bandwidth weighted by hop count), long-term average revenue (LAR), long-term revenue-cost ratio (LRC), acceptance rate, and embedding delay.

## Method

- **K-means QoS classification.** VNRs are clustered into `k = 3` categories (compute / bandwidth / delay), and the cluster determines which reward function the RL agent uses — adapting embedding to the request's dominant QoS need.
- **Feature extraction.** Five per-node features: CPU, node degree, sum of adjacent link bandwidth, sum of adjacent link delay, and average distance to non-embedded virtual nodes — normalized into a feature matrix as the agent's state.
- **Policy network (RL agent).** Four layers — input (feature matrix), convolution (per-node available-resource vector), softmax (embedding probability per physical node), output. Node embedding samples from the probability distribution (not pure argmax) to escape biased initialization; **link embedding uses k-shortest-path**; the QoS-category-dependent reward signal drives training.
- **Robustness.** VNR subgraphs that fail to embed are re-embedded to maintain stable QoS under topology variation.

## Key findings

- Reported to perform well on **delay, acceptance rate, and revenue** versus comparison schemes (parse). Specific numeric margins are figure-derived; treat exact values as indicative.
- The K-means QoS-category-driven **dynamic reward switching** is the central design choice enabling adaptation to differentiated QoS demands in a heterogeneous multi-domain substrate.

## Limitations / future work

Evaluation is **simulation-only**. The model fixes `k = 3` QoS categories and extracts five node features (a stated complexity-vs-fidelity trade-off), and assumes limited InP information sharing. The paper states it "summarizes the article and prospects future work" but the specific future-work items are otherwise `not in parse`.

## Relation to the corpus

The corpus's **virtual-network-embedding / resource-orchestration** entry for non-terrestrial networks, extending [[space-air-ground-integrated-network|SAGIN]] with an **ocean** segment (see [[space-air-ground-ocean-integrated-network]]). It is the closest sibling to [[zhang-2025-vnf-sgin-dql]] — both build SDN/[[network-function-virtualization|NFV]] satellite-ground substrates and learn embedding/chaining policies with RL (DQL there, a convolutional policy-gradient agent here) — and shares the resource-orchestration framing with the MADDPG service-placement work [[du-2023-maddpg-service-placement-agin]]. It grounds [[virtual-network-embedding]] and connects to [[network-slicing]], [[service-function-chaining]], and [[dynamic-qos-constraints]] within the [[non-terrestrial-network]] context. Co-author [[chunxiao-jiang]] also anchors several satellite/maritime entries.

## Raw artifacts

- `raw/sources/QoS_Aware_Virtual_Network_Embedding_in_Space-Air-Ground-Ocean_Integrated_Network/QoS_Aware_Virtual_Network_Embedding_in_Space-Air-Ground-Ocean_Integrated_Network.md`
- Original PDF and extracted figures (`images/`) in the same folder.
