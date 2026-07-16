---
type: source
title: "A Survey of Graph-Based Resource Management in Wireless Networks—Part II: Learning Approaches"
authors: ["Yanpeng Dai", "Ling Lyu", "Nan Cheng", "Min Sheng", "Junyu Liu", "Xiucheng Wang", "Shuguang Cui", "Lin Cai", "Xuemin Shen"]
year: 2024
url: "https://doi.org/10.1109/TCCN.2024.3508777"
venue: "IEEE Transactions on Cognitive Communications and Networking (IEEE TCCN)"
modeling_card: not_applicable
tags:
  - source
  - survey
  - graph-based-resource-management
  - graph-neural-network
  - resource-allocation
  - power-control
  - beamforming
  - task-offloading
related:
  - "[[graph-based-resource-management]]"
  - "[[graph-neural-network]]"
  - "[[dai-2024-graph-rm-survey-optimization]]"
  - "[[drl-backbones-across-uav-mec-sources]]"
  - "[[collaborative-beamforming]]"
  - "[[task-offloading]]"
  - "[[non-terrestrial-network]]"
  - "[[shuguang-cui]]"
  - "[[xuemin-shen]]"
created: 2026-06-03
updated: 2026-07-16
---

# A Survey of Graph-Based Resource Management in Wireless Networks—Part II: Learning Approaches

## Citation
Yanpeng Dai, Ling Lyu, Nan Cheng, Min Sheng, Junyu Liu, Xiucheng Wang, [[shuguang-cui|Shuguang Cui]], Lin Cai, [[xuemin-shen|Xuemin Shen]], "A Survey of Graph-Based Resource Management in Wireless Networks—Part II: Learning Approaches," *IEEE Transactions on Cognitive Communications and Networking*, 2024. DOI: 10.1109/TCCN.2024.3508777. (Corresponding author: Nan Cheng. Dalian Maritime University + Xidian University + CUHK-Shenzhen + Univ. of Victoria + Univ. of Waterloo.)

## TL;DR
Part II of the two-part graph-based-resource-management survey, shifting from graph optimization ([[dai-2024-graph-rm-survey-optimization|Part I]]) to **graph learning**. It introduces modern graph-neural-network (GNN) models and reviews their application to five resource-management issues — power control, spectrum management, beamforming design, task scheduling, and aerial coverage planning — then consolidates the technical challenges and future directions for the whole two-part survey.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Dai et al. [x] provided the learning part of a two-part survey on graph-based resource management in wireless networks. They introduced graph learning fundamentals and several modern graph neural network models, then organized the reviewed literature by power control, spectrum management, beamforming design, task scheduling, and aerial coverage planning. The survey discusses scalability, training efficiency, generalization, and compatibility with existing graph models as properties motivating graph learning for wireless resource management. It also consolidates technical challenges involving network scale and density, dynamicity, device heterogeneity, and incomplete network data, and identifies advanced graphs, scalable graph methods, graph generative models, and domain-knowledge-infused graph learning as future directions.

## Problem framing
Graph optimization (Part I) is mature but struggles with scale (graph size grows with network size) and combinatorial hardness, which conflicts with low-latency demands. Graph learning, especially GNNs and graph embedding, is presented as the complementary direction whose stated advantages are: (1) scalability with network size (GNN parameter count is independent of network size), (2) training efficiency on wireless-network data, (3) generalization to dynamic network status (permutation invariance/equivariance), and (4) compatibility with existing graph models. Part II reviews how these properties are exploited for resource management.

## System model
As a survey, the structure is a taxonomy:
- **Graph-learning fundamentals:** an overview of graph representation learning and several modern GNN model families (graph-in-graph-out architecture with message passing).
- **Five resource-management issue classes** used to organize the literature review (Section III): power control, spectrum management, beamforming design, task scheduling, and aerial coverage planning.
- **Cross-cutting challenges (consolidated for both parts):** network scale and density, dynamicity in wireless networks, heterogeneity of wireless devices, and incompleteness of network data.

## Method
The contribution is a categorized review of graph-learning-for-resource-management work, organized by the five issue classes above, plus the survey's forward-looking analysis:
- Documents the lineage of GNNs in wireless networks — e.g., Eisen and Ribeiro's first use of GNNs for link scheduling and multiple-access scheduling; Shen et al.'s demonstration that GNNs converge faster and generalize better than MLPs at large scale; hybrid designs that integrate GNNs with existing iterative algorithms (Chowdhury et al.; Yang et al.) and with reinforcement learning to handle dynamics and randomness.
- Names four future directions: advanced graphs for wireless networking, scalable resource management with graphs, generative models on graphs, and graph learning infused with resource-management domain knowledge.

## Key findings
Survey-level, grounded claims:
- GNNs' four claimed advantages for resource management are scalability, training efficiency, generalization, and compatibility with existing graph models.
- Combining GNNs with iterative algorithms is highlighted as a way to get the efficiency of learning and the accuracy of classical iteration simultaneously.
- Coupling GNNs with reinforcement-learning frameworks is identified as the route to handling dynamic, random wireless environments.
- The survey frames graph learning as still emerging, with substantial headroom in optimality and efficiency — hence the named future directions.

## Limitations / future work
- No new method is proposed or evaluated; it is a literature synthesis.
- The named open challenges (scale/density, dynamicity, device heterogeneity, data incompleteness) and four future directions are presented as open, not solved.

## Relation to the corpus
This is the learning half of the corpus's graph-based-resource-management survey, paired with [[dai-2024-graph-rm-survey-optimization]] (optimization half). It is the corpus's primary anchor for the [[graph-neural-network]] concept and complements [[graph-based-resource-management]]. Its issue-class taxonomy intersects the corpus's [[task-offloading]] and [[collaborative-beamforming|beamforming]] threads and its GNN-plus-[[drl-backbones-across-uav-mec-sources|DRL]] discussion connects to the corpus's heavy DRL-for-MEC literature. Shared authorship with the corpus via [[shuguang-cui]] and [[xuemin-shen]].

## Raw artifacts
- Parse: `raw/sources/A_Survey_of_Graph-Based_Resource_Management_in_Wireless_NetworksPart_II_Learning_Approaches/full.md`
- Origin PDF: `raw/sources/A_Survey_of_Graph-Based_Resource_Management_in_Wireless_NetworksPart_II_Learning_Approaches/e8665d88-3f6b-4b18-b801-2ef12d508743_origin.pdf`
- Figures: `raw/sources/A_Survey_of_Graph-Based_Resource_Management_in_Wireless_NetworksPart_II_Learning_Approaches/images/`
