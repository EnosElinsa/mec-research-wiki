---
type: source
title: "Placement Optimization of UAV-Mounted Mobile Base Stations"
authors: ["Jiangbin Lyu", "Yong Zeng", "Rui Zhang", "Teng Joon Lim"]
year: 2017
url: "https://doi.org/10.1109/LCOMM.2016.2633248"
venue: "IEEE Communications Letters (IEEE COMML)"
tags: [source, cellular-connected-uav, drone-cell-3d-placement, geometric-disk-cover, air-to-ground-channel-model, uav-communications]
related:
  - "[[drone-cell-3d-placement]]"
  - "[[geometric-disk-cover]]"
  - "[[cellular-connected-uav]]"
  - "[[weighted-kmeans-uav-deployment]]"
  - "[[bor-yaliniz-2016-3d-abs-placement]]"
  - "[[al-hourani-2014-optimal-lap-altitude]]"
  - "[[zeng-2016-throughput-relaying]]"
  - "[[mozaffari-2017-uav-iot-energy-efficient]]"
created: 2026-06-02
updated: 2026-06-02
---

# Placement Optimization of UAV-Mounted Mobile Base Stations

## Citation

Lyu, J., Zeng, Y., Zhang, R., & Lim, T. J. (2017). *Placement Optimization of UAV-Mounted Mobile Base Stations*. **IEEE Communications Letters**. DOI: 10.1109/LCOMM.2016.2633248. (Manuscript received 26 October 2016; revised 21 November 2016; accepted 22 November 2016; date of publication 29 November 2016; date of current version 8 March 2017 → year 2017. Volume/issue/pages `not in parse`.)

## TL;DR

Minimizes the **number of UAV-mounted mobile base stations (MBSs)** needed to provide wireless coverage to a set of ground terminals (GTs), so each GT lies within the communication radius `r` of at least one MBS. The paper casts this as the NP-hard **Geometric Disk Cover (GDC)** problem and proposes a **polynomial-time `O(K^3)`-worst-case spiral algorithm**: MBSs are placed **sequentially along the boundary (convex-hull perimeter) of the still-uncovered GTs and nudged inward** toward the area center, so their connecting line traces an inward spiral until all GTs are covered. Numerically, it nearly matches the exact (exponential) core-sets optimum on small instances and beats strip-based, K-means, and random heuristics on both MBS count and runtime.

## Problem framing

UAV-mounted MBSs can give wireless connectivity where there is no terrestrial infrastructure (battlefields, disaster zones), backhaul-connected via satellite. Assuming GT locations are known, UAVs fly at a fixed altitude `H`, and UAV–GT channels are LoS-dominated (free-space path loss → a coverage radius `r` for the SNR threshold), the deployment cost reduces to **how few MBSs are needed and where to place them**. This is the GDC problem, NP-hard in general; the exact core-sets method has running time exponential in the number of GTs `K`, and the existing strip-based heuristic loses performance by partitioning the plane into independent strips. The paper seeks a low-complexity placement that avoids that independent-region loss.

## System model

- **Coverage.** `K` GTs at known 2-D locations; each MBS covers a ground disk of radius `r` (LoS free-space path-loss model, fixed altitude `H`, fixed transmit power, minimum SNR threshold). (P1) minimizes `|M|` (the MBS count) such that every GT is within `r` of some MBS.
- **Relation to classic problems.** (P1) is the **GDC** problem; it is linked to the **p-center** problem (P2) (locate `p` centers minimizing the covering radius `ρ`), so GDC can be solved as a series of p-center problems with increasing `p`. Both are NP-hard (brute-force p-center is `O(p^K)`).

## Method

- **Spiral placement (Algorithm 1).** Repeatedly: find the boundary GTs of the uncovered set via the **convex hull**, list them counter-clockwise, place an MBS to cover a boundary GT `k0`, then refine its location inward to cover as many additional boundary then inner GTs as possible; advance counter-clockwise to the next uncovered boundary GT. Priority to boundary GTs reduces dedicated-MBS "outliers."
- **LocalCover (Algorithm 2).** Refines a single MBS location to guarantee a prioritized GT set and greedily add nearby secondary GTs, pruning GTs more than `2r` apart (they cannot share an MBS) and solving the **1-center** problem to test single-disk coverage. This avoids the exhaustive `2^{|P_sec|}` subset search of the underlying combinatorial problem (P3).
- **Complexity.** Worst-case `O(K[K log K + K·C(K)])` where `C(K)` is the 1-center subroutine cost (so `O(K^3)` with an `O(K^2)` 1-center), comparable to strip-based but far below core-sets; actual runtime is much lower thanks to the faraway-GT pruning.

## Key findings

- On an 80-GT example (`r = 0.5` km), the spiral algorithm needs **11 MBSs** — the same as the **core-sets exact minimum** — while the strip-based algorithm needs 13.
- Across averaged trials (`K = 80` and `K = 400`, varying `D/r`), the spiral algorithm yields **fewer MBSs than strip-based, K-means, and random** placement and is much faster than core-sets and K-means; its advantage over strip-based **grows with the `D/r` ratio** (more strips → more strip-based loss). Specific table values (e.g. `K=400, D/r=20`: spiral 85.6 vs strip 111.0 vs K-means 120.2 MBSs) are from the parse's Table I.

## Limitations / future work

The model is **communication-coverage only** (a single-snapshot GDC), assuming **LoS free-space channels, fixed altitude, fixed transmit power, and known static GT locations**; inter-cell interference for GTs covered by multiple MBSs is left to subsequent channel-assignment/power control. The authors name future extensions: **backhaul-connectivity constraints between MBSs** and **adaptive placement for moving GTs**.

## Relation to the corpus

A foundational **aerial-base-station deployment** entry. Where [[bor-yaliniz-2016-3d-abs-placement]] optimizes the **3-D placement of a single** drone-cell against an [[air-to-ground-channel-model|air-to-ground channel]] (see [[drone-cell-3d-placement]], [[al-hourani-2014-optimal-lap-altitude]]), this paper solves the complementary **multi-MBS minimum-count coverage** problem as the [[geometric-disk-cover]] problem with a spiral heuristic. It contrasts with clustering-based multi-UAV siting like [[weighted-kmeans-uav-deployment]] (which the paper uses as a benchmark) and treats the UAV as a base station rather than a [[cellular-connected-uav|cellular user]]. It shares the NUS UAV-communications lineage of [[zeng-2016-throughput-relaying]] (co-authors [[yong-zeng]], Rui Zhang, Teng Joon Lim) and complements the energy-efficient UAV-IoT 3-D placement of [[mozaffari-2017-uav-iot-energy-efficient]].

## Raw artifacts

- `raw/sources/Placement_Optimization_of_UAV-Mounted_Mobile_Base_Stations/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
