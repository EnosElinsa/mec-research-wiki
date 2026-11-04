---
type: source
title: "Diffusion-Based Dynamic Contract for Federated AI Agent Construction in Mobile Metaverses"
authors: ["Jinbo Wen", "Jiawen Kang", "Yang Zhang", "Yue Zhong", "Dusit Niyato", "Jie Xu", "Jianhang Tang", "Chau Yuen"]
year: 2026
url: "https://doi.org/10.1109/TSC.2026.3665640"
venue: "IEEE Transactions on Services Computing"
modeling_card: required
tags: [source, contract-theory, dynamic-contract, ai-agent, mobile-metaverse, diffusion-model, soft-actor-critic]
related:
  - "[[contract-theory]]"
  - "[[diffusion-model-as-optimizer]]"
  - "[[soft-actor-critic]]"
  - "[[generative-ai-for-mec]]"
  - "[[jiawen-kang]]"
  - "[[dusit-niyato]]"
  - "[[jie-xu]]"
created: 2026-11-02
updated: 2026-11-02
---

# Diffusion-Based Dynamic Contract for Federated AI Agent Construction in Mobile Metaverses

## Citation

Wen, J., Kang, J., Zhang, Y., Zhong, Y., Niyato, D., Xu, J., Tang, J., & Yuen, C. (2026). *Diffusion-Based Dynamic Contract for Federated AI Agent Construction in Mobile Metaverses*. **IEEE Transactions on Services Computing**. DOI: 10.1109/TSC.2026.3665640.

## TL;DR

Edge servers build AI agent modules for mobile metaverses, and a cloud server integrates them into agents deployed back at the edge. Because edge servers' willingness to participate changes over time and is private, the cloud server offers a two-period dynamic contract, and EDMSAC, a diffusion-model soft actor-critic with dynamic structured pruning of the actor, generates the optimal contracts.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A cloud server (CS) contracts with $K$ edge server (ES) types $\theta^1_k$ in period 1 and types $\theta^2_j$ in period 2, whose type evolves between periods. Each ES contributes to agent-module creation, and module quality $Q^1_k=1-2^{-T^1_k(2-L\delta)\delta\varepsilon/2}$ grows with its contracted contribution.

**Problem & objective**: Problem (27): $\max_{\{T^1_k,T^2_j(\theta^1_k)\}}U^1_{CS}(T^1_k)+\beta U^2_{CS}(T^2_j(\theta^1_k))$, the CS's expected two-period utility.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Period-1 contract item | $T^1_k$ | nonnegative, monotone in type | Contribution requested from a type-$\theta^1_k$ ES |
| Period-2 contract item | $T^2_j(\theta^1_k)$ | nonnegative | Contribution requested in period 2 given the period-1 type |
| Rewards | $R^1_k$, $R^2_j$ | determined by (19) and (24) | Payments that satisfy incentive constraints |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| (19) | Optimal period-2 rewards from individual rationality and incentive compatibility. |
| (24) | Optimal period-1 rewards, accounting for period-2 information rents. |
| Monotonicity | Contract items ordered by ES type. |

**Algorithm**: Substitute the optimal rewards to reduce variables from $4K$ to $2K$, then solve with EDMSAC, where a diffusion-model actor generates contracts and redundant actor neurons are pruned dynamically to improve denoising efficiency.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Wen et al. [x] developed an edge-cloud collaboration-based federated AI agent construction framework for mobile metaverses, motivated by the latency and data-leakage risks of building AI agents on cloud-based large language and vision-language models. In the framework, edge servers create agent modules in a distributed manner, and the cloud server integrates them into AI agents and deploys them at the edge for low-latency services. Because edge servers may exhibit dynamic willingness to participate, they designed a two-period dynamic contract model that continuously incentivizes participation and addresses dynamic information asymmetry. They proposed an enhanced diffusion model-based soft actor-critic algorithm that applies dynamic structured pruning to diffusion-based actor networks to generate optimal dynamic contracts. Simulation results show that the algorithm outperforms the original diffusion-based soft actor-critic by up to 23% in optimal contract generation.

## Problem framing

Static contracts assume fixed private types. When types change between periods, the principal must anticipate future information rents when designing current contracts.

## System model

- Two contracting periods with a discount factor $\beta$.
- Module quality depends on the contracted contribution.

## Method

Closed-form rewards reduce the problem; EDMSAC searches the remaining contract items.

## Key findings

- EDMSAC outperforms DMSAC by up to 23% in contract utility.
- Pruning the diffusion actor improves denoising efficiency and policy learning.

## Limitations / future work

The model uses two periods.

## Relation to the corpus

Extends [[contract-theory]] incentives with [[diffusion-model-as-optimizer]] solvers in a [[generative-ai-for-mec]] setting.

## Raw artifacts

- Parse: `raw/sources/Diffusion-Based_Dynamic_Contract_for_Federated_AI_Agent_Construction_in_Mobile_Metaverses/Diffusion-Based_Dynamic_Contract_for_Federated_AI_Agent_Construction_in_Mobile_Metaverses.md`
- Extracted figures are in the same folder; no companion PDF is present.
