---
type: concept
title: "Device Association"
tags: [resource-allocation, mec, aerial-mec, matching]
related:
  - "[[task-offloading]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[matching-theory-for-resource-allocation]]"
  - "[[uav-trajectory-control]]"
  - "[[chen-2023-aiot-device-association]]"
  - "[[gao-2026-fmad3qn-uav-gd-association]]"
  - "[[zhan-2026-gatd3qn-dependent-offloading]]"
created: 2026-06-02
updated: 2026-07-07
---

# Device Association

**Device association** is the decision of **which serving node (and often which subchannel/beam) each device attaches to** — for example, which ground or UAV base station an IoT device connects to for uplink and offloading. In multi-node aerial/terrestrial MEC it is a distinct decision dimension from the **offloading** decision (where a task is computed) and the **trajectory** decision (where the UAV flies), and the three are coupled: association sets the achievable rates that bound what offloading and trajectory can exploit.

Association is typically **combinatorial** (discrete, often NP-hard, with contention when several devices prefer the same node/subchannel), so it is solved with greedy/recursive heuristics, [[matching-theory-for-resource-allocation|matching theory]], or auction mechanisms rather than continuous optimization.

In the wiki, [[chen-2023-aiot-device-association]] makes device association a first-class decision in a distributed multi-UAV + GBS MEC network, solving it with a greedy **recursive selection-and-replacement transmission-rate-based (RSRT)** algorithm — devices contend for the subchannel that maximizes their transmission rate, and losers recurse to their next-best option — jointly with knapsack-based offloading and MADDPG trajectory control. [[zhan-2026-gatd3qn-dependent-offloading]] also optimizes UAV-ground-user association as part of JSPO before dependent-task offloading. Related association/assignment patterns appear across the aerial-MEC track via [[matching-theory-for-resource-allocation]] and [[generalized-assignment-problem]].
