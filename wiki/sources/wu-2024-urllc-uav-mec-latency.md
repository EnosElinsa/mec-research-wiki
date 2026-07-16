---
type: source
modeling_card: required
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
updated: 2026-07-16
---

# Latency Minimization for UAV-Enabled URLLC-Based Mobile Edge Computing Systems

## Citation

Wu, Q., Cui, M., Zhang, G., Wang, F., Wu, Q., & Chu, X. (2024). *Latency Minimization for UAV-Enabled URLLC-Based Mobile Edge Computing Systems*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2023.3307154. (Date of publication 28 Aug 2023; date of current version 11 Apr 2024.)

## TL;DR

A UAV-enabled MEC system where K ground devices offload **mission-critical, latency-sensitive** tasks to a UAV-carried MEC server over **URLLC (finite-blocklength)** links and compute the rest locally. It minimizes the **maximum computation latency** among all devices by jointly optimizing devices'/UAV's computing times and CPU frequencies, devices' offloading bandwidths, and the **3D UAV location**. The non-convex problem is decomposed (via **BCD**) into three subproblems — UAV horizontal location, UAV altitude, and bandwidth+CPU-frequency — solved alternately with **SCA**; the bandwidth/frequency subproblem gets a **semi-closed-form** solution.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: $K$ ground devices partially offload mission-critical tasks to one UAV MEC server over finite-blocklength URLLC links and compute the remaining bits locally. An angle-dependent Rician channel couples three-dimensional UAV placement, bandwidth, decoding reliability, and computation time.

**Problem & objective**: A non-convex min-max latency problem minimizes the slowest device, $\min \max_k T_k$, over UAV location, offloading bandwidth, device and UAV CPU frequencies, and computation times.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV horizontal location | $\mathbf q$ | continuous 2-D position | Ground projection of the UAV MEC server |
| UAV altitude | $H$ | continuous, bounded | Server altitude and elevation angle |
| Offloading bandwidth | $b_k$ | continuous, nonnegative | URLLC bandwidth allocated to device $k$ |
| CPU frequencies | $f_k,f_k^{\mathrm U}$ | continuous, bounded | Local and UAV computing rates for device $k$ |
| Computing time | $t_k$ | continuous, nonnegative | End-to-end computation latency variable |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Local and offloaded computation together complete each task |
| C2 | Finite-blocklength offloading meets the target decoding-error probability |
| C3 | Bandwidth allocations satisfy $\sum_k b_k\le B$ |
| C4 | Device and UAV CPU frequencies stay within their limits |
| C5 | UAV horizontal position and altitude remain in the feasible deployment region |

**Algorithm**: Approximate the finite-blocklength rate by a tractable logarithmic form → update horizontal UAV location with SCA → update altitude with SCA → transform bandwidth and CPU allocation into a max-min completed-task-ratio problem → solve it with the two-layer semi-closed-form routine → alternate the BCD blocks.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Wu et al. [x] studied latency minimization for UAV-enabled URLLC mobile edge computing with partial offloading and finite-blocklength links. They formulated a non-convex min-max problem over three-dimensional UAV placement, device bandwidth, computing times, and device and UAV CPU frequencies. The channel model uses angle-dependent Rician fading, and the finite-blocklength rate is approximated by a tractable logarithmic expression. Their block-coordinate method alternates SCA updates of horizontal position and altitude with a two-layer semi-closed-form bandwidth and frequency solver. Simulations report lower maximum computation latency than the evaluated location, resource-allocation, and Shannon-rate baselines.

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
