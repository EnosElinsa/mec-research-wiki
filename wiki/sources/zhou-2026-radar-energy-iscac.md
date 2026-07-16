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
modeling_card: required
created: 2026-07-07
updated: 2026-07-16
---

# Trade-Off Between Radar Sensing and Energy Consumption in Integrated Sensing, Computing, and Communication UAV Network

## Citation

Zhou, Y., & Liu, X. (2026). *Trade-Off Between Radar Sensing and Energy Consumption in Integrated Sensing, Computing, and Communication UAV Network*. **IEEE Transactions on Green Communications and Networking**, 10, 511-521. DOI: 10.1109/TGCN.2025.3587751. The top-level local parse is silent on DOI; DOI/venue/year were verified against a title-matched Crossref/IEEE DOI record.

## TL;DR

Models a multi-UAV ISCAC system where UAVs sense ground users, process some radar data locally, and offload remaining sensing data to a HAP MEC server. A three-layer alternating algorithm jointly optimizes sensing scheduling, UAV transmit power, and UAV/HAP trajectories to trade radar sensing-data volume against total system energy.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Multiple UAVs sense ground users, process radar data locally, and offload the remaining data to a HAP MEC server through a two-subslot time-division protocol; the air links use LoS-dominant distance-dependent channels.

**Problem & objective**: Problem (29), a non-convex mixed scheduling, power, and trajectory program, maximizes $\sum_{n\in\mathcal N} l_{n,\mathrm{rad}}-\xi E_{\mathrm{tot}}$ to trade sensed radar data against total UAV and HAP energy.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Sensing schedule | $\alpha_{n,k}[z]$ | Binary | Whether UAV $n$ senses user $k$ in slot $z$ |
| UAV transmit power | $p_n[z]$ | Continuous, $0\le p_n[z]\le p_{\max}$ | Power used to offload sensing data to the HAP |
| UAV and HAP trajectories | $\mathbf q_n[z],\mathbf q_0[z]$ | Continuous 3-D positions | Slotwise flight paths of UAV $n$ and the HAP |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | UAV and HAP processing latency must not exceed $T_{\max}$, as imposed by (29b) and (29c) |
| C2 | Each UAV senses at most one user and each user is assigned to at most one UAV per slot, $\sum_k\alpha_{n,k}[z]\le1$ and $\sum_n\alpha_{n,k}[z]\le1$ |
| C3 | Transmit power is bounded by $0\le p_n[z]\le p_{\max}$ |
| C4 | Periodic endpoints and speed limits constrain $\mathbf q_n[z]$ and $\mathbf q_0[z]$ |
| C5 | UAV separation satisfies $\|\mathbf q_n[z]-\mathbf q_s[z]\|^2\ge d_{\min}^2$ |

**Algorithm**: Three-layer alternating optimization, relax and convexify sensing scheduling, update UAV transmit power, update UAV and HAP trajectories by SCA, and repeat until convergence to a local solution.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zhou and Liu [x] studied a multi-UAV integrated sensing, computing, and communication system in which UAVs sense ground users and offload sensing data to a HAP for MEC processing. They formulated a non-convex trade-off problem that maximizes radar sensing-data acquisition while penalizing total UAV and HAP energy consumption. Their three-layer iterative algorithm alternates sensing scheduling, UAV transmit-power allocation, and UAV-HAP trajectory optimization using relaxation and successive convex approximation. At 100 Mbits of sensing data, simulations report energy reductions of 28.7% and 20.3% relative to the ground-AP and initial-trajectory benchmarks. Under a 40 J energy constraint, the reported sensing gains are 34.7% and 24.6% over the same benchmarks.

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
