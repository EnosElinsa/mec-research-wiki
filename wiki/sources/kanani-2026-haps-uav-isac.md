---
type: source
title: "Optimizing Network Performance and Resource Allocation in HAPS-UAV Integrated Sensing and Communication Systems for 6G"
authors: ["Parisa Kanani", "Mohammad Javad Omidi", "Mahmoud Modarres-Hashemi", "Halim Yanikomeroglu"]
year: 2026
url: "https://doi.org/10.1109/TWC.2025.3608619"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), vol. 25, pp. 4098-4112"
tags: [source, haps, uav, isac, resource-allocation, multi-objective-optimization, nsga-ii]
related:
  - "[[haps-uav-isac-resource-allocation]]"
  - "[[high-altitude-platform-station]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[genetic-algorithm]]"
  - "[[non-dominated-sorting-genetic-algorithm]]"
  - "[[halim-yanikomeroglu]]"
created: 2026-07-14
modeling_card: required
updated: 2026-07-16
---

# Optimizing Network Performance and Resource Allocation in HAPS-UAV Integrated Sensing and Communication Systems for 6G

## Citation

Kanani, P., Omidi, M. J., Modarres-Hashemi, M., & Yanikomeroglu, H. (2026). *Optimizing Network Performance and Resource Allocation in HAPS-UAV Integrated Sensing and Communication Systems for 6G*. **IEEE Transactions on Wireless Communications, 25**, 4098-4112. DOI: 10.1109/TWC.2025.3608619.

## TL;DR

Uses a HAPS as a centralized processor for multi-UAV ISAC and applies GA or NSGA-II to trade target-echo power against worst-user communication SINR through UAV positions, beamforming, and power allocation.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Multiple MIMO UAV access points serve ground communication users and sense designated targets in a two-slot ISAC cycle, then relay target echoes over a directional D-band LoS link to a UPA-equipped HAPS processor; UAV-to-ground communication uses a sub-6-GHz LoS channel.

**Problem & objective**: The bi-objective problem maximizes $(\Omega,\eta)$, where $\Omega$ is HAPS-received target-echo power and $\eta\leq\min_k\mathrm{SINR}_k$; its scalarized form maximizes $\mu\Omega+(1-\mu)\eta$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Communication beamformer | $\mathbf w_k^m[n]$ | Complex continuous vector | Directs UAV $m$'s signal to user $k$ |
| Sensing beamformer | $\mathbf r_j^m[n]$ | Complex continuous vector | Directs UAV $m$'s probing signal to target $j$ |
| UAV horizontal position | $\mathbf q^m[n]$ | Continuous, region bounded | Sets user, target, and HAPS geometry |
| Worst-user SINR variable | $\eta$ | Continuous, nonnegative | Lower-bounds every user's SINR |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Sensing power respects its assigned share of the UAV budget |
| C2 | Combined communication and sensing power is at most $P_{\max}^m$ |
| C3 | UAV displacement is bounded by $V_{\max}^m\Delta t$ and positions remain in the flight region |
| C4 | Target beam-pattern gain remains above $\Gamma_j^{\mathrm{th}}$ after path-loss scaling |
| C5 | Every user satisfies $\eta\leq\mathrm{SINR}_k$ and $\mathrm{SINR}_k\geq\mathrm{SINR}_{\mathrm{th}}$ |

**Algorithm**: A canonical genetic algorithm encodes positions and beamformers to solve the weighted scalarization with constraint penalties; NSGA-II applies non-dominated sorting and crowding distance to the original bi-objective formulation and returns a diverse Pareto set for operating-point selection.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Kanani et al. [x] studied a two-slot HAPS-UAV ISAC architecture in which MIMO UAVs serve communication users and sense ground targets before relaying echoes to a HAPS processor. They jointly optimized communication beamformers, sensing beamformers, UAV positions, and power allocation to maximize HAPS-received echo power and the minimum user SINR under transmit-power, mobility, flight-region, beam-pattern, and SINR constraints. A canonical genetic algorithm solves a weighted scalarization, while NSGA-II directly generates a Pareto set for the two objectives. Simulations show the expected trade-off between sensing power and minimum SINR and report that NSGA-II produces a richer Pareto front than the weighted approach. In the reported power sweep, NSGA-II achieved higher minimum SINR than PPO and the standard genetic algorithm, and the HAPS-UAV model improved worst-user rate relative to the adapted UAV-only reference.

## Problem and system model

Multiple MIMO UAVs act as dual-purpose access points. In the first slot they transmit combined communication and sensing signals to ground communication users and targets, then receive target echoes. In the second slot they relay information toward a HAPS, which serves as an aerial CPU and coordinates beamforming and processing.

The bi-objective problem maximizes HAPS-received echo power and the minimum user SINR subject to per-UAV power, beam-pattern gain, and communication constraints. The minimum-SINR objective supplies a max-min user criterion; the paper's broader fairness language is not a separate fairness-index formulation.

## Method

The [[haps-uav-isac-resource-allocation]] design exposes both a weighted-sum scalarization and the original Pareto problem. A canonical [[genetic-algorithm]] solves the scalarized form, while [[non-dominated-sorting-genetic-algorithm|NSGA-II]] evolves a diverse Pareto set without collapsing the two objectives into one reward. A PPO comparator instead uses a scalar reward based on echo power, minimum SINR, and constraint penalties.

## Key findings

- The simulations show the expected sensing/communication trade-off as the Pareto weight changes; no single point maximizes both objectives.
- Adding the HAPS processor improves the plotted SINR/resource-allocation results over the paper's UAV-only comparison.
- Minimum user SINR rises with transmit power for GA, PPO, and NSGA-II; in the displayed comparison NSGA-II is strongest, PPO is second, and GA is third.
- The comparison is algorithmic and simulation-based; the paper does not prove that an evolved solution is globally Pareto optimal.

## Limitations

The model assumes LoS propagation, perfect CSI, and accurate separation of target echoes. The 120 GHz HAPS-UAV backhaul is especially sensitive to blockage and estimation error. Results are simulation-only, and evolutionary search can be computationally expensive; no flight or radio prototype validates the centralized two-slot architecture.

## Relation to the corpus

This source makes [[high-altitude-platform-station|HAPS]] an ISAC processing tier rather than only a relay or MEC destination. It connects [[integrated-sensing-and-communication]] to explicit Pareto search and complements single-objective aerial ISAC controllers that hide the sensing/communication trade-off inside a scalar reward.

## Raw artifacts

- Parse: `raw/sources/Optimizing_Network_Performance_and_Resource_Allocation_in_HAPS-UAV_Integrated_Sensing_and_Communication_Systems_for_6G/Optimizing_Network_Performance_and_Resource_Allocation_in_HAPS-UAV_Integrated_Sensing_and_Communication_Systems_for_6G.md`
- Origin PDF and extracted figures (`images/`) are in the same folder.
