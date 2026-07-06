---
type: source
title: "Optimizing Energy and Revenue Efficiency in UAV-Assisted Vehicular Networks with Enhanced Reward Twin Actor TD3 and Secure Caching Strategies"
authors: ["Shibo Hu", "Guizhong Liu", "Xing Chen"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3709182"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, vehicular-mec, secure-caching, service-caching, td3, task-offloading, uav-trajectory-control]
related:
  - "[[vehicular-mec]]"
  - "[[secure-caching-uav-mec]]"
  - "[[privacy-sensitive-data-partitioning]]"
  - "[[service-caching-mec]]"
  - "[[td3]]"
  - "[[task-offloading]]"
  - "[[uav-trajectory-control]]"
created: 2026-07-07
updated: 2026-07-07
---

# Optimizing Energy and Revenue Efficiency in UAV-Assisted Vehicular Networks with Enhanced Reward Twin Actor TD3 and Secure Caching Strategies

## Citation

Hu, S., Liu, G., & Chen, X. (2026). *Optimizing Energy and Revenue Efficiency in UAV-Assisted Vehicular Networks with Enhanced Reward Twin Actor TD3 and Secure Caching Strategies*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2026.3709182. DOI/venue/year are parse-silent at the top level and verified against a title-matched Crossref/IEEE DOI record.

## TL;DR

Proposes a cache-enabled UAV vehicular MEC architecture where UAVs process offloaded vehicle tasks and cache task results, while private tasks keep sensitive final processing local. The ERTATD3 algorithm extends [[td3]] with twin actor networks and enhanced reward design to jointly optimize UAV trajectory, offloading, resource allocation, and secure caching for energy efficiency and service revenue.

## Problem

Vehicular MEC links are unstable because vehicles move quickly and wireless conditions change. Caching popular task results at UAV edge servers can reduce repeated computation and delay, but naive full-result caching can leak private vehicle information. The paper therefore optimizes a three-way tradeoff among task delay, UAV energy, provider revenue, and secure use of cached results.

## System model

The system contains vehicles and cache-enabled UAVs that act as aerial edge servers with limited computing and storage. Each vehicle requests one task. UAVs can process offloaded tasks, cache general task results, and cache only sectional intermediate results for private tasks. For private navigation or AR-HUD-like services, generic map/routing or rendering components can be cached at the UAV, while personalized origin/destination, preferences, or calibration remain for local vehicle-side processing. The paper assumes an LRU caching policy and an OFDMA radio model with fixed subcarrier bandwidth.

## Method

ERTATD3 builds on TD3 by using twin actor networks whose proposed actions are fused. The reward is hierarchical: constraint satisfaction shapes feasible actions first; delay violations and complex actions are penalized; normalized energy and revenue terms guide optimization after feasibility. The action space includes UAV movement, offloading decisions, UAV-side resource allocation, and caching choices.

## Key findings

- Training stabilizes after roughly 1800 episodes in the reported curves, with ERTATD3 reaching higher asymptotic reward and lower rolling-reward variance than TD3/DDPG-style baselines.
- DDPG is reported to converge only after about 8000 episodes and to a lower final reward, while no-enhanced-reward variants are unstable and one fails to converge after 10000 episodes.
- Secure caching reduces privacy-leakage probability and keeps task-related energy comparable to general caching, with slightly higher revenue than the non-secure alternatives in the reported comparisons.
- ERTATD3 is reported to achieve lower average delay and lower delay variance across vehicle-speed ranges.
- The processing-distribution analysis reports that larger tasks tend to stay local because transmission delay dominates, while higher computation density increases UAV offloading.

## Limitations / future work

The parse reports simulation comparisons but does not describe hardware validation. Explicit future-work directions are not in parse.

## Relation to the corpus

This source connects [[vehicular-mec]], [[service-caching-mec]], and [[privacy-sensitive-data-partitioning]] through [[secure-caching-uav-mec]]. It differs from ordinary content caching because the cache policy is split by task privacy: general results can be reused, while private results are only partially cached and finalized locally. Algorithmically, it broadens the [[td3]] line with twin-actor action fusion and reward shaping for a joint energy/revenue objective.

## Raw artifacts

- `raw/sources/Optimizing Energy and Revenue Efficiency in UAV-Assisted Vehicular Networks with Enhanced Reward Twin Actor TD3 and Secure Caching Strategies/Optimizing Energy and Revenue Efficiency in UAV-Assisted Vehicular Networks with Enhanced Reward Twin Actor TD3 and Secure Caching Strategies.md`
- Original PDF and extracted figures (`images/`) in the same folder.
