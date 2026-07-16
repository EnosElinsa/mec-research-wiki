---
type: source
title: "A Fast UAV Trajectory Planning Framework in RIS-Assisted Communication Systems With Accelerated Learning via Multithreading and Federating"
authors: ["Jun Huang", "Beining Wu", "Qiang Duan", "Liang Dong", "Shui Yu"]
year: 2025
url: "https://doi.org/10.1109/TMC.2025.3544903"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
modeling_card: required
tags: [source, uav-communications, intelligent-reflecting-surface, uav-trajectory-control, fedx-training-acceleration, federated-reinforcement-learning, soft-actor-critic, ppo, csi-estimation-error, rotary-wing-propulsion-energy-model]
related:
  - "[[intelligent-reflecting-surface]]"
  - "[[fedx-training-acceleration]]"
  - "[[federated-reinforcement-learning]]"
  - "[[soft-actor-critic]]"
  - "[[ppo]]"
  - "[[uav-trajectory-control]]"
  - "[[rotary-wing-propulsion-energy-model]]"
  - "[[csi-estimation-error]]"
  - "[[air-to-ground-channel-model]]"
  - "[[qin-2023-ris-uav-mec-ee]]"
  - "[[wu-2026-model-based-ppo-ris-uav-mec]]"
created: 2026-07-10
updated: 2026-07-16
---

# A Fast UAV Trajectory Planning Framework in RIS-Assisted Communication Systems With Accelerated Learning via Multithreading and Federating

## Citation

Huang, J., Wu, B., Duan, Q., Dong, L., & Yu, S. (2025). *A Fast UAV Trajectory Planning Framework in RIS-Assisted Communication Systems With Accelerated Learning via Multithreading and Federating*. **IEEE Transactions on Mobile Computing (IEEE TMC)**. DOI: 10.1109/TMC.2025.3544903.

## TL;DR

Designs FedX, a parallel training framework for RL-based trajectory planning in RIS-assisted UAV communications. The paper models imperfect channel information and quadrotor propulsion energy, then instantiates FedX with SAC and PPO as FedSAC and FedPPO. The headline result is training acceleration without materially changing the energy/throughput quality of the learned UAV trajectories.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A quadrotor UAV serves ground terminals in an urban RIS-assisted communication system with imperfect channel information. Over discrete slots, it moves horizontally and vertically, selects a terminal, chooses the slot duration, uploads the terminal's data, and eventually navigates toward a charging station while expending propulsion energy.

**Problem & objective**: The trajectory-planning problem minimizes $\sum_{n=1}^{N}E[n]$, the UAV's total three-dimensional propulsion energy across the mission, while completing the terminals' data transmissions.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Horizontal movement | $l[n]$ | discrete direction | UAV horizontal move in slot $n$ |
| Vertical movement | $h[n]$ | discrete, $\{-h_s,0,h_s\}$ | Descend, hover, or ascend |
| Terminal scheduling | $c_{k,i}[n]$ | binary | Ground terminal selected in slot $n$ |
| Slot duration | $\delta_t[n]$ | discrete, $[t_{\min},t_{\max}]$ | Flight and communication duration of slot $n$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | At most one ground terminal is served in each slot: $\sum_k c_{k,i}[n]\le1$ |
| C2 | Every terminal's required data volume is delivered within the mission |
| C3 | Horizontal and vertical speeds do not exceed their maximum values |
| C4 | The UAV remains within the admissible altitude and operating region |
| C5 | Terminal scheduling is binary and movement actions belong to their discrete action sets |

**Algorithm**: FedX forks multiple training threads, gives each an independent replay stream, runs a selected RL solver in parallel, and periodically aggregates thread parameters by data-weighted averaging. FedSAC and FedPPO instantiate this framework with SAC and PPO, using UAV position, remaining data, and charging-station distance as state and movement, scheduling, and slot duration as action.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Huang et al. [x] studied energy-aware three-dimensional trajectory planning for a quadrotor UAV serving ground terminals through an RIS-assisted link with imperfect channel information. They minimized total propulsion energy over horizontal and vertical movement, terminal scheduling, and slot-duration decisions under service, mission-completion, speed, and altitude constraints. FedX accelerates an arbitrary RL solver by training multiple threads in parallel and aggregating their parameters, with FedSAC and FedPPO as concrete instances. With five and ten agents, FedSAC achieved speedups of about 3.72 and 7.43 and FedPPO achieved 4.53 and 7.44, while their energy and throughput distributions remained close to those of the unaccelerated solvers.

## Problem

RIS-assisted UAV communication needs responsive trajectory decisions because UAV battery limits and wireless channels change quickly. The paper argues that prior solutions often assume complete CSI, rely on single-rotor energy models, and accept slow RL training, which weakens their fit for dynamic RIS-assisted UAV networks.

The optimization objective is to minimize UAV energy consumption while maintaining communication throughput. The hard part is the joint coupling among UAV movement, RIS-assisted channel quality, incomplete CSI, and quadrotor propulsion power.

## System model

- A UAV aerial base station serves multiple ground terminals with help from a fixed RIS.
- The communication model includes incomplete CSI through an MMSE-style imperfect channel estimate.
- The channel includes UAV-RIS and RIS-ground-terminal links under Rician fading assumptions.
- The UAV energy model is for a quadrotor and includes horizontal and vertical flight power.
- The trajectory problem is cast as an MDP where the controller moves the UAV to satisfy throughput while reducing flight energy.

## Method

FedX parallelizes RL training by forking multiple worker threads that interact with the environment, maintain local replay buffers, update local models, and periodically aggregate model parameters. The authors emphasize that this differs from conventional federated RL because the workers are training threads under centralized control rather than independent clients with distinct private environments.

The paper implements two FedX variants:

- **FedSAC**, which aggregates SAC actor, critic, target actor, and target critic networks.
- **FedPPO**, which uses PPO's clipped-policy update and synchronous actor/critic structure for more stable aggregation.

FedSAC gives stronger exploration but is more sensitive to asynchronous parameter mismatch. FedPPO is reported as more stable in the asynchronous FedX setup.

## Key findings

- The abstract reports more than 3x faster training with 5 agents and 7x faster training with 10 agents compared with the corresponding standard RL algorithms.
- In the detailed speedup analysis, FedSAC reaches about 3.72x and 7.43x speedup with 5 and 10 agents, while FedPPO reaches about 4.53x and 7.44x.
- SAC and FedSAC all converge, but FedSAC with 5 agents stabilizes around 6000 episodes; PPO and FedPPO converge around 2000 episodes.
- FedSAC and FedPPO produce trajectories with similar energy consumption and throughput to their non-accelerated SAC/PPO counterparts.
- The trajectory patterns show the UAV descending and approaching ground terminals to strengthen links when needed.

## Limitations / future work

FedX assumes a homogeneous training dataset. The authors state that heterogeneous data would require redesign. They also note that the current trajectory study covers flight and communication phases, but not takeoff, return, and landing energy, which are left for later modeling.

## Relation to the corpus

This is a communication-layer counterpart to the corpus's RIS-assisted MEC sources. It is closest to [[qin-2023-ris-uav-mec-ee]] and [[wu-2026-model-based-ppo-ris-uav-mec]] in using RIS phase behavior and UAV trajectory as coupled controls, but it focuses on communications rather than computation offloading. Methodologically, [[fedx-training-acceleration]] extends [[federated-reinforcement-learning]] into an intra-training acceleration pattern for [[soft-actor-critic]] and [[ppo]].

## Raw artifacts

- Parse: `raw/sources/A_Fast_UAV_Trajectory_Planning_Framework_in_RIS-Assisted_Communication_Systems_With_Accelerated_Learning_via_Multithreading_and_Federating/A_Fast_UAV_Trajectory_Planning_Framework_in_RIS-Assisted_Communication_Systems_With_Accelerated_Learning_via_Multithreading_and_Federating.md`
- Origin PDF: `raw/sources/A_Fast_UAV_Trajectory_Planning_Framework_in_RIS-Assisted_Communication_Systems_With_Accelerated_Learning_via_Multithreading_and_Federating/A_Fast_UAV_Trajectory_Planning_Framework_in_RIS-Assisted_Communication_Systems_With_Accelerated_Learning_via_Multithreading_and_Federating.pdf`
- Figures: `raw/sources/A_Fast_UAV_Trajectory_Planning_Framework_in_RIS-Assisted_Communication_Systems_With_Accelerated_Learning_via_Multithreading_and_Federating/images/`
