---
type: concept
title: "UAV-Assisted Mobile Crowd Sensing"
tags: [uav, mobile-crowd-sensing, data-collection, incentives, calibration]
related:
  - "[[gao-2023-uav-mcs-uma]]"
  - "[[uav-data-collection]]"
  - "[[maddpg]]"
  - "[[semi-markov-decision-process]]"
  - "[[edge-intelligence]]"
created: 2026-07-10
updated: 2026-07-10
---

# UAV-Assisted Mobile Crowd Sensing

A sensing architecture where human participants and UAVs jointly collect task data. Human participants provide opportunistic coverage through daily movement, while UAVs fill coverage holes and calibrate noisy participant sensors when they meet them.

[[gao-2023-uav-mcs-uma]] uses this pattern in UMA. Participant-side allocation combines incentives, point-importance estimates, and semi-Markov participant-quality prediction. UAV-side scheduling is modeled as an MDP over UAV position, energy, participant positions, calibration timing, obstacles, and point completion, then trained with [[maddpg]].

The concept broadens [[uav-data-collection]] beyond WSN/IoT data harvesting. The collected object is not only device data from fixed sensors; it can be human-carried sensor data whose quality changes by participant, time, and calibration history.
