---
type: concept
title: "Integrated Sensing, Computation, and Communication (ISCC)"
tags: [isac, edge-computing, resource-allocation, federated-learning]
related:
  - "[[tang-2024-iscc-uav-feel]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[federated-learning]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[hou-2025-pbia-air-iscc-uav-its]]"
  - "[[ye-2026-deeplsc-lae-isac]]"
  - "[[zhao-2026-mappo-jscc-aec]]"
  - "[[zhou-2026-radar-energy-iscac]]"
  - "[[radar-sensing-energy-tradeoff]]"
created: 2026-05-29
updated: 2026-07-07
---

# Integrated Sensing, Computation, and Communication (ISCC)

An extension of [[integrated-sensing-and-communication|ISAC]] that explicitly couples **computation** with sensing and communication, recognizing that on a resource-limited platform (e.g. a UAV) these three functions compete for the same bandwidth, energy, and time, and that platform placement affects all three.

In [[tang-2024-iscc-uav-feel]], ISCC resources (bandwidth, batch size, position) are jointly optimized with UAV deployment to minimize federated-edge-learning training time: the paper links sensing elevation angle to data-sample quality, bounds training loss via successful sensing probability, and solves the mixed-integer non-convex problem by alternating optimization (the BBPO scheme). ISCC ties the ISAC and [[federated-learning]] threads together.

[[zhao-2026-mappo-jscc-aec]] adds a HAP-assisted multi-UAV aerial-edge version: sensing-device repeat times, NOMA/OMA uplink power, UAV trajectories, offloading, and communication resources are jointly optimized, with Lyapunov energy-stability control and MAPPO embedded with SCA/Dinkelbach sub-solvers.

[[hou-2025-pbia-air-iscc-uav-its]] adds a UAV-swarm ITS version of over-the-air ISCC. UAVs sense traffic environments, communicate with IoTDs, and allocate computing resources, while a PPO-based PBIA policy controls time-slot scheduling, power, service association, and resource allocation.

[[zhou-2026-radar-energy-iscac]] adds the radar-data / HAP-offloading variant: multiple UAVs collect radar sensing data, process part locally, and offload the rest to a HAP MEC server while jointly controlling sensing scheduling, transmit power, and UAV/HAP trajectories for a sensing-data versus energy tradeoff.
