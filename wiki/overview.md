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

- **Curated sources:** 89 (12 initial + 14 from the first 2026-05-29 batch + 13 from the second 2026-05-29 batch + 43 from the third 2026-05-29 batch + 7 from batch 1/8 of the 2026-05-31 multi-batch run) — see `wiki/index.md` for the type-grouped directory.
- **Concepts:** 180 across MEC fundamentals, aerial architectures, DRL backbones, game theory, optimization techniques (classical + evolutionary + DRO), channel modeling, sensing + security, distributed inference, federation, generative-AI, and fairness/freshness metrics — including a [[fairness-metrics-in-mec]] synthesis hub. Batch 1/8 added [[collaborative-beamforming]], [[coalition-formation-game]], [[cellular-connected-uav]], and [[uav-data-collection]].
- **Entities:** 48 author pages + [[pytorch]] (49 entity pages total). Batch 1/8 added [[boxiong-wang]] and [[hui-kang]] (both Jilin University, [[geng-sun]] aerial-MEC cluster, 2 sources each, email-confirmed). The 2026-05-31 pass added 8 affiliation-verified authors ([[shuang-liang]]; [[weifeng-zhong]], [[shengli-xie]]; [[qiqi-xie]]; [[nei-kato]], [[jiadai-wang]], [[yijie-xun]], [[yangbo-liu]]). The 2026-05-30 pass added 5 confirmed authors ([[ying-chen]], [[jie-xu]], [[fuhong-song]], [[yong-wang]], [[wei-zhang]]); one recurring "Nan Zhao" name remains deferred as a genuine namesake (two different institutions). A second deferral was logged in batch 1/8: a "Qingqing Wu" in the 2019 UAV tutorial is listed at NUS, not SJTU, so it was not merged into [[qingqing-wu]]. Earlier passes confirmed the 21 batch-4 authors (NUAA, Jilin/NTU, Dalian-Maritime, NWPU, NCEPU, SCAU clusters + cross-cutting seniors).
- **Analytical layer:** 12 findings, 10 synthesis pages, 4 comparisons, 4 queries, 2 methodology pages, 1 thesis — the 2026-05-31 pass added an ACBFT consensus-throughput finding ([[acbft-throughput-increase]]) and a blockchain-on-edge trust-layer synthesis ([[blockchain-on-edge-trust-layer]]); the 2026-05-30 pass added SAGIN / ISAC / maritime synthesis, a game-theoretic-formulations comparison, the AO+SDR+SCA methodology, and DRO-vs-DRL / rich-media-offloading queries.
- **References:** mined citation database ([[reference-database]], 2981 unique refs) + scout [[recommendations]] for not-yet-curated papers.
- **Hardware-validated sources:** 2 ([[sun-2024-asap-uav-swarm]] on 24 Jetson computers + 5 real UAVs; [[shao-2024-drl-antijamming-mec]] on Raspberry Pi/USRP). The rest are simulation-only.
- **Earliest sources:** the corpus now reaches back to foundational works — the 2017 MEC communication survey [[mao-2017-mec-survey-communication]] and the 2019 EUAGame [[he-2019-euagame-user-allocation]] / ToDeTaS [[wang-2019-todetas-deployment-scheduling]] papers anchor the historical baseline.
- **Analytical layer now spans the whole corpus.** The 2026-05-30 pass broadened the derived pages beyond the original UAV-MEC + DRL track: track-level synthesis for SAGIN/satellite ([[sagin-satellite-offloading-landscape]]), ISAC/sensing ([[isac-sensing-in-aerial-mec]]), and maritime ([[maritime-mec-architectures]]); a game-theoretic-formulations comparison ([[game-theoretic-offloading-formulations]]); the cross-source AO+SDR+SCA methodology ([[ao-sdr-sca-convex-pipeline]]); and findings tied to specific parses across maritime, satellite-FL, swarm-inference, and secure-MEC sources. The [[liu-2026-jppo-en-convntm]]-anchored thesis ([[hybrid-action-memory-augmented-drl-wins-uav-mec]]) remains scoped to that framework, as intended.

## Tracks emerging from the corpus

| Track | Representative sources | Status |
|---|---|---|
| Foundational surveys / overviews | [[mao-2017-mec-survey-communication]], [[wang-2025-lae-network-survey]], [[khoramnejad-2025-gai-wireless-optimization-survey]], [[meng-2024-uav-isac-overview]], [[du-2024-distributed-foundation-models-6g]], [[zeng-2019-uav-comm-tutorial-5g]] | 6 anchors spanning MEC, LAE, GAI, ISAC, 6G-FMs, UAV-comms |
| UAV-MEC + DRL | [[liu-2026-jppo-en-convntm]], [[peng-2025-drudm-cfg]], [[zhang-2025-ssac-mgi-heterogeneous-uav]], [[bi-2025-sg-mapg]], [[hao-2024-clp-multiuav-priority-offloading]], [[zhao-2022-matd3-multiuav-ec-offloading]], [[chang-2022-marl-multiuav-trajectory]], [[he-2023-fairness-3d-multiuav-maddpg]] | Working thesis: [[hybrid-action-memory-augmented-drl-wins-uav-mec]] |
| Classical/convex optimization UAV-MEC | [[zhang-2019-uav-iot-comp-comm]], [[yu-2020-uav-ec-collaborative-offloading]], [[liu-2022-miso-uav-mec-trajectory]], [[yang-2022-stochastic-uav-mec-lyapunov]] | Large new SCA/AO/Lyapunov sub-corpus |
| Hierarchical aerial MEC (UAV+HAP) | [[nabi-2025-jour-hierarchical-aerial]], [[bao-2025-ddpg-video-offloading]], [[jia-2025-dro-uav-hap-mec]], [[jia-2022-hierarchical-aerial-matching]], [[kang-2023-mappo-hierarchical-aerial]], [[chen-2023-dotora-air-ground-online]] | 6+ sources; matching/DRL/DRO/online variants |
| SAGIN / satellite offloading & federation | [[gao-2024-sagin-perception-offloading]], [[chen-2024-thoas-traffic-aware-sagin]], [[chen-2024-ulse-game]], [[han-2024-sagin-fl-handover]], [[qin-2025-matd3-noma-queue-sagin]], [[wang-2024-hybrid-oma-noma-sagin]], [[zhai-2023-fedleo-decentralized-fl]], [[mao-2024-ntn-hierarchical-caching-cav]] | Large; ready for refreshed synthesis |
| CMOP / evolutionary UAV-MEC (Peng/Huang lineage) | [[peng-2022-cmop-uav-path-planning]], [[peng-2024-energy-time-uav-its]], [[huang-2023-mu-aec-task-energy]], [[huang-2025-cmop-dispersed-computing]], [[wu-2026-terrain-aware-uav-mec]], [[xie-2026-uav-multisource-fusion]], [[wang-2019-todetas-deployment-scheduling]], [[wang-acve-constraint-violation-cmop]] | Lineage synthesis exists; new DE + CVE methods sources |
| Vehicular MEC | [[zhang-2025-mcma-task-migration]], [[ma-2025-pdqn-vehicular-mec]], [[xie-2026-uav-multisource-fusion]], [[sun-2023-bargain-match-vec]] | 4 sources (DRL + game-theoretic) |
| Maritime MEC | [[wang-2026-aerial-marine-msar]], [[liu-2025-haps-uav-maritime-iot]], [[wang-2025-double-edge-samin]], [[zhang-2025-three-tier-maritime-offloading]], [[zhang-2024-dlrl-maritime-usv]], [[you-2025-uncertain-maritime-hasac]], [[wang-2024-twotier-satellite-marine]] | 7 sources — now a major track (optimization / DRL / game theory) |
| Trust / security / federation | [[mao-2025-bcsa-frl]], [[qin-2025-bcuav-masac]], [[han-2024-sagin-fl-handover]], [[wang-2025-acbft-uav-consensus]] | BFT-consensus layer added; [[blockchain-on-edge-trust-layer]] synthesis maps the 3 blockchain sources |
| Anti-jamming / security-DRL | [[shao-2024-drl-antijamming-mec]] | 1 source — hardware-validated |
| UAV-swarm collaborative computing | [[sun-2024-asap-uav-swarm]], [[li-2025-stochastic-game-uav-swarm]], [[zhang-2024-gdmtd3-aerial-secure-cb]] | 3 sources |
| Collaborative beamforming (virtual antenna array) | [[sun-2025-emoppo-vlh-aerial-cb]], [[li-2024-emodrl-ground-space-cb]], [[zhang-2024-gdmtd3-aerial-secure-cb]] | 3 sources — aerial / ground-space / secure CB, evolutionary-MORL + diffusion |
| Foundational DRL methods | [[fujimoto-2018-td3-actor-critic]] | 1 source — TD3 origin paper, anchors the TD3/MATD3 lineage |
| ISAC / sensing / PLS | [[benaya-2025-aerial-isac-haps]], [[jiang-2025-isac-lae-overview]], [[meng-2024-uav-isac-overview]], [[faisal-2025-cgan-ris-isac-channel]], [[zhang-2025-gan-td3-isac-active-ris]], [[tang-2024-iscc-uav-feel]], [[yao-2025-secure-isac-dual-eavesdropping]] | 7 sources — now a major track |
| Game-theoretic offloading | [[chen-2024-ulse-game]], [[li-2025-stochastic-game-uav-swarm]], [[wang-2025-uav-swarm-stackelberg]], [[bi-2025-sg-mapg]], [[he-2019-euagame-user-allocation]], [[sun-2023-bargain-match-vec]], [[wang-2024-twotier-satellite-marine]], [[sun-2024-mvtora-postdisaster-vfc]], [[chen-2024-three-party-hierarchical-game-pls]] | Potential / Stackelberg / bargaining / matching / coalition |
| Generative-AI MEC | [[ye-2025-aigc-diffusion-contract]], [[peng-2025-drudm-cfg]], [[zhang-2024-gdmtd3-aerial-secure-cb]], [[fu-2025-otae-inference-lae-batching]], [[faisal-2025-cgan-ris-isac-channel]], [[zhang-2025-gan-td3-isac-active-ris]] | Diffusion-as-optimizer + GAN-enhanced; survey anchor added |
| Caching / service placement | [[zhao-2025-traj-offload-cache-migration]], [[gao-2024-service-experience-cache-uav]], [[zhao-2024-caching-service-placement-uav]], [[du-2023-maddpg-service-placement-agin]], [[mao-2024-ntn-hierarchical-caching-cav]] | 5 sources |
| Energy efficiency & WPT | [[zhu-2025-lycnn-drl-wpt-mec]], [[wu-2025-iopo-irs-uav-thz-mec]], [[chen-2025-swipt-mec-sac]], [[hsu-2025-drl-hues-hap-noma]], [[zhou-2018-uav-wireless-powered-mec]] | SWIPT + classical WPT-MEC anchor added |
| Post-disaster MEC | [[peng-2025-drudm-cfg]], [[sun-2024-mvtora-postdisaster-vfc]] | 2 sources (DRL + game/VFC) |

## Cross-cutting observations

(Originally drawn from the first 12 sources; updated where the new batch changes the picture.)

1. **Lyapunov + DRL hybrids are still common** for long-term-constrained per-slot MEC optimization ([[qin-2025-bcuav-masac]], [[zhu-2025-lycnn-drl-wpt-mec]]). The new batch reinforces this — see the alternating-optimization (AO + SDR + SCA) version in [[benaya-2025-aerial-isac-haps]].
2. **CTDE remains the default multi-agent paradigm** ([[peng-2025-drudm-cfg]], [[zhang-2025-mcma-task-migration]], [[zhang-2025-ssac-mgi-heterogeneous-uav]], [[qin-2025-bcuav-masac]]).
3. **Stackelberg + matching keeps showing up** ([[wang-2025-uav-swarm-stackelberg]], [[bi-2025-sg-mapg]], [[wang-2026-aerial-marine-msar]] adds many-to-one matching, [[nabi-2025-jour-hierarchical-aerial]] adds Gale-Shapley).
4. **Two-stage decomposition (discrete-then-continuous) is a recurring solver pattern** — [[wang-2026-aerial-marine-msar]], [[nabi-2025-jour-hierarchical-aerial]], [[jia-2025-dro-uav-hap-mec]]. Compare with the **joint hybrid-action** family ([[liu-2026-jppo-en-convntm|j-PPO]], [[ma-2025-pdqn-vehicular-mec|P-DQN]]). See [[two-stage-decomposition]].
5. **Fairness metrics fragment** — Jain, Theil, and now energy-balancing variance ([[huang-2023-mu-aec-task-energy]], [[nabi-2025-jour-hierarchical-aerial]]) and completion-time difference ([[peng-2024-energy-time-uav-its]]). The [[fairness-metrics-in-mec]] page now collects these side by side.
6. **CSI uncertainty is now an explicit concern** in three different ways: distributionally robust ([[jia-2025-dro-uav-hap-mec]]), known-route side-step ([[wang-2026-aerial-marine-msar]]), and terrain-aware geometric ([[wu-2026-terrain-aware-uav-mec]]).
7. **DRL is not the only game in town.** The new batch makes the **evolutionary / classical** branch comparable in size to the DRL branch. A "DRL-vs-evolutionary-vs-classical" synthesis is now justified.
8. **Most papers are still simulation-only.** Only 2 of 89 curated sources are hardware-validated ([[sun-2024-asap-uav-swarm]], [[shao-2024-drl-antijamming-mec]]). Worth keeping in mind for any thesis claim.

## Open questions

- [[query-real-world-validation-of-jppo-en-convntm]] — sim-to-real transfer.
- [[query-does-en-convntm-generalize-beyond-uav-mec]] — generalization of memory-augmented encoders.
- [[query-when-does-dro-beat-drl-for-csi-uncertainty]] — DRO vs DRL vs structural side-step for CSI uncertainty (promoted from the SAGIN/robustness synthesis in the 2026-05-30 pass).
- [[query-video-vs-cooperative-perception-offloading-shape]] — whether video-analytics and cooperative-perception offloading share one fidelity-vs-cost optimization shape.

## Where to go next

- `wiki/index.md` — full type-grouped page directory.
- `wiki/log.md` — reverse-chronological activity log.
- `raw/sources/` — drop new papers here for the next curation pass.
