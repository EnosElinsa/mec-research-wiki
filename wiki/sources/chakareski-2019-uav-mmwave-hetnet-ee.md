---
type: source
title: "An Energy Efficient Framework for UAV-Assisted Millimeter Wave 5G Heterogeneous Cellular Networks"
authors: ["Jacob Chakareski", "Syed Naqvi", "Nicholas Mastronarde", "Jie Xu", "Fatemeh Afghah", "Abolfazl Razi"]
year: 2019
url: "https://doi.org/10.1109/TGCN.2019.2892141"
venue: "IEEE Transactions on Green Communications and Networking (IEEE TGCN), vol. 3, no. 1, pp. 37-44, Mar. 2019"
tags: [source, uav-base-station, mmwave, heterogeneous-network, energy-efficiency, radio-resource-management, drone-cell]
related:
  - "[[drone-cell-3d-placement]]"
  - "[[air-to-ground-channel-model]]"
  - "[[cellular-connected-uav]]"
  - "[[mozaffari-2015-drone-small-cells]]"
  - "[[mozaffari-2019-uav-wireless-tutorial]]"
created: 2026-07-11
updated: 2026-07-11
---

# An Energy Efficient Framework for UAV-Assisted Millimeter Wave 5G Heterogeneous Cellular Networks

## Citation

Chakareski, J., Naqvi, S., Mastronarde, N., Xu, J., Afghah, F., & Razi, A. (2019). *An Energy Efficient Framework for UAV-Assisted Millimeter Wave 5G Heterogeneous Cellular Networks*. **IEEE Transactions on Green Communications and Networking**, 3(1), 37-44. DOI: 10.1109/TGCN.2019.2892141. DOI/venue/year were verified against a title-matched Crossref/IEEE DOI record; technical claims are grounded in the local parse.

Author-disambiguation note: the "Jie Xu" in this paper is identified by the local parsed bio as an Electrical and Computer Engineering faculty member at the University of Miami, distinct from the CUHK-Shenzhen ISAC author entity [[jie-xu]].

## TL;DR

Analyzes a multi-band HetNet with one microwave macro BS, ground dual-mode mmWave small cells, and UAV small BSs. A two-layer optimization framework first derives UAV coverage radius/altitude from maximum allowed path loss, then maximizes system energy efficiency through radio resource allocation under QoS and transmit-power constraints.

## Problem

UAV base stations can extend 5G coverage and throughput, but their energy limits, interference behavior, altitude-dependent air-to-ground channel, and coexistence with terrestrial macro/mmWave small cells make placement and resource management coupled. The paper asks when adding a UAV tier improves energy efficiency rather than simply adding more power consumption.

## System model

The simulated HetNet has one microwave macro BS, three dual-mode mmWave SBSs, two UAV BSs, and users distributed in a 1 km by 1 km area. The macro and UAV tiers use 2 GHz carriers and 20 MHz bandwidth. SBSs use 28 GHz and 73 GHz bands with larger bandwidths. Users associate through biased received power or biased SINR, and the UAV air-to-ground channel uses a LoS-probability/path-loss model.

## Method

The outer layer derives the UAV coverage radius and height from a maximum path-loss threshold. The inner layer maximizes system energy efficiency, defined as aggregate user data rate divided by aggregate transmission plus circuit power. The paper compares the proposed EE-maximization resource allocation against power-minimization and rate-maximization baselines.

## Key findings

- Introducing the UAV tier can nearly double system energy efficiency at specific target SINR values; at tau = 0 dB, the reported EE-maximization curve with UAVs is almost twice the no-UAV case.
- The proposed EE-maximization approach outperforms power-minimization and rate-maximization baselines in system EE.
- In the reported setting, system EE peaks at UAV altitude 140 m, corresponding to maximum path loss 68.8 dB; the system EE at 140 m is 35% greater than at 10 m.
- System sum rate for the rate-maximization approach is about 13% greater with the UAV tier; for power minimization at tau = 20 dB, the sum rate is about 10% greater with UAVs.
- Increasing the UAV biasing factor can pull substantially more users into the UAV tier, but macro/mmWave biasing can reduce UAV-tier association.

## Limitations / future work

The paper presents a first study of this particular UAV-assisted multi-band HetNet and compares against border-case baselines rather than directly matched prior systems. Future work includes complexity analysis, lower-complexity suboptimal methods, practical implementation, joint power allocation and user association, horizon-based dynamic UAV placement, and economics of UAV-enabled rural coverage.

## Relation to the corpus

This is an early UAV-as-aerial-small-cell energy-efficiency source, adjacent to [[mozaffari-2015-drone-small-cells]] and the broader [[drone-cell-3d-placement]] / [[air-to-ground-channel-model]] foundation. Unlike later UAV-MEC papers, it does not optimize computation offloading; it supplies a communication-side energy-efficiency baseline for how UAV tiers interact with terrestrial macro/mmWave small cells.

## Raw artifacts

- `raw/sources/An_Energy_Efficient_Framework_for_UAV-Assisted_Millimeter_Wave_5G_Heterogeneous_Cellular_Networks/An_Energy_Efficient_Framework_for_UAV-Assisted_Millimeter_Wave_5G_Heterogeneous_Cellular_Networks.md`
- Original PDF and extracted figures (`images/`) in the same folder.
