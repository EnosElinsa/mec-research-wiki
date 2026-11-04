---
type: source
modeling_card: required
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
updated: 2026-11-03
---

# Mobile Edge Deployment and Resource Management for Maritime Wireless Networks

## Citation

Zhang, C., Lin, B., Chen, Z., Cai, L. X., & Duan, J. (2024). *Mobile Edge Deployment and Resource Management for Maritime Wireless Networks*. **IEEE Transactions on Vehicular Technology**. DOI: 10.1109/TVT.2024.3521393.

## TL;DR

Mobile edge deployment + resource management for **MEC-assisted maritime wireless networks**, where **unmanned surface vehicles (USVs)** with diverse compute resources provide edge services complementing the cloud. The authors minimize expected response time by jointly optimizing USV deployment and computation-offloading decisions. The MINLP is solved with a **dual-layer reinforcement learning (DLRL)** framework: **DDPG** in the outer layer (USV deployment) and **Q-learning** in the inner layer (offloading decisions), handling continuous + discrete variables.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Clusters of heterogeneous unmanned surface vehicles (USVs) act as mobile edge nodes for vessels, with a remote cloud center providing complementary computation. USV cluster placement changes communication delay, while each vessel's offloading choice determines edge and cloud load.

**Problem & objective**: Problem ERTM (14) minimizes the expected response time, $\min_{\mathbf L^{\mathrm{usv}},\boldsymbol\alpha}T=\frac1M\sum_m(T_{m,n}+T_{m,0})$, over USV cluster deployment and vessel offloading decisions.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| USV cluster deployment | $\mathbf L_n=(x_n,y_n)$ | continuous position | Location of USV cluster $n$ |
| Offloading decision | $\alpha_{m,n}$ | binary | Vessel $m$ offloads to USV cluster $n$ or the cloud ($n=0$) |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| (14a)-(14b) | Each vessel offloads to exactly one USV cluster or the cloud |
| (14c) | Offloaded load at each cluster stays within its computing resource, $\sum_m\alpha_{m,n}\lambda_mc_m\leq C_n$ |
| (14d) | USV cluster positions stay within the service area, $0\leq x_n\leq x_{\max}$, $0\leq y_n\leq y_{\max}$ |

**Algorithm**: Outer-layer DDPG proposes continuous USV cluster deployments; for each deployment, inner-layer Q-learning chooses vessel offloading actions; the resulting response time is returned as the outer reward, and both layers update until deployment and offloading policies converge.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zhang et al. [x] studied mobile edge deployment and resource management for maritime wireless networks using heterogeneous unmanned surface vehicles. They formulated expected response-time minimization over continuous USV deployment and discrete computation-offloading decisions under single-destination offloading, computing-capacity, and service-area constraints. Their dual-layer reinforcement-learning framework uses DDPG in the outer layer to place USVs and Q-learning in the inner layer to select offloading actions. The inner response-time value guides the outer deployment policy. Simulations report lower expected response time than DDPG, DQN, PSO-DDQN, and PSO-greedy benchmarks, converging in about 400 episodes.

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

- `raw/sources/Mobile_Edge_Deployment_and_Resource_Management_for_Maritime_Wireless_Networks/Mobile_Edge_Deployment_and_Resource_Management_for_Maritime_Wireless_Networks.md`
- Original PDF and extracted figures in the same folder.
