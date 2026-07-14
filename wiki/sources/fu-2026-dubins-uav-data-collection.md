---
type: source
title: "Dubins Path Planning of Heterogeneous UAV Collaborative Data Collection for IoT Network"
authors: ["Jinyu Fu", "Guanghui Sun", "Weiran Yao", "Chengwei Wu", "Ligang Wu"]
year: 2026
url: "https://doi.org/10.1109/TITS.2025.3645094"
venue: "IEEE Transactions on Intelligent Transportation Systems (IEEE T-ITS)"
tags: [source, uav-data-collection, dubins-path, heterogeneous-uav, obstacle-avoidance, ant-colony-optimization, rendezvous]
related:
  - "[[releasing-collecting-recycling-uav-framework]]"
  - "[[uav-data-collection]]"
  - "[[uav-trajectory-control]]"
  - "[[heterogeneous-uav-fleet]]"
  - "[[ant-colony-optimization]]"
  - "[[constraint-regimes-in-uav-data-collection]]"
created: 2026-07-13
updated: 2026-07-14
---

# Dubins Path Planning of Heterogeneous UAV Collaborative Data Collection for IoT Network

## Citation

Fu, J., Sun, G., Yao, W., Wu, C., & Wu, L. (2026). *Dubins Path Planning of Heterogeneous UAV Collaborative Data Collection for IoT Network*. **IEEE Transactions on Intelligent Transportation Systems**, 27(2), 2214-2224. DOI: 10.1109/TITS.2025.3645094.

## TL;DR

Builds an offline release-collect-recover mission for one fast transport UAV carrying several slower communication UAVs. Hierarchical altitude clustering, obstacle-aware bundled ant-colony tours, and time-synchronized Dubins recovery jointly choose the subordinate fleet size and mission trajectories.

## Problem

Collecting data from ground terminals in mountainous or obstacle-filled space couples communication throughput, obstacle avoidance, minimum turning radius, heterogeneous aircraft speeds, and synchronized recovery. A carrier can shorten deployment travel, but releasing too few or too many communication UAVs increases waiting and total mission time.

## System model

- One transport UAV (T-UAV) carries `K` communication UAVs (C-UAVs) from a base, releases them to collect terminal data, recovers them, and returns.
- A global controller knows terminal coordinates and terrain maps and plans all routes before dispatch. C-UAVs and communication tasks are homogeneous even though the carrier/subordinate roles are heterogeneous.
- UAVs follow Dubins motion with minimum turning radii. C-UAVs cannot hover, terminals transmit sequentially within a maximum effective distance, and one retry is allowed after a sudden communication failure.
- Recovery occurs when horizontal positions align and altitude differs by less than 1 m; recovery-operation time is ignored.

## Method

The [[releasing-collecting-recycling-uav-framework]] has three stages. Multi-height hierarchical target clustering assigns terminals and flight planes to C-UAVs. During collection, a bundling ant colony system groups adjacent unobstructed terminals and uses dynamic adaptive-window probabilistic roadmaps for obstacle-avoidance distances, producing open collection chains rather than closed TSP rings.

Recovery orders requests, uses T-UAV time as the synchronization axis, and lengthens the carrier trajectory through homotopy or curve-straight adjustments when the T-UAV would otherwise arrive too early. The complete procedure compares candidate values of `K` and fixes all trajectories before launch.

## Key findings

- The simulation uses T-UAV/C-UAV turning radii of `0.5 km`/`0.15 km`, horizontal speeds of `30 m/s`/`15 m/s`, and C-UAV vertical speed `10 m/s`.
- In the five-cluster example, cluster sizes are 14, 7, 11, 14, and 11, with assigned altitudes from 3,775 m to 4,116 m; the T-UAV begins at 4,500 m.
- The five reported data-collection routes measure `77.19`, `53.14`, `88.32`, `95.84`, and `68.79 km`.
- Across 30 Monte Carlo experiments comparing `K=3,4,5,6`, the method selects `K=5`. Waiting time is `6,939.5 s`, which is `9,213.3 s` less than `K=4` and `2,063.0 s` less than `K=6`.
- Staying time accounts for `72.63%`, `64.46%`, `37.65%`, and `67.44%` of total task time for `K=3,4,5,6`, showing the reported non-monotonic fleet-size tradeoff.

## Limitations / parse caveats

Evidence is simulation-only. The design assumes globally known terminals and terrain, centralized offline planning, no UAV damage, homogeneous C-UAVs and tasks, no C-UAV hovering, and zero recovery-operation time. The abstract's claim that the framework is optimal for Pareto solutions is supported by numerical experiments rather than a general optimality proof. OCR damage affects the terminal count, several equations, and figure labels, so those values are excluded. The parse supplies the DOI but not final year/venue/pages; the 2026 T-ITS record was verified through the exact-title Crossref entry.

## Relation to the corpus

This source adds carrier-subordinate synchronization to [[uav-data-collection]] and [[heterogeneous-uav-fleet]] planning. It differs from [[li-2023-energy-constrained-uav-data-collection]], which plans depot-returning tours under a single-UAV energy budget, and from [[liu-2026-usp-nfrp-emergency-communication]], where fixed-wing UAVs cycle through persistent communication and charging roles rather than being released and recovered in flight.

## Raw artifacts

- Parse: `raw/sources/Dubins_Path_Planning_of_Heterogeneous_UAV_Collaborative_Data_Collection_for_IoT_Network/Dubins_Path_Planning_of_Heterogeneous_UAV_Collaborative_Data_Collection_for_IoT_Network.md`
- Origin PDF: `raw/sources/Dubins_Path_Planning_of_Heterogeneous_UAV_Collaborative_Data_Collection_for_IoT_Network/Dubins_Path_Planning_of_Heterogeneous_UAV_Collaborative_Data_Collection_for_IoT_Network.pdf`
- Figures: `raw/sources/Dubins_Path_Planning_of_Heterogeneous_UAV_Collaborative_Data_Collection_for_IoT_Network/images/`
