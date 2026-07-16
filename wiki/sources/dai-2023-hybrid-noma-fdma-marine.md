---
type: source
title: "UAV-Assisted Multi-Access Computation Offloading via Hybrid NOMA and FDMA in Marine Networks"
authors: ["Minghui Dai", "Yuan Wu", "Liping Qian", "Zhou Su", "Bin Lin", "Nan Chen"]
year: 2023
url: "https://doi.org/10.1109/TNSE.2022.3205303"
venue: "IEEE Transactions on Network Science and Engineering (IEEE TNSE)"
modeling_card: required
tags: [source, maritime-mec, computation-offloading, noma, fdma, energy-efficiency, physical-layer-security, multi-access]
related:
  - "[[maritime-mec]]"
  - "[[noma]]"
  - "[[task-offloading]]"
  - "[[two-stage-decomposition]]"
  - "[[physical-layer-security]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[dai-2023-hybrid-marine-mmwl]]"
  - "[[dai-2024-multiuav-marine-welfare]]"
  - "[[li-2023-secure-marine-iot-jamming]]"
  - "[[lyu-2023-noma-marine-emergency-offloading]]"
  - "[[minghui-dai]]"
  - "yuan-wu"
  - "[[liping-qian]]"
  - "[[bin-lin]]"
created: 2026-06-01
updated: 2026-07-16
---

# UAV-Assisted Multi-Access Computation Offloading via Hybrid NOMA and FDMA in Marine Networks

## Citation

Dai, M., Wu, Y., Qian, L., Su, Z., Lin, B., & Chen, N. (2023). *UAV-Assisted Multi-Access Computation Offloading via Hybrid NOMA and FDMA in Marine Networks*. **IEEE Transactions on Network Science and Engineering**. DOI: 10.1109/TNSE.2022.3205303. (Manuscript received 16 May 2022; accepted 5 September 2022; date of publication 9 September 2022; date of current version 6 January 2023 → year 2023.)

## TL;DR

A two-segment **marine multi-access computation offloading** scheme that minimizes the **total energy consumption of ocean devices**. In the **underwater segment**, multiple **underwater sensor nodes (USNs)** covered by an **unmanned surface vehicle (USV)** upload sensing data via **NOMA** over acoustic channels (improving channel utilization). In the **radio-frequency segment**, multiple **UAVs** hovering as aerial edge servers receive USV-offloaded workloads via **FDMA** (avoiding co-channel interference), while a **malicious node** may overhear the USV's offloading transmission. The non-convex joint optimization of USNs' uploading time, USV's computation offloading, USV's offloading time, and **secrecy provisioning** is solved by a **layered (top-problem / sub-problem) decomposition** with line-search algorithms.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Underwater sensor nodes upload sensing data over acoustic NOMA to a USV, which transcodes the data, computes part locally, and offloads the remainder over RF FDMA to multiple hovering UAV edge servers. A malicious node can overhear USV-to-UAV transmissions, so the model includes secrecy-outage provisioning.

**Problem & objective**: Problem (ECM) is a strictly nonconvex energy-minimization problem, $E_{\mathrm{tot}}^{\min}=\min E^{\mathrm{tot}}$, where total energy includes USN uploading and USV transcoding, local-computing, and offloading energy.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Underwater uploading time | $t^{\mathrm{Ph-I}}$ | continuous, $[0,t^{\max}]$ | NOMA duration for USN-to-USV uploading |
| UAV offloaded workload | $d_{u,k}^{\mathrm{off}}$ | continuous, $[0,D_u^{\mathrm{tot}}]$ | Data assigned by the USV to UAV $k$ |
| RF offloading time | $t_{u,k}^{\mathrm{Ph-IV}}$ | continuous, nonnegative | FDMA duration for USV-to-UAV $k$ offloading |
| Secrecy provisioning | $\varsigma_k$ | continuous, $[0,1]$ | Secrecy-outage allocation for the link to UAV $k$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| 33 | Uploaded data satisfies $0\leq d_i^{\mathrm{up}}\leq D_i^{\max}$ |
| 34-35 | USN and USV transmit powers satisfy $p_{i,u}^{\mathrm{Ph-I}}\leq P_{i,u}^{\max}$ and $q_{u,k}\leq Q_{u,k}^{\max}$ |
| 36-37 | Each $d_{u,k}^{\mathrm{off}}$ and their sum do not exceed $D_u^{\mathrm{tot}}$ |
| 38 | Underwater NOMA time satisfies $0\leq t^{\mathrm{Ph-I}}\leq t^{\max}$ |
| 39 | Overall completion latency satisfies $0\leq t^{\mathrm{ove}}\leq T^{\max}$ |
| 1, 20, 28 | USV displacement, offloaded-data balance, and secrecy-outage requirements remain feasible |

**Algorithm**: Decompose ECM into a top problem for $t^{\mathrm{Ph-I}}$ and a subproblem for workload, RF time, and secrecy provisioning; solve the workload subproblem as a strictly convex program for fixed RF time and secrecy; use two-dimensional line search for $t_{u,k}^{\mathrm{Ph-IV}}$ and $\varsigma_k$; then use one-dimensional line search for $t^{\mathrm{Ph-I}}$.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Dai et al. [x] studied energy-efficient computation offloading through hybrid NOMA and FDMA in a two-segment marine network. Underwater sensor nodes upload data to a USV through acoustic NOMA, and the USV partially offloads the processed workload through RF FDMA to hovering UAV edge servers while accounting for a malicious eavesdropper. They formulated ECM to minimize the total energy consumption of the sensor nodes and USV over uploading time, offloaded workload, RF offloading time, and secrecy provisioning, and solved it with a layered combination of a convex subroutine and one-dimensional and two-dimensional line searches. Numerical results show that the proposed algorithms obtain energy values close to the LINGO global solution with substantially lower computation time than LINGO in the reported experiments.

## Problem framing

Marine applications (safe navigation, offshore-platform monitoring, hydrological sensing, maritime rescue) generate compute-intensive, delay-sensitive tasks, but USNs are battery-powered, hard to recharge, and connected by low-rate, high-delay, lossy acoustic links. Energy-efficient offloading is therefore essential. The paper argues TDMA (strict timing overhead) and FDMA (low acoustic-bandwidth utilization) are inferior to **NOMA** for the underwater uploading, while the radio broadcast nature of the RF segment exposes the USV's offloading to eavesdropping — so **secrecy provisioning** must enter the energy-minimization design.

## System model

- **Underwater segment.** USNs form a **NOMA** cluster to upload sensing data to the USV over acoustic channels.
- **RF segment.** The USV offloads partial workloads to multiple hovering **UAVs** (aerial base stations / edge servers) via **FDMA**, subject to an **eavesdropping attack** from a malicious node (secrecy provisioning required).
- **Objective.** Minimize the **total energy consumption** of the USNs and the USV, jointly over: USNs' uploading time, USV's computation-offloading decision, USV's offloading time, and the secrecy provisioning.

## Method

- **Layered-structure decomposition** of the non-convex joint problem into a **top-problem** (USNs' uploading time) and a **sub-problem** (USV's computation offloading + offloading time + secrecy provisioning).
- **Sub-problem:** given the uploading time, offloading time, and secrecy provisioning, first solve the optimal USV computation offloading; then a **two-dimensional line-searching** algorithm finds the optimal USV offloading time and secrecy provisioning.
- **Top-problem:** a line-searching method finds the optimal USNs' uploading time.

## Key findings

- The proposed algorithms obtain the **minimum energy consumption** and are validated against the **globally optimal solution from the LINGO solver** (stated; the parse asserts effectiveness/efficiency vs LINGO without quoting a fixed gap percentage → magnitudes figure-derived and indicative).
- The scheme **significantly reduces energy consumption versus benchmark schemes** (abstract, verbatim sense).

## Limitations / future work

Simulation-based. Future work (stated): study the **multi-USN NOMA grouping** scenario in the underwater environment, where the **coalition formation** of NOMA grouping will be investigated.

## Relation to the corpus

A **maritime MEC** entry from the University-of-Macau group around [[minghui-dai]], yuan-wu, and [[liping-qian]] (with [[bin-lin]]). It is **distinct from** the same lead author's [[dai-2023-hybrid-marine-mmwl]]: that paper (IEEE TCOMM) minimizes **max workloads latency (MMWL)** with FDMA-offshore + NOMA-aerial access, whereas this one (IEEE TNSE) minimizes **total energy** with **NOMA-underwater (USN→USV) + FDMA-aerial (USV→UAV)** access and adds an explicit **secrecy-provisioning** term against an eavesdropper. It complements the secure marine-IoT cooperative-jamming design [[li-2023-secure-marine-iot-jamming]] (shares [[bin-lin]]) and the multi-UAV marine welfare/auction design [[dai-2024-multiuav-marine-welfare]], and shares the NOMA + decomposition recipe with [[lyu-2023-noma-marine-emergency-offloading]]. Reinforces [[maritime-mec]], [[noma]], and [[physical-layer-security]].

## Raw artifacts

- `raw/sources/UAV-Assisted_Multi-Access_Computation_Offloading_via_Hybrid_NOMA_and_FDMA_in_Marine_Networks/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
