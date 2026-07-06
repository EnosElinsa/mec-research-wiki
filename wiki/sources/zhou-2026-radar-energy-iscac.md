---
type: source
title: "Trade-Off Between Radar Sensing and Energy Consumption in Integrated Sensing, Computing, and Communication UAV Network"
authors: ["Yige Zhou", "Xin Liu"]
year: 2026
url: "https://doi.org/10.1109/TGCN.2025.3587751"
venue: "IEEE Transactions on Green Communications and Networking (IEEE TGCN), vol. 10, pp. 511-521, 2026"
tags: [source, iscc, iscac, radar-sensing, uav-hap, energy-efficiency, trajectory-optimization, sca]
related:
  - "[[integrated-sensing-computation-communication]]"
  - "[[radar-sensing-energy-tradeoff]]"
  - "[[hierarchical-aerial-mec]]"
  - "[[high-altitude-platform-station]]"
  - "[[uav-trajectory-control]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[two-stage-decomposition]]"
  - "[[mmwave-radar-sensing]]"
created: 2026-07-07
updated: 2026-07-07
---

# Trade-Off Between Radar Sensing and Energy Consumption in Integrated Sensing, Computing, and Communication UAV Network

## Citation

Zhou, Y., & Liu, X. (2026). *Trade-Off Between Radar Sensing and Energy Consumption in Integrated Sensing, Computing, and Communication UAV Network*. **IEEE Transactions on Green Communications and Networking**, 10, 511-521. DOI: 10.1109/TGCN.2025.3587751. The top-level local parse is silent on DOI; DOI/venue/year were verified against a title-matched Crossref/IEEE DOI record.

## TL;DR

Models a multi-UAV ISCAC system where UAVs sense ground users, process some radar data locally, and offload remaining sensing data to a HAP MEC server. A three-layer alternating algorithm jointly optimizes sensing scheduling, UAV transmit power, and UAV/HAP trajectories to trade radar sensing-data volume against total system energy.

## Problem

UAV-enabled ISAC improves sensing coverage, but radar sensing, communication offloading, onboard computing, HAP computing, and mobility all consume energy. The paper asks how to maximize radar sensing data while minimizing total energy in a multi-UAV and HAP-assisted [[integrated-sensing-computation-communication|ISCAC]] system.

## System model

The network contains ground users, multiple UAVs, and a HAP. Each UAV carries an ISAC device and MEC server, senses users during the first subslot of each time slot, and offloads sensing data to the HAP during the second subslot. Radar sensing is scheduled so each UAV senses at most one user and each user is sensed by at most one UAV in a slot. Computation splits between UAV local processing and HAP processing, with latency constrained by the maximum of local and HAP-side processing paths. Energy includes UAV radar transmit, offloading transmit, computation, propulsion, and HAP computation/propulsion terms.

## Method

The non-convex optimization is decomposed into three subproblems:

- sensing scheduling optimization;
- UAV transmit-power optimization;
- UAV-HAP trajectory optimization.

Relaxation and [[alternating-optimization-sdr-sca|successive convex approximation]] convert the subproblems into tractable convex forms where possible. Algorithm 2 alternates over the three layers and converges to at least one local optimum according to the parse.

## Key findings

- In a 1.2 km by 1.2 km simulation area, optimized UAV/HAP trajectories reduce unnecessary motion while preserving radar sensing and LoS connectivity.
- At an equivalent sensing-data amount of 100 Mbits, the proposed scheme reduces energy consumption by 28.7% versus the ground-AP design and 20.3% versus the initial-trajectories design.
- Under the same 40 J energy constraint, it improves sensing performance by 34.7% and 24.6% over those two benchmarks.
- The proposed scheme maintains the lowest total energy as HAP CPU frequency and UAV CPU frequency vary in the reported figures.
- Energy consumption per megabit decreases as UAV bandwidth increases, and the proposed scheme remains lowest under identical bandwidth conditions.

## Limitations / future work

The conclusion does not list future work. The method is a local iterative optimization rather than a global optimum guarantee, and the evaluation is numerical simulation.

## Relation to the corpus

This source extends [[integrated-sensing-computation-communication]] from single-UAV or learning-centric entries into a classical [[radar-sensing-energy-tradeoff]] problem with a HAP edge server. It is close to [[zhao-2026-mappo-jscc-aec]] in coupling sensing data, UAV control, and HAP computation, but it uses SCA/alternating optimization rather than MAPPO-based control.

## Raw artifacts

- `raw/sources/Trade-Off Between Radar Sensing and Energy Consumption in Integrated Sensing- Computing- and Communication UAV Network/Trade-Off Between Radar Sensing and Energy Consumption in Integrated Sensing- Computing- and Communication UAV Network.md`
- Original PDF and extracted figures (`images/`) in the same folder.
