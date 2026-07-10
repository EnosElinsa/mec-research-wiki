---
type: source
title: "A Hierarchical MAFDRL-Based Resource Allocation and Incentive Mechanism for TN-NTN in 6G Networks"
authors: ["Abegaz Mohammed Seid", "Aiman Erbad", "Hayla Nahom Abishu", "Gordon Owusu Boateng", "Latif U. Khan", "Carla Fabiana Chiasserini", "Mohsen Guizani"]
year: 2026
url: "https://doi.org/10.1109/TMC.2025.3608291"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, non-terrestrial-network, space-air-ground-integrated-network, task-offloading, hierarchical-aerial-mec, hierarchical-federated-drl, double-auction, federated-reinforcement-learning, centralized-training-decentralized-execution, maddpg, ddpg]
related:
  - "[[non-terrestrial-network]]"
  - "[[space-air-ground-integrated-network]]"
  - "[[hierarchical-aerial-mec]]"
  - "[[task-offloading]]"
  - "[[hierarchical-federated-drl]]"
  - "[[federated-reinforcement-learning]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[double-auction]]"
  - "[[maddpg]]"
  - "[[ddpg]]"
  - "[[high-altitude-platform-station]]"
  - "[[leo-satellite-edge-computing]]"
  - "[[zhao-2026-hcdrl-ga-sagin-sar]]"
  - "[[han-2024-sagin-fl-handover]]"
created: 2026-07-10
updated: 2026-07-10
---

# A Hierarchical MAFDRL-Based Resource Allocation and Incentive Mechanism for TN-NTN in 6G Networks

## Citation

Seid, A. M., Erbad, A., Abishu, H. N., Boateng, G. O., Khan, L. U., Chiasserini, C. F., & Guizani, M. (2026). *A Hierarchical MAFDRL-Based Resource Allocation and Incentive Mechanism for TN-NTN in 6G Networks*. **IEEE Transactions on Mobile Computing (IEEE TMC)**. DOI: 10.1109/TMC.2025.3608291.

## TL;DR

Proposes a hierarchical federated multi-agent DRL framework for joint task offloading, resource allocation, and incentive pricing across terrestrial and non-terrestrial networks with EDs, UAVs, HAPs, and LEO satellites. A hierarchical double auction trades computation, bandwidth, transmission power, and FL service participation; DDPG handles auctioneer decisions and MADDPG handles lower-layer allocation decisions under CTDE.

## Problem

The paper targets the CORI problem: joint computation offloading and resource allocation with incentives. The objective is to maximize system utility and social welfare while reducing ED and aerial-server costs and preserving local data privacy. Binary association/trading decisions and continuous compute, bandwidth, and power allocations make the formulation an NP-hard MINLP.

## System model

- EDs generate computation tasks and may compute locally, offload to a GBS, offload to a UAV, offload directly to a HAP, or use a UAV-to-HAP path.
- UAVs and HAPs are aerial resource providers; LEO satellites extend coverage and HAP connectivity.
- The optimization model omits the LEO satellite to reduce complexity, even though the architecture includes it.
- Links include ED-to-UAV, ED-to-HAP, and UAV-to-HAP LoS communication.
- Hierarchical FL aggregates from EDs through UAVs and HAPs while avoiding raw-data upload.

## Method

The incentive layer is a hierarchical double auction. EDs request computation, communication, and power resources, while resource providers price and allocate them. The auctioneer selects clearing prices, winners, and buyer-seller matches; the mechanism is analyzed for truthfulness, individual rationality, and welfare retention under a double-sided market.

The learning layer transforms CORI into a stochastic game. A DDPG auctioneer chooses clearing-price and matching actions, while HAP, UAV/UCH, and ED agents use MADDPG under centralized training and decentralized execution. Hierarchical federated aggregation shares model parameters upward while keeping local data at the agents.

## Key findings

- FeDRL converges within approximately 300 episodes and improves convergence reward by 9.83%, 15.13%, and 44.07% over modified MADDPG, FRL, and DDPG.
- Social welfare reaches about 250 units after convergence and improves by 6.38%, 17.43%, and 28.73% over the same baselines.
- Seller/provider utility reaches about 1450 utility units after convergence, with gains of 9.722%, 18.93%, and 26.20%.
- Social welfare increases with more EDs and ABSs in the reported simulations, but the paper notes a complexity/equilibrium effect after roughly 350 episodes in one sensitivity study.
- Higher computation, communication, and transmission-power prices are reported to increase social welfare under the tested schemes, with FeDRL highest across the compared algorithms.

## Limitations / future work

LEO satellites are architectural participants but are omitted from the optimization formulation. The parse also leaves the secure multi-party computation claim at a high level, without a detailed protocol, threat model, overhead analysis, or privacy experiment. The authors list future work on multimodal language models, O-RAN, digital twins, HFL/MADRL, and group local differential privacy for emergency management.

## Relation to the corpus

This source extends the [[space-air-ground-integrated-network]] and [[non-terrestrial-network]] offloading line with explicit incentive pricing. It is close to [[han-2024-sagin-fl-handover]] on FL over SAGIN and to [[zhao-2026-hcdrl-ga-sagin-sar]] on hierarchical aerial control, but its distinctive contribution is the combination of [[hierarchical-federated-drl]] with a [[double-auction]] resource/FL-service market.

## Raw artifacts

- Parse: `raw/sources/A_Hierarchical_MAFDRL-Based_Resource_Allocation_and_Incentive_Mechanism_for_TN-NTN_in_6G_Networks/A_Hierarchical_MAFDRL-Based_Resource_Allocation_and_Incentive_Mechanism_for_TN-NTN_in_6G_Networks.md`
- Origin PDF: `raw/sources/A_Hierarchical_MAFDRL-Based_Resource_Allocation_and_Incentive_Mechanism_for_TN-NTN_in_6G_Networks/A_Hierarchical_MAFDRL-Based_Resource_Allocation_and_Incentive_Mechanism_for_TN-NTN_in_6G_Networks.pdf`
- Figures: `raw/sources/A_Hierarchical_MAFDRL-Based_Resource_Allocation_and_Incentive_Mechanism_for_TN-NTN_in_6G_Networks/images/`
