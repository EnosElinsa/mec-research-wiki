---
type: source
title: "Energy-Efficient Resource Allocation for Mobile-Edge Computation Offloading"
authors: ["Changsheng You", "Kaibin Huang", "Hyukjin Chae", "Byoung-Hoon Kim"]
year: 2017
url: "https://doi.org/10.1109/TWC.2016.2633522"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, mobile-edge-computing, computation-offloading, binary-vs-partial-offloading, convex-optimization, mixed-integer-nonlinear-programming, resource-allocation]
related:
  - "[[mobile-edge-computing]]"
  - "[[task-offloading]]"
  - "[[binary-vs-partial-offloading]]"
  - "[[energy-latency-tradeoff]]"
  - "[[mixed-integer-nonlinear-programming]]"
  - "[[mao-2016-lodco-eh-mec-offloading]]"
  - "[[mao-2017-mec-survey-communication]]"
  - "[[zhang-2013-energy-optimal-mcc-stochastic]]"
  - "[[miettinen-2010-mcc-energy-efficiency]]"
created: 2026-06-02
updated: 2026-07-16
modeling_card: required
---

# Energy-Efficient Resource Allocation for Mobile-Edge Computation Offloading

## Citation

You, C., Huang, K., Chae, H., & Kim, B.-H. (2017). *Energy-Efficient Resource Allocation for Mobile-Edge Computation Offloading*. **IEEE Transactions on Wireless Communications**, 16(3), 1397–1411. DOI: 10.1109/TWC.2016.2633522. (Manuscript received 5 June 2016; revised 24 September and 13 November 2016; accepted 20 November 2016; date of publication 1 December 2016; date of current version 8 March 2017 → year 2017. Presented in part at IEEE Globecom 2016.)

## TL;DR

A foundational **resource-allocation** treatment of **multiuser mobile-edge computation offloading (MECO)** that derives the *structure* of the optimal policy rather than just an algorithm. For a **TDMA** MECO system, minimizing **weighted-sum mobile energy** under a shared latency constraint is a convex problem whose optimal policy is **threshold-based** with respect to a derived **offloading priority function** (a function of each user's channel gain and local-computing energy): users above the threshold do **complete** offloading, users below do **minimum** offloading. The result is extended to a **finite-capacity** cloud (modified priority function + a low-complexity threshold search) and to an **OFDMA** system (a mixed-integer problem solved sub-optimally by transforming it to its TDMA counterpart via average sub-channel gains).

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Multiple mobile devices split computation between local CPUs and one edge cloud through a base station. The base station centrally allocates TDMA time or OFDMA subchannels under a common latency deadline and possibly finite cloud capacity.

**Problem & objective**: TDMA Problem P1 minimizes weighted mobile energy, $\min_{\{\ell_k,t_k\}}\sum_k\beta_k[\frac{t_k}{h_k^2}f(\ell_k/t_k)+(R_k-\ell_k)C_kP_k]$, with analogous OFDMA allocation in Problem P4.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Offloaded data | $\ell_k$ | continuous, $[m_k^+,R_k]$ | Input bits offloaded by mobile $k$ |
| TDMA offloading time | $t_k$ | continuous, nonnegative | Uplink duration assigned to mobile $k$ |
| OFDMA offloaded data | $\ell_{k,n}$ | continuous, nonnegative | Bits mobile $k$ sends on subchannel $n$ |
| Subchannel assignment | $\rho_{k,n}$ | binary | Assigns subchannel $n$ to mobile $k$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| TDMA time | Shared uplink time satisfies $\sum_kt_k\leq T$ |
| Cloud capacity | Offloaded computation satisfies $\sum_kC_k\ell_k\leq F$ when capacity is finite |
| Offload bounds | Latency-required minimum and task size give $m_k^+\leq\ell_k\leq R_k$ |
| OFDMA exclusivity | Each subchannel is assigned to at most one user, $\sum_k\rho_{k,n}\leq1$ |
| OFDMA domain | Subchannel indicators are binary and each user's total offload stays within its bounds |

**Algorithm**: KKT analysis yields an offloading-priority function and a threshold policy that gives users complete or minimum offloading in TDMA. Finite-cloud algorithms search the associated multipliers, while the OFDMA heuristic reserves channels for mandatory offloaders, solves an average-gain TDMA counterpart, assigns integer subchannels by priority, and adjusts per-channel offloaded data.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

You et al. [x] derived structure-revealing resource-allocation policies for multiuser mobile-edge computation offloading. Their TDMA formulation minimizes weighted mobile energy over offloaded data and transmission time under latency and cloud-capacity constraints. KKT analysis produces an offloading-priority function and a threshold that separates complete offloading from the minimum amount required by latency. The finite-cloud method modifies the priority and reduces multiplier search, while the OFDMA method assigns integer subchannels through average channel gains and priority ordering. In the reported TDMA experiments, the suboptimal finite-capacity policy remained close to optimal and consumed less than half the energy of equal allocation in the highlighted time-slot sweep. With 256 OFDMA subchannels, the proposed method used 0.0005 J versus 0.0004 J for relaxation and rounding, while its average runtime was 0.6338 seconds versus 247.4548 seconds.

## Problem framing

The IoT will connect billions of battery- and compute-limited devices; offloading intensive computation to nearby edge clouds (MECO) prolongs battery life and boosts capacity, but only if the **joint design of offloading and wireless communication** is energy-efficient. Prior MECO work emphasized complex algorithmic designs that gave little insight into the **structure** of the optimal policy. This paper instead seeks closed-form policy structure (priority + threshold) for the multiuser case and uses it to design a low-complexity OFDMA scheme.

## System model

- **Setup.** K single-antenna mobiles served by one BS that gateways a single edge cloud; mobiles compute different loads under a **common latency constraint** T. The BS has perfect knowledge of channel gains, per-bit local-computing energy, input-data sizes, and fairness factors, and does **centralized** resource allocation.
- **Partial offloading.** Computation data can be split, so each mobile can simultaneously **compute locally and offload** part of its data.
- **Multiple access.** **TDMA** (time split into per-user offloading slots) and **OFDMA** (sub-channel assignment) are both considered; the time slot T is sized to meet the latency requirement.
- **Objective.** Minimize the **weighted-sum mobile energy consumption** (weights are per-user fairness factors) subject to the latency constraint and, in the finite-capacity case, a per-slot cloud computation cap.

## Method

- **TDMA, infinite-capacity cloud.** Convex formulation; an **offloading priority function** is derived and the optimal policy is proved to be **threshold-based** (complete vs minimum offloading split by the threshold).
- **TDMA, finite-capacity cloud.** An **effective** offloading priority function and a modified threshold policy; a low-complexity algorithm reduces a 2-D Lagrange-multiplier search to a 1-D search based on the approximated priority order, shown near-optimal by simulation.
- **OFDMA.** A **mixed-integer** resource-allocation problem; a low-complexity sub-optimal algorithm transforms it to the TDMA counterpart using **average sub-channel gains**, defines an average offloading priority function, assigns integer sub-channels by priority order, then adjusts offloaded-data allocation; shown close-to-optimal by simulation.

## Key findings

- The optimal TDMA MECO policy has a clean **threshold-on-priority** structure — users are ranked by a priority that increases with channel gain and local-computing energy, and the threshold cleanly separates complete from minimum offloading. This structural insight, not just a number, is the contribution.
- The finite-capacity TDMA and OFDMA algorithms achieve **close-to-optimal** performance in simulation (evaluated over 200 channel realizations with 30 users). Specific gaps are figure-derived; treat exact values as indicative.

## Limitations / future work

The framework assumes a common per-user latency constraint and perfect knowledge at the BS; the authors note extension to **heterogeneous latency constraints and finite cloud resource** via dynamic cloud control (demand scheduling / load shifting), and to **predictive computing** for arriving data. Analysis/simulation only.

## Relation to the corpus

An early, widely-cited **MEC fundamentals** anchor that complements the energy-harvesting online policy of [[mao-2016-lodco-eh-mec-offloading]] and the stochastic-channel MCC scheduling of [[zhang-2013-energy-optimal-mcc-stochastic]] with a **static, structure-revealing** multiuser resource-allocation result (priority + threshold). It is methodologically cited by the MEC communication survey [[mao-2017-mec-survey-communication]] (which shares authors You and Huang), and it formalizes the local-vs-offload energy trade-off that the measurement study [[miettinen-2010-mcc-energy-efficiency]] frames empirically. Its **partial (data-split) offloading** model grounds [[binary-vs-partial-offloading]].

## Raw artifacts

- `raw/sources/Energy-Efficient_Resource_Allocation_for_Mobile-Edge_Computation_Offloading/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
