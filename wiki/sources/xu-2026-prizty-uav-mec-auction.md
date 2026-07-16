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
updated: 2026-07-16
---

# A Privacy-Preserving Auction for Task Offloading and Resource Allocation in UAV-Assisted MEC

## Citation

Xu, J., Xu, X., Cui, G., Bilal, M., Gu, R., Dou, W., & Nallanathan, A. (2026). *A Privacy-Preserving Auction for Task Offloading and Resource Allocation in UAV-Assisted MEC*. **IEEE Transactions on Mobile Computing**, 25(2), 2611-2626. DOI: 10.1109/TMC.2025.3609202.

## TL;DR

Introduces **Prizty**, a privacy-preserving reverse-auction framework for UAV-assisted MEC task offloading and resource allocation. Edge computing nodes (edge servers plus UAVs) bid to serve UE tasks, while UE locations are obfuscated before scheduling. The mechanism jointly handles UAV/edge-server service selection, UAV target locations, computation resources, and payments, targeting low social cost while preserving truthfulness and individual rationality.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: UEs submit delay-sensitive tasks to fixed edge servers, mobile UAV edge nodes, or a remote cloud over slotted NOMA access. Edge nodes bid to provide service, UE locations are perturbed for geo-indistinguishability, and UAV movement, computing capacity, and battery constrain feasible winners.

**Problem & objective**: A privacy-preserving reverse-auction allocation problem minimizes total social cost, $\min C_{\mathrm{social}}=C_{\mathrm{latency}}+C_{\mathrm{energy}}+C_{\mathrm{payment}}$, while preserving truthful and individually rational bidding.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Winner assignment | $x_{u,j}$ | binary | Edge node $j$ selected for UE task $u$ |
| UAV target location | $\mathbf q_j$ | continuous 3-D position | Service position of UAV bidder $j$ |
| CPU allocation | $f_{u,j}$ | continuous, nonnegative | Computing resource assigned to task $u$ |
| Winning payment | $p_j$ | continuous, nonnegative | Critical payment to winning edge node $j$ |
| Perturbed UE location | $\tilde{\mathbf w}_u$ | randomized continuous point | Privacy-preserving scheduling location |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Each accepted task is assigned to one feasible edge node or the cloud |
| C2 | UAV coverage, target distance, movement, and battery remain feasible |
| C3 | Per-node CPU allocations do not exceed computing capacity |
| C4 | Task communication and computation meet latency and NOMA/SIC conditions |
| C5 | Winner selection and critical payments satisfy truthfulness and individual rationality |

**Algorithm**: Add Laplace noise to UE locations and verify geo-indistinguishability → construct feasible service sets and UAV target locations with SSEA → evaluate bidder cost from latency, energy, and residual battery → select winners with WPA → compute critical incremental-cost payments → execute offloading and resource allocation.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Xu et al. [x] studied a privacy-preserving reverse auction for task offloading and resource allocation in UAV-assisted mobile edge computing. The model jointly selects fixed or UAV edge servers, UAV target locations, computation resources, and payments under coverage, latency, NOMA, CPU, movement, and battery constraints. UE locations are perturbed with Laplace noise and checked against geo-indistinguishability before allocation. SSEA constructs feasible service sets and UAV positions, while WPA selects winners and computes critical-bid payments that target truthfulness and individual rationality. Simulations report lower social cost, latency, and energy than the evaluated Greedy, TOCA, and Ptero methods, while the measured inference-attack success remains low in the tested settings.

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
