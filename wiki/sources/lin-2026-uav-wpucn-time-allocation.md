---
type: source
title: "UAV-Enabled Wireless-Powered Underground Communication Networks: A Novel Time Allocation Approach"
authors: ["Kaiqiang Lin", "Yijie Mao", "Onel Luis Alcaraz López", "Mohamed-Slim Alouini"]
year: 2026
url: "https://doi.org/10.1109/TGCN.2025.3644128"
venue: "IEEE Transactions on Green Communications and Networking (IEEE TGCN), vol. 10, pp. 1618-1632"
tags: [source, wireless-powered-underground-communication, wireless-energy-transfer, uav-data-collection, csi-free-wet, time-allocation, convex-optimization]
related:
  - "[[wireless-powered-underground-communication-network]]"
  - "[[csi-free-multiantenna-wireless-energy-transfer]]"
  - "[[wireless-power-transfer]]"
  - "[[rf-energy-harvesting]]"
  - "[[uav-data-collection]]"
  - "[[rotary-wing-propulsion-energy-model]]"
  - "[[uav-trajectory-control]]"
  - "[[xie-2021-uav-wpt-tutorial]]"
  - "[[xu-2018-uav-wpt-trajectory]]"
  - "[[you-2019-rician-uav-data-harvesting]]"
  - "[[zeng-2019-rotary-wing-energy-min]]"
  - "[[xie-2023-wireless-powered-short-packet-uav]]"
created: 2026-07-14
updated: 2026-07-14
---

# UAV-Enabled Wireless-Powered Underground Communication Networks: A Novel Time Allocation Approach

## Citation

Lin, K., Mao, Y., López, O. L. A., & Alouini, M.-S. (2026). *UAV-Enabled Wireless-Powered Underground Communication Networks: A Novel Time Allocation Approach*. **IEEE Transactions on Green Communications and Networking**, 10, 1618-1632. DOI: 10.1109/TGCN.2025.3644128.

## TL;DR

A terrestrial hybrid access point (HAP) and a rotary-wing UAV jointly power underground devices, after which the UAV collects their TDMA uploads and returns the data to the HAP. For fixed flight geometry, speed, altitude, and hover position, the paper reduces UAV-energy minimization to a convex allocation of WET and uplink durations. It also compares ideal full-CSI beamforming with several [[csi-free-multiantenna-wireless-energy-transfer|CSI-free multi-antenna WET]] schemes under RF-chain and servo-power costs.

## Problem

Large-scale [[wireless-powered-underground-communication-network|wireless-powered underground communication networks]] face severe soil attenuation, non-line-of-sight propagation, costly CSI acquisition, and long links to fixed above-ground power sources. Deploying a UAV above the monitored area shortens the air path, but the UAV must spend energy on flight, hovering, WET, data collection, and forwarding. The paper therefore minimizes modeled UAV energy while requiring every underground device to meet a data threshold and all collected data to reach the HAP.

## System model

- One terrestrial HAP and one rotary-wing UAV serve `N` single-antenna underground devices in a circular monitoring area. The HAP and UAV each carry a `Q`-element half-wavelength ULA.
- Operation has four phases: HAP-to-UAV wireless charging for `T_p1`; HAP/UAV energy transfer to underground devices for `T_p2`; TDMA device uploads over slots `tau_n`, totaling `T_p3`; and UAV-to-HAP data offloading for `T_p4`.
- The underground WET path combines air attenuation, air-to-soil refraction loss, and soil attenuation. The soil permittivity model depends on burial depth, volumetric water content, carrier frequency, and clay fraction.
- Harvesting uses a linear RF-to-DC model. Each device reserves a fraction of harvested energy for wireless information transmission and the remainder for circuit operation.
- Hybrid HAP-UAV WET uses independent, uncoordinated, zero-mean signals, so their average received powers add non-coherently rather than through coherent joint beamforming.
- The UAV energy model includes WET and forwarding transmit energy, hovering during service phases, and round-trip acceleration, cruise, and deceleration energy from a [[rotary-wing-propulsion-energy-model]].

## Method

The ideal full-CSI benchmark maximizes the minimum incident energy across devices through a semidefinite program over the transmit covariance matrix. The CSI-free alternatives are switching antennas, all-antennas independent signals, two all-antennas same-signal configurations, and rotary antenna beamforming; their usable transmit power accounts for different RF-chain and servo costs.

With the WET design and flight geometry fixed, complete forwarding determines `T_p4`. Because the remaining variable UAV energy is linear in `T_p2`, `T_p3`, and `T_p4`, the optimization reduces to minimizing `T_p2 + sum_n tau_n` subject to positive durations and per-device throughput thresholds. The paper rewrites each throughput constraint as a convex inequality, establishes a positive-semidefinite Hessian, and solves the resulting problem with CVX. It then derives the HAP charging duration `T_p1` needed to support the modeled UAV expenditure.

## Key findings

- In the baseline simulation with 64 devices, 0.4 m burial depth, 15% volumetric water content, a 5 m monitoring radius, 600 m flight distance, and 32 antennas at both transmitters, AASS-II is selected for HAP WET and rotary antenna beamforming for UAV WET under the modeled hardware budgets.
- Hybrid WET provides the highest average worst-device RF energy over the simulated 200-800 m HAP-to-area distance range. UAV-only energy delivery is nearly insensitive to that distance because the UAV hovers over the monitored area.
- Performance falls with device count, burial depth, and soil water content. In the reported simulation, increasing depth from 0.2 m to 1 m reduces average worst-device RF energy by about 30 dB; at volumetric water content 0.4 and depth 0.4 m, none of the compared approaches reaches the harvesting threshold.
- Table III reports the lowest modeled UAV energy for hybrid CSI-free WET: `56.45 kJ`, with `T_p1 = 79.23 s`, `T_p2 = 89.46 s`, `T_p3 = 683.93 s`, and `T_p4 = 126.87 s`. These are scenario-specific simulation results, not field measurements or general guarantees.

## Limitations / parse caveats

The solved problem fixes UAV distance, speed, altitude, route, and central hover point; it is a time-allocation result, not a [[uav-trajectory-control|trajectory-optimization]] result. The model also assumes a common burial depth, vertical soil propagation, quasi-static Rician WET, an ideal or slowly varying HAP-UAV charging link, unit uplink fading gains, linear harvesting, and no finite mission-duration or battery-capacity constraint inside the convex program. Full-CSI acquisition, feedback, and optimization costs are omitted, while switch and phase-shifter costs are neglected.

The feasibility statement depends on allowing `T_p2` or `T_p3` to grow without a mission deadline and on positive usable channel gains. The parse is internally inconsistent about a `12500` versus `125000 kbps` threshold, and its throughput expression behaves like a data amount although the threshold is labeled as a rate. The charging-time expression also warrants source-side verification because the displayed denominator adds charging-phase hover power where a net charging-rate derivation would normally subtract consumption. These ambiguities should not be used as normalized quantitative facts.

## Relation to the corpus

[[xie-2021-uav-wpt-tutorial]] supplies the broader UAV-WPT, WPCN, and trajectory-design framework cited by this paper. This source specializes that line to buried devices and soil-aware propagation, adds hybrid fixed-HAP/UAV energy delivery, and solves phase-duration allocation while holding mobility variables fixed. [[xu-2018-uav-wpt-trajectory]] instead optimizes fair aerial WPT through UAV movement, while [[xie-2023-wireless-powered-short-packet-uav]] studies a static UAV HAP serving above-ground devices with finite-blocklength uploads. The collection and propulsion components connect to [[you-2019-rician-uav-data-harvesting]] and [[zeng-2019-rotary-wing-energy-min]], respectively.

## Raw artifacts

- Parse: `raw/sources/UAV-Enabled_Wireless-Powered_Underground_Communication_Networks_A_Novel_Time_Allocation_Approach/UAV-Enabled_Wireless-Powered_Underground_Communication_Networks_A_Novel_Time_Allocation_Approach.md`
- Origin PDF: `raw/sources/UAV-Enabled_Wireless-Powered_Underground_Communication_Networks_A_Novel_Time_Allocation_Approach/UAV-Enabled_Wireless-Powered_Underground_Communication_Networks_A_Novel_Time_Allocation_Approach.pdf`
- Figures: `raw/sources/UAV-Enabled_Wireless-Powered_Underground_Communication_Networks_A_Novel_Time_Allocation_Approach/images/`
