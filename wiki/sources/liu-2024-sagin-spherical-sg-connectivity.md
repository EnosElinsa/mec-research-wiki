---
type: source
title: "Space-Air-Ground Integrated Networks: Spherical Stochastic Geometry-Based Uplink Connectivity Analysis"
authors: ["Yalin Liu", "Hong-Ning Dai", "Qubeijian Wang", "Om Jee Pandey", "Yaru Fu", "Ning Zhang", "Dusit Niyato", "Chi Chung Lee"]
year: 2024
url: "https://doi.org/10.1109/JSAC.2024.3365891"
venue: "IEEE Journal on Selected Areas in Communications (IEEE JSAC)"
tags: [source, sagin, stochastic-geometry, uplink-connectivity, aerial-vehicle, satellite, analysis]
related:
  - "[[queueing-theory]]"
  - "[[dusit-niyato]]"
  - "[[ullah-2026-mec-drl-ntn-survey]]"
  - "[[liu-2023-sagecn-online-offloading]]"
created: 2026-06-04
updated: 2026-06-04
---

# Space-Air-Ground Integrated Networks: Spherical Stochastic Geometry-Based Uplink Connectivity Analysis

## Citation

Liu, Y., Dai, H.-N., Wang, Q., Pandey, O. J., Fu, Y., Zhang, N., Niyato, D., & Lee, C. C. (2024). *Space-Air-Ground Integrated Networks: Spherical Stochastic Geometry-Based Uplink Connectivity Analysis*. **IEEE Journal on Selected Areas in Communications**, 42(5). DOI: 10.1109/JSAC.2024.3365891. (Received 13 July 2023; accepted 15 December 2023; published 16 February 2024; current version 9 May 2024.)

## TL;DR

Develops an analytical model for the **uplink path connectivity** of SAGINs — the probability of establishing an end-to-end path from ground users (GUs) to a high-altitude satellite, with or without aerial vehicle (AV) relay assistance. Unlike prior work that distributes nodes on a flat plane, this paper models GUs and AVs on **spherical surfaces** (as they appear to a high-altitude satellite), introducing a new **spherical stochastic geometry** approach. Derives closed-form analytical expressions for three connectivity metrics and validates them against simulations. Claims to be the first study of SAGIN uplink path connectivity.

## Problem framing

SAGINs combine satellite, aerial, and terrestrial communication. The uplink (GU → satellite) is essential for global data collection, but: (i) energy-constrained GUs cannot directly connect to satellites; (ii) AVs as relays reduce access load and GU transmission energy. Analyzing connectivity in large-scale SAGINs requires modeling the global distribution of GUs and AVs — which, under high-altitude satellites, must be placed on spherical surfaces, not a flat plane. Standard flat-plane stochastic geometry (PPP, PCP) fails here; spherical geometry is needed.

## System model

- **Three-tier SAGIN:** satellite (space base station) + multiple AVs (aerial relays) + GUs (ground devices), all on/near Earth's surface.
- **Node distributions:** GUs modeled as a Poisson cluster process (PCP) on a sphere (hotspot-like clustering); AVs distributed as a PPP on a spherical shell.
- **Transmission links:** GU→AV direct link, GU→satellite direct link, GU→AV→satellite two-hop relay link.
- **Spherical stochastic geometry:** coverage regions are spherical caps; distances and angles computed in spherical coordinates; analytical connectivity derived by integrating over all spherical node configurations.
- **Three connectivity metrics:** (1) probability of establishing a direct GU→satellite link; (2) probability of at least one GU→AV link (AV relay accessible); (3) end-to-end path connectivity = any path (direct or relayed) exists.

## Key findings

- Derived **closed-form analytical expressions** for all three uplink connectivity metrics in a SAGIN using spherical stochastic geometry (parse Section III).
- Extensive simulations confirm the accuracy of the analytical model across a range of SAGIN parameters (parse abstract + Section IV).
- AV relay assistance significantly **increases end-to-end path connectivity** compared to direct GU→satellite transmission only (parse Section IV).
- The spherical model reveals coverage gaps that flat-plane models underestimate for high-altitude satellite scenarios (parse motivation + Section II).

## Limitations / future work

Parse does not include resource allocation, offloading optimization, or throughput analysis — pure connectivity characterization. Interference between links in the SAGIN is not modeled (future work, per Section V).

## Relation to the corpus

Provides a foundational analytical tool for SAGIN connectivity that complements the SAGIN offloading/computing papers ([[liu-2023-sagecn-online-offloading]], [[zhou-2024-mco-satellite-edge-offloading]], [[cheng-2025-dos-satellite-edge-computing]]). The spherical stochastic geometry approach is unique in the corpus (other stochastic geometry papers use flat-plane PPP). Dusit Niyato ([[dusit-niyato]]) co-authored.

## Raw artifacts

- `raw/sources/Space-Air-Ground_Integrated_Networks_Spherical_Stochastic_Geometry-Based_Uplink_Connectivity_Analysis/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
