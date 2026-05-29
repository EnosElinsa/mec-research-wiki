---
type: synthesis
title: "Maritime MEC architectures"
tags: [synthesis, maritime-mec, offloading, comparison]
related:
  - "[[wang-2026-aerial-marine-msar]]"
  - "[[liu-2025-haps-uav-maritime-iot]]"
  - "[[wang-2025-double-edge-samin]]"
  - "[[zhang-2025-three-tier-maritime-offloading]]"
  - "[[zhang-2024-dlrl-maritime-usv]]"
  - "[[you-2025-uncertain-maritime-hasac]]"
  - "[[wang-2024-twotier-satellite-marine]]"
  - "[[maritime-mec]]"
  - "[[three-tier-cloud-edge-end]]"
  - "[[maritime-three-tier-energy-saving]]"
created: 2026-05-30
updated: 2026-05-30
---

# Maritime MEC architectures

Seven curated sources target the maritime setting — vessels / maritime wireless devices (MWDs) far from terrestrial base stations, served by some mix of UAV, HAPS, USV, offshore base station (OBS), and LEO satellite. This page maps the tiering choices and the solver families.

## Roster

| Source | Venue / year | Tiers | Core method | Distinctive knob |
|---|---|---|---|---|
| [[wang-2026-aerial-marine-msar]] | TCCN 2026 | UAV + HAPS + MASS (3) | Matching + convex + PGD (JCORA) | Search-and-rescue; known-route side-step of CSI |
| [[zhang-2025-three-tier-maritime-offloading]] | TVT 2025 | MWD + OBS + LEO (3) | MINLP decomposition (4 subproblems) | 39.3% energy saving ([[maritime-three-tier-energy-saving]]) |
| [[wang-2025-double-edge-samin]] | TVT 2025 | UAV + LEO (2 edges) | AO + layered decomposition | Double-edge (air + space) |
| [[wang-2024-twotier-satellite-marine]] | IoT-J 2024 | Satellite + marine (2) | Hybrid Stackelberg-Bargaining game | NOMA/FDMA mode choice |
| [[liu-2025-haps-uav-maritime-iot]] | TMC 2025 | HAP + UAV + vessel (3) | Multi-verse optimizer + step-wise | HAP-as-backhaul, UAV multicast, vessel unicast |
| [[you-2025-uncertain-maritime-hasac]] | TVT 2025 | AAV + vessel | Lyapunov + Markov game + HASAC | Uncertain maritime environment |
| [[zhang-2024-dlrl-maritime-usv]] | TVT 2024 | USV mobile edge | Dual-layer RL (DDPG / Q-learning) | USV deployment + offloading |

## Tiering patterns

- **Three-tier (aerial + sea-surface + space)** is the dominant shape: [[wang-2026-aerial-marine-msar]] (UAV+HAPS+MASS), [[zhang-2025-three-tier-maritime-offloading]] (MWD+OBS+LEO), [[liu-2025-haps-uav-maritime-iot]] (HAP+UAV+vessel). See [[three-tier-cloud-edge-end]].
- **Two-edge (air + space)**: [[wang-2025-double-edge-samin]] and [[wang-2024-twotier-satellite-marine]] drop the sea-surface compute tier and split work between an aerial edge and a satellite edge.
- **Single mobile-edge platform**: [[zhang-2024-dlrl-maritime-usv]] puts the edge server on a USV; [[you-2025-uncertain-maritime-hasac]] uses AAVs cooperating with vessels.

## Solver split (mirrors the corpus-wide divide)

- **Classical / convex / metaheuristic**: [[wang-2026-aerial-marine-msar]] (matching + convex + PGD), [[zhang-2025-three-tier-maritime-offloading]] (MINLP → 4 convex/dual subproblems), [[wang-2025-double-edge-samin]] (AO + layered), [[liu-2025-haps-uav-maritime-iot]] (multi-verse optimizer).
- **Game-theoretic**: [[wang-2024-twotier-satellite-marine]] (hybrid Stackelberg-Bargaining) — see [[game-theoretic-offloading-formulations]].
- **DRL**: [[zhang-2024-dlrl-maritime-usv]] (dual-layer RL), [[you-2025-uncertain-maritime-hasac]] (Lyapunov + heterogeneous-agent SAC).

The maritime track is **classical-solver-heavy** relative to the UAV-MEC track — four of seven are convex/metaheuristic. The reason is structural: maritime mobility is slow and routes are often known (shipping lanes), which lets these sources side-step the CSI-uncertainty that pushes the aerial track toward DRL or DRO.

## Distinctive maritime constraints

1. **Known/predictable routes.** [[wang-2026-aerial-marine-msar]] explicitly exploits known vessel routes to avoid modeling CSI uncertainty — a maritime-specific simplification not available to the UAV track.
2. **Backhaul scarcity is acute.** Vessels are far from shore, so the satellite/HAP backhaul link is the dominant bottleneck in every two/three-tier design.
3. **Energy is the headline objective** more often than latency — [[zhang-2025-three-tier-maritime-offloading]] optimizes system energy explicitly; MWDs/vessels are energy-constrained.

## Gaps

- **No security/trust source in the maritime track** — unlike the UAV track, no maritime source addresses jamming, blockchain, or zero-trust, despite maritime networks being exposed.
- **CSI uncertainty is mostly side-stepped** (known routes) rather than handled robustly — the maritime analog of [[jia-2025-dro-uav-hap-mec]]'s DRO approach is absent.
- **No head-to-head between the classical-heavy maritime solvers and a DRL controller** on the same maritime benchmark.
