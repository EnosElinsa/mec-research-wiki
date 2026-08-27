---
type: source
title: "Context-Aware AIGC Service Migration in Edge Intelligence Networks via Transformer DRL"
authors: ["Jiaxi Wang", "Yixue Hao", "Rui Wang", "Long Hu", "Kaibin Huang", "Dusit Niyato", "Min Chen"]
year: 2026
url: "https://doi.org/10.1109/TSC.2026.3656910"
venue: "IEEE Transactions on Services Computing (IEEE TSC)"
modeling_card: required
tags: [source, mobile-aigc, service-migration, value-of-context, transformer, soft-actor-critic, edge-intelligence]
related:
  - "[[mobile-aigc-network]]"
  - "[[aigc-service-provider]]"
  - "[[service-migration]]"
  - "[[value-of-context-aigc]]"
  - "[[transformer-encoder]]"
  - "[[soft-actor-critic]]"
  - "[[xu-2024-mobile-aigc-survey]]"
created: 2026-08-27
updated: 2026-08-27
---

# Context-Aware AIGC Service Migration in Edge Intelligence Networks via Transformer DRL

## Citation

Wang, J., Hao, Y., Wang, R., Hu, L., Huang, K., Niyato, D., & Chen, M. (2026). *Context-Aware AIGC Service Migration in Edge Intelligence Networks via Transformer DRL*. **IEEE Transactions on Services Computing**. DOI: 10.1109/TSC.2026.3656910.

## TL;DR

The paper migrates historical AIGC context rather than large generative models when mobile users move between edge servers. A Value of Context metric combines freshness and semantic relevance, and a transformer-based Soft Actor-Critic policy, TFSCM, jointly balances inference accuracy, service latency, and context-migration cost.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A mobile user accesses an AIGC service through a current edge server while the service host may remain at the previous server or move to the current access server. Historical text or image context windows can be migrated to preserve inference continuity under model token limits and finite edge storage.

**Problem & objective**: Maximize weighted utility, $\max_{u,b}\;\mathcal F=\mu_1A-\mu_2C-\mu_3D$, combining inference accuracy $A$, context migration cost $C$, and end-to-end latency $D$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Service migration | $u(t)$ | Binary in $[0,1]$ | Whether the AIGC service host changes at slot $t$ |
| Context amount | $b(t)$ | Continuous/integer in $[0,\Omega_t]$ | Migrated context-window length |
| Service host | $y_t$ | Discrete server index | Host selected from $\{y_{t-1},x_t\}$ |
| Context window | $w(t)$ | Structured token/patch record | Historical prompt/output content and keyword indicator |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Service migration action is bounded: $u(t)\in[0,1]$. |
| C2 | Migrated context is bounded by available context: $b(t)\in[0,\Omega_t]$. |
| C3 | Effective context length obeys $\Omega_t\le\Omega$. |
| C4 | The host is either retained or moved to the current access server: $y_t\in\{y_{t-1},x_t\}$. |
| C5 | End-to-end service latency remains below the user tolerance: $D(t)<\tau_{\max}$. |

**Algorithm**: Formulate the process as an MDP and use a transformer actor over the previous $N$ state vectors, dual MLP critics, replay, and entropy-regularized SAC. The resulting TFSCM policy outputs discrete migration and context-transfer actions while the environment computes VoC, accuracy, latency, and cost.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Wang et al. [x] formulated context-aware AIGC service migration for mobile users in edge intelligence networks. They migrated historical context windows instead of large AIGC models and optimized inference accuracy, service latency, and migration cost through service and context decisions. Their Value of Context metric combines temporal freshness with keyword-based semantic relevance, while TFSCM uses a transformer actor inside Soft Actor-Critic to exploit long-term decision dependencies. Experiments on the Telecom Shanghai dataset and a second dataset report higher utility than static, random, fixed, full, PPO, and fully connected SAC migration baselines. The reported accuracy and latency trends arise from the paper's logarithmic accuracy and token-based latency models rather than measurements of a deployed AIGC service.

## Problem and system model

Mobile users may change access edge servers while AIGC inference depends on historical prompts and generated content. Migrating full-scale models is costly, but discarding context can reduce inference accuracy. The model represents each context window by input/output token or patch lengths and a keyword indicator, limits context by model capacity and host availability, and allows the service host to stay or move to the current access server.

## Method

VoC discounts stale context and semantically dissimilar windows, then accumulates their values for the current request. A logarithmic function maps accumulated VoC to inference accuracy; transmission, computation, and context-migration terms form service latency. TFSCM uses a transformer actor over a sequence retrieved from replay, twin critics, and SAC entropy regularization.

## Key findings

- TFSCM converges within about 50 episodes and reaches the highest reward in the reported DRL comparison; PPO converges faster but to a lower reward, while fully connected SAC converges more slowly.
- TFSCM has the highest system utility across tested context lengths, accuracy coefficients, datasets, and edge-server densities.
- The evaluated TFSCM configuration uses an average inference time of about 1.0 ms and an average training time of about 216 s on the reported GPU/CPU platform.
- Full migration can incur strongly negative utility because context-transfer cost outweighs its accuracy benefit, while static hosting saves migration cost but loses contextual accuracy.

## Limitations / future work

The evaluation uses simulated AIGC accuracy coefficients, CogView2 parameters, and a time-slotted mobility trace rather than an end-to-end deployed model. Future work in the paper targets structural-level memory migration and multi-user heterogeneous edge-cloud integration.

## Relation to the corpus

This source extends [[mobile-aigc-network]] and [[aigc-service-provider]] with context continuity as a migration decision. It complements [[service-migration]] studies that move service instances or tasks and connects [[soft-actor-critic]] with a transformer history encoder.

## Raw artifacts

- Parse: `raw/sources/Context-Aware_AIGC_Service_Migration_in_Edge_Intelligence_Networks_via_Transformer_DRL/Context-Aware_AIGC_Service_Migration_in_Edge_Intelligence_Networks_via_Transformer_DRL.md`
- Origin PDF and extracted figures (`images/`) are in the same folder.
