---
type: source
title: "Joint Computation and Communication Design for UAV-Assisted Mobile Edge Computing in IoT"
authors: ["Tiankui Zhang", "Yu Xu", "Jonathan Loo", "Dingcheng Yang", "Lin Xiao"]
year: 2019
url: "https://doi.org/10.1109/TII.2019.2948406"
venue: "IEEE Transactions on Industrial Informatics (IEEE TII)"
tags: [source, uav-mec, computation-offloading, trajectory-optimization, energy-minimization, sca, iot]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[uav-trajectory-control]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[binary-vs-partial-offloading]]"
  - "[[energy-latency-tradeoff]]"
  - "[[yu-2020-uav-ec-collaborative-offloading]]"
  - "[[liu-2022-miso-uav-mec-trajectory]]"
  - "[[lin-xiao]]"
  - "[[yu-xu]]"
  - "[[dingcheng-yang]]"
  - "[[tiankui-zhang]]"
created: 2026-05-29
updated: 2026-07-16
modeling_card: required
---

# Joint Computation and Communication Design for UAV-Assisted Mobile Edge Computing in IoT

## Citation

Zhang, T., Xu, Y., Loo, J., Yang, D., & Xiao, L. (2019). *Joint Computation and Communication Design for UAV-Assisted Mobile Edge Computing in IoT*. **IEEE Transactions on Industrial Informatics**. DOI: 10.1109/TII.2019.2948406.

## TL;DR

A single-UAV-with-MEC-server system serving IoT terminal devices (TDs) over a finite period. Each TD has three options per slot: compute locally, partially offload to the UAV, or offload to an access point **via UAV relaying**. The paper minimizes total energy (communication + computation + UAV flight) by jointly optimizing bit allocation, time-slot scheduling, power allocation, and UAV trajectory, solving the non-convex problem in two parts via **Lagrangian duality** and **successive convex approximation (SCA)**.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: One fixed-altitude rotary-wing UAV with an MEC server serves multiple single-antenna IoT terminal devices and can decode-and-forward their tasks to an MEC-enabled access point. OFDMA assigns one equal-bandwidth subcarrier to each terminal, while terminal-to-UAV and UAV-to-AP links use free-space LoS path loss.

**Problem & objective**: Nonconvex problem (P1) minimizes total communication, local and UAV computation, and weighted flight energy, $\min_{\mathbf L,\boldsymbol\tau,\mathbf P,\mathbf Q}E_{\mathrm{comm}}+E_{\mathrm{comp}}+wE_{\mathrm{fly}}$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Computation-bit allocation | $l_{u,k}[n],l_{h,k}[n],l_{a,k}[n]$ | continuous, nonnegative | Bits computed locally, at the UAV, or at the AP via relaying |
| Subslot fractions | $\tau_{k,m}[n]$ | continuous, $[0,1]$ | Time assigned to the two uplinks and the UAV-to-AP forwarding phase |
| Transmit powers | $p_{k,m}[n]$ | continuous, bounded | Terminal or UAV power in communication phase $m$ |
| UAV trajectory and velocity | $\mathbf q[n],\mathbf v[n]$ | continuous | Horizontal location and velocity of the UAV |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| 2 | Per-slot task demand is met, $l_{u,k}[n]+l_{h,k}[n]+l_{a,k}[n]\geq L_{k,n}^{\min}$ |
| 5-6 | Communication phases satisfy $\sum_{m=1}^{3}\tau_{k,m}[n]\leq1$ and $0\leq\tau_{k,m}[n]\leq1$ |
| 10-11 | UAV computing obeys cumulative causality, and relayed bits do not exceed either hop's transferable bits |
| 13-14 | Local and UAV CPU-cycle demands stay within their maximum frequencies |
| 18a-c | The UAV starts and ends at prescribed points and obeys $\|\mathbf q[n+1]-\mathbf q[n]\|\leq\delta_tV_{\max}$ |
| 22a-c | Terminal and UAV transmit powers stay within their instantaneous limits |

**Algorithm**: Fix the UAV trajectory, introduce time-energy perspective variables, and solve the resulting convex bit, time, and power problem through Lagrangian duality; then fix those variables and apply successive convex approximation to the trajectory and flight-energy block; alternate both parts until the total-energy objective converges.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zhang et al. [x] studied joint computation and communication design for UAV-assisted mobile edge computing in IoT. Each terminal can compute locally, offload task bits to the UAV for computing, or offload them to an access point through UAV relaying. They formulated a nonconvex total-energy minimization problem over computation-bit allocation, time-slot scheduling, power allocation, and UAV trajectory. The proposed iterative method solves the fixed-trajectory resource-allocation block by Lagrangian duality and the trajectory block by successive convex approximation. Numerical results report convergence within approximately fifteen iterations and lower energy consumption than the evaluated straight-flight, no-AP, relay-only, and no-UAV-cooperation designs.

## Problem framing

Latency-critical IoT tasks exceed TD compute/battery budgets. A UAV-mounted MEC server (and the UAV as relay to an AP) extends compute coverage, but the joint bit/time/power/trajectory design is non-convex.

## System model

- **Actors.** One UAV (MEC server + relay), multiple IoT TDs, an access point.
- **Per-TD options.** Local compute; partial offload to UAV; offload to AP via UAV relay ([[binary-vs-partial-offloading]] — partial).
- **Objective.** Minimize sum of communication-related, computation-related, and UAV flight energy.

## Method

- Decompose into two sub-problems solved by **Lagrangian duality** and **SCA**, combined into an iterative algorithm guaranteed to converge within a dozen iterations ([[alternating-optimization-sdr-sca]]).

## Key findings

- Numerical results validate the algorithm and show its superiority over benchmark designs (qualitative; specific energy curves in the paper).

## Limitations / future work

Single-UAV; the parse does not enumerate explicit future work beyond the established design.

## Relation to the corpus

An early, **optimization-based single-UAV MEC** entry that anchors the classic "joint trajectory + offloading + resource" formulation later revisited with collaboration ([[yu-2020-uav-ec-collaborative-offloading]]), MISO beamforming ([[liu-2022-miso-uav-mec-trajectory]]), and DRL ([[zhang-2024-uav-task-offloading-ddpg]]). Reinforces [[alternating-optimization-sdr-sca]] and [[uav-trajectory-control]].

## Raw artifacts

- `raw/sources/Joint_Computation_and_Communication_Design_for_UAV-Assisted_Mobile_Edge_Computing_in_IoT/full.md`
- Original PDF and extracted figures in the same folder.
