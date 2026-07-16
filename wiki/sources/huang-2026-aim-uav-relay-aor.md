---
type: source
title: "AIM: Angle-of-Radiation-Based Deployment of UAV Relays for Connectivity in 3D Environments"
authors: ["Kuang-Hui Huang", "Fang-Jing Wu", "Yu-Yu Chen", "Ai-Chun Pang"]
year: 2026
url: "https://doi.org/10.1109/TMC.2025.3630751"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
modeling_card: required
tags: [source, uav-communications, uav-relay, relay-deployment, antenna-radiation, angle-of-radiation, graph-search]
related:
  - "[[angle-of-radiation-uav-relay]]"
  - "[[uav-mobile-relaying]]"
  - "[[air-to-ground-channel-model]]"
  - "[[wireless-backhaul]]"
  - "[[zeng-2016-throughput-relaying]]"
  - "[[zhan-2011-uav-relay-heading-optimization]]"
created: 2026-07-10
updated: 2026-07-16
---

# AIM: Angle-of-Radiation-Based Deployment of UAV Relays for Connectivity in 3D Environments

## Citation

Huang, K.-H., Wu, F.-J., Chen, Y.-Y., & Pang, A.-C. (2026). *AIM: Angle-of-Radiation-Based Deployment of UAV Relays for Connectivity in 3D Environments*. **IEEE Transactions on Mobile Computing**, 25(4), 5434-5447. DOI: 10.1109/TMC.2025.3630751.

## TL;DR

Formulates UAV relay-chain deployment with non-isotropic antenna radiation as a joint position-and-heading problem. The AIM algorithm builds an angle-of-radiation-aware reachability table over feasible 3-D grid positions and headings, then reconstructs a minimum-relay chain from destination back to source while maintaining per-link RSS thresholds.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A three-dimensional operational area is discretized into obstacle-free grid positions, and every UAV can select one of several headings. Each position-heading pair is an operational state, and a directed link exists only when the transmitter and receiver antenna radiation angles yield received signal strength above a required threshold.

**Problem & objective**: Given fixed source and destination operational states, the deployment problem selects a relay chain $R=\arg\min_{\widetilde R}\lvert\widetilde R\rvert$, minimizing the number of operational states and therefore the number of UAVs in the chain.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Relay-chain sequence | $R$ | ordered subset of graph vertices | Source, selected relay states, and destination |
| Relay position | $q_i$ | discrete feasible grid point | Three-dimensional location of relay $i$ |
| Relay heading | $a_i$ | discrete element of $\mathcal H$ | Antenna orientation of relay $i$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Distinct relays cannot occupy the same grid position: $\widetilde q_i\ne\widetilde q_j$ |
| C2 | Every consecutive relay link meets the RSS threshold: $e(\widetilde v_i,\widetilde v_{i+1})\ge\gamma$ |
| C3 | The source-to-first-relay and last-relay-to-destination links also meet $\gamma$ |
| C4 | Every selected position is obstacle-free and every heading belongs to the allowed set $\mathcal H$ |

**Algorithm**: AIM sorts operational states by position, builds an angle-of-radiation-aware reachability table from the source, and records for every state the minimum relay count, predecessor, and bottleneck RSS. It then backtracks predecessors from the destination to recover the chain, breaking equal-hop ties in favor of stronger minimum RSS.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Huang et al. [x] modeled three-dimensional UAV relay deployment with non-isotropic antenna radiation, so each graph vertex jointly specifies a feasible position and heading. They minimized relay-chain length while requiring distinct relay positions and an RSS threshold on every source, relay, and destination link. AIM creates a source-rooted reachability table that records minimum hop count, predecessor, and bottleneck RSS, then reconstructs the chain by reverse lookup. Across 100 source-destination pairs, AIM used 52.1%, 61.2%, and 14.6% fewer UAVs than the two-stage, greedy, and MADRL baselines, respectively.

## Problem

Emergency or remote users may need on-demand connectivity through chained UAV relays, but ideal isotropic antenna assumptions hide a practical failure mode: the received signal strength depends on the transmitter and receiver headings, vertical angle, horizontal angle, and radiation pattern. The paper asks how to minimize the number of relay UAVs while guaranteeing end-to-end RSS when both positions and headings affect every UAV-to-UAV link.

## System model

- A 3-D operational region is discretized into feasible grid positions, excluding terrain or obstacle cells.
- Each UAV operational state is a pair of position and heading.
- Source and destination operational states are known.
- A link is feasible when the RSS computed from free-space path loss plus transmit/receive antenna gains is above the application threshold.
- The simulations use half-wavelength dipole radiation, 5 GHz carrier frequency, 20 dBm transmit power, 30 m grid size, 8 heading options, and application thresholds of -67 dBm for VoIP/video and -70 dBm for web browsing.

## Method

- Proves the AoR-based deployment decision problem is NP-hard by reduction from rainbow vertex-connected path.
- Constructs an AoR-based graph over candidate operational states.
- Sorts candidate states by distance from the source and updates each state's reachability, predecessor, and bottleneck RSS.
- Looks up predecessors from the destination back to the source to produce the relay chain.
- Compares against a two-stage position-then-heading method, a greedy farthest-link method, and a MADRL baseline modified to choose both positions and headings.

## Key findings

- In the 600 m by 600 m scenario, AIM reduces the number of used relays by 52.1% versus the two-stage baseline, 61.2% versus greedy, and 14.6% versus MADRL.
- AIM reaches 100% success rate for both VoIP/video and web-browsing RSS thresholds; the two-stage method reaches 40% and 35%, and MADRL reaches 77% and 96%.
- Among successful cases, AIM uses 2.68 relays on average for VoIP/video and 1.91 for web browsing, lower than the corresponding two-stage, greedy, and MADRL counts.
- Across 300 m, 600 m, and 900 m terrain sizes, AIM maintains 100% success rate and lower relay-count variation than the baselines.
- The configuration study finds that 30-40 m grid sizes and 4-8 heading options offer a practical runtime/performance tradeoff in the tested setup.

## Limitations / future work

The evaluation is simulation-based and uses known terrain, fixed source/destination states, and homogeneous antenna assumptions. The paper lists dynamic no-fly zones/obstacles, heterogeneous antenna patterns, and advanced beamforming or phased-array antennas as future directions.

## Relation to the corpus

This is an adjacent UAV-communications foundation rather than an MEC offloading paper. It extends [[uav-mobile-relaying]] from trajectory/power optimization toward deployment geometry under non-isotropic antennas. The new [[angle-of-radiation-uav-relay]] concept connects it to the corpus's channel and trajectory-control foundations, especially [[zhan-2011-uav-relay-heading-optimization]], where heading already appears as a controllable communication variable.

## Raw artifacts

- `raw/sources/AIM_Angle-of-Radiation-Based_Deployment_of_UAV_Relays_for_Connectivity_in_3D_Environments/AIM_Angle-of-Radiation-Based_Deployment_of_UAV_Relays_for_Connectivity_in_3D_Environments.md`
- `raw/sources/AIM_Angle-of-Radiation-Based_Deployment_of_UAV_Relays_for_Connectivity_in_3D_Environments/AIM_Angle-of-Radiation-Based_Deployment_of_UAV_Relays_for_Connectivity_in_3D_Environments.pdf`
- Extracted figures in `raw/sources/AIM_Angle-of-Radiation-Based_Deployment_of_UAV_Relays_for_Connectivity_in_3D_Environments/images/`
