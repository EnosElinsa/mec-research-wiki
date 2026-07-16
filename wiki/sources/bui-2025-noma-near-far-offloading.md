---
type: source
title: "Task Offloading Optimization for UAV-Aided NOMA Networks With Coexistence of Near-Field and Far-Field Communications"
authors: ["Tinh T. Bui", "Thinh Quang Do", "Dang Van Huynh", "Tan Do-Duy", "Long D. Nguyen", "Tuan-Vu Cao", "Vishal Sharma", "Trung Q. Duong"]
year: 2025
url: "https://doi.org/10.1109/TGCN.2024.3417697"
venue: "IEEE Transactions on Green Communications and Networking (IEEE TGCN), vol. 9, no. 1, pp. 327-337, Mar. 2025"
modeling_card: required
tags: [source, noma, near-field-communications, task-offloading, mobile-edge-computing, multi-uav-assisted-mec]
related:
  - "[[noma]]"
  - "[[near-field-communications]]"
  - "[[task-offloading]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[mobile-edge-computing]]"
  - "[[mixed-integer-nonlinear-programming]]"
  - "[[chen-2026-qos-noma-multiuav]]"
  - "[[mohammadi-2026-star-ris-uav-mec-noma]]"
created: 2026-07-07
updated: 2026-07-16
---

# Task Offloading Optimization for UAV-Aided NOMA Networks With Coexistence of Near-Field and Far-Field Communications

## Citation

Bui, T. T., Do, T. Q., Huynh, D. V., Do-Duy, T., Nguyen, L. D., Cao, T.-V., Sharma, V., & Duong, T. Q. (2025). *Task Offloading Optimization for UAV-Aided NOMA Networks With Coexistence of Near-Field and Far-Field Communications*. **IEEE Transactions on Green Communications and Networking**, 9(1), 327-337. DOI: 10.1109/TGCN.2024.3417697. DOI evidence appears in the local parse and was cross-checked against title-matched DOI metadata.

## TL;DR

Studies UAV-aided NOMA MEC when near-field and far-field users coexist around UAV-mounted large antenna arrays. It jointly optimizes user transmit powers, user association/offloading choices, and UAV-MEC computing allocation to minimize total latency under power, association, rate, served-user-count, delay, and compute-capacity constraints.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Multiple fixed UAVs act as flying MEC servers with $N$-antenna uniform linear arrays and nonoverlapping UE clusters. Uplink NOMA uses MRC and SIC, while UEs inside the Rayleigh distance use spherical-wave near-field channels and the remaining UEs use plane-wave far-field channels; each UE either computes locally or offloads to its cluster UAV.

**Problem & objective**: Problem (23) is a nonconvex nonlinear integer program that minimizes total task latency, $\min_{\mathbf p,\boldsymbol\pi,\boldsymbol\xi}\sum_{k\in\mathcal K^{NF}}T_k^{NF}(\mathbf p,\boldsymbol\pi,\boldsymbol\xi)+\sum_{k\in\mathcal K^{FF}}T_k^{FF}(\mathbf p,\boldsymbol\pi,\boldsymbol\xi)$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UE transmit power | $p_k$ | continuous, $0\leq p_k\leq P_k^{\max}$ | Uplink power used by UE $k$ |
| UAV association and offloading | $\pi_{k,u}$ | binary, $\{0,1\}$ | Whether UE $k$ offloads its task to UAV $u$ |
| UAV-MEC computing allocation | $\zeta_{k,u}$ | continuous, $\zeta_{k,u}\geq 0$ | CPU capacity that UAV $u$ assigns to UE $k$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| 23b | UE power is bounded, $p_k\leq P_k^{\max}$ |
| 23c | Association is binary, $\pi_{k,u}\in\{0,1\}$ |
| 23d | UAV $u$ serves at most $\Pi^{\max}$ UEs, $\sum_{k\in\mathcal K_u}\pi_{k,u}\leq\Pi^{\max}$ |
| 23e | Each task meets the latency limit, $T_k(\mathbf p,\boldsymbol\pi,\zeta_{k,u})\leq T^{\max}$ |
| 23f | Each selected uplink meets its rate requirement, $R_k(\mathbf p,\boldsymbol\pi)\geq\pi_{k,u}R_{\min}^{ul}$ |
| 23g | Each UAV respects its compute budget, $\sum_{k\in\mathcal K_u}\pi_{k,u}\zeta_{k,u}\leq\zeta^{\max}$ |

**Algorithm**: The iterative block-coordinate procedure first relaxes and convexifies the association subproblem with logarithmic lower bounds, retains the largest feasible $\pi_{k,u}$ values, then convexifies the power subproblem and solves the computing-allocation subproblem with CVX. The three blocks repeat until the latency change is below $\varepsilon=0.01$ or the iteration count exceeds $I^{\max}=20$.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Bui et al. [x] studied task offloading in a multi-UAV NOMA MEC network where near-field spherical-wave and far-field plane-wave users coexist around large antenna arrays. They formulated a nonlinear mixed-integer latency-minimization problem over UE transmit power, binary UAV association and offloading, and UAV-MEC computing capacity, subject to power, served-user-count, latency, uplink-rate, and compute-capacity constraints. Their iterative block-coordinate method relaxes and convexifies association, power, and computing subproblems, then selects the largest association values within each UAV's capacity and solves the convex stages with CVX. Simulations report the lowest total latency across the tested task sizes and network sizes, with RandomSelection 15.24% to 18.68% higher and EqualPower 5.04% to 7.66% higher over the task-size sweep, while NOMA also outperforms OFDM.

## Problem

Most UAV-MEC NOMA work assumes far-field propagation. With large arrays and high frequencies, some users can fall inside the Rayleigh distance, where spherical-wave near-field channels matter. The paper asks how task offloading should be optimized when near-field and far-field users coexist and share NOMA uplink resources.

## System model

Multiple UAVs act as flying MEC servers with N-antenna uniform linear arrays. Users are categorized as near-field or far-field relative to the Rayleigh distance. Near-field channels use spherical-wave geometry over antenna positions; far-field channels use a plane-wave angle-of-arrival model. UAV receivers use MRC and NOMA SIC. Each user either computes locally or offloads to a UAV; total latency includes local computing, uplink transmission, and UAV computation, while downlink result return is ignored in the parse.

## Method

The latency-minimization problem is nonconvex because of binary association/offloading decisions, NOMA interference, and coupled communication/computation variables. The paper applies an alternating/BCD iterative strategy:

- offloading decisions are relaxed and lower-bounded through logarithmic inequalities plus auxiliary variables, then solved as a convex problem;
- the largest relaxed association values are selected subject to UAV capacity;
- transmit powers are optimized through a similar convex transformation;
- UAV computing-capacity allocation is convex and solved with CVX.

## Key findings

- In the reported 600 m by 600 m simulation with four UAVs at 40 m, 128 antennas, 28 GHz carrier frequency, and 86.45 m Rayleigh distance, the power-allocation subproblem converges in 3 iterations and edge-selection in 5 iterations.
- The proposed algorithm has the lowest total latency across task sizes from 0.3 MB to 0.9 MB. The parse reports RandomSelection as 15.24%-18.68% higher and EqualPower as 5.04%-7.66% higher.
- NOMA outperforms OFDM in the reported comparisons.
- As the user count grows from 24 to 56, the proposed method remains the lowest-latency method.
- Far-field users are offloaded more often than near-field users in the reported setting; the parse attributes this to the SIC/interference behavior in the NOMA system.
- Increasing UAV compute capacity reduces latency with diminishing returns, and stronger local UE computing narrows the benefit of offloading.

## Limitations / future work

The conclusion states that future work should jointly consider UAV deployment and resource allocation because moving UAVs changes near-/far-field regions and can exploit LoS, energy, and spectrum more efficiently.

## Relation to the corpus

This source bridges [[noma]], [[near-field-communications]], and [[task-offloading]]. It complements [[chen-2026-qos-noma-multiuav]], which focuses on task priorities and improved SAC for NOMA multi-UAV offloading, and [[mohammadi-2026-star-ris-uav-mec-noma]], which adds STAR-RIS energy minimization. Here the distinguishing feature is explicit near-field/far-field coexistence in UAV-aided NOMA MEC.

## Raw artifacts

- `raw/sources/Task Offloading Optimization for UAV-Aided NOMA Networks With Coexistence of Near-Field and Far-Field Communications/Task Offloading Optimization for UAV-Aided NOMA Networks With Coexistence of Near-Field and Far-Field Communications.md`
- Original PDF and extracted figures (`images/`) in the same folder.
