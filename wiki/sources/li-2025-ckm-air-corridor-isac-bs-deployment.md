---
type: source
title: "Channel Knowledge Map Enabled Low-Altitude ISAC Networks: Joint Air Corridor Planning and Base Station Deployment"
authors: ["Jiaxuan Li", "Yilong Chen", "Fan Liu", "Jie Xu"]
year: 2025
url: "https://doi.org/10.1109/LWC.2025.3642429"
venue: "IEEE Wireless Communications Letters"
modeling_card: required
tags: [source, channel-knowledge-map, air-corridor, base-station-deployment, isac, low-altitude-economy, integer-programming]
related:
  - "[[channel-knowledge-map]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[low-altitude-intelligent-network]]"
  - "[[anti-uav-interference-base-station-deployment]]"
  - "[[fan-liu]]"
  - "[[jie-xu]]"
created: 2026-11-02
updated: 2026-11-02
---

# Channel Knowledge Map Enabled Low-Altitude ISAC Networks: Joint Air Corridor Planning and Base Station Deployment

## Citation

Li, J., Chen, Y., Liu, F., & Xu, J. (2025). *Channel Knowledge Map Enabled Low-Altitude ISAC Networks: Joint Air Corridor Planning and Base Station Deployment*. **IEEE Wireless Communications Letters**. DOI: 10.1109/LWC.2025.3642429.

## TL;DR

UAVs fly within a structured air corridor of connected cubic segments, and ground base stations must be placed so the corridor has both sensing and communication coverage. Using a CKM to predict each candidate site's channels offline, the letter minimizes a weighted sum of corridor length and the number of deployed BSs, solved with a coarse-to-fine grid decomposition.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: An urban area is gridded into $N\times N$ cells $\mathcal R_{i,j}$ at corridor height. UAVs travel from a departure point to a destination inside a corridor to be designed, and $K$ candidate BS sites can host ISAC base stations with transmit power $P$ and gain $G$. CKMs give minimum and maximum channel gains $h^{\min}_{k,i,j}$, $h^{\max}_{k,i,j}$ and LoS indicators $\mathcal L_{k,i,j}$ per cell.

**Problem & objective**: (P1), a nonconvex integer program: $\min_{\mathbf A,\boldsymbol\delta}\ \alpha_1\mathbf 1^\top\mathbf A\mathbf 1+\alpha_2\sum_{k=1}^K\delta_k$ with $\alpha_1+\alpha_2=1$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Corridor cells | $A_{i,j}$ | binary | Cell $(i,j)$ belongs to the air corridor |
| BS deployment | $\delta_k$ | binary | A BS is deployed at candidate site $k$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| (9a) | Sensing power, $\sum_k\delta_kp_{k,i,j}\ge\epsilon_1A_{i,j}$. |
| (9b) | LoS visibility from at least three BSs, $\sum_k\delta_k\mathcal L_{k,i,j}\ge3A_{i,j}$. |
| (9c) | Worst-case communication SINR, $\max_k\underline\gamma_{k,i,j}(\boldsymbol\delta)\ge\epsilon_2A_{i,j}$. |
| (9d) | Binary $\delta_k$ and $A_{i,j}$. |
| (2)-(4) | Corridor connectivity from departure to destination. |

**Algorithm**: Hierarchical coarse-to-fine grid decomposition. The coarse layer reformulates the problem as a linear integer program to obtain a feasible corridor and deployment. The fine layer refines it by alternating optimization of corridor cells and BS selection.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Li et al. [x] addressed joint air corridor planning and base station deployment for low-altitude integrated sensing and communication networks. In their system, unmanned aerial vehicles operate within a structured air corridor composed of connected cubic segments, and multiple base stations are selectively deployed at candidate locations to provide sensing and communication coverage throughout the corridor. They leveraged the channel knowledge map to characterize wireless channels for candidate sites before deployment, enabling offline planning. The system cost, a weighted sum of the air corridor length and the number of deployed base stations, is minimized subject to sensing and communication performance constraints, and the resulting large-scale nonconvex integer program is solved with a hierarchical coarse-to-fine grid decomposition algorithm. Simulation results show that the joint design reduces corridor length and deployment cost compared with benchmark schemes while ensuring coverage.

## Problem framing

Corridor routing and ISAC infrastructure are usually planned separately. Joint planning lets the corridor bend toward well-covered regions so fewer BSs are needed.

## System model

- Communication coverage uses the worst-case SINR over sampling points in each cell, with interference from other deployed BSs at maximum gain.
- Sensing assumes monostatic LoS echoes and needs at least three LoS BSs for localization.

## Method

The decision space has $N^2+K$ binary variables, which motivates decomposition rather than relaxation.

## Key findings

- The method yields shorter corridors and fewer BSs than the baseline methods.
- CKMs allow candidate sites to be evaluated without real-time measurements.

## Limitations / future work

Results depend on CKM accuracy and a fixed corridor height.

## Relation to the corpus

Uses [[channel-knowledge-map]] priors for [[integrated-sensing-and-communication]] infrastructure in the [[low-altitude-intelligent-network]]; a related deployment problem is [[anti-uav-interference-base-station-deployment]].

## Raw artifacts

- Parse: `raw/sources/Channel_Knowledge_Map_Enabled_Low-Altitude_ISAC_Networks_Joint_Air_Corridor_Planning_and_Base_Station_Deployment/Channel_Knowledge_Map_Enabled_Low-Altitude_ISAC_Networks_Joint_Air_Corridor_Planning_and_Base_Station_Deployment.md`
- Extracted figures are in the same folder; no companion PDF is present.
