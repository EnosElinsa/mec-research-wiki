---
type: source
title: "User Association and Communication-Computation Co-Design for Wireless Control Networks"
authors: ["Zhilin Liu", "Yiyang Li", "Huijun Xing", "Ye Zhang", "Jie Xu", "Shuguang Cui"]
year: "not in parse"
url: "not in parse"
venue: "not in parse"
modeling_card: required
tags: [source, wireless-networked-control, user-association, massive-mimo, hrllc, edge-computing, successive-convex-approximation]
related:
  - "[[wireless-networked-control-system]]"
  - "[[device-association]]"
  - "[[finite-blocklength-urllc]]"
  - "[[li-2025-wireless-control-hrllc-scheduling]]"
  - "[[yiyang-li]]"
  - "[[jie-xu]]"
  - "[[shuguang-cui]]"
created: 2026-11-02
updated: 2026-11-03
---

# User Association and Communication-Computation Co-Design for Wireless Control Networks

## Citation

Liu, Z., Li, Y., Xing, H., Zhang, Y., Xu, J., & Cui, S. *User Association and Communication-Computation Co-Design for Wireless Control Networks*. Venue, year, and DOI are not in the parse.

## TL;DR

Several massive-MIMO base stations jointly close the control loops of many plants: each sensor offloads to an associated BS for MEC processing, and the BS returns commands. With BSs taking turns in TDMA slots, the paper minimizes the network's sampling period under control stability and short-packet reliability by optimizing BS-sensor/actuator association, powers, and slot times with AO and SCA.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: $M$ BSs with massive MIMO and MEC servers of capacity $F_m$ serve $K$ subsystems. BSs collect uplink data and broadcast downlink commands in orthogonal TDMA slots, and each BS serves its associated subsystems on the same time-frequency resources with inter-user interference. HRLLC error probabilities follow short-packet formulas.

**Problem & objective**: (P1): $\min_{p,t,\alpha}T$, the sampling period of the whole network.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Association | $\alpha_{m,k}$ | binary | Subsystem $k$ is associated with BS $m$ |
| Powers | $\overline p_{m,k}$, $\underline p_{m,k}$ | nonnegative | Uplink and downlink transmit power |
| Slot times | $\overline t_m$, $\underline t_m$, $\hat t$ | positive | Uplink, downlink, and computation durations |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| (16a)–(16b) | Reliability: $\overline\varepsilon_k,\underline\varepsilon_k\le\varepsilon_{\mathrm{th}}$ |
| (16c) | Stability: $\boldsymbol\Phi_kT^2+\boldsymbol\Upsilon_kT+(\eta_k-1)\mathbf Q_k\succeq\mathbf0$ |
| (16d) | Computation at BS $m$ finishes in its available window: $F_m(\sum_{i>m}\overline t_i+\hat t+\sum_{i<m}\underline t_i)\ge\sum_k\alpha_{m,k}S_k\hat\lambda_k$ |
| (16e) | Period: $\sum_m\overline t_m+\hat t+\sum_m\underline t_m=T$ |
| (16f)–(16g) | Binary association, each subsystem to exactly one BS: $\sum_m\alpha_{m,k}=1$ |
| (16h)–(16i) | Power limits: $\alpha_{m,k}\overline p_{m,k}\le\overline P_k$; per-BS downlink power $\sum_k\alpha_{m,k}\underline p_{m,k}\le\underline P_m$ |

**Algorithm**: Alternating optimization over association, powers, and times, with SCA for the nonconvex reliability and stability terms.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Liu et al. [x] studied a wireless networked control system in which multiple base stations cooperatively coordinate the wireless control of subsystems, each consisting of a plant, a sensor, and an actuator. Each sensor offloads its sensing data to an associated base station, which employs mobile edge computing to process the data and sends command signals back to the actuator. Using a time-division multiple access protocol among base stations and massive MIMO within each base station, they jointly designed base station-sensor/actuator association and communication and computation resource allocation to minimize the closed-loop control latency while ensuring control stability. The design accounts for transmission uncertainty from hyper-reliable and low-latency communications, inter-user interference, and resource constraints, and is solved with alternating optimization and successive convex approximation. Numerical results show that the joint association and resource allocation design achieves lower control latency than association-only, resource-allocation-only, and FDMA benchmark designs.

## Problem framing

With many control loops, a single BS becomes a bottleneck. Spreading loops across BSs creates an association problem coupled with each BS's slot length and computing load.

## System model

- Massive MIMO lets each BS serve its associated subsystems simultaneously, with residual inter-user interference.
- The network period is the sum of all BSs' uplink and downlink slots plus computation time.

## Method

AO with SCA over the binary association and continuous resources.

## Key findings

- Joint association and resource design yields lower latency and better stability than benchmarks.

## Limitations / future work

Not stated beyond the presented design.

## Relation to the corpus

Extends the single-BS [[wireless-networked-control-system]] design in [[li-2025-wireless-control-hrllc-scheduling]] to multiple BSs with [[device-association]].

## Raw artifacts

- Parse: `raw/sources/User_Association_and_Communication-Computation_Co-Design_for_Wireless_Control_Networks/User_Association_and_Communication-Computation_Co-Design_for_Wireless_Control_Networks.md`
- Extracted figures are in the same folder; no companion PDF is present.
