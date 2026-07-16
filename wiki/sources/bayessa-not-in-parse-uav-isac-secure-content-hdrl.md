---
type: source
title: "Attention-Based Hierarchical-DRL With Mask for Multi-Timescale Caching, Association, and Secure Content Delivery in UAV-Enabled ISAC Networks"
authors: ["Gezahegn Abdissa Bayessa", "Rong Chai", "Chengchao Liang", "Qinyuan Wang", "Jun Li", "Qianbin Chen"]
year: ""
url: ""
venue: ""
modeling_card: required
tags: [source, integrated-sensing-and-communication, secure-content-delivery, hierarchical-drl, action-mask, ddqn, content-caching, crlb, physical-layer-security]
related:
  - "[[integrated-sensing-and-communication]]"
  - "[[action-masked-hierarchical-drl]]"
  - "[[hierarchical-reinforcement-learning]]"
  - "[[ddqn]]"
  - "[[service-caching-mec]]"
  - "[[secure-caching-uav-mec]]"
  - "[[cramer-rao-bound]]"
  - "[[physical-layer-security]]"
  - "[[yao-2025-secure-isac-dual-eavesdropping]]"
  - "[[bai-2026-aoi-uav-isac]]"
  - "[[rong-chai]]"
  - "[[qianbin-chen]]"
created: 2026-07-11
updated: 2026-07-16
---

# Attention-Based Hierarchical-DRL With Mask for Multi-Timescale Caching, Association, and Secure Content Delivery in UAV-Enabled ISAC Networks

## Citation

Bayessa, G. A., Chai, R., Liang, C., Wang, Q., Li, J., & Chen, Q. *Attention-Based Hierarchical-DRL With Mask for Multi-Timescale Caching, Association, and Secure Content Delivery in UAV-Enabled ISAC Networks*. The local parse gives the title and author line but does not expose reliable publication year, venue, or DOI metadata; those fields are left blank rather than inferred.

## TL;DR

Studies secure content delivery in UAV-enabled ISAC networks where UAVs cache requested content, serve mobile users, and sense mobile UAV eavesdroppers. The proposed attention-based hierarchical DRL separates long-timescale caching from short-timescale association, deployment, and beamforming, using action masks to keep DDQN decisions inside feasibility constraints.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Multi-antenna ISAC UAVs cache files and deliver requested content to mobile single-antenna UEs while sensing multiple mobile UAV eavesdroppers. Each long-timescale frame contains short-timescale slots, content delivery uses OFDMA subcarriers, and estimated eavesdropper positions feed the deployment and beamforming decisions.

**Problem & objective**: Problem P2 in (28) is a mixed-integer nonlinear program that maximizes the expected long-term secure content delivery throughput, $\lim_{T\to\infty}\mathbb{E}\left[\frac{1}{T}\sum_t\sum_{j=1}^{J}\sum_{i=1}^{I}\alpha_{i,j}^{t}\hat{R}_{i,j}^{\mathrm{sc},t}\right]$, over caching, association, deployment, and communication/sensing beamforming.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Content caching | $\delta_{j,f}^{\ell}$ | Binary, $\{0,1\}$ | Whether UAV $j$ caches file $f$ in frame $\ell$ |
| UE association | $\alpha_{i,j}^{t}$ | Binary, $\{0,1\}$ | Whether UE $i$ is associated with UAV $j$ in slot $t$ |
| UAV deployment | $\mathbf{q}_{j}^{t}=(x_j^t,y_j^t,z_j^t)$ | Continuous 3D coordinate | Position of UAV $j$ in slot $t$ |
| Joint beamforming | $\mathbf{W}_{j}^{t}$ | Complex matrix, $\mathbb{C}^{N\times(I+K)}$ | Communication and sensing beamformers of UAV $j$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1-C2 | Each UE associates with at most one UAV, $\sum_j\alpha_{i,j}^{t}\leq1$, and each UAV serves no more than its association limit |
| C3-C7 | UAV coordinates remain inside the allowed horizontal and altitude bounds, with minimum UAV-to-UAV and UAV-to-eavesdropper separation |
| C8-C10 | Secure rate, sensing accuracy, and power satisfy $R_{i,j}^{\mathrm{sc},t}\geq R_i^{\mathrm{th}}$, $\operatorname{Tr}(\mathbf{J}_{\hat{\mathbf{q}}_k^{e,t}}^{-1})\leq\kappa$, and $\lVert\mathbf{W}_j^t\rVert^2\leq P_{j,\max}$ |
| C11 | Content-delivery delay satisfies $\sum_f\gamma_{i,f}^{\ell}\alpha_{i,j}^{t}\delta_{j,f}^{\ell}\eta_f/R_{i,j}^{\mathrm{sc},t}\leq D_i^{\mathrm{th}}$ |
| C12 | Cache use satisfies $\sum_i\sum_f\eta_f\gamma_{i,f}^{\ell}\delta_{j,f}^{\ell}\leq\rho_j$ |

**Algorithm**: Maximum-likelihood time-of-arrival measurements are processed by EKF, FIM, and CRLB steps to estimate eavesdropper positions. A hierarchical controller then uses a DDQN for long-timescale caching and an attention-based DDQN for short-timescale association, deployment, and beamforming; its action mask assigns $-\infty$ Q-value to actions that violate the applicable constraints before action selection.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Bayessa et al. [x] studied long-term secure content delivery in a multi-UAV ISAC network with mobile users and mobile UAV eavesdroppers. They estimated eavesdropper locations from time-of-arrival measurements using maximum likelihood, an extended Kalman filter, a Fisher information matrix, and a Cramer-Rao lower bound. Given those estimates, they formulated a mixed-integer nonlinear program that maximizes long-term secure throughput by jointly selecting content caching, user association, UAV deployment, and communication and sensing beamforming under association, deployment, rate, sensing-accuracy, power, delay, and cache constraints. Their hierarchical solution uses a DDQN for long-timescale caching and an attention-based DDQN with an action mask for short-timescale association, deployment, and beamforming. Simulations reported the highest cumulative reward for the proposed method relative to attention-based DDQN, DDQN, and DQN baselines, and higher secure throughput than the evaluated reference algorithms. The reported secure throughput increased with UAV transmit power and decreased as the number of eavesdroppers or noise power increased.

## Problem

UAV content delivery is exposed to mobile aerial eavesdroppers, and secure throughput depends on a coupled set of decisions: eavesdropper localization, content caching, user association, UAV deployment, communication beamforming, and sensing beamforming. The resulting problem is a mixed-integer nonlinear program with different timescales and many feasibility constraints.

## System model

- Multi-antenna UAVs serve single-antenna UEs as aerial BSs while storing user-requested content files.
- An attacker deploys multiple UAV eavesdroppers that try to intercept content delivery.
- UAVs perform ISAC sensing, forward sensed information to a controller, and estimate eavesdropper positions.
- The model uses time frames for caching and time slots for association, deployment, communication, and sensing decisions.

## Method

The paper first estimates eavesdropper positions using TOA/MLE, FIM/CRLB, and EKF logic. It then decomposes secure throughput maximization into a long-timescale content-caching DDQN and a short-timescale attention-based DDQN with an action mask. The short-timescale policy jointly chooses user association, UAV deployment, communication beamforming, and sensing beamforming while masking infeasible actions before Q-value evaluation.

## Key findings

- The simulation setup includes `I = 9` UEs and `K = 2` eavesdroppers in a `1000 m x 1000 m` area, with 4 UAV antennas, 2.4 GHz carrier frequency, 40 MHz subcarrier bandwidth, 10 files, and file sizes in `[5, 10]` Mbits.
- The proposed HDRL with action mask obtains the highest cumulative reward compared with attention-DDQN, DDQN, and DQN baselines.
- Stable learning rates are reported around `1e-4` to `5e-4`; higher rates such as `0.001` and `0.005` cause volatile reward behavior.
- Secure throughput improves with higher UAV transmit power and stricter CRLB thresholds, decreases with more eavesdroppers or higher noise, and outperforms A2C / DDQN / DQN-style baselines in the plotted comparisons.

## Limitations / future work

The parse has OCR corruption in author punctuation, equations, and table units. Future work proposes mobile UAVs, aerial and ground eavesdroppers, game-theoretic adversary trajectories, jamming beamforming, and integration of caching, computation, and target detection at the UAVs.

## Relation to the corpus

This source combines [[integrated-sensing-and-communication]], [[physical-layer-security]], and caching control. It differs from [[yao-2025-secure-isac-dual-eavesdropping]], which focuses on joint beamforming and UAV trajectory under dual eavesdropping, by adding multi-timescale content caching and [[action-masked-hierarchical-drl]]. It also complements [[bai-2026-aoi-uav-isac]]: Bai et al. make freshness the ISAC target, while Bayessa et al. make secure throughput and content delivery the target.

## Raw artifacts

- `raw/sources/Attention-Based_Hierarchical-DRL_With_Mask_for_Multi-Timescale_Caching_Association_and_Secure_Content_Delivery_in_UAV-Enabled_ISAC_Networks/Attention-Based_Hierarchical-DRL_With_Mask_for_Multi-Timescale_Caching_Association_and_Secure_Content_Delivery_in_UAV-Enabled_ISAC_Networks.md`
- Original PDF and extracted figures (`images/`) in the same folder.
