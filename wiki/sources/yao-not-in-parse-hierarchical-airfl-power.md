---
type: source
title: "Optimizing Power for Interference-Resilient Hierarchical Over-the-Air Federated Learning"
authors: ["Jianping Yao", "Dashun He", "Jinming Wen", "Yi Fang", "Jie Xu", "Guojun Han"]
year: "not in parse"
url: "not in parse"
venue: "not in parse"
modeling_card: required
tags: [source, hierarchical-over-the-air-federated-learning, over-the-air-computation, power-allocation, amplify-and-forward, inter-cluster-interference]
related:
  - "[[hierarchical-over-the-air-federated-learning]]"
  - "[[over-the-air-computation]]"
  - "[[channel-inversion-power-control]]"
  - "[[jianping-yao]]"
  - "[[jie-xu]]"
  - "[[yi-fang]]"
  - "[[guojun-han]]"
created: 2026-11-02
updated: 2026-11-03
---

# Optimizing Power for Interference-Resilient Hierarchical Over-the-Air Federated Learning

## Citation

Yao, J., He, D., Wen, J., Fang, Y., Xu, J., & Han, G. *Optimizing Power for Interference-Resilient Hierarchical Over-the-Air Federated Learning*. Venue, year, and DOI are not in the parse.

## TL;DR

In a hierarchical over-the-air FL network, devices aggregate gradients to their cluster base stations by AirComp, and the base stations amplify-and-forward the aggregates to a fusion center, while clusters interfere with each other. After bounding the optimality gap, the paper minimizes it over device powers, BS amplification factors, and the denoising factor with a three-phase alternating optimization that has closed-form subproblem solutions.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A fusion center (FC) serves clusters $\mathcal C$, each with a BS and devices $\mathcal K_c$, over $T$ rounds. Devices transmit gradients with power $p_k^{(t)}$ to their BS, which amplifies the received signal $I_c^{(t)}=\sum_{k\in\mathcal K_c}p_k^{(t)}|h_{c,k}^{(t)}|^2+S_{c,j}^{(t)}$ (including inter-cluster interference) by $\alpha_c^{(t)}$ toward the FC, which applies denoising factor $\theta^{(t)}$.

**Problem & objective**: (P1): $\min_{\{\alpha_c^{(t)}\},\{p_k^{(t)}\},\{\theta^{(t)}\}}\Phi(\{p_k^{(t)}\},\{\alpha_c^{(t)}\},\{\theta^{(t)}\})$, the optimality-gap bound.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Device power | $p_k^{(t)}$ | $[0,P_k^{\max}]$ | Gradient transmit power of device $k$ |
| BS amplification | $\alpha_c^{(t)}$ | $\ge0$ | Amplify-and-forward gain at BS $c$ |
| Denoising factor | $\theta^{(t)}$ | $\ge0$ | Receive scaling at the FC |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| (31b) | Peak device power, $0\le p_k^{(t)}\le P_k^{\max}$. |
| (31c) | Average device power, $\frac1T\sum_tp_k^{(t)}\le P_k^{\mathrm{avg}}$. |
| (31d) | Peak BS power, $\alpha_c^{(t)}I_c^{(t)}\le P_c^{\max}$. |
| (31e) | Average BS power, $\frac1T\sum_t\alpha_c^{(t)}I_c^{(t)}\le P_c^{\mathrm{avg}}$. |
| (31f) | $\alpha_c^{(t)}\ge0$, $\theta^{(t)}\ge0$. |

**Algorithm**: Three-phase alternating optimization over device power, BS power, and denoising factor. Each convex subproblem has a closed-form Lagrangian-duality solution with a weighted, regularized channel-inversion structure, and the objective decreases monotonically.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Yao et al. [x] investigated a large-scale hierarchical over-the-air federated learning network comprising a fusion center and multiple clusters, each with a base station and several edge devices. Over-the-air computation is used for gradient aggregation from devices to their base stations and from the base stations to the fusion center, with a two-stage amplify-and-forward relaying mechanism to improve communication efficiency. Because clusters share wireless resources, inter-cluster interference is a major challenge. They first conducted a convergence analysis of the optimality gap and then proposed a power allocation strategy, solved by alternating optimization with closed-form subproblem solutions, that minimizes the gap. On a synthetic ridge-regression task, the method reaches a lower optimality gap and prediction error than per-round MSE minimization, constant power, and a benchmark that ignores inter-cluster interference, which it matches only after about 100 rounds.

## Problem framing

Flat AirComp FL scales poorly over large areas, but adding a BS tier exposes each cluster to interference from neighboring clusters' simultaneous transmissions.

## System model

- Gradients are aggregated twice, at the BS and at the FC.
- Interference from other clusters enters each BS's received signal.

## Method

Convergence analysis gives $\Phi$; alternating closed-form updates minimize it.

## Key findings

- Optimal device and BS powers follow a weighted, regularized channel-inversion form.
- The proposed allocation outperforms baseline power schemes in the reported simulations.

## Limitations / future work

Evaluation uses a synthetic ridge regression task.

## Relation to the corpus

A power-control design for [[hierarchical-over-the-air-federated-learning]] related to [[channel-inversion-power-control]]; the same authors study secure UAV AirComp in [[gong-2025-secure-uav-aircomp]].

## Raw artifacts

- Parse: `raw/sources/Optimizing_Power_for_Interference-Resilient_Hierarchical_Over-the-Air_Federated_Learning/Optimizing_Power_for_Interference-Resilient_Hierarchical_Over-the-Air_Federated_Learning.md`
- Extracted figures are in the same folder; no companion PDF is present.
