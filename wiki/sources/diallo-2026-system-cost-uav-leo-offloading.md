---
type: source
title: "System Cost Optimization-Based Task Offloading for UAV-Assisted LEO Satellite Networks"
authors: ["Elhadj Moustapha Diallo", "Rong Chai", "Amayika Kakati", "Chao Yang", "Mohamed Basher Omer", "Linji Ye", "Chengchao Liang", "Qianbin Chen"]
year: 2026
url: "https://doi.org/10.1109/TGCN.2026.3654247"
venue: "IEEE Transactions on Green Communications and Networking (IEEE TGCN), vol. 10, pp. 1980-1993"
tags: [source, leo-satellite-edge-computing, space-air-ground-integrated-network, task-offloading, uav-trajectory-control, mobile-edge-computing, mixed-integer-nonlinear-programming]
related:
  - "[[leo-satellite-edge-computing]]"
  - "[[space-air-ground-integrated-network]]"
  - "[[task-offloading]]"
  - "[[uav-trajectory-control]]"
  - "[[mixed-integer-nonlinear-programming]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[linear-programming]]"
  - "[[chen-2024-ulse-game]]"
  - "[[zhang-2024-coma-satellite-offloading]]"
created: 2026-07-07
updated: 2026-07-12
---

# System Cost Optimization-Based Task Offloading for UAV-Assisted LEO Satellite Networks

## Citation

Diallo, E. M., Chai, R., Kakati, A., Yang, C., Omer, M. B., Ye, L., Liang, C., & Chen, Q. (2026). *System Cost Optimization-Based Task Offloading for UAV-Assisted LEO Satellite Networks*. **IEEE Transactions on Green Communications and Networking**, 10, 1980-1993. DOI: 10.1109/TGCN.2026.3654247. The local parse title has "Ofloading"; DOI/venue/page metadata were verified against a title-matched Crossref/IEEE DOI record.

## TL;DR

Optimizes task offloading in a UAV-assisted LEO satellite network where IoT devices send tasks to UAVs and UAVs either compute locally or offload to LEO satellites. The paper minimizes a weighted system cost combining dropped-task penalty and energy consumption by jointly optimizing IoT task transmission, UAV trajectory, transmit power, and offloading/computing schedules.

## Problem

IoT devices in remote or infrastructure-poor areas can generate computation-intensive tasks that exceed local resources. UAVs can collect tasks and relay work to LEO satellites, but the joint task scheduling, resource allocation, UAV trajectory, and task-dropping decision is a nonconvex mixed-integer problem. The paper explicitly includes the cost of dropping tasks predicted to miss their deadlines.

## System model

The model contains multiple LEO satellites, multiple UAVs, and multiple static IoT devices over slotted time. UAVs fly at a fixed altitude, collect tasks from IoT devices over free-space LoS links, and may either compute tasks locally or offload them over UAV-satellite links. Each task has data size, computation intensity, and deadline parameters. System cost combines UAV flight energy, task transmission/execution energy, and weighted task-drop cost.

## Method

The original MINLP is decomposed into four subproblems:

- IoT task-transmission scheduling is relaxed and solved as a linear program.
- UAV trajectory is handled through successive convex approximation and first-order Taylor convexification.
- Power allocation is solved with Lagrange-dual updates.
- Task offloading and computing scheduling use a virtual-time-axis heuristic that prioritizes tighter task deadlines.

The alternating iteration-based algorithm repeats the four blocks until convergence.

## Key findings

- MATLAB/STK simulations over 500 independent trials report convergence within a small number of iterations; the parse reports about six iterations for the three-UAV setting and about nine for the five-UAV setting.
- System cost increases as the number of IoT devices grows and decreases when more UAVs are deployed.
- Increasing satellite computing capability reduces system cost by making satellite offloading more attractive.
- The proposed method reports lower system cost than the compared baselines from the paper's references [29], [33], and [36].
- The proposed method has the lowest task-dropping rate in the reported IoT-count sweep.

## Limitations / future work

The parse assumes direct UAV-satellite links. The conclusion names relay-UAV multi-hop transmission as future work when direct UAV-satellite links are unavailable. The model also uses static IoT devices and single-antenna UAVs/satellites; the paper notes mobility and multi-antenna beamforming as future extensions.

## Relation to the corpus

This source extends the wiki's [[leo-satellite-edge-computing]] and [[space-air-ground-integrated-network]] track from satellite-edge scheduling into UAV-assisted LEO task dropping and energy control. It is close to [[chen-2024-ulse-game]] and [[zhang-2024-coma-satellite-offloading]] on LEO/SAGIN offloading, but it stays in a classical decomposition pipeline rather than a game or CTDE multi-agent RL formulation.

## Raw artifacts

- `raw/sources/System_Cost_Optimization-Based_Task_Offloading_for_UAV-Assisted_LEO_Satellite_Networks/System_Cost_Optimization-Based_Task_Offloading_for_UAV-Assisted_LEO_Satellite_Networks.md`
- Original PDF and extracted figures (`images/`) in the same folder.
