---
type: source
title: "Multi-Frequency Radio Map Assisted Unmanned Aerial Relay for Bridging Ground D2D Networks"
authors: ["Yangrui Dong", "Chen He", "Huiyu Bai", "Dusit Niyato", "Z. Jane Wang"]
year: 2026
url: "https://doi.org/10.1109/TWC.2025.3600610"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), vol. 25, pp. 2970-2983"
modeling_card: required
tags: [source, radio-map, device-to-device, uav-relay, terrain-aware-channel, k-means]
related:
  - "[[multi-frequency-radio-map-uav-relaying]]"
  - "[[device-to-device-communication]]"
  - "[[terrain-aware-channel-model]]"
  - "[[air-to-ground-channel-model]]"
  - "[[uav-mobile-relaying]]"
  - "[[dusit-niyato]]"
created: 2026-07-13
updated: 2026-07-16
---

# Multi-Frequency Radio Map Assisted Unmanned Aerial Relay for Bridging Ground D2D Networks

## Citation

Dong, Y., He, C., Bai, H., Niyato, D., & Wang, Z. J. (2026). *Multi-Frequency Radio Map Assisted Unmanned Aerial Relay for Bridging Ground D2D Networks*. **IEEE Transactions on Wireless Communications, 25**, 2970-2983. DOI: 10.1109/TWC.2025.3600610.

## TL;DR

Uses Longley-Rice radio maps over real terrain data to construct ground D2D subnetworks, select one aerial gateway per subnetwork, and deploy multi-band UAV relays with a rate-weighted k-means heuristic.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Ground users in complex terrain form D2D subnetworks from a terrain-aware radio map. One gateway user per subnetwork connects to fixed-altitude UAV relays, and each aerial link selects one of several frequency bands whose rates come from user-specific Longley-Rice radio maps.

**Problem & objective**: The joint topology and deployment problem maximizes mean air-to-ground rate, $\max_{\mathbf x,\mathbf a,\mathbf b,\mathbf e}\frac{1}{K}\sum_{k=1}^{K}\sum_{n=1}^{N}\sum_{w=1}^{W}a_k^n b_k^w e_k R_n^{k,w}$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV position | $x_n$ | discrete grid point, $x_n\in X$ | Deployment location of UAV $n$ |
| UAV association | $a_k^n$ | binary, $\{0,1\}$ | Whether gateway user $k$ connects to UAV $n$ |
| Frequency selection | $b_k^w$ | binary, $\{0,1\}$ | Whether user $k$ uses aerial band $w$ |
| Ground-node role | $e_k$ | discrete, $\{0,I_h\}$ | Whether user $k$ is a D2D node or the weighted gateway of subnetwork $h$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| 13-15 | A user can be a D2D node only when it has an eligible ground link whose radio-map rate meets $R_d$ |
| 19-20 | Each connected component selects one gateway with maximum D2D closeness centrality, while independent nodes serve as their own gateways |
| 22a | Every UAV position lies on the mission-region grid, $x_n\in X$ |
| 22b | Each gateway associates with exactly one UAV, $a_k^n\in\{0,1\}$ and $\sum_n a_k^n=1$ |
| 22c | Each gateway selects exactly one aerial band, $b_k^w\in\{0,1\}$ and $\sum_w b_k^w=1$ |

**Algorithm**: Longley-Rice maps first define the D2D adjacency graph, connected subnetworks, and one gateway per component through rate-weighted closeness centrality. A radio-map k-means stage then alternates assigning each gateway to the UAV-band pair with highest rate and moving each UAV to the grid point that maximizes its assigned aggregate rate until assignments stop changing or the iteration cap is reached.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Dong et al. [x] designed multi-frequency UAV relays that bridge ground D2D subnetworks over complex terrain using Longley-Rice radio maps. They jointly modeled D2D topology, one aerial gateway per connected subnetwork, UAV grid placement, user association, and band selection to maximize mean air-to-ground rate. Their pipeline constructs a radio-map adjacency graph, selects gateways by rate-weighted closeness centrality, and replaces Euclidean k-means with alternating rate-maximizing assignment and grid updates. In the 400-user mountainous-terrain study, the multi-frequency D2D architecture has the highest plotted rate, and the 50-iteration radio-map heuristic approaches exhaustive grid traversal while outperforming free-space and ordinary k-means baselines.

## Problem and system model

Ground users form D2D subnetworks at 2.4 GHz, while selected cellular users connect those subnetworks to multiple fixed-altitude UAVs. GMTED2010/OpenStreetMap terrain and Longley-Rice propagation generate one D2D map plus per-user maps for 949 MHz, 2555 MHz, and 3500 MHz air links.

The objective maximizes aggregate air-to-ground transmission rate over D2D structure, gateway selection, UAV placement, user association, and frequency selection.

## Method

An RSS-threshold adjacency matrix identifies connected D2D subnetworks. Radio-map-weighted closeness centrality selects one cellular gateway in each. [[multi-frequency-radio-map-uav-relaying]] then replaces Euclidean k-means assignment and centroids with rate-maximizing user/frequency assignment and grid-position updates. Ground gateway selection is exhaustively optimal under the stated model; UAV deployment remains a suboptimal heuristic.

## Key findings

- The main simulation uses 400 users, three UAVs at 100 m, and a 39.43 km2 mountainous region in Taiping National Forest Park.
- The multi-frequency D2D architecture has the highest plotted rate among fixed-band and no-D2D structures.
- Fifty-iteration radio-map k-means approaches exhaustive grid traversal and exceeds free-space and ordinary k-means baselines in the displayed comparison.
- Rate stabilizes at three or more UAVs in this scenario; this is not a general fleet-sizing result.

## Limitations

The study is simulation-only: radio maps are model-generated from terrain rather than measured. It assumes static users and UAV deployment, link symmetry, one gateway per D2D subnetwork, and a fixed traffic model. Dynamic trajectories, asymmetric links, and real-time demand remain future work. Comparative gains are figure-derived without prose-level exact percentages.

## Relation to the corpus

This source extends [[terrain-aware-channel-model]] from LoS classification to multi-band rate maps and uses [[device-to-device-communication]] to reduce direct aerial links. It consumes radio maps for topology and placement, distinct from channel-estimation and path-planning uses.

## Raw artifacts

- `raw/sources/Multi-Frequency_Radio_Map_Assisted_Unmanned_Aerial_Relay_for_Bridging_Ground_D2D_Networks/Multi-Frequency_Radio_Map_Assisted_Unmanned_Aerial_Relay_for_Bridging_Ground_D2D_Networks.md`
- Original PDF and extracted figures (`images/`) are in the same folder.
