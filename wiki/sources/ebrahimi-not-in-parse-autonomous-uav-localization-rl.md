---
type: source
title: "Autonomous UAV Trajectory for Localizing Ground Objects: A Reinforcement Learning Approach"
authors: ["Dariush Ebrahimi", "Sanaa Sharafeddine", "Pin-Han Ho", "Chadi Assi"]
year: ""
url: ""
venue: ""
tags: [source, uav-localization, rssi, reinforcement-learning, q-learning, uav-trajectory-control, air-to-ground-channel-model]
related:
  - "[[rss-based-uav-localization]]"
  - "[[uav-trajectory-control]]"
  - "[[air-to-ground-channel-model]]"
  - "[[rotary-wing-propulsion-energy-model]]"
  - "[[uav-localization-under-jamming]]"
  - "[[autonomous-uav-swarms]]"
  - "[[zhu-2026-uav-localization-jamming]]"
  - "[[cao-2026-uav-self-tracking-ms-mm]]"
  - "[[zhu-2024-zdrl-uav-tracking]]"
created: 2026-07-11
updated: 2026-07-11
---

# Autonomous UAV Trajectory for Localizing Ground Objects: A Reinforcement Learning Approach

## Citation

Ebrahimi, D., Sharafeddine, S., Ho, P.-H., & Assi, C. *Autonomous UAV Trajectory for Localizing Ground Objects: A Reinforcement Learning Approach*. The local parse gives the title and author line but does not expose reliable publication year, venue, or DOI metadata; those fields are left blank rather than inferred.

## TL;DR

Uses Q-learning to let one UAV act as an autonomous aerial anchor for RSSI-based localization of multiple ground objects. The UAV first performs an initial scan to discover object count and rough positions, then chooses waypoints that reduce average localization error under energy, time, waypoint-count, or path-length budgets.

## Problem

In disaster response, search and rescue, and health monitoring, ground objects may not have GPS or infrastructure support. RSSI is cheap and simple but noisy, especially in urban shadowing. A UAV can collect RSSI from better vantage points, but pre-planned paths are weak when object locations and object count are unknown.

## System model

- A single UAV flies at fixed altitude over an urban search region and acts as a mobile aerial anchor.
- Ground objects periodically broadcast probe requests. The UAV hovers at selected waypoints, collects RSSI measurements, estimates distance from a path-loss model, and localizes objects by multilateration.
- The channel model includes LoS/NLoS behavior, elevation-angle effects, empirical path loss, and log-normal shadowing.
- The energy model includes flying and hovering costs, so trajectory quality is evaluated under energy, time, path-length, and waypoint limits.

## Method

The method has two phases. In the initial scan, the UAV covers the region with a minimum set of waypoints to discover the number of objects and obtain rough positions while bootstrapping Q-values. In the RL phase, the UAV treats the current waypoint cell as the state, neighboring cells as actions, and average localization-error reduction as reward, then follows a learned Q-learning policy to choose the next waypoints.

## Key findings

- Simulations use a `900 x 700 m^2` region, default altitude `100 m`, communication range `200 m`, hovering time `5 s`, velocity `40 km/h`, UAV mass `5 kg`, and urban LoS/shadowing parameters from prior work.
- With enough energy to visit all 120 waypoints, methods converge around `11 m` average error for 20 nodes and `9.4 m` for 30 nodes; under constrained energy/path/time/waypoints, the RL trajectory performs best.
- Path-length tests from 1 to 7 km report best-case improvements up to 47.8%, 62.7%, 63%, and 62.9% over Random, SCAN, LMAT, and MAZE for the 20-node case.
- More communication range and more waypoints reduce localization error; at `D = 200 m`, parsed values are `48.6 m` and `26.5 m` error after 20 and 40 waypoints.
- Increasing altitude does not monotonically improve localization because it raises LoS probability while reducing the ground coverage footprint.

## Limitations / future work

The parse contains IEEE watermark interruptions, corrupted punctuation, and figure-linked values that are partly displaced. The study is simulation-based. Future work proposes adaptive UAV altitude based on LoS probability and communication range, and multiple collaborative UAVs for ground-object localization.

## Relation to the corpus

This is an adjacent UAV-sensing foundation rather than an MEC offloading paper. It anchors [[rss-based-uav-localization]] beside later sensing-control pages such as [[zhu-2026-uav-localization-jamming]] and [[cao-2026-uav-self-tracking-ms-mm]]. It also connects [[uav-trajectory-control]] to [[air-to-ground-channel-model]] because waypoint selection is valuable only through the RSSI/path-loss geometry it creates.

## Raw artifacts

- `raw/sources/Autonomous_UAV_Trajectory_for_Localizing_Ground_Objects_A_Reinforcement_Learning_Approach/Autonomous_UAV_Trajectory_for_Localizing_Ground_Objects_A_Reinforcement_Learning_Approach.md`
- Original PDF and extracted figures (`images/`) in the same folder.
