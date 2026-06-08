---
type: source
title: "Mobile Unmanned Aerial Vehicles (UAVs) for Energy-Efficient Internet of Things Communications"
authors: ["Mohammad Mozaffari", "Walid Saad", "Mehdi Bennis", "Mérouane Debbah"]
year: 2017
url: "https://doi.org/10.1109/TWC.2017.2751045"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, uav, internet-of-things, 3d-placement, uav-data-collection, energy-efficiency, air-to-ground-channel-model, uplink-power-control]
related:
  - "[[drone-cell-3d-placement]]"
  - "[[air-to-ground-channel-model]]"
  - "[[uav-data-collection]]"
  - "[[rotary-wing-propulsion-energy-model]]"
  - "[[al-hourani-2014-optimal-lap-altitude]]"
  - "[[bor-yaliniz-2016-3d-abs-placement]]"
  - "[[mozaffari-2019-uav-wireless-tutorial]]"
  - "[[weighted-kmeans-uav-deployment]]"
created: 2026-06-01
updated: 2026-06-08
---

# Mobile Unmanned Aerial Vehicles (UAVs) for Energy-Efficient Internet of Things Communications

## Citation

Mozaffari, M., Saad, W., Bennis, M., & Debbah, M. (2017). *Mobile Unmanned Aerial Vehicles (UAVs) for Energy-Efficient Internet of Things Communications*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2017.2751045. (Manuscript received 5 August 2016; date of publication 15 September 2017; date of current version 9 November 2017 → year 2017.)

## TL;DR

A framework for deploying and **moving multiple UAVs** as aerial base stations that collect uplink data from ground **IoT devices** with **minimum total device transmit power**. It jointly optimizes the UAVs' **3D placement**, **device-UAV association**, and **uplink power control**, then — because IoT devices activate at different times — derives **when the UAVs should update their positions** (the "update times") and the **energy-minimizing 3D trajectory** between those stops. Simulation results report the device total transmit power is reduced by **45%** versus stationary aerial base stations, with up to **28%** higher system reliability, and reveal a tradeoff: more frequent updates lower device transmit power at the cost of more UAV mobility energy.

## Problem framing

IoT devices (sensors, monitors) are battery-limited and cannot transmit far. UAVs can move toward them to shorten links and establish line-of-sight, enabling low-power uplink collection. Prior work treated single UAVs, fixed deployments, or static sensor sets; none jointly optimized deployment, mobility, association, and uplink power for **time-varying** IoT activation. This paper is positioned as one of the first comprehensive treatments of that joint problem.

## System model

- **Actors.** $L$ ground IoT devices and $K$ rotary-wing UAVs serving uplink over $R$ orthogonal FDMA channels; a central cloud server knows device/UAV locations and computes placement, association, and device transmit powers.
- **Channel.** Probabilistic **ground-to-air** LoS/NLoS model: LoS probability is a sigmoid in elevation angle with environment-dependent constants; average path loss combines LoS/NLoS terms — the same air-to-ground family as [[al-hourani-2014-optimal-lap-altitude]].
- **Activation models.** Two device-activation processes — a **Beta-distribution** bursty model (per 3GPP, for random activations like smart traffic) and a **deterministic periodic** model (e.g. smart meters every $\tau_i$ seconds).
- **Channel assignment.** Constrained K-means clustering assigns channels by proximity to mitigate co-channel interference.
- **Objective.** At each update time, minimize total active-device transmit power subject to per-device SINR targets and a max transmit-power cap; over the horizon, minimize UAV mobility energy while serving devices.

## Method

- **Step 1 — deployment + association + power.** Decompose the non-convex original problem into two subproblems solved **iteratively**: (a) given UAV locations, find the optimal device-UAV association and device transmit powers meeting SINR targets; (b) given association, transform the non-convex 3D-location problem to a convex form and solve for the UAV positions. Iterate until convergence (total transmit power decreases each step).
- **Step 2 — mobility.** Derive **closed-form expressions for the update times** at which UAVs must relocate as the active-device set changes, then compute the **optimal 3D UAV trajectory** minimizing total mobility energy across the update stops.

## Key findings

- The proposed approach reduces **total IoT-device transmit power by 45%** compared with stationary aerial base stations (abstract, parse).
- It yields up to **28% higher system reliability** than the stationary case (abstract, parse).
- There is an inherent tradeoff between the **number of update times**, **UAV mobility**, and **device transmit power**: more updates lower device transmit power but raise UAV energy consumption (the analytical update-time derivations are verified in simulation).

## Limitations / future work

The framework assumes a centralized cloud with known device/UAV locations, average-channel-gain SINR modeling, and rotary-wing UAVs. The parse does not enumerate an explicit future-work list → `not in parse`.

## Relation to the corpus

A **UAV-deployment + data-collection anchor** from the same Mozaffari/Saad/Bennis/Debbah group as the tutorial [[mozaffari-2019-uav-wireless-tutorial]], and a companion to the placement-oriented [[bor-yaliniz-2016-3d-abs-placement]] (both pose **3D UAV placement** over the urban [[air-to-ground-channel-model]], one for coverage-maximization, this one for **uplink-power-minimizing IoT collection**). Its proximity-based channel assignment relates to [[weighted-kmeans-uav-deployment]]. It is a *placement/mobility + data-collection* paper rather than a compute-offloading one, complementing [[uav-data-collection]] and the [[rotary-wing-propulsion-energy-model]] used for its mobility-energy objective.

## Raw artifacts

- Parse: `raw/sources/Mobile_Unmanned_Aerial_Vehicles_UAVs_for_Energy-Efficient_Internet_of_Things_Communications/full.md`
- Origin PDF: `raw/sources/Mobile_Unmanned_Aerial_Vehicles_UAVs_for_Energy-Efficient_Internet_of_Things_Communications/b905eb51-494c-4f5b-95c4-b1f8f6ac328f_origin.pdf`
- Figures: `raw/sources/Mobile_Unmanned_Aerial_Vehicles_UAVs_for_Energy-Efficient_Internet_of_Things_Communications/images/`
