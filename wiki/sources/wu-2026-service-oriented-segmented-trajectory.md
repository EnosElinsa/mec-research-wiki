---
type: source
title: "Service-Oriented Segmented Trajectory Design for Low-Altitude UAV-Assisted MEC Networks"
authors: ["Pengfei Wu", "Fu Xiao", "Chao Sha", "Haiping Huang"]
year: 2026
url: "https://doi.org/10.1109/TMC.2025.3605865"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, low-altitude-economy, uav-trajectory-control, trajectory-privacy, mobile-edge-computing, q-learning]
related:
  - "[[low-altitude-intelligent-network]]"
  - "[[uav-trajectory-control]]"
  - "[[trajectory-privacy]]"
  - "[[mobile-edge-computing]]"
  - "[[multi-agent-q-learning]]"
  - "[[service-caching-mec]]"
created: 2026-07-07
updated: 2026-07-07
---

# Service-Oriented Segmented Trajectory Design for Low-Altitude UAV-Assisted MEC Networks

## Citation

Wu, P., Xiao, F., Sha, C., & Huang, H. (2026). *Service-Oriented Segmented Trajectory Design for Low-Altitude UAV-Assisted MEC Networks*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2025.3605865. DOI/venue/year are parse-silent at the top level and verified against a title-matched Crossref/IEEE DOI record.

## TL;DR

Designs privacy-aware low-altitude UAV-MEC trajectories for high-rise smart-building IoT. The framework jointly assigns active smart-window tasks to UAVs, plans service trajectories, and manages energy, using a variable-strategy RL Lin-Kernighan-Helsgaun solver plus trajectory-refinement modules that avoid privacy-sensitive window crossings.

## Problem

High-rise IoT devices need temporary or flexible edge-computing service, but UAVs flying near windows create privacy exposure and battery pressure. The paper maximizes system utility across service latency, energy efficiency, and trajectory privacy for a computation-offloading trajectory optimization problem that is non-convex and NP-hard.

## System model

Smart windows are arranged on high-rise building facades. A UAV flies in a vertical plane parallel to the facade at a constant perpendicular distance, starts and ends at a base station, and visits waypoints associated with active tasks. Each task includes a location, data volume, transmission rate, processing rate, and service sequence information. The model defines a trajectory-privacy metric based on crossings of privacy-sensitive windows and assumes window-to-UAV transmission powers are predetermined rather than jointly optimized.

## Method

The paper decomposes the computation-offloading trajectory problem into coupled assignment and routing decisions. VSRL-LKH combines Q-learning, Sarsa, and Monte Carlo strategy selection with Lin-Kernighan-Helsgaun local search. TRA refines candidate paths to preserve visual privacy, and SOS-TRA extends the refinement to multi-UAV service segmentation, balancing task assignment, energy, and privacy constraints.

## Key findings

- VSRL-TRA produces non-crossing routes with smoother task sequencing than the single-UAV simulated-annealing and genetic-algorithm baselines shown in the parsed trajectory figure.
- VSRL-TRA consistently reports lower service delay than SSA-TRA and SGA-TRA; the advantage grows at larger task scales and under heavier computation.
- Energy efficiency drops as task demand grows, from about 1.2 KB/J at 100 task demands to about 0.2 KB/J at 900 task demands; VSRL-TRA reports roughly 5-10% lower energy consumption.
- Without TRA, VSRL maintains privacy protection above 0.82 in the parsed heavy-task privacy comparison; with TRA, the paper reports 100% privacy protection by avoiding window crossings.
- The battery-utilization analysis marks 100-500 task demands as a safe zone, 500-600 as critical, and beyond 600 as unsustainable for the reported UAV configuration.
- SOS-TRA maintains privacy above 0.85 in the multi-UAV comparisons, with 8-12 UAVs identified as a practical balance point before latency improvements become marginal.
- The conclusion reports up to 43.86% system-reliability improvement and system scores above 0.8 across the evaluated demand scales.

## Limitations / future work

Future work includes adaptive task scheduling for real-time environmental dynamics, distributed coordination for large-scale UAV swarms, and joint optimization of dynamic UAV communication transmit power with trajectory and offloading policies.

## Relation to the corpus

This source extends [[low-altitude-intelligent-network]] and [[uav-trajectory-control]] with [[trajectory-privacy]] for facade-adjacent smart-building service. It is adjacent to [[gong-2026-safe-economic-lae-trajectory]], but where Gong et al. model obstacles, no-fly zones, speed limits, and landing constraints, this paper focuses on service-oriented path segmentation and visual privacy near smart windows.

## Raw artifacts

- `raw/sources/Service-Oriented Segmented Trajectory Design for Low-Altitude UAV-Assisted MEC Networks/Service-Oriented Segmented Trajectory Design for Low-Altitude UAV-Assisted MEC Networks.md`
- Original PDF and extracted figures (`images/`) in the same folder.
