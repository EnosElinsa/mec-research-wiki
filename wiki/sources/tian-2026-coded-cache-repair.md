---
type: source
title: "Multi-Agent DRL-Based Coded Caching and Resource Allocation in UAV-Assisted Networks"
authors: ["Bingxin Tian", "Li Wang", "Zheng Chang", "Lianming Xu", "Aiguo Fei"]
year: 2026
url: "https://doi.org/10.1109/TWC.2025.3587959"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), vol. 25, pp. 931-947"
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
updated: 2026-07-13
---

# Multi-Agent DRL-Based Coded Caching and Resource Allocation in UAV-Assisted Networks

## Citation

Tian, B., Wang, L., Chang, Z., Xu, L., & Fei, A. (2026). *Multi-Agent DRL-Based Coded Caching and Resource Allocation in UAV-Assisted Networks*. **IEEE Transactions on Wireless Communications, 25**, 931-947. DOI: 10.1109/TWC.2025.3587959.

## TL;DR

Uses erasure and regenerating codes to distribute emergency content across UAV caches, then applies a two-timescale hierarchical multi-agent P-DQN to choose coding/cache decisions, requester and repair pairing, and UAV motion.

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
