---
type: source
title: "QoS-Aware Scheduling of Airship-Assisted Millimeter Wave Communications for High-Speed Railway"
authors: ["Lei Liu", "Bo Ai", "Yong Niu", "Zhu Han", "Ning Wang"]
year: 2024
url: "https://doi.org/10.1109/TVT.2024.3450693"
venue: "IEEE Transactions on Vehicular Technology, 73(12)"
modeling_card: required
tags: [source, airship, mmwave, high-speed-railway, sagin, flow-scheduling, mobile-relay]
related:
  - "[[high-altitude-platform-station]]"
  - "[[space-air-ground-integrated-network]]"
  - "[[zhu-han]]"
created: 2026-11-02
updated: 2026-11-02
---

# QoS-Aware Scheduling of Airship-Assisted Millimeter Wave Communications for High-Speed Railway

## Citation

Liu, L., Ai, B., Niu, Y., Han, Z., & Wang, N. (2024). *QoS-Aware Scheduling of Airship-Assisted Millimeter Wave Communications for High-Speed Railway*. **IEEE Transactions on Vehicular Technology, 73**(12). DOI: 10.1109/TVT.2024.3450693.

## TL;DR

In a SAGIN, an airship covers a high-speed railway line with mmWave links to the train's mobile relays (MRs) where terrestrial coverage is too costly. The paper maximizes the number of flows whose QoS is met by selecting which MRs are covered in each frame and scheduling time slots to flows with a max-flow ordering algorithm.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: An airship at height $\Delta h$ above the train serves MRs on a straight and curved route. Coverage radius follows from the link budget, $d_{\max}=(k_0G^tG^rP^t/R_s)^{1/\gamma}$. Each frame has $M$ time slots (TSs) and a schedule phase $T_s$; flow $i$ has QoS requirement $\hat q_{i,n}$.

**Problem & objective**: P1: $\max\sum_{n=1}^{N^{frame}}\sum_{i=1}^{N^{flow}_n}Q_{i,n}$, the number of flow-frame pairs whose QoS is satisfied.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| TS assignment | $a_{i,n,m}$ | binary | TS $m$ of frame $n$ schedules flow $i$ |
| QoS indicator | $Q_{i,n}$ | binary | 1 if $q_{i,n}=\frac{\sum_m R_{i,n,m}\Delta t}{T_s+M\Delta t}\ge\hat q_{i,n}$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| (15) | Each TS serves at most one flow, $\sum_i a_{i,n,m}\le1$. |
| MR access | Only MRs within airship coverage in frame $n$ can be scheduled. |
| Per-MR limit | The airship transmits at most one flow to each MR in a frame. |

**Algorithm**: An MR selection algorithm determines which MRs are inside coverage at every frame. A max-flow scheduling algorithm then orders flows within each frame to maximize completed flows.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Liu et al. [x] considered airship-assisted millimeter-wave communication for high-speed railway in the space-air-ground integrated network, motivated by the high cost of covering railway lines with terrestrial base stations alone. They introduced an optimal scheduling problem that maximizes the number of flows satisfying their quality of service requirements between the airship and the train's mobile relays. A mobile relay selection algorithm determines the number of relays within the airship's coverage at every frame, and a max-flow scheduling algorithm built on it increases the number of successfully scheduled flows by optimizing their scheduling order. Simulation results show that the algorithm improves the number of successfully scheduled flows and transmitted bits, with gains of 36% and 131% over two baselines after 1,900 frames in one setting. The results also show that performance improves further as the number of mobile relays increases.

## Problem framing

Trains move fast along lines through remote areas, so terrestrial mmWave coverage is expensive. An airship can cover a long section, but coverage geometry and flow QoS make frame-by-frame scheduling necessary.

## System model

- Route geometry includes a straight segment and a curve of radius $r$, which changes how long MRs remain covered.
- Flow throughput depends on the TSs it receives in a frame.

## Method

MR selection uses the coverage geometry; max-flow scheduling picks the order of flows per frame.

## Key findings

- After 1,900 frames, the algorithm outperforms RC by 36% and SMR2 by 131% in completed flows, and RC by 21% and SMR1 by 85% in another case.
- At $v=100$ km/h, transmitted bits are 20% higher than RC; at $\mathrm{QoS}_{max}=3$ Gbps, completed flows exceed RC by 10% and SMR1 by 120%, with 34% more bits than RC.
- Route curvature radius and airship height affect the number of completed flows.

## Limitations / future work

The model uses one airship and a fixed route geometry.

## Relation to the corpus

An airship-based [[high-altitude-platform-station]] application within [[space-air-ground-integrated-network]] railway coverage.

## Raw artifacts

- Parse: `raw/sources/QoS-Aware_Scheduling_of_Airship-Assisted_Millimeter_Wave_Communications_for_High-Speed_Railway/QoS-Aware_Scheduling_of_Airship-Assisted_Millimeter_Wave_Communications_for_High-Speed_Railway.md`
- Origin PDF and extracted figures are in the same folder.
