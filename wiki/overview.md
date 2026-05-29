---
type: overview
title: Project Overview
tags: [mec, research-wiki]
related:
  - "[[mobile-edge-computing]]"
  - "[[wang-2025-lae-network-survey]]"
  - "[[design-recipe-multi-uav-mec]]"
  - "[[constrained-multi-objective-evolutionary-algorithm]]"
---

# Overview

A long-running research wiki on **mobile edge computing (MEC)** broadly construed — task offloading, resource allocation, trajectory and infrastructure design, and intelligent decision-making algorithms across UAV, HAPS, LEO-satellite, vehicular, maritime, and terrestrial deployments. Open-ended scope; sources accumulate as the corpus grows.

## Snapshot

- **Curated sources:** 39 (12 initial + 14 from the first 2026-05-29 batch + 13 from the second 2026-05-29 batch) — see `wiki/index.md` for the type-grouped directory.
- **Concepts:** ~158 across MEC fundamentals, aerial architectures, DRL backbones, game theory, optimization techniques (classical + evolutionary + DRO), channel modeling, sensing + security, distributed inference, federation, generative-AI, and fairness/freshness metrics.
- **Hardware-validated sources:** 2 ([[sun-2024-asap-uav-swarm]] on 24 Jetson computers + 5 real UAVs; [[shao-2024-drl-antijamming-mec]] on Raspberry Pi/USRP). The rest are simulation-only.
- **Methodology / findings / thesis / synthesis pages** still anchored in the original UAV-MEC + DRL track ([[liu-2026-jppo-en-convntm]] follow-ups). Most synthesis pages are due for a refresh under the expanded corpus — see Open questions below.

## Tracks emerging from the corpus

| Track | Representative sources | Status |
|---|---|---|
| UAV-MEC + DRL | [[liu-2026-jppo-en-convntm]], [[peng-2025-drudm-cfg]], [[zhang-2025-ssac-mgi-heterogeneous-uav]], [[bi-2025-sg-mapg]], [[hao-2024-clp-multiuav-priority-offloading]] | Working thesis: [[hybrid-action-memory-augmented-drl-wins-uav-mec]] |
| Hierarchical aerial MEC (UAV+HAP) | [[nabi-2025-jour-hierarchical-aerial]], [[bao-2025-ddpg-video-offloading]], [[jia-2025-dro-uav-hap-mec]], [[peng-2025-drudm-cfg]], [[song-2024-mol-aoi-energy]] | 5+ sources; synthesis page exists |
| **SAGIN / satellite offloading** | [[gao-2024-sagin-perception-offloading]], [[chen-2024-thoas-traffic-aware-sagin]], [[chen-2024-ulse-game]], [[han-2024-sagin-fl-handover]] | 4 sources, new in this batch — ready for a synthesis |
| **CMOP / evolutionary UAV-MEC** (Peng/Huang lineage) | [[peng-2022-cmop-uav-path-planning]] (seed), [[peng-2024-energy-time-uav-its]], [[huang-2023-mu-aec-task-energy]], [[huang-2025-cmop-dispersed-computing]], [[wu-2026-terrain-aware-uav-mec]], [[xie-2026-uav-multisource-fusion]] | 6 sources — lineage synthesis exists |
| Vehicular-MEC | [[zhang-2025-mcma-task-migration]], [[ma-2025-pdqn-vehicular-mec]], [[xie-2026-uav-multisource-fusion]] | 3 sources, no thesis yet |
| Maritime MEC | [[wang-2026-aerial-marine-msar]], [[liu-2025-haps-uav-maritime-iot]] | 2 sources |
| Trust / security / federation | [[mao-2025-bcsa-frl]], [[qin-2025-bcuav-masac]], [[han-2024-sagin-fl-handover]] | 3 sources; FL-over-SAGIN added |
| **Anti-jamming / security-DRL** | [[shao-2024-drl-antijamming-mec]] | 1 source, new — hardware-validated |
| **UAV-swarm collaborative computing** | [[sun-2024-asap-uav-swarm]], [[li-2025-stochastic-game-uav-swarm]] | 2 sources, new in this batch |
| ISAC | [[benaya-2025-aerial-isac-haps]], [[jiang-2025-isac-lae-overview]] | 2 sources |
| Spectrum / governance / architecture | [[wang-2025-uav-swarm-stackelberg]], [[wang-2025-lae-network-survey]], [[hsu-2025-drl-hues-hap-noma]] | Foundation papers; anchor the LAE / SAGIN umbrella |
| **Game-theoretic offloading** | [[chen-2024-ulse-game]], [[li-2025-stochastic-game-uav-swarm]], [[wang-2025-uav-swarm-stackelberg]], [[bi-2025-sg-mapg]] | 4 sources spanning potential / stochastic / Stackelberg games |
| **Generative-AI MEC** | [[ye-2025-aigc-diffusion-contract]], [[peng-2025-drudm-cfg]] | 2 sources using diffusion models as decision generators |
| Energy efficiency & WPT | [[zhu-2025-lycnn-drl-wpt-mec]], [[wu-2025-iopo-irs-uav-thz-mec]] | 2 sources; IRS/THz added |
| Generic offloading techniques | [[hao-2025-priority-aware-task-driven-co]], [[zhao-2025-traj-offload-cache-migration]], [[gao-2024-service-experience-cache-uav]] | Priority, caching/migration, fairness |

## Cross-cutting observations

(Originally drawn from the first 12 sources; updated where the new batch changes the picture.)

1. **Lyapunov + DRL hybrids are still common** for long-term-constrained per-slot MEC optimization ([[qin-2025-bcuav-masac]], [[zhu-2025-lycnn-drl-wpt-mec]]). The new batch reinforces this — see the alternating-optimization (AO + SDR + SCA) version in [[benaya-2025-aerial-isac-haps]].
2. **CTDE remains the default multi-agent paradigm** ([[peng-2025-drudm-cfg]], [[zhang-2025-mcma-task-migration]], [[zhang-2025-ssac-mgi-heterogeneous-uav]], [[qin-2025-bcuav-masac]]).
3. **Stackelberg + matching keeps showing up** ([[wang-2025-uav-swarm-stackelberg]], [[bi-2025-sg-mapg]], [[wang-2026-aerial-marine-msar]] adds many-to-one matching, [[nabi-2025-jour-hierarchical-aerial]] adds Gale-Shapley).
4. **Two-stage decomposition (discrete-then-continuous) is a recurring solver pattern** — [[wang-2026-aerial-marine-msar]], [[nabi-2025-jour-hierarchical-aerial]], [[jia-2025-dro-uav-hap-mec]]. Compare with the **joint hybrid-action** family ([[liu-2026-jppo-en-convntm|j-PPO]], [[ma-2025-pdqn-vehicular-mec|P-DQN]]). See [[two-stage-decomposition]].
5. **Fairness metrics fragment** — Jain, Theil, and now energy-balancing variance ([[huang-2023-mu-aec-task-energy]], [[nabi-2025-jour-hierarchical-aerial]]) and completion-time difference ([[peng-2024-energy-time-uav-its]]). A side-by-side comparison page would be useful.
6. **CSI uncertainty is now an explicit concern** in three different ways: distributionally robust ([[jia-2025-dro-uav-hap-mec]]), known-route side-step ([[wang-2026-aerial-marine-msar]]), and terrain-aware geometric ([[wu-2026-terrain-aware-uav-mec]]).
7. **DRL is not the only game in town.** The new batch makes the **evolutionary / classical** branch comparable in size to the DRL branch. A "DRL-vs-evolutionary-vs-classical" synthesis is now justified.
8. **Most papers are still simulation-only.** The wiki has 0 hardware-validated curated sources. Worth keeping in mind for any thesis claim.

## Open questions

- [[query-real-world-validation-of-jppo-en-convntm]] — sim-to-real transfer.
- [[query-does-en-convntm-generalize-beyond-uav-mec]] — generalization of memory-augmented encoders.
- (More to come as additional sources highlight new gaps. The expanded corpus opens questions like "when DRO beats DRL for CSI uncertainty," "video vs cooperative-perception offloading shape," and "the right granularity for the discrete-then-continuous decomposition" — pending synthesis.)

## Where to go next

- `wiki/index.md` — full type-grouped page directory.
- `wiki/log.md` — reverse-chronological activity log.
- `raw/sources/` — drop new papers here for the next curation pass.
