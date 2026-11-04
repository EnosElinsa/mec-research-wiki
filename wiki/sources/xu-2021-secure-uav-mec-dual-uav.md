---
type: source
modeling_card: required
title: "Joint Resource and Trajectory Optimization for Security in UAV-Assisted MEC Systems"
authors: ["Yu Xu", "Tiankui Zhang", "Dingcheng Yang", "Yuanwei Liu", "Meixia Tao"]
year: 2021
url: "https://doi.org/10.1109/TCOMM.2020.3025910"
venue: "IEEE Transactions on Communications (IEEE TCOMM)"
tags: [source, uav-mec, physical-layer-security, noma, trajectory-optimization, resource-allocation, secure-computing-capacity]
related:
  - "[[secure-computation-efficiency]]"
  - "[[uav-trajectory-control]]"
  - "[[task-offloading]]"
  - "[[michailidis-2024-secure-ris-uav-mec-iot]]"
  - "[[yuanwei-liu]]"
  - "[[meixia-tao]]"
  - "[[yu-xu]]"
  - "[[dingcheng-yang]]"
  - "[[tiankui-zhang]]"
created: 2026-06-04
updated: 2026-11-03
---

# Joint Resource and Trajectory Optimization for Security in UAV-Assisted MEC Systems

## Citation

Xu, Y., Zhang, T., Yang, D., Liu, Y., & Tao, M. (2021). *Joint Resource and Trajectory Optimization for Security in UAV-Assisted MEC Systems*. **IEEE Transactions on Communications**, 69(1). DOI: 10.1109/TCOMM.2020.3025910. (Received 11 March 2020; accepted 14 September 2020; published 22 September 2020; current version 15 January 2021.)

## TL;DR

Studies a **dual-UAV** MEC security framework: one UAV serves as an aerial MEC server (computes offloaded tasks from ground terminals); the other UAV acts as a **cooperative jammer** to suppress eavesdroppers. Formulates **minimum secure computing capacity maximization** (average achievable secure computing bits per period) problems for both TDMA and NOMA, jointly optimizing communication resources, computation resources, and both UAVs' trajectories. Proposes BCD-based and penalized-BCD algorithms for the two schemes. Claims to be the first work using secure computing capacity as the PLS performance metric in UAV-MEC. Finding: NOMA is superior to TDMA for security.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Ground terminals partially offload tasks to a server UAV under TDMA or NOMA while a second UAV transmits artificial noise toward multiple eavesdroppers. Communication, local and aerial computation, SIC order, and both fixed-altitude trajectories determine secure computing capacity.

**Problem & objective**: Problems (25) for TDMA and (26) for NOMA maximize worst-terminal secure computing capacity, $\max \min_k C_k^{\mathrm{sec}}$, over radio resources, computation resources, and server/jammer trajectories.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Server-UAV trajectory | $\mathbf q_S[n]$ | continuous position | MEC server path |
| Jammer-UAV trajectory | $\mathbf q_J[n]$ | continuous position | Cooperative jammer path |
| Local bits | $l_{loc,k}[n]$ | continuous, nonnegative | Task bits computed locally by terminal $k$ |
| Terminal power/time | $p_k[n],\tau_k[n]$ | continuous, bounded | TDMA or NOMA uplink resources |
| UAV CPU allocation | $f_k[n]$ | continuous, nonnegative | Server computation assigned to terminal $k$ |
| SIC order | $\lambda_{k,l}[n]$ | binary | NOMA decoding-order relation |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| (1) | Both UAVs start and end at prescribed points and obey per-slot speed limits $\lVert\mathbf q_i[n+1]-\mathbf q_i[n]\rVert^2\leq(\delta_tV_i^{\max})^2$ |
| (4) | Terminal transmit power, $0\leq p_k[n]\leq P_k^{\max}$ |
| (5a)-(5b) | TDMA time shares satisfy $\sum_k\tau_k[n]\leq1$ and $0\leq\tau_k[n]\leq1$ |
| (11)-(12) | Local computing within $F_k^{\max}$, and UAV computing of securely offloaded bits within $\tau_k[n]F_s^{\max}$ |
| (13), (22) | Local plus secure offloaded bits reach the common capacity $Q_m$ (TDMA and NOMA forms) |
| (14) | NOMA SIC-order variables $\lambda_{k,l}[n]$ are binary and mutually consistent |
| (20)-(21) | NOMA UAV CPU allocation $\sum_kf_k[n]\leq F^{\max}$ and secure offloaded bits within allocated CPU |
| (25b) | Average terminal energy for local computing and offloading stays within $\bar P_k$ |

**Algorithm**: Split TDMA variables into radio/computation and dual-trajectory blocks → convexify non-convex rate and distance constraints with SCA and SOC forms → alternate BCD updates → for NOMA add decoding-order variables and exact-penalty terms → run penalized BCD until minimum secure computing capacity converges.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Xu et al. [x] studied joint resource and trajectory optimization for secure UAV-assisted mobile edge computing with a server UAV and a cooperative-jamming UAV. They formulated TDMA and NOMA problems that maximize the minimum secure computing capacity across ground terminals through communication, computation, and dual-trajectory decisions. The TDMA solver applies block coordinate descent with successive convex and second-order-cone approximations. The NOMA solver adds SIC-order variables and uses a penalized block-coordinate procedure. Simulations report higher minimum secure computing capacity than the no-power-control and no-local-computing benchmarks, approaching an upper bound with unconstrained UAV speed as the period grows; the paper's double-semicycle flight beats straight flight, and NOMA outperforms TDMA.

## Problem framing

UAV-MEC's LoS channels between UAV and ground are also LoS to potential eavesdroppers — a fundamental security vulnerability. A cooperative jammer UAV transmits noise toward eavesdroppers while the server UAV handles computation, exploiting trajectory design to keep the jamming effective and the serving link strong. The secure computing capacity metric captures both the computation benefit (bits processed) and the secrecy benefit (capacity minus eavesdropper capacity) jointly.

## System model

- **K ground terminal devices (TDs)** with partial offloading; **multiple eavesdroppers** on the ground.
- **Server UAV:** collects and computes offloaded task bits from TDs via uplink (TDMA or NOMA).
- **Jammer UAV:** transmits artificial noise to degrade eavesdroppers' SINR.
- **Secure computing capacity:** average achievable secure computing bits = f(server UAV channel to TDs, jammer UAV channel to eavesdroppers, compute resource allocation, trajectory).
- **TDMA scheme:** BCD-based algorithm (SCA + SOC for non-convex constraints).
- **NOMA scheme:** P-BCD algorithm (additional binary constraints for SIC decoding order).
- **Objective:** maximize min secure computing capacity over all TDs.

## Key findings

- NOMA scheme achieves **higher minimum secure computing capacity** than TDMA (parse contribution bullets + Section V results).
- Partial offloading (vs. binary or full offloading) achieves the largest objective values (parse results discussion).
- Proposed BCD/P-BCD algorithms improve security performance over benchmarks (static UAV, no jammer, equal resource allocation) in simulations (parse abstract + Section V).
- Trajectory co-design of both UAVs (server + jammer) is essential — fixed-trajectory or single-UAV baselines perform significantly worse.

## Limitations / future work

Parse does not provide explicit numerical gain figures; references simulation figures. Requires two UAVs (hardware complexity + coordination overhead). Eavesdropper channel knowledge assumed at the server UAV for SIC in NOMA scheme.

## Relation to the corpus

Provides the **secure computing capacity** metric definition for UAV-MEC PLS — complementing [[michailidis-2024-secure-ris-uav-mec-iot]] (secure computation efficiency with RIS) and [[benaya-2025-aerial-isac-haps]] (HAPS-based PLS). The dual-UAV architecture (server + jammer) is distinct from single-UAV MEC papers in the corpus.

## Raw artifacts

- Parse: `raw/sources/Joint_Resource_and_Trajectory_Optimization_for_Security_in_UAV-Assisted_MEC_Systems/Joint_Resource_and_Trajectory_Optimization_for_Security_in_UAV-Assisted_MEC_Systems.md`
- Origin PDF: `raw/sources/Joint_Resource_and_Trajectory_Optimization_for_Security_in_UAV-Assisted_MEC_Systems/Joint_Resource_and_Trajectory_Optimization_for_Security_in_UAV-Assisted_MEC_Systems.pdf`
- Figures: `raw/sources/Joint_Resource_and_Trajectory_Optimization_for_Security_in_UAV-Assisted_MEC_Systems/images/`
