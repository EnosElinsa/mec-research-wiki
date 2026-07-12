---
type: source
title: "Online Computation Offloading for Collaborative Space/Aerial-Aided Edge Computing Toward 6G System"
authors: ["Yi Liu", "Li Jiang", "Qi Qi", "Kan Xie", "Shengli Xie"]
year: 2023
url: "https://doi.org/10.1109/TVT.2023.3312676"
venue: "IEEE Transactions on Vehicular Technology (IEEE TVT)"
tags: [source, space-air-ground-integrated-network, leo-satellite-edge-computing, task-offloading, lyapunov-optimization, computation-peer-offloading, queueing-theory, non-terrestrial-network]
related:
  - "[[space-air-ground-integrated-network]]"
  - "[[leo-satellite-edge-computing]]"
  - "[[task-offloading]]"
  - "[[lyapunov-optimization]]"
  - "[[computation-peer-offloading]]"
  - "[[queueing-theory]]"
  - "[[non-terrestrial-network]]"
  - "[[lyapunov-guided-drl]]"
  - "[[sagin-satellite-offloading-landscape]]"
  - "[[gao-2024-sagin-perception-offloading]]"
  - "[[chen-2024-thoas-traffic-aware-sagin]]"
  - "[[qin-2025-matd3-noma-queue-sagin]]"
  - "[[zhang-2024-mhspo-satellite-peer-offloading]]"
  - "[[cheng-2025-dos-satellite-edge-computing]]"
  - "[[qi-qi]]"
created: 2026-06-02
updated: 2026-07-13
---

# Online Computation Offloading for Collaborative Space/Aerial-Aided Edge Computing Toward 6G System

## Citation

Liu, Y., Jiang, L., Qi, Q., Xie, K., & Xie, S. (2023). *Online Computation Offloading for Collaborative Space/Aerial-Aided Edge Computing Toward 6G System*. **IEEE Transactions on Vehicular Technology**. DOI: 10.1109/TVT.2023.3312676. (Manuscript received 17 May 2023; revised 11 July 2023; accepted 18 August 2023; date of publication 7 September 2023; date of current version 13 February 2024; year 2023.)

## TL;DR

Proposes a **collaborative space/aerial-aided edge computing network (SAGECN)** for 6G in which **LEO satellites act as both "servers" and "users"**: besides serving ground users/IoT devices in remote areas, a resource-limited LEO satellite can offload its own tasks to a **nearby aircraft over a one-hop link** or to the **cloud server along a multi-hop inter-satellite path**, and decide the ratio of local vs offloaded computation. To minimize the **long-term task completion delay** of the LEO satellites under a time-varying space/aerial environment, the problem is cast as a **stochastic optimization** and solved with **Lyapunov optimization** (drift-plus-penalty), which decouples it into per-slot deterministic subproblems; a **delayed online learning** technique predicts the dynamic **task arrival and queue length** of satellites and aircraft, feeding the prediction into the per-slot offloading/scheduling decision (a bounded integer program).

## Problem framing

In 6G, the space-air-ground integrated network (SAGIN) is meant to give worldwide connectivity in remote areas (desert, ocean, mountains) that ground BSs cannot cover, with LEO satellites providing massive access and backhaul. But satellites have **limited computation and energy**, so a heavily loaded satellite degrades service coverage and quality. The paper's key reframing: rather than treating the LEO satellite only as an edge **server** for ground demand, it should also be seen as a **user** that itself needs computation services (for its own applications). Two technical issues follow: (i) the **variability** of the space/aerial network — satellites/aircraft have different, time-varying capacities and relative positions, task generation is highly variable, and queue lengths are hard to know in advance (signaling overhead, privacy); and (ii) the **computation-vs-communication tradeoff** between multi-hop offloading to the distant cloud (lower compute latency, higher transmission latency) versus one-hop offloading to a nearby aircraft.

## System model

- **Topology.** A set of LEO satellites $\mathbb N$ and a set of aircraft $\mathbb U$ (balloons, airships, fixed-/rotary-wing UAVs in the stratosphere). Satellites are linked by backhaul; tasks at a satellite can be processed **locally**, offloaded **one hop to the nearest aircraft**, or offloaded **multiple hops to the cloud** via inter-satellite links. Operation is time-slotted with binary decisions $\alpha_n(t)$ (offload or local), $\beta_{n,m}(t)$ (relay to neighbor satellite $m$), and $\theta_{n,u}(t)$ (offload to aircraft $u$), with $\alpha_n + \sum\beta_{n,m} + \sum\theta_{n,u} \le 1$.
- **Links.** Satellite-aircraft rate uses a constant channel gain; multi-hop satellite rate uses transceiver peak gain $G$, Boltzmann constant, and **free-space path loss**; the multi-hop delay sums per-hop transmission delays along the offloading path.
- **Computing & queues.** Satellite/aircraft processing rate depends on workload and available resources; task queues $Q_n(t)$, $Q_u(t)$ evolve with arrivals (own + relayed) minus processed tasks, under a **stability constraint** (bounded time-averaged backlog).
- **Objective.** Minimize the **long-term (time-averaged) completion delay** $D(t)$ — transmission + computation, including relay hops — over the offloading/dispatch decisions, subject to the one-action constraint and per-slot caps on tasks dispatched to satellites ($J^S_{\max}$) and aircraft ($J^U_{\max}$).

## Method

- **Lyapunov optimization.** A quadratic Lyapunov function over the aggregate queue vector and the **drift-plus-penalty** framework (parameter $V$ tuning the delay-vs-stability tradeoff) decompose the long-term stochastic problem into **per-slot deterministic subproblems** for each satellite, yielding an online offloading and scheduling policy.
- **Delayed online learning prediction.** Because the per-slot policy needs task-arrival and queue-length knowledge that is not available in advance, a **delayed online learning** method predicts both at satellites and aircraft, minimizing loss from prediction errors over time; the predicted queue information continuously adjusts the offloading/scheduling strategy (queue awareness). The resulting per-slot decision is obtained via a **bounded integer program**.

## Key findings

- Numerical results confirm the collaborative offloading scheme **reduces the long-term task completion delay of LEO satellites while guaranteeing computation efficiency**, relative to comparison schemes. Specific numeric margins are figure-derived; treat exact values as indicative.
- The combination of Lyapunov decomposition with **predicted** (rather than assumed-known) task arrivals and queue lengths is the paper's core mechanism for handling space/aerial variability.

## Limitations / future work

The evaluation is numerical/simulation-based, and several modeling simplifications are made (constant satellite-aircraft channel gain, per-slot bounded offloading capacities). The prediction quality of the delayed online learning bounds achievable performance. Explicit future work is not stated.

## Relation to the corpus

A **SAGIN / satellite offloading** entry distinctive for treating the **LEO satellite as both server and user** and for combining **Lyapunov drift-plus-penalty** with **delayed online learning** to predict task arrivals and queue lengths — a prediction-augmented online offloading policy rather than a DRL or game-theoretic one. It grounds [[space-air-ground-integrated-network]], [[lyapunov-optimization]], and the [[queueing-theory]]-based stability view, and its one-hop-aircraft-vs-multi-hop-cloud choice is a form of [[computation-peer-offloading]] along the constellation. It sits within the satellite-offloading landscape mapped in [[sagin-satellite-offloading-landscape]], beside the Lyapunov-+-DRL perception-aided SAGIN offloading [[gao-2024-sagin-perception-offloading]], the traffic-aware THOAS scheme [[chen-2024-thoas-traffic-aware-sagin]], and the Lyapunov-+-MATD3 NOMA queue-aware offloading [[qin-2025-matd3-noma-queue-sagin]]; its multi-hop inter-satellite offloading parallels the horizontal peer offloading of [[zhang-2024-mhspo-satellite-peer-offloading]], and its energy/queue-aware satellite focus relates to [[cheng-2025-dos-satellite-edge-computing]]. The Lyapunov-guided online-control pattern is mapped in the [[lyapunov-guided-drl]] methodology page.

## Raw artifacts

- `raw/sources/Online_Computation_Offloading_for_Collaborative_Space_Aerial-Aided_Edge_Computing_Toward_6G_System/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
