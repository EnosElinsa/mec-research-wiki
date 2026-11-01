---
type: source
title: "Integrated Sensing, Communication, and Computation for Over-the-Air Federated Edge Learning"
authors: ["Dingzhu Wen", "Sijing Xie", "Xiaowen Cao", "Yuanhao Cui", "Jie Xu", "Yuanming Shi", "Shuguang Cui"]
year: 2025
url: "https://doi.org/10.1109/TWC.2025.3598997"
venue: "IEEE Transactions on Wireless Communications"
modeling_card: required
tags: [source, integrated-sensing-computation-communication, over-the-air-computation, federated-edge-learning, batch-size, convergence-analysis]
related:
  - "[[integrated-sensing-computation-communication]]"
  - "[[over-the-air-computation]]"
  - "[[federated-learning]]"
  - "[[wen-2024-iscc-edge-ai]]"
  - "[[dingzhu-wen]]"
  - "[[jie-xu]]"
  - "[[yuanming-shi]]"
  - "[[shuguang-cui]]"
created: 2026-11-02
updated: 2026-11-02
---

# Integrated Sensing, Communication, and Computation for Over-the-Air Federated Edge Learning

## Citation

Wen, D., Xie, S., Cao, X., Cui, Y., Xu, J., Shi, Y., & Cui, S. (2025). *Integrated Sensing, Communication, and Computation for Over-the-Air Federated Edge Learning*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2025.3598997.

## TL;DR

Edge devices sense objects wirelessly, train a recognition model on the sensed samples, and aggregate gradients by over-the-air computation (AirComp). A convergence analysis shows that sensing noise, batch size, and AirComp distortion jointly set the convergence rate, and an alternating design of batch sizes and sensing, computing, and AirComp resources maximizes loss degradation per round under latency and energy budgets.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: One edge server coordinates $K$ devices. In each round, device $k$ senses $b_k$ samples with sensing power $P_{k,s}$ over time $\tau_s$ per sample, computes local gradients at CPU frequency $f_k$, and uploads them by AirComp over $\lceil N/M\rceil$ slots of length $\tau_u$. Sensing noise $\delta_s^2$, channel noise $\sigma^2$, and AirComp distortion enter the convergence bound.

**Problem & objective**: $\mathcal P_2$ (per round): $\min_{\eta,\{b_k\},\{\alpha_k\},\{P_{k,s}\},\{f_k\}}\frac{\delta_u^2}{\eta}+\sum_k\frac{\alpha_k^2}{b_k}\left[\sigma^2+A^2\left(\delta_{k,c}^2+\frac{\delta_s^2}{P_{k,s}}\right)\right]$, equivalent to maximizing the loss-function degradation.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Batch size | $b_k$ | positive | Samples sensed and used by device $k$ |
| Aggregation weight | $\alpha_k=b_k/b$ | $\sum_k\alpha_k=1$ | Share of device $k$ in the global batch |
| Sensing power | $P_{k,s}$ | positive | Power used to sense each sample |
| CPU frequency | $f_k$ | positive | Local computing speed |
| AirComp factor | $\eta$ | positive | Normalizing factor of over-the-air aggregation |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| (44) | $\sum_k\alpha_k=1$. |
| (45) | Round latency, $b_k\tau_s+\frac{b_kC}{f_k}+\lceil N/M\rceil\tau_u\le\mathcal T$. |
| (46) | Device energy, $P_{k,s}b_k\tau_s+\Omega_kb_kCf_k^2+\frac{\eta\alpha_k^2N\tau_u}{H_k}\le E_k$. |

**Algorithm**: Decompose $\mathcal P_2$ into two convex subproblems, batch-size optimization and resource allocation, and solve them by alternating optimization in every round.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Wen et al. [x] studied an over-the-air federated edge learning system with integrated sensing, communication, and computation, in which an edge server coordinates multiple edge devices that wirelessly sense objects and use the sensing data to train a recognition model collaboratively. Over-the-air computation enables one-shot model aggregation from the devices. They analyzed convergence in terms of loss function degradation, accounting for wireless sensing noise during data acquisition and AirComp distortion during aggregation, and showed that sensing, communication, and computation compete for network resources to determine the convergence rate. Based on the analysis, they designed the ISCC parameters to maximize loss function degradation under per-round latency and energy budgets, using a low-complexity algorithm that alternately optimizes batch size control and network resource allocation. The results show that a device should spend less sensing power when it obtains a larger batch of samples and vice versa, and simulations verify the convergence behavior and performance gain of the scheme.

## Problem framing

Earlier Air-FEEL work assumed training data were already available. When devices must sense their own data, sensing quality and quantity become part of the learning-resource tradeoff.

## System model

- The convergence bound depends on sensing noise, batch size, and AirComp distortion.
- Each round has fixed latency and per-device energy budgets.

## Method

Variable substitution $\alpha_k=b_k/b$ yields $\mathcal P_2$, then batch size and resources are optimized in turn.

## Key findings

- Sensing, communication, and computation compete for resources to set the convergence rate.
- Larger batches call for less sensing power per sample, and the reverse.
- Simulations confirm faster convergence than baseline designs.

## Limitations / future work

The authors list further learning-performance enhancements as future directions.

## Relation to the corpus

Extends [[integrated-sensing-computation-communication]] and the edge-AI design in [[wen-2024-iscc-edge-ai]] to [[over-the-air-computation]]-based [[federated-learning]].

## Raw artifacts

- Parse: `raw/sources/Integrated_Sensing_Communication_and_Computation_for_Over-the-Air_Federated_Edge_Learning/Integrated_Sensing_Communication_and_Computation_for_Over-the-Air_Federated_Edge_Learning.md`
- Extracted figures are in the same folder; no companion PDF is present.
