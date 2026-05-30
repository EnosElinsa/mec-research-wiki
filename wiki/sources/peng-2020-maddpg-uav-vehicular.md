---
type: source
title: "Multi-Agent Reinforcement Learning Based Resource Management in MEC- and UAV-Assisted Vehicular Networks"
authors: ["Haixia Peng", "Xuemin Shen"]
year: 2020
url: "https://doi.org/10.1109/JSAC.2020.3036962"
venue: "IEEE Journal on Selected Areas in Communications (IEEE JSAC)"
tags: [source, vehicular-mec, multi-uav-assisted-mec, multi-agent-drl, maddpg, resource-allocation, task-offloading, centralized-training-decentralized-execution]
related:
  - "[[vehicular-mec]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[maddpg]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[task-offloading]]"
  - "[[dynamic-qos-constraints]]"
  - "[[uav-enabled-its]]"
  - "[[ddpg]]"
created: 2026-05-31
updated: 2026-05-31
---

# Multi-Agent Reinforcement Learning Based Resource Management in MEC- and UAV-Assisted Vehicular Networks

## Citation

Peng, H., & Shen, X. (2020). *Multi-Agent Reinforcement Learning Based Resource Management in MEC- and UAV-Assisted Vehicular Networks*. **IEEE Journal on Selected Areas in Communications**. DOI: 10.1109/JSAC.2020.3036962. (Manuscript received July 15, 2020; date of publication November 10, 2020; date of current version December 16, 2020 → year 2020.)

## TL;DR

**Multi-dimensional resource management** for UAV-assisted vehicular networks, where a macro eNodeB and a UAV — both carrying **MEC** servers — cooperatively make **vehicle-association** and **resource-allocation** decisions. With no central controller, allocation is posed as a **distributive optimization** maximizing the number of offloaded tasks subject to heterogeneous QoS, and solved with a **multi-agent DDPG (MADDPG)** method: the MEC servers act as learning agents, trained centrally offline and executing rapidly online. The MADDPG scheme converges within ~200 training episodes (comparable to single-agent DDPG) and achieves higher delay/QoS satisfaction ratios than single-agent DDPG (SADDPG) and random schemes.

## Problem framing

Vehicular networks face growing computation load and limited onboard/spectrum resources. MEC plus UAVs can supply on-demand compute, but with no central controller the association + resource-allocation problem is naturally distributed across the eNodeB and UAV servers — motivating a multi-agent learning formulation that maximizes offloaded tasks while meeting heterogeneous QoS.

## System model

- **Actors.** A macro eNodeB and a UAV, each MEC-equipped, acting as cooperating learning agents serving vehicles.
- **Objective.** Maximize the number of offloaded tasks subject to heterogeneous per-task QoS requirements.
- **Decisions.** Vehicle association + multi-dimensional resource allocation, formulated as a distributive optimization (no central controller).

## Method

- **MADDPG** with **centralized offline training, decentralized online execution** ([[centralized-training-decentralized-execution]]): MEC servers as agents learn association + allocation policies and act quickly at runtime.

## Key findings

- The MADDPG method **converges within 200 training episodes**, comparable to single-agent DDPG (SADDPG) (verbatim from the abstract).
- The MADDPG resource-management scheme achieves **higher delay/QoS satisfaction ratios** than SADDPG and random schemes (qualitative; specific curves in the figures).

## Limitations / future work

No explicit quantitative future-work targets are grounded in the captured parse → `not in parse`.

## Relation to the corpus

An early (2020) **vehicular MEC + UAV** MADDPG entry by the Waterloo group (Haixia Peng; Xuemin Shen). It complements the corpus's vehicular-MEC track ([[zhang-2025-mcma-task-migration]], [[ma-2025-pdqn-vehicular-mec]], [[sun-2023-bargain-match-vec]]) by adding a **UAV-assisted** twist, and joins the MADDPG multi-agent family with [[seid-2021-madrl-multiuav-iot-edge]] and [[wang-2021-maddpg-multiuav-trajectory]] (grounding the shared [[maddpg]] page). Co-author Xuemin Shen also appears on [[duan-2023-moto-smallcell-offloading]]; co-author Haixia Peng recurs in the maritime [[wang-2024-twotier-satellite-marine]] / [[wang-2024-maritime-eh-jcora]] (Xi'an Jiaotong University in those papers).

## Raw artifacts

- `raw/sources/Multi-Agent_Reinforcement_Learning_Based_Resource_Management_in_MEC-_and_UAV-Assisted_Vehicular_Networks/full.md`
- Original PDF (`e792cab5-4bb8-4122-80c1-05a90eb3a865_origin.pdf`) and extracted figures (`images/`) in the same folder.
