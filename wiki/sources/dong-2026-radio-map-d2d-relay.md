---
type: source
title: "Multi-Frequency Radio Map Assisted Unmanned Aerial Relay for Bridging Ground D2D Networks"
authors: ["Yangrui Dong", "Chen He", "Huiyu Bai", "Dusit Niyato", "Z. Jane Wang"]
year: 2026
url: "https://doi.org/10.1109/TWC.2025.3600610"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), vol. 25, pp. 2970-2983"
tags: [source, radio-map, device-to-device, uav-relay, terrain-aware-channel, k-means]
related:
  - "[[multi-frequency-radio-map-uav-relaying]]"
  - "[[device-to-device-communication]]"
  - "[[terrain-aware-channel-model]]"
  - "[[air-to-ground-channel-model]]"
  - "[[uav-mobile-relaying]]"
  - "[[dusit-niyato]]"
created: 2026-07-13
updated: 2026-07-13
---

# Multi-Frequency Radio Map Assisted Unmanned Aerial Relay for Bridging Ground D2D Networks

## Citation

Dong, Y., He, C., Bai, H., Niyato, D., & Wang, Z. J. (2026). *Multi-Frequency Radio Map Assisted Unmanned Aerial Relay for Bridging Ground D2D Networks*. **IEEE Transactions on Wireless Communications, 25**, 2970-2983. DOI: 10.1109/TWC.2025.3600610.

## TL;DR

Uses Longley-Rice radio maps over real terrain data to construct ground D2D subnetworks, select one aerial gateway per subnetwork, and deploy multi-band UAV relays with a rate-weighted k-means heuristic.

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
