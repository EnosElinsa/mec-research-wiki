---
type: concept
title: Coalition Formation Game
tags: [game-theory, coalition, cooperative-game, physical-layer-security]
related:
  - "[[chen-2024-three-party-hierarchical-game-pls]]"
  - "[[stackelberg-game]]"
  - "[[nash-equilibrium]]"
  - "[[physical-layer-security]]"
  - "[[friendly-jamming-uav]]"
  - "[[li-2026-jscfg-uav-grouping]]"
  - "[[joint-switch-coalition-formation-game]]"
created: 2026-05-31
updated: 2026-07-13
---

# Coalition Formation Game

A cooperative-game framework in which self-interested players partition themselves into **coalitions** to improve their individual payoffs, and the coalition structure can itself **merge and split** over time. A **hedonic** coalition game is the special case where each player's preference depends only on the members of its own coalition. Stability concepts (e.g. a stable partition where no player prefers to defect to another coalition) play the role that Nash equilibrium plays in non-cooperative games.

## In this wiki

[[chen-2024-three-party-hierarchical-game-pls]] uses a **dynamic trilateral coalition formation game (CFG)** among three [[physical-layer-security|PLS]] parties — legitimate users, eavesdroppers, and jammers — where jammers ([[friendly-jamming-uav|friendly jamming]] is the cooperative case) may ally with either the legitimate users or the eavesdroppers per time slot. The paper proves a stable coalition partition exists and proposes a **hedonic coalition selection and formation (HCSF)** algorithm to reach it, nested inside a [[stackelberg-game|hierarchical (Stackelberg-style)]] game whose equilibrium is then tracked over time with DRL.

[[li-2026-jscfg-uav-grouping]] adds a [[joint-switch-coalition-formation-game]] for heterogeneous UAV mission groups. Several UAVs can change memberships together, including across overlapping coalitions, so ordered-subtask type requirements remain feasible during topology reconfiguration.

## Contrast with other game forms

- **Non-cooperative ([[nash-equilibrium]], [[stackelberg-game]]):** players act individually; no binding agreements.
- **Coalition formation:** players form binding groups; the solution is a *partition*, and dynamics (merge/split) matter when the environment evolves.
