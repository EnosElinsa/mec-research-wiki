---
type: finding
title: Distributed collaborative beamforming cuts LEO handover frequency ~30% at similar uplink rate
source: "[[li-2024-emodrl-ground-space-cb]]"
confidence: medium
replicated: null
tags: [collaborative-beamforming, leo-satellite, handover, multi-objective, non-terrestrial-network]
related:
  - "[[li-2024-emodrl-ground-space-cb]]"
  - "[[collaborative-beamforming]]"
  - "[[collaborative-beamforming-in-aerial-mec]]"
  - "[[seamless-handover]]"
  - "[[leo-satellite-edge-computing]]"
  - "[[evolutionary-reinforcement-learning]]"
created: 2026-06-01
updated: 2026-06-01
---

# Distributed collaborative beamforming cuts LEO handover frequency ~30% at similar uplink rate

In [[li-2024-emodrl-ground-space-cb]], energy-sensitive ground terminals with coarse antennas cooperate as a **distributed collaborative beamforming (DCB)** virtual antenna array to reach a LEO satellite on the uplink. The headline quantified result is stated in the abstract:

> the proposed algorithm lets terminals that individually cannot meet the uplink-rate threshold "achieve efficient direct uplink transmission, and save 30% handover frequency with a similar uplink achievable rate compared with the rate greedy method" (parse abstract).

## Mechanism

The work optimizes three conflicting objectives — uplink achievable rate, total terminal energy, and **satellite switching (handover) frequency** — as a long-term MOP, reformulated into an action-space-reduced, scale-universal MOMDP and solved by an **Evolutionary Multi-Objective DRL (EMODRL)** algorithm that masks low-value actions to speed convergence. Because EMODRL returns a *set* of trade-off policies in one run, the 30% figure is the handover-favoring policy measured against a rate-greedy baseline at matched uplink rate, not a single forced operating point. Reducing switching directly mitigates the **ping-pong handover** problem that plagues fast-moving LEO links.

## Caveats

- Single-paper, simulation-only result → `confidence: medium`. The comparison is specifically against the "rate greedy method"; the margin against other baselines is figure-derived and not asserted here.
- "Similar uplink achievable rate" is the paper's qualifier — the 30% saving is conditioned on matched rate, so it is a trade-off-curve point, not a free improvement.
- This is the clearest quantified collaborative-beamforming result in the corpus; the sibling CB sources ([[sun-2025-emoppo-vlh-aerial-cb]], [[li-2024-emssa-uav-swarm-vaa]], [[sun-2024-imssa-uav-secure-cb]], [[zhang-2024-gdmtd3-aerial-secure-cb]]) report IGD/hypervolume or "outperforms benchmarks" claims whose magnitudes are figure-derived and indicative.

## Relation to the corpus

Anchors the quantified end of the [[collaborative-beamforming-in-aerial-mec]] synthesis and ties the CB thread to the NTN/LEO [[sagin-satellite-offloading-landscape|satellite-offloading landscape]] via the shared handover/[[seamless-handover]] concern. It is the only CB source whose extra objective is handover frequency rather than secrecy or completion time.
