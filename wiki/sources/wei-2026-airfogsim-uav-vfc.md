---
type: source
modeling_card: not_applicable
title: "AirFogSim: A Light-Weight and Modular Simulator for UAV-Integrated Vehicular Fog Computing"
authors: ["Zhiwei Wei", "Bing Li", "Rongqing Zhang", "Xiang Cheng", "Liuqing Yang"]
year: 2026
url: "https://doi.org/10.1109/TMC.2025.3641373"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, vehicle-fog-computing, vehicular-mec, uav-enabled-its, task-offloading, resource-allocation, simulation, security, blockchain]
related:
  - "[[airfogsim]]"
  - "[[vehicle-fog-computing]]"
  - "[[vehicular-mec]]"
  - "[[uav-enabled-its]]"
  - "[[task-offloading]]"
  - "[[uav-trajectory-control]]"
  - "[[air-to-ground-channel-model]]"
  - "[[sun-2024-mvtora-postdisaster-vfc]]"
  - "[[peng-2020-maddpg-uav-vehicular]]"
  - "[[ma-2025-pdqn-vehicular-mec]]"
created: 2026-07-06
updated: 2026-07-16
---

# AirFogSim: A Light-Weight and Modular Simulator for UAV-Integrated Vehicular Fog Computing

## Citation

Wei, Z., Li, B., Zhang, R., Cheng, X., & Yang, L. (2026). *AirFogSim: A Light-Weight and Modular Simulator for UAV-Integrated Vehicular Fog Computing*. **IEEE Transactions on Mobile Computing**, 25(5), 6755-6766. DOI: 10.1109/TMC.2025.3641373.

## TL;DR

Introduces [[airfogsim|AirFogSim]], a lightweight modular simulator for UAV-integrated vehicular fog computing. It targets the gap between theoretical UAV/VFC algorithm design and practical validation by providing a structured simulation stack for aerial-ground interactive computing, including communication, computation, mobility, traffic, security, privacy, energy, blockchain, UAV trajectory, task offloading, and resource allocation modules.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Wei et al. [x] introduce AirFogSim, a modular simulator for UAV-integrated vehicular fog computing. The framework combines traffic, mobility, communication, computation, energy, security, privacy, blockchain, trajectory, offloading, and resource-allocation modules in a discrete-time environment. It demonstrates how assignment and optimization algorithms can be evaluated in a controlled aerial-ground setting and exposes interfaces for new policies. As a simulator paper, its central contribution is an evaluation environment rather than one reusable application-specific decision model.

## Problem framing

UAV-integrated VFC adds 3D mobility, UAV battery constraints, aerial-ground channel variation, and road-network dynamics to already complex vehicular fog computing. Real-world experiments are hard to run repeatedly, while many existing simulators are specialized, hard to extend, or missing key UAV/VFC interactions. AirFogSim is positioned as a reusable environment for testing competing algorithms under controlled but high-fidelity system assumptions.

## System model

- The architecture includes vehicles, UAVs, RSUs, and cloud servers across cloud, edge/fog, and cloudlet layers.
- Fog nodes are computationally capable vehicles or low-altitude UAVs; edge servers include RSUs or 5G co-located servers; high-altitude UAVs can act as mobile cloudlets.
- The simulation loop is discrete-time and organized into Traffic Front-End, Fog Node Network Simulation, Environment Scheduler, and Algorithm Application layers.
- Built-in models include 3GPP/WINNER-style path loss, log-normal shadow fading updates, Rayleigh fast fading, task queues, CPU allocation, transmission delay, blockchain, and attack models.

## Method

- Uses SUMO/traci for vehicular traffic and a Python-native UAV mobility module.
- Provides modular managers for communication, computation, mobility, security, privacy, and energy.
- Demonstrates a reliable V2X task-offloading case study using WHO: Window-based Hungarian task assignment plus alternating optimization for resource allocation.
- Also demonstrates PMA authentication, K-Means UAV positioning, and PoS blockchain-enabled task offloading.

## Key findings

- Scenario analysis reports task completion rate dropping from 0.616 in "Low Noise, Low Density" to 0.495 in "High Noise, High Density".
- Scaling fog nodes from 20 to 60 improves completion rate from 0.466 to 0.583; increasing to 100 gives 0.601.
- PMA authentication latency remains below 0.5 ms with 100 nodes and six authentication factors.
- With 50% malicious nodes, standard greedy completion rate is 17.9%, while Auth-Greedy maintains 37.8%.
- WHO reaches near-optimal performance with lower complexity than Gurobi; with 50 task vehicles, it reaches a stable 80% successful task ratio versus 72% for greedy.
- The blockchain case reports certified transactions per second stabilizing around 110 with 50 task vehicles, 50 serving vehicles, and 4 UAVs.

## Limitations / future work

The authors plan to enrich AirFogSim with more diverse missions and robust security models and apply it to broader ITS applications. They also name additional attacks and prevention methods, including cipher and Sybil attacks, as future work; PoW and PoA consensus support is planned, while the current blockchain demonstration uses PoS. The evaluation uses synthetic traffic data in the case study.

## Relation to the corpus

This is the corpus's first simulator/tool source for UAV-integrated [[vehicle-fog-computing]]. It makes the system assumptions behind sources such as [[sun-2024-mvtora-postdisaster-vfc]], [[peng-2020-maddpg-uav-vehicular]], and [[ma-2025-pdqn-vehicular-mec]] more operational: road mobility, queues, channels, task offloading, UAV mobility, and security modules become reusable experimental infrastructure rather than one-off simulation code.

## Raw artifacts

- `raw/sources/AirFogSim_A_Light-Weight_and_Modular_Simulator_for_UAV-Integrated_Vehicular_Fog_Computing/AirFogSim_A_Light-Weight_and_Modular_Simulator_for_UAV-Integrated_Vehicular_Fog_Computing.md`
- Original PDF and extracted figures (`images/`) in the same folder.
