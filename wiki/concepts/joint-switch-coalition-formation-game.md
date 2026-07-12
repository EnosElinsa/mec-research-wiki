---
type: concept
title: "Joint-Switch Coalition Formation Game"
tags: [game-theory, coalition-formation, heterogeneous-uav, dynamic-grouping, topology-optimization]
related:
  - "[[li-2026-jscfg-uav-grouping]]"
  - "[[coalition-formation-game]]"
  - "[[potential-game]]"
  - "[[nash-equilibrium]]"
  - "[[heterogeneous-uav-fleet]]"
created: 2026-07-13
updated: 2026-07-13
---

# Joint-Switch Coalition Formation Game

A joint-switch coalition formation game permits several players to change coalition memberships together. Coordinated moves preserve group-level feasibility constraints that a single-player switch could violate, and can span multiple or overlapping coalitions.

[[li-2026-jscfg-uav-grouping]] applies the mechanism to heterogeneous UAV mission groups with minimum per-type requirements for ordered search, lock, and attack subtasks. Its common-improvement preference accounts for switch participants, overlapping members, and other affected coalition members before accepting the largest positive utility gain.

This is a constrained specialization of [[coalition-formation-game]]. The paper establishes an exact [[potential-game]] characterization for abundant-resource single-node switching and argues finite joint improvement reaches a [[nash-equilibrium|Nash-stable]] coalition structure in balanced or insufficient-resource cases. The guarantee applies to topology regrouping under fixed paths and the paper's negligible-overhead assumptions.
