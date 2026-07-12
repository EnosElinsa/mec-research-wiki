---
type: source
title: "UAV-Aided Offloading for Cellular Hotspot"
authors: ["Jiangbin Lyu", "Yong Zeng", "Rui Zhang"]
year: 2018
url: "https://doi.org/10.1109/TWC.2018.2818734"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, uav-base-station, cellular-offloading, trajectory-optimization, spectrum-sharing, cyclical-trajectory, throughput-maximization]
related:
  - "[[cellular-connected-uav]]"
  - "[[uav-trajectory-control]]"
  - "[[drone-cell-3d-placement]]"
  - "[[zeng-2019-uav-comm-tutorial-5g]]"
  - "[[lyu-2017-spiral-mbs-placement]]"
  - "[[yong-zeng]]"
created: 2026-06-04
updated: 2026-07-13
---

# UAV-Aided Offloading for Cellular Hotspot

## Citation

Lyu, J., Zeng, Y., & Zhang, R. (2018). *UAV-Aided Offloading for Cellular Hotspot*. **IEEE Transactions on Wireless Communications**, 17(6). DOI: 10.1109/TWC.2018.2818734. (Received 21 November 2017; accepted 19 March 2018; published 30 March 2018; current version 8 June 2018.)

## TL;DR

Proposes using a UAV as a **flying aerial base station** that cycles along the cell edge to offload data traffic from cell-edge mobile terminals (MTs), relieving the heavily-loaded ground base station (GBS) in hotspot periods. Jointly optimizes the UAV's **cyclical trajectory**, **bandwidth allocation**, and **user partitioning** (which MTs are served by the UAV vs. the GBS) to **maximize minimum throughput** across all MTs. Considers both **orthogonal spectrum sharing** (UAV and GBS use separate bands) and **spectrum reuse** (shared band with interference control). Shows significant spatial throughput improvement over GBS-only and outperforms conventional small-cell offloading.

## Problem framing

Cell-edge MTs have poor channels to the GBS, especially when the GBS is heavily loaded. A UAV flying close to cell-edge MTs establishes short-range LoS links that can offload traffic. The cyclical trajectory (UAV circles the cell edge periodically) is a practical, systematic design that ensures all cell-edge MTs get served. Jointly designing the cycle path, bandwidth split, and user assignment under max-min throughput fairness is the core challenge.

## System model

- **One GBS** at cell center + **one UAV** flying cyclically at fixed altitude at cell edge. **K mobile terminals (MTs)** distributed in the cell.
- **User partitioning:** MTs either connect to GBS or UAV in each time period.
- **Orthogonal spectrum sharing:** GBS and UAV use disjoint frequency bands — no interference; simpler problem.
- **Spectrum reuse:** GBS and UAV share the total bandwidth — mutual interference; tighter constraints but higher potential throughput.
- **Objective:** maximize minimum throughput of all MTs (max-min fairness) subject to: UAV speed + bandwidth + partitioning constraints.
- **Optimization:** block coordinate descent-type approach; trajectory optimization via iterative convex approximation; bandwidth and partitioning solved as LP/QP subproblems.

## Key findings

- Proposed UAV offloading with cyclical trajectory **significantly improves spatial throughput** over GBS-only network (parse abstract + numerical results).
- **Spectrum reuse provides further throughput gains** over orthogonal spectrum sharing, at the cost of slightly higher computational complexity for interference control (parse abstract + Section V).
- Compared to a conventional terrestrial **small-cell offloading scheme**, the UAV offloading scheme achieves **higher throughput** while saving infrastructure cost (parse abstract + Section V).

## Limitations / future work

Single UAV model; fixed cyclical trajectory topology (not fully free-form 2D trajectory). Fixed UAV altitude. The optimization assumes time-varying user positions are known (offline).

## Relation to the corpus

From the Zeng/Zhang group (NUS) — same authors as the UAV-comms tutorial [[zeng-2019-uav-comm-tutorial-5g]]. Complements [[lyu-2017-spiral-mbs-placement]] (which places UAV-MBSes geometrically without trajectory optimization) and [[wu-2018-multiuav-minrate-trajectory]] (max-min-rate multi-UAV). The cyclical trajectory idea connects to the successive-hover-and-fly pattern in [[successive-hover-and-fly-trajectory]]. Establishes the **cellular hotspot offloading** use case for UAVs that later corpus sources build on.

## Raw artifacts

- `raw/sources/UAV-Aided_Offloading_for_Cellular_Hotspot/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
