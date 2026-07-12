---
type: source
title: "DDRL: A Dual-Phase Deep Reinforcement Learning Approach for UAV-Assisted Content Delivery Across Multiple Base Stations"
authors: ["Xinshuai Hua", "Long Chen", "Xia Zhu", "Xiaoping Li", "Jingjing Li"]
year: 2026
url: "https://doi.org/10.1109/TWC.2026.3677068"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, uav, content-caching, multi-bs, trajectory-control, ppo, particle-swarm-optimization]
related:
  - "[[uav-content-caching]]"
  - "[[ppo]]"
  - "[[particle-swarm-optimization]]"
  - "[[uav-trajectory-control]]"
  - "[[wireless-backhaul]]"
  - "[[rotary-wing-propulsion-energy-model]]"
created: 2026-07-12
updated: 2026-07-12
---

# DDRL: A Dual-Phase Deep Reinforcement Learning Approach for UAV-Assisted Content Delivery Across Multiple Base Stations

## Citation

Hua, X., Chen, L., Zhu, X., Li, X., & Li, J. (2026). *DDRL: A Dual-Phase Deep Reinforcement Learning Approach for UAV-Assisted Content Delivery Across Multiple Base Stations*. **IEEE Transactions on Wireless Communications**, 25, 14367-14381. DOI: 10.1109/TWC.2026.3677068.

## TL;DR

Coordinates cache-enabled UAV motion, content replacement, and transmission behavior across three base stations. Online CNN-GRU PPO decisions control UAV movement and power, offline PPO updates retrain the policy, and PSO tunes a cache score over popularity, size ratio, and request frequency.

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
