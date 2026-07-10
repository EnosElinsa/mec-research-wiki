---
type: source
title: "Demand-Aware Multi-Area Multi-UAV Empowered Mobile Edge Computing: A Joint Energy and Delay Optimization"
authors: ["Chaoda Peng", "Yanglin Chen", "Xumin Huang", "Zexiong Wu", "Yueting Xu", "Yuan Wu"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3697839"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, uav-assisted-mec, multi-uav, smart-city, demand-aware-deployment, constrained-multi-objective-optimization, evolutionary-algorithm, pareto]
related: ["[[constrained-multi-objective-evolutionary-algorithm]]", "[[multi-uav-assisted-mec]]", "[[load-balancing-uav-mec]]", "[[constraint-violation-evaluation]]", "[[peng-2022-cmop-uav-path-planning]]", "[[peng-2024-energy-time-uav-its]]", "[[huang-2023-mu-aec-task-energy]]", "[[chaoda-peng]]", "[[xumin-huang]]"]
created: 2026-07-06
updated: 2026-07-06
---

# Demand-Aware Multi-Area Multi-UAV Empowered Mobile Edge Computing: A Joint Energy and Delay Optimization

## Citation

Peng, C., Chen, Y., Huang, X., Wu, Z., Xu, Y., & Wu, Y. (2026). *Demand-Aware Multi-Area Multi-UAV Empowered Mobile Edge Computing: A Joint Energy and Delay Optimization*. **IEEE Transactions on Mobile Computing**, early access, 1-14. DOI: 10.1109/TMC.2026.3697839.

## TL;DR

A demand-aware smart-city UAV-MEC deployment model where a control center flexibly allocates multiple UAVs across heterogeneous service areas instead of assigning a fixed number per area. The paper formulates joint UAV deployment, user association, bandwidth allocation, and computing-resource allocation as a constrained bi-objective optimization problem over energy and delay, then solves it with a constraint-guided multi-objective evolutionary algorithm.

## Problem

Fixed multi-UAV allocation can waste fleet capacity in low-demand areas while under-serving high-demand areas. The paper targets a multi-area MEC setting where regional user density, task sizes, and area radii differ. The objective is to minimize normalized total energy consumption and average user task-completion delay under deployment, association, resource-capacity, energy-budget, and delay constraints.

## System model

- **Fleet / areas:** M UAVs serve N ground service areas, with M > N so high-demand areas can receive multiple UAVs.
- **Deployment:** each deployed UAV flies from a control center to one area, maintains safe separation, and operates within its assigned service area.
- **Communication:** users offload tasks to associated UAVs over OFDMA air-to-ground links with probabilistic LoS channel modeling.
- **Computing:** UAVs allocate bandwidth and CPU cycles to associated users; total user delay includes UAV flight time, uplink transmission, and computing time.
- **Energy:** each UAV's modeled energy includes weighted round-trip flight and hovering energy plus offloading and computing energy.

## Method

The decision vector encodes UAV-to-area assignment, UAV positions, bandwidth allocation, CPU allocation, and user-UAV association. The proposed CMOEA maintains two populations and uses constraint-domination plus adaptive epsilon selection. Its key mechanism is constraint-guided solution reconstruction (CGSR), which repairs infeasible offspring by rebuilding area coverage, UAV positions, nearest-UAV associations, and resource allocations before evolutionary selection.

## Key findings

- Regional-demand experiments show that low-demand areas can stabilize with **1 to 3 UAVs**, while high-demand / large-task areas need roughly **5 to 7 UAVs** for comparable energy-delay performance.
- The algorithm generates energy-oriented, balanced, and delay-oriented Pareto solutions, allowing a control center to trade energy against service delay.
- Across CMOP1, CMOP2, and CMOP3, the proposed algorithm reports the lowest IGD and highest HV among five compared CMOEAs.
- The parse reports that MSCEA and MOEA/D-CDP fail to find feasible solutions on CMOP2 and CMOP3, while CMOEA-TS fails on CMOP3; the proposed reconstruction mechanism remains effective as problem scale increases.

## Limitations / future work

The paper is simulation-based. The conclusion names dynamic MEC scenarios with time-varying user demands, lower-runtime algorithms, and fairness-aware objective formulations as future research directions.

## Relation to the corpus

This source extends the Peng/Huang [[constrained-multi-objective-evolutionary-algorithm]] lineage from per-task or per-path UAV-MEC optimization toward fleet-level, multi-area demand provisioning. It sits near [[peng-2024-energy-time-uav-its]] and [[huang-2023-mu-aec-task-energy]] methodologically, but the decision layer is higher: how many UAVs each area receives, where they deploy, and how each area's users are associated and provisioned. It also sharpens the [[load-balancing-uav-mec]] theme by making regional heterogeneity explicit.

## Raw artifacts

- `raw/sources/Demand-Aware Multi-Area Multi-UAV Empowered Mobile Edge Computing A Joint Energy and Delay Optimization/Demand-Aware Multi-Area Multi-UAV Empowered Mobile Edge Computing A Joint Energy and Delay Optimization.md`
- Original PDF and extracted figures (`images/`) in the same folder.
