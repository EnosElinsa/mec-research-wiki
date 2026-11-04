---
type: source
title: "Aerial Refueling: Scheduling Wireless Energy Charging for UAV Enabled Data Collection"
authors: ["Kun Zhu", "Jia Yang", "Yang Zhang", "Jiangtian Nie", "Wei Yang Bryan Lim", "Hongliang Zhang", "Zehui Xiong"]
year: 2022
url: "https://doi.org/10.1109/TGCN.2022.3164602"
venue: "IEEE Transactions on Green Communications and Networking, 6(3)"
modeling_card: required
tags: [source, uav-to-uav-wireless-charging, wireless-power-transfer, uav-data-collection, ddpg, maddpg, markov-game]
related:
  - "[[in-flight-uav-energy-replenishment]]"
  - "[[wireless-power-transfer]]"
  - "[[uav-charging-scheduling]]"
  - "[[uav-data-collection]]"
  - "[[ddpg]]"
  - "[[maddpg]]"
  - "[[zehui-xiong]]"
  - "[[wei-yang-bryan-lim]]"
created: 2026-11-02
updated: 2026-11-03
---

# Aerial Refueling: Scheduling Wireless Energy Charging for UAV Enabled Data Collection

## Citation

Zhu, K., Yang, J., Zhang, Y., Nie, J., Lim, W. Y. B., Zhang, H., & Xiong, Z. (2022). *Aerial Refueling: Scheduling Wireless Energy Charging for UAV Enabled Data Collection*. **IEEE Transactions on Green Communications and Networking, 6**(3). DOI: 10.1109/TGCN.2022.3164602. A preliminary version appeared at WASA 2021.

## TL;DR

Inspired by aircraft aerial refueling, charging UAVs (CUAVs) wirelessly recharge mission UAVs (MUAVs) in flight so data collection never pauses for landing. After checking feasibility with commercial UAV parameters, the paper schedules CUAV paths and charging targets to minimize mission completion time, using DDPG for one CUAV and MADDPG with adaptive parameter-space noise for several.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: MUAVs follow pre-planned paths over a 2-D area with obstacles, hovering at points of interest (PoIs) $P_i$ for collection time $Dt(P_i)$. One or more CUAVs fly with the MUAVs and charge an adjacent MUAV wirelessly; the feasibility analysis uses DJI parameters for RF charging at about 0.5 m and for laser charging. All UAVs move a constant distance $l$ per slot at speed $v$. Ground charging stations, fixed platforms, and charging vehicles are the alternatives.

**Problem & objective**: Minimize the average mission completion time $\frac1n\sum_{i=1}^n T_i$, where $T_i=Tm_i+Tc_i+Tw_i$ sums moving, data-collection, and waiting-to-be-charged times, modeled as an MDP for one CUAV and a Markov game for several.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| CUAV moving direction | $\theta_{C^t}$ | continuous 2-D unit direction | Flight direction of the CUAV in slot $t$ |
| Charging target | $C^t$ | discrete, one MUAV or none | Which adjacent MUAV the CUAV charges |
| CUAV action | $A^t$ | hybrid of the two above | Move or charge decision per slot |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| Obstacles | CUAVs avoid blocks and the area boundary. |
| Energy safety | An MUAV must be recharged before its energy falls below the safety threshold. |
| Charging geometry | The CUAV moves or hovers together with the target MUAV while charging it. |
| Mission | The mission ends when all PoI data are collected and MUAVs return to the station. |

**Algorithm**: For one CUAV, DDPG maps a state of MUAV locations, remaining energy, accumulated charged energy, and CUAV status to a continuous direction and a softmax-chosen charging target. For multiple CUAVs, MADDPG with adaptive parameter-space noise learns coordinated charging schedules.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zhu et al. [x] proposed an aerial refueling scheme in which charging UAVs recharge mission UAVs on the fly through wireless power transmission, so that the mission UAVs can operate without interrupting their missions. The feasibility of aerial wireless charging for small UAVs is first discussed and evaluated with parameters of commercial UAV products. They then considered multiple mission UAVs collecting data from several points of interest and formulated the scheduling of each charging UAV's flying path and charging process to minimize the mission time. Deep reinforcement learning based algorithms are proposed for both single and multiple charging UAVs, solving a Markov decision process and a Markov game, respectively. Simulation evaluations show that the scheme improves mission completion and charging efficiency compared with ground-based charging alternatives.

## Problem framing

Landing to recharge, or replacing a depleted UAV, delays completion. Larger batteries add weight. Mobile charging aircraft avoid both, but their routes and charging order must be scheduled.

## System model

- Hovering power follows a thrust-based model for an $N$-rotor UAV.
- Near-field charging at about 90% efficiency is judged feasible, and far-field RF charging is analyzed with the Friis equation.
- Baselines: return to a station for battery replacement, two fixed charging platforms, and a mobile ground charging vehicle, all with the same charging power.

## Method

Actor and critic networks have two hidden layers of 64 neurons; replay holds 600,000 records with 1024-sample updates, learning rate 0.01, discount 0.95, and 60,000 training episodes.

## Key findings

- In-flight charging lets MUAVs finish missions without landing.
- Mission completion time is clearly shorter than with fixed ground charging facilities.

## Limitations / future work

The environment is two-dimensional with static blocks, and MUAV paths are fixed in advance.

## Relation to the corpus

An early learning-based instance of [[in-flight-uav-energy-replenishment]]; the charging-distance physics are analyzed in [[yan-2025-in-flight-uav-charging-distance]]. It complements ground-station [[uav-charging-scheduling]] and [[wireless-power-transfer]] for [[uav-data-collection]].

## Raw artifacts

- Parse: `raw/sources/Aerial_Refueling_Scheduling_Wireless_Energy_Charging_for_UAV_Enabled_Data_Collection/Aerial_Refueling_Scheduling_Wireless_Energy_Charging_for_UAV_Enabled_Data_Collection.md`
- Origin PDF and extracted figures are in the same folder.
