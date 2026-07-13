---
type: source
title: "Movable Antenna Enhanced Cellular-Connected UAV Communication With Trajectory Planning"
authors: ["Tianshi Ren", "Xianchao Zhang", "Wenyan Ma", "Lipeng Zhu", "Xiaozheng Gao", "Rui Zhang"]
year: 2026
url: "https://doi.org/10.1109/TWC.2026.3687538"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), vol. 25, pp. 16351-16368"
tags: [source, movable-antenna, cellular-connected-uav, trajectory-planning, beamforming, graph-search]
related:
  - "[[movable-antenna]]"
  - "[[cellular-connected-uav]]"
  - "[[uav-trajectory-control]]"
  - "[[air-to-ground-channel-model]]"
  - "[[selective-uniform-cost-search]]"
created: 2026-07-13
updated: 2026-07-13
---

# Movable Antenna Enhanced Cellular-Connected UAV Communication With Trajectory Planning

## Citation

Ren, T., Zhang, X., Ma, W., Zhu, L., Gao, X., & Zhang, R. (2026). *Movable Antenna Enhanced Cellular-Connected UAV Communication With Trajectory Planning*. **IEEE Transactions on Wireless Communications, 25**, 16351-16368. DOI: 10.1109/TWC.2026.3687538.

## TL;DR

Minimizes a cellular-connected UAV's mission time by jointly planning its path, serving-BS association, MMSE receive beamforming, and onboard movable-antenna positions under a lower-bound expected-SINR condition and mechanical movement constraints.

## Problem and system model

One fixed-altitude UAV flies between prescribed endpoints while ground BSs share spectrum. One BS serves the UAV and the others interfere. The UAV carries a two-dimensional movable receive array whose elements obey region, speed, and spacing limits. Slowly varying channel/loading information is assumed known for offline planning, and a tractable Jensen lower bound on expected SINR supplies the communication-feasibility condition.

## Method

The flight region becomes a square grid with horizontal and diagonal edges flown at maximum speed. At each candidate node, the algorithm carries forward the previous antenna-position vector, computes MMSE combining, retains the serving BS when feasible or selects the best-SINR BS, and improves antenna positions by successive linearization with feasible-direction line search. [[selective-uniform-cost-search]] expands the lowest accumulated-plus-lower-bound-time node and prunes its candidate history.

The antenna solver converges to a first-order stationary point. The graph-search optimality statement is conditional on a valid remaining-time lower bound; practical pruning, discretization, and local antenna solutions do not establish a global solution to the original continuous problem.

## Key findings

- The antenna-position solver converges within ten iterations in the displayed experiment.
- At a 13 dB SINR threshold, MA-MMSE reduces mission time by 6.46%, 18.55%, and 28.35% relative to MA-MRC, single-antenna MMSE, and fixed-position-array MMSE.
- The proposed scheme remains feasible at SINR thresholds 8, 10, 14, and 22 dB above the four reported comparison methods, respectively.

## Limitations

Results are simulations. The model assumes fixed altitude, LoS free-space links, equivalent single-antenna BSs, and known slowly varying interference loading. Grid granularity and pruning trade quality for complexity; a 20 m grid misses a feasible path at 29 dB in one test. Mechanical settling, fast channel changes, and flight validation are not evaluated.

## Relation to the corpus

This paper adds local [[movable-antenna]] control to the interference-limited aerial-user problem in [[cellular-connected-uav]]. Unlike rate-maximizing trajectory designs, it uses communication feasibility to minimize endpoint-to-endpoint mission time.

## Raw artifacts

- `raw/sources/Movable_Antenna_Enhanced_Cellular-Connected_UAV_Communication_With_Trajectory_Planning/Movable_Antenna_Enhanced_Cellular-Connected_UAV_Communication_With_Trajectory_Planning.md`
- Original PDF and extracted figures (`images/`) are in the same folder.
