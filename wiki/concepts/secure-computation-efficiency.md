---
type: concept
title: "Secure Computation Efficiency"
tags: [security, metric, energy-efficiency, computation-offloading, pls]
related:
  - "[[physical-layer-security]]"
  - "[[secrecy-outage-probability]]"
  - "[[energy-latency-tradeoff]]"
  - "[[michailidis-2024-secure-ris-uav-mec-iot]]"
created: 2026-05-31
updated: 2026-05-31
---

# Secure Computation Efficiency

**Secure computation efficiency (SCE)** is a metric for secure MEC offloading defined as the ratio of **total securely-computed bits** to **weighted total energy consumption** of the system (devices + aerial server + propulsion). It folds together throughput, security, and energy: a scheme that offloads more bits while keeping them confidential from eavesdroppers and spending less energy scores higher. Maximizing SCE (often the *minimum* SCE across users, for fairness) yields a fractional objective typically handled by Dinkelbach-style [[fractional-programming-dinkelbach]].

## In this wiki

- [[michailidis-2024-secure-ris-uav-mec-iot]] maximizes the **minimum SCE** in a UAV-RIS-MEC-IoT network with aerial and ground eavesdroppers, jointly optimizing power, time-slot scheduling, task allocation, and RIS phase shifts under a [[secrecy-outage-probability]] analysis over Nakagami-m fading. SCE complements the broader [[energy-latency-tradeoff]] by adding a security dimension.
