---
type: source
title: "Latency-Aware Computation Offloading in Hybrid UAV-Assisted MEC Systems: Time Scheduling and 3D Trajectory Design"
authors: ["Xiaoyan Hu", "Xingxia Gao", "Pengle Wen", "Kai-Kit Wong", "Kun Yang"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3667786"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), 25(8), 2026"
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
updated: 2026-07-13
---

# Latency-Aware Computation Offloading in Hybrid UAV-Assisted MEC Systems: Time Scheduling and 3D Trajectory Design

## Citation

Hu, X., Gao, X., Wen, P., Wong, K.-K., & Yang, K. (2026). *Latency-Aware Computation Offloading in Hybrid UAV-Assisted MEC Systems: Time Scheduling and 3D Trajectory Design*. **IEEE Transactions on Mobile Computing**, 25(8), 11772-11789. DOI: 10.1109/TMC.2026.3667786. (DOI/venue/year verified against the title-matched Crossref/IEEE DOI record; the parse header itself does not print the DOI.)

## TL;DR

Studies a wireless-powered hybrid UAV-MEC system where one UAV and one ground base station cooperate to serve energy-limited ground users whose direct GBS links are blocked. Users can compute locally, offload to the UAV MEC server, or have the UAV relay task bits onward to the GBS. The paper minimizes total task-completion latency under both TDMA and NOMA by jointly optimizing time scheduling, CPU-frequency allocation, transmit powers, UAV 3D trajectory, and the required number of time slots.

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
