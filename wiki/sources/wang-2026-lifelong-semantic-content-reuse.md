---
type: source
modeling_card: required
title: "Deep Lifelong Learning for Adaptive Semantic-Aware Content Reuse in UAV-Assisted Metaverse"
authors: ["Ning Wang", "Yinxuan Wu", "Beatriz Lorenzo", "Sumudu Samarakoon", "Bing Liu"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3664868"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, uav-assisted-metaverse, semantic-communication, semantic-content-reuse, caching, edge-rendering, lifelong-learning, ppo]
related:
  - "[[semantic-content-reuse]]"
  - "[[semantic-communication]]"
  - "[[service-caching-mec]]"
  - "[[mobile-aigc-network]]"
  - "[[uav-trajectory-control]]"
  - "[[task-offloading]]"
created: 2026-07-06
updated: 2026-07-16
---

# Deep Lifelong Learning for Adaptive Semantic-Aware Content Reuse in UAV-Assisted Metaverse

## Citation

Wang, N., Wu, Y., Lorenzo, B., Samarakoon, S., & Liu, B. (2026). *Deep Lifelong Learning for Adaptive Semantic-Aware Content Reuse in UAV-Assisted Metaverse*. **IEEE Transactions on Mobile Computing**, 25(7), 10847-10863. DOI: 10.1109/TMC.2026.3664868.

## TL;DR

A UAV-assisted Metaverse edge-rendering framework where UAV servers cache semantic subject/object components, reuse semantically similar cached content after cache misses, and adapt across changing semantic environments using Deep-Centralized ELLA (DC-ELLA). The paper focuses on communication and computation savings from semantic reuse; UAV mobility and endurance are treated as exogenous rather than jointly optimized.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Users submit Metaverse frame-rendering requests to UAV semantic edge servers with bounded subject and object caches. Requests are served by exact cache hits, similarity-based semantic reuse, or full rendering as popularity, task arrivals, queues, and semantic environments change.

**Problem & objective**: A stochastic semantic caching and association MDP maximizes discounted service reward, $\max_{\pi}\mathbb E_{\pi}[\sum_t\gamma^t r_t]$, where reward combines computation-time savings, queue reduction, latency satisfaction, and resolution quality.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| User-server association | $x_{u,m}(t)$ | binary | UAV server selected for user $u$ |
| Subject cache placement | $c^{\mathrm{sub}}_{m,f}(t)$ | binary | Subject component $f$ stored at UAV $m$ |
| Object cache placement | $c^{\mathrm{obj}}_{m,f}(t)$ | binary | Object component $f$ stored at UAV $m$ |
| Service mode | $z_{u}(t)$ | categorical | Exact hit, semantic reuse, or full rendering |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Each request associates with one reachable UAV server |
| C2 | Subject and object placements respect each UAV cache capacity |
| C3 | Semantic reuse is selected only when similarity and reuse-probability conditions hold |
| C4 | Rendering and queue service obey UAV computation capacity and request latency limits |
| C5 | Completion quality reflects both latency and resolution satisfaction |

**Algorithm**: Extract subject and object features with the semantic encoder → compute content-level and environment-level similarity → choose association, cache updates, and service mode with local PPO learners → transfer environment-conditioned policy knowledge from the centralized DC-ELLA dictionary → update the lifelong knowledge base after each semantic environment.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Wang et al. [x] studied adaptive semantic-aware content reuse for UAV-assisted Metaverse rendering. They modeled user-server association, semantic subject and object caching, similarity-based reuse, full rendering, queueing, and service quality as a stochastic decision problem. The service policy chooses among exact semantic hits, semantic reuse after a cache miss, and full rendering under cache and computation limits. DC-ELLA maintains a centralized environment dictionary and transfers prior policy knowledge to local PPO-style UAV learners when semantic preferences and arrivals change. Simulations report faster adaptation and greater computation-time savings than the evaluated exact-hit, local-learning, transfer-learning, and lifelong-learning baselines.

## Problem

Metaverse services generate many image/frame rendering requests, but exact-cache-hit policies miss reuse opportunities when requests differ syntactically while sharing semantic content or context. UAV edge servers also face changing user preferences and arrival rates, so a policy trained for one semantic environment can adapt slowly or become unstable in a new one. The paper targets user-server association, semantic caching, rendering, and reuse decisions that improve resource savings and service quality.

## System model

- **Architecture:** users send frame rendering requests to UAV servers acting as mobile semantic edge servers.
- **Semantic representation:** frame contents are decomposed into subject and object semantic symbols, then encoded as semantic feature vectors using a frozen MPNet sentence encoder; RelTR is the scene-graph extractor named in the parse.
- **Cache state:** each UAV server can cache a bounded number of subject and object contents and tracks request popularity plus semantic-environment features.
- **Reuse metric:** content-level and environment-level cosine similarities are combined into a content reuse probability.
- **Quality metric:** task-completion quality combines latency satisfaction and resolution-quality satisfaction.

## Method

The model has three service modes: exact semantic cache hit, semantic cache reuse, and full rendering. User-server association and caching are formulated as an MDP where each UAV server is a local learner, while a central lifelong-learning agent maintains a knowledge base and environment dictionary. DC-ELLA maps semantic-environment feature vectors to policy guidance, transferring prior knowledge to local PPO-style learners when content preferences or task arrival conditions change.

## Key findings

- In static and dynamic semantic environments, the content-reuse mechanism outperforms exact-hit-only caching in reward, computational savings, queue length, and service quality trends reported in the figures.
- The parse reports that Content Reuse + DC-ELLA improves computational time savings by **20% to 65%** compared with the Only Hit + PPO baseline, with the largest gains in medium-demand server categories.
- DC-ELLA starts from higher reward / saving levels and adapts faster than PG-ELLA, transfer learning, and a local PPO learner when the test environment differs from pre-training.
- With fixed caching after a preference shift, semantic content reuse mitigates the performance drop that exact-hit caching suffers after user preferences change.

## Limitations / future work

The paper states four limitations directly: dependence on scene-graph extraction accuracy, centralized lifelong learning that does not fully exploit decentralized / on-device interaction among UAVs, evaluation on a small regional UAV swarm, and no explicit trajectory or propulsion-energy optimization. It also notes that Visual Genome is not Metaverse-specific and defers evaluation on real Metaverse traces.

## Relation to the corpus

This source extends the [[semantic-communication]] and caching track with [[semantic-content-reuse]]: it caches and reuses semantic components rather than only services or task binaries as in [[service-caching-mec]]. It is adjacent to the [[mobile-aigc-network]] track because it targets Metaverse rendering and semantic content delivery, but its main algorithmic contribution is lifelong policy transfer for semantic caching rather than generative content synthesis. Its explicit deferral of trajectory and endurance control makes it complementary to the UAV trajectory / offloading papers filed under [[uav-trajectory-control]] and [[task-offloading]].

## Raw artifacts

- `raw/sources/Deep Lifelong Learning for Adaptive Semantic-Aware Content Reuse in UAV-Assisted Metaverse/Deep Lifelong Learning for Adaptive Semantic-Aware Content Reuse in UAV-Assisted Metaverse.md`
- Original PDF and extracted figures (`images/`) in the same folder.
