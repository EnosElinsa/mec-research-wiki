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
updated: 2026-07-16
---

# Modeling and Capacity Analysis of UAV-Assisted Three-Tier Heterogeneous Wireless Networks

## Citation

Su, Z., Zhu, X., & Qiu, X. (2026). *Modeling and Capacity Analysis of UAV-Assisted Three-Tier Heterogeneous Wireless Networks*. **IEEE Transactions on Green Communications and Networking, 10**, 2865-2876. DOI: 10.1109/TGCN.2026.3685249.

## TL;DR

Models a disaster-area uplink as three spectrum-separated tiers: NOMA device access, multihop UAV relaying, and SDMA UAV-to-BS backhaul. It derives tier capacities, compares throughput and satisfaction-based relay allocation, and max-min allocates bandwidth across the end-to-end bottleneck.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A disaster-area uplink has three separated tiers: NOMA device access to hovering UAVs, OFDM/frequency-hopping multihop UAV relaying, and SDMA UAV-to-BS wireless backhaul. Ground devices form a spatial process, UAV routes are predetermined, pointing jitter affects the phased-array backhaul, and the end-to-end rate is the minimum of access, relay, and backhaul capacities.

**Problem & objective**: The resource-allocation layer maximizes a max-min end-to-end capacity, $\max\min\{C_{\mathrm{access}},C_{\mathrm{relay}},C_{\mathrm{backhaul}}\}$, and also evaluates a demand-normalized satisfaction utility for balanced relay service under fixed topology.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Tier bandwidth split | $B_A,B_R,B_B$ | continuous, nonnegative | Bandwidth assigned to access, relay, and backhaul tiers |
| Relay time-frequency occupancy | $\mathbf x$ | binary/continuous schedule | OFDM and frequency-hopping resources used by routed traffic |
| Flow satisfaction | $u_f$ | continuous, bounded | Delivered fraction of demand for flow $f$ |
| Relay allocation | $\mathbf r$ | continuous, capacity-bounded | Traffic rate assigned to each multihop relay route |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Tier bandwidths partition the available spectrum, $B_A+B_R+B_B\le B_{\mathrm{tot}}$ |
| C2 | NOMA access, relay occupancy, and SDMA backhaul rates are within their tier capacities |
| C3 | Routed traffic is flow-conserving across decode-and-forward UAV hops |
| C4 | Relay allocations satisfy link, time-frequency, and demand limits |
| C5 | The max-min solution and satisfaction utility respect the end-to-end bottleneck definition |

**Algorithm**: Derive stochastic-geometry access capacities and interference transforms → solve relay throughput allocation as a linear program → optimize demand-normalized satisfaction for balanced flows → approximate jittered backhaul capacity with a lower-bound moment model → solve the final max-min bandwidth partition.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Su et al. [x] modeled a disaster-area three-tier UAV wireless network with NOMA device access, multihop UAV relaying, and SDMA UAV-to-base-station backhaul. They derived tier capacities under stochastic-geometry access, predetermined decode-and-forward routes, and pointing-jitter-aware backhaul, and formulated max-min bandwidth allocation over the end-to-end bottleneck. Relay throughput is optimized with a linear program, while a demand-normalized satisfaction utility evaluates balanced flow service. The backhaul analysis uses a moment-matched lower bound and an ellipsoidal pointing-jitter error model. Simulations report an approximately 20% capacity gain over the evaluated two-tier baseline and identify the backhaul as the main bottleneck.

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
