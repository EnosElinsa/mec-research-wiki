---
type: source
title: "An Adaptive Near-Field Channel Model for 6G XL-MIMO UPA-to-Multi-UAV Cooperative Communications"
authors: ["Lu Bai", "Mengyuan Lu", "Ziwei Huang", "Xuesong Cai", "Xiang Cheng"]
year: ""
url: ""
venue: ""
tags: [source, near-field-communications, xl-mimo, channel-modeling, terahertz-communication, multi-uav, physical-layer]
related:
  - "[[near-field-communications]]"
  - "[[selective-near-field-area]]"
  - "[[extremely-large-scale-mimo]]"
  - "[[terahertz-communication]]"
  - "[[air-to-ground-channel-model]]"
  - "[[autonomous-uav-swarms]]"
created: 2026-07-11
updated: 2026-07-11
---

# An Adaptive Near-Field Channel Model for 6G XL-MIMO UPA-to-Multi-UAV Cooperative Communications

## Citation

Bai, L., Lu, M., Huang, Z., Cai, X., & Cheng, X. *An Adaptive Near-Field Channel Model for 6G XL-MIMO UPA-to-Multi-UAV Cooperative Communications*. Venue / year / DOI: **not in parse**. A current Crossref lookup with the exact and simplified title did not return a reliable title-matched record, so the source leaves publication metadata blank rather than inferring it from references.

## TL;DR

Proposes an adaptive near-field channel model for 6G XL-MIMO uniform-planar-array (UPA) links from a ground station to multiple UAVs. The model introduces a [[selective-near-field-area]] so only links inside the near-field region use spherical-wave calculation, while other links can use plane-wave approximations. It also models array, inter-UAV space, time, and frequency non-stationarity, then validates channel statistics against Wireless InSite ray tracing in a National Stadium scenario.

## Problem

Low-THz 6G links and very large UPAs push UAV links into regimes where far-field plane-wave assumptions break down. Existing UAV channel models are often far-field, ULA-oriented, terrestrial, or single-link oriented, and therefore miss UPA two-dimensional array non-stationarity, multi-UAV spatial coupling, 3D UAV trajectories, self-rotation, and frequency-dependent low-THz behavior.

## System model

A ground BS/GS uses an XL-MIMO UPA to communicate with multiple UAV receivers. The channel includes LoS, ground-reflection, and NLoS twin-cluster components. Each channel impulse response is indexed across UPA transmit elements and UAV receivers. UAVs follow 3D trajectories and can self-rotate; the model tracks path gains, delays, angles, and Doppler-like temporal behavior across array, space, time, and frequency.

## Method

The adaptive model defines a selective near-field area around the UPA, with radius derived from the Rayleigh-distance logic. UAVs, clusters, and reflection points inside the SNA are modeled with spherical wavefronts; outside it, the computation falls back to plane-wave approximations to reduce complexity. A seed-growth plus birth-death process captures UPA non-stationarity, while survival probabilities capture non-stationarity over the array, inter-UAV space, and time. The paper then computes channel statistics including ASTF-CF, TSI, DPSD, and SVS.

## Key findings

- The dataset uses 28 GHz with 2 GHz bandwidth and 0.35 THz with 10 GHz bandwidth, UPA sizes from 8 by 8 to 64 by 64, 5- and 10-UAV scenarios, circular UAV trajectories, and 100 snapshots per frequency/array/UAV-count combination, for 1600 snapshots total.
- Larger UPAs and higher frequencies increase spatial-frequency diversity but also strengthen near-field non-stationarity.
- The 0.35 THz channel decorrelates faster than the 28 GHz channel under the same UAV speed, implying more frequent CSI updates and beam tracking for low-THz UAV links.
- SVS is used to assess correlation among multi-UAV channels; lower SVS indicates weaker inter-UAV channel correlation and higher potential spatial multiplexing capacity.
- Simulation results align closely with ray-tracing outputs for the reported channel statistics, but the parse does not provide a numeric validation-error table.

## Limitations / future work

The validation is simulation/ray-tracing based rather than measurement based. The dataset is built for one National Stadium scenario with selected frequencies, UPA sizes, UAV counts, and circular trajectories. The parse has visible OCR/math corruption in formulas, so this page avoids relying on fragile equation details.

## Relation to the corpus

This is a physical-layer/channel-modeling source, not a computation-offloading paper. It extends the wiki's [[near-field-communications]] and [[extremely-large-scale-mimo]] vocabulary from tutorial/offloading contexts into a multi-UAV low-THz channel dataset. It complements [[zeng-2026-movable-antenna-u2u-channel]], which models UAV-to-UAV wideband MIMO channels, and [[bai-2026-multimodal-uav-vehicle-channel]], which uses multimodal environment data for UAV-vehicle channel modeling.

## Raw artifacts

- `raw/sources/An_Adaptive_Near-Field_Channel_Model_for_6G_XL-MIMO_UPA-to-Multi-UAV_Cooperative_Communications/An_Adaptive_Near-Field_Channel_Model_for_6G_XL-MIMO_UPA-to-Multi-UAV_Cooperative_Communications.md`
- Original PDF and extracted figures (`images/`) in the same folder.
