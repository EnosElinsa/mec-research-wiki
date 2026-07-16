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
updated: 2026-07-16
modeling_card: required
---

# Multi-Agent Reinforcement Learning Based Resource Management in MEC- and UAV-Assisted Vehicular Networks

## Citation

Peng, H., & Shen, X. (2020). *Multi-Agent Reinforcement Learning Based Resource Management in MEC- and UAV-Assisted Vehicular Networks*. **IEEE Journal on Selected Areas in Communications**. DOI: 10.1109/JSAC.2020.3036962. (Manuscript received July 15, 2020; date of publication November 10, 2020; date of current version December 16, 2020 → year 2020.)

## TL;DR

**Multi-dimensional resource management** for UAV-assisted vehicular networks, where a macro eNodeB and a UAV — both carrying **MEC** servers — cooperatively make **vehicle-association** and **resource-allocation** decisions. With no central controller, allocation is posed as a **distributive optimization** maximizing the number of offloaded tasks subject to heterogeneous QoS, and solved with a **multi-agent DDPG (MADDPG)** method: the MEC servers act as learning agents, trained centrally offline and executing rapidly online. The MADDPG scheme converges within ~200 training episodes (comparable to single-agent DDPG) and achieves higher delay/QoS satisfaction ratios than single-agent DDPG (SADDPG) and random schemes.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A macro eNodeB and $U$ MEC-equipped UAVs serve moving vehicles without a central controller. Each vehicle has a task with data size $c_i^s(t)$, CPU workload $c_i^c(t)$, and delay tolerance $c_i^d(t)$, and associates with either the MeNB or one UAV.

**Problem & objective**: Each MEC server maximizes the number of associated tasks whose completion time and caching requirement are satisfied, using the indicator objective $\sum_i b_{i,m}(t)H[c_i^d(t)-T_i(t)]H[f_{i,m}^{ca}(t)C_m^{ca}-c_i^s(t)]$ for the MeNB and the analogous UAV objective.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Association | $b_{i,m}(t),b_{i,j}(t)$ | binary | Vehicle $i$ chooses MeNB $m$ or UAV $j$ |
| Spectrum fraction | $f_{i,m}(t),f_{i,j}(t)$ | continuous, $[0,1]$ | Spectrum share at the selected MEC server |
| Computing fraction | $f_{i,m}^{co}(t),f_{i,j}^{co}(t)$ | continuous, $[0,1]$ | CPU share |
| Caching fraction | $f_{i,m}^{ca}(t),f_{i,j}^{ca}(t)$ | continuous, $[0,1]$ | Cache share |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Association is binary: $b_{i,m}(t),b_{i,j}(t)\in\{0,1\}$ |
| C2 | A vehicle in overlapping coverage selects one server: $b_{i,m}(t)+b_{i,j}(t)=1$ |
| C3 | Resource fractions lie in $[0,1]$ |
| C4 | MeNB spectrum shares sum to one: $\sum_i b_{i,m}f_{i,m}=1$ |
| C5 | MeNB computing shares sum to one: $\sum_i b_{i,m}f_{i,m}^{co}=1$ |
| C6 | MeNB caching shares sum to one: $\sum_i b_{i,m}f_{i,m}^{ca}=1$ |
| C7 | UAV analogues hold: $\sum_i b_{i,j}f_{i,j}=\sum_i b_{i,j}f_{i,j}^{co}=\sum_i b_{i,j}f_{i,j}^{ca}=1$ |

**Algorithm**: Recast the coupled per-server problems as a partially observable Markov game, use each MEC server as an agent, and train a cooperative MADDPG with centralized critics and decentralized execution; shape rewards from delay and caching satisfaction.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Peng and Shen [x] formulate distributed resource management for a macro eNodeB and MEC-equipped UAVs serving heterogeneous vehicular tasks. The objective maximizes the number of tasks meeting both completion-delay and caching requirements while vehicle association, spectrum, computing, and caching fractions remain coupled across servers. They transform the mixed-integer allocation problems into a partially observable Markov game and solve them with cooperative MADDPG using centralized offline training and decentralized execution. The reported simulations show convergence within about 200 training episodes and higher delay and QoS satisfaction ratios than single-agent DDPG and random allocation.

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
