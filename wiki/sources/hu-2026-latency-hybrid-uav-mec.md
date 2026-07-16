---
type: source
title: "Latency-Aware Computation Offloading in Hybrid UAV-Assisted MEC Systems: Time Scheduling and 3D Trajectory Design"
authors: ["Xiaoyan Hu", "Xingxia Gao", "Pengle Wen", "Kai-Kit Wong", "Kun Yang"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3667786"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), 25(8), 2026"
modeling_card: required
tags: [source, uav-mec, wireless-powered-mec, task-offloading, noma, tdma, latency, uav-trajectory-control, wireless-power-transfer]
related:
  - "[[task-offloading]]"
  - "[[wireless-power-transfer]]"
  - "[[noma]]"
  - "[[uav-trajectory-control]]"
  - "[[air-to-ground-channel-model]]"
  - "[[wireless-backhaul]]"
  - "[[hu-2019-uav-relay-edge-computing]]"
  - "[[zhou-2018-uav-wireless-powered-mec]]"
  - "[[ji-2021-uav-mec-noma-oma-energy-min]]"
  - "[[kai-kit-wong]]"
  - "[[kun-yang]]"
created: 2026-07-07
updated: 2026-07-16
---

# Latency-Aware Computation Offloading in Hybrid UAV-Assisted MEC Systems: Time Scheduling and 3D Trajectory Design

## Citation

Hu, X., Gao, X., Wen, P., Wong, K.-K., & Yang, K. (2026). *Latency-Aware Computation Offloading in Hybrid UAV-Assisted MEC Systems: Time Scheduling and 3D Trajectory Design*. **IEEE Transactions on Mobile Computing**, 25(8), 11772-11789. DOI: 10.1109/TMC.2026.3667786. (DOI/venue/year verified against the title-matched Crossref/IEEE DOI record; the parse header itself does not print the DOI.)

## TL;DR

Studies a wireless-powered hybrid UAV-MEC system where one UAV and one ground base station cooperate to serve energy-limited ground users whose direct GBS links are blocked. Users can compute locally, offload to the UAV MEC server, or have the UAV relay task bits onward to the GBS. The paper minimizes total task-completion latency under both TDMA and NOMA by jointly optimizing time scheduling, CPU-frequency allocation, transmit powers, UAV 3D trajectory, and the required number of time slots.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: One battery-powered UAV with an MEC server and RF energy transmitter cooperates with a ground base station to serve $K$ energy-limited users whose direct GBS links are blocked. Tasks are bit-wise partitionable among local computing, UAV execution, and UAV-to-GBS relaying. The access schemes are TDMA and NOMA; UAV-ground links follow a probabilistic LoS/NLoS air-to-ground channel model.

**Problem & objective**: Problems (P0) and (P1) are mixed-integer nonconvex task-completion-latency minimizations, $\min N\delta_t$, over the TDMA and NOMA protocols. With fixed $N$, the inner problem is transformed into maximizing the minimum user computation-completion ratio.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Time scheduling | $t_{k,1}[n],t_{k,2}[n],t_{k,3}[n]$ | continuous, $[0,\delta_t]$ | User offloading, UAV relaying/computing, and GBS computing durations |
| CPU frequencies | $f_k^{loc}[n],f_k^{UAV}[n],f_k^{GBS}[n]$ | continuous, bounded | Local, UAV, and GBS computing allocations |
| Transmit powers | $P_k[n],P_{UAV}[n],P_U[n]$ | continuous, bounded | User uplink, UAV relay, and UAV energy-transfer powers |
| UAV 3D trajectory | $\mathbf q[n],z[n]$ | continuous position | Horizontal position and altitude in slot $n$ |
| Mission length | $N$ | positive integer | Number of slots and hence completion latency $N\delta_t$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | TDMA durations fit each slot, or NOMA users share the scheduled resource under SIC |
| C2 | User and UAV energy causality covers computing, transmission, propulsion, and harvested energy |
| C3 | Information causality limits UAV computing and relay bits by previously received task bits |
| C4 | CPU frequencies and transmit powers remain within node-specific bounds |
| C5 | UAV initial and final positions, horizontal and vertical speeds, and altitude bounds are satisfied |
| C6 | Every user completes its required task bits by the selected final slot |

**Algorithm**: Bisect on $N$ with a feasibility test, transform the fixed-$N$ problem into max-min computation-completion-ratio optimization, alternately update trajectory, CPU frequencies, time scheduling, and powers, and solve the updates with SCA, Lagrangian duality, linear programming, and convex optimization until convergence.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Hu et al. [x] studied latency-aware computation offloading in a wireless-powered hybrid UAV-assisted MEC system where one UAV cooperates with a ground base station under TDMA and NOMA. They formulated mixed-integer nonconvex problems that minimize task-completion latency by jointly optimizing time-slot scheduling, CPU-frequency allocation, transmit powers, the UAV three-dimensional trajectory, and the number of required slots. Their double-loop alternating-optimization algorithm uses bisection to adjust the slot count and transforms the inner problem into max-min computation-completion-ratio optimization. The inner loop decomposes the design into trajectory, CPU-frequency, time-scheduling, and power-allocation subproblems addressed through SCA, Lagrangian duality, linear programming, and convex optimization. Simulations report reduced task-completion latency relative to the evaluated benchmark schemes, particularly when computing resources are limited or user density is high.

## Problem framing

Hybrid UAV-GBS MEC can exploit both aerial flexibility and terrestrial compute, but latency is constrained by user/UAV energy, blocked ground links, and the need to coordinate local computing, UAV execution, and GBS relay execution. The paper adds wireless power transfer from the UAV to the users and treats the number of slots itself as part of the latency-minimization problem.

## System model

- **Network.** $K$ ground users, one battery-powered UAV with a lightweight MEC server and RF energy transmitter, and one GBS with a MEC server.
- **Blocked direct links.** Users cannot communicate directly with the GBS, so the UAV acts as both MEC server and aerial relay.
- **Task split.** User tasks are bit-wise partitionable across local computing, UAV execution, and UAV-to-GBS relaying.
- **Energy.** Users harvest RF energy from the UAV while performing offloading under FDD operation.
- **Channels.** UAV-ground links use a probabilistic LoS/NLoS air-to-ground model; UAV altitude is optimized within minimum/maximum flight-altitude limits.

## Method

The TDMA and NOMA formulations are mixed-integer non-convex problems. The proposed solution uses a double-loop alternating-optimization structure:

- The outer loop applies bisection search on the required number of slots, with feasibility decided by a computation-completion-ratio test.
- The inner loop converts the problem into maximizing the minimum computation-completion ratio across users.
- The transformed problem is decomposed into four alternating subproblems over UAV 3D trajectory, CPU-frequency allocation, time-slot scheduling, and transmit-power allocation; the parse describes SCA, Lagrange-duality, and convex-optimization steps inside the updates.

## Key findings

- The inner computation-completion ratio converges close to 1 after several iterations, and the outer-loop task-completion latency stabilizes in the reported convergence plots.
- Optimized UAV trajectories move toward dense user regions and then balance user-to-UAV and UAV-to-GBS channels; larger task sizes induce more altitude variation.
- Against WOA (fixed altitude), WLC (no local computing), URO (relay only), ETS (equal time scheduling), and GA baselines, the proposed TDMA/NOMA designs reduce task-completion latency.
- At $\bar I=400$ Mbit in Fig. 8, the proposed TDMA scheme reaches a computation-completion ratio above 1 at $N=42$, while URO and ETS are about 0.6 and 0.8; the proposed NOMA scheme completes the task within 27 slots in the same experiment.
- Latency increases with task size and user count, and decreases with stronger user/UAV CPU capacity; the NOMA advantage becomes more visible as the number of users grows.

## Limitations / future work

The future-work paragraph proposes extending the framework to multi-UAV cooperation and heterogeneous mobile-user access technologies, and adding robust optimization plus intelligent decision-making to handle real-world CSI acquisition and UAV flight-control uncertainty.

## Relation to the corpus

This source is a latency-oriented, classical-optimization counterpart to the DRL-heavy UAV-MEC offloading track. It extends the relay-plus-MEC role of [[hu-2019-uav-relay-edge-computing]] into a wireless-powered latency objective and connects the WPT-MEC lineage of [[zhou-2018-uav-wireless-powered-mec]] and [[wireless-power-transfer]] to TDMA/NOMA access and 3D [[uav-trajectory-control]]. Its NOMA-vs-TDMA comparison complements [[ji-2021-uav-mec-noma-oma-energy-min]] and the broader [[noma]] concept.

## Raw artifacts

- `raw/sources/Latency-Aware Computation Offloading in Hybrid UAV-Assisted MEC Systems Time Scheduling and 3D Trajectory Design/Latency-Aware Computation Offloading in Hybrid UAV-Assisted MEC Systems Time Scheduling and 3D Trajectory Design.md`
- Original PDF and extracted figures (`images/`) in the same folder.
