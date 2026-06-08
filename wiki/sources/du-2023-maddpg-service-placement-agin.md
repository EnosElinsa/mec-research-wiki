---
type: source
title: "MADDPG-Based Joint Service Placement and Task Offloading in MEC Empowered Air-Ground Integrated Networks"
authors: ["Jianbo Du", "Ziwen Kong", "Aijing Sun", "Jiawen Kang", "Dusit Niyato", "Xiaoli Chu", "F. Richard Yu"]
year: 2023
url: "https://doi.org/10.1109/JIOT.2023.3326820"
venue: "IEEE Internet of Things Journal (IEEE IoT-J)"
tags: [source, air-ground-integrated-network, service-placement, task-offloading, maddpg, multi-agent-drl, minlp]
related:
  - "[[air-ground-integrated-network]]"
  - "[[service-caching-mec]]"
  - "[[multi-agent-td3]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[mixed-integer-nonlinear-programming]]"
  - "[[task-offloading]]"
  - "[[zhao-2024-caching-service-placement-uav]]"
  - "[[he-2023-fairness-3d-multiuav-maddpg]]"
created: 2026-05-29
updated: 2026-06-08
---

# MADDPG-Based Joint Service Placement and Task Offloading in MEC Empowered Air-Ground Integrated Networks

## Citation

Du, J., Kong, Z., Sun, A., Kang, J., Niyato, D., Chu, X., & Yu, F. R. (2023). *MADDPG-Based Joint Service Placement and Task Offloading in MEC Empowered Air-Ground Integrated Networks*. **IEEE Internet of Things Journal**. DOI: 10.1109/JIOT.2023.3326820.

## TL;DR

A comprehensive **air-ground integrated MEC** framework where UAV-carried edge servers serve IoT devices/UE. The goal is to minimize the long-term average weighted sum of task-completion delay and economic expenditure across all UEs, via service-instance pre-installation/removal, offloading decisions, access control, service-instance selection, and resource allocation. The MINLP is reformulated as an MDP and solved with **MADDPG**, with continuous outputs converted to discrete variables while preserving coupling constraints.

## Problem framing

MEC-empowered AGINs deliver compute for applications like forest-fire monitoring and emergency rescue. The joint service-placement (which apps live on which UAV, under storage limits) + task-offloading problem has integer, binary, and continuous variables and is a tightly-coupled MINLP, hard for traditional optimization, and aims at long-term (not per-slot) cost.

## System model

- **Actors.** UAVs carrying edge servers + service instances; IoT devices and UE (collectively UEs).
- **Decisions.** Service-instance pre-installation/removal (storage-constrained), offloading decision, access control, service-instance selection, UE transmit power, UAV compute-resource assignment.
- **Objective.** Minimize long-term average weighted sum of completion delay + economic expenditure.

## Method

- Reformulate the MINLP as an MDP; solve with **MADDPG** ([[multi-agent-td3]] family / [[centralized-training-decentralized-execution]]).
- Normalize continuous variables and **convert MADDPG's continuous outputs into discrete variables** while preserving coupling constraints between variables.

## Key findings

- Simulations show fast convergence and superior cost minimization (weighted delay + expenditure) versus baselines (qualitative; specific reward curves in the paper).

## Limitations / future work

The conclusion does not enumerate explicit future work beyond the established framework.

## Relation to the corpus

A **service-placement + offloading** entry that complements the QoE-driven UAV caching/placement work [[zhao-2024-caching-service-placement-uav]] (matching+Gibbs) by instead using MADDPG, and joins the MADDPG/MATD3 multi-agent family ([[he-2023-fairness-3d-multiuav-maddpg]], [[zhao-2022-matd3-multiuav-ec-offloading]]). The continuous-to-discrete action conversion is a recurring hybrid-action workaround (cf. [[ma-2025-pdqn-vehicular-mec]]). Shares co-authors Jiawen Kang / Dusit Niyato with [[ye-2025-aigc-diffusion-contract]]. Reinforces [[air-ground-integrated-network]] and [[service-caching-mec]].

## Raw artifacts

- `raw/sources/MADDPG-Based_Joint_Service_Placement_and_Task_Offloading_in_MEC_Empowered_AirGround_Integrated_Networks/full.md`
- Original PDF and extracted figures in the same folder.
