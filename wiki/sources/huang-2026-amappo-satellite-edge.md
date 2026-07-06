---
type: source
title: "Cost-Aware Dependent Task Offloading and Resource Allocation for Satellite Edge Computing: An Asynchronous Deep Reinforcement Learning Approach"
authors: ["Hualong Huang", "Hancong Duan", "Wenhan Zhan", "Geyong Min", "Kai Peng", "Yuchuan Lei"]
year: 2026
url: "https://doi.org/10.1109/TMC.2025.3645456"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, satellite-edge-computing, sagin, uav-assisted-sec, dag, task-offloading, resource-allocation, asynchronous-marl, mappo, gnn]
related:
  - "[[leo-satellite-edge-computing]]"
  - "[[space-air-ground-integrated-network]]"
  - "[[interdependent-tasks-dag]]"
  - "[[task-offloading]]"
  - "[[matching-theory-for-resource-allocation]]"
  - "[[mappo]]"
  - "[[graph-neural-network]]"
  - "[[cheng-2019-sagin-iot-offloading-rl]]"
  - "[[cheng-2025-dos-satellite-edge-computing]]"
  - "[[qin-2025-matd3-noma-queue-sagin]]"
  - "[[huang-2023-mu-aec-task-energy]]"
created: 2026-07-06
updated: 2026-07-06
---

# Cost-Aware Dependent Task Offloading and Resource Allocation for Satellite Edge Computing: An Asynchronous Deep Reinforcement Learning Approach

## Citation

Huang, H., Duan, H., Zhan, W., Min, G., Peng, K., & Lei, Y. (2026). *Cost-Aware Dependent Task Offloading and Resource Allocation for Satellite Edge Computing: An Asynchronous Deep Reinforcement Learning Approach*. **IEEE Transactions on Mobile Computing**, 25(6), 7782-7799. DOI: 10.1109/TMC.2025.3645456.

## TL;DR

A UAV-assisted satellite edge computing (SEC) framework for remote IoT applications whose tasks are interdependent DAGs. IoTDs in spacious regions can communicate directly with LEO satellites; IoTDs in obstructive regions use UAVs as mobile access points / edge servers and relays toward satellites or cloud servers. The method decomposes the joint MINLP into IoTD-UAV association, multi-application DAG sequencing, and asynchronous graph-aware MAPPO (AMAPPO) for offloading and resource allocation.

## Problem

Satellite edge computing extends service to remote IoT regions, but direct IoTD-to-LEO links are costly or unreliable in obstructive terrain. UAV relays improve coverage, yet dynamic LEO visibility, constrained UAV / satellite resources, and DAG task dependencies make synchronous, independent-task MARL a poor fit. The paper minimizes a system cost combining latency and energy while satisfying application latency requirements.

## System model

- **Tiers:** IoTDs, UAVs with edge servers, LEO satellites with edge servers, and cloud servers reached through the satellite backbone.
- **Regions:** spacious areas such as deserts support direct IoTD-to-LEO transmission; obstructive areas such as jungles use UAV relay / service.
- **Tasks:** each IoTD application is a DAG; predecessor tasks must finish before successors can execute, and intermediate outputs may need transmission across tiers.
- **Links:** G2U, U2S, G2S, inter-satellite / satellite-backbone links, and cloud backhaul are all considered in the SEC architecture.
- **Decisions:** IoTD-UAV association, transmit power, task offloading location, bandwidth / communication resources, and compute resources.

## Method

The paper first solves IoTD association with a one-to-many matching algorithm. It then uses MATS (multi-application task sequence) to merge multiple DAG applications and sort task execution order. The main learning component is AMAPPO: an asynchronous GNN-augmented MAPPO framework with a graph-aware encoder-decoder, so agents can act after completing their own tasks rather than waiting for synchronous global decision epochs.

## Key findings

- On the reported real-world-dataset simulations, AMAPPO + matching + MATS converges faster and more stably than the ablated variants and benchmark MARL methods.
- With 200 IoTDs, the proposed method consumes about **10.3% less energy** than MAPPO in the reported comparison.
- With 50 DAG tasks, the proposed method consumes about **16.3% less energy** than IPPO and is about **10.9% faster** than MAPPO.
- At 1.6 Gcycles task demand, the paper reports an **11.3%** energy reduction versus MAPPO.
- Under heavy shadowing, it reports at least **12.1%** lower energy than MAPPO / IPPO and **13.9%** lower latency than A-PPO.

## Limitations / future work

The paper is simulation-based. UAV placement, LEO constellation structure, and cloud connectivity are modeled rather than deployed. The system handles DAG dependencies and asynchronous action timing, but does not report real satellite/UAV experiments or full protocol-stack implementation. Exact robustness beyond the evaluated shadowing and coverage scenarios is not established in the parse.

## Relation to the corpus

This extends the [[space-air-ground-integrated-network]] / [[leo-satellite-edge-computing]] track with three distinguishing ingredients: DAG applications ([[interdependent-tasks-dag]]), UAV-assisted SEC across direct and relay regions, and asynchronous graph-aware MARL. It is closer to [[cheng-2019-sagin-iot-offloading-rl]] in architecture, but newer than the single-satellite energy-control framing in [[cheng-2025-dos-satellite-edge-computing]]. Methodologically it adds a GNN + [[mappo]] datapoint to the corpus's structured-MARL theme and complements the DAG scheduling already represented by [[huang-2023-mu-aec-task-energy]].

## Raw artifacts

- `raw/sources/Cost-Aware Dependent Task Offloading and Resource Allocation for Satellite Edge Computing An Asynchronous Deep Reinforcement Learning Approach/Cost-Aware Dependent Task Offloading and Resource Allocation for Satellite Edge Computing An Asynchronous Deep Reinforcement Learning Approach.md`
- Original PDF and extracted figures (`images/`) in the same folder.
