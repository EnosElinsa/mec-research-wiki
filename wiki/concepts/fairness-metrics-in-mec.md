---
type: concept
title: Fairness Metrics in MEC
tags: [fairness, metric, evaluation, mec, synthesis]
related:
  - "[[jains-fairness-index]]"
  - "[[theil-fairness-index]]"
  - "[[spatial-equity-index]]"
  - "[[equilibrium-efficiency-metric]]"
  - "[[service-experience-ratio]]"
  - "[[energy-balancing-uav]]"
  - "[[liu-2026-jppo-en-convntm]]"
  - "[[peng-2025-drudm-cfg]]"
  - "[[he-2023-fairness-3d-multiuav-maddpg]]"
  - "[[gao-2024-service-experience-cache-uav]]"
  - "[[wang-2026-llm-qos-multiuav-resource]]"
  - "[[lin-2025-energy-effective-ris-multiuav-coverage]]"
created: 2026-05-29
updated: 2026-07-11
---

# Fairness Metrics in MEC

A hub for the fairness vocabulary used across this corpus. "Fairness" in MEC papers means *equitable distribution* of some scarce quantity — service, coverage, delay, or energy — rather than a single agreed-upon formula. Different sources reach for different measures depending on what they want to equalize and how sharply they want to punish disparity.

## The measures in this wiki

| Measure | Page | What it equalizes | Direction |
|---|---|---|---|
| Jain's index $J(x)$ | [[jains-fairness-index]] | per-user allocation (general) | maximize, range $[1/n, 1]$ |
| Spatial equity index $f_n$ | [[spatial-equity-index]] | per-device cumulative visit counts | maximize, range $[1/D, 1]$ |
| Theil coefficient $T$ | [[theil-fairness-index]] | per-region service counts | minimize, range $[0, \ln N]$ |
| Service-experience ratio | [[service-experience-ratio]] | Jain over per-UE delay ÷ mean delay | couples fairness with latency |
| Energy balancing | [[energy-balancing-uav]] | per-UAV energy depletion | equalize (avoid early UAV death) |

The spatial equity index $f_n$ is a Jain-style index specialized to UAV visit counts, so it inherits Jain's scale- and population-independence.

## How the corpus actually uses them

- [[liu-2026-jppo-en-convntm]] embeds a Jain-style spatial equity index $f_n$ over per-device visit counts directly into its [[equilibrium-efficiency-metric|equilibrium efficiency metric]] $\Omega_n = \psi_n f_n / \kappa_n$, so fairness is multiplied against data-collection and energy terms rather than scored separately.
- [[peng-2025-drudm-cfg]] instead uses the [[theil-fairness-index|Theil coefficient]] over per-region service counts as a reward regularizer ($-\beta \bar{TL}(t)$), chosen because Theil decomposes into within- and between-group inequality — useful when dense and sparse post-disaster regions need different treatment.
- [[he-2023-fairness-3d-multiuav-maddpg]] frames its energy objectives "based on fairness among UAVs" and links [[jains-fairness-index]]; fairness here is an inter-UAV equity premise on the trajectory/offloading derivation.
- [[gao-2024-service-experience-cache-uav]] folds Jain's index over per-UE delay into a single [[service-experience-ratio]], coupling fairness with latency in one [[qoe-modeling-mec]] objective.
- [[wang-2026-llm-qos-multiuav-resource]] combines delay with Jain-style fairness in a weighted delay-fairness objective for LLM-teacher / MAPPO-student multi-UAV resource allocation.
- Energy-balancing work ([[energy-balancing-uav]]) treats fairness as equalizing depletion across UAVs rather than equalizing user-facing service — a related but distinct notion.

[[lin-2025-energy-effective-ris-multiuav-coverage]] uses throughput variance as a service-fairness diagnostic in RIS-assisted UAV communications; its fair-screening rule prevents repeatedly serving only high-channel-gain GTs.

## Why this matters for cross-paper comparison

The measures are not directly comparable: Jain and spatial-equity are maximized on $[1/N, 1]$, while Theil is minimized on $[0, \ln N]$, and Theil punishes outliers more sharply than Jain. A claim that one method is "fairer" than another only holds within the same metric and the same partition/population definition. Normalize before comparing, and note that Theil's value is sensitive to how regions are defined (coarse partitions can mask intra-region inequity).
