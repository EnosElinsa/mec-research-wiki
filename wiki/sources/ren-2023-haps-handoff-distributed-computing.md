---
type: source
title: "Handoff-Aware Distributed Computing in High Altitude Platform Station (HAPS)-Assisted Vehicular Networks"
authors: ["Qiqi Ren", "Omid Abbasi", "Gunes Karabulut Kurt", "Halim Yanikomeroglu", "Jian Chen"]
year: 2023
url: "https://doi.org/10.1109/TWC.2023.3266344"
venue: "IEEE Transactions on Wireless Communications, 22(12)"
modeling_card: required
tags: [source, haps, vehicular-mec, task-offloading, handoff, successive-convex-approximation]
related:
  - "[[high-altitude-platform-station]]"
  - "[[vehicular-mec]]"
  - "[[task-offloading]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[halim-yanikomeroglu]]"
created: 2026-08-27
updated: 2026-08-27
---

# Handoff-Aware Distributed Computing in High Altitude Platform Station (HAPS)-Assisted Vehicular Networks

## Citation

Ren, Q., Abbasi, O., Kurt, G. K., Yanikomeroglu, H., & Chen, J. (2023). *Handoff-Aware Distributed Computing in High Altitude Platform Station (HAPS)-Assisted Vehicular Networks*. **IEEE Transactions on Wireless Communications, 22**(12), 8814-8827. DOI: 10.1109/TWC.2023.3266344.

## TL;DR

Splittable vehicle tasks execute in parallel locally, at a roadside unit, and at a 20-km HAPS. The formulation minimizes total completion delay while requiring the RSU portion to finish before handoff; successive convex approximation optimizes split ratios, power, bandwidth, and CPU shares.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Vehicles move along a one-way road covered by RSUs and a HAPS. Each task is divided among local execution, the associated RSU, and the HAPS so that the RSU portion meets the next handoff deadline.

**Problem & objective**: Minimize aggregate parallel completion delay, $\min\sum_n\max\{T_n^L,T_n^R,T_n^H\}$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
| --- | --- | --- | --- |
| Task split | $x_n^R,x_n^H$ | continuous, $[0,1]$ | Fractions sent to RSU and HAPS |
| Transmit power | $p_n^R,p_n^H$ | continuous | Power shares on RSU/HAPS links |
| Bandwidth | $b_n^R,b_n^H$ | continuous | Orthogonal-link bandwidth ratios |
| CPU share | $f_n^R,f_n^H$ | continuous | RSU/HAPS compute allocation |

**Constraints**:

| ID | Meaning and key expression |
| --- | --- |
| Split | $x_n^R+x_n^H\leq1$; the remainder executes locally. |
| Handoff | RSU completion delay satisfies $T_n^R\leq T_{\mathrm{handoff}}$. |
| Radio | Bandwidth and per-vehicle power shares remain within their budgets. |
| Compute | RSU and HAPS CPU shares sum within each server's capacity. |

**Algorithm**: Replace coupled variables to convexify the subproblems, then alternate successive-convex-approximation updates for bandwidth, power, task splits, and CPU allocation until convergence.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Ren et al. [x] studied distributed task execution across vehicles, roadside units, and a HAPS when vehicles move between RSU coverage areas. They jointly optimized task split ratios, transmit power, bandwidth, and compute shares to minimize parallel completion delay while forcing the RSU portion to finish before handoff. Variable transformations and successive convex approximation solve the resulting nonconvex formulation. Simulations report that the HAPS tier absorbs more task load during handoff and keeps delay growth below the no-HAPS benchmark in the tested road setting. HAPS hovering and computing energy are omitted from the objective.

## Problem and system model

Each vehicle splits one task among local CPU, its associated RSU, and the HAPS. The RSU and HAPS links have separate fading and bandwidth models, and RSU execution must complete before the vehicle leaves coverage.

## Method

The paper derives local, RSU, and HAPS communication/computation delay expressions, imposes bandwidth, power, CPU, and handoff constraints, and solves the nonconvex problem with alternating SCA updates.

## Key findings

- The proposed three-tier system outperforms configurations without the RSU or without the HAPS in the reported simulations.
- Handoff delay increases by less than 10 ms for the HAPS-assisted design versus roughly 150 ms without HAPS.
- During handoff, the RSU task fraction falls to about 3% while the HAPS fraction rises to roughly 62% to 78% in the reported cases.

## Limitations / future work

HAPS hovering and computing energy are omitted; including them may reduce the HAPS advantage and increase delay.

## Relation to the corpus

This source connects [[high-altitude-platform-station]] and [[vehicular-mec]] with handoff-aware parallel offloading and complements UAV/HAPS offloading studies.

## Raw artifacts

- Parse: `raw/sources/Handoff-Aware_Distributed_Computing_in_High_Altitude_Platform_Station_HAPSAssisted_Vehicular_Networks/Handoff-Aware_Distributed_Computing_in_High_Altitude_Platform_Station_HAPSAssisted_Vehicular_Networks.md`
- Origin PDF and figures are in the same folder.
