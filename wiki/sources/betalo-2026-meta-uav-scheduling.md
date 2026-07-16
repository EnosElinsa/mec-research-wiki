---
type: source
title: "Meta-Learning-Enhanced Task Assignment and Resource Scheduling for UAV-Assisted WSNs in 6G-Enabled ITS"
authors: ["Mesfin Leranso Betalo", "Amr Mohamed", "Amin Sharafian", "Zongze Wu", "Jianqiang Li", "Xiaoshan Bai"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3696005"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), accepted manuscript, pp. 1-18"
modeling_card: required
tags: [source, uav-enabled-its, wireless-sensor-network, meta-learning, maddpg, fairness, resource-allocation]
related:
  - "[[mw-mad3pg]]"
  - "[[meta-deep-reinforcement-learning]]"
  - "[[maddpg]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[uav-enabled-its]]"
  - "[[uav-trajectory-control]]"
  - "[[jains-fairness-index]]"
created: 2026-07-13
updated: 2026-07-16
---

# Meta-Learning-Enhanced Task Assignment and Resource Scheduling for UAV-Assisted WSNs in 6G-Enabled ITS

## Citation

Betalo, M. L., Mohamed, A., Sharafian, A., Wu, Z., Li, J., & Bai, X. (2026). *Meta-Learning-Enhanced Task Assignment and Resource Scheduling for UAV-Assisted WSNs in 6G-Enabled ITS*. **IEEE Transactions on Mobile Computing**, accepted manuscript, 1-18. DOI: 10.1109/TMC.2026.3696005.

## TL;DR

Combines MAML-style adaptation with fairness-aware multi-agent deterministic actor-critic learning. UAVs jointly choose movement, sensor-node assignment, and communication resources in a 6G ITS data-collection network under power, QoS, latency, range, and airspace constraints.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A set $\mathcal{U}$ of UAVs collects traffic data from distributed sensor nodes $\mathcal{I}$ and relays it to a ground control station over 6G links. UAVs move in a bounded three-dimensional airspace, while formal channel rates use distance-dependent path loss and small-scale Rician fading.

**Problem & objective**: Problem P1 in (21) is a non-convex MINLP that maximizes weighted sensor data rate minus UAV transmit power, $\max_{P_u,x_i,R_{u,i},\mathbf{q}_u}\sum_{u\in\mathcal{U}}\sum_{i\in\mathcal{I}}x_iR_{u,i}\eta_u-\sum_{u\in\mathcal{U}}P_u$, while maintaining QoS and feasible flight.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Sensor-node selection | $x_i$ | Binary, $\{0,1\}$ | Whether sensor node $i$ is selected |
| UAV transmit power | $P_u$ | Continuous, $0\leq P_u\leq P_{\max}$ | Power allocated to UAV $u$ |
| Link rate | $R_{u,i}$ | Continuous, $R_{u,i}\geq R_{\min}$ | Achievable rate between UAV $u$ and sensor node $i$ |
| UAV position | $\mathbf{q}_u=(x_u,y_u,z_u)$ | Continuous, $\mathbf{q}_u\in\mathcal{Q}$ | Three-dimensional deployment and mobility decision |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Sensor activation is binary, $x_i\in\{0,1\}$ |
| C2 | Selected links stay inside communication range, $\sqrt{(x_u-x_i)^2+(y_u-y_i)^2+z_u^2}\leq D_{\max}$ |
| C3-C5 | $P_u\leq P_{\max}$, $R_{u,i}\geq R_{\min}$, and $\sum_{u\in\mathcal{U}}P_u\leq P_{\mathrm{total}}$ |
| C6 | Processing latency satisfies $T_{\mathrm{proc}}\leq T_{\max}$ |
| C7 | UAV position remains feasible, $\mathbf{q}_u\in\mathcal{Q}$ |

**Algorithm**: P1 is separated into trajectory/deployment, sensor selection, and communication scheduling subproblems, then represented as a constrained multi-agent stochastic game. MW-MAD3PG embeds MAML inner and outer updates into centralized-training/decentralized-execution deterministic actor-critic learning, shares selected replay information, and shapes the reward with Jain-fairness term $f_t^{\alpha}$ so agents can adapt mobility, selection, and power policies to new traffic and channel tasks with few updates.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Betalo et al. [x] studied joint sensor selection, UAV deployment and mobility, and communication scheduling for UAV-assisted wireless sensor networks in 6G-enabled intelligent transportation systems. They formulated a non-convex mixed-integer problem that maximizes a weighted sensor data-rate term minus UAV transmit power under binary selection, communication-range, per-UAV and total-power, minimum-rate, processing-latency, and feasible-airspace constraints. The authors represented the control process as a constrained multi-agent stochastic game whose actions select UAV movement, sensor nodes, and communication resources, and whose reward combines energy-efficient data throughput, energy use, and Jain fairness. Their MW-MAD3PG algorithm embeds model-agnostic meta-learning within deterministic multi-agent actor-critic training to adapt policies across traffic, energy, sensor-distribution, and channel tasks. The reported quantitative table assigns MW-MAD3PG 95.2% system reliability, 92.4% deployment efficiency, and 88.9% offloading capacity, together with 0.98 seconds of training time per episode and 6.5 milliseconds of inference latency per action. The paper also reports improvements of up to 25% in UAV coordination or deployment efficiency and 30% in data offloading capacity over its evaluated baselines.

## Problem and system model

Multiple UAVs collect traffic-sensor data and relay it to a ground control station. The model couples rotary-wing mobility, air-to-ground rates, interference-aware scheduling, communication and processing energy, and binary UAV-sensor association. The stated energy-efficient-data-throughput objective is formally a weighted throughput-minus-power expression rather than a throughput/energy ratio.

The formulation is a non-convex MINLP. It separates deployment, sensor selection, and resource scheduling while retaining a stochastic-game/CMDP view whose state includes position, residual energy, sensor activity, and link rates.

## Method

[[mw-mad3pg]] augments [[maddpg]] with MAML-style inner/outer updates across traffic, energy, sensor-distribution, and channel tasks. Local actors choose movement, sensor selection, and resources; critics and replay aggregation support coordination. Jain-index reward shaping favors under-served sensors, while target networks and soft updates stabilize training.

## Key findings

- Table III reports 95.2% reliability, 92.4% deployment efficiency, and 88.9% offloading capacity for MW-MAD3PG, above the displayed MADDPG, Meta-SGD, and Meta-QL values; the denominators for the latter two percentage metrics are not defined in the parse.
- Table IV reports 0.98 s training time per episode, 6.5 ms inference latency per action, and a 38 MB model.
- The paper's headline claims of up to 25% better coordination/deployment and 30% greater offloading capacity are narrative or figure-level claims rather than directly reproducible table differences.

## Limitations / parse caveats

Evaluation is simulation-only. The parse conflicts on fixed versus variable altitude, Rician versus Rayleigh fading, two versus three decomposed subproblems, and MW-MAD3PG versus MW-MADDPG naming. It also gives incompatible training hardware/timing descriptions. Security mechanisms are discussed and evaluated in parts of the paper, but the conclusion says they are not integrated into the core algorithm. The accepted-manuscript banner warns that content may change.

## Relation to the corpus

This source joins [[meta-deep-reinforcement-learning]] with fairness-aware multi-UAV control in [[uav-enabled-its]]. Unlike conventional MEC offloading papers, its formal decisions center on sensor assignment, data collection, flight, and communication resources rather than a detailed local-versus-edge execution model.

## Raw artifacts

- `raw/sources/Meta-Learning-Enhanced_Task_Assignment_and_Resource_Scheduling_for_UAV-Assisted_WSNs_in_6G-Enabled_ITS/Meta-Learning-Enhanced_Task_Assignment_and_Resource_Scheduling_for_UAV-Assisted_WSNs_in_6G-Enabled_ITS.md`
- Original PDF and extracted figures (`images/`) are in the same folder.
