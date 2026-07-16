---
type: source
title: "Multi-Agent DRL-Based Coded Caching and Resource Allocation in UAV-Assisted Networks"
authors: ["Bingxin Tian", "Li Wang", "Zheng Chang", "Lianming Xu", "Aiguo Fei"]
year: 2026
url: "https://doi.org/10.1109/TWC.2025.3587959"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), vol. 25, pp. 931-947"
modeling_card: required
tags: [source, coded-caching, erasure-coding, cache-repair, parameterized-dqn, multi-agent-drl, resource-allocation]
related:
  - "[[coded-caching]]"
  - "[[erasure-coded-edge-storage]]"
  - "[[uav-content-caching]]"
  - "[[regenerating-codes]]"
  - "[[parameterized-dqn]]"
  - "[[two-timescale-optimization]]"
  - "[[hybrid-action-decision-making]]"
  - "[[ma-pomdp]]"
  - "[[li-wang]]"
  - "[[lianming-xu]]"
  - "[[zheng-chang]]"
created: 2026-07-13
updated: 2026-07-16
---

# Multi-Agent DRL-Based Coded Caching and Resource Allocation in UAV-Assisted Networks

## Citation

Tian, B., Wang, L., Chang, Z., Xu, L., & Fei, A. (2026). *Multi-Agent DRL-Based Coded Caching and Resource Allocation in UAV-Assisted Networks*. **IEEE Transactions on Wireless Communications, 25**, 931-947. DOI: 10.1109/TWC.2025.3587959.

## TL;DR

Uses erasure and regenerating codes to distribute emergency content across UAV caches, then applies a two-timescale hierarchical multi-agent P-DQN to choose coding/cache decisions, requester and repair pairing, and UAV motion.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Coded content fragments are distributed across mobile UAV caches for emergency delivery. A requester reconstructs content from at least $k_f$ valid fragments, while a replacement UAV repairs a lost fragment by contacting at least $d_f$ surviving caches; a ground station supplies fallback data when aerial repair is infeasible.

**Problem & objective**: Problem P1 in (35) maximizes $T^{-1}\sum_t(\Pr^{Hit}(t)+\Pr^{Rep}(t))$, the time-average sum of content-download and fragment-repair success probabilities, over code, cache, matching, and UAV-motion decisions.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Code and cache design | $\mathcal C_f,(n_f,k_f,d_f),x_{if}$ | categorical, integer, and binary | Code family and parameters plus fragment placement on UAVs |
| Download matching | $z_{i,m,f}^{dl}(t)$ | binary, $\{0,1\}$ | UAV $i$ serves requester $m$ for content $f$ |
| Repair matching | $y_{i,j,f}^{rep}(t)$ | binary, $\{0,1\}$ | Valid UAV $i$ helps replacement UAV $j$ repair content $f$ |
| UAV speed | $v_i(t)$ | continuous, $[0,V_{\max}]$ | Travel distance control for UAV $i$ |
| UAV heading | $\theta_i(t)$ | continuous, $[0,2\pi]$ | Horizontal movement direction |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| 35b-35c | Cache placement is binary, fits UAV storage, and places each coded item on exactly $n_f$ UAVs |
| 35d-35e | Speed and heading remain within their physical ranges |
| 35f | Each UAV serves at most $q_i^{\max}$ download and repair recipients per slot |
| 35g-35h | A download uses at least $k_f$ helpers and a repair uses at least $d_f$ helpers |
| 35i-35j | UAVs maintain safety distance $D_{\min}$ and obey the per-slot movement limit $D_{\max}$ |

**Algorithm**: H-MA-PDQN separates decisions across two timescales. A control-station CP-PDQN updates code family, code parameters, and cache placement by time frame, while decentralized PT-PDQN agents update requester and repair matching together with continuous speed and heading in each short slot.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Tian et al. [x] studied coded content delivery and cache repair in a mobile UAV network with requester churn and battery-driven UAV replacement. They maximize average download and repair success probability by jointly selecting code parameters, fragment placement, requester and repair matching, and UAV trajectories under storage, service-count, reconstruction, safety, and mobility constraints. Their H-MA-PDQN framework places code and cache decisions in a slow control-station layer and matching and motion decisions in faster decentralized UAV agents. Parameterized Q-networks represent the resulting mixture of categorical, binary, and continuous actions without uniformly discretizing the motion variables. Simulations report higher success probability and lower transmission cost than DQN and greedy baselines, and dynamic UAV trajectories outperform static deployment under the tested requester distributions.

## Problem and system model

Files are split into coded fragments and placed across cache-enabled UAVs. A requester reconstructs a file after receiving at least `k` fragments; when a cache UAV becomes invalid, its replacement repairs a fragment by downloading data from at least `d` surviving UAVs. A ground control station provides fallback content when too few UAVs remain.

The model includes Zipf requests, requester arrivals/departures, direct or two-hop U2U/U2G delivery, full-duplex relay self-interference, rotary-wing energy, cache capacity, safety distance, service-count limits, and a battery-based invalid-UAV threshold. The displayed objective maximizes average download-plus-repair success probability; communication cost is derived and evaluated but is not an explicit objective term.

## Method

The slow CP-PDQN at the control station selects MDS/MSR/MBR code family, code parameters, and cache placement. Fast PT-PDQN agents independently choose requester/repair matches, speed, and heading within a cooperative [[ma-pomdp|Dec-POMDP]]. P-DQN couples discrete matching/coding actions to continuous motion parameters, with replay, epsilon-greedy exploration, target networks, and penalties that cancel unsafe movement.

## Key findings

- The abstract reports 26.7% and 66.7% higher success probability than DQN and greedy baselines, plus 27.3% and 42.9% lower transmission cost in the simulated comparisons.
- The default experiment uses four UAVs, ten requesters, two invalid UAVs, five content items, and a 2 km by 2 km area.
- Success saturates beyond roughly 30 MHz in the displayed setting; cost reaches its plotted minimum near repair interval 40.
- Dynamic UAV movement outperforms static deployment qualitatively in the reported request-distribution and mobility comparisons.

## Limitations

Evaluation is simulation-only and provides no global optimum, approximation bound, repeated-seed uncertainty, or deployment-latency evidence. The model assumes constant altitude, orthogonal UAV spectrum, equal bandwidth sharing, LoS U2U, at-most-two-hop delivery, full-duplex relay operation, known popularity, and control-station fallback. Energy enters state/accounting but the displayed optimization lacks a clear hard battery constraint. Several coding and energy equations are parse-damaged.

## Relation to the corpus

This source extends [[coded-caching]] from delivery into repairable aerial storage. [[regenerating-codes]] makes the MSR/MBR storage-versus-repair-bandwidth trade-off explicit, while [[two-timescale-optimization]] separates durable code/cache choices from fast matching and trajectory control.

## Raw artifacts

- `raw/sources/Multi-Agent_DRL-Based_Coded_Caching_and_Resource_Allocation_in_UAV-Assisted_Networks/Multi-Agent_DRL-Based_Coded_Caching_and_Resource_Allocation_in_UAV-Assisted_Networks.md`
- Original PDF and extracted figures (`images/`) are in the same folder.
