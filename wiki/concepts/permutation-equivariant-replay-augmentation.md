---
type: concept
title: "Permutation-Equivariant Replay Augmentation"
tags: [multi-agent-drl, replay-buffer, symmetry, data-augmentation]
related:
  - "[[qin-2023-symmetry-augmented-uav-isac]]"
  - "[[soft-actor-critic]]"
  - "[[masac]]"
  - "[[centralized-training-decentralized-execution]]"
created: 2026-07-12
updated: 2026-07-12
---

# Permutation-Equivariant Replay Augmentation

Permutation-equivariant replay augmentation generates additional multi-agent transitions by relabeling homogeneous agents consistently across state, action, next state, and every agent-indexed parameter. If the objective and reward are invariant to the labels, each relabeling describes the same physical decision with a different tensor ordering and can be stored as equivalent replay data.

[[qin-2023-symmetry-augmented-uav-isac]] applies this pattern to centralized [[soft-actor-critic|SAC]] for homogeneous UAVs. RSAC samples a fixed number of random label permutations, while ASAC decays the augmentation count during training, enriching replay early and improving replay-buffer de-correlation later.

The transformation is valid only when every permuted capability, constraint, channel, position, power, and reward term remains symmetric. Fixed heterogeneous UAV roles or capabilities can break the equivalence; relabeling only the observation tensor without the corresponding action and parameter dimensions does not produce a valid transition.
