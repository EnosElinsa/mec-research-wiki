---
type: concept
title: "Autonomous UAV Swarms"
tags: [uav, swarm, autonomy, planning, coordination]
related:
  - "[[du-2025-autonomous-intelligent-uav-swarms]]"
  - "[[uav-trajectory-control]]"
  - "[[b-spline-trajectory]]"
  - "[[particle-swarm-optimization]]"
  - "[[cooperative-perception]]"
  - "[[cellular-connected-uav]]"
  - "[[uav-data-collection]]"
  - "[[uav-mobile-relaying]]"
  - "[[uav-enabled-its]]"
  - "[[huang-2026-aircomp-uav-swarms-afl]]"
  - "[[aircomp-assisted-asynchronous-fl]]"
created: 2026-07-10
updated: 2026-07-11
---

# Autonomous UAV Swarms

The robotics and networking substrate underneath many UAV-MEC papers: multiple UAVs coordinate mission assignment, path planning, local collision avoidance, control, perception, localization, and communication so that the fleet behaves as a system rather than as independent aircraft.

[[du-2025-autonomous-intelligent-uav-swarms]] is the corpus's broad survey anchor. It separates swarm autonomy into scheduling/coordination, global task assignment, local planning, trajectory generation, formation/exploration/tracking/monitoring behaviors, and the hardware/software stack that makes those behaviors deployable.

For the MEC wiki, the concept is useful because later papers often import only one piece of the autonomy stack. A UAV-MEC source may optimize [[uav-trajectory-control]], use [[b-spline-trajectory]] parameterization, call a [[particle-swarm-optimization]] planner, or assume cellular-connected control links without restating the swarm-autonomy assumptions. This page keeps that background discoverable without merging every autonomy paper into the offloading taxonomy.

[[huang-2026-aircomp-uav-swarms-afl]] adds a learning-coordination angle: sensing UAVs and communication UAVs form an asynchronous federated-learning swarm where [[aircomp-assisted-asynchronous-fl]] reduces uplink aggregation latency while staleness-aware weighting protects the global model.
