---
type: synthesis
title: "UAV energy replenishment and service continuity"
tags: [synthesis, uav-energy, service-continuity, uav-charging, battery-swapping, uav-replacement]
related:
  - "[[uav-charging-scheduling]]"
  - "[[battery-swapping-uav-mec]]"
  - "[[in-flight-uav-energy-replenishment]]"
  - "[[uav-substitution-relaying]]"
  - "[[persistent-emergency-uav-swarm-service]]"
  - "[[stateful-edge-microservice-migration]]"
  - "[[laser-power-transfer]]"
  - "[[dynamic-programming-battery-station-insertion]]"
  - "[[parallel-cooperative-uav-charging]]"
  - "[[liu-2026-jppo-en-convntm]]"
  - "[[shi-2025-aoi-energy-replenishment-multiuav]]"
  - "[[ma-2025-adrl-si-uav-charging-coverage]]"
  - "[[zhu-2026-hab-mappo-target-search]]"
  - "[[zhang-2022-solar-charging-uav-iot]]"
  - "[[yang-2026-udi-docking-point-charging]]"
  - "[[wu-2026-parallel-cooperative-charging]]"
  - "[[wang-2023-multi-uav-dynamic-demand-charging]]"
  - "[[chang-2026-data-offloading-energy-constraints]]"
  - "[[ye-2026-flight-speed-battery-swapping]]"
  - "[[song-2024-k-coverage-uav-recharging]]"
  - "[[arribas-not-in-parse-uav-resupply-scheduling]]"
  - "[[liu-2026-usp-nfrp-emergency-communication]]"
  - "[[zhang-2022-uav-relay-substitution]]"
  - "[[zhu-2022-aerial-refueling-uav-charging]]"
  - "[[yan-2025-in-flight-uav-charging-distance]]"
  - "[[li-2026-battery-mule-uav-swarm-scheduling]]"
  - "[[gupta-not-in-parse-uav-replacement]]"
  - "[[li-2026-two-timescale-uav-replacement-hap]]"
  - "[[ye-2023-seamless-service-handover-uav-mec]]"
  - "[[frejo-martin-2025-uav-stateful-microservice-live-migration]]"
  - "[[zhang-2025-kubespt-stateful-pod-migration]]"
  - "[[belmekki-2022-networked-tethered-flying-platforms]]"
created: 2026-11-03
updated: 2026-11-03
---

# UAV energy replenishment and service continuity

Every UAV source on this page starts from the same limit: a battery-powered UAV cannot serve indefinitely. The sources differ on two questions. Where does the new energy come from, and what happens to the users, data collection, or hosted computation while a UAV is refilling? This page maps the corpus along those two axes and then along the decision layer each source optimizes. The table rows summarize each paper's own abstract and model; the grouping and the gaps are cross-source inference.

## Roster

| Source | Energy path | Service while a UAV refills | Decision optimized | Method | Reported evaluation |
|---|---|---|---|---|---|
| [[liu-2026-jppo-en-convntm]] | Return to a charging station | Paused for that UAV; the objective weighs data collection, fairness, and energy | Charging indicator, trajectory, and offloading | j-PPO with a discrete charging head | Simulation; service continuity named as a target |
| [[shi-2025-aoi-energy-replenishment-multiuav]] | UAVs recharge at stations and power sensor nodes by WPT | Paused for the recharging UAV | Flight, sensor association, recharging | VDN and QMIX on a POMDP | Simulation against baselines |
| [[ma-2025-adrl-si-uav-charging-coverage]] | Return to a station | Replacement and charging kept near the station so service is not interrupted | Adaptive charging with coverage fairness | MOPSO-assisted DRL with a survival incentive | Simulation |
| [[zhu-2026-hab-mappo-target-search]] | Laser charging from the ground | A UAV either searches or charges in each offloading subslot | Search-or-charge choice, trajectory, offloading | Heuristic-embedded MAPPO | Simulation |
| [[zhang-2022-solar-charging-uav-iot]] | On-board solar plus charging stations | Single UAV; outage avoidance enters the trajectory | Trajectory, including charging-station visits | On-policy and off-policy RL | Simulation |
| [[yang-2026-udi-docking-point-charging]] | Docking points on traffic lights, street lamps, and base stations | Not modeled; queueing delay at docks is | Dock deployment and multi-UAV access | HUDD layout plus convex relaxation and rounding | Simulation on urban datasets |
| [[wu-2026-parallel-cooperative-charging]] | Shared charging facilities | Not modeled | Charging groups and facility assignment | Approximation algorithms (UPMSP, set covering) | Up to 59.81% lower total cost than benchmarks |
| [[wang-2023-multi-uav-dynamic-demand-charging]] | Station visits inserted into routes | Demands are served when a UAV arrives | Swarm path planning over hotspots and stations | Dynamic program, ILP on a state DAG, approximation ratios | Theory plus simulation |
| [[chang-2026-data-offloading-energy-constraints]] | Battery replacement at battery stations | Single UAV; replacement detours add completion time | Visiting order and station insertion | TSP with precedence, then dynamic-programming insertion | Simulation |
| [[ye-2026-flight-speed-battery-swapping]] | Battery swapping at the base station that hosts the MEC server | Single patrol UAV; swaps add cost and detours | Flight speed, swapping, and offloading | Mixed-integer convex reformulation plus an ATC heuristic | Simulation |
| [[song-2024-k-coverage-uav-recharging]] | Solar-powered charging platforms | Coverage held by assigning other UAVs to monitoring points | UAV-to-platform or point assignment per slot | MILP, MPC, and MCTS | MPC and MCTS reach about 81.04% and 67.07% of the MILP optimum |
| [[arribas-not-in-parse-uav-resupply-scheduling]] | Generic resupply station (swap, recharge, or refuel) | Permanent coverage by rotation | Fleet size and resupply schedule | HORR (exact for equidistant locations) and PHERR (heterogeneous case) | Analysis and numerical study |
| [[liu-2026-usp-nfrp-emergency-communication]] | Rotation of replacement UAVs | Continuous multi-hop connectivity by periodic rotation | UAV-target association, trajectories, backhaul tree | PRP, DTBL, and a max-min ant system | Up to 30.9% fewer UAVs than baselines |
| [[zhang-2022-uav-relay-substitution]] | Successive relay UAVs | Relay link extended by substitution | Relay trajectories and transmit powers | Block coordinate ascent with SCA | Simulation |
| [[zhu-2022-aerial-refueling-uav-charging]] | Charging UAVs transfer power to mission UAVs in flight | Mission UAVs keep working | Charging-UAV routes and charging process | DRL for single and multiple charging UAVs | Simulation; mission time minimized |
| [[yan-2025-in-flight-uav-charging-distance]] | UAV-to-UAV wireless charging | Not a scheduling paper; link-level design | Charging distance under a minimum rate | Analysis of aligned and moving schemes | Optimal distance lies in the Fresnel zone |
| [[li-2026-battery-mule-uav-swarm-scheduling]] | Battery mules swap batteries in the air | Recipients keep serving | Recipient assignment and mule tours | Greedy load balancing plus a time-constrained TSP heuristic | At least 30.70% higher average continuous service ratio than benchmarks |
| [[gupta-not-in-parse-uav-replacement]] | Depleted UAV returns; charged UAV replaces it | Coverage continuity during the swap | 3-D trajectories and user resource shares | Alternating optimization with SCA | Numerical comparison with benchmarks |
| [[li-2026-two-timescale-uav-replacement-hap]] | Depot dispatches a replacement UAV | Devices offload to the HAP or wait for the replacement | Slow-timescale trajectory and replacement; fast-timescale delegation | Two coupled stochastic games solved by RL (UTRTD) | Simulation against MADDPG and fixed strategies |
| [[ye-2023-seamless-service-handover-uav-mec]] | Fully charged UAV dispatched from a station | Users, data, models, and task states move before the old UAV leaves | Retrieval station, launch station, launch time | Sort-by-battery, nearest-feasible-station dispatch rule | Event-driven simulation |
| [[frejo-martin-2025-uav-stateful-microservice-live-migration]] | Node replacement in a UAV network | Pre-copy live migration of stateful microservices | Architecture, not an optimization | Digital twin, swarm manager, image server | Evaluation left to future work |
| [[belmekki-2022-networked-tethered-flying-platforms]] | Continuous power through a tether | No refill interruption by design | Survey | Survey | Survey |

## Axis 1: where the energy comes from

- **Return to a ground facility.** Most sources return the UAV to a station that charges it ([[liu-2026-jppo-en-convntm]], [[shi-2025-aoi-energy-replenishment-multiuav]], [[ma-2025-adrl-si-uav-charging-coverage]]) or swaps its battery ([[ye-2026-flight-speed-battery-swapping]], [[chang-2026-data-offloading-energy-constraints]]). [[arribas-not-in-parse-uav-resupply-scheduling]] keeps the mechanism generic and models only a resupply time.
- **Denser or shared infrastructure.** [[yang-2026-udi-docking-point-charging]] reuses urban street furniture as docks, and [[wu-2026-parallel-cooperative-charging]] schedules more UAVs than there are facilities. Both optimize the infrastructure side and leave the mission side out.
- **Ambient or beamed energy.** [[zhang-2022-solar-charging-uav-iot]] and the solar platforms in [[song-2024-k-coverage-uav-recharging]] add harvested energy, and [[zhu-2026-hab-mappo-target-search]] uses [[laser-power-transfer]] from the ground.
- **Energy delivered in the air.** [[zhu-2022-aerial-refueling-uav-charging]] and [[yan-2025-in-flight-uav-charging-distance]] use wireless power between UAVs, and [[li-2026-battery-mule-uav-swarm-scheduling]] swaps batteries in the air. These are the [[in-flight-uav-energy-replenishment]] branch.
- **No refill at all.** Tethered platforms in [[belmekki-2022-networked-tethered-flying-platforms]] draw continuous power from the ground, at the cost of mobility.

## Axis 2: what happens to service during a refill

The sources fall into four groups. The grouping is this page's inference from each paper's model.

1. **Accept the gap and price it.** The learned schedulers ([[liu-2026-jppo-en-convntm]], [[shi-2025-aoi-energy-replenishment-multiuav]], [[zhu-2026-hab-mappo-target-search]], [[zhang-2022-solar-charging-uav-iot]]) let a UAV stop serving while it charges and let the reward decide when the loss is worth it. [[ma-2025-adrl-si-uav-charging-coverage]] starts from the same tension (charging trips interrupt service, and long-distance replacement wastes energy) but resolves it differently, by replacing low-energy UAVs only near the charging station so that service is not interrupted.
2. **Avoid the gap by not leaving.** In-flight charging and battery mules keep the working UAV in place. [[li-2026-battery-mule-uav-swarm-scheduling]] is the only source here that reports a continuity metric for this choice, the average continuous service ratio.
3. **Cover the gap with fleet rotation.** [[arribas-not-in-parse-uav-resupply-scheduling]], [[liu-2026-usp-nfrp-emergency-communication]], [[song-2024-k-coverage-uav-recharging]], and [[zhang-2022-uav-relay-substitution]] size or rotate a fleet so a location, a coverage count, or a relay link is always served. Their objectives are fleet size, coverage lifetime, or throughput, not per-user downtime.
4. **Cover the gap with replacement and handover.** [[gupta-not-in-parse-uav-replacement]] keeps users' throughput up while a replacement flies in. [[li-2026-two-timescale-uav-replacement-hap]] lets devices choose between the HAP (no waiting, longer transmission) and the arriving replacement UAV (waiting, shorter transmission). [[ye-2023-seamless-service-handover-uav-mec]] launches the replacement early so that users and task state move before the old UAV departs, and [[frejo-martin-2025-uav-stateful-microservice-live-migration]] proposes pre-copy live migration for that state transfer.

## Axis 3: the decision layer and its guarantees

- **Combinatorial schedules with guarantees.** [[arribas-not-in-parse-uav-resupply-scheduling]] proves HORR uses the minimum number of UAVs for equidistant locations and shows the heterogeneous case is NP-hard. [[wang-2023-multi-uav-dynamic-demand-charging]] gives approximation ratios for swarm routing with station visits, and [[wu-2026-parallel-cooperative-charging]] builds on approximation algorithms for parallel-machine scheduling and set covering.
- **Exact or near-exact formulations with heuristics for scale.** [[song-2024-k-coverage-uav-recharging]] needs non-causal energy-arrival knowledge for its MILP and reports how close MPC and MCTS get. [[ye-2026-flight-speed-battery-swapping]] reformulates to a mixed-integer convex problem on an extended graph. [[chang-2026-data-offloading-energy-constraints]] inserts stations with [[dynamic-programming-battery-station-insertion]].
- **Continuous optimization.** [[gupta-not-in-parse-uav-replacement]] and [[zhang-2022-uav-relay-substitution]] use SCA-based trajectory and power design, and [[yang-2026-udi-docking-point-charging]] uses convex relaxation with rounding for dock access.
- **Learned per-slot policies.** The schedulers in group 1 above and [[zhu-2022-aerial-refueling-uav-charging]] use DRL or MARL. [[li-2026-two-timescale-uav-replacement-hap]] separates a slow replacement timescale from a fast task-delegation timescale and proves that a Nash equilibrium exists.
- **Rules without optimality analysis.** [[ye-2023-seamless-service-handover-uav-mec]] uses a sort-by-battery, nearest-feasible-station dispatch rule and states its objective only in words, and [[frejo-martin-2025-uav-stateful-microservice-live-migration]] is an architecture without a reported evaluation.

## Where the application state goes

Among the UAV sources on this page, only [[ye-2023-seamless-service-handover-uav-mec]] and [[frejo-martin-2025-uav-stateful-microservice-live-migration]] treat the computation hosted on the UAV as state that must move. The other sources model service as coverage, throughput, AoI, or task completion, so a replacement UAV can serve as soon as it arrives. [[ye-2023-seamless-service-handover-uav-mec]] reduces state transfer to a handover time inside a reachability check.

The corpus has no measured state-transfer time on UAV hardware. One measured reference is a three-node Kubernetes testbed: [[zhang-2025-kubespt-stateful-pod-migration]] reports 10.76 s of downtime and 79.81 s of total migration time for an 8 GB Redis pod over 3 Gbps links. Other edge testbeds, such as the Podman/CRIU and OpenStack experiments of the Calagna et al. papers, are covered in [[stateful-edge-microservice-migration]]. A UAV link is likely slower than that testbed, so a launch-time rule that budgets handover time would need margins measured on the actual link. This is inference, not a result of any source.

## Disagreements and tensions

- **Continuity costs fleet size.** [[ye-2023-seamless-service-handover-uav-mec]] reports 28 UAVs used with handover versus 24 without, and more frequent response-time spikes because replacements launch early. No source trades handover downtime against fleet size as a cost: [[arribas-not-in-parse-uav-resupply-scheduling]] and [[liu-2026-usp-nfrp-emergency-communication]] minimize fleet size subject to gap-free coverage or connectivity, and [[ye-2023-seamless-service-handover-uav-mec]] reduces downtime without optimizing fleet size.
- **Near-station versus long-distance replacement.** [[ma-2025-adrl-si-uav-charging-coverage]] limits replacement to UAVs near the charging station to save flight energy, while [[gupta-not-in-parse-uav-replacement]] and [[ye-2023-seamless-service-handover-uav-mec]] fly a replacement from a station to wherever it is needed. The two choices have not been compared on the same scenario.
- **Who absorbs the gap.** [[li-2026-two-timescale-uav-replacement-hap]] gives devices a second tier (the HAP) during replacement. The single-tier sources must either wait or pre-position a replacement.

## Limitations of the evidence

- Nearly every row is simulation-only. [[frejo-martin-2025-uav-stateful-microservice-live-migration]] has no evaluation, and [[belmekki-2022-networked-tethered-flying-platforms]] is a survey.
- The reported gains are against each paper's own baselines and metrics, so the percentages in the roster are not comparable with one another.
- No source compares station charging, battery swapping, in-flight replenishment, and replacement within one scenario.

## Open questions

- How should a launch-time rule budget for state transfer when the migrated state is large or the link is weak? The corpus has the dispatch rule ([[ye-2023-seamless-service-handover-uav-mec]]) and data-center migration measurements ([[zhang-2025-kubespt-stateful-pod-migration]]) but no joint model.
- When does airborne replenishment ([[li-2026-battery-mule-uav-swarm-scheduling]]) beat replacement with handover in UAVs used per unit of service time?
- Can the two-tier fallback in [[li-2026-two-timescale-uav-replacement-hap]] reduce the extra UAVs that early dispatch needs in [[ye-2023-seamless-service-handover-uav-mec]]?

## See also

- [[uav-charging-scheduling]], [[battery-swapping-uav-mec]], and [[in-flight-uav-energy-replenishment]] define the replenishment mechanisms.
- [[uav-substitution-relaying]] and [[persistent-emergency-uav-swarm-service]] cover rotation-based continuity.
- [[stateful-edge-microservice-migration]] covers the state-transfer side.
- [[hierarchical-aerial-mec-design-space]] covers UAV and HAP hierarchical MEC more broadly.
