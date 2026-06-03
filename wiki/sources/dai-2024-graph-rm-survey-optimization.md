---
type: source
title: "A Survey of Graph-Based Resource Management in Wireless Networks—Part I: Optimization Approaches"
authors: ["Yanpeng Dai", "Ling Lyu", "Nan Cheng", "Min Sheng", "Junyu Liu", "Xiucheng Wang", "Shuguang Cui", "Lin Cai", "Xuemin Shen"]
year: 2024
url: "https://doi.org/10.1109/TCCN.2024.3508783"
venue: "IEEE Transactions on Cognitive Communications and Networking (IEEE TCCN)"
tags:
  - source
  - survey
  - graph-based-resource-management
  - graph-neural-network
  - resource-allocation
  - combinatorial-optimization
  - non-terrestrial-network
  - mobile-edge-computing
related:
  - "[[graph-based-resource-management]]"
  - "[[graph-neural-network]]"
  - "[[dai-2024-graph-rm-survey-learning]]"
  - "[[matching-theory-for-resource-allocation]]"
  - "[[gale-shapley-matching]]"
  - "[[non-terrestrial-network]]"
  - "[[mobile-edge-computing]]"
  - "[[computational-task-caching]]"
  - "[[shuguang-cui]]"
  - "[[xuemin-shen]]"
created: 2026-06-03
updated: 2026-06-03
---

# A Survey of Graph-Based Resource Management in Wireless Networks—Part I: Optimization Approaches

## Citation
Yanpeng Dai, Ling Lyu, Nan Cheng, Min Sheng, Junyu Liu, Xiucheng Wang, [[shuguang-cui|Shuguang Cui]], Lin Cai, [[xuemin-shen|Xuemin Shen]], "A Survey of Graph-Based Resource Management in Wireless Networks—Part I: Optimization Approaches," *IEEE Transactions on Cognitive Communications and Networking*, 2024. DOI: 10.1109/TCCN.2024.3508783. (Corresponding author: Nan Cheng. Dalian Maritime University + Xidian University + CUHK-Shenzhen + Univ. of Victoria + Univ. of Waterloo.)

## TL;DR
Part I of a two-part survey on using graphs for resource management in wireless networks. It lays out the fundamentals of graph theory and the classic **graph-optimization** problem family (graph coloring, maximum independent set, maximum flow, shortest path, bipartite/stable matching), then reviews how these combinatorial tools are applied to resource management across six scenario classes: cellular networks, device-to-device (D2D) communications, multi-hop networks, multi-antenna systems, edge caching and computing, and non-terrestrial networks (NTNs). The companion [[dai-2024-graph-rm-survey-learning|Part II]] covers the graph-learning (GNN) side and the joint challenges/future directions.

## Problem framing
The dimensionality of wireless-network resources (spatial, time, frequency, code, power domains, plus hybrid communication/computation and terrestrial/aerial resources) keeps expanding, which makes resource management harder. Graph theory has long modeled wireless networks — nodes/infrastructures as vertices, relationships such as connection and interference as edges — turning resource-management tasks into optimization problems over graphs. The survey argues that prior surveys treat either graph optimization *or* graph learning in isolation, and often cover an incomplete set of network types (missing emerging cellular/cell-free networks, edge caching/computing, etc.). Part I addresses the graph-optimization half comprehensively.

## System model
This is a survey, so the "model" is a taxonomy rather than a single system:
- **Graph fundamentals:** a graph G = (V, E); vertex degree and edge/vertex weights; directed vs undirected vs bipartite graphs; hypergraphs (a hyperedge joins any number of vertices); matrix representations (incidence, adjacency, weight matrices).
- **Graph-optimization problem catalog (with named algorithms):** graph coloring (K-coloring judgment, chromatic-number problems), maximum independent set, maximum flow (and its multi-source/sink and double-capacity variants, some still open), and bipartite matching (maximal/maximum matching via Hopcroft–Karp, maximum-weight matching, stable matching).
- **Stated advantages of graph optimization:** adaptability (topology maps directly to graph models) and a mature theoretical-algorithm foundation balancing optimality and efficiency.
- **Stated limitations:** graph size grows with network scale (storage/processing burden), and most graph-optimization problems are combinatorial and not polynomial-time solvable, so the algorithmic overhead can violate low-latency requirements.

## Method
The contribution is a categorized literature review. Part I organizes graph-optimization-for-resource-management work by scenario:
1. **Cellular networks** — interference modeling, graph coloring for beam/channel/frequency assignment, the interference graph as a foundational model.
2. **D2D communications** — link scheduling and resource sharing.
3. **Multi-hop networks** — link scheduling, flow.
4. **Multi-antenna systems** — beamforming/grouping.
5. **Edge caching and computing** — content placement and task assignment over graphs.
6. **Non-terrestrial networks (NTNs)** — satellite/aerial resource allocation.

It traces the historical arc from early graph-coloring beam-switching (Chawla and Qiu, 1999) and the interference graph (Jain et al.; Kodialam and Nandagopal) through hypergraph models after 2010, and positions graph optimization as the foundation that graph learning (Part II) builds on.

## Key findings
This is a survey; its "findings" are organizational claims, grounded in the parse:
- Graph optimization's two stated strengths are adaptability and a strong theoretical algorithm base; its two stated weaknesses are poor scaling of graph size with network scale and the combinatorial (non-polynomial) hardness of most problems, which hurts timeliness for low-latency applications.
- The survey's Table I positions it against prior surveys ([25]–[33]) as the one work covering **both** graph optimization and graph learning across a broad set of wireless networks specifically for resource management.
- The two-part structure is deliberate: Part I (optimization) is presented as laying the foundation for the graph-learning methods in Part II.

## Limitations / future work
- As a survey it does not propose or evaluate a new method; it inherits the literature's own evaluation gaps.
- Technical challenges and future directions are deferred to and consolidated in [[dai-2024-graph-rm-survey-learning|Part II]] (network scale/density, dynamicity, device heterogeneity, data incompleteness; future directions around advanced graphs, scalable graph RM, generative models on graphs, and domain-knowledge-infused graph learning).

## Relation to the corpus
This is one of two halves of the corpus's dedicated graph-based-resource-management survey; its companion is [[dai-2024-graph-rm-survey-learning]] (learning approaches). It provides the optimization-theory anchor for the corpus's recurring combinatorial methods — [[matching-theory-for-resource-allocation]] and [[gale-shapley-matching]] (bipartite/stable matching) and the broader [[graph-based-resource-management]] concept. Its edge-caching/computing and NTN scenario chapters connect to the corpus's [[mobile-edge-computing]], [[computational-task-caching]], and [[non-terrestrial-network]] threads. Authors [[shuguang-cui]] and [[xuemin-shen]] also appear elsewhere in the corpus.

## Raw artifacts
- Parse: `raw/sources/A_Survey_of_Graph-Based_Resource_Management_in_Wireless_NetworksPart_I_Optimization_Approaches/full.md`
- Origin PDF: `raw/sources/A_Survey_of_Graph-Based_Resource_Management_in_Wireless_NetworksPart_I_Optimization_Approaches/08cb4879-c577-432f-8a9d-4c2bc815bbd8_origin.pdf`
- Figures: `raw/sources/A_Survey_of_Graph-Based_Resource_Management_in_Wireless_NetworksPart_I_Optimization_Approaches/images/`
