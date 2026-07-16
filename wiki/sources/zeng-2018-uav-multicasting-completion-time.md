---
type: source
modeling_card: required
title: "Trajectory Design for Completion Time Minimization in UAV-Enabled Multicasting"
authors: ["Yong Zeng", "Xiaoli Xu", "Rui Zhang"]
year: 2018
url: "https://doi.org/10.1109/TWC.2018.2790401"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), vol. 17, no. 4, pp. 2233-2246"
tags: [source, uav-multicasting, random-linear-network-coding, completion-time, trajectory-optimization, virtual-base-station]
related:
  - "[[random-linear-network-coding-multicast]]"
  - "[[virtual-base-station-waypoint-design]]"
  - "[[minimum-connection-time-trajectory]]"
  - "[[uav-trajectory-control]]"
  - "[[air-to-ground-channel-model]]"
  - "[[linear-programming]]"
  - "[[geometric-disk-cover]]"
  - "[[device-to-device-communication]]"
  - "[[lyu-2017-spiral-mbs-placement]]"
  - "[[yong-zeng]]"
created: 2026-07-14
updated: 2026-07-16
---

# Trajectory Design for Completion Time Minimization in UAV-Enabled Multicasting

## Citation

Zeng, Y., Xu, X., & Zhang, R. (2018). *Trajectory Design for Completion Time Minimization in UAV-Enabled Multicasting*. **IEEE Transactions on Wireless Communications, 17**(4), 2233-2246. DOI: 10.1109/TWC.2018.2790401.

## TL;DR

Uses random linear network coding to broadcast one file from a mobile UAV, conservatively reduces each receiver's recovery-probability requirement to minimum time inside a distance threshold, and constructs piecewise-linear routes through virtual base-station coverage regions with LP speed allocation.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: One fixed-altitude UAV broadcasts random-linear-network-coded packets at fixed rate to known static ground terminals. A terminal recovers the common file after enough independently faded packets, and proximity determines packet success probability.

**Problem & objective**: A non-convex mission problem minimizes multicast completion time, $\min T$, while every terminal's file-recovery probability exceeds its target under the UAV speed limit.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV trajectory | $\mathbf q(t)$ | continuous 2-D path | Broadcast route |
| Virtual-BS waypoint | $\mathbf v_j$ | continuous point in a coverage intersection | Representative visit point for a terminal cluster |
| Waypoint order | $\pi$ | discrete permutation | Open-tour order of virtual BSs |
| Segment traversal time | $\tau_l$ | continuous, nonnegative | Time allocated to sampled path segment $l$ |
| Connection radius | $D_c$ | continuous positive threshold | Distance defining conservative connected time |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | UAV speed along every segment does not exceed $V_{\max}$ |
| C2 | Each terminal accumulates its required minimum connection duration |
| C3 | The binomial lower bound meets each file-recovery probability target |
| C4 | Waypoints lie in their assigned coverage-disk intersections |
| C5 | Segment times and path geometry produce the total completion time $T$ |

**Algorithm**: Choose a connection radius by threshold sweep → cover terminals with virtual-base-station disks using the spiral heuristic → order VBSs by an open TSP → refine entry and exit points in each convex intersection → discretize the route → solve segment traversal times by linear programming under speed and connection-duration constraints.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zeng et al. [x] studied trajectory design for completion-time minimization in UAV-enabled multicasting with random linear network coding. They lower-bounded each terminal's recovery probability by a minimum connection-duration condition inside a distance threshold. A geometric disk-cover heuristic constructs virtual base stations, an open TSP orders them, and waypoint refinement selects points inside coverage intersections. For a fixed sampled route, linear programming allocates segment traversal times under speed and per-terminal connection-duration constraints. Simulations report shorter completion time than terminal-by-terminal and strip-based waypoint routes across the tested deployments.

## System model

- One fixed-altitude UAV broadcasts coded packets at a fixed rate to known, static ground terminals without terrestrial infrastructure.
- A terminal recovers the file after receiving enough independently faded RLNC packets. Its exact count follows a position-dependent Poisson-binomial distribution.
- The original objective minimizes mission time while every terminal meets a target recovery probability, subject only to maximum UAV speed.

## Probability reduction and guarantee scope

- For a chosen connection radius, packets sent inside a terminal's disk are lower-bounded by the edge-of-disk success probability. Stochastic dominance yields a binomial lower bound on file-recovery probability.
- Feasibility of the exact binomial lower-bound reformulation guarantees feasibility of the original probability constraint, but the converse need not hold. A subsequent Gaussian approximation converts that binomial tail into a minimum connection duration without an approximation-error guarantee.
- Theorem 1 proves only that an optimal trajectory for this connection-duration problem can be represented by connected line segments. It does not prove global optimality of the waypoint algorithm or of the original recovery-probability problem.

## Method

- A spiral [[geometric-disk-cover]] heuristic places virtual base stations whose coverage disks include all terminals; an open TSP orders them.
- Fixed clusters/order define convex intersection regions. Entry and exit points are globally optimized for that restricted construction, not for arbitrary waypoint selection.
- For a fixed spatially sampled path, [[linear-programming]] optimizes traversal times subject to speed and per-terminal connection-duration constraints.
- The connection radius is chosen by an average-SNR threshold heuristic and numerical sweep rather than an analytical global optimization.

## Findings

- In one 50-terminal realization, VBS-based waypoint refinement shortens the reported path and completion time relative to terminal-by-terminal and strip routes.
- Across 100 random deployments, the two VBS designs reduce completion time by about 50% versus terminal waypoints and 30% versus strip waypoints at 80 terminals.
- At 100 terminals, the reported mobile-UAV design needs about 210 seconds for all terminals, while a static benchmark serves only 23 terminals after 10,000 seconds.
- These are simulation results under the conservative model; no global-optimum gap is reported.

## Limitations

The model assumes one UAV, fixed altitude/rate, known static terminals, independent packet fading, and no infrastructure, correlated fading, obstacles, localization error, propulsion energy, acceleration, turning radius, or smooth dynamics. Probability is lower-bounded and then Gaussian-approximated without an end-to-end error bound. VBS placement, TSP ordering, and connection-radius selection are heuristic. Evaluation is simulation-only, and the parse damages one power entry and several probability symbols.

## Relation to the corpus

This applies the spiral placement of [[lyu-2017-spiral-mbs-placement]] to route construction and extends the [[yong-zeng]] trajectory line from throughput and energy objectives to common-file recovery time. Deferred D2D packet sharing is not part of the solved system.

## Raw artifacts

- Parse: `raw/sources/Trajectory_Design_for_Completion_Time_Minimization_in_UAV-Enabled_Multicasting/Trajectory_Design_for_Completion_Time_Minimization_in_UAV-Enabled_Multicasting.md`
- Original PDF and extracted figures are in the same folder.
