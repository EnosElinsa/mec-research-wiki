---
type: source
title: "3D Trajectory Optimization in Rician Fading for UAV-Enabled Data Harvesting"
authors: ["Changsheng You", "Rui Zhang"]
year: 2019
url: "https://doi.org/10.1109/TWC.2019.2911939"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, uav-data-collection, wireless-sensor-network, trajectory-optimization, rician-fading, outage-probability, block-coordinate-descent, successive-convex-approximation]
related:
  - "[[uav-data-collection]]"
  - "[[angle-dependent-rician-fading]]"
  - "[[air-to-ground-channel-model]]"
  - "[[uav-trajectory-control]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[zeng-2017-energy-efficient-uav-trajectory]]"
  - "[[zhan-2011-uav-relay-heading-optimization]]"
  - "[[xu-2018-uav-wpt-trajectory]]"
created: 2026-07-07
updated: 2026-07-07
---

# 3D Trajectory Optimization in Rician Fading for UAV-Enabled Data Harvesting

## Citation

You, C., & Zhang, R. (2019). *3D Trajectory Optimization in Rician Fading for UAV-Enabled Data Harvesting*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2019.2911939.

## TL;DR

Optimizes a UAV's 3-D trajectory and sensor scheduling for wireless-sensor-network data harvesting under angle-dependent Rician fading. Instead of assuming deterministic LoS channels, the paper models a Rician factor tied to the UAV-sensor elevation angle, approximates the outage-aware effective fading power with a logistic regression model, then solves the resulting max-min data-rate problem with block coordinate descent and SCA.

## Problem

UAV data-collection papers often optimize 2-D routes at a fixed altitude and assume simplified LoS links. That can be inaccurate in urban/suburban settings where small-scale fading remains relevant. This paper asks how a data-collection UAV should jointly choose horizontal motion, altitude, and sensor scheduling when the achievable rate must satisfy a per-sensor outage probability constraint.

## System model

- A UAV collects sensing data from multiple ground sensor nodes.
- Each sensor transmits only when scheduled/woken by the UAV.
- The objective maximizes the minimum average data-collection rate across sensors.
- The UAV-SN channel uses Rician fading whose factor grows with the elevation angle; the reliability constraint is expressed through a maximum tolerable outage probability.

## Method

- The effective fading power needed for outage-aware rate calculation has no convenient closed form, so the paper fits a logistic S-shaped function to numerical data.
- The approximate optimization is decomposed into communication scheduling, horizontal trajectory, and vertical trajectory blocks.
- The horizontal and vertical trajectory subproblems are handled by successive convex approximation inside a block-coordinate-descent loop.

## Key findings

- Under moderate mission duration, the Rician-fading-based design can attain about two times the max-min rate of the LoS-based benchmark at T = 26 s.
- With stringent outage probability, the proposed Rician-fading-based design improves achieved max-min rate over the LoS-based benchmark by about 1.5 times when epsilon = 0.01.
- The optimized altitude balances two effects: higher elevation angle increases effective fading power, while larger distance increases path loss.
- The conclusion names multi-UAV extension with joint 3-D trajectories, scheduling, resource allocation, and 3-D collision avoidance as a natural next step.

## Relation to the corpus

This is a foundational UAV-data-harvesting/channel-model source rather than an MEC offloading paper. It extends [[uav-data-collection]] and [[air-to-ground-channel-model]] with [[angle-dependent-rician-fading]], a channel model that sits between deterministic LoS simplifications and geometry/statistical LoS-probability models. Its BCD/SCA solution connects to [[alternating-optimization-sdr-sca]] and complements the fixed-/rotary-wing trajectory-energy foundations in [[zeng-2017-energy-efficient-uav-trajectory]] and [[xu-2018-uav-wpt-trajectory]].

## Raw artifacts

- `raw/sources/3D_Trajectory_Optimization_in_Rician_Fading_for_UAV-Enabled_Data_Harvesting/3D_Trajectory_Optimization_in_Rician_Fading_for_UAV-Enabled_Data_Harvesting.md`
- Original PDF and extracted figures (`images/`) in the same folder.
