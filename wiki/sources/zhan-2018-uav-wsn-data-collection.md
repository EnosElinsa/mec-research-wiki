---
type: source
modeling_card: required
title: "Energy-Efficient Data Collection in UAV Enabled Wireless Sensor Network"
authors: ["Cheng Zhan", "Yong Zeng", "Rui Zhang"]
year: 2018
url: "https://doi.org/10.1109/LWC.2017.2776922"
venue: "IEEE Wireless Communications Letters (IEEE WCL)"
tags: [source, uav-data-collection, wireless-sensor-network, trajectory-optimization, energy-minimization, successive-convex-approximation]
related:
  - "[[cheng-zhan]]"
  - "[[uav-data-collection]]"
  - "[[uav-trajectory-control]]"
  - "[[yong-zeng]]"
  - "[[mozaffari-2017-uav-iot-energy-efficient]]"
  - "[[zeng-2019-uav-comm-tutorial-5g]]"
created: 2026-06-04
updated: 2026-07-16
---

# Energy-Efficient Data Collection in UAV Enabled Wireless Sensor Network

## Citation

Zhan, C., Zeng, Y., & Zhang, R. (2018). *Energy-Efficient Data Collection in UAV Enabled Wireless Sensor Network*. **IEEE Wireless Communications Letters**, 7(3). DOI: 10.1109/LWC.2017.2776922. (Received 13 September 2017; accepted 18 November 2017; published 23 November 2017; current version 19 June 2018.)

## TL;DR

Considers a UAV dispatched to collect sensed data from K sensor nodes (SNs) in a WSN under general fading channels. Jointly optimizes the SNs' **wake-up schedule** and the **UAV's trajectory** to minimize the **maximum energy consumption** across all SNs (max-min fairness), subject to reliable data collection constraints (outage probability ≤ ε per SN). The resulting MINLP is solved iteratively via block coordinate descent + **successive convex approximation (SCA)**. A sub-optimal solution achieves significant energy savings over static collector or straight-trajectory benchmarks.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: One fixed-altitude UAV collects required data from $K$ fixed battery-limited sensor nodes over quasi-static general fading. At most one sensor wakes and transmits in a slot, and outage probability depends on the UAV-sensor distance.

**Problem & objective**: P1 is a MINLP that minimizes maximum sensor energy, $\min \theta=\min\max_k E_k$, over binary wake-up scheduling and UAV trajectory.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Wake-up schedule | $x_k[m]$ | binary/relaxed $[0,1]$ | Whether sensor $k$ transmits in slot $m$ |
| UAV trajectory | $\mathbf q[m]$ | continuous 2-D position | Data-collector path |
| Maximum sensor energy | $\theta$ | continuous, nonnegative | Fairness epigraph variable |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | At most one sensor is active per slot, $\sum_kx_k[m]\le1$ |
| C2 | Every sensor uploads at least its required $S_k$ bits |
| C3 | Per-link outage probability does not exceed $\epsilon$ |
| C4 | Each sensor energy satisfies $E_k\le\theta$ |
| C5 | UAV speed, initial position, and final position remain feasible |

**Algorithm**: Relax binary wake-up indicators to fractional fading-block shares → fix trajectory and solve the schedule by linear programming → fix the schedule and convexify distance-rate terms → update trajectory by SCA → alternate the BCD blocks until maximum sensor energy converges.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zhan et al. [x] studied energy-efficient data collection in a UAV-enabled wireless sensor network under general fading. They formulated a mixed-integer problem that minimizes the maximum sensor energy over wake-up scheduling and UAV trajectory under one-active-sensor, required-data, outage, energy, and mobility constraints. Binary scheduling is relaxed to fractional use over sufficiently many fading blocks. For a fixed path the schedule is solved by linear programming, while successive convex approximation updates the path for a fixed schedule. Simulations report lower sensor energy than the evaluated static-collector and straight-trajectory baselines.

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

Sub-optimal (SCA iterative, not globally optimal). Single-UAV, fixed-altitude model; the authors identify a multi-UAV extension with UAV-sensor association and co-channel interference as future work. General fading is handled via outage-probability constraint rather than adaptive rate coding. Battery lifetime of the UAV itself is not jointly optimized.

## Relation to the corpus

From the Zeng/Zhang group (NUS), including [[yong-zeng]] — the same authors behind the UAV-communications tutorial [[zeng-2019-uav-comm-tutorial-5g]]. Focuses on the **data-collection** variant of UAV-enabled WSN rather than MEC offloading, making it a close complement to [[mozaffari-2017-uav-iot-energy-efficient]]. Establishes the max-energy-fairness (min-max) objective for UAV-WSN that recurs in later corpus works, and grounds [[uav-data-collection]] as a primary UAV use case distinct from MEC compute offloading.

## Raw artifacts

- `raw/sources/Energy-Efficient_Data_Collection_in_UAV_Enabled_Wireless_Sensor_Network/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
