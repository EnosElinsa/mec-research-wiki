---
type: source
title: "Learning-Assisted Dynamic VNF Selection and Chaining for 6G Satellite-Ground Integrated Networks"
authors: ["Jianxin Zhang", "Qiang Ye", "Kaige Qu", "Yanglong Sun", "Yuliang Tang", "Dongmei Zhao", "Tong Ye"]
year: 2025
url: "https://doi.org/10.1109/TVT.2024.3454438"
venue: "IEEE Transactions on Vehicular Technology (IEEE TVT)"
tags: [source, satellite-ground-integrated-network, nfv, sdn, service-function-chaining, deep-q-network, vnf-migration, 6g]
related:
  - "[[space-air-ground-integrated-network]]"
  - "[[non-terrestrial-network]]"
  - "[[network-function-virtualization]]"
  - "[[service-function-chaining]]"
  - "[[deep-q-network]]"
  - "[[leo-satellite-edge-computing]]"
  - "[[task-migration]]"
  - "[[chen-2024-thoas-traffic-aware-sagin]]"
  - "[[niazmand-2025-jopa-dnn-pruning-iiot]]"
created: 2026-05-31
updated: 2026-05-31
---

# Learning-Assisted Dynamic VNF Selection and Chaining for 6G Satellite-Ground Integrated Networks

## Citation

Zhang, J., Ye, Q., Qu, K., Sun, Y., Tang, Y., Zhao, D., & Ye, T. (2025). *Learning-Assisted Dynamic VNF Selection and Chaining for 6G Satellite-Ground Integrated Networks*. **IEEE Transactions on Vehicular Technology**. DOI: 10.1109/TVT.2024.3454438. (Date of publication 30 Sep 2024; date of current version 16 Jan 2025.)

## TL;DR

A **deep Q-learning (DQL)** framework for **dynamic VNF selection and chaining (DVSC)** in a **6G satellite-ground integrated network (SGIN)**. Built on SDN/NFV, it determines a set of **VNF selection and chaining policies (VSCPs)** to balance **network resource provisioning + VNF migration costs** against **service performance gain**, maximizing **long-term network profit**. Formulated as a **Markov decision process (MDP)** capturing SGIN heterogeneity and time-varying topology; a new **sharing ratio (SR)** measures compute-resource sharing across VSCP sets.

## Problem framing

6G aims for global seamless coverage, but terrestrial networks reach only ~6% of the earth's surface, so SGINs integrate satellites (global coverage, limited compute/bandwidth) with ground networks (rich compute, limited coverage). Supporting end-to-end services means mapping **service function chains (SFCs)** — ordered sequences of VNFs — across heterogeneous nodes. Two challenges: (1) re-mapping SFCs when traffic/topology change causes frequent costly **VNF migrations**; (2) satellite movement makes the topology time-varying, and prior time-varying-graph snapshot methods are storage- and complexity-heavy.

## System model

- **Architecture.** An **SDN/NFV-based SGIN** with a satellite network segment and a ground network segment; an NFV orchestrator (with SDN controller) places VNFs and routes flows. Satellites covering the ground segment are identified via the **virtual node (VN)** approach.
- **Decision.** A **VSCP set** = joint VNF selection + virtual-link mapping for multiple flows; the **sharing ratio (SR)** elaborates the level of compute-resource sharing.
- **Objective.** Maximize long-term network profit = service performance gain minus resource provisioning + VNF migration costs, under service/capacity/delay/flow-conservation constraints.

## Method

- Formulate DVSC as an **[[deep-q-network|MDP]]**; build the action space by (1) **clustering historical network-load records** (k-means-style) into load levels, then (2) **greedily searching** the optimal VSCP set per cluster (breadth-first over VSCPs, descending SR, keeping the highest estimated profit).
- Train a **deep Q-network (DQN)** with an evaluation + target network, replay buffer, and ε-greedy exploration to pick the VSCP set per network state — the **DDVSC** algorithm. VSCP sets are delivered to satellites covering the ground segment to remain feasible under satellite movement.

## Key findings

- The proposed DQL-based VNF selection and chaining algorithm **outperforms baseline algorithms and approaches the performance upper bound**, and balances resource provisioning + VNF migration costs against service-performance gain under dynamic network load (the paper's stated result; specific curves in Section VI).

## Limitations / future work

Simulation-based. The parse's conclusion section was not reached in the read range, so explicit further-work items are `not in parse`.

## Relation to the corpus

A distinctive **NFV/SDN service-function-chaining** entry in the SGIN/satellite track — it optimizes **VNF placement + chaining + migration** rather than task offloading, complementing the slicing-based SAGIN scheme [[chen-2024-thoas-traffic-aware-sagin]] and connecting to [[leo-satellite-edge-computing]] and [[task-migration]]. Shares author Qiang Ye (University of Calgary) with three other batch-4 sources (the Qiang-Ye cross-cutting thread; see [[niazmand-2025-jopa-dnn-pruning-iiot]]). Anchors the new [[network-function-virtualization]] and [[service-function-chaining]] concepts.

## Raw artifacts

- `raw/sources/Learning-Assisted_Dynamic_VNF_Selection_and_Chaining_for_6G_Satellite-Ground_Integrated_Networks/full.md`
- Original PDF and extracted figures in the same folder.
