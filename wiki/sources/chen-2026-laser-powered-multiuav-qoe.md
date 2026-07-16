---
type: source
title: "QoE Maximization for Laser-Powered Multi-UAV Communication Networks"
authors: ["Jianchao Chen", "Ming Jiang"]
year: 2026
url: "https://doi.org/10.1109/TMC.2025.3610026"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), vol. 25, no. 2, pp. 2676-2690"
modeling_card: required
tags: [source, laser-power-transfer, multi-uav, qoe, matching, resource-reallocation, post-disaster-communication]
related:
  - "[[laser-power-transfer]]"
  - "[[gale-shapley-rematching]]"
  - "[[redundant-resource-reallocation]]"
  - "[[qoe-modeling-mec]]"
  - "[[matching-theory-for-resource-allocation]]"
  - "[[device-association]]"
  - "[[wireless-backhaul]]"
created: 2026-07-14
updated: 2026-07-16
---

# QoE Maximization for Laser-Powered Multi-UAV Communication Networks

## Citation

Chen, J., & Jiang, M. (2026). *QoE Maximization for Laser-Powered Multi-UAV Communication Networks*. **IEEE Transactions on Mobile Computing, 25**(2), 2676-2690. DOI: 10.1109/TMC.2025.3610026.

## TL;DR

Places laser-charged UAV access points in a post-disaster downlink, rematches users and laser stations, then reclaims excess power and backhaul from already-qualified users to maximize how many meet rate- and delay-derived QoE thresholds.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A surviving macro base station and multiple laser-powered UAV access points serve ground users, while laser-power-transfer stations charge the UAVs. Users associate with the base station or one UAV, laser stations associate with UAVs, and UAV downlinks share interference while BS-UAV backhaul and optical charging operate in parallel.

**Problem & objective**: The first problem maximizes aggregate average data rate, $P_1:\max_{\mathbf U,\mathbf I,\mathbf L}\sum_{k=1}^{K}r_k^{\mathrm d}(\mathbf U,\mathbf I,\mathbf L,\mathbf P^{[0]})$, and the second problem maximizes the number of QoE-qualified users, $P_2:\max_{\mathbf c^{\mathrm b},\mathbf P}\sum_k\Pr(r_k^{\mathrm d}\ge\mathcal Q_k)$, by reallocating redundant power and backhaul.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV positions | $\mathbf U$ | continuous coordinates | Placement of BS/UAV access points |
| UE association | $\mathbf I$ | binary or integer matching | BS/UAV serving assignment for each user |
| LPTS association | $\mathbf L$ | binary matching | Laser station to UAV assignment |
| Transmit power | $\mathbf P$ | continuous, nonnegative | Per-user BS/UAV transmit powers |
| Backhaul allocation | $\mathbf c^{\mathrm b}$ | continuous, nonnegative | BS-to-UAV capacity allocated to users |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Each user is associated with at most one BS or UAV. |
| C2 | Each BS or UAV serves no more than its maximum associated-user count. |
| C3 | Each UAV is associated with at most one laser-power-transfer station. |
| C4 | Each laser station is assigned to one UAV under the matching rule. |
| C5 | UAV positions stay inside the service region of radius $R_C$. |
| C6 | Distinct UAVs maintain guard distance $d^{\mathrm L}$. |
| C7 | Backhaul allocation is bounded: $\sum_{k\in\mathcal K_m}c_k^{\mathrm b}\le C_m$. |
| C8 | Transmit power is bounded: $\sum_{k\in\mathcal K_m}P_k\le P_m$. |

**Algorithm**: Initialize positions and matches, alternate UE matching and LPTS matching with Gale-Shapley, optimize UAV positions with the convexified L2-norm polynomial program, rematch locally poor pairs with GSRM, then run redundant-resource reallocation using block SCA and quadratic transforms for backhaul and power.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Chen et al. [x] studied post-disaster downlink communication with laser-powered UAV access points, user and laser-station associations, UAV placement, transmit power, and BS-UAV backhaul allocation. They maximized sum average data rate first and then maximized the number of users meeting rate and delay QoE thresholds under association, service-region, anti-collision, backhaul, and power constraints. QWLMU alternates Gale-Shapley matching, GSRM rematching, convexified UAV-position optimization, and redundant-resource reallocation with quadratic transforms. Simulations show positive rematching gains, improved QoE-qualified-user counts at 60 m and 300 m, and higher energy efficiency than the compared LGD-UPS and MWEP schemes.

## Problem and system model

A surviving macro base station and multiple UAV access points serve ground users, while distributed laser-power-transfer stations charge the UAVs. Ground users associate with either the BS or one UAV; each laser station associates with one UAV. BS and UAV access use orthogonal bands, but different UAVs interfere. UAV delivery uses BS-UAV backhaul followed by UAV-user access, while optical charging can continue in parallel.

QoE requires a user-specific minimum average data rate and a mean-opinion-score-derived delay threshold. The decisions are UAV placement, user and laser-station association, transmit power, and backhaul allocation. This is a communication network, not an edge-computing/offloading model.

## Method

The QWLMU procedure first maximizes sum average data rate by alternating placement and association. [[gale-shapley-rematching]] repairs locally poor conventional matches, while an L2-norm polynomial reformulation handles UAV placement. [[redundant-resource-reallocation]] then takes excess power and backhaul from users already meeting QoE and alternates block-SCA/quadratic-transform updates to qualify more users.

## Key findings

- In 10,000 random matching instances, rematching gives positive normalized weight gain over ordinary Gale-Shapley matching and converges after a few iterations.
- In the four-laser-station/four-UAV simulation, increasing laser transmit power from 600 to 2000 W eventually saturates average-data-rate gains.
- The placement-and-association stage outperforms ordinary matching and compared placement methods in system average data rate, especially at low-to-medium altitude or with more users; the text gives no exact margin.
- At the evaluated 60 m and 300 m altitudes, placement optimization increases the number of QoE-qualified users, and redundant-resource reallocation increases it further.
- QWLMU reports higher simulated energy efficiency than the compared LGD-UPS and MWEP methods, without a text-level exact percentage.

## Limitations

Evidence is simulation-only. The first stage converges to a stationary, not globally optimal, solution. Laser alignment is assumed manageable for slowly moving or hovering UAVs; weather, blockage, alignment error, eye safety, and a physical laser-power prototype are not evaluated. Channels and user layouts are synthetic, small-scale fading is assumed estimable, and multiple band/slot orthogonality assumptions simplify interference.

## Relation to the corpus

This source adds [[laser-power-transfer]] to UAV communication and separates threshold satisfaction from sum-throughput maximization. It is adjacent to laser-powered aerial MEC, but no computation tasks or CPUs are modeled here.

## Raw artifacts

- Parse: `raw/sources/QoE_Maximization_for_Laser-Powered_Multi-UAV_Communication_Networks/QoE_Maximization_for_Laser-Powered_Multi-UAV_Communication_Networks.md`
- Origin PDF and extracted figures (`images/`) are in the same folder.
