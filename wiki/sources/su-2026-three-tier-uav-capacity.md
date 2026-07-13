---
type: source
title: "Modeling and Capacity Analysis of UAV-Assisted Three-Tier Heterogeneous Wireless Networks"
authors: ["Zhan Su", "Xiaorong Zhu", "Xiaohua Qiu"]
year: 2026
url: "https://doi.org/10.1109/TGCN.2026.3685249"
venue: "IEEE Transactions on Green Communications and Networking (IEEE TGCN), vol. 10, pp. 2865-2876"
tags: [source, emergency-network, noma, multihop-relaying, wireless-backhaul, stochastic-geometry, fairness]
related:
  - "[[noma]]"
  - "[[stochastic-geometry-network-analysis]]"
  - "[[wireless-backhaul]]"
  - "[[jains-fairness-index]]"
  - "[[fairness-metrics-in-mec]]"
  - "[[post-disaster-mec]]"
created: 2026-07-13
updated: 2026-07-13
---

# Modeling and Capacity Analysis of UAV-Assisted Three-Tier Heterogeneous Wireless Networks

## Citation

Su, Z., Zhu, X., & Qiu, X. (2026). *Modeling and Capacity Analysis of UAV-Assisted Three-Tier Heterogeneous Wireless Networks*. **IEEE Transactions on Green Communications and Networking, 10**, 2865-2876. DOI: 10.1109/TGCN.2026.3685249.

## TL;DR

Models a disaster-area uplink as three spectrum-separated tiers: NOMA device access, multihop UAV relaying, and SDMA UAV-to-BS backhaul. It derives tier capacities, compares throughput and satisfaction-based relay allocation, and max-min allocates bandwidth across the end-to-end bottleneck.

## System model

Ground devices form a PPP and transmit to hovering UAVs with perfect, worst-case, or imperfect SIC. Aggregated traffic follows predetermined decode-and-forward UAV routes using OFDM, frequency hopping, and CSMA/CA. Backhaul UAVs transmit to one phased-array BS under transmitter and receiver pointing jitter. The end-to-end rate is the minimum of access, relay, and backhaul capacities.

## Method

The access tier uses PPP order statistics and interference Laplace transforms. Relay throughput maximization is a linear program over time-frequency occupancy, while a concave demand-normalized satisfaction utility trades throughput for flow balance. The backhaul analysis replaces random interference gains by their means, proves the resulting approximation is a lower bound, and bounds its error with a pointing-jitter feasible ellipsoid. A final max-min problem partitions total bandwidth across the three tiers.

## Key findings

- In the simulated network, the paper describes about a 20% capacity gain over a two-tier baseline and identifies backhaul as the main bottleneck.
- NOMA with sufficient SIC depth outperforms OMA in the plotted access comparison; altitude, antenna angle, and imperfect SIC reduce capacity.
- Throughput maximization yields more aggregate relay capacity, while satisfaction maximization maintains a higher and steadier [[jains-fairness-index|Jain index]] in the displayed cases.
- Backhaul capacity is highest at low pointing jitter with an interior beamwidth trade-off when jitter grows.

## Limitations / parse caveats

UAV positions, routes, and topology are fixed, and the model has one BS. Infinite-plane PPP analysis is compared with a finite square simulation. Several appendix equations are OCR-corrupted. The prose's 20% three-tier gain appears inconsistent with the extracted plot levels, so it remains an attributed claim rather than an independently recomputed result.

## Relation to the corpus

This is supporting emergency-network capacity analysis rather than an MEC computation model. It connects [[noma]], stochastic-geometry access analysis, multihop relay fairness, and [[wireless-backhaul]] into one end-to-end bottleneck model relevant to [[post-disaster-mec]].

## Raw artifacts

- `raw/sources/Modeling_and_Capacity_Analysis_of_UAV-Assisted_Three-Tier_Heterogeneous_Wireless_Networks/Modeling_and_Capacity_Analysis_of_UAV-Assisted_Three-Tier_Heterogeneous_Wireless_Networks.md`
- Original PDF and extracted figures (`images/`) are in the same folder.
