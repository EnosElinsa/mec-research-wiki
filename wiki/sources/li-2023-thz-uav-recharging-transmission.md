---
type: source
title: "A Cooperative Recharging-Transmission Strategy in Powered UAV-Aided Terahertz Downlink Networks"
authors: ["Qi Li", "Amiya Nayak", "Yibo Zhang", "F. Richard Yu"]
year: 2023
url: "https://doi.org/10.1109/TVT.2022.3227989"
venue: "IEEE Transactions on Vehicular Technology, 72(4)"
modeling_card: required
tags: [source, terahertz-communication, wireless-power-transfer, uav-placement, sub-band-association, alternating-optimization, knapsack]
related:
  - "[[terahertz-communication]]"
  - "[[wireless-power-transfer]]"
  - "[[harvest-transmit-store-scheduling]]"
  - "[[drone-cell-3d-placement]]"
  - "[[device-association]]"
  - "[[uav-charging-scheduling]]"
created: 2026-11-02
updated: 2026-11-03
---

# A Cooperative Recharging-Transmission Strategy in Powered UAV-Aided Terahertz Downlink Networks

## Citation

Li, Q., Nayak, A., Zhang, Y., & Yu, F. R. (2023). *A Cooperative Recharging-Transmission Strategy in Powered UAV-Aided Terahertz Downlink Networks*. **IEEE Transactions on Vehicular Technology, 72**(4). DOI: 10.1109/TVT.2022.3227989.

## TL;DR

Hovering UAVs harvest energy from a central charging base station (CBS) and then forward content to blocked users over terahertz links in a save-then-transmit timeslot. The paper derives the minimum charging and THz-transmitting windows and minimizes the resulting minimum timeslot requirement (MTR) by alternating UAV placement and UAV-to-user THz sub-band association.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A three-tier cell of radius $R_c$ with a CBS at the center, $M$ UAVs hovering at fixed altitude $H$, and $K$ users whose direct reception is blocked. Each timeslot has a wireless charging window $T_c$, in which UAVs harvest energy from the CBS, and a THz-transmitting window $T_z$, in which they forward requested content. The THz band of bandwidth $W_u$ is split into $L$ sub-bands with molecular absorption in the path loss.

**Problem & objective**: Problem (13), a mixed-integer nonconvex problem: $\min_{(\mathcal X,\mathcal Y),\omega} MTR$, the average minimum timeslot length $T_c+T_z$ that lets every user receive its content.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV placement | $(x^u_m,y^u_m)\in(\mathcal X,\mathcal Y)$ | continuous, within radius $R_c$ | Horizontal hovering position of UAV $m$ |
| Sub-band association | $\omega_{m,k,l}$ | binary | 1 if UAV $m$ serves user $k$ on THz sub-band $l$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| (13b) | Serving range, $\sqrt{(x^u_m)^2+(y^u_m)^2}\le R_c$. |
| (13c) | Each user is served by one UAV on one sub-band, $\sum_m\sum_l\omega_{m,k,l}=1$. |
| (13d) | Each UAV-sub-band pair serves at most one user, $\sum_k\omega_{m,k,l}\le1$. |
| (13e) | Binary association, $\omega_{m,k,l}\in\{0,1\}$. |

**Algorithm**: Alternating optimization. With association fixed, UAV placement is solved by combining interior-point and gradient-descent steps. With placement fixed, the association matrix is transformed into a knapsack-style assignment solved by the Hungarian algorithm. Iterate until the MTR change is below $\varepsilon$.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Li et al. [x] studied a cooperative recharging-transmission strategy for powered UAV-aided terahertz downlink networks, where UAVs with limited energy provide long-term coverage. They proposed a UAV-to-user THz sub-band association scheme to eliminate interference and derived the minimum requirements of the wireless charging window and the THz-transmitting window. A minimization problem of the minimum timeslot requirement was formulated to jointly optimize UAV placement and UAV-to-user THz sub-band association. The nonconvex problem is solved by alternating optimization, where UAV placement combines interior point and gradient descent methods and the association subproblem is solved as a knapsack-style assignment with the Hungarian algorithm after transforming the association matrix. The authors describe the strategy as quasi-optimal; in the reported two-UAV, eight-user simulations it achieves a lower minimum timeslot requirement than a cellular-frequency variant and a baseline strategy from prior work as the path-loss exponent grows.

## Problem framing

UAV location affects both energy-harvesting efficiency from the CBS and THz link quality to users. Co-sub-band and inter-sub-band interference make association and spectrum assignment as important as placement.

## System model

- Save-then-transmit protocol: UAVs first charge from the CBS, then transmit, within the same timeslot.
- Simulation defaults include 16 dB per-sub-band transmit power, 40 dB charging power, a THz carrier chosen to avoid absorption peaks, 10 GHz THz bandwidth, and 20 dBi antenna gains.
- Absorption loss depends only on water-vapor molecules.

## Method

Algorithm 2 initializes placement and association, solves the placement subproblem with Algorithm 1, solves association with the Hungarian algorithm, and repeats until convergence or an iteration limit.

## Key findings

- MTR falls as the number of UAVs grows and rises with the number of users, because dispersed UAVs harvest and transmit less efficiently.
- A larger CBS-to-UAV path-loss coefficient lengthens charging time and MTR for all strategies, but the proposed strategy keeps the lowest MTR against a cellular-frequency variant and the baseline of the earlier powered-UAV work.

## Limitations / future work

UAVs hover at a fixed altitude and the model treats one CBS per cell.

## Relation to the corpus

Couples [[wireless-power-transfer]] from a ground station with [[terahertz-communication]] downlink scheduling, a timeslot split related to [[harvest-transmit-store-scheduling]]. Mobile charging of UAVs by other aircraft appears in [[zhu-2022-aerial-refueling-uav-charging]].

## Raw artifacts

- Parse: `raw/sources/A_Cooperative_Recharging-Transmission_Strategy_in_Powered_UAV-Aided_Terahertz_Downlink_Networks/A_Cooperative_Recharging-Transmission_Strategy_in_Powered_UAV-Aided_Terahertz_Downlink_Networks.md`
- Origin PDF and extracted figures are in the same folder.
