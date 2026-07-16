---
type: source
title: "A UAV-Assisted Multi-Task Allocation Method for Mobile Crowd Sensing"
authors: ["Hui Gao", "Jianhao Feng", "Yu Xiao", "Bo Zhang", "Wendong Wang"]
year: 2023
url: "https://doi.org/10.1109/TMC.2022.3147871"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
modeling_card: required
tags: [source, mobile-crowd-sensing, uav-data-collection, multi-task-allocation, incentives, maddpg, calibration]
related: ["[[uav-data-collection]]", "[[maddpg]]", "[[semi-markov-decision-process]]", "[[edge-intelligence]]"]
created: 2026-07-10
updated: 2026-07-16
---

# A UAV-Assisted Multi-Task Allocation Method for Mobile Crowd Sensing

## Citation

Gao, H., Feng, J., Xiao, Y., Zhang, B., & Wang, W. (2023). *A UAV-Assisted Multi-Task Allocation Method for Mobile Crowd Sensing*. **IEEE Transactions on Mobile Computing**, 22(7), 3790-3804. DOI: 10.1109/TMC.2022.3147871.

## TL;DR

Proposes UMA, a UAV-assisted mobile-crowd-sensing framework that assigns sensing tasks to human participants while scheduling UAVs to cover missed points of interest and calibrate human sensor data. The method combines online incentives, participant quality prediction, Shapley-style point importance, and MADDPG UAV scheduling.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Multiple concurrent mobile-crowd-sensing tasks define budgets, time slots, points of interest, and data-quality requirements. Human participants collect data for rewards, while multiple UAVs visit rarely sensed points and calibrate participant sensors; UAV motion consumes distance-proportional energy and must avoid obstacles and the area boundary.

**Problem & objective**: Problem (1) is a budgeted maximum-coverage problem that maximizes high-quality sensing data, $\max \sum_t\lvert\cup_i\mathcal L_i^h\rvert+\lvert\cup_j\mathcal L_j\rvert\eta_p^t$, under task-budget and per-UAV energy constraints; the UAV subproblem is a continuous-action MDP maximizing discounted collection, calibration, and energy-aware reward.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Participant sensing assignment | $x_i(k^t,p^t)$ | binary, $\{0,1\}$ | Whether participant $i$ senses point $p^t$ in slot $k^t$ |
| Maximum offered reward | $c_p^f(k^t)$ | continuous, nonnegative | Highest reward offered for one data item at a point |
| UAV acceleration | $a_j^k=(\theta_j^a,d_j^a)$ | continuous, $\theta_j^a\in[0,2\pi)$ and $d_j^a\in[0,d_{max}]$ | Direction and acceleration chosen for UAV $j$ |
| UAV sensing and calibration action | $\pi_j(s^k)$ | continuous policy | Motion policy balancing collection and participant calibration |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| 1a | Total participant payments do not exceed the sum of task budgets, $\sum c(\mathcal L_i)\leq\sum_t B^t$ |
| 1b | Each UAV respects its battery budget, $\sum_{t,k^t}e_j(k^t)\leq E_j$ |
| Motion | UAV speed and acceleration are bounded by $v_{max}$ and $d_{max}$ |
| Safety | Obstacle collisions and leaving the sensing region incur penalties and are avoided by the learned policy |
| Coverage | Each point is collected only up to its task-specific sensing requirement |

**Algorithm**: Compute basic and DRL-based floating rewards, rank scarce points with a Shapley-value mechanism, and recommend tasks using predicted participant quality; formulate UAV position, energy, participant, obstacle, and completion information as an MDP; train separate CNN-assisted MADDPG actor and critic policies for each UAV; then calibrate participant data with the system-level estimator.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Gao et al. [x] studied UAV-assisted multi-task allocation for mobile crowd sensing in which human participants and UAVs jointly collect data and UAVs also calibrate participant sensors. They formulated a budgeted maximum-coverage objective for high-quality sensing data and a continuous-control UAV scheduling problem whose reward combines data collection, calibration, energy use, and safety penalties. Their UMA method combines an online incentive mechanism, task recommendation and participant-quality prediction, Shapley-based point ranking, and CNN-assisted MADDPG trajectory scheduling. Simulations report a 90.1% covered-collection-ratio gain over participant-only sensing at 200 points of interest and a 13.3% energy-efficiency gain over UAV-only sensing at a 12 m sensing range, together with gains in task fairness and calibration.

## Problem

Human participants in mobile crowd sensing may not visit all points of interest because of traffic, road conditions, or daily-route bias. UAVs can supplement human coverage and calibrate noisy human sensors, but they add battery, trajectory, and collision constraints. The paper jointly asks which participants should be rewarded and how UAVs should move across multiple sensing tasks.

## System model

- There are multiple concurrent sensing tasks, each with a budget, a set of points of interest, data-piece requirements, and quality goals.
- Human participants provide sensed data when they visit points of interest.
- UAVs collect from uncovered points and calibrate participant sensors when they encounter participants.
- UAV motion uses velocity/acceleration constraints, energy proportional to distance, finite battery capacity, and obstacle/border penalties.

## Method

UMA has two coupled parts. The participant side uses a basic reward plus a DRL-derived floating reward, ranks rarely sensed and important points with a Shapley-value idea, and predicts participant quality through a semi-Markov quality model. The UAV side is an MDP whose state includes UAV position/energy, participant positions/calibration timing, obstacles, and point completion; actions are UAV direction and acceleration; rewards trade data collection, calibration meetings, energy, and safety penalties. The multi-UAV controller is trained with MADDPG and CNN feature extraction.

## Key findings

- Simulations use Rome taxi mobility traces, OpenSense Zurich, Beijing air-quality data, and map-offset correction data.
- The parsed default setting has 98 candidates, 5 UAVs, sensing range 15 m, 300 points of interest, 6 tasks, budget 2000 units, and 17 time slots.
- DJI Mavic 2 parameters include max speed 20 m/s, max flight distance 18000 m, and acceleration range [0, 5] m/s^2.
- UMA improves covered collection ratio by 90.1% over participant-only sensing at 200 points of interest and improves energy efficiency by 13.3% over UAV-only sensing at 12 m sensing range.
- Reported covered-collection-ratio gains include 11.0% over TARP at 200 points, 25.0% over Reward M at 280 points, and 54.2% over MADDPG in the UAV-count setting.
- Calibration improves calibrating ratio by 56.9% over PoI M and Reward M at 5 UAVs; the Bayesian estimator reduces calibration error by 69.4% versus GMR at 2 calibration times in OpenSense Zurich.

## Relation to the corpus

This is not MEC offloading, but it is close to the corpus's UAV data-collection branch. It broadens [[uav-data-collection]] from IoT/WSN collection toward human-participant mobile crowd sensing, with UAVs serving both coverage and calibration roles. It also gives [[maddpg]] a non-offloading multi-UAV scheduling case where the reward blends collection utility, energy, and safety.

## Limitations / extraction notes

The local parse is noisy and does not expose DOI, venue, or issue metadata in the header; the bibliographic fields above are title-matched DOI metadata. The paper's own discussion leaves open how to determine point-of-interest counts, sensing-data-piece counts, and quality confidence intervals.

## Raw artifacts

- Parse: `raw/sources/A_UAV-Assisted_Multi-Task_Allocation_Method_for_Mobile_Crowd_Sensing/A_UAV-Assisted_Multi-Task_Allocation_Method_for_Mobile_Crowd_Sensing.md`
- Origin PDF: `raw/sources/A_UAV-Assisted_Multi-Task_Allocation_Method_for_Mobile_Crowd_Sensing/A_UAV-Assisted_Multi-Task_Allocation_Method_for_Mobile_Crowd_Sensing.pdf`
- Figures: `raw/sources/A_UAV-Assisted_Multi-Task_Allocation_Method_for_Mobile_Crowd_Sensing/images/`
