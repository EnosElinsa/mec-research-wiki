---
type: source
title: "Cooperative UAVs for Remote Data Collection Under Limited Communications: An Asynchronous Multiagent Learning Framework"
authors: ["Cuong Le", "Symeon Chatzinotas", "Thang X. Vu"]
year: 2026
url: "https://doi.org/10.1109/TWC.2026.3656853"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
modeling_card: required
tags: [source, uav, data-collection, marl, qmix, semi-markov, energy-efficiency, limited-communication]
related:
  - "[[asynchronous-qmix]]"
  - "[[uav-data-collection]]"
  - "[[qmix]]"
  - "[[semi-markov-decision-process]]"
  - "[[ma-pomdp]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[angle-dependent-rician-fading]]"
  - "[[shi-2025-aoi-energy-replenishment-multiuav]]"
  - "[[you-2019-rician-uav-data-harvesting]]"
created: 2026-07-12
updated: 2026-07-16
---

# Cooperative UAVs for Remote Data Collection Under Limited Communications: An Asynchronous Multiagent Learning Framework

## Citation

Le, C., Chatzinotas, S., & Vu, T. X. (2026). *Cooperative UAVs for Remote Data Collection Under Limited Communications: An Asynchronous Multiagent Learning Framework*. **IEEE Transactions on Wireless Communications**, 25, 11336-11349. DOI: 10.1109/TWC.2026.3656853.

## TL;DR

Models remote multi-UAV collection with unequal action durations as a decentralized partially observable semi-Markov process. Asynchronous-QMIX (AQMIX) lets only the next finishing UAV choose a new action while other agents continue their current actions; a local convex optimizer then allocates bandwidth at each hover point under imperfect CSI.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Heterogeneous-speed rotary-wing UAVs explore a gridded remote area at fixed altitude and collect initially unknown data from sensor nodes under limited inter-UAV communication. Each hovering UAV uses FDMA for active sensors, and different UAVs occupy orthogonal bands. UAV-sensor links combine probabilistic LoS/NLoS propagation with angle-dependent Rician fading and imperfect CSI.

**Problem & objective**: Problem (P) is a stochastic, nonconvex joint trajectory and bandwidth-allocation design that maximizes overall collection energy efficiency, $\max_{\mathbf w,\mathbf b}\Phi(\mathbf w,\mathbf b)/\psi(\mathbf w,\mathbf b)$, and is represented as a decentralized partially observable semi-Markov decision process for asynchronous control.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV cell action | $u_m^n$ | discrete, hover or four cardinal moves | Next asynchronous action of UAV $n$ |
| UAV trajectory | $\mathbf w^n$ | discrete cell sequence | Visited collection and transit cells |
| Sensor bandwidth | $b^{in}(t)$ | continuous, nonnegative | Bandwidth allocated by UAV $n$ to active sensor $i$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Every UAV starts and ends at its prescribed locations |
| C2 | Remaining energy always covers safe return to the final location plus a reserve margin |
| C3 | Per-UAV FDMA allocations satisfy $\sum_i b^{in}(t)\leq B_{max}/N$ |
| C4 | A UAV terminates only after mission completion or when the safe-return energy condition triggers |
| C5 | Actions depend only on local observations and information exchanged within communication range |

**Algorithm**: Formulate trajectory control as a Dec-POSMDP, use AQMIX to advance only the agent whose current action finishes first, train recurrent decentralized utilities with a monotonic mixing network and sum-pooled completion maps, then solve a local convex min-max hovering-time bandwidth problem under imperfect CSI at each visited collection point.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Le et al. [x] studied cooperative UAV data collection with stochastic data availability, unequal action durations, and limited inter-UAV communication. They formulated joint trajectory and bandwidth allocation to maximize collection energy efficiency and represented asynchronous trajectory control as a decentralized partially observable semi-Markov decision process. Their AQMIX method retains monotonic QMIX value factorization while allowing only the earliest-finishing UAV to select a new action and uses pooled completion maps to reduce the global state. After trajectory learning, each hovering UAV solves a convex local bandwidth-allocation problem under imperfect CSI. Simulations report higher energy efficiency and lower completion time than the evaluated synchronous QMIX, independent-learning, and heuristic baselines across the tested grid sizes, UAV counts, communication ranges, energy budgets, and data densities.

## Problem

Sensor locations and data volumes are unknown before deployment, collection times vary with demand and channel quality, and range-limited UAVs cannot synchronize at every step. Synchronous MARL wastes hover energy waiting for slower actions and can invalidate coordinated policies when decision epochs drift.

## System model

- Heterogeneous-speed rotary-wing UAVs move among cells at fixed altitude, hover until all discovered data in a cell are collected, and terminate on completion or reserve-energy limits.
- Each agent has local position, energy, completion-map, and nearby-demand observations. In-range UAVs exchange positions and completion maps.
- UAV-sensor links combine probabilistic LoS/NLoS and angle-dependent Rician fading. FDMA and orthogonal per-UAV bands avoid receiver interference.
- Energy efficiency is collected data divided by aggregate propulsion energy; communication energy is ignored.

## Method

The trajectory layer is a Dec-POSMDP with five local actions: hover plus four cardinal moves. AQMIX retains QMIX's monotonic mixing condition but maintains action-completion timestamps; only the earliest-finishing agent transitions and selects a new action. Parameter-shared recurrent agent networks support local execution, while global state drives the mixing network during training. Sum-pooled completion maps reduce state dimension. During testing, each hovering UAV solves a convex min-max completion-time bandwidth problem under channel-estimation error.

## Key findings

- Default experiments use two UAVs at 5 and 10 m/s, 100 m altitude, a 200 m communication range, a `3 x 3` observation window, and policies trained with 1,000 kJ per UAV.
- Tests span `8 x 8` through `20 x 20` grids and one to six UAVs. AQMIX has the strongest qualitative learning curves against synchronous QMIX and independent AIQL across the reported scales.
- On 1,000 common test scenarios, 150 kJ is sufficient for AQMIX, QMIX, and the heuristic to collect all data; AIQL needs more than 400 kJ.
- Moving from one to two UAVs reduces AQMIX completion time by approximately 75% while energy efficiency falls by less than 10%; the corresponding QMIX comparison is 50% and 30%.
- Policies trained at data density 0.3 remain strongest over densities 0.1-0.5. Longer inter-UAV communication range improves AQMIX/QMIX but not AIQL.
- A `3 x 3` downsampling kernel, matching the local observation window, performs best among the tested `1 x 1` to `5 x 5` kernels.

## Limitations / parse caveats

Evidence is simulation-only. Motion is grid-based at fixed altitude/speed, communication energy is ignored, UAV bands are orthogonal, hovering continues until all local data are collected, and map exchange is abstracted as immediate whenever agents are in range. Centralized training assumes global state, and the active-data-size distribution is unnamed. Full-band operation and a concrete UAV-UAV protocol remain future work. Several equations are OCR-damaged. Publication metadata is absent from the parse and was verified through the exact-title Crossref record; technical claims come only from the parse.

## Relation to the corpus

[[asynchronous-qmix]] combines the value factorization of [[qmix]] with irregular [[semi-markov-decision-process|semi-Markov]] decision epochs. It complements the synchronous QMIX/VDN collection and charging problem in [[shi-2025-aoi-energy-replenishment-multiuav]] and the continuous trajectory optimization in [[you-2019-rician-uav-data-harvesting]].

## Raw artifacts

- Parse: `raw/sources/Cooperative_UAVs_for_Remote_Data_Collection_Under_Limited_Communications_An_Asynchronous_Multiagent_Learning_Framework/Cooperative_UAVs_for_Remote_Data_Collection_Under_Limited_Communications_An_Asynchronous_Multiagent_Learning_Framework.md`
- Origin PDF: `raw/sources/Cooperative_UAVs_for_Remote_Data_Collection_Under_Limited_Communications_An_Asynchronous_Multiagent_Learning_Framework/Cooperative_UAVs_for_Remote_Data_Collection_Under_Limited_Communications_An_Asynchronous_Multiagent_Learning_Framework.pdf`
- Figures: `raw/sources/Cooperative_UAVs_for_Remote_Data_Collection_Under_Limited_Communications_An_Asynchronous_Multiagent_Learning_Framework/images/`
