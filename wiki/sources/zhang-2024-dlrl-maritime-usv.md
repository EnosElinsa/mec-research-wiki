---
type: source
title: "Mobile Edge Deployment and Resource Management for Maritime Wireless Networks"
authors: ["Chaoyue Zhang", "Bin Lin", "Ziru Chen", "Lin X. Cai", "Jianli Duan"]
year: 2024
url: "https://doi.org/10.1109/TVT.2024.3521393"
venue: "IEEE Transactions on Vehicular Technology (IEEE TVT)"
tags: [source, maritime-mec, usv, mobile-edge-deployment, dual-layer-reinforcement-learning, ddpg, q-learning]
related:
  - "[[maritime-mec]]"
  - "[[ddpg]]"
  - "[[multi-agent-q-learning]]"
  - "[[weighted-kmeans-uav-deployment]]"
  - "[[mixed-integer-nonlinear-programming]]"
  - "[[zhang-2025-three-tier-maritime-offloading]]"
  - "[[liu-2025-haps-uav-maritime-iot]]"
created: 2026-05-29
updated: 2026-05-29
---

# Mobile Edge Deployment and Resource Management for Maritime Wireless Networks

## Citation

Zhang, C., Lin, B., Chen, Z., Cai, L. X., & Duan, J. (2024). *Mobile Edge Deployment and Resource Management for Maritime Wireless Networks*. **IEEE Transactions on Vehicular Technology**. DOI: 10.1109/TVT.2024.3521393.

## TL;DR

Mobile edge deployment + resource management for **MEC-assisted maritime wireless networks**, where **unmanned surface vehicles (USVs)** with diverse compute resources provide edge services complementing the cloud. The authors minimize expected response time by jointly optimizing USV deployment and computation-offloading decisions. The MINLP is solved with a **dual-layer reinforcement learning (DLRL)** framework: **DDPG** in the outer layer (USV deployment) and **Q-learning** in the inner layer (offloading decisions), handling continuous + discrete variables.

## Problem framing

Internet of Vessels (IoV) maritime applications need high bandwidth, low latency, and more compute. USVs are flexible, low-cost, maneuverable mobile edge nodes. The joint USV-deployment + offloading problem mixes continuous (deployment locations) and discrete (offloading) variables — an MINLP.

## System model

- **Actors.** USVs with diverse computation resources as mobile edge nodes; vessels/maritime users; cloud as complement.
- **Objective.** Minimize expected response time via joint USV deployment + offloading decisions ([[mixed-integer-nonlinear-programming]]).

## Method

- **DLRL** two-layer framework:
  - **Outer layer:** [[ddpg|DDPG]] for best USV deployment (continuous).
  - **Inner layer:** Q-learning for best offloading decisions (discrete) ([[multi-agent-q-learning]]).

## Key findings

- USV-cluster deployment provides an efficient, scalable solution for large-scale maritime networks; DLRL achieves significant expected-response-time reduction versus four literature benchmarks (DDPG, DQN, PSO-DDQN, etc.) — convergence-curve values are figure-derived and indicative.

## Limitations / future work

Future work: heterogeneous maritime MEC with different task types and QoS requirements.

## Relation to the corpus

A **DRL-based maritime MEC** entry that complements the optimization-based [[zhang-2025-three-tier-maritime-offloading]] and the HAP-UAV maritime IoT study [[liu-2025-haps-uav-maritime-iot]]; its USV (surface-vehicle) edge nodes differ from the AAV/vessel cooperation in [[you-2025-uncertain-maritime-hasac]] and the UAV+LEO double-edge of [[wang-2025-double-edge-samin]]. Its outer-DDPG/inner-Q-learning split is a distinctive dual-layer hybrid. Shares co-author Bin Lin with the other maritime sources. Reinforces [[maritime-mec]] and [[ddpg]].

## Raw artifacts

- `raw/sources/Mobile_Edge_Deployment_and_Resource_Management_for_Maritime_Wireless_Networks/full.md`
- Original PDF and extracted figures in the same folder.
