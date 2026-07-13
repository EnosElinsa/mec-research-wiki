---
type: source
title: "SLIM+: Jointly Optimizing EIV Placement and UAV Fleet Sizing for Deadline-Driven Tasks"
authors: ["Jianping Huang", "Feng Shan", "Junzhou Luo"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3690854"
venue: "IEEE Transactions on Mobile Computing (early access; accepted author version)"
tags: [source, edge-intelligent-vehicle, multi-uav, fleet-sizing, facility-location, deadline-scheduling, dynamic-programming, approximation-algorithm, deployment-cost]
related:
  - "[[edge-intelligent-vehicle]]"
  - "[[joint-eiv-placement-uav-fleet-sizing]]"
  - "[[mobile-edge-computing]]"
  - "[[uav-data-collection]]"
  - "[[uav-trajectory-control]]"
  - "[[rotary-wing-propulsion-energy-model]]"
  - "[[mixed-integer-nonlinear-programming]]"
  - "[[energy-latency-tradeoff]]"
  - "[[two-stage-decomposition]]"
  - "[[task-offloading]]"
created: 2026-07-14
updated: 2026-07-14
---

# SLIM+: Jointly Optimizing EIV Placement and UAV Fleet Sizing for Deadline-Driven Tasks

## Citation

Huang, J., Shan, F., & Luo, J. (2026). *SLIM+: Jointly Optimizing EIV Placement and UAV Fleet Sizing for Deadline-Driven Tasks*. **IEEE Transactions on Mobile Computing**, early access, accepted author version. DOI: 10.1109/TMC.2026.3690854.

> **Publication status.** The supplied accepted-author-version manuscript is numbered pages 1-16. Those numbers are manuscript pagination, not a final journal page range. The embedded `PP/99` fields are placeholders; no final volume, issue, or publication pages are available in the parse.

## TL;DR

Jointly places mobile edge-support vehicles along a linear task route and chooses each route segment's UAV fleet size, common speed, and deadline-feasible schedule. An outer dynamic program evaluates segment boundaries, while exact or approximation scheduling handles the inner fleet-sizing problem. The method is centralized, offline, simulation-tested, and approximate when the scalable inner solver is used.

## Problem and system model

The paper defines an [[edge-intelligent-vehicle]] as both a UAV launch, recovery, and recharge hub and an edge-processing node. Multiple EIVs are selected at task locations along a straight route and partition it into independent segments. Identical UAVs start at a segment's initial EIV, fly forward without turning back, collect assigned task data in route order, offload it to the nearer endpoint EIV, and finish at the ending EIV.

Each task has a route location, data volume, acquisition rate, and hard completion deadline. Service time includes acquisition, offloading, and EIV processing. UAV energy combines speed-dependent rotary-wing flight energy with hovering and acquisition energy. All UAVs in a segment use one selected speed, and each EIV has setup time, processing and communication parameters, deployment cost, and a fleet-support limit.

The [[joint-eiv-placement-uav-fleet-sizing]] objective minimizes EIV deployment cost plus UAV fleet cost while choosing EIV locations, segment speeds, fleet sizes, task assignments, and service start times. Constraints enforce forward route flow, one service per task, indivisible tasks, deadline completion, UAV energy, EIV capacity, setup time, and speed bounds. The resulting formulation is a [[mixed-integer-nonlinear-programming|mixed-integer nonlinear problem]].

## Method

For a fixed segment and speed, the paper subtracts setup and travel time from each task deadline to obtain an effective scheduling deadline, and reserves flight energy to obtain a service-duration capacity.

1. **SLIM-DP:** a Boolean dynamic program assigns the first $j$ tasks over a sorted UAV-workload vector. Sorting removes permutations of identical UAVs, and bisection over fleet size finds the minimum feasible value. This exact solver is intended for small instances because its state space grows rapidly with fleet size.
2. **SLIM-AG:** tasks are first sorted by nondecreasing deadline slack and assigned in route-compatible order while ignoring energy capacity. Workloads are then split at the service-duration capacity, and fractionally split boundary tasks are moved to new UAVs to restore indivisibility. The paper proves a $2(2\alpha+1)$ approximation, where $\alpha=\lceil d'_{\max}/d'_{\min}\rceil$, and $O(n^2)$ time.
3. **DP-AG:** an outer dynamic program considers each possible final segment, adds its EIV and UAV costs, and reconstructs the selected boundaries from predecessor states. For every candidate segment it prunes the feasible speed interval, searches a discrete speed grid, and calls the inner SLIM solver. Its stated complexity is $O(n^4(v_{\max}-v_{\min})/\Delta v)$.

The mission planner is centralized and offline: it receives the complete task and system model, computes placements and schedules, and then sends EIV commands and UAV flight plans.

## Key findings

- For small instances, Fig. 7 and its discussion say SLIM-AG uses about **15% more UAVs** than exact SLIM-DP, but the same text gives a fleet-size ratio of approximately **1.18**, which implies about 18%. The inconsistency is preserved rather than resolved.
- In large simulations, the paper reports that SLIM-AG reduces average fleet size by **21.3%** relative to NF-GPA, GBF, and MEFN. This comparison spans the paper's simulated task, deadline, and energy settings.
- Across Fig. 9 placement scenarios, DP-AG is reported to reduce deployment cost by **19.5%-29.5%** relative to the next-best placement baseline. The same figure discussion reports 66.5% lower cost than Uniform-K for a bimodal task layout and 33.4% over the best baseline when the EIV/UAV cost ratio is 4. These are figure-derived simulation comparisons.
- Fig. 10 and the detailed results text report **up to 21.9%** lower end-to-end deployment cost than Greedy-GBF. At 700 tasks, DP-AG takes about 25 s, while the compared baselines take under 5 s. The abstract instead describes 21.9% as an average, so the comparator-qualified “up to” result is used here.
- In the Shenzhen transport-derived case in Fig. 12, a 6,000 m route is divided by **8 EIVs** into 8 segments, and segment 5 uses **6 UAVs** whose plotted Gantt schedule meets the modeled deadlines. These values are figure- and caption-derived planner outputs, not a field deployment or hardware experiment.

The simulation range includes 200-800 tasks, routes of 5-30 km, average task data volumes of 200-500 MB, EIV processing rates of 50-250 Mbps, and EIV/UAV cost ratios of 2-10. The evaluated setup uses homogeneous pre-deployed EIVs with zero setup time and a 0.5 m/s speed-search increment.

## Limitations

The planner assumes a static, fully known task set, data volumes, deadlines, costs, service times, and energy model. It is centralized and offline; dynamic task arrivals and service times are left for future online adaptation. Routes are linear, UAVs cannot turn back, placements are restricted to task locations, and all UAVs in a segment share one speed. Nonlinear routes and heterogeneous UAV/EIV capabilities are future work.

Segments are modeled independently. The formulation does not expose EIV compute queues, simultaneous-offloading contention, finite processing concurrency, failures, uncertain channels or task durations, weather, collision avoidance, or cross-segment fleet repositioning. Simulation assumes zero EIV setup time and describes the EIVs as pre-deployed, which weakens evidence for the modeled mobile-placement process.

Speed is selected on a discrete grid, so speed optimality is relative to that grid. The outer recurrence is exact for the segment costs it receives, but DP-AG normally uses approximate SLIM-AG inside each segment. It therefore does not establish a global optimum for the original continuous SLIM+ problem. The paper's malformed comparison table, conflicting 15% versus 1.18 small-instance gap, and average-versus-up-to 21.9% wording should not be treated as mutually validating evidence.

## Relation to the corpus

This source combines [[mobile-edge-computing]] with air-ground logistics: UAVs perform [[uav-data-collection]] and then [[task-offloading|offload]] data to EIVs for processing, while [[rotary-wing-propulsion-energy-model]] creates an [[energy-latency-tradeoff]] between faster deadline completion and residual service energy. The outer placement and inner scheduling structure resembles [[two-stage-decomposition]], but its objective is deployment cost and fleet size rather than makespan.

## Raw artifacts

- Parse: `raw/sources/SLIM_Jointly_Optimizing_EIV_Placement_and_UAV_Fleet_Sizing_for_Deadline-Driven_Tasks/SLIM_Jointly_Optimizing_EIV_Placement_and_UAV_Fleet_Sizing_for_Deadline-Driven_Tasks.md`
- Origin PDF: `raw/sources/SLIM_Jointly_Optimizing_EIV_Placement_and_UAV_Fleet_Sizing_for_Deadline-Driven_Tasks/SLIM_Jointly_Optimizing_EIV_Placement_and_UAV_Fleet_Sizing_for_Deadline-Driven_Tasks.pdf`
- Figures: `raw/sources/SLIM_Jointly_Optimizing_EIV_Placement_and_UAV_Fleet_Sizing_for_Deadline-Driven_Tasks/images/`
