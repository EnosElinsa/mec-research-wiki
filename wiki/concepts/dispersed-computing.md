---
type: concept
title: "Dispersed Computing"
tags: [edge-computing, volunteer-iot, heterogeneous-processors, computation-paradigm]
related:
  - "[[mobile-edge-computing]]"
  - "[[task-redundancy-for-reliability]]"
  - "[[parallel-vs-serial-processing]]"
  - "[[huang-2025-cmop-dispersed-computing]]"
created: 2026-05-29
updated: 2026-05-29
---

# Dispersed Computing

A computing paradigm that exploits **underutilized resources** on a swarm of dispersed devices (volunteer IoT devices, idle laptops, smartphones) to assist an overloaded edge server. The dispersed devices are typically heterogeneous, unreliable, and selfish — three traits that distinguish dispersed computing from classical MEC.

The wiki's entry is [[huang-2025-cmop-dispersed-computing]]. Key modeling choices that show up:

- **Heterogeneous processors** — edge server runs tasks in parallel; volunteer IoTDs queue tasks and run them serially. See [[parallel-vs-serial-processing]].
- **Task redundancy** — to overcome IoTD unreliability, the same task runs on multiple IoTDs in parallel ([[task-redundancy-for-reliability]]).
- **Incentives** — selfish IoTDs need monetary or reputational rewards (Stackelberg-game pricing in some sources, fixed-rate charging in this one).

Sits adjacent to but distinct from **federated** computing (one task per device, model-aggregation focus) and from **cloud-edge-end** offloading (assumes reliable, dedicated edge servers).
