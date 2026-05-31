---
type: synthesis
title: "The SAGIN / satellite-offloading landscape"
tags: [synthesis, sagin, leo-satellite, offloading, comparison]
related:
  - "[[gao-2024-sagin-perception-offloading]]"
  - "[[chen-2024-thoas-traffic-aware-sagin]]"
  - "[[chen-2024-ulse-game]]"
  - "[[han-2024-sagin-fl-handover]]"
  - "[[qin-2025-matd3-noma-queue-sagin]]"
  - "[[wang-2024-hybrid-oma-noma-sagin]]"
  - "[[zhai-2023-fedleo-decentralized-fl]]"
  - "[[mao-2024-ntn-hierarchical-caching-cav]]"
  - "[[space-air-ground-integrated-network]]"
  - "[[leo-satellite-edge-computing]]"
  - "[[non-terrestrial-network]]"
  - "[[fedleo-delay-accuracy-tradeoff]]"
created: 2026-05-30
updated: 2026-06-02
---

# The SAGIN / satellite-offloading landscape

A cluster of curated sources put a satellite (usually LEO) into the offloading hierarchy; the eight mapped below split cleanly by **what the satellite is for** and **what solver shape the per-slot problem takes**. This page maps those eight onto those axes and calls out the shared assumptions and gaps.

## Roster

| Source | Venue / year | Satellite role | Core method | Distinctive knob |
|---|---|---|---|---|
| [[gao-2024-sagin-perception-offloading]] | JSAC 2024 | Compute + backhaul tier | Lyapunov + DDPG + DQN + SGHS | Perception (mmWave radar + YOLOv7) feeds the DRL state |
| [[chen-2024-thoas-traffic-aware-sagin]] | JSAC 2024 | Slicing-enabled offload tier | Probsparse-attention prediction + distilled PPO | Traffic prediction drives slicing |
| [[chen-2024-ulse-game]] | TMC 2024 | LEO compute tier | Potential game (LUTO-Game / JULTO) | Distributed best-response, no central solver |
| [[han-2024-sagin-fl-handover]] | JSAC 2024 | FL participant + relay | Federated learning + adaptive inter-layer offload | Seamless satellite handover during training |
| [[qin-2025-matd3-noma-queue-sagin]] | TVT 2025 | Backhaul tier | Lyapunov + MATD3 | NOMA + queue-aware AAV 3D trajectory |
| [[wang-2024-hybrid-oma-noma-sagin]] | TVT 2024 | Access/compute tier | SCA + Lagrange + DQN | Hybrid OMA/NOMA mode selection |
| [[zhai-2023-fedleo-decentralized-fl]] | TMC 2023 | FL aggregation ring | Decentralized FL + greedy offload | Server-free ring aggregation |
| [[mao-2024-ntn-hierarchical-caching-cav]] | JSAC 2024 | Caching tier (LEO+UAV) | DM-ACO + MADRL-HCAU | Content caching for connected vehicles |

## What the satellite is *for* (three roles)

1. **Compute / backhaul tier** — the satellite is a deeper offload destination than the aerial layer ([[gao-2024-sagin-perception-offloading]], [[qin-2025-matd3-noma-queue-sagin]], [[wang-2024-hybrid-oma-noma-sagin]], [[chen-2024-ulse-game]]). The aerial layer (UAV/AAV) collects and partially processes; the LEO link is the friction.
2. **Federated-learning fabric** — the constellation *is* the distributed training system ([[zhai-2023-fedleo-decentralized-fl]], [[han-2024-sagin-fl-handover]]). Here the offloading question is "which satellite trains/aggregates what", not "where does a task run". See [[fedleo-delay-accuracy-tradeoff]].
3. **Caching tier** — the satellite stores content closer to mobile consumers ([[mao-2024-ntn-hierarchical-caching-cav]]). Offloading becomes a content-placement problem.

## Solver-shape split

- **Lyapunov + DRL** dominates the per-slot compute-tier problems ([[gao-2024-sagin-perception-offloading]], [[qin-2025-matd3-noma-queue-sagin]]) — long-term queue/energy constraints decoupled into per-slot drift-plus-penalty, then a DRL actor. Consistent with the corpus-wide pattern noted in [[drl-backbones-across-uav-mec-sources]].
- **Game-theoretic / distributed** appears once ([[chen-2024-ulse-game]]), trading a global optimum for decentralized best-response convergence — useful when no central SAGIN controller exists. See [[game-theoretic-offloading-formulations]].
- **Convex + light DRL** ([[wang-2024-hybrid-oma-noma-sagin]]: SCA + Lagrange for the continuous block, DQN for mode selection).
- **Prediction-first** ([[chen-2024-thoas-traffic-aware-sagin]]: predict traffic, then a distilled lightweight PPO acts) — the only source that treats the satellite link's time-variability as a forecasting problem.

## Shared assumptions worth questioning

1. **LEO coverage windows are mostly modeled as availability indicators**, not as a hard scheduling constraint — only [[zhai-2023-fedleo-decentralized-fl]] (ring topology, [[walker-star-constellation]]) and [[chen-2024-ulse-game]] ([[leo-satellite-coverage-time]]) treat the orbital geometry as first-class. The compute-tier sources tend to abstract the satellite as "a slower link to more compute".
2. **Backhaul capacity is the implicit bottleneck** but is rarely the optimized variable — most sources optimize the aerial layer and treat the satellite link as a fixed-rate pipe.
3. **Energy of the satellite itself is unbounded** in every source; only the aerial/ground layers have energy budgets.

## Gaps

- **No head-to-head between the compute-tier solver families** (Lyapunov+DRL vs game-theoretic vs convex) on a common SAGIN benchmark.
- **FL-over-SAGIN and compute-offloading-over-SAGIN are studied separately** — no source co-optimizes a training workload and an inference/offloading workload over the same constellation.
- **Security appears only in the FL sources** (poisoning robustness); the compute-tier offloading sources assume honest satellites. Cross-link with [[bcsa-frl-vs-bc-uav-masac]] for the threat-model angle.

## Open question promoted from this synthesis

[[query-when-does-dro-beat-drl-for-csi-uncertainty]] — the SAGIN compute-tier sources all assume known or learnable channel statistics; none uses the distributionally-robust approach that the hierarchical-aerial track has started adopting.
