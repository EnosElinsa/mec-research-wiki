---
type: source
title: "Cooperative Pursuit-Evasion With Low Altitude Wireless Network: A Hierarchical Reinforcement Learning Approach"
authors: ["Zhengzhi Yang", "Yuanhao Cui", "Wenbo Du", "Fanbiao Li", "Yumeng Li"]
year: 2025
url: "https://doi.org/10.1109/GCWkshps68340.2025.11591106"
venue: "2025 IEEE Globecom Workshops (GC Wkshps)"
tags: [source, uav, anti-uav, pursuit-evasion, hierarchical-reinforcement-learning, multi-agent-rl, low-altitude-network]
related:
  - "[[cooperative-uav-pursuit-evasion]]"
  - "[[hierarchical-reinforcement-learning]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[maddpg]]"
  - "[[mappo]]"
  - "[[multi-agent-td3]]"
  - "[[low-altitude-intelligent-network]]"
  - "[[autonomous-uav-swarms]]"
  - "[[zhang-2025-cooperative-anti-uav-isac]]"
created: 2026-07-12
updated: 2026-07-12
---

# Cooperative Pursuit-Evasion With Low Altitude Wireless Network: A Hierarchical Reinforcement Learning Approach

## Citation

Yang, Z., Cui, Y., Du, W., Li, F., & Li, Y. (2025). *Cooperative Pursuit-Evasion With Low Altitude Wireless Network: A Hierarchical Reinforcement Learning Approach*. **2025 IEEE Globecom Workshops (GC Wkshps)**, 1705-1710. DOI: 10.1109/GCWkshps68340.2025.11591106.

## TL;DR

Decomposes multi-UAV interception into Approach, Expand, Surround, Enclose, and Capture subtasks. An upper Q-network selects the current pursuit subtask, while CTDE actor-critic policies generate pursuer accelerations from local observations and the selected subtask.

## Problem

Multiple counter-UAVs must safely encircle a more agile rogue UAV in urban airspace. Monolithic MARL must learn long-horizon formation behavior over a large joint state/action space, while fixed three-stage policies cannot adapt task order to changing geometry. The paper learns both subtask selection and lower-level maneuver control.

## System model

- Homogeneous pursuers and one fixed-policy evader move in a two-dimensional obstacle field at one altitude.
- Continuous acceleration actions are bounded by speed and acceleration limits, while inter-pursuer and building conflicts receive reward penalties rather than being hard-excluded.
- Capture requires proximity and formation geometry around the evader within a finite horizon.
- The title frames a low-altitude wireless network, but the model has no channel, latency, loss, bandwidth, or resource variables and assumes ideal inter-agent communication.

## Method

HCDRL gives each of five subtasks its own shaped reward and completion condition. The upper Q-network selects a subtask from joint observations and receives the lower agents' average reward with exponential duration decay. Lower MADDPG-like actors execute continuous accelerations from local observations plus a one-hot subtask; centralized critics use joint observations/actions during training. A subtask ends when completed or when its duration limit expires.

## Key findings

- Across 1,200 validation episodes, HCDRL reports 89.08% capture probability, 26.63 s mean successful-capture time, 0.0966 average pursuer-pursuer collisions, and 0.1286 average building collisions.
- The best capture-rate baseline, MAC3, reaches 77.91%; the table difference is 11.17 percentage points. HCDRL's 26.63 s is 9.94% below MAC3's 29.57 s.
- HCDRL has the lowest two collision averages among the tested methods, but not the lowest reward variance.
- When the evader speed rises from 1.1 to 1.5 times pursuer speed, capture probability falls from 89.08% to 78.30% and mean capture time rises from 26.63 s to 34.26 s.
- Increasing pursuers from three to five raises capture probability from 89.08% to 95.12% and lowers mean capture time from 26.63 s to 22.74 s in the reported simulation.

## Limitations / parse caveats

Evidence is simulation-only. The model is planar, assumes homogeneous pursuers and ideal communication, exposes broad state information at execution, and evaluates against one fixed TD3 evader-policy distribution. Reward weights and stage thresholds are manually selected. Several speed, safety-distance, and replay-capacity values are OCR-damaged. Publication metadata is absent from the parse and was verified through the exact-title Crossref record; technical claims come only from the parse.

## Relation to the corpus

[[cooperative-uav-pursuit-evasion]] uses [[hierarchical-reinforcement-learning]] for physical interception rather than communication or offloading. It complements the sensing-layer anti-UAV coordination in [[zhang-2025-cooperative-anti-uav-isac]], but the current source assumes rather than optimizes the supporting wireless network.

## Raw artifacts

- Parse: `raw/sources/Cooperative_Pursuit-Evasion_With_Low_Altitude_Wireless_Network_A_Hierarchical_Reinforcement_Learning_Approach/Cooperative_Pursuit-Evasion_With_Low_Altitude_Wireless_Network_A_Hierarchical_Reinforcement_Learning_Approach.md`
- Origin PDF: `raw/sources/Cooperative_Pursuit-Evasion_With_Low_Altitude_Wireless_Network_A_Hierarchical_Reinforcement_Learning_Approach/Cooperative_Pursuit-Evasion_With_Low_Altitude_Wireless_Network_A_Hierarchical_Reinforcement_Learning_Approach.pdf`
- Figures: `raw/sources/Cooperative_Pursuit-Evasion_With_Low_Altitude_Wireless_Network_A_Hierarchical_Reinforcement_Learning_Approach/images/`
