---
type: source
title: "A UAV-Assisted Multi-Task Allocation Method for Mobile Crowd Sensing"
authors: ["Hui Gao", "Jianhao Feng", "Yu Xiao", "Bo Zhang", "Wendong Wang"]
year: 2023
url: "https://doi.org/10.1109/TMC.2022.3147871"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, mobile-crowd-sensing, uav-data-collection, multi-task-allocation, incentives, maddpg, calibration]
related:
  - "[[uav-assisted-mobile-crowd-sensing]]"
  - "[[uav-data-collection]]"
  - "[[maddpg]]"
  - "[[semi-markov-decision-process]]"
  - "[[edge-intelligence]]"
created: 2026-07-10
updated: 2026-07-10
---

# A UAV-Assisted Multi-Task Allocation Method for Mobile Crowd Sensing

## Citation

Gao, H., Feng, J., Xiao, Y., Zhang, B., & Wang, W. (2023). *A UAV-Assisted Multi-Task Allocation Method for Mobile Crowd Sensing*. **IEEE Transactions on Mobile Computing**, 22(7), 3790-3804. DOI: 10.1109/TMC.2022.3147871.

## TL;DR

Proposes UMA, a UAV-assisted mobile-crowd-sensing framework that assigns sensing tasks to human participants while scheduling UAVs to cover missed points of interest and calibrate human sensor data. The method combines online incentives, participant quality prediction, Shapley-style point importance, and MADDPG UAV scheduling.

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
