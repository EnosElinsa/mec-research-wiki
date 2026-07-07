---
type: source
title: "3D Trajectory and Pickup/Drop-Off Strategy for UAV-Enabled Delivery: Trade-Off Between Time and Energy Minimization"
authors: ["Kisong Lee", "Sung Ho Chae"]
year: 2026
url: "https://doi.org/10.1109/TITS.2025.3628828"
venue: "IEEE Transactions on Intelligent Transportation Systems (IEEE T-ITS)"
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
created: 2026-07-07
updated: 2026-07-07
---

# 3D Trajectory and Pickup/Drop-Off Strategy for UAV-Enabled Delivery: Trade-Off Between Time and Energy Minimization

## Citation

Lee, K., & Chae, S. H. (2026). *3D Trajectory and Pickup/Drop-Off Strategy for UAV-Enabled Delivery: Trade-Off Between Time and Energy Minimization*. **IEEE Transactions on Intelligent Transportation Systems**. DOI: 10.1109/TITS.2025.3628828.

## TL;DR

Formulates UAV parcel delivery as a joint 3-D trajectory, pickup/drop-off, and time-slot-length optimization problem. The objective is a weighted sum of mission completion time and propulsion energy under payload weight, pickup/drop-off, altitude, and no-fly-zone constraints. The paper relaxes the MINLP, uses SCA plus a penalty convex-concave procedure to preserve binary pickup/drop-off indicators, and studies the practical time-energy tradeoff.

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

This is a low-altitude logistics source adjacent to MEC rather than an offloading source. It complements [[chen-2026-cargo-uav-pickup-lae]], which handles cellular-connected cargo-UAV pickup with learning and simulated annealing. Here the key contribution is optimization-grounded [[uav-delivery-pickup-dropoff]] under payload-weight, [[rotary-wing-propulsion-energy-model]], [[uav-trajectory-control]], [[energy-latency-tradeoff]], and no-fly-zone constraints.

## Raw artifacts

- `raw/sources/3D_Trajectory_and_Pickup-Drop-Off_Strategy_for_UAV-Enabled_Delivery_Trade-Off_Between_Time_and_Energy_Minimization/3D_Trajectory_and_Pickup-Drop-Off_Strategy_for_UAV-Enabled_Delivery_Trade-Off_Between_Time_and_Energy_Minimization.md`
- Original PDF and extracted figures (`images/`) in the same folder.
