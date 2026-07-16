---
type: source
modeling_card: required
title: "JDACO: Joint Data Aggregation and Computation Offloading in UAV-Enabled Internet of Things for Post-Disaster Scenarios"
authors: ["Asif Mahmud Raivi", "Sangman Moh"]
year: 2024
url: "https://doi.org/10.1109/JIOT.2024.3354950"
venue: "IEEE Internet of Things Journal (IEEE IoT-J)"
tags: [source, post-disaster-mec, multi-uav-assisted-mec, task-offloading, uav-data-collection, multi-agent-reinforcement-learning, hierarchical-aerial-mec]
related:
  - "[[post-disaster-mec]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[uav-data-collection]]"
  - "[[task-offloading]]"
  - "[[value-decomposition-network]]"
  - "[[ddqn]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[rotary-wing-propulsion-energy-model]]"
  - "[[zhou-2024-jdl-abs-postdisaster-rescue]]"
  - "[[sun-2024-mvtora-postdisaster-vfc]]"
created: 2026-06-01
updated: 2026-07-16
---

# JDACO: Joint Data Aggregation and Computation Offloading in UAV-Enabled Internet of Things for Post-Disaster Scenarios

## Citation

Raivi, A. M., & Moh, S. (2024). *JDACO: Joint Data Aggregation and Computation Offloading in UAV-Enabled Internet of Things for Post-Disaster Scenarios*. **IEEE Internet of Things Journal**. DOI: 10.1109/JIOT.2024.3354950. (Manuscript received 11 September 2023; date of publication 16 January 2024; date of current version 25 April 2024 → year 2024.)

## TL;DR

A **joint data-aggregation + computation-offloading (JDACO)** scheme for a multi-UAV post-disaster IoT network where ground BSs are gone. **Low-tier UAVs (LT-UAVs)** hover over the area to aggregate sensor data from ground IoT nodes and process it locally; based on task size they offload to a higher-flying **high-tier UAV (HT-UAV)** with more compute. The objective minimizes total energy + latency of *both* the aggregation and offloading processes while maximizing IoT-device coverage. It is cast as a Markov game and solved by a multi-agent DRL algorithm, **VD3QN** = dueling double DQN (D3QN) + value-decomposition network (VDN) for cooperative learning.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Multiple low-tier UAVs aggregate data from ground IoT nodes and either process it locally or offload it to one higher-tier UAV with more computation. IoT-to-low-tier links use TDMA with probabilistic LoS/NLoS channels, low-tier-to-high-tier forwarding uses FDMA, and each low-tier UAV moves inside a bounded post-disaster region under rotary-wing energy and flight-time limits.

**Problem & objective**: A cooperative Markov-game control problem minimizes joint aggregation and offloading energy-delay cost while maximizing covered IoT devices, represented by $\min(E_{\mathrm{agg}}+E_{\mathrm{off}}+\lambda L)-\mu C_{\mathrm{covered}}$ over motion, aggregation, and execution decisions.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Local/offloaded execution | $\Phi_{j,k}$ | binary | Whether low-tier UAV $k$ processes IoT task $j$ locally or sends it to the high-tier UAV |
| Low-tier UAV motion | $\mathbf a_k(t)$ | discrete direction and distance | Movement selected by UAV $k$ per slot |
| Data aggregation choice | $g_{j,k}(t)$ | binary/assignment | IoT node or task aggregated by low-tier UAV $k$ |
| Offloaded workload | $b_{j,k}(t)$ | continuous, nonnegative | Data sent from low-tier UAV $k$ to the high-tier UAV |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Each IoT node is assigned to an in-range low-tier UAV and covered devices remain within the service region |
| C2 | Low-tier UAV motion stays inside the bounded region and avoids prohibited states |
| C3 | Local and high-tier CPU resources, FDMA bandwidth, and TDMA aggregation slots remain feasible |
| C4 | Low-tier UAV flight time and rotary-wing energy remain below their limits |
| C5 | Each task selects one local or high-tier execution mode through $\Phi_{j,k}$ |

**Algorithm**: Encode aggregation and offloading as a cooperative Markov game → learn discrete motion and execution policies with per-agent dueling double DQN → decompose team values with VDN → execute the VD3QN policies for joint data collection, local processing, and high-tier offloading.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Raivi and Moh [x] studied joint data aggregation and computation offloading in a two-tier UAV-enabled post-disaster IoT network. Low-tier UAVs aggregate and locally process ground data or offload larger tasks to a higher-tier UAV, and the objective combines aggregation and offloading energy and latency with IoT-device coverage. They modeled the joint decisions as a cooperative Markov game and proposed VD3QN, which combines dueling double DQN agents with a value-decomposition network. The learned policies coordinate UAV motion, data aggregation, and local-versus-high-tier execution in the discrete action space. Simulations report 20% lower training time, 11.4% more processed data, 5.6% higher energy efficiency, 11.2% shorter mission duration, and service for up to 98% of IoT devices compared with the conventional schemes.

## Problem framing

Existing work studied **data aggregation** and **computation offloading** separately. In a post-disaster region the prior communication infrastructure is disrupted, IoT nodes are energy/compute-constrained, and UAVs have limited battery/flight time. The paper argues these two problems should be solved **jointly** under one umbrella for data-driven aerial computing, minimizing aggregation+offloading cost while covering as many IoT devices as possible.

## System model

- **Two-tier UAV hierarchy.** Multiple LT-UAVs (single-core CPU, aggregate + locally compute + offload) under the coverage of one higher-altitude HT-UAV (longer flight time, higher compute) acting as the aerial edge server ([[hierarchical-aerial-mec]]).
- **Mobility/energy.** LT-UAV moves by (direction, distance) per slot within a bounded region; power follows the **rotary-wing propulsion** model ([[rotary-wing-propulsion-energy-model]]); each LT-UAV flies up to $T_{\max}$ / $E_{\max}$ then lands.
- **Communication.** IoT→LT-UAV downlink uses a probabilistic LoS/NLoS path-loss model with TDMA (no intra-cluster interference); LT-UAV→HT-UAV uplink uses free-space path loss with FDMA (bandwidth split into non-overlapping sub-bands).
- **Decision.** Binary local-vs-offload variable $\Phi_{j,k}$ between LT-UAV and HT-UAV.

## Method

The joint optimization is framed as a **Markov game** and solved with a multi-agent DRL (MA-DRL) algorithm:

- **D3QN** (dueling double DQN) per UAV agent for the discrete action space.
- **VDN** (value-decomposition network) for cooperative learning — agents share experiences and a decomposed team value.
- Combined into **VD3QN**, an off-policy method. Benchmarked against two other off-policy learners and one non-learning algorithm.

## Key findings

- Per the abstract (verbatim), JDACO surpasses the conventional schemes in **training-time reduction by 20%, processed data volume by 11.4%, energy efficiency by 5.6%, and mission duration by 11.2%**, while **serving up to 98% of IoT devices**.
- The comparison table positions JDACO as the only scheme covering both data aggregation *and* offloading with all four considered factors (trajectory/hovering, energy, delay, max IoT devices) using DRL.

## Limitations / future work

Future work will consider mobile ground nodes, add object-detection ability for individual UAVs, and extend the model to heterogeneous IoT nodes. LT-UAVs are single-core (one task at a time), node locations are assumed known beforehand, and the HT-UAV hovers at a fixed altitude.

## Relation to the corpus

A **post-disaster MEC** entry that uniquely **fuses data aggregation with offloading** in a two-tier LT/HT-UAV hierarchy. It is distinct from the other post-disaster sources: [[zhou-2024-jdl-abs-postdisaster-rescue]] (single-ABS queuing-delay min via Lyapunov + SCA-critic actor-critic) and [[sun-2024-mvtora-postdisaster-vfc]] (game-theoretic vehicle-fog computing) — different objective (joint aggregation+offload cost + coverage) and solver (VD3QN). Its VDN cooperative learning and CTDE-style sharing connect it to the multi-agent DRL track ([[value-decomposition-network]], [[ddqn]], [[centralized-training-decentralized-execution]]).

## Raw artifacts

- `raw/sources/JDACO_Joint_Data_Aggregation_and_Computation_Offloading_in_UAV-Enabled_Internet_of_Things_for_Post-Disaster_Scenarios/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
