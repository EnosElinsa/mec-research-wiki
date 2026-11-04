---
type: source
title: "The Larger the Merrier? Efficient Large AI Model Inference in Wireless Edge Networks"
authors: ["Zhonghao Lyu", "Ming Xiao", "Jie Xu", "Mikael Skoglund", "Marco Di Renzo"]
year: 2026
url: "https://doi.org/10.1109/JSAC.2025.3645168"
venue: "IEEE Journal on Selected Areas in Communications"
modeling_card: required
tags: [source, large-ai-model, co-inference, model-pruning, model-partition, rate-distortion, edge-inference]
related:
  - "[[dnn-model-partition]]"
  - "[[collaborative-dl-inference]]"
  - "[[distributed-foundation-models]]"
  - "[[zhonghao-lyu]]"
  - "[[jie-xu]]"
  - "[[marco-di-renzo]]"
created: 2026-11-02
updated: 2026-11-03
---

# The Larger the Merrier? Efficient Large AI Model Inference in Wireless Edge Networks

## Citation

Lyu, Z., Xiao, M., Xu, J., Skoglund, M., & Di Renzo, M. (2026). *The Larger the Merrier? Efficient Large AI Model Inference in Wireless Edge Networks*. **IEEE Journal on Selected Areas in Communications**. DOI: 10.1109/JSAC.2025.3645168.

## TL;DR

A pretrained large AI model (LAIM) is pruned and split into on-device and on-server sub-models for edge-device co-inference. The paper bounds output distortion by parameter distortion, lower-bounds parameter distortion with rate-distortion theory as a function of pruning ratio, and minimizes that bound over pruning ratios, split point, transmit power, and CPU frequencies under delay and energy limits.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A device runs the first $L_D$ layers of a pruned LAIM and sends intermediate features to an edge server over a wireless link with power $p$; the server runs the rest. Device and server prune with ratios $\rho$ and $\tilde\rho$ and compute at frequencies $f$ and $\tilde f$.

**Problem & objective**: (P1): $\min_{\rho,f,p,L_D,\tilde\rho,\tilde f}\hat D(\rho,\tilde\rho,L_D)$, the lower bound on co-inference distortion.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Pruning ratios | $\rho$, $\tilde\rho$ | $[0,1]$ | Fraction pruned on device and server sub-models |
| Split point | $L_D$ | integer layer index | Number of layers on the device |
| Transmit power | $p$ | bounded by the device maximum | Feature upload power |
| CPU frequencies | $f$, $\tilde f$ | $[0,f^{\max}]$, $[0,\tilde f^{\max}]$ | Device and server computing speeds |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| (44a) | Inference delay, $T(\rho,f,p,L_D,\tilde\rho,\tilde f)\le T_0$. |
| (44b) | Energy, $E(\rho,f,p,L_D,\tilde\rho,\tilde f)\le E_0$. |
| (44c)-(44d) | $0\le\rho\le1$, $0\le\tilde\rho\le1$. |
| (44e)–(44f) | CPU limits $0\le f\le f^{\max}$, $0\le\tilde f\le\tilde f^{\max}$, and the power constraint (1), $0\le p\le P_{\max}$ |

**Algorithm**: For each split point $L_D$, introduce auxiliary variables $\rho',\tilde\rho'$ (P2), linearize the non-convex delay and energy terms, and solve the convex problems (P3.k) by SCA with non-increasing objective values; pick the best $L_D$ by exhaustive search.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Lyu et al. [x] investigated pruning-aware large artificial intelligence model co-inference, in which a pre-trained model is pruned and partitioned into on-device and on-server sub-models for resource-efficient execution in wireless edge networks. They first proved that the model's output distortion is upper bounded by its parameter distortion, and then derived a lower bound on parameter distortion via rate-distortion theory that captures the relationship between pruning ratio and co-inference performance. Based on this analysis, they formulated a distortion bound minimization problem that jointly optimizes the pruning ratio, split point, transmit power, and computation frequency under system resource, inference delay, and energy constraints. An efficient algorithm is developed for the resulting highly non-convex problem. Experiments with ViT and VideoMAE show that the design outperforms on-device inference, on-server inference, and a PPO-based baseline in balancing inference performance, latency, and energy consumption, and that the bound tracks measured distortion closely when more than 40% of parameters are retained.

## Problem framing

Large models exceed device resources, and moving all computation to the server stresses the link. Pruning trades accuracy for resources, so it should be designed together with the split and the radio.

## System model

- Delay and energy include device computation, feature transmission, and server computation.
- Distortion depends on pruning ratios and the split point.

## Method

Rate-distortion analysis gives a tractable objective; optimization then balances delay, energy, and distortion.

## Key findings

- Output distortion is bounded by parameter distortion.
- The analytical bound is tight when over 40% of parameters are kept.
- The joint design outperforms benchmarks across delay and energy budgets.

## Limitations / future work

The analysis targets one device and one server.

## Relation to the corpus

Extends [[dnn-model-partition]] and [[collaborative-dl-inference]] to pruned large models, related to [[distributed-foundation-models]].

## Raw artifacts

- Parse: `raw/sources/The_Larger_the_Merrier_Efficient_Large_AI_Model_Inference_in_Wireless_Edge_Networks/The_Larger_the_Merrier_Efficient_Large_AI_Model_Inference_in_Wireless_Edge_Networks.md`
- Extracted figures are in the same folder; no companion PDF is present.
