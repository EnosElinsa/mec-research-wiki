---
type: source
title: "Intelligent Heterogeneous Aerial Edge Computing for Advanced 5G Access"
authors: ["Tri-Hai Nguyen", "Thanh Phung Truong", "Anh-Tien Tran", "Nhu-Ngoc Dao", "Laihyuk Park", "Sungrae Cho"]
year: 2024
url: "https://doi.org/10.1109/TNSE.2024.3371434"
venue: "IEEE Transactions on Network Science and Engineering, 11(4)"
modeling_card: required
tags: [source, hierarchical-aerial-mec, noma, partial-offloading, maddpg, high-altitude-platform-station, resource-allocation]
related:
  - "[[hierarchical-aerial-mec]]"
  - "[[noma]]"
  - "[[maddpg]]"
  - "[[binary-vs-partial-offloading]]"
  - "[[high-altitude-platform-station]]"
created: 2026-11-02
updated: 2026-11-02
---

# Intelligent Heterogeneous Aerial Edge Computing for Advanced 5G Access

## Citation

Nguyen, T.-H., Truong, T. P., Tran, A.-T., Dao, N.-N., Park, L., & Cho, S. (2024). *Intelligent Heterogeneous Aerial Edge Computing for Advanced 5G Access*. **IEEE Transactions on Network Science and Engineering, 11**(4). DOI: 10.1109/TNSE.2024.3371434.

## TL;DR

One HAP and several UAVs act as aerial computing platforms (ACPs) for IoT devices using NOMA uplinks. The paper minimizes the devices' delay-and-energy cost over association, partial offloading ratio, transmit power, and ACP computing allocation, modeled as a multi-agent MDP and solved with MADDPG plus an action pretreatment function.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: $K$ IoT devices (IoTDs) offload tasks to $N$ ACPs (UAVs and a HAP) over NOMA with SIC; ACP $n$ has bandwidth $W_n$ and computing capacity $F_n$. Each task has size $s_k[t]$, cycles per bit $w_k[t]$, and deadline $d_k[t]$; part $o_k[t]$ is offloaded and the rest computed locally.

**Problem & objective**: (P1): $\min_{\{a_{k,n}[t],o_k[t],p_k[t],f_{k,n}[t]\}}\sum_{k\in\mathcal K}C_k[t]$, the total weighted delay and energy cost of IoTDs.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Association | $a_{k,n}[t]$ | binary | IoTD $k$ associated with ACP $n$ |
| Offloading ratio | $o_k[t]$ | $[0,1]$ | Share of the task offloaded |
| Transmit power | $p_k[t]$ | $[0,p_{\max}]$ | IoTD uplink power |
| Computing | $f_{k,n}[t]$ | nonnegative | CPU allocated by ACP $n$ to IoTD $k$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| (15b)-(15c) | Binary association, at most one ACP per IoTD. |
| (15d) | $o_k[t]\in[0,1]$. |
| (15e) | $0\le p_k[t]\le p_{\max}$. |
| (15f) | ACP capacity, $\sum_ka_{k,n}f_{k,n}\le F_n$. |
| (15g) | Offloading needs an associated ACP, positive power, and computing. |
| (15h) | Deadline, $T_k[t]\le d_k[t]$. |

**Algorithm**: Model the problem as a multi-agent MDP in which the HAP and each UAV are agents, and solve it with MADDPG under centralized training and decentralized execution; an action pretreatment function maps raw actions to feasible associations and allocations.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Nguyen et al. [x] presented a multi-aerial computing platform enabled NOMA edge network in which heterogeneous platforms, such as unmanned aerial vehicles and a high-altitude platform with edge computing capabilities, provide computational assistance to Internet of Things devices. To minimize delay and energy consumption, they formulated a joint task offloading and resource allocation problem over device association, offloading ratio, transmit power, and computational resource allocation. Because of its complexity, the problem is modeled as a multi-agent Markov decision process and solved with a multi-agent deep deterministic policy gradient framework with an action pretreatment function. Extensive simulations show that the framework reduces task computation overhead, cutting episode cost by about 30% compared with single-agent DDPG and by factors of 2.4 to 3.44 compared with full offloading, random, and greedy schemes.

## Problem framing

UAVs are close but small; the HAP is large but far. NOMA lets several IoTDs share an ACP's uplink, and partial offloading uses local CPUs too.

## System model

- NOMA uplink rates with SIC ordering at each ACP.
- Local delay and energy follow CPU frequency and effective capacitance.

## Method

MADDPG with action pretreatment for feasibility.

## Key findings

- Episode cost falls by about 30% versus DDPG and by 2.4, 2.99, and 3.44 times versus FULL, RANDOM, and GREEDY.
- Task success rate is about 95% at 0.8 Mbit tasks and about 70% at 1.2 Mbit.
- More agents improve over single-agent DDPG by about 35% and 59% in two scenarios.

## Limitations / future work

The authors plan to adapt the algorithm to further system and application scenarios.

## Relation to the corpus

A NOMA-based instance of [[hierarchical-aerial-mec]] with [[binary-vs-partial-offloading]] decisions learned by [[maddpg]].

## Raw artifacts

- Parse: `raw/sources/Intelligent_Heterogeneous_Aerial_Edge_Computing_for_Advanced_5G_Access/Intelligent_Heterogeneous_Aerial_Edge_Computing_for_Advanced_5G_Access.md`
- Origin PDF and extracted figures are in the same folder.
