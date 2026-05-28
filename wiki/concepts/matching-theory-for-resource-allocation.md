---
type: concept
title: Matching Theory for Resource Allocation
tags: [matching, optimization, assignment, mechanism-design]
related:
  - "[[stackelberg-game]]"
  - "[[wang-2025-uav-swarm-stackelberg]]"
created: 2026-05-28
updated: 2026-05-28
---

# Matching Theory for Resource Allocation

Mathematical framework (Gale–Shapley, Roth–Sotomayor) for pairing agents from two disjoint sets — typically buyers/sellers, students/schools, users/resources — under each side's preferences over the other.

## Properties of interest in MEC

- **Stability.** No two unmatched agents prefer each other to their current matches. The deferred-acceptance algorithm (Gale–Shapley) achieves stable matching in polynomial time.
- **Pareto efficiency.** No re-match makes someone better off without making someone else worse off.
- **Strategy-proofness.** Agents have no incentive to misreport preferences.

## Matching variants

| Variant | Setup | When it appears |
|---|---|---|
| **One-to-one** | Each agent matches with at most one peer | Pairing UAV-to-charging-station, U2U-to-U2B |
| **Many-to-one** | One side accepts multiple matches | Multiple users to one MEC server |
| **Many-to-many** | Both sides multi-match | Federated learning round assignments |
| **With externalities** | Agent utility depends on others' matches too | Spectrum sharing with interference |

## In this wiki

[[wang-2025-uav-swarm-stackelberg]] uses many-to-one matching (multiple U2U links to a single U2B sub-band) as the second layer atop the [[stackelberg-game]] pricing layer. The combination is increasingly common in MEC papers — Stackelberg fixes the *price*, matching fixes the *assignment*.

## Caveats

- Matching with externalities (interference, congestion) may not be NP-hard but rarely admits a closed-form stable solution. Approximation / iterative-deferred-acceptance variants are typical.
- "Preferences" in the abstract framework usually translate into utility / latency / energy functions whose values must be computable up front. In dynamic MEC, this is non-trivial.
