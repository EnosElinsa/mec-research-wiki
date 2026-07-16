---
type: source
title: "Energy-Latency Tradeoff for Joint Optimization of Vehicle Selection and Resource Allocation in UAV-Assisted Vehicular Edge Computing"
authors: ["Chunlin Li", "Jianyang Wu", "Yong Zhang", "Shaohua Wan"]
year: 2025
url: "https://doi.org/10.1109/TGCN.2024.3433457"
venue: "IEEE Transactions on Green Communications and Networking (IEEE TGCN)"
tags: [source, vehicular-mec, federated-learning, energy-latency-tradeoff, ddqn, mixed-integer-nonlinear-programming, uav-assisted-vec]
related:
  - "[[vehicular-mec]]"
  - "[[federated-learning]]"
  - "[[energy-latency-tradeoff]]"
  - "[[ddqn]]"
  - "[[mixed-integer-nonlinear-programming]]"
  - "[[uav-trajectory-control]]"
  - "[[li-2024-airground-vec-offloading]]"
  - "[[ma-2025-pdqn-vehicular-mec]]"
  - "[[zhang-2025-mcma-task-migration]]"
created: 2026-07-07
updated: 2026-07-16
modeling_card: required
---

# Energy-Latency Tradeoff for Joint Optimization of Vehicle Selection and Resource Allocation in UAV-Assisted Vehicular Edge Computing

## Citation

Li, C., Wu, J., Zhang, Y., & Wan, S. (2025). *Energy-Latency Tradeoff for Joint Optimization of Vehicle Selection and Resource Allocation in UAV-Assisted Vehicular Edge Computing*. **IEEE Transactions on Green Communications and Networking**. DOI: 10.1109/TGCN.2024.3433457. (Manuscript received 10 January 2024; accepted 18 July 2024; date of publication 25 July 2024; date of current version 21 May 2025 -> year 2025.)

## TL;DR

Optimizes **vehicle selection** and communication / computation resource allocation for **hierarchical federated learning** in a UAV-assisted VEC system. More vehicles can improve FL training but also increase uplink latency, bandwidth pressure, and energy consumption. The paper formulates a weighted **energy-latency tradeoff** with constraints on vehicle departure time, vehicle battery level, participant count, UAV bandwidth, and UAV compute resources. The resulting MINLP is modeled as an MDP and solved with **AB-DDQN**, a double-DQN variant trained with AdamW and tuned by the butterfly optimization algorithm.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Hierarchical federated learning uses vehicles as clients, UAVs as local aggregators, a base station as edge aggregator, and a cloud coordinator over mobile vehicular links.

**Problem & objective**: Select FL participants and allocate communication and local-compute shares to minimize the weighted round cost $\sum_k\left(\alpha T_k+(1-\alpha)E_k\right)$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
| --- | --- | --- | --- |
| Vehicle selection | $X_{u,m}^k$ | binary | Selects vehicle $m$ under UAV $u$ in round $k$ |
| Communication allocation | $\xi_k$ | continuous ratios in $[0,1]$ | Uplink and downlink bandwidth shares on BS-UAV and UAV-vehicle links |
| Local compute allocation | $\tau_{u,m}^k$ | continuous in $[0,1]$ | Fraction of vehicle CPU assigned to local FL training |

**Constraints**:

| ID | Meaning and key expression |
| --- | --- |
| C1 | Round latency is within the vehicle departure time and participant count lies between $M_{\min}$ and UAV capacity $M_u$. |
| C2 | Cumulative vehicle energy stays below its battery limit, $\hat E_{u,m}^K\leq E_{u,m}^{\mathrm{limit}}$. |
| C3 | BS-UAV and UAV-vehicle bandwidth allocation ratios remain in $[0,1]$. |
| C4 | Aggregate BS-UAV and UAV-vehicle bandwidth does not exceed each link capacity. |
| C5 | Local CPU allocation ratios satisfy $\tau_{u,m}^k\in[0,1]$. |

**Algorithm**: Model the MINLP as an MDP and solve it with AB-DDQN, using Double-DQN targets, AdamW updates, a butterfly optimizer for hidden-size, replay-buffer, and discount-factor tuning, and a mobility-aware departure filter.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Li et al. [x] studied participant selection and resource allocation for hierarchical federated learning in UAV-assisted vehicular edge computing. They minimized a weighted latency and energy cost over binary vehicle participation, BS-UAV and UAV-vehicle bandwidth shares, and vehicle CPU allocations under departure, battery, participant-count, and capacity constraints. Their AB-DDQN combines Double-DQN with AdamW training and butterfly-based hyperparameter search, while a mobility filter rejects vehicles that cannot finish a round before leaving coverage. Experiments on the GTSDB workload report lower weighted cost than DDPG-CRA, DQN-USCRA, and Q-US across data size, participant count, model size, and UAV count sweeps.

## Problem framing

Vehicular FL protects raw driving data by keeping it local, but a UAV-assisted VEC deployment must decide which moving vehicles should participate before they leave coverage, and how much bandwidth / CPU resource each selected vehicle should receive. The paper targets this scheduling layer rather than the model-aggregation algorithm itself: it asks how to pick FL participants and allocate UAV resources so the training round stays energy- and latency-efficient.

## System model

- **Four layers.** Vehicles train local models; UAVs act as hovering local aggregators; an edge server performs higher-level aggregation; a cloud server provides global coordination.
- **Mobility.** Vehicle availability is bounded by departure time; hotspot regions guide UAV paths, with a TSP / genetic-algorithm trajectory planner used before resource allocation.
- **Learning task.** Vehicles participate in hierarchical FL; the experiments use the GTSDB traffic-sign dataset.
- **Decision variables.** Binary vehicle-selection variables, UAV bandwidth ratios, and UAV compute-resource ratios.
- **Objective.** Minimize $\alpha T_k + (1-\alpha)E_k$, where $T_k$ is FL latency and $E_k$ covers vehicle and UAV energy.

## Method

The MINLP is converted into an MDP whose state includes latency, compute resources, bandwidth, vehicle battery state, and zero-padded vehicle slots for a fixed action shape. The action jointly chooses participating vehicles and resource ratios. AB-DDQN uses Double DQN to reduce Q-value overestimation, AdamW for optimization, and butterfly optimization to tune hyperparameters such as hidden-neuron count, replay-buffer size, and discount factor. A mobility-aware participant filter based on departure time avoids selecting vehicles that cannot complete the round.

## Key findings

- AB-DDQN converges after roughly 450 iterations in the reported training curves.
- Across local-data-size, participant-count, model-size, and UAV-count sweeps, AB-DDQN reports lower weighted cost than DDPG-CRA, DQN-USCRA, and Q-US baselines.
- With local-data-size variation, reported energy reductions are 13.26% versus DDPG-CRA, 87.92% versus DQN-USCRA, and 91.45% versus Q-US.
- With participant-count variation, reported cost reductions are 18.91%, 87.02%, and 94.49% versus the same baselines.
- The method trades some latency against energy in participant-count settings: latency is lower than DDPG-CRA but higher than DQN-USCRA and Q-US, while total cost is lower.

## Limitations / future work

The evaluation is based on a campus-style experimental / emulation environment rather than a full real-UAV field deployment. The authors identify adversarial FL participants and stronger privacy protections as future work.

## Relation to the corpus

This is a **vehicular MEC + FL scheduling** source. It is closest to [[li-2024-airground-vec-offloading]] in its air-ground VEC substrate, but it narrows the decision problem to selecting FL participants and allocating UAV resources. It complements [[zhang-2025-mcma-task-migration]] and [[ma-2025-pdqn-vehicular-mec]] by making the energy-latency tradeoff explicit at the learning-round level rather than only at task offloading or migration time.

## Raw artifacts

- `raw/sources/Energy-Latency Tradeoff for Joint Optimization of Vehicle Selection and Resource Allocation in UAV-Assisted Vehicular Edge Computing/Energy-Latency Tradeoff for Joint Optimization of Vehicle Selection and Resource Allocation in UAV-Assisted Vehicular Edge Computing.md`
- Original PDF and extracted figures (`images/`) in the same folder.
