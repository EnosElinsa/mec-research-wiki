---
type: synthesis
title: "Constraint regimes in UAV data collection"
tags: [synthesis, uav-data-collection, constraints, trajectory, freshness, energy]
related:
  - "[[zhu-2023-aoi-transformer-trajectory]]"
  - "[[samir-2020-time-constrained-data-collection]]"
  - "[[chang-2026-data-offloading-energy-constraints]]"
  - "[[qi-2026-ocma-ddqn-data-collection]]"
  - "[[zhao-2026-uav-carrier-vcs]]"
  - "[[li-2023-energy-constrained-uav-data-collection]]"
  - "[[fu-2026-dubins-uav-data-collection]]"
  - "[[guo-2026-spatiotemporal-information-quality-ugrnet]]"
  - "[[generalized-traveling-salesman-problem]]"
  - "[[hovering-disk-data-collection]]"
  - "[[transformer-weighted-a-star-trajectory-planning]]"
  - "[[deadline-constrained-uav-data-collection]]"
  - "[[branch-reduce-and-bound]]"
  - "[[many-to-one-pickup-and-delivery]]"
  - "[[dynamic-programming-battery-station-insertion]]"
  - "[[mixed-integer-linear-programming]]"
  - "[[opportunistic-cooperative-multi-uav-ddqn]]"
  - "[[lstm-interruption-compensation]]"
  - "[[experience-value-circles]]"
  - "[[attentive-memory-integrated-information-exchange]]"
  - "[[hidden-state-sharing-marl]]"
  - "[[mutual-policy-divergence-exploration]]"
  - "[[energy-constrained-uav-data-collection-orienteering]]"
  - "[[heterogeneous-uav-fleet]]"
  - "[[spatiotemporal-information-quality]]"
  - "[[age-of-information]]"
  - "[[design-recipe-multi-uav-mec]]"
  - "[[safety-and-robustness-mechanisms-in-mec]]"
created: 2026-07-14
updated: 2026-07-14
---

# Constraint regimes in UAV data collection

## Scope and constraint taxonomy

The eight papers use “constraint” for different objects: a feasible contact region, a packet lifetime, a precedence relation, a battery state, a communication graph, a vehicle kinematic envelope, or a probabilistic information bound. The distinction matters before choosing a solver. A hard constraint removes an action or route from the feasible set; a soft term changes a reward, penalty, or weighted objective; a reported guarantee belongs only to the model and assumptions that establish it.

| Source | Hard constraints and state limits | Soft or surrogate terms | Objective and horizon |
|---|---|---|---|
| [[zhu-2023-aoi-transformer-trajectory]] | Fixed altitude and speed, one SNR-feasible hovering point per cluster, a permutation visiting every cluster, and a return to the BS. | Distance versus uplink time is traded inside total AoI; propulsion energy is evaluated but not a displayed budget. | Minimize total AoI of packets over one closed collection tour; the sampled GTSP is finite after disk discretization. |
| [[samir-2020-time-constrained-data-collection]] | Each admitted device must receive its minimum service between its generation time and hard deadline; mission duration, fixed altitude, maximum per-slot displacement, and endpoint constraints apply. | The second-stage distance minimization preserves the admitted set; path-loss planning followed by slot-wise CSI repair is a practical surrogate. | Maximize the number of completely served devices, then shorten the route, over a fixed N-slot mission. |
| [[chang-2026-data-offloading-energy-constraints]] | Every IoT pickup precedes its designated edge-server delivery, service nodes are visited once, battery energy remains feasible, and the UAV returns to its depot. | Dynamic programming optimizes station insertion for a fixed service order; iterative refinement then changes within-segment service order and reinserts stations. | Minimize total completion time for one depot-returning mission with finite service nodes and stations. |
| [[li-2023-energy-constrained-uav-data-collection]] | A closed depot tour must satisfy one travel-plus-hover energy capacity; discretized hover locations and one-visit/subtour conditions define the route. | Marginal data per added energy is used for overlap cases; non-overlap instances admit metric-orienteering approximations. | Maximize collected bits, fully or partially, in one battery-limited tour. |
| [[qi-2026-ocma-ddqn-data-collection]] | Fixed-altitude grid actions, rate-threshold collection, no-fly/obstacle boundaries, and collision-triggered position resets constrain transitions; jammer parameters are fixed per episode as environment assumptions. | The game utility balances data against cooperation and energy costs; the DDQN reward additionally uses movement and collision penalties plus a landing bonus and remaining-energy term, so landing and residual energy are soft incentives rather than hard constraints. | Maximize decentralized data-collection utility over an episodic grid trajectory; tested swarms contain up to four UAVs. |
| [[zhao-2026-uav-carrier-vcs]] | UGV motion follows roads, UAVs use a flight/charge action, link-qualified messages gate observations, obstacles are unsafe, and active/inactive status enforces unequal decision durations. | Data ratio, geographic fairness, sensing expansion, and energy enter the efficiency objective or step rewards; overlap is reported separately as a coordination metric. | Maximize episode-level efficiency over T timeslots while UGVs collect data and UAVs discover PoIs. |
| [[fu-2026-dubins-uav-data-collection]] | Communication distance/throughput, obstacle avoidance, minimum turning radii, release/recovery geometry, and synchronized rendezvous are explicit. | BACS, DAWPRM, and trajectory elongation trade path length against waiting and recovery feasibility. | Produce Pareto mission-time/cluster-count trajectories in an offline release–collect–recover horizon. |
| [[guo-2026-spatiotemporal-information-quality-ugrnet]] | One-to-one region assignment and queue-stability assumptions constrain collection; DVPB is a modeled probabilistic bound rather than a packet-by-packet deadline. | A weighted temporal DVPB plus spatial Wasserstein index is optimized through task-completion ratios. | Minimize an aggregate information-quality index over long numerical runs; the source sweeps ratios rather than supplying a trajectory solver. |

This taxonomy keeps collected bits, AoI, delay violations, mission time, energy, fairness, overlap, and information quality as separate quantities. A “better” value in one row cannot be promoted to a cross-paper ranking.

## Energy, travel, and replenishment

[[li-2023-energy-constrained-uav-data-collection]] makes the energy budget the route feasibility boundary. Flying between hover cells and hovering to transfer data consume separate rates, so the controller chooses a subset and sojourn durations rather than visiting every sensor. The paper gives separately stated approximation results for its full- and partial-collection no-overlap variants; overlapping coverage makes residual rewards depend on previous visits, so the paper switches to greedy heuristics. Each guarantee is therefore conditional on its coverage/collection regime and discretization.

[[chang-2026-data-offloading-energy-constraints]] models a different endurance problem. Data must be physically carried from many pickups to predetermined servers, and a battery station can be revisited before the residual energy reaches its limit. Its MILP formulation uses dummy station nodes to represent possible repeated visits. The dynamic program is optimal for inserting stations after a fixed service order; the three-stage TMTP procedure has no whole-problem approximation ratio. This is a replenishment-and-precedence regime, not the same orienteering objective as Li.

In [[zhu-2023-aoi-transformer-trajectory]], propulsion and hover energy appear in the model and simulations, but the displayed optimization minimizes AoI rather than enforcing a battery budget. [[samir-2020-time-constrained-data-collection]] likewise leaves UAV/IoT energy consumption as future work while enforcing service deadlines. By contrast, [[qi-2026-ocma-ddqn-data-collection]] uses movement, data, cooperation, and collision terms together with a landing bonus and remaining-energy reward while retaining battery state, and [[zhao-2026-uav-carrier-vcs]] treats remaining energy in the episode efficiency and charge action. These reward/state treatments are not interchangeable with a hard route budget.

## Deadlines and freshness

[[samir-2020-time-constrained-data-collection]] uses a device-specific generation time and expiry deadline. A device counts only if its minimum service amount is completed inside that lifetime; the objective is admission count, not the age of partially served packets. The customized [[branch-reduce-and-bound]] procedure is global for the tolerance-qualified small formulation, while successive convex approximation is the scalable suboptimal path.

[[zhu-2023-aoi-transformer-trajectory]] assigns an age to every packet and sums the age accumulated until the UAV returns with the data. A hover point near a disk center improves rate but can lengthen flight; a boundary point can shorten flight while increasing collection time. The Transformer orders clusters and weighted A-star chooses a sampled point, producing a learned GTSP solution without a global-optimality or approximation-ratio result.

These are two freshness regimes: a continuous penalty on return-time age versus a hard admission window. [[age-of-information]] should therefore remain distinct from [[deadline-constrained-uav-data-collection]]. [[guo-2026-spatiotemporal-information-quality-ugrnet]] adds a third regime: a martingale-derived delay-violation probability bound is combined with Wasserstein spatial mismatch. It is neither AoI nor a per-device upload deadline, and its numerical interior optima do not establish a universal completion ratio.

## Connectivity, interruption, and adversarial robustness

In [[qi-2026-ocma-ddqn-data-collection]], jammers and buildings can interrupt UAV-to-UAV exchange and UAV-to-station collection. The opportunistic mechanism shares grid-map exploration and historical information such as obstacle-avoidance experience according to distance/value-circle gates. Communication/cooperation cost enters separately through the game utility. [[lstm-interruption-compensation]] predicts a neighbor's next action from recent positions, actions, and a local map during a short outage; a confidence filter falls back to the last valid state. The paper evaluates short interruptions and episode-wise static jammer configurations, not arbitrary outages or changing adversaries.

[[zhao-2026-uav-carrier-vcs]] addresses a different communication interface. [[attentive-memory-integrated-information-exchange]] sends link-qualified hidden representations, inactive-agent actions, and sequentially announced active actions while retaining per-agent memory across unequal UAV/UGV decision durations. [[mutual-policy-divergence-exploration]] adds inter-agent and inter-episode policy divergence so scouts and road-bound carriers avoid collapsing to redundant roles. Message-loss and latency experiments show graceful degradation in the simulated maps, but they do not prove safety or convergence under arbitrary delay.

The two mechanisms can be composed conceptually, but they operate at different layers: Qi imputes a missing neighbor action in a grid policy, whereas Zhao fuses available representations and memory before selecting heterogeneous actions. Neither source claims that its learned controller is robust to every jammer, outage length, or swarm size. [[hidden-state-sharing-marl]] is a useful boundary concept because hidden-state exchange is not the same as Qi's map/experience sharing.

## Kinematics and fleet heterogeneity

The motion abstraction determines which constraints are even expressible. Zhu's rotary-wing UAV can hover at sampled points; Samir uses fixed-altitude slotted motion with a maximum-displacement speed bound; Chang uses fixed speed with explicit flight and hover energy; Li discretizes candidate hover cells. Qi turns flight into cardinal grid actions, hover, and landing, with collision resets rather than continuous dynamics.

[[fu-2026-dubins-uav-data-collection]] makes turning radius and rendezvous first-class constraints. A fast transport UAV releases slower communication UAVs, each follows an obstacle-aware Dubins chain, and the carrier elongates its path when it would reach a recovery point too early. The RCR algorithm is planned offline and its Pareto language is supported by simulations, not a theorem of global optimality. [[heterogeneous-uav-fleet]] captures this architectural heterogeneity: carrier speed, subordinate endurance, communication range, and recovery timing cannot be collapsed into one homogeneous-UAV route variable.

[[zhao-2026-uav-carrier-vcs]] is heterogeneous in another way: UGVs are road-bound data collectors and UAVs are aerial scouts that return for charging. Active/inactive flags represent unequal action durations, so a synchronous single-agent trajectory model would lose a central constraint. [[guo-2026-spatiotemporal-information-quality-ugrnet]] instead models ground robots, UAV relays, and a command center as a multi-hop information system; its spatial path variables describe robot region transitions rather than Dubins flight.

## Information quality and delay guarantees

The evidence types form a ladder, not a leaderboard:

| Evidence type | Source-specific statement | What it does not establish |
|---|---|---|
| Tolerance-qualified global optimization | Samir's BRB solves the formulated small MINLP globally up to its stopping tolerance. | The guarantee is formulation- and tolerance-specific, and BRB does not scale like the paper's SCA alternative. |
| Exact formulation with heuristic full-route solution | Chang writes an exact MILP formulation, but reports that solving the full model globally is impractical at scale and instead uses the TMTP heuristic; its DP is exact only for station insertion after a fixed service order. | An exact formulation is not evidence of an exact full-instance solve, and conditional DP optimality does not make TMTP globally optimal. |
| Conditional approximation | Li states separate approximation results for the full- and partial-collection no-overlap variants. | The overlap heuristics do not inherit those results, and each statement remains tied to its discretization and collection regime. |
| Learned or heuristic routing | Zhu's Transformer–weighted-A-star pipeline, Qi's DDQN, Zhao's HADRL, and Fu's BACS/DAWPRM are evaluated in their declared settings. | Reported outcomes do not transfer to another objective, channel, fleet, or constraint regime. |
| Probabilistic information bound | Guo derives a martingale DVPB for heterogeneous multi-hop queues and combines it with Wasserstein spatial mismatch. | A DVPB is not AoI, collected-bit volume, or a deterministic deadline guarantee; the source supplies no end-to-end trajectory optimizer. |

The same separation applies to failure modes. A deadline miss, an energy-depleted route, a jammer-induced outage, a collision reset, a late rendezvous, and a high Wasserstein distance are different failure events. Robustness claims must name the event and the tested horizon.

## Cross-source design map

The following direct relationships are accepted because each pair exposes a specific interface or boundary. They are cross-source inferences grounded in the cited source sections; they do not claim that either paper implements the combined design.

| ID | Direct pair | Design axis and useful contrast | Boundary |
|---:|---|---|---|
| 1 | [[zhu-2023-aoi-transformer-trajectory]] ↔ [[samir-2020-time-constrained-data-collection]] | Continuous AoI minimization over a closed tour versus hard per-device lifetime admission. | AoI and served-device count are not ranked. |
| 2 | [[zhu-2023-aoi-transformer-trajectory]] ↔ [[chang-2026-data-offloading-energy-constraints]] | Feasible hover-point/cluster ordering versus pickup-before-delivery ordering with replenishment. | The two routes have different node semantics and objectives. |
| 3 | [[deadline-constrained-uav-data-collection]] ↔ [[transformer-weighted-a-star-trajectory-planning]] | Deadline admission makes time windows hard; TWA* learns order and searches contact points for AoI. | The learned pipeline has no deadline-feasibility theorem. |
| 4 | [[deadline-constrained-uav-data-collection]] ↔ [[generalized-traveling-salesman-problem]] | Device admission under service windows versus one representative hover point per sampled cluster. | Group representatives are not deadline admissions. |
| 5 | [[generalized-traveling-salesman-problem]] ↔ [[many-to-one-pickup-and-delivery]] | Both group route decisions, but GTSP selects one point per group while many-to-one routing requires all pickups before one delivery. | Neither precedence nor representative choice can be inferred from the other. |
| 6 | [[transformer-weighted-a-star-trajectory-planning]] ↔ [[branch-reduce-and-bound]] | Learned sequence/search decomposition versus tolerance-controlled global partitioning for a small nonconvex formulation. | No optimality or approximation guarantee transfers to TWA*. |
| 7 | [[transformer-weighted-a-star-trajectory-planning]] ↔ [[mixed-integer-linear-programming]] | Neural ordering plus weighted A-star versus explicit binary route/energy logic in Chang's MILP formulation. | Exact formulation status is model-specific and does not validate learned routes. |
| 8 | [[samir-2020-time-constrained-data-collection]] ↔ [[generalized-traveling-salesman-problem]] | Time-expanded trajectory/admission decisions versus sampled neighborhood representatives. | Samir's service windows are not a GTSP neighborhood model. |
| 9 | [[chang-2026-data-offloading-energy-constraints]] ↔ [[deadline-constrained-uav-data-collection]] | Chang directly cites Samir's deadline route, then changes optional complete-within-lifetime admission into mandatory pickup-before-delivery plus battery feasibility. | Chang has no packet expiry objective; Samir has no battery-station insertion. |
| 10 | [[samir-2020-time-constrained-data-collection]] ↔ [[many-to-one-pickup-and-delivery]] | Admission and service windows versus mandatory pickup-before-delivery precedence. | Samir's endpoint service is not physical edge-server delivery. |
| 11 | [[samir-2020-time-constrained-data-collection]] ↔ [[dynamic-programming-battery-station-insertion]] | Samir identifies energy study as an open extension; Chang's DP supplies fixed-order replenishment logic. | DP does not repair deadline admission or optimize service order. |
| 12 | [[deadline-constrained-uav-data-collection]] ↔ [[many-to-one-pickup-and-delivery]] | Hard temporal expiry and hard pickup precedence are two independent route-feasibility layers. | Combining them would require a new joint formulation. |
| 13 | [[deadline-constrained-uav-data-collection]] ↔ [[dynamic-programming-battery-station-insertion]] | Deadline feasibility and battery-feasible station insertion constrain different state variables. | A battery-feasible route may still miss a device deadline. |
| 14 | [[branch-reduce-and-bound]] ↔ [[mixed-integer-linear-programming]] | BRB certifies a small nonconvex admission problem; Chang's MILP formulation explicitly encodes precedence and energy logic. | Samir reports a tolerance-qualified global solve; Chang reports an exact model but not a globally solved full instance. |
| 15 | [[branch-reduce-and-bound]] ↔ [[dynamic-programming-battery-station-insertion]] | Global bounds over joint admission/trajectory versus optimal replenishment insertion for one fixed order. | Fixed-order DP cannot inherit BRB's global claim. |
| 16 | [[chang-2026-data-offloading-energy-constraints]] ↔ [[qi-2026-ocma-ddqn-data-collection]] | Battery feasibility is the hard route constraint and completion time is the objective in Chang; Qi embeds energy and cooperation cost in decentralized utility under jamming. | Single-UAV pickup delivery and multi-UAV grid learning use different horizons and metrics. |
| 18 | [[mixed-integer-linear-programming]] ↔ [[opportunistic-cooperative-multi-uav-ddqn]] | Explicit binary route/energy feasibility versus reward-shaped decentralized policy decisions. | A learned policy is not an exact MILP solution or a solver guarantee. |
| 19 | [[qi-2026-ocma-ddqn-data-collection]] ↔ [[zhao-2026-uav-carrier-vcs]] | Qi handles intermittent UAV links and jammer-aware grid collection; Zhao handles link-qualified, unequal-duration UAV/UGV cooperation. | Their data ratios, efficiency indices, maps, and agent roles differ. |
| 21 | [[lstm-interruption-compensation]] ↔ [[attentive-memory-integrated-information-exchange]] | Short-outage neighbor-action imputation versus attention over available messages plus persistent memory. | Neither mechanism guarantees arbitrary delay or packet loss. |
| 24 | [[opportunistic-cooperative-multi-uav-ddqn]] ↔ [[attentive-memory-integrated-information-exchange]] | Opportunistic map/experience sharing and game utility versus attentive hidden-state/action exchange with memory. | The mechanisms operate at different representation and timing layers. |

The matrix deliberately leaves four tempting direct pairs unlinked: pickup precedence versus opportunistic exchange, distance-gated map sharing versus hidden-state exchange, value-circle thresholds versus policy-divergence exploration, and action imputation versus hidden-state sharing. Each pair is useful for explaining a boundary, but its shared axis is too indirect for a direct core edge without claiming a mechanism that neither endpoint implements.

## Non-comparability and evidence limits

- Collected bits, served-device count, AoI, deadline violations, completion time, energy consumption, data-collection ratio, fairness, overlap, DVPB, and Wasserstein distance remain separate metrics. No exact, MILP, branch-and-bound, DP, heuristic, or DRL method is ranked across these instances.
- A hard deadline is not an AoI penalty; a battery station is not a soft energy reward; and a DVPB is not a deterministic deadline guarantee. The same word “timely” can refer to different state variables.
- Grid actions, fixed-speed waypoint models, continuous hover disks, pickup/delivery nodes, Dubins paths, and robot-region transitions have incompatible kinematics. A route length or mission time from one model cannot be substituted into another.
- Zhu's sampled disks, Samir's path-loss/CSI repair, Chang's idealized LoS and constant replacement delay, Li's discretization and overlap cases, Qi's static-per-episode jammers, Zhao's realistic-map simulation, Fu's offline planning, and Guo's queue independence/stability assumptions bound the scope of their evidence.
- Guo's martingale bound and Li's no-overlap approximation are formal statements under explicit assumptions. Qi, Zhao, and Fu report simulation robustness or Pareto behavior; those observations do not prove safety, convergence, or global optimality outside the tested settings.

## Design implications and open gaps

1. **Declare the feasibility state first.** Specify whether the active boundary is a packet deadline, residual battery, pickup precedence, link availability, turning radius, queue stability, or region assignment. Do not hide a hard boundary inside a reward weight.
2. **Choose the objective after the boundary.** Keep freshness, collected volume, completion time, energy, and information quality as distinct outputs; if a weighted objective is needed, report each component and its units.
3. **Match the solver to the horizon.** Use BRB solutions or solved MILP models as small-instance references; use DP only for fixed-order replenishment; and use learned/heuristic policies with explicit out-of-distribution and failure tests.
4. **Separate communication control from motion feasibility.** Distance-gated exchange, outage prediction, hidden-state sharing, and policy-divergence exploration address different layers. A controller that predicts an action during an outage still needs collision, battery, and kinematic checks.
5. **Treat heterogeneity as structure.** Carrier/subordinate UAVs and UAV/UGV teams need release, recovery, road, charging, and decision-duration states; collapsing them into a homogeneous multi-UAV action space removes the constraints that drive mission time.
6. **Report guarantees with their regimes.** State overlap assumptions for approximation ratios, tolerance and dimension for BRB, fixed-order scope for DP, queue assumptions for DVPB, and simulation horizon/agent count for learned robustness.

Open gaps include a joint formulation that combines hard deadlines with battery-station insertion, a route model that couples continuous hover neighborhoods to pickup/delivery precedence, interruption-aware control with continuous Dubins dynamics, and an end-to-end information-quality objective that exposes both DVPB and spatial mismatch while retaining a verifiable safety constraint. None of the eight sources supplies that complete stack.
