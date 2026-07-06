---
type: source
title: "Joint UAVs Deployment and Resource Allocation for AoI-Aware RIS-Assisted UAV-USV MEC Network"
authors: ["Yangzhe Liao", "Yuanyan Song", "Dan Song"]
year: 2026
url: "https://doi.org/10.1109/TMC.2025.3611808"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), vol. 25, no. 3, Mar. 2026"
tags: [source, maritime-mec, uav-usv-cooperative-mec, age-of-information, intelligent-reflecting-surface, lyapunov-optimization, whale-optimization-algorithm]
related:
  - "[[maritime-mec]]"
  - "[[uav-usv-cooperative-mec]]"
  - "[[age-of-information]]"
  - "[[aoi-energy-tradeoff]]"
  - "[[uav-mounted-ris]]"
  - "[[intelligent-reflecting-surface]]"
  - "[[lyapunov-optimization]]"
  - "[[whale-optimization-algorithm]]"
  - "[[liao-2025-ris-uav-usv-resource-allocation]]"
created: 2026-07-07
updated: 2026-07-07
---

# Joint UAVs Deployment and Resource Allocation for AoI-Aware RIS-Assisted UAV-USV MEC Network

## Citation

Liao, Y., Song, Y., & Song, D. (2026). *Joint UAVs Deployment and Resource Allocation for AoI-Aware RIS-Assisted UAV-USV MEC Network*. **IEEE Transactions on Mobile Computing**, 25(3), 3103-3118. DOI: 10.1109/TMC.2025.3611808.

## TL;DR

Builds an AoI-aware RIS-assisted UAV-USV MEC architecture for inland waterways. A tethered UAV carries the RIS, while rotary-wing UAVs serve USVs that generate bidirectional data-computation tasks. The optimization minimizes a weighted sum of USV average AoI and RUAV flight energy by jointly choosing RUAV service durations, TUAV/RIS altitude, RIS phase shifts, and RUAV trajectories under a mixed linear-quadratic Lyapunov framework.

## Problem

USV data in inland waterways is freshness-sensitive: stale sensing or task-result information weakens monitoring and control even if raw latency looks acceptable. At the same time, rotary-wing UAVs have limited flight energy, and ship/shore blockage makes direct links unreliable. The paper therefore couples AoI, UAV propulsion energy, RIS-aided link quality, and task service scheduling in one long-term stochastic control problem.

## System model

- The network includes USVs, rotary-wing UAVs, and one RIS-carried tethered UAV.
- USVs require bidirectional data computation, and their average AoI is constrained.
- RUAV service-duration indicators decide which USVs are served in each slot.
- TUAV hovering altitude and RIS phase shifts shape the assisted wireless channel.
- RUAV trajectories determine flight energy and link geometry.

## Method

The paper first turns the long-term stochastic problem into deterministic single-slot subproblems with a mixed linear quadratic Lyapunov framework. The single-slot problem is then split into:

- RUAV trajectory optimization via an enhanced whale optimization algorithm.
- Service duration, RIS phase shift, and TUAV hovering-altitude optimization via an enhanced alternating optimization algorithm.

## Key findings

- The abstract reports about 50% long-term RUAV flight-energy reduction while maintaining satisfactory USV average AoI.
- In the reported comparison, the proposed design gives about 3.3e5 J RUAV flight energy and 9.6 s average AoI, compared with 3.8e5 J / 10.5 s for DE, 4.3e5 J / 11.8 s for GD, and 6.6e5 J / 19.6 s for random placement.
- With 1, 3, and 5 RUAVs, the proposed energy values are reported as about 7.8e4 J, 3.2e5 J, and 4.8e5 J.
- Increasing RIS elements improves freshness in the reported setup: the parse reports average AoI near 7.4 s with 30 elements and near 4.2 s with 50 elements.

## Limitations / future work

The paper identifies digital-twin-supported physical/virtual task dynamics, deep-learning or multi-agent-DRL online UAV/RIS design, and RIS-assisted ship-to-shore protocol/performance analysis as future work. The evaluation is simulation-based.

## Relation to the corpus

This page is the freshness-oriented companion to [[liao-2025-ris-uav-usv-resource-allocation]]. Both use RIS-assisted UAV-USV MEC for inland waterways, but this source makes [[age-of-information]] and RUAV flight energy the central tradeoff. It adds [[lyapunov-optimization]] and [[whale-optimization-algorithm]] to the maritime RIS branch, and links [[uav-mounted-ris]] with [[uav-usv-cooperative-mec]].

## Raw artifacts

- `raw/sources/Joint UAVs Deployment and Resource Allocation for AoI-Aware RIS-Assisted UAV-USV MEC Network/Joint UAVs Deployment and Resource Allocation for AoI-Aware RIS-Assisted UAV-USV MEC Network.md`
- Original PDF and extracted figures (`images/`) in the same folder.
