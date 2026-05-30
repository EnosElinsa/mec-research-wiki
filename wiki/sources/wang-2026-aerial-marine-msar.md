---
type: source
title: "Computation-Efficient Aerial-Marine Integrated Networks for Search and Rescue via Cooperative HAPS, UAVs, and MASSs"
authors: ["Zhen Wang", "Bin Lin", "Qiang Ye"]
year: 2026
url: "https://doi.org/10.1109/TCCN.2025.3642113"
venue: "IEEE Transactions on Cognitive Communications and Networking"
tags: [maritime, msar, haps, uav, mass, mec, matching, two-stage-optimization, jcora]
related:
  - "[[maritime-mec]]"
  - "[[high-altitude-platform-station]]"
  - "[[matching-theory-for-resource-allocation]]"
  - "[[hierarchical-aerial-mec]]"
  - "[[two-stage-decomposition]]"
  - "[[peng-2025-drudm-cfg]]"
created: 2026-05-29
updated: 2026-05-29
---

# Computation-Efficient Aerial-Marine Integrated Networks for Search and Rescue via Cooperative HAPS, UAVs, and MASSs

## Citation

Wang, Z., Lin, B., & Ye, Q. (2026). *Computation-Efficient Aerial-Marine Integrated Networks for Search and Rescue via Cooperative HAPS, UAVs, and MASSs*. **IEEE Transactions on Cognitive Communications and Networking**. DOI: 10.1109/TCCN.2025.3642113.

## TL;DR

A maritime search-and-rescue (MSAR) MEC architecture that combines **three** edge tiers — surveillance UAVs (sensors), maritime autonomous surface ships (MASSs, near-surface compute), and a HAPS (long-endurance high-altitude compute). UAVs generate computation-intensive tasks and offload them to either an MASS or the HAPS via multi-access. The authors minimize **system computation overhead (CO)** = weighted sum of completion time + energy.

The MINLP is decomposed into four subproblems and solved by the **JCORA** algorithm:

| Stage | Subproblem | Method |
|---|---|---|
| I | Edge-server selection (UAV → HAPS or MASS) | many-to-one matching |
| II.a | UAV transmit power allocation | quasi-convex |
| II.b | Edge computing resource allocation | projected gradient descent |
| II.c | Local computing resource allocation | convex |

## Why this matters

This is the wiki's first **MSAR / maritime** entry. Two architectural innovations:

1. **Three computation tiers including a sea-surface tier (MASS)** — distinct from the wiki's previous land/air mix. MASSs sit between UAVs and HAPS in compute capacity and proximity.
2. **Both `UAV → HAPS` and `UAV → MASS` offloading routes** are jointly optimized. Most prior aerial-MEC papers use only one of these.

Compare with [[peng-2025-drudm-cfg]] (HAPS + UAV for **post-disaster ground**) — same hierarchical-aerial pattern, different physical layer (Rician fading on air-to-sea) and a non-DRL solver.

## Channel model highlights

- **UAV → MASS:** Rician fading with explicit shadow fading X_σ and a "ducting" propagation parameter F (sea-surface path-loss exponent < 2).
- **UAV → HAPS:** sigmoid-LoS-probability over elevation angle (now standard for HAPS papers — see also [[hsu-2025-drl-hues-hap-noma]]).

The MASS model is novel for the wiki: **historical / pre-measured CSI** is assumed available because MASSs travel along established shipping routes. This is a clever way to side-step the imperfect-CSI problem that [[jia-2025-dro-uav-hap-mec]] solves with DRO.

## Findings

- JCORA reduces system CO vs benchmarks (random matching, random power, etc.).
- Matching-based server selection beats greedy because greedy ignores the rejection structure of multi-UAV-to-MASS contention.
- HAPS is preferred for tasks with relaxed latency budgets (long propagation) but heavy compute; MASS for tight-latency tasks.

## Limitations

- Single HAPS, deterministic CSI, MASS positions known and quasi-stationary during a slot.
- No DRL — all subproblems are solved by classical methods, which makes per-slot replanning fast but loses the ability to learn from environmental drift.
- Energy on the HAPS / MASS side is treated as unbounded; the wiki's other HAPS-side energy paper [[hsu-2025-drl-hues-hap-noma]] disagrees.

## Cross-link with related sources

- **Maritime track:** a core member of the maritime MEC track. Related to [[liu-2025-haps-uav-maritime-iot]] (HAP-UAV maritime IoT).
- **Hierarchical aerial MEC:** alongside [[peng-2025-drudm-cfg]], [[nabi-2025-jour-hierarchical-aerial]], [[bao-2025-ddpg-video-offloading]].
- **Solver:** classical decomposition (matching + convex + PGD) rather than DRL — same family as [[bi-2025-sg-mapg]] and [[wang-2025-uav-swarm-stackelberg]].

## Raw artifacts

- `raw/sources/Computation-Efficient Aerial-Marine Integrated Networks for Search and Rescue via Cooperative HAPS/full.md`
