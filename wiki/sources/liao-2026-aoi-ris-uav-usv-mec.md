---
type: source
title: "Joint UAVs Deployment and Resource Allocation for AoI-Aware RIS-Assisted UAV-USV MEC Network"
authors: ["Yangzhe Liao", "Yuanyan Song", "Dan Song"]
year: 2026
url: "https://doi.org/10.1109/TMC.2025.3611808"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), vol. 25, no. 3, Mar. 2026"
modeling_card: required
tags: [source, maritime-mec, uav-usv-cooperative-mec, age-of-information, intelligent-reflecting-surface, lyapunov-optimization, whale-optimization-algorithm]
related:
  - "[[maritime-mec]]"
  - "[[uav-usv-cooperative-mec]]"
  - "[[age-of-information]]"
  - "[[aoi-energy-tradeoff]]"
  - "[[uav-mounted-ris]]"
  - "[[intelligent-reflecting-surface]]"
  - "[[lyapunov-optimization]]"
  - "[[whale-optimization-algorithm]]"
  - "[[liao-2025-ris-uav-usv-resource-allocation]]"
created: 2026-07-07
updated: 2026-07-16
---

# Joint UAVs Deployment and Resource Allocation for AoI-Aware RIS-Assisted UAV-USV MEC Network

## Citation

Liao, Y., Song, Y., & Song, D. (2026). *Joint UAVs Deployment and Resource Allocation for AoI-Aware RIS-Assisted UAV-USV MEC Network*. **IEEE Transactions on Mobile Computing**, 25(3), 3103-3118. DOI: 10.1109/TMC.2025.3611808.

## TL;DR

Builds an AoI-aware RIS-assisted UAV-USV MEC architecture for inland waterways. A tethered UAV carries the RIS, while rotary-wing UAVs serve USVs that generate bidirectional data-computation tasks. The optimization minimizes a weighted sum of USV average AoI and RUAV flight energy by jointly choosing RUAV service durations, TUAV/RIS altitude, RIS phase shifts, and RUAV trajectories under a mixed linear-quadratic Lyapunov framework.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Inland-waterway USVs generate divisible bidirectional tasks whose local data and Internet-originating data must both reach rotary-wing UAV MEC servers. A tethered UAV carries a RIS between the terrestrial base station and the rotary-wing swarm, while the untethered UAVs move horizontally and share each slot among USVs.

**Problem & objective**: The long-term controller minimizes $\limsup_{T\to\infty}\frac{1}{T}\sum_{t=1}^{T}\mathbb E\left[X_w\sum_i\Delta_i(t)+\sum_mp_m(t)\right]$, a weighted sum of USV average AoI and rotary-wing UAV flight power.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| USV service duration | $\alpha_i(t)$ | continuous, nonnegative | Portion of slot $t$ allocated to USV $i$ |
| RIS phase shift | $\theta_k(t)$ | continuous, $[0,2\pi]$ | Phase of RIS element $k$ |
| Tethered-UAV altitude | $H_{\mathrm{TUAV}}(t)$ | continuous altitude | Time-varying height of the RIS platform |
| Rotary-wing trajectories | $\mathbf q_m(t)$ | continuous horizontal positions | Slotwise paths of MEC UAVs |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Service durations satisfy $\alpha_i(t)\geq0$ and $\sum_i\alpha_i(t)\leq\delta$ |
| C2 | Every RIS phase lies in $[0,2\pi]$ |
| C3 | Each USV's AoI remains below its prescribed threshold $\Delta_i^{\max}$ |
| C4 | Tethered-UAV altitude and climb or descent rate remain within their bounds |
| C5 | Rotary-wing UAV speed and steering angle remain below their maxima |
| C6 | Each USV satisfies its long-term average transmission-power limit |

**Algorithm**: An auxiliary queue and mixed linear-quadratic Lyapunov transformation replace the long-term power constraint with per-slot deterministic problems. Each slot then alternates an enhanced whale optimizer for rotary-wing UAV trajectories with an enhanced alternating optimizer for service durations, RIS phases, and tethered-UAV altitude.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Liao et al. [x] jointly deployed a RIS-carrying tethered UAV and rotary-wing MEC UAVs for age-sensitive bidirectional USV tasks. Their long-term objective balances average AoI against flight energy over service durations, RIS phases, tethered-UAV altitude, and rotary-wing trajectories under freshness, mobility, phase, and average-power constraints. A mixed linear-quadratic Lyapunov transformation produces deterministic slot problems solved by enhanced whale optimization and alternating resource updates. The proposed design reported about $3.3\times10^5$ J of flight energy at 9.6 s average AoI and approximately 50% long-term flight-energy reduction while maintaining satisfactory freshness.

## Problem

USV data in inland waterways is freshness-sensitive: stale sensing or task-result information weakens monitoring and control even if raw latency looks acceptable. At the same time, rotary-wing UAVs have limited flight energy, and ship/shore blockage makes direct links unreliable. The paper therefore couples AoI, UAV propulsion energy, RIS-aided link quality, and task service scheduling in one long-term stochastic control problem.

## System model

- The network includes USVs, rotary-wing UAVs, and one RIS-carried tethered UAV.
- USVs require bidirectional data computation, and their average AoI is constrained.
- RUAV service-duration indicators decide which USVs are served in each slot.
- TUAV hovering altitude and RIS phase shifts shape the assisted wireless channel.
- RUAV trajectories determine flight energy and link geometry.

## Method

The paper first turns the long-term stochastic problem into deterministic single-slot subproblems with a mixed linear quadratic Lyapunov framework. The single-slot problem is then split into:

- RUAV trajectory optimization via an enhanced whale optimization algorithm.
- Service duration, RIS phase shift, and TUAV hovering-altitude optimization via an enhanced alternating optimization algorithm.

## Key findings

- The abstract reports about 50% long-term RUAV flight-energy reduction while maintaining satisfactory USV average AoI.
- In the reported comparison, the proposed design gives about 3.3e5 J RUAV flight energy and 9.6 s average AoI, compared with 3.8e5 J / 10.5 s for DE, 4.3e5 J / 11.8 s for GD, and 6.6e5 J / 19.6 s for random placement.
- With 1, 3, and 5 RUAVs, the proposed energy values are reported as about 7.8e4 J, 3.2e5 J, and 4.8e5 J.
- Increasing RIS elements improves freshness in the reported setup: the parse reports average AoI near 7.4 s with 30 elements and near 4.2 s with 50 elements.

## Limitations / future work

The paper identifies digital-twin-supported physical/virtual task dynamics, deep-learning or multi-agent-DRL online UAV/RIS design, and RIS-assisted ship-to-shore protocol/performance analysis as future work. The evaluation is simulation-based.

## Relation to the corpus

This page is the freshness-oriented companion to [[liao-2025-ris-uav-usv-resource-allocation]]. Both use RIS-assisted UAV-USV MEC for inland waterways, but this source makes [[age-of-information]] and RUAV flight energy the central tradeoff. It adds [[lyapunov-optimization]] and [[whale-optimization-algorithm]] to the maritime RIS branch, and links [[uav-mounted-ris]] with [[uav-usv-cooperative-mec]].

## Raw artifacts

- `raw/sources/Joint UAVs Deployment and Resource Allocation for AoI-Aware RIS-Assisted UAV-USV MEC Network/Joint UAVs Deployment and Resource Allocation for AoI-Aware RIS-Assisted UAV-USV MEC Network.md`
- Original PDF and extracted figures (`images/`) in the same folder.
