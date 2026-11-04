---
type: source
title: "Service Migration Strategies Based on Partially Observable and Multi-Objective Optimization"
authors: ["Yingzhen Hou", "Lei Yang", "Yu Dai"]
year: "not in parse"
url: "not in parse"
venue: "not in parse"
modeling_card: required
tags: [source, service-migration, vehicular-mec, pomdp, multi-objective-reinforcement-learning, maximum-entropy]
related:
  - "[[service-migration]]"
  - "[[vehicular-mec]]"
  - "[[pomdp]]"
  - "[[soft-actor-critic]]"
created: 2026-08-27
updated: 2026-11-03
---

# Service Migration Strategies Based on Partially Observable and Multi-Objective Optimization

## Citation

Hou, Y., Yang, L., & Dai, Y. *Service Migration Strategies Based on Partially Observable and Multi-Objective Optimization*. Venue and year are not in the parse.

## TL;DR

AVSI-MEMPO selects MEC migration nodes for highly mobile vehicles under incomplete observations and conflicting latency and energy objectives. An adversarial variational LSTM infers hidden state, while a maximum-entropy multi-policy optimizer produces policies across dynamic objective weights.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A vehicle moves across MEC coverage areas and must select a target server for its service instance using only partial observations of a changing IoV environment; non-local server loads are not observed in real time.

**Problem & objective**: Problem (11) chooses migration decisions $\{a_t(n)\}$ that minimize total cost over horizon $T$, $\min_{\{a_t(n)\}}\sum_{t=1}^{T}r(T_t^{\mathrm{total}}(n),E_t^{\mathrm{total}}(n))$, where $T^{\mathrm{total}}$ is migration, transmission, propagation, and computation delay, $E^{\mathrm{total}}$ is the corresponding energy consumption, and $r$ is either reward, their average, or their sum.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
| --- | --- | --- | --- |
| Migration destination | $a_t(n)$ | discrete, $a_t(n)\in\mathcal M$ | MEC server selected for user $n$ in slot $t$ |
| Learned objective weights | $\delta^t,\eta^t$ | continuous, updated by (26)-(27) | MEMPO weights between the latency and energy critics; not part of (11) |
| Latent state | $z_t(n)$ | continuous encoding | AVSI estimate of the hidden environment state; not part of (11) |

**Constraints**:

| ID | Meaning and key expression |
| --- | --- |
| (11), action set | Each user's migration target is a server in $\mathcal M$: $a_t(n)\in\mathcal M$ |
| (11), capacity | Task load plus real-time server load stays within the server capacity: $\sum_n(c_t(n)+\eta_t(n))\leq f_{\max}$ |

**Algorithm**: Encode observation sequences with a variational LSTM trained with reconstruction and adversarial objectives, then use maximum-entropy multi-objective policy optimization with separate latency and energy critics and dynamic weights to learn migration policies.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Hou et al. [x] modeled vehicular MEC service migration with incomplete information as a partially observable Markov decision process. Their AVSI encoder combines an encoder-decoder, variational inference, adversarial learning, and LSTM memory to estimate hidden environmental state from observation histories. MEMPO then uses maximum entropy and dynamic objective weights to search for migration policies balancing latency and energy consumption. Experiments on San Francisco and Rome mobility traces report consistent gains over the compared migration baselines, including DRACM and VRMPO_AC, and near-optimal results in the evaluated scenarios. The near-optimal statement is empirical for those scenario sets rather than a general optimality guarantee.

## Problem and system model

Vehicle mobility makes server and link state difficult to observe completely, while low interruption latency and green energy goals can conflict. The decision is which MEC node should host the moving user's service.

## Method

AVSI learns a latent representation of hidden environment state from partial histories. MEMPO augments multi-objective actor-critic learning with entropy and changing preference weights so that a collection of policies approximates the latency-energy Pareto front.

## Key findings

- AVSI-MEMPO outperforms four reported baselines over real-trajectory experiments.
- The inferred hidden state improves migration decisions relative to methods using limited observation directly.
- Maximum-entropy exploration and dynamic weights improve the evaluated Pareto policy set.

## Limitations / future work

Evaluation is dataset- and simulation-based. The paper's near-optimal wording is tied to the tested scenario sets and does not establish global optimality for arbitrary MEC dynamics.

## Relation to the corpus

This source extends [[service-migration]] into partial observability and explicit latency-energy Pareto control. It complements single-policy [[soft-actor-critic]] migration formulations by producing policies for multiple objective preferences.

## Raw artifacts

- Parse: `raw/sources/Service_Migration_Strategies_Based_on_Partially_Observable_and_Multi-Objective_Optimization/Service_Migration_Strategies_Based_on_Partially_Observable_and_Multi-Objective_Optimization.md`
- Origin PDF and extracted figures are in the same folder.
