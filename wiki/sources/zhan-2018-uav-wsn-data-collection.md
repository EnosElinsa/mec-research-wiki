---
type: source
title: "Energy-Efficient Data Collection in UAV Enabled Wireless Sensor Network"
authors: ["Cheng Zhan", "Yong Zeng", "Rui Zhang"]
year: 2018
url: "https://doi.org/10.1109/LWC.2017.2776922"
venue: "IEEE Wireless Communications Letters (IEEE WCL)"
tags: [source, uav-data-collection, wireless-sensor-network, trajectory-optimization, energy-minimization, successive-convex-approximation]
related:
  - "[[uav-data-collection]]"
  - "[[uav-trajectory-control]]"
  - "[[mozaffari-2017-uav-iot-energy-efficient]]"
  - "[[zeng-2019-uav-comm-tutorial-5g]]"
created: 2026-06-04
updated: 2026-06-04
---

# Energy-Efficient Data Collection in UAV Enabled Wireless Sensor Network

## Citation

Zhan, C., Zeng, Y., & Zhang, R. (2018). *Energy-Efficient Data Collection in UAV Enabled Wireless Sensor Network*. **IEEE Wireless Communications Letters**, 7(3). DOI: 10.1109/LWC.2017.2776922. (Received 13 September 2017; accepted 18 November 2017; published 23 November 2017; current version 19 June 2018.)

## TL;DR

Considers a UAV dispatched to collect sensed data from K sensor nodes (SNs) in a WSN under general fading channels. Jointly optimizes the SNs' **wake-up schedule** and the **UAV's trajectory** to minimize the **maximum energy consumption** across all SNs (max-min fairness), subject to reliable data collection constraints (outage probability ≤ ε per SN). The resulting MINLP is solved iteratively via block coordinate descent + **successive convex approximation (SCA)**. A sub-optimal solution achieves significant energy savings over static collector or straight-trajectory benchmarks.

## Problem framing

Sensor nodes have limited battery energy; once depleted they cannot be replaced. A UAV as mobile data collector can move close to each SN before waking it, drastically reducing uplink transmission energy. The key design challenges are: (i) the sleep/wake-up schedule must be binary (at most one SN awake per slot), and (ii) a general fading channel (not just LoS) between SN and UAV must be handled, allowing a per-slot outage probability constraint. Jointly optimizing trajectory and wake-up schedule was not previously studied under a general fading model.

## System model

- **K sensor nodes** at fixed locations; UAV dispatched for T seconds, flies at fixed altitude H with speed ≤ V_max.
- **Channel model:** quasi-static block fading; large-scale attenuation β_k[m] ∝ d_k[m]^{-α}; small-scale fading ρ_k[m,l] i.i.d. with unit mean power. Outage probability p_k^out[m] = F(SNR threshold × distance), non-decreasing in rate.
- **Wake-up schedule:** binary variable x_k[m] ∈ {0,1}; at most one SN awake per slot.
- **Objective (P1):** minimize θ = max_k SN energy consumption, subject to: total energy of each SN ≤ θ; reliable data collection (≥ S_k bits from each SN with outage ≤ ε); UAV speed + boundary constraints.

## Method

1. Binary constraints relaxed to [0,1]; converted to a fractional schedule over fading blocks with sufficiently large L.
2. **Block coordinate descent:** alternately solve wake-up schedule X (LP for fixed trajectory Q) and trajectory Q (non-convex, solved via SCA for fixed X).
3. Iterates until convergence to a sub-optimal solution.

## Key findings

- Proposed joint design achieves **significant energy savings** for sensor nodes compared to benchmarks with (a) a static data collector and (b) a straight-line UAV trajectory (parse Abstract, Section IV).
- The UAV moves close to each SN before waking it, reducing the SN's transmission energy substantially — the "mobile proximity" benefit of UAV data collection.
- The sub-optimal SCA-based solution converges reliably in simulations.

## Limitations / future work

Sub-optimal (SCA iterative, not globally optimal). Single-UAV, fixed-altitude model. General fading is handled via outage-probability constraint rather than adaptive rate coding. Battery lifetime of the UAV itself is not jointly optimized.

## Relation to the corpus

From the Zeng/Zhang group (NUS) — the same authors behind the UAV-communications tutorial [[zeng-2019-uav-comm-tutorial-5g]]. Focuses on the **data-collection** variant of UAV-enabled WSN rather than MEC offloading, making it a close complement to [[mozaffari-2017-uav-iot-energy-efficient]]. Establishes the max-energy-fairness (min-max) objective for UAV-WSN that recurs in later corpus works, and grounds [[uav-data-collection]] as a primary UAV use case distinct from MEC compute offloading.

## Raw artifacts

- `raw/sources/Energy-Efficient_Data_Collection_in_UAV_Enabled_Wireless_Sensor_Network/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
