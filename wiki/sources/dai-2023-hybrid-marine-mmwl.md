---
type: source
title: "Latency Minimization Oriented Hybrid Offshore and Aerial-Based Multi-Access Computation Offloading for Marine Communication Networks"
authors: ["Minghui Dai", "Ning Huang", "Yuan Wu", "Liping Qian", "Bin Lin", "Zhou Su", "Rongxing Lu"]
year: 2023
url: "https://doi.org/10.1109/TCOMM.2023.3306581"
venue: "IEEE Transactions on Communications (IEEE TCOMM)"
modeling_card: required
tags: [source, maritime-mec, computation-offloading, noma, fdma, latency-minimization, resource-allocation, multi-access]
related:
  - "[[maritime-mec]]"
  - "[[noma]]"
  - "[[task-offloading]]"
  - "[[two-stage-decomposition]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[wang-2024-maritime-eh-jcora]]"
  - "[[lyu-2023-noma-marine-emergency-offloading]]"
  - "[[wang-2024-twotier-satellite-marine]]"
created: 2026-05-31
updated: 2026-07-16
---

# Latency Minimization Oriented Hybrid Offshore and Aerial-Based Multi-Access Computation Offloading for Marine Communication Networks

## Citation

Dai, M., Huang, N., Wu, Y., Qian, L., Lin, B., Su, Z., & Lu, R. (2023). *Latency Minimization Oriented Hybrid Offshore and Aerial-Based Multi-Access Computation Offloading for Marine Communication Networks*. **IEEE Transactions on Communications**. DOI: 10.1109/TCOMM.2023.3306581. (Date of publication 18 Aug 2023; date of current version 20 Nov 2023.)

## TL;DR

A **hybrid offshore + aerial multi-access MEC** scheme for marine networks where an **unmanned surface vehicle (USV)** simultaneously offloads parts of its workload to an **offshore base station via FDMA** and to **multiple hovering UAVs via NOMA**. It **Minimizes the Maximum Workloads Latency (MMWL)** by jointly optimizing the offloading decision, FDMA/NOMA transmission durations, and computing-rate allocation across USV, UAVs, and base station. The non-convex problem is decomposed via a **layered structure** into three subproblems with efficient near-optimal algorithms.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: One USV divides each marine task among local computation, an offshore BS edge server, and a cluster of hovering UAV edge servers. The USV uses FDMA for the offshore link and NOMA for simultaneous aerial offloading; aerial channels are quasi-static LoS links under fixed USV and UAV positions during transmission.

**Problem & objective**: Problem (MMWL) is a strictly nonconvex min-max latency problem, $\min\max_{n\in\mathcal N} t_n^{\mathrm{ove}}$, over workload splitting, FDMA and NOMA durations, and computing-rate allocation.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| BS offloading ratio | $\alpha_{n,B}$ | continuous, $[0,1]$ | Fraction of task $n$ offloaded to the offshore BS |
| UAV offloading ratio | $\alpha_{n,k}$ | continuous, $[0,1]$ | Fraction of task $n$ offloaded to UAV $k$ |
| NOMA transmission time | $t^{\mathrm{tran}}$ | continuous, $[0,T^{\max}]$ | Common duration for aerial NOMA offloading |
| FDMA transmission time | $t_{u,B}$ | continuous, $[0,T_B^{\max}]$ | Duration of USV offloading to the offshore BS |
| USV compute rate | $\varrho_u$ | continuous, $[0,\varrho_u^{\max}]$ | CPU rate assigned to local execution |
| BS compute rate | $\varrho_B$ | continuous, $[0,\varrho_B^{\max}]$ | Offshore BS CPU allocation |
| UAV compute rate | $\varrho_k$ | continuous, $[0,\varrho^{\max}]$ | CPU allocation at UAV $k$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| 1, 19-21 | Task fractions satisfy $\sum_k\alpha_{n,k}+\alpha_{n,B}+\beta_n=1$ and each fraction lies in $[0,1]$ |
| 22-23 | FDMA and NOMA durations satisfy $t_{u,B}\leq T_B^{\max}$ and $t^{\mathrm{tran}}\leq T^{\max}$ |
| 24-25 | USV transmit powers for the BS and UAV links do not exceed $P^{\max}$ and $Q^{\max}$ |
| 26 | Per-task USV energy satisfies $E_{u,n}^{\mathrm{tot}}\leq E^{\max}$ |
| 27-29 | BS, USV, and UAV computing rates remain within their respective capacities |

**Algorithm**: Transform MMWL into a layered sequence of three subproblems; test feasible offloading regions for a candidate maximum latency, use bisection to obtain workload fractions, apply two-dimensional linear search to the FDMA and NOMA durations, recover the computing-rate allocations, and propagate each optimum to the next layer.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Dai et al. [x] studied hybrid offshore and aerial multi-access computation offloading for a marine network in which a USV uses FDMA to an offshore BS and NOMA to multiple hovering UAV edge servers. They formulated the MMWL problem to minimize the maximum workload latency by jointly optimizing task offloading ratios, FDMA and NOMA transmission durations, and computing-rate allocation under transmission, power, energy, and computing-capacity limits. Their layered approach decomposes the strictly nonconvex formulation into three subproblems and combines feasibility checking, bisection, and linear search to obtain the solutions. Simulations report an average latency difference no greater than 3% relative to the LINGO global solution and average computation-time savings above 90%.

## Problem framing

Marine applications (ocean farming, marine tourism, environmental sensing) generate compute-intensive, delay-sensitive tasks, but marine networks have limited communication and computing resources and harsh channels. Multi-access edge computing splits a task across multiple servers; the design question is how to combine offshore (powerful, but higher transmission delay) and aerial (flexible, on-demand LoS) computing with appropriate multiple-access modes to minimize completion latency.

## System model

- **Actors.** One USV (the task source), an **offshore base station** with edge server (high compute), and a **cluster of UAVs** hovering as aerial MEC servers.
- **Multi-access.** Workloads partially offloaded to the base station over **FDMA** (avoids co-channel interference) and to multiple UAVs over **NOMA** (improves channel utilization), in a [[two-stage-decomposition|multi-access]] manner.
- **Objective.** Minimize the maximum workloads latency (MMWL) by jointly optimizing offloading decision, FDMA transmission duration, NOMA transmission duration, and computing-rate allocation at USV/UAV/BS, while reducing USV energy consumption.

## Method

- Exploit the structure of the formulated non-convex problem to apply a **layered structure** decomposition into **three subproblems**.
- Design efficient algorithms to obtain the (near-)optimal solutions for each subproblem and validate optimality.

## Key findings

- The proposed algorithms attain a latency very close to the global optimum from the **LINGO** solver, with **average difference no greater than 3%** (stated verbatim).
- Computation time is greatly reduced — **average saving above 90%** versus LINGO (stated verbatim).
- The scheme also beats other benchmark schemes for task completion time.

## Limitations / future work

Simulation-based. Future work (stated): model the **underwater acoustic communication** system (channel attenuation, time-varying multipath) to further enhance underwater throughput.

## Relation to the corpus

A **maritime MEC** entry whose defining feature is **hybrid FDMA-offshore + NOMA-aerial multi-access** offloading — a complement to the energy-harvesting Lyapunov scheme [[wang-2024-maritime-eh-jcora]] (shares co-author Bin Lin) and the NOMA-based marine emergency offloading of [[lyu-2023-noma-marine-emergency-offloading]] (both use NOMA + decomposition for marine IoT). Its multi-server split echoes the game-theoretic two-tier satellite-marine design [[wang-2024-twotier-satellite-marine]]. Shares senior author Yuan Wu (University of Macau) with the CMOP-evolutionary lineage. Reinforces [[maritime-mec]] and [[noma]].

## Raw artifacts

- `raw/sources/Latency_Minimization_Oriented_Hybrid_Offshore_and_Aerial-Based_Multi-Access_Computation_Offloading_for_Marine_Communication_Networks/full.md`
- Original PDF and extracted figures in the same folder.
