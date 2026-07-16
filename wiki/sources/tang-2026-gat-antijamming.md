---
type: source
title: "Graph Attention Network-Driven Hierarchical Learning for Anti-Jamming UAV Communications"
authors: ["Xiao Tang", "Kexin Zhao", "Chao Shen", "Chenhao Lin", "Shuai Liu", "Bohui Wang", "Dusit Niyato", "Zhu Han"]
year: 2026
url: "https://doi.org/10.1109/TWC.2025.3618614"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
modeling_card: required
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
updated: 2026-07-16
---

# Graph Attention Network-Driven Hierarchical Learning for Anti-Jamming UAV Communications

## Citation

Tang, X., Zhao, K., Shen, C., Lin, C., Liu, S., Wang, B., Niyato, D., & Han, Z. (2026). *Graph Attention Network-Driven Hierarchical Learning for Anti-Jamming UAV Communications*. **IEEE Transactions on Wireless Communications**, 25, 5432-5445. DOI: 10.1109/TWC.2025.3618614.

## TL;DR

Separates anti-jamming control into a graph-attention beamforming layer and an adversarial deployment/power layer. A pretrained GAT supplies beamformers inside a two-agent MADDPG loop that moves legitimate UAVs while jammers change transmit power.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Multiple multi-antenna UAV base stations serve associated ground users over shared spectrum while multiple single-antenna jammers transmit adversarial interference. UAVs move horizontally at a fixed altitude, and the achievable sum rate depends jointly on beamforming, deployment, mutual interference, and jammer powers.

**Problem & objective**: Problems (5)-(7) form a zero-sum game in which the legitimate side maximizes sum rate $R$ over UAV beamformers and positions while the jammer side minimizes the same rate over its power vector.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV beamformer | $\mathbf f_k$ | complex vector, bounded norm | Downlink beamforming vector for UAV $k$ |
| UAV horizontal position | $\mathbf w_k$ | continuous, $\mathbf w_k\in\mathcal Q$ | Deployment of UAV $k$ in the service area |
| Jammer power | $p_j$ | continuous, $0\leq p_j\leq P_j$ | Transmit power selected by jammer $j$ |
| Deployment update | $\Delta\mathbf w_k$ | continuous bounded displacement | Outer-layer movement action for UAV $k$ |
| Power update | $\Delta p_j$ | continuous bounded increment | Outer-layer action used to update jammer power |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| 5b | UAV transmit-power limit, $\lVert\mathbf f_k\rVert^2\leq P_k$ |
| 5c | UAV deployment remains inside $\mathcal Q$ |
| 6b | Each jammer obeys $0\leq p_j\leq P_j$ |
| 6c / 9 | Aggregate jamming power satisfies $\sum_j p_j\leq P_{\max}$ |
| 26-28 | Movement and power increments are bounded and clipped or normalized back into their feasible sets |

**Algorithm**: An unsupervised GAT is pretrained to map current channels and jamming powers to rate-maximizing beamformers. The outer zero-sum game is then represented by two MADDPG agents, one updating all UAV positions and the other updating all jammer powers, with the frozen GAT called inside each transition to compute the rate reward.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Tang et al. [x] formulated multi-UAV anti-jamming communication as a zero-sum game over legitimate beamforming and deployment and adversarial jamming power. Their hierarchical solution trains a graph attention network to produce beamformers from channel and jamming conditions, then embeds that network in a two-agent MADDPG controller for UAV displacement and jammer-power updates. The strategy spaces enforce UAV transmit-power and deployment limits together with individual and aggregate jammer-power limits. Simulations report stable learning convergence and higher transmission rates than GCN, MLP, successive-convex-approximation, DDQN, and genetic-algorithm baselines across the tested configurations. The graph representation also permits fine-tuned transfer to different numbers of legitimate links and jammers while keeping inference time comparatively stable.

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
