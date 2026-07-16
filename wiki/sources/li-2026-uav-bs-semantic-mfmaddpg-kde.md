---
type: source
title: "3D Deployment of UAV-BSs in Semantic Communication Networks: Mean-Field Multi-Agent Reinforcement Learning Approach"
authors: ["Hui Li", "Kun Zhu", "Tianxu Li", "Heng Zhu", "Jingfeng Zhang"]
year: 2026
url: "https://doi.org/10.1109/TWC.2025.3641947"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, semantic-communication, uav-base-station, drone-cell-placement, mean-field-marl, maddpg, kernel-density-estimation, bleu-score]
related:
  - "[[semantic-communication]]"
  - "[[kernel-density-mean-field-marl]]"
  - "[[maddpg]]"
  - "[[mean-field-game]]"
  - "[[drone-cell-3d-placement]]"
  - "[[multi-modal-semantic-communication]]"
  - "[[zhao-2025-probabilistic-semantic-sagin]]"
  - "[[wang-2026-diffusion-semantic-uav-edge]]"
  - "[[he-2023-fairness-3d-multiuav-maddpg]]"
created: 2026-07-07
updated: 2026-07-16
modeling_card: required
---

# 3D Deployment of UAV-BSs in Semantic Communication Networks: Mean-Field Multi-Agent Reinforcement Learning Approach

## Citation

Li, H., Zhu, K., Li, T., Zhu, H., & Zhang, J. (2026). *3D Deployment of UAV-BSs in Semantic Communication Networks: Mean-Field Multi-Agent Reinforcement Learning Approach*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2025.3641947.

## TL;DR

Treats 3-D UAV base-station deployment as a semantic-fidelity problem rather than a bit-throughput problem. The method extends mean-field MADDPG with kernel density estimation (MF-MADDPG-KDE), so each UAV models a distribution of neighboring actions in continuous 3-D deployment space. A BLEU-based reward, mapped from SINR through a DeepSC-style fitting pipeline, guides UAV-BSs toward high-semantic-value user regions.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Multiple UAV base stations serve fixed ground-user hotspots in 3-D space. Each UAV serves one cluster, uses OFDMA inside the cluster, and shares spectrum with other clusters under frequency reuse one; links follow probabilistic LoS/NLoS air-to-ground channels.

**Problem & objective**: Semantic-aware 3-D deployment, a continuous multi-agent optimization, maximizes aggregate semantic fidelity, $\max_{\mathbf q,\mathbf p}\sum_{i}\sum_{k_i}\mathrm{BLEU}_{i,k_i}(\mathrm{SINR}_{i,k_i})$, subject to SINR, flight-region, power, and interference-filtering constraints.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV position | $\mathbf q_i=[x_i,y_i,z_i]$ | continuous 3-D, $z_{\min}\le z_i\le z_{\max}$ | Deployment location of UAV-BS $i$ |
| Downlink power | $p_{k_i,i}$ | continuous, bounded | Power allocated by UAV $i$ to user $k_i$ |
| Neighbor action statistic | $\bar a_i$ | continuous distribution | Mean-field representation of neighboring UAV actions |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Each UAV stays in the permitted 3-D deployment region and altitude interval |
| C2 | Each served user meets the semantic-quality threshold, $\mathrm{SINR}_{k_i,i}\ge\mathrm{SINR}_{th}$ |
| C3 | Per-user and per-UAV transmit powers obey their bounds |
| C4 | Only path-loss-qualified cross-cluster links contribute interference in the filtered SINR model |

**Algorithm**: Fit a differentiable SINR-to-BLEU mapping from DeepSC samples → apply mean-field MADDPG for scalable coordination → estimate continuous neighbor-action distributions with KDE → train centralized critics and decentralized actors until the BLEU reward converges.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Li et al. [x] studied three-dimensional deployment of large-scale UAV base stations for semantic communication. They formulated a continuous multi-agent deployment problem that maximizes a BLEU-based semantic-fidelity objective under SINR, power, altitude, and deployment-region constraints. The system uses OFDMA within each user cluster and frequency reuse one across clusters, so UAV positions jointly affect useful links and inter-cluster interference. They proposed MF-MADDPG-KDE, which combines mean-field coordination with kernel density estimation for continuous neighbor-action distributions and uses an SINR-to-BLEU fitting pipeline for the reward. Simulations report higher semantic transmission quality and more stable training than discrete action mapping and epsilon-net baselines, including a 36-UAV deployment experiment.

## Problem

Large multi-UAV communication systems are usually optimized for bit-level throughput, energy, or coverage. In semantic communication, those objectives can miss whether the received content preserves task meaning, especially under low SINR. The paper asks how to deploy large-scale UAV-BSs when the target is semantic restoration quality and the joint action space is continuous and high-dimensional.

## System model

- Multiple UAV-BSs serve user hotspots / points of interest in a 3-D region.
- Semantic quality is measured with BLEU and connected to physical-layer SINR through DeepSC-based simulation and least-squares fitting.
- Interference is reduced to relevant links by a path-loss threshold, limiting long-range interference calculations.
- UAV deployment is learned as a multi-agent continuous-control problem.

## Method

- **Mean-field reduction.** Neighbor interactions are approximated through an aggregate neighborhood behavior, improving scalability for many UAVs.
- **KDE action modeling.** Kernel density estimation replaces a single mean or coarse action map with a smoothed distribution over neighboring continuous actions.
- **Semantic reward.** The reward uses BLEU only when SINR exceeds a threshold, aligning the policy with semantic-fidelity recovery rather than raw bit rate.

## Key findings

- In 4-, 6-, and 9-UAV tests, MF-MADDPG-KDE reports the highest final rewards: 21696.76, 31839.374, and 45839.70, with training times of 2780.15 s, 3184.60 s, and 5829.41 s.
- The method outperforms fine/coarse discrete action mapping and epsilon-net approximations, especially as the UAV count grows.
- In a 36-UAV test, the BLEU-based reward stabilizes around 185000, indicating scalability to a larger multi-agent deployment setting in the parse.
- The evaluation is simulation-based and communication-focused, not MEC offloading.

## Relation to the corpus

This source expands [[semantic-communication]] from UAV-assisted edge processing and SAGIN semantics into aerial-BS deployment. It links the semantic-communication track to [[drone-cell-3d-placement]] and [[maddpg]], while [[kernel-density-mean-field-marl]] captures the paper's specific continuous-action mean-field approximation. It is adjacent to [[wang-2026-diffusion-semantic-uav-edge]], which optimizes semantic extraction/transmission/recovery around UAV edge computing, and [[zhao-2025-probabilistic-semantic-sagin]], which reduces semantic transmission energy through shared probabilistic graphs.

## Raw artifacts

- `raw/sources/3D_Deployment_of_UAV-BSs_in_Semantic_Communication_Networks_Mean-Field_Multi-Agent_Reinforcement_Learning_Approach/3D_Deployment_of_UAV-BSs_in_Semantic_Communication_Networks_Mean-Field_Multi-Agent_Reinforcement_Learning_Approach.md`
- Original PDF and extracted figures (`images/`) in the same folder.
