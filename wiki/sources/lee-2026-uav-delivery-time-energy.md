---
type: source
title: "3D Trajectory and Pickup/Drop-Off Strategy for UAV-Enabled Delivery: Trade-Off Between Time and Energy Minimization"
authors: ["Kisong Lee", "Sung Ho Chae"]
year: 2026
url: "https://doi.org/10.1109/TITS.2025.3628828"
venue: "IEEE Transactions on Intelligent Transportation Systems (IEEE T-ITS)"
modeling_card: required
tags: [source, uav-delivery, trajectory-optimization, pickup-dropoff, time-energy-tradeoff, no-fly-zone, rotary-wing-uav, successive-convex-approximation]
related:
  - "[[uav-delivery-pickup-dropoff]]"
  - "[[uav-trajectory-control]]"
  - "[[rotary-wing-propulsion-energy-model]]"
  - "[[energy-latency-tradeoff]]"
  - "[[mixed-integer-nonlinear-programming]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[compliance-aware-uav-trajectory]]"
  - "[[chen-2026-cargo-uav-pickup-lae]]"
  - "[[cao-2026-radio-map-cargo-pickup]]"
created: 2026-07-07
updated: 2026-07-16
---

# 3D Trajectory and Pickup/Drop-Off Strategy for UAV-Enabled Delivery: Trade-Off Between Time and Energy Minimization

## Citation

Lee, K., & Chae, S. H. (2026). *3D Trajectory and Pickup/Drop-Off Strategy for UAV-Enabled Delivery: Trade-Off Between Time and Energy Minimization*. **IEEE Transactions on Intelligent Transportation Systems**. DOI: 10.1109/TITS.2025.3628828.

## TL;DR

Formulates UAV parcel delivery as a joint 3-D trajectory, pickup/drop-off, and time-slot-length optimization problem. The objective is a weighted sum of mission completion time and propulsion energy under payload weight, pickup/drop-off, altitude, and no-fly-zone constraints. The paper relaxes the MINLP, uses SCA plus a penalty convex-concave procedure to preserve binary pickup/drop-off indicators, and studies the practical time-energy tradeoff.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A single rotary-wing UAV starts with delivery parcels, visits designated delivery zones, collects additional parcels from pickup zones, avoids cylindrical no-fly zones, and reaches a prescribed destination. Parcel weight changes propulsion demand, and variable-length time slots describe the three-dimensional flight and landing operations.

**Problem & objective**: Problem P1 minimizes $\nu\sum_{n=1}^{N}\delta[n]+(1-\nu)\sum_{n=1}^{N}E[n]$, a weighted sum of mission completion time and payload-dependent propulsion energy.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Pickup indicator | $\alpha_k[n]$ | binary | Whether parcel $k$ is picked up in slot $n$ |
| Drop-off indicator | $\beta_m[n]$ | binary | Whether parcel $m$ is delivered in slot $n$ |
| Horizontal trajectory | $\mathbf Q$ | continuous position sequence | UAV horizontal coordinates over the mission |
| Vertical trajectory | $\mathbf Z$ | continuous altitude sequence | UAV altitude over the mission |
| Slot duration | $\delta[n]$ | continuous, nonnegative | Duration of flight and service slot $n$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | The UAV starts and ends at prescribed locations and obeys $\lVert\mathbf c[n]-\mathbf c[n-1]\rVert\le V_{\max}\delta[n]$ |
| C2 | Every continuous segment avoids each cylindrical no-fly zone |
| C3 | Each parcel is picked up or delivered once, and at most one service event occurs per slot |
| C4 | Carried payload never exceeds $W_{\max}$ |
| C5 | Altitude remains within bounds except for valid landing operations inside pickup or delivery zones |
| C6 | All required pickup and delivery events are completed before the destination is reached |

**Algorithm**: The solver relaxes the binary indicators, forms convex inner approximations of the trajectory, service-zone, and propulsion terms with SCA, and adds PCCP slack penalties that are increased until pickup and drop-off decisions become binary. It repeatedly solves the resulting convex program and updates the linearization point until the weighted objective stabilizes.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Lee and Chae [x] jointly optimized parcel pickup, drop-off, variable slot duration, and three-dimensional UAV trajectory for a payload-sensitive delivery mission. They minimized a weighted sum of completion time and propulsion energy under start-end, speed, payload, altitude, service-zone, mission-completion, and continuous no-fly-zone constraints. Their iterative method combines successive convex approximation with a penalty convex-concave procedure that recovers binary service indicators. The energy-minimizing strategy used more than 20% less energy but required about 10% more mission time than the time-minimizing strategy, while intermediate weights produced balanced plans.

## Problem

Unlike UAV communication systems, parcel delivery requires the UAV to physically carry items, visit pickup and delivery zones sequentially, and change energy consumption as payload weight changes. Existing delivery heuristics often minimize either completion time or energy without deriving an integrated 3-D strategy under no-fly-zone constraints. This paper asks how the delivery route and pickup/drop-off sequence should change as the operator weights time versus energy.

## System model

- A single rotary-wing UAV visits pickup and delivery zones with height and horizontal location constraints.
- Each parcel changes the carried weight, which affects propulsion power.
- The UAV must avoid cylindrical no-fly zones and obey altitude bounds.
- The objective is a weighted sum of completion time and energy consumption.

## Method

- The original problem is a mixed-integer nonlinear program with continuous trajectory/time-slot variables and binary pickup/drop-off indicators.
- SCA converts non-convex continuous constraints into convex approximations.
- A penalty convex-concave procedure keeps the relaxed pickup/drop-off variables close to binary behavior.
- The optimized plan can be computed offline on a ground server and uploaded before flight; the parse reports about 2 minutes runtime on an AMD Ryzen 9 5950X workstation.

## Key findings

- The energy-minimization strategy reduces energy consumption by more than 20% but takes roughly 10% longer than the time-minimization strategy.
- Energy-oriented routes prefer smoother motion, low altitude, and earlier drop-off of carried parcels to reduce payload-induced propulsion power.
- The method fully avoids no-fly zones in the reported simulations while preserving binary pickup/drop-off indicators after relaxation.
- Future work targets low-level dynamics such as acceleration and steering angle, plus multi-UAV cooperative task allocation and trajectory planning.

## Relation to the corpus

This is a low-altitude logistics source adjacent to MEC rather than an offloading source. It complements [[chen-2026-cargo-uav-pickup-lae]], which handles cellular-connected cargo-UAV pickup with learning and simulated annealing, and [[cao-2026-radio-map-cargo-pickup]], which uses an expected-SNR map, A* paths, PSO allocation, and payload-aware speed control. Here the key contribution is optimization-grounded [[uav-delivery-pickup-dropoff]] under payload-weight, [[rotary-wing-propulsion-energy-model]], [[uav-trajectory-control]], [[energy-latency-tradeoff]], and no-fly-zone constraints.

## Raw artifacts

- `raw/sources/3D_Trajectory_and_Pickup-Drop-Off_Strategy_for_UAV-Enabled_Delivery_Trade-Off_Between_Time_and_Energy_Minimization/3D_Trajectory_and_Pickup-Drop-Off_Strategy_for_UAV-Enabled_Delivery_Trade-Off_Between_Time_and_Energy_Minimization.md`
- Original PDF and extracted figures (`images/`) in the same folder.
