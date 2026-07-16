---
type: source
modeling_card: required
title: "Terahertz Communication Multi-UAV-Assisted Mobile Edge Computing System"
authors: ["Heekang Song", "Hyowoon Seo", "Wan Choi"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3708383"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), pp. 1-15"
tags: [source, terahertz-communication, multi-uav-assisted-mec, uav-mobile-relaying, penalty-dual-decomposition, queueing-theory, task-offloading]
related:
  - "[[terahertz-communication]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[uav-mobile-relaying]]"
  - "[[penalty-dual-decomposition]]"
  - "[[queueing-theory]]"
  - "[[task-offloading]]"
  - "[[mobile-edge-computing]]"
  - "[[tun-2025-thz-sag-mec-resource-allocation]]"
  - "[[wu-2025-iopo-irs-uav-thz-mec]]"
created: 2026-07-07
updated: 2026-07-16
---

# Terahertz Communication Multi-UAV-Assisted Mobile Edge Computing System

## Citation

Song, H., Seo, H., & Choi, W. (2026). *Terahertz Communication Multi-UAV-Assisted Mobile Edge Computing System*. **IEEE Transactions on Mobile Computing**, 1-15. DOI: 10.1109/TMC.2026.3708383. The top-level local parse is silent on DOI; DOI/venue/year were verified against a title-matched Crossref/IEEE DOI record.

## TL;DR

Optimizes a THz multi-UAV relay MEC system where IoT devices either offload directly to MEC servers or through UAV relays. The objective is long-term average service-delay minimization, including THz communication delay and M/M/s MEC queueing delay, through relay selection, UAV power control, UAV deployment, and user-resource association.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: IoT devices with Poisson task arrivals either connect directly to MEC servers or use multiple UAV relays over wideband THz links. Molecular absorption and blockage determine communication delay, while each MEC server is modeled as an M/M/s queue and UAV relay selection, power, position, and user-subband association are coupled.

**Problem & objective**: Problem P1, a mixed-integer nonlinear queue-aware program, minimizes long-term average service delay, $\min\limsup_T T^{-1}\sum_t D_{\mathrm{service}}(t)$, subject to queue stability and communication, association, power, and UAV-position limits.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Relay selection | $x_{i,u}(t)$ | binary | Whether IoT device $i$ uses UAV relay $u$ |
| UAV transmit power | $p_u(t)$ | continuous, bounded | Relay transmit power |
| UAV position | $\mathbf q_u(t)$ | continuous 2-D/3-D position | Deployment location of relay $u$ |
| User-subband association | $a_{i,s}(t)$ | binary | THz sub-band/resource assigned to device $i$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Each device uses a direct or one-relay path and each sub-band serves feasible users |
| C2 | Relay and device powers satisfy peak limits |
| C3 | THz communication queues and M/M/s MEC queues remain stable |
| C4 | UAV positions and relay links satisfy deployment and blockage assumptions |
| C5 | Service rates, molecular absorption, and queueing delays meet the long-term delay domain |

**Algorithm**: Introduce slack equalities and an augmented Lagrangian for binary variables → alternate relay selection, power control, UAV positioning, and user-resource association in a PDD inner loop → update dual variables and penalties in the outer loop → optionally use theorem-based closed forms, clustering, and greedy association for a lower-complexity variant.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Song et al. [x] studied long-term service-delay minimization in a terahertz multi-UAV relay MEC system. IoT devices use direct or relayed THz paths to MEC servers, while molecular absorption, blockage, and M/M/s queueing determine communication and execution delay. They formulated a mixed-integer nonlinear problem that jointly optimizes relay selection, UAV transmit power and positions, and user-subband association under queue-stability and resource constraints. A penalty dual decomposition method alternates the four variable blocks and updates augmented-Lagrangian multipliers, with closed-form relay and power structures at convergence. In the stated 400 m by 400 m simulation, PDD reaches 2.3687 s average service delay versus 2.1319 s for exhaustive search and 2.3894 s for the upper-bound reference.

## Problem

MEC systems face spectrum scarcity and blockage-prone links. THz communication offers very wide bandwidth but suffers molecular absorption and blockage. Prior UAV-aided MEC work often focuses on a single UAV, UAV-side computation, or short-term delay. This paper instead uses multiple UAVs as communication relays for long-term user service-delay minimization.

## System model

The system contains multiple UAV relays, IoT devices, and MEC servers. IoT devices generate Poisson task arrivals and do not compute locally. A task can use a direct IoT-MEC path or a relayed IoT-UAV-MEC path. THz transmission uses ultra-wideband transmission windows split into sub-bands, with molecular absorption based on HITRAN-style modeling. Direct IoT-MEC links have a non-blockage probability, while UAV relays are assumed to avoid blockers. MEC computation is modeled with an M/M/s queue and Erlang-C queueing delay, and queue stability is enforced.

## Method

The original MINLP jointly optimizes relay selection, UAV transmit power, UAV positions, and user-resource/sub-band association. The paper proposes a PDD double-loop algorithm:

- binary variables are transformed through slack equality constraints and an augmented Lagrangian;
- the inner loop alternates relay selection, power control, UAV positioning, and user-resource association subproblems;
- the outer loop updates dual variables and penalty parameters.

Theorems provide closed-form relay-selection and power-control structures at convergence, including a Lambert-W expression for power. A lower-complexity alternating optimization variant combines theorem-based updates, clustering, and greedy association.

## Key findings

- In a 400 m by 400 m simulation with 20 IoT devices, four MEC servers, three UAVs, 0.34 THz carrier frequency, and 1 GHz sub-bands, PDD converges to average service delay 2.3687 s versus exhaustive-search 2.1319 s and upper-bound 2.3894 s in the parse.
- The proposed method outperforms the listed baselines UO, UAO, NR-SCA, UO-GUAO, BCD-SCA, DE, MG, and DRL.
- Joint communication and computation optimization is important: communication-only optimization can reduce link delay while still overloading MEC queues.
- The proposed association balances server utilization and keeps queues stable in the reported figures.
- Higher traffic load increases delay through queueing, higher carrier frequency can degrade performance because of molecular absorption, and more sub-bands reduce delay with execution-time saturation.
- More UAVs help, especially in larger networks, while higher IoT transmit power reduces relay dependence.

## Limitations / future work

The conclusion in the parse does not list future work. The method is suboptimal rather than globally optimal, PDD complexity grows with sub-band and network scale, and the lower-complexity variant trades solution quality for execution time. The model also assumes stationary or limited-mobility IoT conditions in the reported setup.

## Relation to the corpus

This source is a THz relay-side counterpart to [[tun-2025-thz-sag-mec-resource-allocation]] and [[wu-2025-iopo-irs-uav-thz-mec]]. It reinforces [[terahertz-communication]], [[multi-uav-assisted-mec]], [[uav-mobile-relaying]], [[penalty-dual-decomposition]], and [[queueing-theory]] by putting THz blockage/absorption and MEC queue stability into one optimization problem.

## Raw artifacts

- `raw/sources/Terahertz Communication Multi-UAV-Assisted Mobile Edge Computing System/Terahertz Communication Multi-UAV-Assisted Mobile Edge Computing System.md`
- Original PDF and extracted figures (`images/`) in the same folder.
