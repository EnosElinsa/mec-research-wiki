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
updated: 2026-11-03
---

# Deep Lifelong Learning for Adaptive Semantic-Aware Content Reuse in UAV-Assisted Metaverse

## Citation

Wang, N., Wu, Y., Lorenzo, B., Samarakoon, S., & Liu, B. (2026). *Deep Lifelong Learning for Adaptive Semantic-Aware Content Reuse in UAV-Assisted Metaverse*. **IEEE Transactions on Mobile Computing**, 25(7), 10847-10863. DOI: 10.1109/TMC.2026.3664868.

## TL;DR

A UAV-assisted Metaverse edge-rendering framework where UAV servers cache semantic subject/object components, reuse semantically similar cached content after cache misses, and adapt across changing semantic environments using Deep-Centralized ELLA (DC-ELLA). The paper focuses on communication and computation savings from semantic reuse; UAV mobility and endurance are treated as exogenous rather than jointly optimized.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Users submit Metaverse frame-rendering requests to UAV semantic edge servers with bounded subject and object caches. Requests are served by exact cache hits, similarity-based semantic reuse, or full rendering as popularity, task arrivals, queues, and semantic environments change.

**Problem & objective**: Problem P1 (17) jointly chooses user-server association, subject and object caching, and content-reuse selection to maximize server utility $U_j(t)$ (16), a weighted sum of average computation-time saving $S_{j,v}^{ave}(t)$ and task completion quality $Sa_j(t)$ (15). The parse garbles the objective and constraint block of (17); check the published paper. P1 is then recast as a sequence of MDP tasks whose reward equals $U_j(t)$, with long-term objective (18).

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| User-server association | $z_{i,j}^v(t)$ | binary | User $i$ uploads frame $v$ to UAV server $j$ |
| Subject caching | $\mathbf 1_{j,n}^s(t)$ | binary | Subject content $n$ is cached at server $j$ |
| Object caching | $\mathbf 1_{j,k}^o(t)$ | binary | Object content $k$ is cached at server $j$ |
| Content reuse | $x_{j,n,n'}^s,\ y_{j,k,k'}^o$ | binary | Cached item reused for a missed subject or object; set deterministically, not learned |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| (17.a) | Each user selects only one UAV server per time step |
| (17.b) | The number of users choosing servers is at most the maximum number of users |
| (17.c) | Cached subjects and objects at each server fit its storage capacity $N_{F_j}$ |
| (17.d)-(17.e) | Reused content is the most similar item and must already be cached |
| (17.f) | Exactly one cached item is reused for each content request |

**Algorithm**: Extract subject and object features with the semantic encoder, compute content-level and environment-level similarity, let each UAV server's local PPO learner choose association and cache updates, transfer environment-conditioned policy knowledge from the centralized DC-ELLA dictionary, and update the lifelong knowledge base after each semantic environment.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Wang et al. [x] studied adaptive semantic-aware content reuse for UAV-assisted Metaverse rendering. They modeled user-server association, semantic subject and object caching, similarity-based reuse, full rendering, queueing, and service quality as a stochastic decision problem. The service policy chooses among exact semantic hits, semantic reuse after a cache miss, and full rendering under association, cache-capacity, and reuse-selection constraints. DC-ELLA maintains a centralized environment dictionary and transfers prior policy knowledge to local PPO-style UAV learners when semantic preferences and arrivals change. Simulations report higher long-term rewards than PPO, PG-ELLA, and transfer-learning baselines, and 20% to 65% more computation-time saving than an exact-hit-only PPO baseline; the gap narrows when semantic reuse is degraded.

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

- `raw/sources/Deep_Lifelong_Learning_for_Adaptive_Semantic-Aware_Content_Reuse_in_UAV-Assisted_Metaverse/Deep_Lifelong_Learning_for_Adaptive_Semantic-Aware_Content_Reuse_in_UAV-Assisted_Metaverse.md`
- Original PDF and extracted figures (`images/`) in the same folder.
