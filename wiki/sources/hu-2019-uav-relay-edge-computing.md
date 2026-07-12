---
type: source
title: "UAV-Assisted Relaying and Edge Computing: Scheduling and Trajectory Optimization"
authors: ["Xiaoyan Hu", "Kai-Kit Wong", "Kun Yang", "Zhongbin Zheng"]
year: 2019
url: "https://doi.org/10.1109/TWC.2019.2928539"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, uav-mec, uav-mobile-relaying, computation-offloading, trajectory-design, resource-scheduling, information-causality-constraint, alternating-optimization-sdr-sca]
related:
  - "[[uav-mobile-relaying]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[task-offloading]]"
  - "[[uav-trajectory-control]]"
  - "[[information-causality-constraint]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[energy-latency-tradeoff]]"
  - "[[zeng-2016-throughput-relaying]]"
  - "[[hu-2019-pdd-uav-mec-offloading]]"
  - "[[zhang-2019-uav-iot-comp-comm]]"
  - "[[yu-2020-uav-ec-collaborative-offloading]]"
  - "[[kai-kit-wong]]"
created: 2026-06-01
updated: 2026-07-13
---

# UAV-Assisted Relaying and Edge Computing: Scheduling and Trajectory Optimization

## Citation

Hu, X., Wong, K.-K., Yang, K., & Zheng, Z. (2019). *UAV-Assisted Relaying and Edge Computing: Scheduling and Trajectory Optimization*. **IEEE Transactions on Wireless Communications**, 18(10), 4738–4752. DOI: 10.1109/TWC.2019.2928539. (Received 5 Dec 2018; revised 13 Apr 2019 and 19 Jun 2019; accepted 28 Jun 2019; date of publication 19 Jul 2019; date of current version 9 Oct 2019 → year 2019. Presented in part at IEEE GLOBECOM 2019.)

## TL;DR

A UAV-assisted MEC architecture where one **cellular-connected UAV** simultaneously acts as (1) an **MEC server** computing user-equipment (UE) tasks and (2) a **relay** that further offloads UE tasks to an access point (AP) for computing — exploiting the UAV's energy-efficient LoS links. The paper minimizes the **weighted sum energy consumption (WSEC)** of the UAV and the UEs, subject to UE task constraints, **information-causality constraints**, bandwidth-allocation constraints, and UAV trajectory constraints, by jointly optimizing **computation-resource scheduling**, **bandwidth allocation**, and the **UAV trajectory** via an iterative **alternating optimization** algorithm with guaranteed convergence.

## Problem framing

Cellular-based MEC completes UE tasks at the AP; UAV-enabled MEC completes them at the UAV's onboard server. But for UEs whose link to the AP is severely blocked, the AP's compute cannot be used directly; and relying only on the size/resource-limited UAV is risky. This is the first work to let the UAV serve as an **MEC server and a relay at the same time**, using both the UAV's and the AP's compute. The resulting joint scheduling + bandwidth + trajectory problem is non-convex due to coupled variables.

## System model

- **Actors.** One AP (grid power + ultra-high-performance server), one **cellular-connected UAV** (battery-powered, onboard comms circuit + compute processor), and $K$ ground UEs, all single-antenna. Each UE has a bit-wise-independent computation-intensive task.
- **UAV roles.** Provide MEC service (share compute with UEs) **and** relaying service (forward part of UEs' offloaded tasks to the AP to save UAV energy).
- **Constraints.** UE task constraints; **[[information-causality-constraint]]** (forward only already-received data); bandwidth-allocation constraints; UAV trajectory constraints.
- **Objective.** Minimize the **weighted sum energy consumption** of the UAV + UEs.

## Method

- **Alternating optimization** decoupling the problem into three subproblems solved iteratively:
  1. **Computation-resource scheduling** (offload/download task sizes, CPU frequencies at each UE and the UAV) and **bandwidth allocation** — obtained in **closed form** via Lagrange duality (subgradient for inequality multipliers, bisection for equality multipliers).
  2. **UAV trajectory** — solved with CVX via **[[alternating-optimization-sdr-sca|SCA]]**.
- Convergence of the alternating algorithm is guaranteed; complexity is reported as acceptable.

## Key findings

- The optimized **UAV trajectory is strongly shaped** by the relative AP location and the distribution of UE task sizes (parse, conclusion).
- The proposed algorithm yields **significant and more stable performance gains** over baselines: preset-trajectory, offloading-only, equal-bandwidth-allocation, and local-computing-without-offloading (stated; magnitudes figure-derived and indicative).
- Advantages become **more prominent for computation-intensive, latency-critical tasks** (stated).

## Limitations / future work

Simulation-based; single UAV, single AP, single-antenna nodes. The parse does not enumerate an explicit future-work list → `not in parse`.

## Relation to the corpus

The **relay + MEC-server fusion** entry of the UAV-MEC track: it inherits the **information-causality + SCA** machinery of the UAV mobile-relaying anchor [[zeng-2016-throughput-relaying]] (grounding [[uav-mobile-relaying]] and [[information-causality-constraint]]) but redirects it from a throughput objective to a **weighted-sum-energy offloading** objective. Distinct from the same-surname single-UAV MEC offloading paper [[hu-2019-pdd-uav-mec-offloading]] (different first author — **Qiyu Hu**, Zhejiang University — and a penalty-dual-decomposition min-max-delay design). Methodologically adjacent to the convex/SCA UAV-MEC line [[zhang-2019-uav-iot-comp-comm]] and the collaborative UAV+edge-cloud offloading of [[yu-2020-uav-ec-collaborative-offloading]].

## Raw artifacts

- `raw/sources/UAV-Assisted_Relaying_and_Edge_Computing_Scheduling_and_Trajectory_Optimization/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
