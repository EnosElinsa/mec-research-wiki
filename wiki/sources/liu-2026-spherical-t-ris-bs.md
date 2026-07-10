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
updated: 2026-07-11
---

# Angle-Insensitive Spherical T-RIS-Enabled Base Station

## Citation

Liu, J., Xu, W., & Zhang, H. (2026). *Angle-Insensitive Spherical T-RIS-Enabled Base Station*. **IEEE Transactions on Wireless Communications**, 25, 12295-12308. DOI: 10.1109/TWC.2026.3656594. The parse lacks a publication header; venue, year, pages, and DOI were verified from a title-matched Crossref record.

## TL;DR

Proposes a [[spherical-transmissive-ris|spherical transmissive RIS (ST-RIS) enabled base station]] for dynamic low-altitude communication. Instead of a conventional BS antenna array or planar transmissive RIS, the architecture combines one omnidirectional antenna with a spherical T-RIS to reduce angle-sensitive gain loss across 3-D directions. A low-altitude application then jointly optimizes RIS phase shifts, transmit power, user scheduling, and UAV 3-D trajectories to maximize collected sensor data while guaranteeing cellular-user uplink rates.

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
