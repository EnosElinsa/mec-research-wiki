---
type: concept
title: "Device Association"
tags: [resource-allocation, mec, aerial-mec, matching]
related:
  - "[[wang-2026-ikpp-vehicular-uav]]"
  - "[[shah-2026-cellfree-mimo-fap-control]]"
  - "[[yao-2026-transformer-mean-field-isac-sagin]]"
  - "[[liu-2026-heterogeneous-sensor-satisfaction]]"
  - "[[zhou-2026-jrc-multiuav-resource]]"
  - "[[ron-2026-federated-a3c-uav-energy]]"
  - "[[wang-2026-glint-aoi-wireless-powered-edge]]"
  - "[[dual-network-sequential-aoi-control]]"
  - "[[task-offloading]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[matching-theory-for-resource-allocation]]"
  - "[[uav-trajectory-control]]"
  - "[[chen-2023-aiot-device-association]]"
  - "[[hou-2025-pbia-air-iscc-uav-its]]"
  - "[[chen-2026-pddqn-sagin-mec]]"
  - "[[gao-2026-fmad3qn-uav-gd-association]]"
  - "[[zhan-2026-gatd3qn-dependent-offloading]]"
  - "[[meng-2026-uav-isac-corrections]]"
  - "[[spatially-separated-uav-isac-role-scheduling]]"
created: 2026-06-02
updated: 2026-07-13
---

# Device Association

**Device association** is the decision of **which serving node (and often which subchannel/beam) each device attaches to** — for example, which ground or UAV base station an IoT device connects to for uplink and offloading. In multi-node aerial/terrestrial MEC it is a distinct decision dimension from the **offloading** decision (where a task is computed) and the **trajectory** decision (where the UAV flies), and the three are coupled: association sets the achievable rates that bound what offloading and trajectory can exploit.

Association is typically **combinatorial** (discrete, often NP-hard, with contention when several devices prefer the same node/subchannel), so it is solved with greedy/recursive heuristics, [[matching-theory-for-resource-allocation|matching theory]], or auction mechanisms rather than continuous optimization.

In the wiki, [[chen-2023-aiot-device-association]] makes device association a first-class decision in a distributed multi-UAV + GBS MEC network, solving it with a greedy **recursive selection-and-replacement transmission-rate-based (RSRT)** algorithm — devices contend for the subchannel that maximizes their transmission rate, and losers recurse to their next-best option — jointly with knapsack-based offloading and MADDPG trajectory control. [[zhan-2026-gatd3qn-dependent-offloading]] also optimizes UAV-ground-user association as part of JSPO before dependent-task offloading. [[hou-2025-pbia-air-iscc-uav-its]] controls service association between IoTDs and UAVs inside an Air-ISCC policy, while [[chen-2026-pddqn-sagin-mec]] combines IoT-device association with LEO satellite selection in a hybrid-action SAGIN-MEC policy. Related association/assignment patterns appear across the aerial-MEC track via [[matching-theory-for-resource-allocation]] and [[generalized-assignment-problem]].

[[meng-2026-uav-isac-corrections]] shows why association indicators must be tracked carefully inside convexified rate expressions: a duplicated `alpha_k[n]` factor caused one UAV-ISAC subproblem to be mislabeled non-convex until the rate definition was repaired.

[[wang-2026-glint-aoi-wireless-powered-edge]] places association between two learned stages: actor 1 selects UAV positions, path-loss preference matching assigns candidate sensors, and actor 2 schedules WPT time and transmissions. The matcher keeps binary contention outside the mobility actor; the evaluated actor chooses among 11 discrete movement actions.
