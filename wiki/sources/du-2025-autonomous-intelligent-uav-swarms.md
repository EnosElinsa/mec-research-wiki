---
type: source
title: "A Survey on Autonomous and Intelligent Swarms of Uncrewed Aerial Vehicles (UAVs)"
authors: ["Zhenpeng Du", "Chunbo Luo", "Geyong Min", "Jia Wu", "Cai Luo", "Jian Pu", "Shuai Li"]
year: 2025
url: "https://doi.org/10.1109/TITS.2025.3569500"
venue: "IEEE Transactions on Intelligent Transportation Systems (IEEE T-ITS)"
modeling_card: not_applicable
tags: [source, survey, uav-swarm, autonomy, trajectory-planning, task-assignment, localization, perception, communication]
related:
  - "[[autonomous-uav-swarms]]"
  - "[[uav-trajectory-control]]"
  - "[[b-spline-trajectory]]"
  - "[[particle-swarm-optimization]]"
  - "[[cooperative-perception]]"
  - "[[cellular-connected-uav]]"
  - "[[uav-data-collection]]"
  - "[[uav-mobile-relaying]]"
  - "[[uav-enabled-its]]"
created: 2026-07-10
updated: 2026-07-16
---

# A Survey on Autonomous and Intelligent Swarms of Uncrewed Aerial Vehicles (UAVs)

## Citation

Du, Z., Luo, C., Min, G., Wu, J., Luo, C., Pu, J., & Li, S. (2025). *A Survey on Autonomous and Intelligent Swarms of Uncrewed Aerial Vehicles (UAVs)*. **IEEE Transactions on Intelligent Transportation Systems**, 26(10), 14477-14500. DOI: 10.1109/TITS.2025.3569500.

## TL;DR

Surveys autonomous and intelligent UAV swarms across trajectory planning, task assignment, control, localization, perception, communication, and civil applications. It is useful as a taxonomy anchor for non-MEC swarm autonomy methods that later appear inside UAV-MEC, ITS, sensing, and edge-intelligence papers.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Du et al. [x] surveyed autonomous and intelligent UAV swarms across trajectory planning, task assignment, control, localization, perception, communication, and civil applications. They organized planning methods by synchronous or asynchronous scheduling and centralized or distributed coordination, and reviewed global assignment, local trajectory generation, and task-oriented cooperation. The survey compared algorithmic demands, flexibility, robustness, and efficiency while connecting the enabling hardware and software stack to formation, exploration, tracking, monitoring, logistics, disaster response, and smart-city applications. It identified open problems in scalable hybrid coordination, semantic and learning-based planning, adaptive formations, robust perception, onboard computation, localization, energy, and low-latency communication rather than reporting a new benchmark experiment.

## Scope

The survey organizes swarm autonomy into trajectory planning, cooperative mission behavior, enabling hardware/software, and application domains. It separates scheduling and coordination, global task assignment, local planning, and trajectory generation, then compares centralized and distributed coordination in terms of efficiency, communication overhead, robustness, computational load, and adaptability.

## Methods covered

- Global planning and assignment: TSP-style routing, auctions, genetic algorithms, PSO, ant colony optimization, wolf-pack algorithms, reinforcement learning, and digital twins.
- Local planning and trajectory generation: PRM, RRT/RRT*, A*, D3QN, polynomial curves, Bezier curves, B-splines, MINVO, MINCO, safe-flight corridors, ESDF, EGO-planner, velocity obstacles, ORCA, BVC, MPC, NMPC, and learning-based planners.
- Cooperation modes: formation, exploration, tracking, and monitoring.
- Enabling stack: PX4, Crazyflie, STM32, IMU, GPS, RealSense, LiDAR, Raspberry Pi, NVIDIA Jetson, PID/LQR/DFBC/geometric control/MPC/NMPC, GNSS RTK, VIO, UWB, SLAM, occupancy grids, Wi-Fi, 4G/5G, LoRa, and COFDM.

## Key facts

- The paper spans 24 printed pages and cites 267 references in the local parse.
- Table I summarizes recent survey papers; Table II compares centralized and distributed coordination.
- The survey notes 6-DoF UAV motion, VIO update rates around 200 Hz, agile-control velocities up to 20 m/s, NMPC solve time of 2.7 ms, and DFBC solve time of 0.020 ms in cited examples.
- Communication examples include Wi-Fi LAN latency from a few milliseconds to tens of milliseconds, radio latency of several hundred milliseconds, and 5G URLLC targets below 1 ms with 99.999% reliability.
- It does not contribute a new benchmark experiment or dataset; its role is taxonomy and synthesis.

## Relation to the corpus

This page complements UAV-MEC-specific surveys by exposing the autonomy substrate behind many corpus mechanisms: [[uav-trajectory-control]], [[b-spline-trajectory]], [[particle-swarm-optimization]], cooperative perception, cellular-connected UAVs, UAV data collection, UAV relaying, UAV-ITS, and edge intelligence. It is especially useful for interpreting papers that import robotics-style swarm planning without making those robotics assumptions explicit.

## Limitations / extraction notes

The local Markdown parse is missing top-level DOI, venue, and year; the bibliographic fields above come from the local PDF metadata and first-page evidence. The parse has flattened tables, checkbox artifacts, and corrupted symbols, so detailed table wording should be checked against the PDF before quoting.

## Raw artifacts

- Parse: `raw/sources/A_Survey_on_Autonomous_and_Intelligent_Swarms_of_Uncrewed_Aerial_Vehicles_UAVs-/A_Survey_on_Autonomous_and_Intelligent_Swarms_of_Uncrewed_Aerial_Vehicles_UAVs-.md`
- Origin PDF: `raw/sources/A_Survey_on_Autonomous_and_Intelligent_Swarms_of_Uncrewed_Aerial_Vehicles_UAVs-/A_Survey_on_Autonomous_and_Intelligent_Swarms_of_Uncrewed_Aerial_Vehicles_UAVs-.pdf`
- Figures: `raw/sources/A_Survey_on_Autonomous_and_Intelligent_Swarms_of_Uncrewed_Aerial_Vehicles_UAVs-/images/`
