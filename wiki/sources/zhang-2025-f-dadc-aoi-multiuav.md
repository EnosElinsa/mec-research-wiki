---
type: source
title: "Age of Information Minimization in UAV-Enabled IoT Networks via Federated Reinforcement Learning"
authors: ["Xuhui Zhang", "Huijun Xing", "Yanyan Shen", "Jie Xu", "Shuguang Cui"]
year: 2025
url: "https://doi.org/10.1109/TWC.2025.3563426"
venue: "IEEE Transactions on Wireless Communications"
modeling_card: required
tags: [source, age-of-information, uav-data-collection, federated-reinforcement-learning, multi-uav, segmented-channel]
related:
  - "[[age-of-information]]"
  - "[[uav-data-collection]]"
  - "[[federated-reinforcement-learning]]"
  - "[[jie-xu]]"
  - "[[shuguang-cui]]"
created: 2026-11-02
updated: 2026-11-03
---

# Age of Information Minimization in UAV-Enabled IoT Networks via Federated Reinforcement Learning

## Citation

Zhang, X., Xing, H., Shen, Y., Xu, J., & Cui, S. (2025). *Age of Information Minimization in UAV-Enabled IoT Networks via Federated Reinforcement Learning*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2025.3563426.

## TL;DR

Several UAVs each collect data in their own area under a segmented channel that is Rician with LoS and Rayleigh when blocked. The paper minimizes average AoI over time allocation, flight direction and distance, device scheduling, and a variable mission completion time, first with DRL for one UAV and then with F-DADC, a federated DRL algorithm across UAVs.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: $N$ UAVs serve $K$ IoT devices, device $k$ assigned to UAV $n$ by $\lambda_{k,n}$, in a $D\times D$ area over slots of length $\varsigma$ within a time block $T$. Each slot splits into flying and hovering time. Devices have battery $E^k_{\max}$ and power $P_k\le P_{\max}$; UAVs have energy $E_{\max}$.

**Problem & objective**: Problem (23): $\min_{T,\varpi,d,S,\tau}\mathcal A$, the average AoI of all IoT devices.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Time allocation | $T$ | per-slot flying and hovering times | Split of each slot |
| Flying direction | $\varpi_{n,t}$ | $[0,2\pi]$ | Heading of UAV $n$ |
| Flying distance | $d_{n,t}$ | nonnegative | Distance moved by UAV $n$ in slot $t$ |
| Scheduling | $S_{n,k,t}$ | binary | UAV $n$ collects from device $k$ in slot $t$ |
| Completion time | $\tau_n$ | $\tau_n\le T$ | Mission completion time of UAV $n$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Each device served by one UAV, $\sum_n\lambda_{k,n}=1$. |
| C2 | Slot time, $t^{\mathrm{fly}}_{n,t}+t^{\mathrm{hov}}_{n,t}=\varsigma$. |
| C3 | Mission completion time, $\tau_n\le T$. |
| C4-C5 | Heading in $[0,2\pi]$ and speed in $[0,V_{\max}]$. |
| C6-C8 | Positions stay in $[0,D]$ and UAV separation satisfies $\lVert q_{n,t}-q_{j,t}\rVert\ge D_U$. |
| C9 | UAV energy, $\sum_t(e_{n,t}+e^{\mathrm{off}}_{n,t})\le E_{\max}$. |
| C10-C11 | Device power $P_k\le P_{\max}$ and transmission energy within $E^k_{\max}$. |
| C12 | Device transmission and UAV offloading times fit within the UAV hovering time. |
| C13 | Scheduled devices per UAV do not exceed $K_{\max}$ (16). |
| C14 | All devices are collected by the end of the mission, (19). |

**Algorithm**: A DRL algorithm handles the single-UAV case with a variable-length horizon; F-DADC extends it to multiple UAVs by federated aggregation of the UAVs' DRL models.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zhang et al. [x] studied UAV-enabled data collection for Internet of Things networks in which multiple UAVs are dispatched to collect data in a timely manner over their designated areas. They considered a segmented channel model in which the air-to-ground channel follows Rayleigh or Rician fading when the line-of-sight link is blocked or unblocked. The average Age of Information of IoT devices is minimized by jointly optimizing the UAV trajectory, collection scheduling, and completion time, a nonconvex problem whose number of variables changes with the completion time. They first proposed a deep reinforcement learning algorithm for the single-UAV case and then extended it to multiple UAVs with a federated learning and deep reinforcement learning algorithm called F-DADC. Numerical results show that the approach outperforms benchmarks in convergence and testing performance, improving the total AoI and the average AoI per device by 45.6% and 45.9% compared with a greedy benchmark.

## Problem framing

AoI depends on when each device is visited, and the mission length is itself a decision, which makes fixed-dimension optimization methods unsuitable.

## System model

- Segmented Rayleigh/Rician fading depends on whether LoS is blocked.
- Devices transmit within their battery budgets.

## Method

Single-UAV DRL followed by federated aggregation across UAVs.

## Key findings

- F-DADC outperforms benchmarks in convergence and testing.
- Total and per-device AoI improve by 45.6% and 45.9% over a greedy benchmark.

## Limitations / future work

UAV-IoT device associations are fixed within one time block, and areas are pre-partitioned among UAVs.

## Relation to the corpus

Applies [[federated-reinforcement-learning]] to [[age-of-information]]-driven [[uav-data-collection]].

## Raw artifacts

- Parse: `raw/sources/Age_of_Information_Minimization_in_UAV-Enabled_IoT_Networks_via_Federated_Reinforcement_Learning/Age_of_Information_Minimization_in_UAV-Enabled_IoT_Networks_via_Federated_Reinforcement_Learning.md`
- Extracted figures are in the same folder; no companion PDF is present.
