---
type: source
title: "Digital Twin-Assisted Space-Air-Ground Integrated Multi-Access Edge Computing for Low-Altitude Economy: An Online Decentralized Optimization Approach"
authors: ["Long He", "Geng Sun", "Zemin Sun", "Jiacheng Wang", "Hongyang Du", "Dusit Niyato", "Jiangchuan Liu", "Victor C. M. Leung"]
year: 2026
url: "https://doi.org/10.1109/TMC.2025.3623636"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
modeling_card: required
tags: [source, digital-twin, sagimec, low-altitude-economy, uav-assisted-mec, leo-satellite, lyapunov-optimization, stackelberg-game, online-optimization]
related:
  - "[[digital-twin]]"
  - "[[space-air-ground-integrated-network]]"
  - "[[leo-satellite-edge-computing]]"
  - "[[low-altitude-intelligent-network]]"
  - "[[lyapunov-optimization]]"
  - "[[stackelberg-game]]"
  - "[[task-offloading]]"
  - "[[uav-trajectory-control]]"
  - "[[geng-sun]]"
  - "[[zemin-sun]]"
  - "[[jiacheng-wang]]"
  - "[[dusit-niyato]]"
  - "[[victor-c-m-leung]]"
created: 2026-07-06
updated: 2026-07-16
---

# Digital Twin-Assisted Space-Air-Ground Integrated Multi-Access Edge Computing for Low-Altitude Economy: An Online Decentralized Optimization Approach

## Citation

He, L., Sun, G., Sun, Z., Wang, J., Du, H., Niyato, D., Liu, J., & Leung, V. C. M. (2026). *Digital Twin-Assisted Space-Air-Ground Integrated Multi-Access Edge Computing for Low-Altitude Economy: An Online Decentralized Optimization Approach*. **IEEE Transactions on Mobile Computing**, 25(3), 4363-4380. DOI: 10.1109/TMC.2025.3623636.

## TL;DR

Proposes a **digital-twin-assisted space-air-ground integrated multi-access edge computing (SAGIMEC)** architecture for the low-altitude economy. Terrestrial intelligent sensing devices (ISDs) can offload to a UAV, the UAV can connect through selected LEO satellites toward a cloud center, and a DT layer at the cloud keeps virtual models of the ISDs, UAV, and satellite network for monitoring and management. The joint satellite-selection / computation-offloading / communication-resource / computation-resource / UAV-trajectory problem is converted into per-slot decisions using Lyapunov optimization, then solved by an online decentralized optimization approach (ODOA) that combines satellite-latency learning with game-theoretic decision making.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Intelligent sensing devices can compute locally, offload to an aerial MEC UAV, or use that UAV and a selected LEO satellite to reach a cloud center. A cloud digital twin stores physical-layer and workload feedback, including uncertain satellite round-trip latency, for online space-air-ground control.

**Problem & objective**: Minimize time-averaged sensing-device cost, $\min_{\mathbf A,\mathbf B,\mathbf F,\mathbf W,\mathbf Q}T^{-1}\sum_t\sum_m C_m(t)$, where cost combines task latency and device energy and the decisions cover offloading, satellite relay, resources, and UAV motion.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Computation mode | $a_m^t$ | discrete, local/UAV/cloud | Execution tier for device $m$'s task |
| Satellite selection | $b_u^t$ | discrete satellite choice | Accessible LEO relay used by the UAV |
| UAV compute allocation | $F_{u,m}^t$ | continuous, positive | CPU resource assigned to an offloaded task |
| Communication share | $w_{u,m}^t$ | continuous, $(0,1]$ | UAV link resource assigned to device $m$ |
| UAV position | $\mathbf q_u^t$ | continuous 2-D position | Aerial MEC location in slot $t$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Long-term average UAV energy does not exceed $\bar E_u$. |
| C2 | Each task chooses local, UAV, or cloud execution and meets its completion deadline. |
| C3 | The UAV selects one relay from the currently accessible satellite set. |
| C4 | Per-task and aggregate UAV compute allocations do not exceed $F_u^{\max}$. |
| C5 | Communication shares are positive and sum to at most one for offloaded tasks. |
| C6 | The UAV starts at the prescribed point and moves at most $v_u^{\max}\tau$ per slot. |

**Algorithm**: Maintain digital-twin virtual queues for UAV communication, computation, and propulsion energy, and apply Lyapunov drift-plus-penalty to form a current-slot MINLP. Predict each accessible satellite's round-trip latency with an upper-confidence-bound multi-armed bandit, decompose offloading and UAV responses as a multi-leader common-follower Stackelberg game, solve resource and trajectory subproblems, and update the queues after physical execution.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

He et al. [x] proposed digital-twin-assisted space-air-ground MEC in which sensing devices choose local, UAV, or cloud execution and the UAV reaches the cloud through an accessible LEO satellite. They minimized time-averaged latency-and-energy cost over offloading, satellite selection, communication and compute resources, and UAV trajectory under deadline, capacity, mobility, and long-term UAV-energy constraints. ODOA uses Lyapunov queues for online feasibility, upper-confidence-bound learning for uncertain satellite round-trip latency, and a Stackelberg game with convex trajectory updates for decentralized decisions. The reported method improved QoS by at least 14.5% over DRL approaches, met its UAV-energy budget, and required 59 ms per slot for 20 sensing devices.

## Problem

Low-altitude applications generate latency-sensitive sensing and computation workloads, but a single terrestrial or UAV edge layer has limited coverage, compute, and backhaul. The paper frames the resulting problem as maximizing ISD quality of service under coupled decisions: where each task is executed, which satellite path supports cloud-side service, how wireless and compute resources are allocated, and how the UAV moves over time.

## System model

- **Physical layer.** Ground ISDs generate tasks; a UAV provides aerial communication/computation; LEO satellites relay between the UAV and the cloud center; the cloud maintains the DT layer.
- **DT layer.** The cloud-side DT mirrors the ISD, UAV, and satellite states, enabling virtual monitoring and resource-management decisions without assuming a static physical environment.
- **Objective.** The QoS metric combines task-completion latency and ISD energy consumption. The JSC4OP problem jointly controls satellite selection, offloading, communication resources, compute resources, and UAV trajectory.

## Method

Lyapunov optimization transforms the long-term problem into a per-slot resource-decision optimization problem. ODOA then handles the per-slot mixed decisions with an online latency-prediction component for uncertain satellite task round-trip delay and a Stackelberg-game-based decentralized decision procedure. The algorithm is designed for online operation rather than offline policy training.

## Key findings

- The abstract reports at least **14.5% QoS improvement** over DRL-based approaches.
- In the simulation studies, ODOA outperforms UAC, ERA, DSCT, DMSSCT, OCQ, and epsilon-greedy baselines in time-averaged ISD cost and average task-completion latency.
- At task data size 4 Mb, the reported average-latency reductions are 10.9%, 16.3%, 11.1%, 5.3%, 7.6%, and 3.3% against UAC, ERA, DSCT, DMSSCT, OCQ, and epsilon-greedy, respectively.
- With UAV compute resource 50 GHz, the paper reports ISD-cost reductions of 34.3%, 16.3%, 25.4%, 13.6%, 6.0%, and 2.6%, and latency reductions of 23.8%, 22.4%, 14.6%, 11.1%, 6.4%, and 2.1% over the same baselines.
- The reported running time is 59 ms for a 20-ISD case, fitting a 1 s decision slot in the simulation setting.

## Limitations / future work

The conclusion identifies two main extensions: the edge layer uses only one UAV, limiting service coverage and capacity, and the satellite network is treated as a communication relay rather than a compute tier. The authors propose scaling the edge network and integrating satellite computing in future work.

## Relation to the corpus

This page links the low-altitude-economy track to the SAGIN/satellite offloading line: unlike [[huang-2026-amappo-satellite-edge]], where UAVs relay IoTD access to satellite edge computing, this paper centers a DT-assisted UAV-plus-LEO-plus-cloud architecture and uses Lyapunov-plus-game online control rather than asynchronous MARL. It also extends [[digital-twin]] beyond semantic-communication and ISCC examples into a SAGIMEC resource-management role, and it connects the Jilin/NTU aerial-MEC author cluster around [[geng-sun]], [[zemin-sun]], [[jiacheng-wang]], [[dusit-niyato]], and [[victor-c-m-leung]] to DT-assisted low-altitude computing.

## Raw artifacts

- `raw/sources/Digital Twin-Assisted Space-Air-Ground Integrated Multi-Access Edge Computing for Low-Altitude Economy An Online Decentralized Optimization Approach/Digital Twin-Assisted Space-Air-Ground Integrated Multi-Access Edge Computing for Low-Altitude Economy An Online Decentralized Optimization Approach.md`
- Original PDF and extracted figures (`images/`) in the same folder.
