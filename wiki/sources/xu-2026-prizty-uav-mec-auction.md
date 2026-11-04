---
type: source
modeling_card: required
title: "A Privacy-Preserving Auction for Task Offloading and Resource Allocation in UAV-Assisted MEC"
authors: ["Jiajie Xu", "Xiaolong Xu", "Guangming Cui", "Muhammad Bilal", "Rong Gu", "Wanchun Dou", "Arumugam Nallanathan"]
year: 2026
url: "https://doi.org/10.1109/TMC.2025.3609202"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, uav-mec, mobile-edge-computing, task-offloading, resource-allocation, reverse-auction-incentive, privacy, noma, uav-trajectory-control]
related: ["[[mobile-edge-computing]]", "[[task-offloading]]", "[[multi-uav-assisted-mec]]", "[[uav-trajectory-control]]", "[[reverse-auction-incentive]]", "[[noma]]", "[[privacy-sensitive-data-partitioning]]", "[[xu-2021-secure-uav-mec-dual-uav]]", "[[wang-2024-blockchain-uav-mec-dpos]]", "[[zhang-2024-uav-task-offloading-ddpg]]"]
created: 2026-07-06
updated: 2026-11-03
---

# A Privacy-Preserving Auction for Task Offloading and Resource Allocation in UAV-Assisted MEC

## Citation

Xu, J., Xu, X., Cui, G., Bilal, M., Gu, R., Dou, W., & Nallanathan, A. (2026). *A Privacy-Preserving Auction for Task Offloading and Resource Allocation in UAV-Assisted MEC*. **IEEE Transactions on Mobile Computing**, 25(2), 2611-2626. DOI: 10.1109/TMC.2025.3609202.

## TL;DR

Introduces **Prizty**, a privacy-preserving reverse-auction framework for UAV-assisted MEC task offloading and resource allocation. Edge computing nodes (edge servers plus UAVs) bid to serve UE tasks, while UE locations are obfuscated before scheduling. The mechanism jointly handles UAV/edge-server service selection, UAV target locations, computation resources, and payments, targeting low social cost while preserving truthfulness and individual rationality.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: UEs offload delay-sensitive tasks over NOMA uplinks to edge computing nodes (ECNs), which include UAVs, or to a remote cloud. Each slot runs a reverse auction in which ECNs bid to serve sets of UEs. UE locations are perturbed with Laplace noise for geo-indistinguishability before scheduling, and UAV energy and processing range limit which UEs an ECN can serve.

**Problem & objective**: Problem (9) minimizes the total social cost $\sum_t\sum_n\sum_{s\in\mathbf J_n^t}\big(x_{n,s}^tP_{n,s}^t+\sum_{m\in\mathbf S_c^t}\xi\,d(m)\big)$, the winning bid prices plus the cost of tasks sent to the cloud, with truthful and individually rational bidding.

**Decision variables**:
| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Bid acceptance | $x_{n,s}^t$ | binary | Whether bid $s$ of ECN $n$ wins in slot $t$ |
| Computing allocation | $r_n^t$ | continuous, nonnegative | Computing resource allocated to ECN $n$ |
| Payment | $w_n^t$ | continuous, nonnegative | Payment to winning ECN $n$, equal to its critical bid |
| Perturbed UE location | $(x',y')$ | randomized point | Laplace-perturbed location used for scheduling |

**Constraints**:
| ID | Meaning and key expression |
|---|---|
| (9a) | Every UE not sent to the cloud is covered by a winning bid |
| (9b) | Each ECN wins at most one bid per round (XOR bidding) |
| (9c) | Allocated computing does not exceed the total, $\sum_nr_n^t\le r_{\mathrm{total}}^t$ |
| (9d) | $x_{n,s}^t\in\{0,1\}$ |
| (9e) | UAV energy stays within $[\beta E_{u,\max},E_{u,\max}]$ |
| (9f) | Served UEs lie within the ECN processing distance, $D_{m,n}^t\le D_n^{\max}+R_n^{\max}$ |
| (9g) | Served workload fits ECN capacity, $\sum_mc(m)\le F_n^{\max}$ |

**Algorithm**: Prizty first perturbs UE locations with Laplace noise (PPA), then SSEA builds feasible service regions and UAV positions from intersecting coverage areas, and WPA selects winners by balancing social cost and utility and sets critical payments. Tasks go to the cloud when no ECN is available or computing is exhausted. The auction is proven truthful and individually rational.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Xu et al. [x] studied a privacy-preserving reverse auction for task offloading and resource allocation in UAV-assisted mobile edge computing. The model selects winning bids, computing allocation, and payments to minimize social cost under coverage, XOR-bidding, computing, UAV energy, processing-range, and capacity constraints. UE locations are perturbed with Laplace noise and checked against geo-indistinguishability before allocation. SSEA constructs feasible service sets and UAV positions, while WPA selects winners and computes critical-bid payments that target truthfulness and individual rationality. Simulations show Prizty slightly ahead of Greedy, TOCA, and Ptero (average gains of about 1% to 2.4%), but behind the optimal allocation, with about 12.9% higher social cost than the optimum in one experiment set.

## Problem framing

UAVs can temporarily provide MEC offloading service when edge servers are damaged, overloaded, or unavailable. Existing UAV-assisted MEC systems still face uneven resource allocation, low utilization, load imbalance, and poor dynamic adaptability. The paper adds a privacy constraint: UE-sensitive information, especially location, can leak during UAV-assisted computation, so offloading and resource allocation should not require exposing exact UE locations.

## System model

- The system contains UEs, edge servers, UAVs, and a remote cloud over discrete time slots.
- Active UEs generate service demands; tasks may be served by edge servers, UAVs, or the cloud.
- Edge computing nodes include both fixed edge servers and UAVs, with UAV movement, coverage, compute, and battery constraints.
- Communication uses a 3D distance model with NOMA/SIC for concurrent UE access.
- Computation latency depends on allocated CPU frequency; the objective is total social cost minimization subject to coverage, bid, resource, battery, distance, and CPU constraints.

## Method

- Models service provisioning as a reverse auction where edge computing nodes are bidders and the service provider is the auctioneer.
- Ties bids to latency, energy consumption, and UAV residual battery rather than treating bids as opaque prices.
- Uses a privacy-preserving auction phase that perturbs UE locations with Laplace noise, expands the measurement area, and checks Geo-Indistinguishability.
- Builds feasible service sets and UAV target locations through SSEA under distance, computation, and energy constraints.
- Runs WPA to select winners and compute payments with a critical-bid / second-price-style incremental cost rule.

## Key findings

- On the small-scale setting, Prizty is second to Optimal and outperforms Greedy, TOCA, and Ptero across offload rate, latency, energy, and social cost.
- The small-scale averages report Prizty within 0.98% fewer offloaded UEs than Optimal, with 2.78% higher latency, 3.16% higher energy, and 12.88% higher social cost.
- On large-scale settings where Optimal is not executable, Prizty outperforms Greedy, TOCA, and Ptero in offload rate, latency, energy, and total system cost.
- The privacy evaluation reports that Prizty balances privacy and location-data utility, with inference attack success rate below 7% in the evaluated scenarios.

## Limitations / future work

The explicit future-work direction is time-slot utilization: instead of discarding unfinished tasks at slot boundaries, future designs should allow tasks to continue into later slots.

## Relation to the corpus

This page extends the market-mechanism side of the corpus. It is a UAV-MEC reverse-auction counterpart to [[zeng-2024-usv-fleet-collaborative-offloading]], but adds UE-location privacy and UAV trajectory-aware service feasibility. Its privacy angle sits near [[privacy-sensitive-data-partitioning]], while its NOMA/SIC offloading model connects it to [[noma]] and the broader [[task-offloading]] track. It is also a useful security/trust neighbor to [[wang-2024-blockchain-uav-mec-dpos]] and [[xu-2021-secure-uav-mec-dual-uav]], though its mechanism is auction/privacy rather than blockchain or physical-layer secure computation.

## Raw artifacts

- Parse: `raw/sources/A_Privacy-Preserving_Auction_for_Task_Offloading_and_Resource_Allocation_in_UAV-Assisted_MEC/A_Privacy-Preserving_Auction_for_Task_Offloading_and_Resource_Allocation_in_UAV-Assisted_MEC.md`
- Origin PDF: `raw/sources/A_Privacy-Preserving_Auction_for_Task_Offloading_and_Resource_Allocation_in_UAV-Assisted_MEC/A_Privacy-Preserving_Auction_for_Task_Offloading_and_Resource_Allocation_in_UAV-Assisted_MEC.pdf`
- Figures: `raw/sources/A_Privacy-Preserving_Auction_for_Task_Offloading_and_Resource_Allocation_in_UAV-Assisted_MEC/images/`
