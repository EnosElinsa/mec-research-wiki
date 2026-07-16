---
type: source
title: "DDRL: A Dual-Phase Deep Reinforcement Learning Approach for UAV-Assisted Content Delivery Across Multiple Base Stations"
authors: ["Xinshuai Hua", "Long Chen", "Xia Zhu", "Xiaoping Li", "Jingjing Li"]
year: 2026
url: "https://doi.org/10.1109/TWC.2026.3677068"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
modeling_card: required
tags: [source, uav, content-caching, multi-bs, trajectory-control, ppo, particle-swarm-optimization]
related:
  - "[[uav-content-caching]]"
  - "[[ppo]]"
  - "[[particle-swarm-optimization]]"
  - "[[uav-trajectory-control]]"
  - "[[wireless-backhaul]]"
  - "[[rotary-wing-propulsion-energy-model]]"
created: 2026-07-12
updated: 2026-07-16
---

# DDRL: A Dual-Phase Deep Reinforcement Learning Approach for UAV-Assisted Content Delivery Across Multiple Base Stations

## Citation

Hua, X., Chen, L., Zhu, X., Li, X., & Li, J. (2026). *DDRL: A Dual-Phase Deep Reinforcement Learning Approach for UAV-Assisted Content Delivery Across Multiple Base Stations*. **IEEE Transactions on Wireless Communications**, 25, 14367-14381. DOI: 10.1109/TWC.2026.3677068.

## TL;DR

Coordinates cache-enabled UAV motion, content replacement, and transmission behavior across three base stations. Online CNN-GRU PPO decisions control UAV movement and power, offline PPO updates retrain the policy, and PSO tunes a cache score over popularity, size ratio, and request frequency.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Cache-enabled fixed-altitude UAVs deliver content to stationary users across a three-base-station service area, with the base stations also supplying content and charging. A cache miss adds a BS-to-UAV wireless-backhaul transfer before downlink delivery. OFDMA removes inter-user interference, and UAV-ground propagation follows a probabilistic LoS/NLoS channel model.

**Problem & objective**: Equation (15) defines a nonconvex joint design that minimizes total content-acquisition delay, $\min \sum_g D_{i,g}$, over UAV trajectory, cache replacement, and transmission power. Cache-hit rate and energy efficiency are incorporated into the learning reward under cache, motion, and battery limits.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV movement | $d_u[n],\phi_u[n]$ | continuous, bounded | Travel distance and direction in slot $n$ |
| Transmit power | $p_u[n]$ | continuous, bounded | UAV content-delivery power |
| Cache placement | $\beta_{u,q}$ | binary | Whether UAV $u$ stores content $q$ |
| Cache-score weights | $w_1,w_2,w_3$ | continuous, normalized | PSO-tuned weights for popularity, size ratio, and request frequency |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | UAV movement remains inside the service area and respects per-slot mobility limits |
| C2 | UAV separation and collision-avoidance conditions hold |
| C3 | Residual battery energy supports movement and content delivery, including return to a base station |
| C4 | Cached content sizes satisfy the UAV capacity limit, $\sum_q \beta_{u,q}S_q\leq C$ |
| C5 | Transmission power remains within the permitted action range |

**Algorithm**: Encode spatial and temporal state with a CNN-GRU actor-critic, use clipped PPO for offline policy and value updates, deploy the trained policy for online movement and power decisions, and run PSO to tune the cache-replacement score used by the environment.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Hua et al. [x] studied cache-enabled UAV-assisted content delivery across multiple base stations under limited battery and storage capacity. They formulated the joint optimization of UAV trajectory, cache replacement, and transmission power to minimize total content-acquisition delay. Their DDRL framework combines online decision making with offline clipped-PPO training and uses a CNN-GRU model to capture spatial and temporal information in user requests, UAV energy, and mobility. A particle swarm optimization procedure tunes a cache-replacement score based on content popularity, size ratio, and request frequency. Simulations report up to an 8 percent latency reduction and a 5 percent cache-hit-rate improvement relative to the best evaluated baseline.

## Problem

UAVs can relieve congested base stations by carrying popular content closer to users, but limited flight energy and cache capacity couple where a UAV moves, what it stores, and when a cache miss must traverse the BS-UAV backhaul. Dynamic, geographically distributed requests make a fixed route or static popularity cache insufficient.

## System model

- Three base stations supply content and charging to multiple fixed-altitude UAVs serving stationary ground users in a `1 km x 1 km` region.
- A cache hit is transmitted directly from UAV to user; a miss first retrieves the object from a base station over [[wireless-backhaul]]. Requests follow a Zipf distribution.
- Probabilistic LoS/NLoS air-ground links determine path loss, while OFDMA is assumed to remove interference among user transmissions.
- The formal optimization in Eq. (15) minimizes total content-acquisition delay. Cache-hit and served-users-per-energy terms enter the learning reward rather than a second constrained objective.
- UAV motion, collision separation, residual energy, and cache capacity constrain the policy. The parse is inconsistent about transmit power: power is part of the learned action, while the communication setup also states fixed `20 dBm` power.

## Method

The Dual-Phase Deep Reinforcement Learning framework uses a CNN-GRU actor-critic with clipped [[ppo|PPO]]. During online decision-making, spatial and temporal features from users, requests, UAVs, batteries, and base stations produce each UAV's movement distance, direction, and power action; transitions enter an experience buffer. Offline training computes TD errors and generalized advantage estimates, applies clipped policy and value updates, and redistributes the parameters. Separately, [[particle-swarm-optimization|PSO]] selects three normalized weights for a replacement score combining content popularity, size ratio, and request frequency; cache-hit rate is the particle fitness.

## Key findings

- The abstract reports up to `8%` lower latency and `5%` higher cache-hit rate than the best tested baseline. These percentages are not reproduced in a machine-readable result table and are kept as abstract-attributed claims.
- The convergence discussion says DDRL typically stabilizes after about 1,500 of 2,500 training episodes and then maintains a lower energy-consumption ratio than CPPO and DCPPO.
- Cache comparisons cover DDRS, popularity, LRU, and random replacement. As users increase from 16 to 128, the proposed policy remains the highest-ranked curve; exact proposed cache-hit values are figure-only.
- Capacity (`40-100 Mbits`) and bandwidth (`8-14 MHz`) sweeps reduce acquisition delay in the plotted comparisons, but the parse does not transcribe exact delay ordinates.

## Limitations / parse caveats

Evaluation is simulation-only with stationary users, fixed UAV altitude, Zipf requests, orthogonal user transmissions, and a controlled communication model. The conclusion identifies dynamic mobility, environmental interference, and large scenario-specific datasets as future work. The power-action/fixed-power inconsistency and a mismatched Fig. 10 caption are unresolved. Publication metadata is absent from the parse and was verified through the exact-title Crossref record; technical claims come only from the parse.

## Relation to the corpus

[[uav-content-caching]] distinguishes content placement and replacement from service or computation caching. This source adds a multi-BS, energy-aware control loop in which [[uav-trajectory-control]] changes both access delay and the cost of fetching uncached content. Its PSO component tunes cache policy parameters rather than planning the flight path, unlike trajectory-oriented uses of PSO elsewhere in the corpus.

## Raw artifacts

- Parse: `raw/sources/DDRL_A_Dual-Phase_Deep_Reinforcement_Learning_Approach_for_UAV-Assisted_Content_Delivery_Across_Multiple_Base_Stations/DDRL_A_Dual-Phase_Deep_Reinforcement_Learning_Approach_for_UAV-Assisted_Content_Delivery_Across_Multiple_Base_Stations.md`
- Origin PDF: `raw/sources/DDRL_A_Dual-Phase_Deep_Reinforcement_Learning_Approach_for_UAV-Assisted_Content_Delivery_Across_Multiple_Base_Stations/DDRL_A_Dual-Phase_Deep_Reinforcement_Learning_Approach_for_UAV-Assisted_Content_Delivery_Across_Multiple_Base_Stations.pdf`
- Figures: `raw/sources/DDRL_A_Dual-Phase_Deep_Reinforcement_Learning_Approach_for_UAV-Assisted_Content_Delivery_Across_Multiple_Base_Stations/images/`
