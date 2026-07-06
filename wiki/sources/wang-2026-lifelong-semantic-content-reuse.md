---
type: source
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
updated: 2026-07-06
---

# Deep Lifelong Learning for Adaptive Semantic-Aware Content Reuse in UAV-Assisted Metaverse

## Citation

Wang, N., Wu, Y., Lorenzo, B., Samarakoon, S., & Liu, B. (2026). *Deep Lifelong Learning for Adaptive Semantic-Aware Content Reuse in UAV-Assisted Metaverse*. **IEEE Transactions on Mobile Computing**, 25(7), 10847-10863. DOI: 10.1109/TMC.2026.3664868.

## TL;DR

A UAV-assisted Metaverse edge-rendering framework where UAV servers cache semantic subject/object components, reuse semantically similar cached content after cache misses, and adapt across changing semantic environments using Deep-Centralized ELLA (DC-ELLA). The paper focuses on communication and computation savings from semantic reuse; UAV mobility and endurance are treated as exogenous rather than jointly optimized.

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
