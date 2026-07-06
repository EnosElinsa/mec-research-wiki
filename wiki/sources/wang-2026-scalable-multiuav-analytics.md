---
type: source
title: "Toward Inference Latency Optimization for Scalable Collaborative Multi-UAV Analytics"
authors: ["Ying Wang", "Jingling Yuan", "Wenbo Wu", "Quanfeng Yao", "Donglei Xu", "Zhishu Shen"]
year: 2026
url: "https://doi.org/10.1109/TGCN.2025.3625726"
venue: "IEEE Transactions on Green Communications and Networking (IEEE TGCN), vol. 10, pp. 1364-1377, 2026"
tags: [source, collaborative-uav-analytics, video-analytics, dag-partition, computation-offloading, mappo, green-computing]
related:
  - "[[scalable-uav-video-analytics]]"
  - "[[video-analytics-offloading]]"
  - "[[collaborative-dl-inference]]"
  - "[[interdependent-tasks-dag]]"
  - "[[task-offloading]]"
  - "[[mappo]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[uav-trajectory-control]]"
created: 2026-07-07
updated: 2026-07-07
---

# Toward Inference Latency Optimization for Scalable Collaborative Multi-UAV Analytics

## Citation

Wang, Y., Yuan, J., Wu, W., Yao, Q., Xu, D., & Shen, Z. (2026). *Toward Inference Latency Optimization for Scalable Collaborative Multi-UAV Analytics*. **IEEE Transactions on Green Communications and Networking**, 10, 1364-1377. DOI: 10.1109/TGCN.2025.3625726. The top-level local parse is silent on DOI; DOI/venue/year were verified against a title-matched Crossref/IEEE DOI record.

## TL;DR

Builds a scalable collaborative multi-UAV video-analytics architecture where UAVs capture video, run partial DNN inference, and offload remaining DAG stages to neighboring UAVs. It uses JDTSO for small centralized swarms and MAPDP for larger distributed swarms, trading inference latency, energy consumption, and throughput as UAV scale changes.

## Problem

Collaborative UAV video analytics is constrained by onboard compute, energy, and bandwidth. A small UAV swarm with reliable BS connectivity can use centralized deployment and scheduling, while large swarms or weak BS links need distributed control. The paper therefore asks how to optimize inference latency and energy efficiency across both regimes rather than using one controller for all scales.

## System model

Each UAV captures real-time video, extracts regions of interest, and processes an attribute-recognition task modeled as a [[interdependent-tasks-dag|DAG]] of DNN classifiers. Classification can stop at a partition point on the source UAV, after which the task is sent to an adjacent UAV for further classification. UAVs communicate with each other and with a BS over wireless links such as Wi-Fi or Radio-over-IP. The centralized model includes UAV deployment, computation offloading, communication resource allocation, and DAG partition decisions; the distributed model is posed as a Dec-POMDP for UAV cooperation.

## Method

The UCAA architecture switches between two optimization styles:

- **JDTSO** for centralized control: a two-layer algorithm uses a genetic algorithm for UAV positions, dynamic programming for offloading decisions, convex optimization for communication resources, and brute-force DAG partition enumeration.
- **MAPDP** for distributed control: [[mappo|MAPPO]] supplies centralized-value / distributed-policy learning, while a separate DAG partition strategy decouples partition-point selection from policy training.

## Key findings

- JDTSO has the lowest inference latency, energy consumption, and highest throughput when the UAV count is 20 or fewer in the reported simulations.
- MAPDP performs better for larger swarms above 20 UAVs, supporting the paper's architecture split between centralized small-scale and distributed large-scale operation.
- The proposed methods outperform Random, C-DQN, C-PPO, MADDPG, and independent-UAV baselines in the reported latency, energy, and throughput comparisons.
- MAPDP reward convergence is sensitive to learning rates; the parse reports 0.005 as a balanced setting for the policy learning rate in the 60-UAV experiment.
- Energy-efficiency sensitivity at 60 UAVs mainly lowers average energy consumption without materially changing average latency or throughput in the reported table.

## Limitations / future work

The conclusion says future work will consider UAV trajectory planning, mobility constraints such as minimum turning radius and climb rate, interference from other UAVs, and DRL algorithms for more dynamic and complex scenarios. The reported setup uses simulation and pre-measured Raspberry Pi / Movidius inference parameters rather than a full UAV hardware deployment.

## Relation to the corpus

This source extends [[video-analytics-offloading]] from single-stream UAV/HAP analytics toward [[scalable-uav-video-analytics]] in a collaborative UAV swarm. It also complements [[collaborative-dl-inference]] by treating classifier-level DAG partitioning as the unit of offloaded inference, rather than only DNN layer partitioning or secure split inference as in [[wu-2026-secure-split-offloading-ci]].

## Raw artifacts

- `raw/sources/Toward Inference Latency Optimization for Scalable Collaborative Multi-UAV Analytics/Toward Inference Latency Optimization for Scalable Collaborative Multi-UAV Analytics.md`
- Original PDF and extracted figures (`images/`) in the same folder.
