---
type: source
title: "Joint Optimization of Delay and Power Efficiency of Neighbor Discovery in UAV Networks"
authors: ["Hao Fan", "Zhe Song", "Xuanhe Yang", "Tingting Li", "Shuai Wang", "Chee Yen Leow", "Gaofeng Pan", "Dusit Niyato"]
year: 2026
url: "https://doi.org/10.1109/TMC.2025.3649859"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
modeling_card: required
tags: [source, fanet, neighbor-discovery, directional-antenna, power-delay-product, geometric-programming, convex-concave-procedure]
related:
  - "[[directional-neighbor-discovery]]"
  - "[[power-delay-product]]"
  - "[[directional-fanet-link-maintenance]]"
  - "[[heterogeneous-uav-fleet]]"
  - "[[energy-latency-tradeoff]]"
  - "[[song-2026-albpd-directional-fanet]]"
  - "[[zhe-song]]"
  - "[[xuanhe-yang]]"
  - "[[shuai-wang]]"
  - "[[chee-yen-leow]]"
  - "[[gaofeng-pan]]"
  - "[[dusit-niyato]]"
created: 2026-07-13
updated: 2026-07-16
---

# Joint Optimization of Delay and Power Efficiency of Neighbor Discovery in UAV Networks

## Citation

Fan, H., Song, Z., Yang, X., Li, T., Wang, S., Leow, C. Y., Pan, G., & Niyato, D. (2026). *Joint Optimization of Delay and Power Efficiency of Neighbor Discovery in UAV Networks*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2025.3649859.

> **Metadata grounding note.** DOI, venue, and year are absent from the parse and were verified through its exact-title Crossref record. Technical claims below remain parse-grounded.

## TL;DR

Optimizes directional sector selection and transmit/listen behavior for synchronous and asynchronous UAV neighbor discovery using the power-delay product. Markov-chain power models, order-statistic delay bounds, geometric programming, and a convex-concave procedure yield tractable surrogates; a four-node chamber experiment reports an 11% PDP reduction over an uninformed baseline.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Heterogeneous UAVs know their potential neighbors but not necessarily their active directions. Each half-duplex node activates one directional sector at a time, and discovery uses either synchronous slotted scanning or asynchronous Poisson-like request transmissions under a collision model without capture.

**Problem & objective**: Minimize average or worst-node power-delay product by choosing sector-selection and transmit/listen behavior. A reusable synchronous surrogate is $\min_{\mathcal R,\mathcal S} N^{-1}\sum_i H_{N_i}\bar P_i/\min_{j\in\mathcal N_i}p_{ij}$, with the asynchronous model replacing pairwise discovery probability by its successful-arrival rate.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Sector-selection probability | $s_{i,\theta}$ | continuous, $[0,1]$ | Probability that node $i$ activates sector $\theta$ |
| Synchronous listen probability | $r_{i,\theta}$ | continuous, $[0,1]$ | Conditional probability of listening in the selected sector |
| Synchronous transmit probability | $\bar r_{i,\theta}$ | continuous, $[0,1]$ | Conditional probability of transmitting a discovery request |
| Asynchronous request rate | $\lambda_i$ | continuous, $(0,1]$ | Normalized Poisson request rate for node $i$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Each node selects one sector distribution: $\sum_\theta s_{i,\theta}=1$. |
| C2 | Synchronous actions are complementary: $r_{i,\theta}+\bar r_{i,\theta}=1$; the GP uses the tight relaxation $\leq 1$. |
| C3 | All sector and action probabilities lie in $[0,1]$, and asynchronous rates satisfy $0<\lambda_i\leq1$. |
| C4 | Pairwise success requires directional alignment, one transmitter and one listener, and no collision from other active neighbors. |
| C5 | Every known potential-neighbor link must have positive discovery probability or successful-arrival rate. |
| C6 | Average and worst-node delay use harmonic-number bounds controlled by each node's weakest neighbor link. |

**Algorithm**: Derive average radio power from discrete- or continuous-time Markov chains and bound completion delay with order statistics and harmonic numbers. Substitute the worst-link bounds into the PDP objective, solve the synchronous design as a geometric program, and solve the asynchronous log-domain difference-of-convex formulation with a convex-concave procedure initialized by the delay-oriented solution.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Fan et al. [x] optimized directional neighbor discovery for heterogeneous UAV networks under synchronous slotted scanning and asynchronous random access. They minimized average or worst-node power-delay product over sector-selection probabilities, transmit/listen behavior, and asynchronous request rates under probability-normalization, half-duplex, alignment, and collision constraints. Markov-chain power models and order-statistic delay bounds yield a geometric program for synchronous scanning and a log-domain convex-concave procedure for asynchronous scanning. A four-node anechoic-chamber experiment reported maxPDP of 101.31 versus 113.81 for the uninformed baseline, an 11% reduction.

## System model

- A distributed heterogeneous UAV network uses unique IDs, half-duplex radios, one active directional sector per node, LoS-only links, and a collision model with no capture.
- Synchronous discovery is slotted-ALOHA-like; asynchronous discovery uses exponential waiting intervals and a Poisson transmission approximation.
- Decisions are sector-selection probabilities plus transmit/listen probabilities or normalized asynchronous transmission rates.
- Radio power includes transmit, receive, and listen states. Completion delay is the maximum pairwise time required to discover all known potential neighbors.
- Known link-persistence probabilities and sector distributions extend the model to link breakage and uncertain neighbor direction.

## Method

Discrete- and continuous-time Markov chains derive average radio power. Geometric and exponential pairwise delays feed order-statistic expressions for completion time, but exact expectations require exponentially many neighbor subsets. Harmonic-number bounds replace them with worst-link discovery-probability or arrival-rate surrogates.

The synchronous surrogate becomes a geometric program. The asynchronous log-domain problem is difference-of-convex and is solved by an initialization-sensitive convex-concave procedure. Neither provides an approximation ratio to the exact PDP objective, and CCP does not guarantee a global optimum. Probability equalities are relaxed to inequalities without a proof in the parse that every optimum makes them tight.

The paper's network-maximum metric is `max_i E[C_i]`, which is no greater than `E[max_i C_i]`; it is not the expected realized worst-node PDP.

## Key findings

- Simulations use 36 nodes, 1.5 km range, 2,048 independent topologies per configuration, and eight seeds, with 2-15 average neighbors and 4-16 sectors.
- Analytical and simulated delay, average power, and PDP agree closely; asynchronous error grows with density as finite packet duration departs from the ideal Poisson model.
- PDP-optimized policies generally outperform delay-only and uninformed policies; the figures provide trends rather than exact percentages.
- In a four-node static anechoic-chamber experiment, Table II reports `maxPDP` at **101.31** versus **113.81** for `noinfo`, a **10.98%** reduction consistent with the abstract's 11% claim. PDP units are not in the parse.

## Limitations / interpretation

The framework assumes the potential-neighbor topology, link persistence, and mobility-direction distributions are already known. Delay independence and the asynchronous Poisson process are approximations. Radio-state power excludes propulsion, mission energy, and mode-switch overhead.

The hardware test emulates UAV nodes in a static chamber rather than an outdoor or airborne network, and the mobility/link-breakage extensions are not separately validated. Several equations and the GP/CCP pseudocode are OCR-damaged. Fig. 11's caption says synchronous while its surrounding text says asynchronous; Table II defines absolute deviation but prints a signed `-11.2%`, and the prose further corrupts that value to about `-1.2%`.

## Relation to the corpus

[[directional-neighbor-discovery]] precedes routing and [[directional-fanet-link-maintenance]]: nodes must first discover directional peers before predicting when those links will break. The multiplicative [[power-delay-product]] differs from the weighted-sum [[energy-latency-tradeoff]] used in many MEC optimizers.

## Raw artifacts

- Parse: `raw/sources/Joint_Optimization_of_Delay_and_Power_Efficiency_of_Neighbor_Discovery_in_UAV_Networks/Joint_Optimization_of_Delay_and_Power_Efficiency_of_Neighbor_Discovery_in_UAV_Networks.md`
- Origin PDF and extracted figures (`images/`) in the same folder.
