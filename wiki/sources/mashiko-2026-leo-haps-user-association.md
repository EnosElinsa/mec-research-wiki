---
type: source
title: "Spectral-Efficient Dynamic User Association in LEO Satellite Constellation-HAPS Cooperative Networks"
authors: ["Kazuma Mashiko", "Hiroaki Hashida", "Yuichi Kawamoto", "Nei Kato", "Kohei Yoshida", "Masayuki Ariyoshi"]
year: 2026
url: "https://doi.org/10.1109/TCCN.2025.3569603"
venue: "IEEE Transactions on Cognitive Communications and Networking, 12"
modeling_card: required
tags: [source, leo-satellite, high-altitude-platform-station, user-association, spectral-efficiency, time-expanded-graph, link-switching]
related:
  - "[[high-altitude-platform-station]]"
  - "[[non-terrestrial-network]]"
  - "[[device-association]]"
  - "[[free-space-optical-isl]]"
  - "[[nei-kato]]"
created: 2026-11-02
updated: 2026-11-02
---

# Spectral-Efficient Dynamic User Association in LEO Satellite Constellation-HAPS Cooperative Networks

## Citation

Mashiko, K., Hashida, H., Kawamoto, Y., Kato, N., Yoshida, K., & Ariyoshi, M. (2026). *Spectral-Efficient Dynamic User Association in LEO Satellite Constellation-HAPS Cooperative Networks*. **IEEE Transactions on Cognitive Communications and Networking, 12**. DOI: 10.1109/TCCN.2025.3569603.

## TL;DR

Ground cells can be served directly by LEO satellites or through HAPS connected to satellites by FSO links. The paper models the changing topology as a time-extended graph, chooses the instantaneous link set that maximizes spectral efficiency, and controls when to switch link sets so each set stays in use long enough.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A LEO constellation $V_s$, HAPS nodes $V_h$, and ground cells $V_g$ form a time-extended graph over times $T$. Links include satellite-HAPS FSO links $E_{sh}$, satellite-ground links $E_{sg}$, and HAPS-ground links $E_{hg}$, sharing total RF bandwidth $BW$. Satellites and HAPS have at most $B_s$ and $B_h$ beams.

**Problem & objective**: $\mathbb P_1$: $\max\sum_{t\in T}\sum_{(i_t,j_t)\in E}f_{SE}(i_t,j_t)$, the total spectral efficiency of the selected links.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Link state | $x(i_t,j_t)$ | binary | Link between nodes $i$ and $j$ is active at time $t$ |
| Switching time | link-set update instants | discrete times | When the active link set is replaced |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| (9) | Each satellite has at most one FSO link to a HAPS, $\sum_{E_{sh}}x\le1$. |
| (10) | Each ground cell gets exactly one downlink from a satellite or HAPS. |
| (11) | Satellite beam limit, $\sum_E x\le B_s$. |
| (12) | HAPS beam limit, $\sum_E x\le B_h$. |
| Switching | Link sets must persist at least the minimum control switching time. |

**Algorithm**: Narrow the candidate link sets with an exploration scheme over the time-extended graph to find the instantaneous optimum efficiently, then apply adaptive long-term switching control that keeps an updated optimal set in use for an extended period.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Mashiko et al. [x] studied non-terrestrial networks that combine low-earth orbit satellites and high-altitude platform stations to provide global, high-capacity 6G coverage with efficient spectrum use. Observing that integrating satellite-ground direct links with HAPS relay links introduces coordination challenges and that static HAPS coverage can be inefficient, they proposed a downlink user association method that leverages both LEO satellites and HAPS. The dynamic topology is represented by a time-extended graph, and an optimization problem determines the instantaneous link set that maximizes spectral efficiency under beam and link constraints. An adaptive long-term switching control then decides when to change link sets. Simulation results show that the method outperforms conventional distance-based and fixed-interval approaches, with an average improvement of 19.8% over fixed-period link switching in the application rate.

## Problem framing

Satellite visibility changes continuously, so the best set of satellite-ground and HAPS-ground links changes irregularly, while frequent switching is costly.

## System model

- Satellite-HAPS links use FSO with one-to-one transmitters and receivers.
- RF downlinks to ground cells share a common bandwidth.

## Method

The exploration scheme reduces candidate link sets by more than 99% when there are multiple ground cells.

## Key findings

- The method outperforms distance-based and fixed-interval association.
- Average improvement in application rate over fixed-period switching is 19.8%.

## Limitations / future work

The evaluation uses modeled constellations and cell layouts.

## Relation to the corpus

Adds dynamic [[device-association]] across LEO and [[high-altitude-platform-station]] tiers in a [[non-terrestrial-network]], with [[free-space-optical-isl]]-style satellite-HAPS links.

## Raw artifacts

- Parse: `raw/sources/Spectral-Efficient_Dynamic_User_Association_in_LEO_Satellite_Constellation-HAPS_Cooperative_Networks/Spectral-Efficient_Dynamic_User_Association_in_LEO_Satellite_Constellation-HAPS_Cooperative_Networks.md`
- Origin PDF and extracted figures are in the same folder.
