---
type: source
title: "Latency Minimization for UAV-Enabled URLLC-Based Mobile Edge Computing Systems"
authors: ["Qingjie Wu", "Miao Cui", "Guangchi Zhang", "Feng Wang", "Qingqing Wu", "Xiaoli Chu"]
year: 2024
url: "https://doi.org/10.1109/TWC.2023.3307154"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, uav-mec, urllc, finite-blocklength, latency-minimization, trajectory-design, sca, block-coordinate-descent]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[uav-trajectory-control]]"
  - "[[task-offloading]]"
  - "[[finite-blocklength-urllc]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[binary-vs-partial-offloading]]"
  - "[[hu-2019-pdd-uav-mec-offloading]]"
  - "[[liu-2022-miso-uav-mec-trajectory]]"
  - "[[yang-2022-stochastic-uav-mec-lyapunov]]"
created: 2026-05-31
updated: 2026-06-09
---

# Latency Minimization for UAV-Enabled URLLC-Based Mobile Edge Computing Systems

## Citation

Wu, Q., Cui, M., Zhang, G., Wang, F., Wu, Q., & Chu, X. (2024). *Latency Minimization for UAV-Enabled URLLC-Based Mobile Edge Computing Systems*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2023.3307154. (Date of publication 28 Aug 2023; date of current version 11 Apr 2024.)

## TL;DR

A UAV-enabled MEC system where K ground devices offload **mission-critical, latency-sensitive** tasks to a UAV-carried MEC server over **URLLC (finite-blocklength)** links and compute the rest locally. It minimizes the **maximum computation latency** among all devices by jointly optimizing devices'/UAV's computing times and CPU frequencies, devices' offloading bandwidths, and the **3D UAV location**. The non-convex problem is decomposed (via **BCD**) into three subproblems — UAV horizontal location, UAV altitude, and bandwidth+CPU-frequency — solved alternately with **SCA**; the bandwidth/frequency subproblem gets a **semi-closed-form** solution.

## Problem framing

Existing UAV-MEC work assumes **infinite blocklength** and uses the Shannon capacity, but URLLC packets are short (e.g. 20–32 bytes), so blocklength is finite and decoding error is non-negligible — the Shannon formula cannot express the data rate. The paper is the first (per its claim) to study multi-user **URLLC-based** UAV-MEC, additionally modeling the UAV-device channel with the more accurate **angle-dependent Rician fading** model instead of pure LoS, which makes the finite-blocklength rate intractable and the problem non-convex.

## System model

- **Actors.** One UAV-carried MEC server and K single-antenna ground devices with mission-critical tasks; each device offloads part of its task via URLLC and computes the rest locally.
- **Channel/rate.** Angle-dependent **Rician fading**; the finite-blocklength offloading rate (function of SNR, blocklength, decoding-error probability) is derived for a fixed maximum tolerable outage probability and expressed as a function of UAV location.
- **Objective.** Minimize the maximum computation latency across devices, jointly over computing times, CPU frequencies (devices + UAV), offloading bandwidths, and 3D UAV location.

## Method

- Approximate the finite-blocklength data-rate expression by a tractable **logarithmic form**.
- Decompose via **[[alternating-optimization-sdr-sca|BCD]]** into three subproblems (UAV horizontal location, UAV altitude, bandwidth + CPU frequency), solved alternately with **SCA** to convergence.
- Transform the bandwidth/frequency subproblem (min-max latency) into an equivalent **max-min completed-task-ratio** problem, then solve to a **semi-closed-form** via a novel two-layer algorithm. Complexity O((KN)^3.5 log(1/δ)); converges in ~4 iterations.

## Key findings

- The proposed algorithm achieves **significantly lower computation latency** than benchmarks (w/o location optimization; w/o bandwidth & frequency optimization; Shannon-based) and approaches the "lower bound" scheme (read from Figs. 3–5; reported qualitatively).
- **Bottleneck-dependent insight:** optimizing UAV location + offloading bandwidth helps most when **communication** is the bottleneck, while optimizing CPU frequency helps most when **computing** is the bottleneck (stated in the conclusion).
- Using the **accurate finite-blocklength** rate (vs the Shannon formula) is **necessary** — the latency gap to the Shannon-based scheme is significant.

## Limitations / future work

Single UAV; simulation-based. Conclusion emphasizes the bottleneck insight rather than enumerating further work (additional items `not in parse`).

## Relation to the corpus

A **URLLC / finite-blocklength** UAV-MEC entry — the first in the corpus to drop the infinite-blocklength/Shannon assumption, distinguishing it from the SCA/AO single-UAV designs of [[liu-2022-miso-uav-mec-trajectory]] and [[yang-2022-stochastic-uav-mec-lyapunov]] and the PDD min-max-delay scheme [[hu-2019-pdd-uav-mec-offloading]] (with which it shares the min-max-latency objective and BCD/SCA tooling). Co-author **Qingqing Wu** here is affiliated with **Shanghai Jiao Tong University** (`qingqingwu@sjtu.edu.cn`), matching the existing Qingqing Wu entity. Anchors the new [[finite-blocklength-urllc]] concept.

## Raw artifacts

- `raw/sources/Latency_Minimization_for_UAV-Enabled_URLLC-Based_Mobile_Edge_Computing_Systems/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
