---
type: source
title: "M-SIALNS for Air-Ground Collaborative Inspection: Spatio-Temporal Conflict Mitigation in Complex Bi-Layer Networks"
authors: ["Miaohan Zhang", "Yuanhao Xu", "Xuewei Yu", "Chunyan Zhang", "Jianlei Zhang"]
year: 2026
url: "https://doi.org/10.1109/TITS.2025.3647141"
venue: "IEEE Transactions on Intelligent Transportation Systems (IEEE T-ITS)"
tags: [source, vehicle-uav-inspection, adaptive-large-neighborhood-search, routing, spatiotemporal-conflict]
related:
  - "[[vehicle-uav-collaborative-inspection]]"
  - "[[adaptive-large-neighborhood-search]]"
  - "[[genetic-algorithm]]"
  - "[[qi-2026-drone-vehicle-mec-inspection]]"
  - "[[jia-2026-ufsp-rail-inspection]]"
  - "[[guo-2026-aot-uav-inspection-offloading]]"
created: 2026-07-13
updated: 2026-07-13
---

# M-SIALNS for Air-Ground Collaborative Inspection: Spatio-Temporal Conflict Mitigation in Complex Bi-Layer Networks

## Citation

Zhang, M., Xu, Y., Yu, X., Zhang, C., & Zhang, J. (2026). M-SIALNS for air-ground collaborative inspection: Spatio-temporal conflict mitigation in complex bi-layer networks. *IEEE Transactions on Intelligent Transportation Systems, 27*(3), 3530-3545. https://doi.org/10.1109/TITS.2025.3647141

## TL;DR

M-SIALNS schedules multiple vehicles and UAVs on coupled road and aerial inspection graphs. Clustered initialization plus dependency-aware destruction/repair handles exclusive ground-node occupancy, multi-task sorties, and cross-vehicle UAV recovery.

## Problem and system model

The MUMV-CIVRP-BLRN minimizes inspection completion time. Vehicles move on a ground graph, carry UAVs, and occupy launch/recovery nodes exclusively during operations. UAVs inspect aerial arcs, may chain multiple tasks in one sortie, and may land on a different compatible vehicle. Constraints maintain route continuity, timing, endurance, carrying capacity, task coverage, launch/recovery synchronization, and UAV state across vehicles.

## Method

[[adaptive-large-neighborhood-search|M-SIALNS]] constructs the dual-layer roadmap, applies cluster-first/route-second initialization, and adaptively combines RANDOM, similarity-based, and worst-component destruction with greedy, regret, and noise-based repair. Removing a launch/recovery task also removes dependent successor task chains, preserving predecessor closure and schedule feasibility.

## Key findings

- Synthetic benchmarks adapt Solomon clustered/random/mixed instances to 50-500 inspection arcs and 30-200 km regions; each configuration runs 30 times.
- The abstract reports 1.6%-11.0% shorter inspection duration than comparison algorithms. Section V reports 7.97%-10.22% improvement for medium and 9.76%-11.84% for large instances.
- On R1_6_1-U500-R150-(8:80), the average objective is 24.14, 11.0% below ALNS-GTIS and 13.3% below T-ALNS.
- Conflict plots indicate roughly 28%/35%/42% fewer conflicting tasks and 31%/39%/45% lower conflict duration for small/medium/large cases; these values are figure-derived.
- Sensitivity studies report diminishing returns and context-dependent fleet ratios: 3:4 is best in the modeled complex environment and 4:4 in the modeled urban environment.

## Limitations

Evidence is computational. Benchmarks are synthetic because no established MUMV-CIVRP-BLRN set exists, and the power-grid/urban cases are modeled rather than field deployments. Hardware specifications parameterize simulation but do not constitute a hardware test. Wind and positioning uncertainty, nonlinear UAV energy, time windows, urgency, and adaptive online control remain future work; OCR-damaged complexity expressions are not promoted.

## Relation to the corpus

[[vehicle-uav-collaborative-inspection]] complements MEC-centric inspection work such as [[qi-2026-drone-vehicle-mec-inspection]] and offloading-oriented [[guo-2026-aot-uav-inspection-offloading]]. Its distinctive contribution is fleet-level bi-layer routing with physical node occupancy and flexible UAV recovery.

## Raw artifacts

- Parse: `raw/sources/M-SIALNS_for_Air-Ground_Collaborative_Inspection_Spatio-Temporal_Conflict_Mitigation_in_Complex_Bi-Layer_Networks/M-SIALNS_for_Air-Ground_Collaborative_Inspection_Spatio-Temporal_Conflict_Mitigation_in_Complex_Bi-Layer_Networks.md`
- Origin PDF and extracted figures (`images/`) are in the same folder.
