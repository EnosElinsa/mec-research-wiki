---
type: source
title: "Joint UAV 3D Deployment and Ground Device Association Optimizing for Multi-UAV-Aided MEC Heterogeneous Network"
authors: ["Yunfei Gao", "Peng Wu", "Xiaopeng Yuan", "Yulin Hu", "Xiaoxiang Cao", "Anke Schmeink"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3656412"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), vol. 25, no. 7, Jul. 2026"
modeling_card: required
tags: [source, multi-uav-assisted-mec, device-association, uav-3d-deployment, dueling-dqn, federated-reinforcement-learning, optimal-transport-theory, no-fly-zone]
related:
  - "[[device-association]]"
  - "[[optimal-transport-theory]]"
  - "[[dueling-dqn]]"
  - "[[federated-reinforcement-learning]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[uav-trajectory-control]]"
  - "[[gao-2024-d3qn-uav-mec-mobile-gt]]"
created: 2026-07-07
updated: 2026-07-16
---

# Joint UAV 3D Deployment and Ground Device Association Optimizing for Multi-UAV-Aided MEC Heterogeneous Network

## Citation

Gao, Y., Wu, P., Yuan, X., Hu, Y., Cao, X., & Schmeink, A. (2026). *Joint UAV 3D Deployment and Ground Device Association Optimizing for Multi-UAV-Aided MEC Heterogeneous Network*. **IEEE Transactions on Mobile Computing**, 25(7), 9754-9769. DOI: 10.1109/TMC.2026.3656412.

## TL;DR

Optimizes 3D UAV deployment and ground-device association in a dynamic heterogeneous multi-UAV MEC network with no-fly zones. The paper first derives a closed-form GD association rule using Lagrangian duality and [[optimal-transport-theory]], then uses that association inside a federated multi-agent dueling DDQN controller, FMAD3QN-CUA, for UAV 3D deployment. The goal is to minimize average system operation time for communication, computation, and joint decision-making service.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Heterogeneous UAV MEC servers provide communication, computation, and joint decision-making for ground devices with stochastic requests, heterogeneous task sizes and priorities, and FDMA access. Each service stage jointly assigns every device to one UAV and places UAVs in three dimensions while avoiding no-fly zones under probabilistic LoS and NLoS channels.

**Problem & objective**: Problem P1 is an NP-hard MINLP that minimizes weighted average task delay, $\min_{\mathbf D_{k,n},\mathbf Q_{k,n}}T$, over GD association regions and UAV 3D deployment.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| GD association region | $D_{k,n}$ | spatial partition | Ground region served by UAV $k$ in stage $n$ |
| GD-UAV association | $\varphi_{k,u}$ | binary, $\{0,1\}$ | Whether GD $u$ is assigned to UAV $k$ |
| UAV 3D deployment | $\mathbf q_{k,n}=[x_k,y_k,z_k]$ | continuous within deployment bounds | Location of UAV $k$ in stage $n$ |
| UAV movement action | $a_{k,n}$ | discrete 3D action | Deployment adjustment selected by each FMAD3QN agent |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| 18a | Different UAV service regions do not overlap, $D_{k,n}\cap D_{k^*,n}=\emptyset$ |
| 18b | The union of UAV regions covers the entire service domain |
| 18c-18d | UAVs remain outside no-fly zones and GDs remain inside the service domain |
| 18e-18f | Association is binary and each GD selects exactly one UAV, $\sum_k\varphi_{k,u}=1$ |
| 18g-18i | UAV coordinates remain within the allowed horizontal and altitude ranges |

**Algorithm**: For fixed UAV locations, relax association, apply optimal transport and Lagrangian duality, and recover the integral closed-form GD-UAV mapping; substitute that mapping into the deployment subproblem; model each UAV as an agent whose state and action describe 3D placement and whose reward is negative average delay; train federated multi-agent dueling DDQN policies and aggregate local parameters at the selected frequency.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Gao et al. [x] studied joint three-dimensional UAV deployment and ground-device association in a dynamic heterogeneous multi-UAV MEC network with no-fly zones. They formulated an NP-hard mixed-integer nonconvex program that minimizes weighted average task delay over UAV locations and binary device associations under nonoverlapping coverage, complete assignment, no-fly-zone, and deployment-bound constraints. Their solution derives a closed-form association through Lagrangian duality and optimal transport theory, then embeds it in FMAD3QN-CUA, a federated multi-agent dueling DDQN controller for UAV deployment. Simulations show that the closed-form association matches exhaustive-search delay with much lower runtime and that FMAD3QN-CUA improves training stability and outperforms the evaluated Voronoi, K-means, and non-dueling variants.

## Problem

Ground devices generate stochastic, heterogeneous, priority-differentiated requests. UAVs differ in computation capability and must avoid no-fly zones while serving as aerial MEC nodes. Jointly optimizing UAV locations and GD association is non-convex and scales quickly with the number of UAVs and GDs; exhaustive association search is not practical for real-time deployment.

## System model

- The network has K UAVs and U ground devices in a 3D service region with no-fly zones and obstacles.
- Operation is divided into service stages; GD task requests follow a Bernoulli activity model and task sizes follow a Gamma distribution.
- UAVs collect GD data, process queued tasks sequentially, perform joint decision-making, and send results back to GDs.
- Tasks have priority classes; UAV queues use a priority-weighted sorting mechanism tied to transmission and computation time.
- UAV-GD links use a LoS/NLoS air-to-ground channel model with FDMA to avoid co-channel interference among GDs served by the same UAV.

## Method

The paper decomposes the joint problem by analytically solving GD association. The closed-form association has O(KU) complexity versus O(K^U) exhaustive search and is proven integral under the paper's assumptions. With association characterized, the remaining 3D deployment problem is modeled as an MDP and solved by FMAD3QN-CUA: a federated multi-agent DDQN variant with a dueling network architecture and reward computed from the closed-form association and resulting average delay.

## Key findings

- The closed-form association matches exhaustive-search performance in the reported average task-completion-time test while substantially reducing complexity.
- Against Voronoi and K-means association, the performance gap widens when UAV computation frequency decreases; the parse reports gaps from 18.4% to 30.9% versus Voronoi and from 30% to 38.3% versus K-means.
- Runtime for closed-form association stays nearly flat as GD count grows, from 0.000343 s to 0.000392 s in the reported tests, while exhaustive search grows from 0.003009 s to 38.968381 s.
- FMAD3QN-CUA reaches performance close to FMAD3QN-ESUA but avoids exhaustive association; it outperforms FMADDQN-CUA, FMAD3QN-VUA, and FMAD3QN-KUA.
- The dueling architecture improves training stability compared with the non-dueling FMADDQN-CUA variant.
- Deployment visualizations show UAVs adapting across service stages, avoiding no-fly zones, and prioritizing high-priority GDs by associating them with higher-compute UAVs.

## Limitations / future work

The results are simulation-only. The paper's conclusion proposes meta-learning and graph neural networks for faster adaptation to unseen environments, and extension to ultra-dense integrated sensing, communication, and computing scenarios.

## Relation to the corpus

This source expands [[device-association]] from heuristic or matching-based association into a closed-form [[optimal-transport-theory]] association rule coupled with federated dueling DDQN deployment. It is close to [[gao-2024-d3qn-uav-mec-mobile-gt]] in using D3QN-style value learning for UAV-MEC deployment, but this paper adds heterogeneous task priorities, no-fly zones, federated multi-agent training, and an analytical association subroutine.

## Raw artifacts

- `raw/sources/Joint UAV 3D Deployment and Ground Device Association Optimizing for Multi-UAV-Aided MEC Heterogeneous Network/Joint UAV 3D Deployment and Ground Device Association Optimizing for Multi-UAV-Aided MEC Heterogeneous Network.md`
- Original PDF and extracted figures (`images/`) in the same folder.
