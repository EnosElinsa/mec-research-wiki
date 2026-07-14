---
type: source
title: "UAV Trajectory Planning for IoT Data Collection and Offloading With Energy Constraints"
authors: ["Teng-Wu Chang", "Jang-Ping Sheu", "Nguyen Van Cuong"]
year: 2026
url: "https://doi.org/10.1109/TGCN.2025.3592263"
venue: "IEEE Transactions on Green Communications and Networking (IEEE TGCN), vol. 10, pp. 573-584"
tags: [source, uav-data-collection, data-offloading, energy-constrained-routing, battery-swapping, pickup-and-delivery, mixed-integer-linear-programming, dynamic-programming]
related:
  - "[[many-to-one-pickup-and-delivery]]"
  - "[[dynamic-programming-battery-station-insertion]]"
  - "[[mixed-integer-linear-programming]]"
  - "[[uav-data-collection]]"
  - "[[uav-trajectory-control]]"
  - "[[battery-swapping-uav-mec]]"
  - "[[samir-2020-time-constrained-data-collection]]"
  - "[[li-2023-energy-constrained-uav-data-collection]]"
  - "[[ye-2026-flight-speed-battery-swapping]]"
created: 2026-07-14
updated: 2026-07-14
---

# UAV Trajectory Planning for IoT Data Collection and Offloading With Energy Constraints

## Citation

Chang, T.-W., Sheu, J.-P., & Cuong, N. V. (2026). *UAV Trajectory Planning for IoT Data Collection and Offloading With Energy Constraints*. **IEEE Transactions on Green Communications and Networking, 10**, 573-584. DOI: 10.1109/TGCN.2025.3592263. The article was published online in July 2025 and appears in the final 2026 volume.

## TL;DR

A battery-limited UAV must collect data from every IoT device, deliver each payload to its predetermined edge server, visit battery-replacement stations when needed, and return to its depot. The paper formulates an exact [[mixed-integer-linear-programming]] model and proposes a three-stage heuristic that constructs a precedence-feasible visit order, inserts battery stations by dynamic programming for that fixed order, and iteratively coordinates the two decisions.

## Problem

Each edge server receives data from a group of IoT devices, so every pickup in the group must precede that server's delivery visit. The UAV minimizes total completion time, including flight and constant battery-replacement delays, while satisfying these [[many-to-one-pickup-and-delivery]] constraints and battery feasibility.

Here “offloading” means physically carrying collected IoT data to predetermined edge servers. It is not computation-offloading optimization: the paper does not choose local versus edge execution, server assignment, CPU allocation, or offloading ratios.

## System model

- One fixed-speed, fixed-altitude UAV starts and ends at a depot and visits every IoT device and edge server exactly once.
- Multiple devices may map to one edge server. Each server must be visited after all devices assigned to it.
- The UAV hovers above communication endpoints. Transfer time is fixed by payload and assumed LoS rate; it is independent of visit order but still consumes hover energy.
- Flight and hover consume constant powers. A battery-station visit resets energy to full capacity after a fixed replacement delay.
- Physical battery stations may be revisited through dummy nodes, expanding the exact formulation to at most `(L+1)(N+1)` nodes for `N` service nodes and `L` stations.

## Method

The exact [[mixed-integer-linear-programming|MILP]] uses route-edge binaries, MTZ visit-order variables, pickup-before-delivery precedence constraints, arrival/departure energy states, flow conservation, and dummy battery-station visits. It is NP-hard and becomes impractical at scale; the paper notes that 100 service nodes and four stations can expand to 505 modeled nodes.

The time minimization trajectory planning heuristic has three stages:

1. Solve or approximate a TSP over devices, then greedily insert every edge server after the last pickup in its group at the location with the smallest added distance.
2. Apply [[dynamic-programming-battery-station-insertion]] to choose station identities and insertion positions subject to flight-plus-hover energy feasibility.
3. Split the feasible route at station visits, improve the service-node order within segments, remove and reinsert stations, and repeat while completion time decreases.

The dynamic program is optimal only for the fixed device/server order supplied to stage 2 under the stated energy and replacement model. It does not globally optimize the service order, and the complete heuristic has neither a global-optimality claim nor an approximation ratio. Stage 3's monotonic improvement establishes termination behavior, not convergence to the MILP optimum.

## Key findings

- Simulations average 200 random placements and use 100 service nodes by default in an `8000 m x 8000 m` area, a 9:1 device/server ratio, three stations, a `2.7 kJ` battery, `10 m/s` speed, and `240 s` replacement time.
- TMTP reports lower completion time than Greedy, ACS-SA, Greedy-2opt, and ACS-SA-2opt across the plotted node-count, replacement-time, station-count, device/server-ratio, and battery-capacity sweeps.
- Completion time rises with more service nodes and longer replacement delays, and falls with more stations, fewer precedence constraints, and larger battery capacity in the tested settings.
- Additional stations show diminishing benefit in the dense-station cases and reduce the average number of replacements by shortening detours to replenishment.
- Greedy is fastest but gives the poorest completion-time objective; TMTP runs substantially faster than the ant-colony variants in the reported runtime experiment.

## Limitations

The study is simulation-only and assumes known static node/station positions and assignments, fixed speed and altitude, direct hovering over endpoints, a fixed LoS rate, equal collection/delivery rates, negligible communication energy, constant propulsion powers, and instantaneous full battery replacement after a fixed delay. It serves every device and does not optimize admission, server assignment, radio resources, power, speed, station placement, or computation. The fixed-order scope of stage 2 means a poor service order can remain globally poor even when station insertion is optimal for that order.

## Relation to the corpus

The paper extends battery-limited [[uav-data-collection]] from depot-returning selection in [[li-2023-energy-constrained-uav-data-collection]] to mandatory pickup/delivery precedence and repeated replenishment. It complements [[ye-2026-flight-speed-battery-swapping]], which jointly treats speed, swaps, and computation offloading, whereas this work fixes speed and routes carried data to predetermined servers. Compared with [[samir-2020-time-constrained-data-collection]], it replaces hard-deadline admission and slot-level spectrum allocation with all-node routing, pickup-before-delivery order, and battery-station insertion.

## Raw artifacts

- Parse: `raw/sources/UAV_Trajectory_Planning_for_IoT_Data_Collection_and_Offloading_With_Energy_Constraints/UAV_Trajectory_Planning_for_IoT_Data_Collection_and_Offloading_With_Energy_Constraints.md`
- Origin PDF: `raw/sources/UAV_Trajectory_Planning_for_IoT_Data_Collection_and_Offloading_With_Energy_Constraints/UAV_Trajectory_Planning_for_IoT_Data_Collection_and_Offloading_With_Energy_Constraints.pdf`
- Figures: `raw/sources/UAV_Trajectory_Planning_for_IoT_Data_Collection_and_Offloading_With_Energy_Constraints/images/`
