---
type: source
title: "Joint Computation Offloading and Multidimensional Resource Allocation in Air–Ground Integrated Vehicular Edge Computing Network"
authors: ["Shichao Li", "Laha Ale", "Hongbin Chen", "Fangqing Tan", "Tony Q. S. Quek", "Ning Zhang", "Mianxiong Dong", "Kaoru Ota"]
year: 2024
url: "https://doi.org/10.1109/JIOT.2024.3441236"
venue: "IEEE Internet of Things Journal (IEEE IoT-J)"
tags: [source, vehicular-mec, air-ground-integrated-network, hierarchical-aerial-mec, computation-offloading, matching-theory-for-resource-allocation, uav-trajectory-control, high-altitude-platform-station]
related:
  - "[[vehicular-mec]]"
  - "[[air-ground-integrated-network]]"
  - "[[hierarchical-aerial-mec]]"
  - "[[task-offloading]]"
  - "[[matching-theory-for-resource-allocation]]"
  - "[[coalition-formation-game]]"
  - "[[uav-trajectory-control]]"
  - "[[high-altitude-platform-station]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[li-2025-twohop-airground-drl-offloading]]"
  - "[[chen-2023-dotora-air-ground-online]]"
  - "[[dai-2024-uav-vehicular-offloading-lyapunov]]"
  - "[[nabi-2025-jour-hierarchical-aerial]]"
created: 2026-06-02
updated: 2026-06-02
---

# Joint Computation Offloading and Multidimensional Resource Allocation in Air–Ground Integrated Vehicular Edge Computing Network

## Citation

Li, S., Ale, L., Chen, H., Tan, F., Quek, T. Q. S., Zhang, N., Dong, M., & Ota, K. (2024). *Joint Computation Offloading and Multidimensional Resource Allocation in Air–Ground Integrated Vehicular Edge Computing Network*. **IEEE Internet of Things Journal**. DOI: 10.1109/JIOT.2024.3441236. (Manuscript received 7 May 2024; revised 2 July 2024; accepted 3 August 2024; date of publication 8 August 2024; date of current version 9 October 2024 → year 2024.)

## TL;DR

Minimizes **total task offloading delay** in an **air–ground integrated vehicular edge computing (VEC)** network where vehicles can offload to a **roadside unit (RSU)**, multiple **UAVs**, or a **high-altitude platform (HAP)** — each carrying an MEC server, with UAVs/RSU also acting as relays to the distant HAP. The non-convex **joint multicomputation-equipment-selection and multidimensional-resource-allocation (JCESRA)** problem is tackled with the **block coordinate descent (BCD)** idea: first exclude the HAP and split into three subproblems — low-altitude equipment selection (**many-to-one matching**, with a **coalition game** handling matching externalities), joint bandwidth + computation allocation (**CVX**), and UAV trajectory (**SCA**); then add the HAP as a **knapsack** problem solved by **dynamic programming**, after which freed UAV/RSU compute resources are reallocated. Simulations report lower offloading delay than baselines.

## Problem framing

Autonomous driving generates computation-intensive, delay-sensitive tasks (assisted driving, navigation, HD mapping) that exceed on-board capacity, and terrestrial-only VEC suffers frequent handover/service interruption under high vehicle mobility. An air–ground integrated network (terrestrial RSU + aerial UAVs + HAP) adds ubiquitous coverage and flexible compute, but raises three challenges the paper targets: (i) **selecting** feasible computation equipment among many options; (ii) deciding each node's **role** (compute vs relay — UAVs/RSU can relay tasks to the HAP); and (iii) allocating **multidimensional resources** (compute, transmit power, bandwidth, UAV trajectory). The authors note that few prior air–ground works consider the HAP, and none jointly address all three challenges.

## System model

- **Topology.** A one-way J-lane road covered by one RSU (with MEC server), K UAVs (each with MEC server), and one HAP (with MEC server). RSU and UAVs are "low-altitude computation equipment" (set $\mathcal{A}=\{0,\dots,K\}$, index 0 = RSU); HAP and RSU are static, UAVs move. Time is divided into N slots; each vehicle generates one task per slot, characterized by $\{c_i(n)\text{ (CPU cycles)}, s_i(n)\text{ (data size)}, t_{i,\max}(n)\text{ (delay bound)}\}$.
- **Decisions.** Binary equipment-selection variables $\alpha_{ik}(n)$ (offload to low-altitude equipment k) and $\alpha_{ik}^{\mathrm{hap}}(n)$ (offload to HAP via k as relay), with each task assigned to exactly one server; plus continuous bandwidth $b_{ik}(n)$, compute-frequency $f_{ik}(n)/f_{ik}^{\mathrm{hap}}(n)$, and UAV trajectory $\mathbf{q}_k(n)$.
- **Channels & energy.** Vehicle↔low-altitude link uses a LoS channel gain $\propto 1/(H_{\mathrm{uav}}^2 + \|\mathbf{q}_k(n)-\mathbf{P}_i(n)\|^2)$; HAP link uses a free-space-loss model with antenna gains. UAV trajectory obeys per-slot displacement and inter-UAV safety-distance constraints, and a fixed-wing-style flight-energy model $E^{\mathrm{fly}}(n)=\tau(\theta_1 v^3 + \theta_2/v)$.
- **Objective.** Minimize the total task offloading delay (transmission + computation, including relay hops to the HAP) subject to bandwidth, compute-capacity, delay, and trajectory constraints.

## Method

The non-convex problem is solved via **BCD**, in two stages:

- **Stage 1 (exclude HAP) — JCESRA without HAP.** Decompose into three subproblems: (1) **low-altitude computation-equipment selection** (integer program) via **many-to-one matching**, with the **coalition game** method handling matching **externalities**; (2) **joint bandwidth + computation-resource allocation** via the **CVX** convex-optimization toolbox; (3) **UAV trajectory design** via **successive convex approximation (SCA)**.
- **Stage 2 (add HAP) — complete JCESRA.** The HAP offloading-decision + compute-allocation subproblem is recognized as a **knapsack problem** and solved by **dynamic programming**. Because some tasks move to the HAP, the now-redundant UAV/RSU compute resources are **reallocated** to further reduce delay, yielding the complete JCESRA algorithm.

## Key findings

- The complete JCESRA algorithm is reported to **significantly reduce total task offloading delay** compared with other algorithms across the simulated settings — the paper's stated result. Specific margins are figure-derived; treat exact values as indicative.

## Limitations / future work

The evaluation is simulation-based, and the network is treated as static within each time slot. Explicit future-work statements are `not in parse`.

## Relation to the corpus

A **vehicular MEC + hierarchical aerial** entry distinguished by spanning **three** computation tiers (RSU + UAVs + HAP) with explicit compute-vs-relay role assignment, and by hybridizing combinatorial methods (matching + coalition game + knapsack/DP) with convex/trajectory optimization (CVX + SCA) rather than a single solver family. It shares the Guilin-University-of-Electronic-Technology air-ground line and authors with the two-hop IoRT DRL offloading of [[li-2025-twohop-airground-drl-offloading]], and its air-ground delay-minimization objective parallels the distributed-online DOTORA scheme [[chen-2023-dotora-air-ground-online]] and the Lyapunov UAV-relieves-RSU offloading of [[dai-2024-uav-vehicular-offloading-lyapunov]]. Its HAP-inclusive multi-tier compute substrate and two-stage decomposition connect it to [[hierarchical-aerial-mec]] and the discrete-then-continuous solver pattern of [[nabi-2025-jour-hierarchical-aerial]]; the matching + coalition-game machinery grounds [[matching-theory-for-resource-allocation]] and [[coalition-formation-game]].

## Raw artifacts

- `raw/sources/Joint_Computation_Offloading_and_Multidimensional_Resource_Allocation_in_AirGround_Integrated_Vehicular_Edge_Computing_Network/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
