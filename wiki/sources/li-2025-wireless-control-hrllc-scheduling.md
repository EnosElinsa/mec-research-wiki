---
type: source
title: "Joint Task Scheduling and Communication-Computation Optimization for Wireless Networked Control With HRLLC"
authors: ["Yiyang Li", "Xianxin Song", "Zhiqing Wei", "Zhiyong Feng", "Jie Xu"]
year: 2025
url: "https://doi.org/10.1109/TWC.2025.3598004"
venue: "IEEE Transactions on Wireless Communications"
modeling_card: required
tags: [source, wireless-networked-control, hrllc, short-packet-communication, task-scheduling, edge-computing, flow-shop-scheduling]
related:
  - "[[wireless-networked-control-system]]"
  - "[[finite-blocklength-urllc]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[liu-not-in-parse-wireless-control-association]]"
  - "[[yiyang-li]]"
  - "[[jie-xu]]"
  - "[[zhiyong-feng]]"
created: 2026-11-02
updated: 2026-11-03
---

# Joint Task Scheduling and Communication-Computation Optimization for Wireless Networked Control With HRLLC

## Citation

Li, Y., Song, X., Wei, Z., Feng, Z., & Xu, J. (2025). *Joint Task Scheduling and Communication-Computation Optimization for Wireless Networked Control With HRLLC*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2025.3598004. A conference version considered fixed task scheduling.

## TL;DR

A base station closes the control loops of several plants: it collects sensor states, computes commands at the edge, and sends them to actuators, all over short-packet hyper-reliable low-latency links. Under a TDMA protocol, the paper minimizes the closed-loop sampling period subject to control stability by choosing the order of subsystems, powers, slot lengths, and CPU allocation, using AO with SCA plus exhaustive or flow-shop scheduling.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: $J$ subsystems, each with a plant, sensor, and actuator, share one BS with an edge server. In each period $T$, subsystem $\pi_j$ uploads its state in time $\overline t_{\pi_j}$ with power $\overline p_{\pi_j}$, the server computes with frequency $f_{\pi_j,k}$, and the BS sends commands in time $\underline t_{\pi_j}$ with power $\underline p_{\pi_j}$. Short-packet error probabilities $\overline\varepsilon$ and $\underline\varepsilon$ follow finite-blocklength rate formulas.

**Problem & objective**: (P1): $\min_{\boldsymbol\pi,\mathbf p,\mathbf t,\mathbf f}T$, the closed-loop control period.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Task schedule | $\boldsymbol\pi$ | permutation of subsystems | Order in which subsystems are served |
| Powers | $\overline p_{\pi_j}$, $\underline p_{\pi_j}$ | $[0,P_{\max}]$ | Uplink and downlink transmit power |
| Slot lengths | $\overline t_{\pi_j}$, $\underline t_{\pi_j}$, $\hat t$, $T$ | positive | Uplink, downlink, computation, and period durations |
| CPU allocation | $f_{\pi_j,k}$ | positive | Edge frequency given to each task over time |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| (21b)–(21c) | Power limits: $0\le\overline p_{\pi_j},\underline p_{\pi_j}\le P_{\max}$ |
| (21d)–(21e) | Reliability: $\overline\varepsilon_{\pi_j},\underline\varepsilon_{\pi_j}\le\varepsilon_{\mathrm{th}}$ |
| (21f) | Control stability: $\mathbf P_{\pi_j}T^2+\mathbf M_{\pi_j}T+(\eta_{\pi_j}-1)\mathbf Q_{\pi_j}\succeq\mathbf0$ |
| (21g) | Computation completion: allocated CPU cycles over the available time cover each task |
| (21h) | Edge CPU capacity per stage: $\sum_jf_{\pi_j,i-j}\le F_{\max},\ \forall i\in\{2,\dots,2J\}$ |
| (21i) | Period definition: $T=\sum_j\bar t_{\pi_j}+\hat t+\sum_j\underline t_{\pi_j}$ |
| (21j) | $\boldsymbol\pi$ is a permutation: $\pi_j\in\mathcal J$, $\pi_j\ne\pi_i$ for $j\ne i$ |

**Algorithm**: For a given schedule, optimize powers, times, and CPU frequencies by alternating optimization and SCA. Choose the schedule by exhaustive search or by a low-complexity flow-shop scheduling heuristic.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Li et al. [x] studied a wireless control system at the network edge in which a base station coordinates the closed-loop control of multiple subsystems, each consisting of a plant, a sensor, and an actuator. The base station collects state information from the sensors, processes it via edge computing, and sends command signals back to the actuators, using hyper-reliable and low-latency communications based on short-packet rate formulas. Under a time-division multiple access protocol for coordinating sensing, communication, and computation, they jointly optimized task scheduling and communication and computation resource allocation to minimize the closed-loop control latency while ensuring the stability of all control subsystems. The resulting non-convex combinatorial problem is handled by optimizing resource allocation for given scheduling through alternating optimization and successive convex approximation, and then designing the schedule by exhaustive search or low-complexity flow-shop scheduling. Numerical results show that the joint design with exhaustive search scheduling achieves lower closed-loop latency than communication-only, computation-only, equal-allocation, and fixed-schedule benchmarks, and the flow-shop design comes close to exhaustive search.

## Problem framing

Control stability depends on how often each loop closes, and the period depends on how communication and edge computation are shared and ordered among loops.

## System model

- TDMA coordinates uplink sensing, edge computation, and downlink command transmission.
- Stability conditions take a matrix inequality form in $T$.

## Method

Nested design: inner continuous optimization, outer schedule search.

## Key findings

- Joint scheduling and resource allocation reduce closed-loop latency compared with benchmarks lacking joint optimization.
- Flow-shop scheduling offers a lower-complexity alternative to exhaustive search.

## Limitations / future work

The model uses a single BS and edge server.

## Relation to the corpus

Defines a single-BS [[wireless-networked-control-system]] design with [[finite-blocklength-urllc]] links; the multi-BS association counterpart is [[liu-not-in-parse-wireless-control-association]].

## Raw artifacts

- Parse: `raw/sources/Joint_Task_Scheduling_and_Communication-Computation_Optimization_for_Wireless_Networked_Control_With_HRLLC/Joint_Task_Scheduling_and_Communication-Computation_Optimization_for_Wireless_Networked_Control_With_HRLLC.md`
- Extracted figures are in the same folder; no companion PDF is present.
