---
type: source
title: "Graph Attention Network-Driven Hierarchical Learning for Anti-Jamming UAV Communications"
authors: ["Xiao Tang", "Kexin Zhao", "Chao Shen", "Chenhao Lin", "Shuai Liu", "Bohui Wang", "Dusit Niyato", "Zhu Han"]
year: 2026
url: "https://doi.org/10.1109/TWC.2025.3618614"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, anti-jamming, graph-attention-network, beamforming, uav-deployment, zero-sum-game, maddpg]
related:
  - "[[hierarchical-graph-anti-jamming-control]]"
  - "[[multi-domain-uav-anti-jamming]]"
  - "[[graph-neural-network]]"
  - "[[maddpg]]"
  - "[[uav-trajectory-control]]"
  - "[[nash-equilibrium]]"
  - "[[dusit-niyato]]"
  - "[[zhu-han]]"
created: 2026-07-13
updated: 2026-07-13
---

# Graph Attention Network-Driven Hierarchical Learning for Anti-Jamming UAV Communications

## Citation

Tang, X., Zhao, K., Shen, C., Lin, C., Liu, S., Wang, B., Niyato, D., & Han, Z. (2026). *Graph Attention Network-Driven Hierarchical Learning for Anti-Jamming UAV Communications*. **IEEE Transactions on Wireless Communications**, 25, 5432-5445. DOI: 10.1109/TWC.2025.3618614.

## TL;DR

Separates anti-jamming control into a graph-attention beamforming layer and an adversarial deployment/power layer. A pretrained GAT supplies beamformers inside a two-agent MADDPG loop that moves legitimate UAVs while jammers change transmit power.

## Problem framing

Multi-UAV downlinks face both mutual interference and malicious jamming. Beamforming reacts at the channel scale, while UAV placement changes large-scale geometry and jammers adapt their powers. A monolithic alternating or learned solution couples these scales and opposing objectives.

## System model

- `K` multi-antenna UAV-user pairs and `J` single-antenna jammers share spectrum in a bounded area; UAV altitude is fixed and only horizontal deployment changes.
- Each user is associated with one UAV and receives concurrent interference from other UAVs and all jammers.
- Legitimate decisions are beamformers and UAV positions; jammer decisions obey individual and aggregate power limits.
- The two sides form a claimed zero-sum game over sum spectral rate and its negative.
- The implemented method assumes perfect global CSI and does not model flight energy, collision avoidance, or task computation.

## Method

[[hierarchical-graph-anti-jamming-control]] first encodes each UAV-user pair as a graph node, all jammers as one aggregate node, and interference/jamming channels as directed edge features. A rate-driven, label-free GAT outputs power-normalized complex beamformers.

The outer Markov game groups all legitimate UAVs into one agent and all jammers into another. MADDPG actors produce UAV displacement and jammer-power increments; centralized critics learn from global channels, positions, and powers. Each transition calls the frozen GAT to calculate the sum-rate reward.

## Key findings

- The paper reports that GAT beamforming outperforms GCN, SCA, and MLP across user-count, jammer-count, and transmit-power sweeps, but the prose gives no exact margins.
- Learned UAVs move toward intended users, remain separated, and move away from jammers; MADDPG trajectories are smoother than discrete DDQN trajectories.
- Changed graph sizes use unspecified fine-tuning, so the experiments do not establish zero-shot transfer despite the permutation-equivariance claim.
- The paper explicitly describes the learned outcome as equilibrium-like and locally approximate rather than a proved saddle point or global optimum.

## Limitations / parse caveats

Validation is synthetic simulation with one user per UAV, perfect CSI, fixed altitude, no code/hardware/run statistics, and no flight-energy or safety constraints. The paper provides no rigorous learning-convergence proof or exploitability test. Loss sign, reward scale, log base, power constraints, aggregate-power notation, CTDE observability, feature dimensions, and the reported soft-update coefficient are ambiguous or inconsistent.

## Relation to the corpus

This source adds a beamforming/deployment hierarchy to [[multi-domain-uav-anti-jamming]]. Instead of selecting channels and powers per UAV, it uses graph message passing for physical-layer beamforming and adversarial MARL for spatial adaptation. The parse does not specify different update periods for the two layers. It is a communication-security paper, not an MEC offloading model.

## Raw artifacts

- Parse: `raw/sources/Graph_Attention_Network-Driven_Hierarchical_Learning_for_Anti-Jamming_UAV_Communications/Graph_Attention_Network-Driven_Hierarchical_Learning_for_Anti-Jamming_UAV_Communications.md`
- Origin PDF: `raw/sources/Graph_Attention_Network-Driven_Hierarchical_Learning_for_Anti-Jamming_UAV_Communications/Graph_Attention_Network-Driven_Hierarchical_Learning_for_Anti-Jamming_UAV_Communications.pdf`
- Figures: `raw/sources/Graph_Attention_Network-Driven_Hierarchical_Learning_for_Anti-Jamming_UAV_Communications/images/`
