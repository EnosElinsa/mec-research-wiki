---
type: source
title: "An Energy Efficient Framework for UAV-Assisted Millimeter Wave 5G Heterogeneous Cellular Networks"
authors: ["Jacob Chakareski", "Syed Naqvi", "Nicholas Mastronarde", "Jie Xu", "Fatemeh Afghah", "Abolfazl Razi"]
year: 2019
url: "https://doi.org/10.1109/TGCN.2019.2892141"
venue: "IEEE Transactions on Green Communications and Networking (IEEE TGCN), vol. 3, no. 1, pp. 37-44, Mar. 2019"
modeling_card: required
tags: [source, uav-base-station, mmwave, heterogeneous-network, energy-efficiency, radio-resource-management, drone-cell]
related:
  - "[[drone-cell-3d-placement]]"
  - "[[air-to-ground-channel-model]]"
  - "[[cellular-connected-uav]]"
  - "[[mozaffari-2015-drone-small-cells]]"
  - "[[mozaffari-2019-uav-wireless-tutorial]]"
created: 2026-07-11
updated: 2026-07-16
---

# An Energy Efficient Framework for UAV-Assisted Millimeter Wave 5G Heterogeneous Cellular Networks

## Citation

Chakareski, J., Naqvi, S., Mastronarde, N., Xu, J., Afghah, F., & Razi, A. (2019). *An Energy Efficient Framework for UAV-Assisted Millimeter Wave 5G Heterogeneous Cellular Networks*. **IEEE Transactions on Green Communications and Networking**, 3(1), 37-44. DOI: 10.1109/TGCN.2019.2892141. DOI/venue/year were verified against a title-matched Crossref/IEEE DOI record; technical claims are grounded in the local parse.

Author-disambiguation note: the "Jie Xu" in this paper is identified by the local parsed bio as an Electrical and Computer Engineering faculty member at the University of Miami, distinct from the CUHK-Shenzhen ISAC author entity [[jie-xu]].

## TL;DR

Analyzes a multi-band HetNet with one microwave macro BS, ground dual-mode mmWave small cells, and UAV small BSs. A two-layer optimization framework first derives UAV coverage radius/altitude from maximum allowed path loss, then maximizes system energy efficiency through radio resource allocation under QoS and transmit-power constraints.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A three-tier downlink HetNet contains one microwave macro BS, ground dual-mode millimeter-wave small cells using high and low bands, UAV small BSs sharing microwave subcarriers with the macro tier, and randomly distributed users. Users associate by biased received power or SINR, UAV air-to-ground links use probabilistic LoS and NLoS path loss, and each tier controls resources independently.

**Problem & objective**: The two-layer framework derives UAV height from $\mathrm{PL}_{\max}$ and, for $\phi=\phi_{EE}$, solves the weighted inner objective $\max_{\mathbf p}\;\phi\frac{\sum_{m,n}r_{m,n}^{(\mu W)}}{R_{\mathrm{norm}}}-(1-\phi)\frac{P}{P_{\mathrm{norm}}}$, corresponding to system energy efficiency $\frac{\sum_m\overline R_m}{\sum_m\overline P_m+\sum_kP_{C_k}}$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV altitude | $z_e$ | continuous, derived from $\mathrm{PL}_{\max}$ | Height and corresponding coverage radius of UAV BS $e$ |
| Downlink power allocation | $p_{m,n}^{(k)}$ | continuous, $p_{m,n}^{(k)}\geq0$ | Power assigned by tier $k$ to user $m$ on subcarrier $n$ |
| Subcarrier assignment | $\kappa_{m,n}$ | binary, $\{0,1\}$ | Whether macro subcarrier $n$ is assigned to user $m$ |
| Small-cell band association | $\Upsilon(w,z)$ | discrete, $\{1,2\}$ | Whether user $z$ of small cell $w$ uses the high or low millimeter-wave band |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| 5-6 | UAV coverage height is chosen so the farthest served user satisfies the maximum path-loss limit $\mathrm{PL}_{\max}$ |
| 7a | Macro-tier power is bounded, $\sum_{m,n}p_{m,n}^{(\mu W)}\leq P_{\mu W}^{\max}$ |
| 7b | Every served user meets minimum rate, $R_m\geq R_{\min}$ |
| 7c-7d | Power is nonnegative and subcarrier assignment is binary and exclusive within a BS |
| 12 | UAV power is high enough for $R_{\min}$ but capped by the macro-user QoS and cross-tier interference limit $I_t$ |

**Algorithm**: The outer layer computes coverage radius and $z_e$ from the maximum path loss. The inner layer uses Lagrange multipliers and subgradient updates for power allocation, the Hungarian method for macro subcarrier assignment, QoS and interference clipping for UAV-tier power, and band-specific rate or energy-efficiency allocation for dual-mode small cells.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Chakareski et al. [x] studied downlink radio resource management in a three-tier multi-band HetNet containing a microwave macro base station, dual-mode millimeter-wave small cells, and UAV small base stations. They used a two-layer formulation that derives UAV coverage radius and altitude from a maximum path-loss limit and maximizes system energy efficiency through power and subcarrier allocation under minimum-rate, maximum-power, exclusive-assignment, and cross-tier-interference constraints. Their solution applies Lagrange multipliers and subgradient updates for power allocation, the Hungarian method for subcarrier assignment, constrained UAV-tier power control, and band-specific allocation for the small cells. Simulations report that the UAV tier nearly doubles system energy efficiency at a target SINR of 0 dB, that energy efficiency peaks at 140 m in the tested setting, and that this peak is 35% higher than at 10 m.

## Problem

UAV base stations can extend 5G coverage and throughput, but their energy limits, interference behavior, altitude-dependent air-to-ground channel, and coexistence with terrestrial macro/mmWave small cells make placement and resource management coupled. The paper asks when adding a UAV tier improves energy efficiency rather than simply adding more power consumption.

## System model

The simulated HetNet has one microwave macro BS, three dual-mode mmWave SBSs, two UAV BSs, and users distributed in a 1 km by 1 km area. The macro and UAV tiers use 2 GHz carriers and 20 MHz bandwidth. SBSs use 28 GHz and 73 GHz bands with larger bandwidths. Users associate through biased received power or biased SINR, and the UAV air-to-ground channel uses a LoS-probability/path-loss model.

## Method

The outer layer derives the UAV coverage radius and height from a maximum path-loss threshold. The inner layer maximizes system energy efficiency, defined as aggregate user data rate divided by aggregate transmission plus circuit power. The paper compares the proposed EE-maximization resource allocation against power-minimization and rate-maximization baselines.

## Key findings

- Introducing the UAV tier can nearly double system energy efficiency at specific target SINR values; at tau = 0 dB, the reported EE-maximization curve with UAVs is almost twice the no-UAV case.
- The proposed EE-maximization approach outperforms power-minimization and rate-maximization baselines in system EE.
- In the reported setting, system EE peaks at UAV altitude 140 m, corresponding to maximum path loss 68.8 dB; the system EE at 140 m is 35% greater than at 10 m.
- System sum rate for the rate-maximization approach is about 13% greater with the UAV tier; for power minimization at tau = 20 dB, the sum rate is about 10% greater with UAVs.
- Increasing the UAV biasing factor can pull substantially more users into the UAV tier, but macro/mmWave biasing can reduce UAV-tier association.

## Limitations / future work

The paper presents a first study of this particular UAV-assisted multi-band HetNet and compares against border-case baselines rather than directly matched prior systems. Future work includes complexity analysis, lower-complexity suboptimal methods, practical implementation, joint power allocation and user association, horizon-based dynamic UAV placement, and economics of UAV-enabled rural coverage.

## Relation to the corpus

This is an early UAV-as-aerial-small-cell energy-efficiency source, adjacent to [[mozaffari-2015-drone-small-cells]] and the broader [[drone-cell-3d-placement]] / [[air-to-ground-channel-model]] foundation. Unlike later UAV-MEC papers, it does not optimize computation offloading; it supplies a communication-side energy-efficiency baseline for how UAV tiers interact with terrestrial macro/mmWave small cells.

## Raw artifacts

- `raw/sources/An_Energy_Efficient_Framework_for_UAV-Assisted_Millimeter_Wave_5G_Heterogeneous_Cellular_Networks/An_Energy_Efficient_Framework_for_UAV-Assisted_Millimeter_Wave_5G_Heterogeneous_Cellular_Networks.md`
- Original PDF and extracted figures (`images/`) in the same folder.
