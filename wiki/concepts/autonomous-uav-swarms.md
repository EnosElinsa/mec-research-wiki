---
type: concept
title: "Autonomous UAV Swarms"
tags: [uav, swarm, autonomy, planning, coordination]
related:
  - "[[du-2025-autonomous-intelligent-uav-swarms]]"
  - "[[javaid-2023-collaborative-uav-communication-control]]"
  - "[[collaborative-uav-communication]]"
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
  - "[[zhang-2026-ensemble-marl-uav-target-search]]"
  - "[[wu-not-in-parse-aoi-sampling-buffering-routing]]"
  - "[[yang-2025-hcdrl-pursuit-evasion]]"
  - "[[cooperative-uav-pursuit-evasion]]"
  - "[[li-2026-dff-slam]]"
  - "[[dynamic-feature-filtering-vslam]]"
  - "[[liu-2026-usp-nfrp-emergency-communication]]"
  - "[[persistent-emergency-uav-swarm-service]]"
  - "[[zhang-2026-dt-aircomp-cluster-formation]]"
  - "[[zhang-2026-distance-attention-uav-navigation]]"
  - "[[li-2026-jscfg-uav-grouping]]"
  - "[[joint-switch-coalition-formation-game]]"
  - "[[wang-2026-multimodal-uav-coverage-backhaul]]"
  - "[[multi-modal-uav-coverage-backhaul-control]]"
  - "[[jia-2026-hierarchical-uav-swarms]]"
  - "[[hierarchical-uav-swarm]]"
  - "[[wang-2026-mat-target-tracking]]"
  - "[[ye-2023-graph-uav-coverage]]"
created: 2026-07-10
updated: 2026-07-13
---

# Autonomous UAV Swarms

[[wang-2026-mat-target-tracking]] coordinates a sensing swarm around one moving target using TDOA localization, virtual formation points, Hungarian assignment, and autoregressive Transformer actions.

[[zhang-2026-ensemble-marl-uav-target-search]] adds a heterogeneous-search angle: fixed-wing and multirotor UAVs operate at different altitude bands, and [[ensemble-qmix]] coordinates target search under partial observability, no-fly zones, and collision masks.

[[wu-not-in-parse-aoi-sampling-buffering-routing]] adds a fully airborne monitoring angle: follower UAVs sense, buffer, and relay updates to a leader UAV, so autonomy includes freshness-aware sampling and FANET routing rather than only motion planning or target search.

The robotics and networking substrate underneath many UAV-MEC papers: multiple UAVs coordinate mission assignment, path planning, local collision avoidance, control, perception, localization, and communication so that the fleet behaves as a system rather than as independent aircraft.

[[javaid-2023-collaborative-uav-communication-control]] develops the communication/control side of this substrate. Its [[collaborative-uav-communication]] taxonomy connects UAV-to-UAV and infrastructure links to formation, localization, collision avoidance, shared sensing, offloading, and resource coordination.

[[du-2025-autonomous-intelligent-uav-swarms]] is the corpus's broad survey anchor. It separates swarm autonomy into scheduling/coordination, global task assignment, local planning, trajectory generation, formation/exploration/tracking/monitoring behaviors, and the hardware/software stack that makes those behaviors deployable.

For the MEC wiki, the concept is useful because later papers often import only one piece of the autonomy stack. A UAV-MEC source may optimize [[uav-trajectory-control]], use [[b-spline-trajectory]] parameterization, call a [[particle-swarm-optimization]] planner, or assume cellular-connected control links without restating the swarm-autonomy assumptions. This page keeps that background discoverable without merging every autonomy paper into the offloading taxonomy.

[[huang-2026-aircomp-uav-swarms-afl]] adds a learning-coordination angle: sensing UAVs and communication UAVs form an asynchronous federated-learning swarm where [[aircomp-assisted-asynchronous-fl]] reduces uplink aggregation latency while staleness-aware weighting protects the global model.

[[yang-2025-hcdrl-pursuit-evasion]] adds adversarial swarm control through [[cooperative-uav-pursuit-evasion]], where pursuers learn when to switch formation subtasks and how to execute continuous collision-aware maneuvers around an evading UAV.

[[li-2026-dff-slam]] supplies a GPS-suppressed positioning component for that autonomy stack: [[dynamic-feature-filtering-vslam]] removes moving-scene features before onboard pose estimation, although the paper evaluates one UAV rather than swarm-level coordination.

[[liu-2026-usp-nfrp-emergency-communication]] adds endurance-aware mission coordination through [[persistent-emergency-uav-swarm-service]], where periodic replacement paths and dynamic tree repair keep access and relay tasks continuously staffed.
