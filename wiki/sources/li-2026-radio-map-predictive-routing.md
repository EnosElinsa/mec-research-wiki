---
type: source
title: "Radio Map-Assisted Routing and Predictive Resource Allocation Over Dynamic Low-Altitude Networks"
authors: ["Bowen Li", "Junting Chen"]
year: 2026
url: "https://doi.org/10.1109/TWC.2025.3641394"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), vol. 25, pp. 9955-9970, 2026"
tags: [source, low-altitude-network, radio-map, predictive-routing, space-time-graph, resource-allocation, interference-control, multi-commodity-routing]
related:
  - "[[radio-map-assisted-predictive-routing]]"
  - "[[dynamic-space-time-graph-with-virtual-edges]]"
  - "[[junting-chen]]"
  - "[[graph-based-resource-management]]"
  - "[[uav-mobile-relaying]]"
  - "[[radio-map-assisted-channel-estimation]]"
  - "[[radio-map-aided-uav-path-planning]]"
  - "[[zheng-2026-active-search-low-altitude-uav]]"
  - "[[dong-2026-radio-map-d2d-relay]]"
  - "[[bujari-2018-stateless-fanet-routing]]"
created: 2026-07-14
updated: 2026-07-14
---

# Radio Map-Assisted Routing and Predictive Resource Allocation Over Dynamic Low-Altitude Networks

## Citation

Li, B., & Chen, J. (2026). *Radio Map-Assisted Routing and Predictive Resource Allocation Over Dynamic Low-Altitude Networks*. **IEEE Transactions on Wireless Communications**, 25, 9955-9970. DOI: 10.1109/TWC.2025.3641394.

## TL;DR

Uses predicted UAV trajectories and location-indexed radio-map statistics to jointly plan data routes, hop timing, and transmit power while limiting worst-case interference leakage toward a neighboring terrestrial network. A dynamic space-time graph represents forwarding and caching, and the resulting cross-layer method alternates bottleneck-path selection with fixed-route resource allocation before extending the formulation to multiple commodities through orthogonal time-frequency sharing.

## Problem

UAVs carrying out primary missions often follow predetermined trajectories, making future network topology predictable but time varying. Delivering delay-tolerant data over these moving nodes couples route choice to transmission timing: a poor link now may become useful later, while aerial transmissions must protect terrestrial nodes. Uniformly subdivided time-expanded graphs either become large or impose timing boundaries that do not adapt to interference conditions.

The paper minimizes the maximum instantaneous leakage experienced by protected neighboring-network nodes while delivering a complete package within a deadline. Its multi-commodity extension minimizes the corresponding worst leakage across several packages while allocating shared time-frequency resources.

## System model

The aerial network contains a source, a destination, and mobile relay nodes with known positions or trajectories over a planning horizon. Radio maps map predicted transmitter and receiver locations to large-scale channel gains and fading statistics; future instantaneous small-scale fading is not assumed known. Neighboring-network coverage maps supply interference terms for aerial receivers, while aerial transmitters also leak energy toward protected terrestrial nodes.

Forwarding follows a cache-and-pass model: a complete package reaches one node before that node forwards it. The multi-commodity model uses packages with a common size and deadline and assigns orthogonal time-frequency shares to avoid mutual interference among aerial flows. Perfect Doppler compensation is assumed.

## Method

[[dynamic-space-time-graph-with-virtual-edges]] builds a fixed-depth layered graph. Legitimate edges represent full-package forwarding during an interval and carry the minimum achievable worst-case leakage; zero-cost virtual edges represent caching at the same node. Route cost is the largest edge weight, making route selection a bottleneck-path problem.

For each legitimate edge, a convex link-level problem determines the channel-state-dependent power policy and finds the required leakage level by bisection. Deterministic expressions handle uncertain small-scale channels, although one reported approximate bound is supported numerically rather than proved generally. For a fixed route, equal leakage across used hops and monotonic completion time permit globally optimal time/power allocation by bisection. The overall single-commodity algorithm alternates that subproblem with route selection and is proved to converge, but its near-global behavior is established empirically rather than by a global-optimality theorem. The multi-commodity extension alternates per-flow route/timing updates with a monotone feasibility search over shared time-frequency allocations.

## Key findings

- Over 100 randomized single-commodity experiments, the proposed method nearly matches exhaustive route enumeration. The text reports about 13 dB improvement over the two classical graph-based baselines, not over exhaustive search.
- Deadline and package-size sweeps report average gains of 6 dB and 14 dB over two graph-based baselines. In one delay-sensitive case, both baselines require more than 25 dB additional leakage, while the abstract and conclusion round the most favorable gain to more than 30 dB.
- Figure-based comparisons with more protected neighbors indicate gains above 4 dB and 14 dB over the two baselines in the plotted cases; these are scenario-specific readings rather than tabulated guarantees.
- As the commodity count rises from 1 to 19, the reported baseline leakage grows by about 30 dB and the proposed leakage by about 10 dB. The paper describes the resulting growth in the performance gap as 100-fold; it does not establish a universal 100-fold absolute leakage advantage.
- Segmenting a 2-Gbit package in the reported 10-second case improves leakage by 19 dB in the detailed results, while the abstract and conclusion round this figure-derived result to 20 dB.

## Limitations

Evidence is simulation-only. The method assumes known trajectories over the full horizon, available radio-map statistics, perfect Doppler compensation, and cache-and-pass forwarding. Map error, trajectory deviation, map aging, finite buffers, packet-level pipelining, and real-time signaling for the channel-state-dependent power policy are not evaluated. The multi-commodity experiments use equal package sizes and deadlines with orthogonal sharing. Several numerical conclusions come from figures, and OCR damage affects some equations and notation.

## Relation to the corpus

This source specializes [[graph-based-resource-management]] into [[radio-map-assisted-predictive-routing]] over predetermined moving nodes. It differs from [[radio-map-aided-uav-path-planning]], which changes a UAV's physical route, and from [[radio-map-assisted-channel-estimation]], which uses map priors to estimate current channels. It is closer to [[uav-mobile-relaying]] and [[dong-2026-radio-map-d2d-relay]] at the networking level, while [[bujari-2018-stateless-fanet-routing]] provides a local, non-predictive routing contrast. [[zheng-2026-active-search-low-altitude-uav]] shares radio-map reasoning and author [[junting-chen]] but optimizes UAV search and placement rather than a data route over fixed trajectories.

## Raw artifacts

- Parse: `raw/sources/Radio_Map-Assisted_Routing_and_Predictive_Resource_Allocation_Over_Dynamic_Low-Altitude_Networks/Radio_Map-Assisted_Routing_and_Predictive_Resource_Allocation_Over_Dynamic_Low-Altitude_Networks.md`
- Origin PDF: `raw/sources/Radio_Map-Assisted_Routing_and_Predictive_Resource_Allocation_Over_Dynamic_Low-Altitude_Networks/Radio_Map-Assisted_Routing_and_Predictive_Resource_Allocation_Over_Dynamic_Low-Altitude_Networks.pdf`
- Figures: `raw/sources/Radio_Map-Assisted_Routing_and_Predictive_Resource_Allocation_Over_Dynamic_Low-Altitude_Networks/images/`
