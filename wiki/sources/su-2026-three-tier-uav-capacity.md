---
type: source
modeling_card: required
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
updated: 2026-11-03
---

# Modeling and Capacity Analysis of UAV-Assisted Three-Tier Heterogeneous Wireless Networks

## Citation

Su, Z., Zhu, X., & Qiu, X. (2026). *Modeling and Capacity Analysis of UAV-Assisted Three-Tier Heterogeneous Wireless Networks*. **IEEE Transactions on Green Communications and Networking, 10**, 2865-2876. DOI: 10.1109/TGCN.2026.3685249.

## TL;DR

Models a disaster-area uplink as three spectrum-separated tiers: NOMA device access, multihop UAV relaying, and SDMA UAV-to-BS backhaul. It derives tier capacities, compares throughput and satisfaction-based relay allocation, and max-min allocates bandwidth across the end-to-end bottleneck.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A disaster-area uplink has three tiers: PPP ground devices access hovering UAVs by NOMA with imperfect SIC, flows cross a multihop UAV relay layer on time-frequency resources with per-hop packet loss, and backhaul UAVs reach base stations by SDMA directional beamforming with antenna-orientation jitter at both ends.
**Problem & objective**: (43) maximizes the end-to-end bottleneck capacity, $\max_{B_1,B_2,B_3}\min[R^{\mathrm{access}}(B_1),R^{\mathrm{relay}}(B_2),R^{\mathrm{backhaul}}(B_3)]$ s.t. $0\le B_1+B_2+B_3\le B_{\mathrm{system}}$. Inside the relay layer, P1 (29) maximizes the sum throughput $R^{\mathrm{relay}}$ (THM) and P2 (30) maximizes a demand-normalized satisfaction utility $\sum S(R_{I_U}/A_{I_U})$ (SFM), both over the occupancy factors $\mathbf x$ s.t. (24)–(28).
**Decision variables**:
| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Layer bandwidths | $B_1,B_2,B_3$ | continuous, nonnegative | Bandwidth of the access, relay, and backhaul layers |
| Resource occupancy factor | $x_{I_U,l,f}$ | continuous, $[0,1]$ | Share of resource $f$ on link $l$ used by flow $I_U$ |
**Constraints**:
| ID | Meaning and key expression |
|---|---|
| (43) | Total bandwidth: $0\le B_1+B_2+B_3\le B_{\mathrm{system}}$ |
| (24) | Antenna limit: each UAV uses at most $J$ relay-layer links at once, $\sum_{I_U}\sum_{l\in\mathcal L^U}\sum_f x_{I_U,l,f}\le J$ |
| (25) | Energy limit: link occupancy is bounded by the UAV's remaining hover time, $\le x_U^{\mathrm{remain}}$ |
| (26) | Flow balance: each flow's rate $\sum_f x_{I_U,l,f}C_{l,f}(1-E)^{Z_{I_U,l}}$ is equal on every hop of its path |
| (27) | Minimum rate: each hop rate of each flow is at least $R_{\mathrm{th}}$ |
| (28) | Normalization: $x_{I_U,l,f}\in[0,1]$ |
**Algorithm**: Derive NOMA coverage and ergodic access capacity with stochastic geometry → solve the relay allocation P1 or P2 (P1 is a linear program; SFM reduces to THM for linear $S$) → bound the jittered SDMA backhaul capacity with a moment-based approximation → equalize the three layer capacities to solve the max–min bandwidth split (43).

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Su et al. [x] modeled a disaster-area three-tier UAV wireless network with NOMA device access, multihop UAV relaying, and SDMA UAV-to-base-station backhaul. They derived tier capacities under stochastic-geometry access, predetermined decode-and-forward routes, and pointing-jitter-aware backhaul, and formulated max-min bandwidth allocation over the end-to-end bottleneck. Relay sum throughput (THM) is maximized as a linear program, and a demand-normalized satisfaction utility (SFM) trades some capacity for a higher Jain's fairness index. The backhaul analysis uses a moment-matched lower bound and an ellipsoidal pointing-jitter error model. Simulations report an approximately 20% capacity gain over the evaluated two-tier baseline and identify the backhaul as the main bottleneck.

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
