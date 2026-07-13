---
type: concept
title: "UAV-Assisted Mobile Crowd Sensing"
tags: [uav, mobile-crowd-sensing, data-collection, incentives, calibration]
related:
  - "[[lim-2021-uav-iov-contract-matching]]"
  - "[[gao-2023-uav-mcs-uma]]"
  - "[[zhou-2026-a2g-madrl-air-ground-vcs]]"
  - "[[guo-2026-aoi-uav-mcs-contract]]"
  - "[[sequential-multi-agent-policy-generation]]"
  - "[[aoi-aware-contract-incentives]]"
  - "[[uav-data-collection]]"
  - "[[age-of-information]]"
  - "[[contract-theory]]"
  - "[[maddpg]]"
  - "[[semi-markov-decision-process]]"
  - "[[edge-intelligence]]"
  - "[[liu-2021-edivert-mobile-crowdsensing]]"
  - "[[guang-2026-hiswta-mcs]]"
created: 2026-07-10
updated: 2026-07-14
---

# UAV-Assisted Mobile Crowd Sensing

A mobile sensing architecture in which UAVs either assist human participants or act as the mobile sensing participants themselves. In the human-assisted form, people provide opportunistic coverage through daily movement while UAVs fill coverage holes and calibrate noisy participant sensors. In the UAV-only form, a mobile swarm senses, relays, and divides collection tasks through an aerial communication hierarchy.

[[gao-2023-uav-mcs-uma]] uses this pattern in UMA. Participant-side allocation combines incentives, point-importance estimates, and semi-Markov participant-quality prediction. UAV-side scheduling is modeled as an MDP over UAV position, energy, participant positions, calibration timing, obstacles, and point completion, then trained with [[maddpg]].

[[guo-2026-aoi-uav-mcs-contract]] studies the incentive side directly. UAVs become temporary base stations for congested subregions when average [[age-of-information]] rises, while users choose update frequencies for sensing data. The platform uses [[aoi-aware-contract-incentives]] so both UAVs and users self-select contract items under hidden private types.

[[zhou-2026-a2g-madrl-air-ground-vcs]] studies the control side with UAV-UGV pairs. Its A2G-MADRL controller uses [[sequential-multi-agent-policy-generation]] to coordinate routes and NOMA channel assignments while optimizing sensing capability-aware AoI and latency-weighted data collection ratio.

[[liu-2021-edivert-mobile-crowdsensing]] broadens the term from UAV assistance to sensing performed directly by unmanned vehicles. Its e-Divert controller coordinates data collection, obstacle avoidance, geographic fairness, and charging-station visits through CTDE actor-critic learning and [[ape-x-actor-learner-replay]].

[[guang-2026-hiswta-mcs]] also treats UAVs as the sensing participants themselves. HISWTA dynamically clusters heterogeneous UAVs, routes information among cluster heads, self-heals weak heads, and uses approximate Shapley values to distribute sensing tasks while controlling communication/task energy imbalance.

The concept broadens [[uav-data-collection]] beyond WSN/IoT data harvesting. Depending on the source, the participants can be humans supported and calibrated by UAVs, or mobile UAVs that directly sense, relay, and execute assigned collection tasks.
