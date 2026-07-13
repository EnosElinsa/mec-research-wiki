---
type: source
title: "UAV-to-UAV Communications in Cellular Networks"
authors: ["M. Mahdi Azari", "Giovanni Geraci", "Adrian Garcia-Rodriguez", "Sofie Pollin"]
year: 2020
url: "https://doi.org/10.1109/TWC.2020.3000303"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), 19(9), 6130-6144"
tags: [source, uav-to-uav, cellular-networks, spectrum-sharing, stochastic-geometry, fractional-power-control]
related:
  - "[[uav-to-uav-communication]]"
  - "[[fractional-power-control]]"
  - "[[device-to-device-communication]]"
  - "[[uav-to-x-communication]]"
  - "[[cellular-connected-uav]]"
  - "[[stochastic-geometry-network-analysis]]"
  - "[[overlay-underlay-spectrum-access]]"
  - "[[air-to-ground-channel-model]]"
  - "[[mozaffari-2016-uav-underlaid-d2d]]"
  - "[[zhang-not-in-parse-cellular-uav-to-x]]"
created: 2026-07-14
updated: 2026-07-14
---

# UAV-to-UAV Communications in Cellular Networks

## Citation

Azari, M. M., Geraci, G., Garcia-Rodriguez, A., & Pollin, S. (2020). *UAV-to-UAV Communications in Cellular Networks*. **IEEE Transactions on Wireless Communications**, 19(9), 6130-6144. DOI: 10.1109/TWC.2020.3000303.

## TL;DR

Develops stochastic-geometry expressions for direct UAV-to-UAV links sharing a cellular ground-user uplink. It compares underlay frequency-hopping access with an overlay that orthogonally partitions bandwidth, and quantifies how altitude, UAV density, link distance, PRB allocation, and fractional power control affect U2U and cellular coverage rates.

## Problem

Direct U2U communication can support aerial coordination without routing every exchange through a base station, but aerial LoS channels also expose cellular receivers and other UAVs to strong interference. The paper asks when U2U pairs can coexist with scheduled ground-user uplinks and whether underlay or orthogonal spectrum partitioning better protects low-percentile rates.

## System model

- Base stations and U2U transmitters are modeled by independent homogeneous PPPs. One scheduled ground user per time-frequency resource in each cell is approximated through a PPP-based uplink interference model.
- Each U2U receiver is placed around its transmitter according to a bounded distance model. Links use LoS/NLoS probabilities, distance-dependent loss, Nakagami fading, and a vertical-array base-station antenna pattern.
- Underlay lets every ground user use all PRBs while each U2U transmitter randomly accesses a fraction of PRBs through frequency hopping; the two tiers create mutual interference.
- Overlay divides bandwidth into orthogonal U2U and ground-uplink portions, removing cross-tier interference but retaining same-tier interference and reducing per-tier bandwidth.
- Both ground users and UAVs use capped per-PRB [[fractional-power-control|fractional power control]], with a compensation factor between zero and one.

## Method

Using [[stochastic-geometry-network-analysis|stochastic geometry]] and interference Laplace transforms, Theorems 1 and 2 derive exact, model-conditional underlay coverage-probability expressions for U2U receivers and cellular uplinks. Overlay follows within the paper's model by removing cross-tier interferers and applying the allocated bandwidth fractions.

Three explicit approximations produce compact corollaries: a fitted approximation to the Nakagami fading CDF, omission of selected NLoS interference terms, and replacement of random UAV transmit power by its mean. Proposition 1 derives that mean power for the paper's truncated-Rayleigh U2U-distance and LoS model. “Exact” therefore means exact under the assumed PPP, association, channel, antenna, and power-control model; the compact formulas add further assumptions and become less accurate at low altitude or over wider U2U-distance ranges.

## Key findings

- Exact analysis, compact approximations, and simulations closely match in the plotted scenarios.
- At 50 m altitude with full underlay access, adding U2U interference reduces median cellular-uplink SINR by less than 3 dB in the tested low-power setting.
- Raising UAV altitude from 50 to 150 m degrades both U2U and cellular-uplink performance in the plotted underlay case because increased LoS probability strengthens interference.
- Shorter U2U distances can improve both tiers because power control lets nearby UAV pairs transmit with less power.
- In the tested underlay settings, ground-user interference dominates U2U rates, while overlay makes UAV density more influential because all U2U pairs share the reserved resources without frequency hopping.
- Overlay gives the strongest reported 5th-percentile ground-user performance and allows a larger fraction of U2U pairs to reach 100 kbps in the tested urban regimes. This is a model- and parameter-specific design conclusion, not a universal minimum-rate guarantee.

## Limitations / definition caveat

The analysis assumes Poisson deployments, one active ground user per PRB per cell, closest-base-station association, common UAV altitude in the altitude study, omnidirectional UAV/user antennas, a modeled base-station sidelobe pattern, and capped fractional power control. Mobility, handover, scheduling overhead, correlated deployments, beam tracking, and implementation measurements are outside the demonstrated system.

The paper uses **overlay** to mean a simultaneous orthogonal bandwidth partition reserved separately for U2U and ground-uplink traffic. This differs from the idle-primary-channel meaning used in some cognitive-radio definitions, including the narrow framing currently associated with [[overlay-underlay-spectrum-access]]. Its recommendation must be read under the paper's orthogonal-partition definition. The analytical results are conditional distribution formulas, not guarantees for deployed cellular networks.

## Relation to the corpus

This source specializes [[device-to-device-communication]] and [[uav-to-x-communication]] to direct [[uav-to-uav-communication]] inside a cellular uplink. It complements [[mozaffari-2016-uav-underlaid-d2d]], where the UAV is a downlink base station and the D2D pairs are terrestrial, and [[zhang-not-in-parse-cellular-uav-to-x]], which optimizes relay modes and resources rather than deriving network-level coverage distributions.

## Raw artifacts

- Parse: `raw/sources/UAV-to-UAV_Communications_in_Cellular_Networks/UAV-to-UAV_Communications_in_Cellular_Networks.md`
- Origin PDF: `raw/sources/UAV-to-UAV_Communications_in_Cellular_Networks/UAV-to-UAV_Communications_in_Cellular_Networks.pdf`
- Figures: `raw/sources/UAV-to-UAV_Communications_in_Cellular_Networks/images/`
