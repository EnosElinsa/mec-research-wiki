---
type: concept
title: UAV Data Collection
tags: [uav, data-collection, iot, data-sink, aerial-communications]
related:
  - "[[wang-2025-sac-tma-mec-dc]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[age-of-information]]"
  - "[[task-offloading]]"
  - "[[cai-2026-llm-drl-secure-lae-data]]"
  - "[[zhao-2026-adaptive-wdc-wet-lae]]"
created: 2026-05-31
updated: 2026-07-07
---

# UAV Data Collection

A UAV mission pattern where the aircraft acts as a flying **data sink**, flying to (or hovering over) ground IoT devices to collect their sensed data directly over LoS links — reducing device transmit power and preventing data overflow in hard-to-reach areas. It is the **data-gathering** counterpart to UAV-assisted **computation offloading** ([[task-offloading]]): the former maximizes collected data volume, the latter minimizes compute latency/energy.

## Joint MEC + DC

These two missions are usually studied separately and often run on different UAVs — an MEC-UAV doing real-time compute, a DC-UAV gathering freshness-insensitive data — because mixing them can hurt MEC latency and raise energy use, and isolating the data aids privacy. [[wang-2025-sac-tma-mec-dc]] is the corpus's entry that instead **jointly** optimizes a multi-AAV MEC-DC system, trading off MEC latency against collected data volume under co-channel interference, using SAC plus a matching-based user-association strategy.

## Relation to freshness

When the collected data is delay-sensitive, data-collection objectives connect to [[age-of-information]]; in [[wang-2025-sac-tma-mec-dc]] the DC data is explicitly **freshness-insensitive**, so the objective is total volume rather than AoI. [[cai-2026-llm-drl-secure-lae-data]] studies the freshness-sensitive and security-sensitive case, coordinating a data-collection UAV with a jamming UAV under AoI, energy, and eavesdropping constraints.

[[zhao-2026-adaptive-wdc-wet-lae]] adds the dual-service low-altitude version: UAVs collect fresh data from I-devices while also transferring RF energy to E-devices, with AoI and hungry-level-of-energy balanced by an adaptive reward preference rather than a fixed hand-tuned weight.
