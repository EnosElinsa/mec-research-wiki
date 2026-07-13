---
type: source
title: "Attention-Based Hierarchical-DRL With Mask for Multi-Timescale Caching, Association, and Secure Content Delivery in UAV-Enabled ISAC Networks"
authors: ["Gezahegn Abdissa Bayessa", "Rong Chai", "Chengchao Liang", "Qinyuan Wang", "Jun Li", "Qianbin Chen"]
year: ""
url: ""
venue: ""
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
updated: 2026-07-14
---

# Attention-Based Hierarchical-DRL With Mask for Multi-Timescale Caching, Association, and Secure Content Delivery in UAV-Enabled ISAC Networks

## Citation

Bayessa, G. A., Chai, R., Liang, C., Wang, Q., Li, J., & Chen, Q. *Attention-Based Hierarchical-DRL With Mask for Multi-Timescale Caching, Association, and Secure Content Delivery in UAV-Enabled ISAC Networks*. The local parse gives the title and author line but does not expose reliable publication year, venue, or DOI metadata; those fields are left blank rather than inferred.

## TL;DR

Studies secure content delivery in UAV-enabled ISAC networks where UAVs cache requested content, serve mobile users, and sense mobile UAV eavesdroppers. The proposed attention-based hierarchical DRL separates long-timescale caching from short-timescale association, deployment, and beamforming, using action masks to keep DDQN decisions inside feasibility constraints.

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
