---
type: source
title: "Latency Minimization Oriented Hybrid Offshore and Aerial-Based Multi-Access Computation Offloading for Marine Communication Networks"
authors: ["Minghui Dai", "Ning Huang", "Yuan Wu", "Liping Qian", "Bin Lin", "Zhou Su", "Rongxing Lu"]
year: 2023
url: "https://doi.org/10.1109/TCOMM.2023.3306581"
venue: "IEEE Transactions on Communications (IEEE TCOMM)"
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
updated: 2026-05-31
---

# Latency Minimization Oriented Hybrid Offshore and Aerial-Based Multi-Access Computation Offloading for Marine Communication Networks

## Citation

Dai, M., Huang, N., Wu, Y., Qian, L., Lin, B., Su, Z., & Lu, R. (2023). *Latency Minimization Oriented Hybrid Offshore and Aerial-Based Multi-Access Computation Offloading for Marine Communication Networks*. **IEEE Transactions on Communications**. DOI: 10.1109/TCOMM.2023.3306581. (Date of publication 18 Aug 2023; date of current version 20 Nov 2023.)

## TL;DR

A **hybrid offshore + aerial multi-access MEC** scheme for marine networks where an **unmanned surface vehicle (USV)** simultaneously offloads parts of its workload to an **offshore base station via FDMA** and to **multiple hovering UAVs via NOMA**. It **Minimizes the Maximum Workloads Latency (MMWL)** by jointly optimizing the offloading decision, FDMA/NOMA transmission durations, and computing-rate allocation across USV, UAVs, and base station. The non-convex problem is decomposed via a **layered structure** into three subproblems with efficient near-optimal algorithms.

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
