---
type: source
title: "Cooperative Offloading and Resource Management for UAV-Enabled Mobile Edge Computing in Power IoT System"
authors: ["Yi Liu", "Shengli Xie", "Yan Zhang"]
year: 2020
url: "https://doi.org/10.1109/TVT.2020.3016840"
venue: "IEEE Transactions on Vehicular Technology (IEEE TVT)"
tags: [source, uav-mec, cooperative-offloading, resource-management, deep-reinforcement-learning, power-iot, semi-markov]
related:
  - "[[mobile-edge-computing]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[task-offloading]]"
  - "[[deep-q-network]]"
  - "[[semi-markov-decision-process]]"
  - "[[small-cell-mec]]"
  - "[[seid-2021-madrl-multiuav-iot-edge]]"
  - "[[yu-2020-uav-ec-collaborative-offloading]]"
created: 2026-05-31
updated: 2026-05-31
---

# Cooperative Offloading and Resource Management for UAV-Enabled Mobile Edge Computing in Power IoT System

## Citation

Liu, Y., Xie, S., & Zhang, Y. (2020). *Cooperative Offloading and Resource Management for UAV-Enabled Mobile Edge Computing in Power IoT System*. **IEEE Transactions on Vehicular Technology**. DOI: 10.1109/TVT.2020.3016840.

## TL;DR

A **cooperative UAV-enabled MEC** network for the power Internet of Things, where UAVs act as edge servers that not only serve local devices in their own small-cell but can **help neighboring UAVs** execute computation tasks. A cooperative offloading scheme (with interference mitigation from UAVs to devices) maximizes the network's long-term utility over offloading decisions and resource-management policies. Because device demands and channels are random and time-varying, the problem is cast as a **semi-Markov process** and solved with deep-reinforcement-learning algorithms in both **centralized** and **distributed** frameworks.

## Problem framing

Remote power-IoT areas lack computation services; UAV-enabled MEC can supply them, but the service is constrained by UAV capacities and the distinct demands of power-IoT applications. The objective is to maximize long-term network utility under stochastic channel conditions and demand profiles, while mitigating UAV-to-device interference and allowing UAVs to cooperate rather than work in isolation.

## System model

- **Actors.** K UAVs (UAV-enabled edge computing, "UEC" network), each covering a small-cell with N_k devices; a base station.
- **Links.** Device→UAV, UAV→UAV (cooperation), and UAV→BS data rates, each modeled with state-transition probabilities over a channel-rate state space.
- **Decisions.** Per slot, computation-offloading decisions and resource management (local compute vs cooperative compute vs BS), with utility combining communication and computation terms.
- **Stochasticity.** Random device demands and time-varying channels make the long-term utility maximization a **semi-Markov process**.

## Method

- A **two-phase DRL-based offloading algorithm** for the centralized problem using representation learning.
- A **distributed DRL-based algorithm** using a Q-value transferring method, so UAVs need not send all information to the central operator.
- Both target the long-term utility of the cooperative UEC network.

## Key findings

- The proposed centralized and distributed DRL schemes achieve **better performance than non-cooperative UAV edge computing** methods (stated qualitatively; the parse's figures report service drop rate vs UAV computation capability).
- Allowing UAVs to assist neighboring small-cells improves utility relative to isolated per-UAV operation.

## Limitations / future work

Simulation-only; the parse does not enumerate explicit future work beyond the centralized/distributed comparison. Focused on the power-IoT setting with semi-Markov demand/channel dynamics. DOI date of publication 17 Aug 2020 / date of current version 22 Oct 2020 → year 2020.

## Relation to the corpus

An early **cooperative multi-UAV MEC + DRL** entry where UAVs help each other compute, adjacent to [[seid-2021-madrl-multiuav-iot-edge]] (clustered multi-UAV IoT-edge offloading as a stochastic game with MADDPG) and [[yu-2020-uav-ec-collaborative-offloading]] (collaborative UAV + edge-cloud offloading). It anchors the **power-IoT** application within the broader [[multi-uav-assisted-mec]] track and reinforces [[task-offloading]], [[deep-q-network]], and [[small-cell-mec]]. Co-author [[shengli-xie]] (Guangdong University of Technology) also appears in the CMOP-evolutionary lineage.

## Raw artifacts

- `raw/sources/Cooperative_Offloading_and_Resource_Management_for_UAV-Enabled_Mobile_Edge_Computing_in_Power_IoT_System/full.md`
- Original PDF and extracted figures in the same folder.
