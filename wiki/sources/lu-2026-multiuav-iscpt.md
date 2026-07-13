---
type: source
title: "Multi-UAV Collaborative ISCPT: Joint 3D Deployment and Power Control of UAVs"
authors: ["Yuping Lu", "Ke Xiong", "Wei Chen", "Pingyi Fan", "Derrick Wing Kwan Ng", "Khaled Ben Letaief"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3683050"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), pp. 1-16"
tags: [source, iscpt, multi-uav, three-dimensional-deployment, power-control, graph-attention, multi-objective-optimization]
related:
  - "[[integrated-sensing-communication-power-transfer]]"
  - "[[cascading-residual-graph-attention-network]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[simultaneous-wireless-information-and-power-transfer]]"
  - "[[rf-energy-harvesting]]"
  - "[[graph-neural-network]]"
  - "[[air-to-ground-channel-model]]"
  - "[[ke-xiong]]"
  - "[[pingyi-fan]]"
  - "[[derrick-wing-kwan-ng]]"
  - "[[khaled-ben-letaief]]"
created: 2026-07-13
updated: 2026-07-13
---

# Multi-UAV Collaborative ISCPT: Joint 3D Deployment and Power Control of UAVs

## Citation

Lu, Y., Xiong, K., Chen, W., Fan, P., Ng, D. W. K., & Letaief, K. B. (2026). *Multi-UAV Collaborative ISCPT: Joint 3D Deployment and Power Control of UAVs*. **IEEE Transactions on Mobile Computing**, 1-16. DOI: 10.1109/TMC.2026.3683050.

## TL;DR

Uses a cascading residual graph-attention network to generate static 3-D multi-UAV deployment and transmit powers for integrated sensing, communication, and power transfer, optimizing normalized worst-user SINR, sensing echo power, and harvested energy.

## Problem and system model

A centralized ground station deploys single-antenna UAVs over information users, sensing targets, and RF-energy users. Probabilistic-LoS air-to-ground gains govern all links. Information users associate with the UAV giving highest SINR, all UAVs illuminate sensing targets, and energy users aggregate nonlinear harvested power from every UAV.

The multi-objective problem chooses each UAV's 3-D location and power to maximize the minimum communication SINR, minimum sensing received-signal power, and minimum harvested energy. These objectives conflict because inter-UAV signals interfere with data reception but can strengthen sensing and energy transfer.

## Method

[[cascading-residual-graph-attention-network|CRGAT]] represents users as nodes with type and coordinates and pairwise distance as directed edge features. One residual graph-attention block predicts all UAV coordinates; a learned deployment encoding is injected into a second block that predicts powers. Training directly differentiates a normalized weighted sum of the three physical metrics. This is neural optimization, not reinforcement learning.

Each preference vector requires a separately trained model. Offline training is expensive, but one trained model produces deployment and power through a single forward pass.

## Key findings

- The prose reports more than 39.6% higher composite performance than the baselines, but does not identify one denominator or physical metric for that percentage.
- In the main four-UAV case, two UAVs move toward communication/energy users and two toward sensing targets.
- With total power fixed at 4 W, more UAVs improve weighted performance with diminishing returns; sensing improves, communication SINR falls through added interference, and energy remains comparatively stable.
- Training at 72 users transfers across user counts without retraining, but changing among three spatial-layout families is evaluated through retraining.
- A 0.05 preference grid trains 225 models and yields 104 non-dominated solutions; a denser 0.02 grid uses 1,326 separately trained models.

## Limitations

Evaluation is simulation-only. Deployment is static and omits trajectories, repositioning energy/time, collision constraints, and UAV dynamics. The design assumes known user locations, centralized control, out-of-band command/echo links, matched filtering, and single antennas. No exact optimizer supplies a global-optimality gap. The fully connected user graph grows quadratically, and Pareto coverage requires many separately trained models rather than one preference-conditioned policy.

## Relation to the corpus

This source extends [[integrated-sensing-and-communication]] and [[simultaneous-wireless-information-and-power-transfer]] into three-function aerial [[integrated-sensing-communication-power-transfer|ISCPT]]. It differs from trajectory-oriented UAV-ISAC sources by learning static placement and power directly from a graph of heterogeneous ground services.

## Raw artifacts

- Parse: `raw/sources/Multi-UAV_Collaborative_ISCPT_Joint_3D_Deployment_and_Power_Control_of_UAVs/Multi-UAV_Collaborative_ISCPT_Joint_3D_Deployment_and_Power_Control_of_UAVs.md`
- Origin PDF and extracted figures (`images/`) are in the same folder.
