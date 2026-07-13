---
type: concept
title: "Gale-Shapley Matching"
tags: [matching, association, stable-matching, classical-algorithm]
related:
  - "[[lim-2021-uav-iov-contract-matching]]"
  - "[[multidimensional-contract-matching]]"
  - "[[matching-theory-for-resource-allocation]]"
  - "[[two-stage-decomposition]]"
  - "[[nabi-2025-jour-hierarchical-aerial]]"
created: 2026-05-29
updated: 2026-07-14
---

# Gale-Shapley Matching

A polynomial-time algorithm for **stable many-to-one matching**: given two sets of agents (e.g. ground users vs UAVs) with preference lists over the other side, returns a stable assignment — one in which no unmatched pair would mutually prefer each other to their current partners. Originally designed for college admissions; ubiquitous in resource-allocation problems with strategic preferences.

Used in [[nabi-2025-jour-hierarchical-aerial]] as the discrete-stage solver for GU-UAV association. Each GU prefers UAVs that minimize its task delay; each UAV prefers GUs that fit its remaining compute budget. The algorithm produces an association that no GU-UAV pair would deviate from unilaterally — useful in *non-cooperative* settings even when full cooperation is the system goal.

A standard tool in the [[matching-theory-for-resource-allocation]] family. Different from Hungarian algorithm (which finds optimal matching for additive cost) and from auction-based matching (which prices preferences instead of ranking).
