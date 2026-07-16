---
type: source
title: "Optimizing Energy and Revenue Efficiency in UAV-Assisted Vehicular Networks with Enhanced Reward Twin Actor TD3 and Secure Caching Strategies"
authors: ["Shibo Hu", "Guizhong Liu", "Xing Chen"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3709182"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
modeling_card: required
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
updated: 2026-07-16
---

# Optimizing Energy and Revenue Efficiency in UAV-Assisted Vehicular Networks with Enhanced Reward Twin Actor TD3 and Secure Caching Strategies

## Citation

Hu, S., Liu, G., & Chen, X. (2026). *Optimizing Energy and Revenue Efficiency in UAV-Assisted Vehicular Networks with Enhanced Reward Twin Actor TD3 and Secure Caching Strategies*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2026.3709182. DOI/venue/year are parse-silent at the top level and verified against a title-matched Crossref/IEEE DOI record.

## TL;DR

Proposes a cache-enabled UAV vehicular MEC architecture where UAVs process offloaded vehicle tasks and cache task results, while private tasks keep sensitive final processing local. The ERTATD3 algorithm extends [[td3]] with twin actor networks and enhanced reward design to jointly optimize UAV trajectory, offloading, resource allocation, and secure caching for energy efficiency and service revenue.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Cache-enabled UAVs act as aerial MEC servers for moving vehicles over OFDMA links. A UAV may process and cache reusable general results, while privacy-sensitive tasks cache only intermediate sections and complete personalized processing locally; decisions couple task offloading, CPU and power allocation, secure caching, and UAV service position.

**Problem & objective**: Problem (29) is an NP-hard multi-objective MINLP that minimizes energy minus provider revenue, $\min U=\rho_1\left(\sum_kET_k+E_j\right)-\rho_2\sum_kM_k$, over offloading, resource allocation, transmit power, and UAV movement.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Task offloading | $o_k$ | binary, $\{0,1\}$ | Whether vehicle $k$ offloads rather than processes locally |
| UAV movement | $a_j^{move}$ | binary, $\{0,1\}$ | Whether UAV $j$ flies toward its target service position or hovers |
| UAV compute allocation | $\alpha_{j,k}$ | continuous, $[0,1]$ | UAV computing share allocated to vehicle $k$ |
| Local compute allocation | $\gamma_k$ | continuous, $[0,1]$ | Vehicle-side computing share |
| Vehicle transmit power | $P_k$ | continuous, bounded | Uplink power used by vehicle $k$ |
| UAV service position | $L_j^*=(Lx_j^*,Ly_j^*)$ | continuous in the service region | Target UAV location |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1-C2 | Offloading and UAV movement decisions are binary |
| C3-C5 | UAV and local computing shares lie in $[0,1]$ and aggregate UAV allocation is at most one |
| C6 | Vehicle power satisfies $P_k\leq\bar P_k$ |
| C7 | Vehicle task energy plus UAV energy does not exceed $\bar E$ |
| C8 | Each result delay satisfies $T_k\leq Sd_k$ |
| C9 | UAV coordinates remain in the $1000\times1000$ service region |

**Algorithm**: Model the MINLP as an MDP whose action contains movement, offloading, resource, power, and caching choices; calculate a hierarchical reward that first penalizes constraint and delay violations and then normalizes energy and revenue utility; generate two independent actor actions and fuse them; train the ERTATD3 twin actors and twin critics with replay, target smoothing, and delayed policy updates until reward stabilizes.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Hu et al. [x] studied joint energy and revenue efficiency in a cache-enabled UAV-assisted vehicular MEC network with secure partial-result caching for privacy-sensitive tasks. They formulated an NP-hard mixed-integer nonlinear program over offloading, UAV movement, computing allocation, vehicle power, and service position that minimizes task and UAV energy while maximizing provider revenue under resource, energy, delay, and region constraints. Their ERTATD3 method combines twin actor networks with a hierarchical reward that enforces feasibility before optimizing normalized energy and revenue terms. Simulations report stabilization after about 1800 episodes, lower reward variance and delay than the evaluated TD3 and DDPG variants, and reduced privacy leakage with secure caching.

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
