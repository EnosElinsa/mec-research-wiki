---
type: source
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
updated: 2026-07-07
---

# Terahertz Communication Multi-UAV-Assisted Mobile Edge Computing System

## Citation

Song, H., Seo, H., & Choi, W. (2026). *Terahertz Communication Multi-UAV-Assisted Mobile Edge Computing System*. **IEEE Transactions on Mobile Computing**, 1-15. DOI: 10.1109/TMC.2026.3708383. The top-level local parse is silent on DOI; DOI/venue/year were verified against a title-matched Crossref/IEEE DOI record.

## TL;DR

Optimizes a THz multi-UAV relay MEC system where IoT devices either offload directly to MEC servers or through UAV relays. The objective is long-term average service-delay minimization, including THz communication delay and M/M/s MEC queueing delay, through relay selection, UAV power control, UAV deployment, and user-resource association.

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
