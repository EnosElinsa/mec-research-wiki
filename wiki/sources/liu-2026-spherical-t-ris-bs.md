---
type: source
title: "Angle-Insensitive Spherical T-RIS-Enabled Base Station"
authors: ["Jianghui Liu", "Wenjun Xu", "Hongtao Zhang"]
year: 2026
url: "https://doi.org/10.1109/TWC.2026.3656594"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, ris, transmissive-ris, spherical-ris, low-altitude-communications, uav-data-collection, uav-trajectory-control, sca]
related:
  - "[[spherical-transmissive-ris]]"
  - "[[intelligent-reflecting-surface]]"
  - "[[low-altitude-intelligent-network]]"
  - "[[uav-data-collection]]"
  - "[[uav-trajectory-control]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[lin-2025-energy-effective-ris-multiuav-coverage]]"
  - "[[jeon-2026-ampli-flection-aerial-backhaul]]"
created: 2026-07-11
updated: 2026-07-16
modeling_card: required
---

# Angle-Insensitive Spherical T-RIS-Enabled Base Station

## Citation

Liu, J., Xu, W., & Zhang, H. (2026). *Angle-Insensitive Spherical T-RIS-Enabled Base Station*. **IEEE Transactions on Wireless Communications**, 25, 12295-12308. DOI: 10.1109/TWC.2026.3656594. The parse lacks a publication header; venue, year, pages, and DOI were verified from a title-matched Crossref record.

## TL;DR

Proposes a [[spherical-transmissive-ris|spherical transmissive RIS (ST-RIS) enabled base station]] for dynamic low-altitude communication. Instead of a conventional BS antenna array or planar transmissive RIS, the architecture combines one omnidirectional antenna with a spherical T-RIS to reduce angle-sensitive gain loss across 3-D directions. A low-altitude application then jointly optimizes RIS phase shifts, transmit power, user scheduling, and UAV 3-D trajectories to maximize collected sensor data while guaranteeing cellular-user uplink rates.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A spherical transmissive-RIS base station serves $K_2$ uplink cellular users while $M$ UAVs collect data from $K_1$ remote IoT sensors. Users and sensors share the low-altitude uplink setting, and UAVs relay stored sensor data to the ST-RIS-BS; the channels are low-altitude air-to-ground links with a spherical transmissive surface.

**Problem & objective**: Joint low-altitude data-collection design, a mixed discrete-continuous non-convex optimization, maximizes collected sensor data, $\max\sum_{m,k}\text{collected\_data}_{m,k}$, subject to cellular-user rate, UAV trajectory, collision, scheduling, power, and ST-RIS phase constraints.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Sensor scheduling | $a_{m,k}(t)$ | binary | UAV $m$ collects sensor $k$ in slot $t$ |
| UAV relay/sleep mode | $r_m(t)$ | binary | UAV $m$ relays data or sleeps |
| Cellular-user power | $p_k(t)$ | continuous, bounded | Uplink power of cellular user $k$ |
| ST-RIS phases | $\boldsymbol\theta(t)$ | unit-modulus phases | Spherical transmissive-RIS configuration |
| UAV trajectory | $\mathbf q_m(t)$ | continuous 3-D position | UAV data-collection path |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Cellular users meet their guaranteed uplink-rate requirements |
| C2 | Each sensor/UAV scheduling indicator is binary and respects per-slot service capacity |
| C3 | UAV trajectories satisfy start/end, speed, and collision-avoidance constraints |
| C4 | Cellular-user powers stay within their limits |
| C5 | ST-RIS transmission phases obey the spherical surface model and unit-modulus limits |

**Algorithm**: Derive planar versus spherical spatial-average gain → formulate the joint scheduling/power/phase/trajectory blocks → alternate block coordinate descent updates → use successive convex approximation for the trajectory and coupled continuous subproblems → iterate until collected data converges.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Liu et al. [x] studied a spherical transmissive-RIS-enabled base station for low-altitude communication and UAV data collection. They formulated a joint problem that maximizes collected sensor data while guaranteeing cellular-user uplink rates and coordinating sensor scheduling, UAV relay or sleep decisions, cellular-user power, ST-RIS phases, and UAV trajectories. The spherical surface is introduced to reduce the angle sensitivity of planar transmissive RIS base stations, and spatial average gains are derived for the two architectures. A block coordinate descent procedure with successive convex approximation solves the coupled scheduling, beamforming, and trajectory design. Simulations report higher collected data and spatial-average gain for the spherical configuration than the planar configuration in the evaluated scenarios.

## Problem

Planar transmissive RIS-enabled BSs can be sensitive to incidence/departure angle, which is poorly matched to dynamic low-altitude communication where UAVs and users appear across the 3-D space around the BS. The paper targets the architectural and modeling gap between RIS as an auxiliary wall-mounted reflector and RIS as the radiating module of a low-cost BS.

## System model

- A base station uses one omnidirectional antenna plus a spherical T-RIS.
- The application scenario includes `K1` remote IoT sensors, `K2` uplink cellular users, and `M` UAVs acting as data collectors.
- UAVs collect sensor data, relay stored data to the ST-RIS-BS, and avoid collisions while following start/end position constraints.
- Uplink cellular users share the communication setting and require guaranteed rates.

## Method

The paper derives spatial average gain for planar and spherical transmissive RISs using spatial integration and effective responsive elements. It then formulates a joint low-altitude data-collection problem over sensor scheduling, UAV relay/sleep decisions, cellular-user transmit power, ST-RIS phase shifts, and UAV 3-D trajectories. The solution uses block coordinate descent and successive convex approximation.

## Key findings

- The theoretical spatial-average-gain analysis reports up to 36.6% improvement for ST-RIS over PT-RIS under the same RIS area and user-distance conditions.
- The abstract reports 45% more collected data than the PT-RIS configuration in the evaluated low-altitude scenario.
- At `N = 100`, 1-bit ST-RIS phase quantization loses 18.8%; the loss rises to 26.1% at `N = 200` in the parsed results.
- At `Emax = 80 kJ` and `K1 = 16`, ST-RIS gives about 36.8% improvement over PT-RIS in the parsed simulation discussion.

## Limitations / future work

The future-work discussion names boundary modeling, element effectiveness, coupling, manufacturing imperfections, and non-ideal curvature. The parse has visible OCR/math corruption in equations and constraints, so this page reports only robust headline claims and avoids detailed formula transcription.

## Relation to the corpus

This source extends the wiki's RIS family beyond reflecting, active, STAR, and aerial active-RIS roles. [[lin-2025-energy-effective-ris-multiuav-coverage]] uses facade RIS panels to assist multi-UAV coverage; [[jeon-2026-ampli-flection-aerial-backhaul]] optimizes active-RIS aerial backhaul; this paper instead puts a spherical transmissive RIS directly into the BS architecture and tests it through [[uav-data-collection]] and [[uav-trajectory-control]] decisions.

## Raw artifacts

- `raw/sources/Angle-Insensitive_Spherical_T-RIS-Enabled_Base_Station/Angle-Insensitive_Spherical_T-RIS-Enabled_Base_Station.md`
- Original PDF and extracted figures (`images/`) in the same folder.
