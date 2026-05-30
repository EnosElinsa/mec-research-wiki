---
type: source
title: "AAV-Assisted Joint Mobile Edge Computing and Data Collection via Matching-Enabled Deep Reinforcement Learning"
authors: ["Boxiong Wang", "Hui Kang", "Jiahui Li", "Geng Sun", "Zemin Sun", "Jiacheng Wang", "Dusit Niyato"]
year: 2025
url: "https://doi.org/10.1109/JIOT.2025.3542025"
venue: "IEEE Internet of Things Journal (IEEE IoT-J)"
tags: [source, uav-mec, data-collection, soft-actor-critic, matching-theory, mixed-integer-nonlinear-programming, drl]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[uav-data-collection]]"
  - "[[masac]]"
  - "[[matching-theory-for-resource-allocation]]"
  - "[[mixed-integer-nonlinear-programming]]"
  - "[[uav-trajectory-control]]"
  - "[[chen-2025-swipt-mec-sac]]"
created: 2026-05-31
updated: 2026-05-31
---

# AAV-Assisted Joint Mobile Edge Computing and Data Collection via Matching-Enabled Deep Reinforcement Learning

## Citation

Wang, B., Kang, H., Li, J., Sun, G., Sun, Z., Wang, J., & Niyato, D. (2025). *AAV-Assisted Joint Mobile Edge Computing and Data Collection via Matching-Enabled Deep Reinforcement Learning*. **IEEE Internet of Things Journal**. DOI: 10.1109/JIOT.2025.3542025.

## TL;DR

Unlike prior work that treats AAV-assisted **MEC** and **data collection (DC)** as separate problems, this paper studies a **joint multi-AAV MEC-DC system**: multiple AAVs process computation-intensive MEC tasks while a single AAV performs freshness-insensitive DC, with co-channel interference among UAVs explicitly modeled. The authors formulate a two-objective problem — **minimize total MEC latency** and **maximize collected data volume** — as a non-convex mixed-integer program with long-term, dynamic structure, then solve it with **SAC-TMA**: a soft actor-critic agent that jointly optimizes AAV movement, user transmit power, and user association in real time, where association is handled by a **two-phase matching-based association (TMA)** strategy.

## Problem framing

MEC and DC are usually run on different UAVs (MEC tasks need real-time, continuous compute; mixing in DC hurts MEC latency and raises energy use; isolating the data also aids privacy). But agricultural, traffic-management, and post-disaster scenarios need both at once in the same area. The two goals conflict and interact through shared spectrum and interference, and through energy/trajectory coupling, making a joint design necessary and hard.

## System model

- **Actors.** Multiple MEC-AAVs (process computation-intensive tasks) + one DC-AAV (collects freshness-insensitive data) serving ground users (GUs); co-channel interference among UAVs is modeled rather than ignored.
- **Objectives.** Minimize total MEC system latency; maximize total collected data volume — conflicting and interdependent.
- **Decision variables.** AAV movement (trajectory), user association, and user transmit power.
- **Problem class.** Mixed-integer non-convex with long-term / dynamic optimization properties.

## Method

- **Action-space-reduced MDP.** User association is modeled as a **one-to-many matching game with externalities**, which reduces the action space the DRL agent must search ([[matching-theory-for-resource-allocation]]).
- **SAC-TMA.** A **soft actor-critic** ([[masac|SAC]]) algorithm integrated with the **two-phase matching-based association (TMA)** strategy, jointly optimizing AAV movement, user association, and user transmit power in real time.

## Key findings

- SAC-TMA outperforms four benchmark algorithms across different numbers of MEC-users, jointly improving latency, collected data volume, and coverage (qualitative; specific curves in the paper).
- The TMA strategy outperforms traditional matching-based algorithms and random strategies, and is feasible in terms of algorithm running time.

## Limitations / future work

The parse's contribution/intro framing does not enumerate explicit limitations; the work is simulation-based.

## Relation to the corpus

A **matching + SAC** entry in the Jilin-University / NTU aerial-MEC cluster, sharing the Geng Sun group lineage with [[chen-2025-swipt-mec-sac]] (co-authors Boxiong Wang, Hui Kang, Jiahui Li, Zemin Sun, Jiacheng Wang, Dusit Niyato). It pairs SAC with [[matching-theory-for-resource-allocation]] much as other corpus sources pair Stackelberg/bargaining with matching, and it adds the **data-collection** objective ([[uav-data-collection]]) to the usual MEC offloading picture. Reinforces [[masac]] and [[mixed-integer-nonlinear-programming]].

## Raw artifacts

- `raw/sources/AAV-Assisted_Joint_Mobile_Edge_Computing_and_Data_Collection_via_Matching-Enabled_Deep_Reinforcement_Learning/full.md`
- Original PDF and extracted figures in the same folder.
