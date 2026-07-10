---
type: concept
title: "UAV-Assisted Mobile Crowd Sensing"
tags: [uav, mobile-crowd-sensing, data-collection, incentives, calibration]
related:
  - "[[gao-2023-uav-mcs-uma]]"
  - "[[guo-2026-aoi-uav-mcs-contract]]"
  - "[[aoi-aware-contract-incentives]]"
  - "[[uav-data-collection]]"
  - "[[age-of-information]]"
  - "[[contract-theory]]"
  - "[[maddpg]]"
  - "[[semi-markov-decision-process]]"
  - "[[edge-intelligence]]"
created: 2026-07-10
updated: 2026-07-11
---

# UAV-Assisted Mobile Crowd Sensing

A sensing architecture where human participants and UAVs jointly collect task data. Human participants provide opportunistic coverage through daily movement, while UAVs fill coverage holes and calibrate noisy participant sensors when they meet them.

[[gao-2023-uav-mcs-uma]] uses this pattern in UMA. Participant-side allocation combines incentives, point-importance estimates, and semi-Markov participant-quality prediction. UAV-side scheduling is modeled as an MDP over UAV position, energy, participant positions, calibration timing, obstacles, and point completion, then trained with [[maddpg]].

[[guo-2026-aoi-uav-mcs-contract]] studies the incentive side directly. UAVs become temporary base stations for congested subregions when average [[age-of-information]] rises, while users choose update frequencies for sensing data. The platform uses [[aoi-aware-contract-incentives]] so both UAVs and users self-select contract items under hidden private types.

The concept broadens [[uav-data-collection]] beyond WSN/IoT data harvesting. The collected object is not only device data from fixed sensors; it can be human-carried sensor data whose quality changes by participant, time, incentives, and calibration history.
