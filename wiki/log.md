# Research Log

## 2026-05-28

- Project created.
- Repo initialized as a GitHub repo (private) under `EnosElinsa/mec-research-wiki`.
- Ingested first source: [[liu-2026-jppo-en-convntm]] — Liu et al., *Multi-UAV Path Planning for MEC with High-Density Mobile Devices*.
- Constructed initial wiki graph from this paper:
  - 16 concept pages covering MEC, UAV decisions, the Gauss-Markov mobility model, PPO/GAE/POMDP, NTM/ConvLSTM/STN, and the framework's three evaluation metrics.
  - 6 finding pages capturing the headline experimental results.
  - 1 methodology page describing the simulation protocol.
  - 1 thesis page recording the current working hypothesis.
  - 2 query pages tracking the open sim-to-real and generalization questions.
  - 2 comparison pages and 1 synthesis page (design recipe).
  - 7 entity pages for authors plus PyTorch.
- Set baseline `purpose.md` and `schema.md` left untouched — schema-compliant.

## 2026-05-28 (curation pass — paper 2/12)

- Curated [[mao-2025-bcsa-frl]] — Mao et al. 2025, *Blockchain-Enabled Cold Start Aggregation Scheme for FRL-Based Task Offloading in Zero Trust LEO Satellite Networks* (IEEE JSAC).
- Added concept pages: [[leo-satellite-edge-computing]], [[zero-trust-architecture]], [[federated-reinforcement-learning]], [[blockchain-for-fl-aggregation]], [[ccvm-correction-voting]], [[csra-cold-start-reputation-aggregation]], [[fl-poisoning-attacks]], [[ddqn]].
- Added finding: [[bcsa-frl-tolerates-up-to-half-malicious-satellites]].

## 2026-05-28 (curation pass — paper 3/12)

- Curated [[qin-2025-bcuav-masac]] — Qin et al. 2025, *Cooperative UAV Trajectory Design and Resource Allocation in Blockchain-Enabled Secure Aerial Edge Computing Network* (IEEE TWC).
- Added concept pages: [[lyapunov-optimization]], [[masac]], [[noma]], [[air-ground-integrated-network]].
- Cross-linked with [[mao-2025-bcsa-frl]] (shared blockchain-on-edge thread) and [[liu-2026-jppo-en-convntm]] (shared multi-UAV-DRL thread).

## 2026-05-28 (curation pass — paper 4/12)

- Curated [[peng-2025-drudm-cfg]] — Peng et al. 2025, *DRUDM-CFG: A Fairness-Aware Multi-Agent DRL for AMEC-Assisted TO in Post-Disaster Scenarios*.
- Added concept pages: [[high-altitude-platform-station]], [[post-disaster-mec]], [[theil-fairness-index]], [[hierarchical-aerial-mec]], [[adaptive-entropy-priority-replay]], [[ma-pomdp]].

## 2026-05-28 (curation pass — paper 5/12)

- Curated [[zhu-2025-lycnn-drl-wpt-mec]] — Zhu et al. 2025, *Enhancing Energy Efficiency in WPT-MEC Through Lyapunov-Guided DRL* (IEEE TWC).
- Added concept pages: [[wireless-power-transfer]], [[binary-vs-partial-offloading]], [[fractional-programming-dinkelbach]].

## 2026-05-28 (curation pass — paper 6/12)

- Curated [[zhang-2025-mcma-task-migration]] — Zhang et al. 2025, *Multi-Agent DRL With Trajectory Prediction for Task Migration-Assisted Computation Offloading*.
- Added concept pages: [[vehicular-mec]], [[task-migration]], [[informer-trajectory-prediction]], [[centralized-training-decentralized-execution]].

## 2026-05-28 (curation pass — paper 7/12)

- Curated [[wang-2025-uav-swarm-stackelberg]] — Wang et al. 2025, *Optimizing Spectrum Sharing in UAV Swarms: A Stackelberg Game-Based Incentive Mechanism* (IEEE TVT).
- Added concept pages: [[stackelberg-game]], [[overlay-underlay-spectrum-access]], [[matching-theory-for-resource-allocation]], [[low-altitude-intelligent-network]].
- Note: this is the wiki's first **wireless-foundations** track entry, distinct from the compute-offloading track. Future foundations papers should land under similar concept families.

## 2026-05-28 (curation pass — paper 8/12)

- Curated [[zhang-2025-ssac-mgi-heterogeneous-uav]] — Zhang et al. 2025, *Safe and Energy-Efficient Trajectory Planning for Heterogeneous Multi-UAV Enabled MEC*.
- Added concept pages: [[heterogeneous-uav-fleet]], [[safe-reinforcement-learning]], [[collision-avoidance-mgi]].

## 2026-05-28 (curation pass — paper 9/12)

- Curated [[bi-2025-sg-mapg]] — Bi et al. 2025, *SG-MAPG: A Three-Layer Hierarchical Model for Service Fairness and Cost Optimization in UAV-Assisted MEC*.
- No new concept pages — reuses [[stackelberg-game]], [[ma-pomdp]], [[hierarchical-aerial-mec]], [[matching-theory-for-resource-allocation]]. Multi-agent policy gradient as a Stackelberg-equilibrium approximator is worth synthesizing if a third source uses it.

## 2026-05-28 (curation pass — paper 10/12)

- Curated [[hao-2025-priority-aware-task-driven-co]] — Hao et al. 2025, *Task-Driven Priority-Aware Computation Offloading Using DRL*.
- Added concept pages: [[event-driven-vs-slot-driven-offloading]], [[task-priority-in-mec]].

## 2026-05-28 (curation pass — paper 11/12)

- Curated [[wang-2025-lae-network-survey]] — Wang et al. 2025, *Toward Realization of Low-Altitude Economy Networks* (IEEE TCCN).
- Added concept pages: [[generative-ai-for-mec]] (placeholder for future GAI-MEC sources).
- This is a survey/architecture paper — anchors the wiki's LAE thread and provides the panoramic frame for narrower curated sources.

## 2026-05-28 (curation pass — paper 12/12 — corpus complete)

- Curated [[xie-2026-uav-multisource-fusion]] — Xie et al. 2026, *UAV-Enabled Multi-Source Data Fusion in Vehicular Networks* (IEEE TWC).
- Added concept pages: [[cooperative-perception]], [[dynamic-constrained-multi-objective-optimization]].
- All 12 raw sources are now curated. Refreshing index/overview next.

## 2026-05-29 (cross-source synthesis pass)

- Added [[drl-backbones-across-uav-mec-sources]] — cross-corpus synthesis covering 9 of 12 sources, mapping action-space shape → backbone choice, single vs multi-agent, memory/prediction patterns, and DRL-vs-classical composition. Distills 6 practical recommendations.
- Added [[bcsa-frl-vs-bc-uav-masac]] — head-to-head comparison of the two blockchain-integrated MEC sources. Where they agree, where they disagree, and a hypothetical composition.
- Updated `wiki/index.md` so both pages are reachable from the type-grouped directory.

## 2026-05-29 (synthesis pass continued)

- Added [[maddpg-vs-masac-in-mec]] — synthesis on the recurring "MASAC beats MADDPG" pattern in the cooperative-MEC corpus. Working thesis at medium confidence based on direct evidence from [[qin-2025-bcuav-masac]] and [[zhang-2025-ssac-mgi-heterogeneous-uav]], indirect support from [[peng-2025-drudm-cfg]] and [[liu-2026-jppo-en-convntm]]. Documents the mechanism, when MADDPG is still preferable, and what would promote the thesis to high confidence.
- Updated `wiki/index.md` synthesis section.
## [2026-05-28] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- A DRL-Based High-Altitude Platform Transmission and Energy Harvesting Scheduling Scheme for 6G NOMA.pdf-059269bc-68ac-4e8c-82bc-090d67f163cd/bc50cd1f-cef0-4b2a-a746-92f0c4476f79_origin.pdf
- A DRL-Based High-Altitude Platform Transmission and Energy Harvesting Scheduling Scheme for 6G NOMA.pdf-059269bc-68ac-4e8c-82bc-090d67f163cd/full.md
## [2026-05-28] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- Aerial ISAC A HAPS-Assisted Integrated Sensing, Communications and Computing Framework for Enhanced.pdf-cbfcacfe-e469-42fe-824a-18621d54b72e/7b0dd176-7253-422b-ac0e-8100331fd0d8_origin.pdf
- Aerial ISAC A HAPS-Assisted Integrated Sensing, Communications and Computing Framework for Enhanced.pdf-cbfcacfe-e469-42fe-824a-18621d54b72e/full.md
## [2026-05-28] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- Computation Offloading and Resource Allocation in Vehicular MEC A Parameterized Deep Reinforcement.pdf-6d9ed353-ee3f-4d3e-890d-7128f4199eca/d2b86536-1061-4c7c-83e3-48ab00d620b7_origin.pdf
- Computation Offloading and Resource Allocation in Vehicular MEC A Parameterized Deep Reinforcement.pdf-6d9ed353-ee3f-4d3e-890d-7128f4199eca/full.md
## [2026-05-28] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- Computation-Efficient Aerial-Marine Integrated Networks for Search and Rescue via Cooperative HAPS,.pdf-57ca6536-a6cc-4f20-89f0-85649d831a5f/255b305e-ac42-4253-9f2f-66a881effee7_origin.pdf
- Computation-Efficient Aerial-Marine Integrated Networks for Search and Rescue via Cooperative HAPS,.pdf-57ca6536-a6cc-4f20-89f0-85649d831a5f/full.md
## [2026-05-28] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- Constrained_Multi-Objective_Optimization_for_UAV-Enabled_Mobile_Edge_Computing_Offloading_Optimization_and_Path_Planning.pdf-4a80bf0c-6d3b-42a4-8bf6-e59369b4da45/e2cbd4fd-01db-4ad4-a0b5-46084bd1f98c_origin.pdf
- Constrained_Multi-Objective_Optimization_for_UAV-Enabled_Mobile_Edge_Computing_Offloading_Optimization_and_Path_Planning.pdf-4a80bf0c-6d3b-42a4-8bf6-e59369b4da45/full.md
## [2026-05-28] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- Distributionally Robust Optimization for Aerial Multi-Access Edge Computing via Cooperation of UAVs.pdf-e38a92fb-7eb4-4aec-9514-3d886cf29ddb/ab4c9dcb-8a80-48b3-8fa8-219fd6933dcc_origin.pdf
- Distributionally Robust Optimization for Aerial Multi-Access Edge Computing via Cooperation of UAVs.pdf-e38a92fb-7eb4-4aec-9514-3d886cf29ddb/full.md
## [2026-05-28] external batch delete | 3 source files

Deleted 3 source files and 0 wiki pages.

Sources:
- HAP-UAV-assisted hierarchical aerial computing framework for video offloading a deep reinforcement.pdf-e9aa0ccd-efdc-4604-9432-aa9ebef3b951/84fe2fa2-9cd4-458b-a3fd-c7c1a7fa57ec_origin.pdf
- HAP-UAV-assisted hierarchical aerial computing framework for video offloading a deep reinforcement.pdf-e9aa0ccd-efdc-4604-9432-aa9ebef3b951/full.md
- HAP-UAV-assisted hierarchical aerial computing framework for video offloading a deep reinforcement.pdf-e9aa0ccd-efdc-4604-9432-aa9ebef3b951/origin_file.html
## [2026-05-28] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- HAP-UAV-Assisted Maritime IoT Communication Network.pdf-8e5f50d2-68b9-424e-9991-40a9a02718ca/b802e38e-15e5-414e-b060-b4d4c009a479_origin.pdf
- HAP-UAV-Assisted Maritime IoT Communication Network.pdf-8e5f50d2-68b9-424e-9991-40a9a02718ca/full.md
## [2026-05-28] external batch delete | 3 source files

Deleted 3 source files and 0 wiki pages.

Sources:
- Integrated Sensing and Communication for Low Altitude Economy Opportunities and Challenges.pdf-f86e55d9-a9c9-4c39-a996-de372c281fb2/c3f1156a-22b5-4c6b-9d30-bb1ab8067bf8_origin.pdf
- Integrated Sensing and Communication for Low Altitude Economy Opportunities and Challenges.pdf-f86e55d9-a9c9-4c39-a996-de372c281fb2/full.md
- Integrated Sensing and Communication for Low Altitude Economy Opportunities and Challenges.pdf-f86e55d9-a9c9-4c39-a996-de372c281fb2/origin_file.html
## [2026-05-28] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- Joint Latency and Charge Cost Minimization for Reliable Task Offloading in Dispersed Computing A Mu.pdf-e22a4da7-5b0d-4d45-b0a9-408eac9937e9/39153acd-ed2c-4687-a492-c3198ec29647_origin.pdf
- Joint Latency and Charge Cost Minimization for Reliable Task Offloading in Dispersed Computing A Mu.pdf-e22a4da7-5b0d-4d45-b0a9-408eac9937e9/full.md
## [2026-05-28] external batch delete | 3 source files

Deleted 3 source files and 0 wiki pages.

Sources:
- Joint Offloading Decision, User Association, and Resource Allocation in Hierarchical Aerial Computin.pdf-6f881ad4-c9bf-4289-a14e-3810ec4eea7e/4ee311e2-a918-4848-859b-b50fb4cd16b0_origin.pdf
- Joint Offloading Decision, User Association, and Resource Allocation in Hierarchical Aerial Computin.pdf-6f881ad4-c9bf-4289-a14e-3810ec4eea7e/full.md
- Joint Offloading Decision, User Association, and Resource Allocation in Hierarchical Aerial Computin.pdf-6f881ad4-c9bf-4289-a14e-3810ec4eea7e/origin_file.html
## [2026-05-28] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- Joint_Interdependent_Task_Scheduling_and_Energy_Balancing_for_Multi-UAV-Enabled_Aerial_Edge_Computing_A_Multiobjective_Optimization_Approach.pdf-1cb95c2b-3a53-41eb-914b-77c387e75f7f/4e017c7c-629d-47fd-b843-7c070000881f_origin.pdf
- Joint_Interdependent_Task_Scheduling_and_Energy_Balancing_for_Multi-UAV-Enabled_Aerial_Edge_Computing_A_Multiobjective_Optimization_Approach.pdf-1cb95c2b-3a53-41eb-914b-77c387e75f7f/full.md
## [2026-05-28] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- Optimizing Spectrum Sharing in UAV Swarms A Stackelberg Game-Based Incentive Mechanism.pdf-6a97c5fd-e02f-4437-bc8e-9d0e5269b760/c26b8198-beeb-4fef-bfc5-acabcbeeb05b_origin.pdf
- Optimizing Spectrum Sharing in UAV Swarms A Stackelberg Game-Based Incentive Mechanism.pdf-6a97c5fd-e02f-4437-bc8e-9d0e5269b760/full.md
## [2026-05-28] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- Terrain-Aware_UAV-Enabled_Mobile_Edge_Computing_in_Urban_Environments_A_Constrained_Multi-Objective_Approach_With_Task-Adaptive_Mechanism.pdf-c5060bf2-1356-4406-ab38-e23a3fa3950a/20d2321e-85c6-423b-8fe7-5f0803a7637f_origin.pdf
- Terrain-Aware_UAV-Enabled_Mobile_Edge_Computing_in_Urban_Environments_A_Constrained_Multi-Objective_Approach_With_Task-Adaptive_Mechanism.pdf-c5060bf2-1356-4406-ab38-e23a3fa3950a/full.md
## [2026-05-28] external batch delete | 3 source files

Deleted 3 source files and 0 wiki pages.

Sources:
- UAV-Enabled Multi-Source Data Fusion in Vehicular Networks A Joint Optimization Approach for Reliab.pdf-52077623-c7d8-4498-b885-5d0bbd0e33cf/3f0640e8-069b-47ea-8844-e0100315d78c_origin.pdf
- UAV-Enabled Multi-Source Data Fusion in Vehicular Networks A Joint Optimization Approach for Reliab.pdf-52077623-c7d8-4498-b885-5d0bbd0e33cf/full.md
- UAV-Enabled Multi-Source Data Fusion in Vehicular Networks A Joint Optimization Approach for Reliab.pdf-52077623-c7d8-4498-b885-5d0bbd0e33cf/origin_file.html

## 2026-05-29 (curation pass — 14 new sources)

User dropped 16 new folders into `raw/sources/`; two were duplicate ingests of papers already curated ([[wang-2025-uav-swarm-stackelberg]] and [[xie-2026-uav-multisource-fusion]] each appeared twice with different MinerU UUIDs). Curated the remaining 14 in one pass:

**Hierarchical aerial MEC (UAV + HAP) — 3 new sources:**
- [[nabi-2025-jour-hierarchical-aerial]] — Nabi & Moh 2025 (TMC). Gale-Shapley matching + ESAC for joint offloading, association, resource allocation.
- [[bao-2025-ddpg-video-offloading]] — Bao et al. 2025. UAV+HAP video-analytics offloading with adaptive transcoding; DDPG over a QoE reward. **First video-analytics workload in the wiki.**
- [[jia-2025-dro-uav-hap-mec]] — Jia et al. 2025 (TMC). Distributionally robust UAV-HAP MEC under uncertain CSI; CVaR + primal decomposition + BWOA. **First DRO entry in the wiki.**

**Maritime MEC track (new) — 2 new sources:**
- [[wang-2026-aerial-marine-msar]] — Wang et al. 2026 (TCCN). UAV+HAPS+MASS three-tier MEC for maritime search & rescue. Classical solver (matching + convex + PGD).
- [[liu-2025-haps-uav-maritime-iot]] — Liu et al. 2025 (TMC). HAP-UAV-vessel comm: HAP-as-backhaul, UAV multicast, vessel unicast. Multi-verse optimizer + classical step-wise alternative.

**CMOP / evolutionary UAV-MEC lineage (Peng/Huang group) — 4 new sources:**
- [[peng-2022-cmop-uav-path-planning]] — **Lineage seed** (LWC 2022). CMOP for UAV path planning + offloading; infeasibility-utilization CMOEA.
- [[peng-2024-energy-time-uav-its]] — Peng et al. 2024 (TITS). UAV-ITS energy + completion-time-difference.
- [[huang-2023-mu-aec-task-energy]] — Huang et al. 2023 (IoTJ). Multi-UAV interdependent (DAG) tasks; makespan + energy balancing.
- [[huang-2025-cmop-dispersed-computing]] — Huang et al. 2025. Dispersed computing with task-redundancy reliability; dual-population CMOEA.
- [[wu-2026-terrain-aware-uav-mec]] — Wu et al. 2026 (TVT). Urban UAV-MEC with terrain-aware DEM channel; multi-tasking CMOEA.

(The lineage now has 6 entries including [[xie-2026-uav-multisource-fusion]].)

**HAP / SAGIN foundations — 1 new source:**
- [[hsu-2025-drl-hues-hap-noma]] — Hsu et al. 2025 (TCCN). HAP transmission + RF energy harvesting in NOMA SAGINs; PPO-based DRL-HUES.

**ISAC track — 2 new sources:**
- [[benaya-2025-aerial-isac-haps]] — Benaya et al. 2025 (TGCN). HAPS-mounted FD ISAC + friendly-jamming UAV + ground MEC; AO + SDR + SCA.
- [[jiang-2025-isac-lae-overview]] — Jiang et al. 2025 (ComMag). ISAC-for-LAE survey: IAGN architecture, MBCM channel model, stochastic-geometry analysis.

**Vehicular MEC — 1 new source:**
- [[ma-2025-pdqn-vehicular-mec]] — Ma et al. 2025 (TVT). P-DQN for hybrid-action three-tier vehicular MEC.

### Concept pages added (44)

Added concept stubs for the new vocabulary introduced by these sources, grouped:

- **Communication / sensing / security:** [[integrated-sensing-and-communication]], [[physical-layer-security]], [[friendly-jamming-uav]], [[space-air-ground-integrated-network]], [[rf-energy-harvesting]], [[unicast-multicast-cooperation]], [[wireless-backhaul]].
- **DRL:** [[ddpg]], [[parameterized-dqn]], [[prioritized-experience-replay]].
- **Optimization (classical / metaheuristic):** [[alternating-optimization-sdr-sca]], [[chance-constraint]], [[conditional-value-at-risk]], [[distributionally-robust-optimization]], [[binary-whale-optimization]], [[multi-verse-optimizer]], [[weighted-kmeans-uav-deployment]], [[two-stage-decomposition]], [[gale-shapley-matching]].
- **Evolutionary methods:** [[constrained-multi-objective-evolutionary-algorithm]], [[cmoea-d-cdp]], [[infeasible-individual-utilization]], [[dual-population-evolutionary-algorithm]], [[multi-tasking-evolutionary-algorithm]], [[local-search-evolutionary]], [[b-spline-trajectory]].
- **Channel modeling:** [[blockage-aware-channel-model]], [[terrain-aware-channel-model]], [[stochastic-geometry-network-analysis]], [[csi-estimation-error]].
- **Workload classes / scheduling:** [[video-analytics-offloading]], [[video-transcoding-tradeoff]], [[qoe-modeling-mec]], [[dispersed-computing]], [[task-redundancy-for-reliability]], [[parallel-vs-serial-processing]], [[interdependent-tasks-dag]], [[makespan-minimization]], [[completion-time-difference]], [[multi-source-data-fusion]].
- **Architecture / metrics:** [[three-tier-cloud-edge-end]], [[maritime-mec]], [[uav-enabled-its]], [[service-caching-mec]], [[load-balancing-uav-mec]], [[energy-balancing-uav]].

### What this changes about the corpus

- **Corpus size:** 12 → 26 curated sources.
- **Track distribution shifts.** UAV-MEC + DRL is no longer the dominant majority — the **CMOP/evolutionary** lineage now has 6 entries (including [[xie-2026-uav-multisource-fusion]]), comparable to the DRL-multi-agent track. A "DRL-vs-evolutionary" split is now a real synthesis opportunity.
- **New tracks:** maritime MEC (2), ISAC (2), aerial-MEC robust optimization (1 entry, [[jia-2025-dro-uav-hap-mec]]).
- **CSI uncertainty** is now an explicit modeling concern (DRO, terrain-aware geometric, historical-route side-step).
- **Workload diversity:** the wiki now distinguishes generic offloading, video analytics, cooperative perception, ISAC sensing, and DAG-structured tasks — useful for any future "workload class" synthesis.
- **No new theses or findings yet.** All synthesis pages still reflect the original 12-source corpus. Updating those is the next pass.

### Issues flagged for follow-up

- **Author entity pages** are still only present for the very first source. Several names recur across the new batch (Xumin Huang, Chaoda Peng, Yuan Wu, Jiawen Kang) — worth promoting to entity pages.
- The **synthesis pages** (e.g. [[drl-backbones-across-uav-mec-sources]]) are based on a 12-source view. With 26 sources they're out of date. Plan an explicit synthesis refresh.
- **`overview.md`** still says "12 sources" and lists tracks that are now incomplete. Refreshing in the next step of this pass.

## 2026-05-29 (synthesis + entity follow-up)

Closed the follow-up items flagged at the end of the curation pass.

### Author entity pages (4 added)

The CMOP-evolutionary lineage has four recurring authors. Promoted them to entity pages:

- [[chaoda-peng]] — first author of lineage seed; on 6 of 6 lineage sources.
- [[xumin-huang]] — first/lead author on 2 lineage sources, co-author on 4 more.
- [[yuan-wu]] — senior co-author across all 6 lineage sources.
- [[jiawen-kang]] — co-author on 4 lineage sources.

Each page lists their roster and notes which methodological knobs they're associated with.

### Synthesis pages (3 added, 1 refreshed)

**Added:**

- [[cmop-evolutionary-uav-mec-lineage]] — maps the Peng/Huang group's 6-paper thread (2022-2026), the shared template, the per-paper methodological knob, the inheritance graph, and when to pick CMOEA vs DRL.
- [[hierarchical-aerial-mec-design-space]] — cross-compares the 5 UAV+HAP hierarchical-MEC sources on backbone, decomposition, channel model, objective stack, HAP role. Identifies [[two-stage-decomposition]] as the most portable scaffold and HAP-link / security as gaps.
- [[drl-vs-evolutionary-vs-classical-solvers]] — corpus-wide solver-family synthesis. 12 DRL + 8 evolutionary + 4 classical (with overlap). Operating guide for picking each, plus the gap analysis: no head-to-head between families, robustness only in classical so far.

**Refreshed:**

- [[drl-backbones-across-uav-mec-sources]] — extended the at-a-glance table to cover the 4 new DRL sources (P-DQN, DDPG video, ESAC, HAP-PPO) and added "What the 2026-05-29 batch changes" section with three refinements:
  1. Hybrid-action design space now has a clean three-way taxonomy.
  2. DDPG has a niche after all (single-agent + scalar + pure-continuous).
  3. PER + entropy-regularized policy is now the default off-policy baseline.
  4. SAGIN-tier scheduling has its own optimization shape (resource-constrained aerial scheduling).

### Index updates

- Synthesis section now lists 6 pages.
- Entities section split into Authors / Tools subsections.

### Still not done (intentional, scope-bound)

- **Findings / methodology / thesis pages** still anchored to the original 12-source corpus. They were not touched in this pass — claims like [[hybrid-action-memory-augmented-drl-wins-uav-mec]] are framed as *theses about [[liu-2026-jppo-en-convntm]]'s framework*, not corpus-wide. Refreshing them under the 26-source view would be a separate dedicated pass with new findings derived from the new sources, not just a re-link.
- **No `evolutionary-design-recipe`** companion to [[design-recipe-multi-uav-mec]]. The lineage synthesis page covers the methodological choices but doesn't yet distill them into a checklist. Future work.
- **No fresh queries** raised in this pass. Several open questions are flagged inside the new synthesis pages — they should be promoted to formal `query-*` pages when one accumulates enough signal to be worth tracking.

## 2026-05-29 (audit pass — three corrections)

Reviewed all 14 new source pages against the parsed papers. Three issues found, all fixed:

### bao-2025-ddpg-video-offloading

- **Venue was wrong.** I had marked it as "Journal of Supercomputing / Cluster Computing (Springer; preprint, accepted Sep 2025)" because the MinerU parse didn't capture publication metadata. The actual venue is **Complex & Intelligent Systems** (Springer), DOI `10.1007/s40747-025-02106-1`. Confirmed via web search of the title; updated frontmatter and citation.
- **Findings claim was wrong.** I wrote "DDPG converges faster than PPO baselines on this problem". The actual paper compares DDPG against **AC** and **DQN** baselines (no PPO baseline in the paper). DQN explicitly fails to converge in continuous action space; AC trains but is unstable. Updated the Findings section and added a note that the wiki's broader [[ddpg-vs-jppo]] comparison should be read as cross-source rather than internal to this paper.

### huang-2025-cmop-dispersed-computing

- **Venue was wrong.** I had marked it as "IEEE / preprint (Huang/Peng group, 2025)". The actual venue is **IEEE Transactions on Evolutionary Computation**, DOI `10.1109/TEVC.2025.3569722`. Confirmed by grepping the parsed full.md for the DOI. Updated frontmatter and citation.

### Other checks that passed

- Cross-checked DOIs for the 12 other new source pages against their parsed papers — all match.
- Schema lint: 26 source pages, 103 concept pages, 11 entity pages, 6 synthesis pages all have valid frontmatter (`type`, `title`, `tags`, h1 heading, etc.).
- Method/findings claims spot-checked for: JCORA (wang-2026, two-stage matching+convex+PGD), EMOMVO-CGD/JCCPAPO (liu-2025), ESAC=SAC+PER (nabi-2025), three-tier+binary-offloading+P-DQN (ma-2025), DEM+B-spline+multi-tasking (wu-2026), repair-CHT (peng-2024), dual-population+repair (huang-2025), I≥J standby UAVs (peng-2024), ACCP/ARDCP/MBCM/SRCON (jiang-2025). All consistent with the papers.
- Three dangling wikilinks remain (`hp-mobility-models`, `fairness-metrics-in-mec`, `purpose`) — all pre-existing, not introduced by either the curation or audit pass.
- Graph: 161 nodes, 1073 edges (LLM Wiki API).

The cross-source synthesis pages and concept stubs were not re-audited paragraph-by-paragraph in this pass; they should be reviewed in a future synthesis-refresh pass when new evidence comes in.

## 2026-05-29 (deep synthesis audit)

Read each new synthesis page paragraph by paragraph and cross-checked every factual claim against the underlying papers. Found seven concrete corrections plus several softening edits.

### `cmop-evolutionary-uav-mec-lineage`

- **Overclaim: "B-spline trajectory ... in every paper".** Verified against papers: only [[peng-2022-cmop-uav-path-planning]] and [[wu-2026-terrain-aware-uav-mec]] (the trajectory-design entries) actually use B-splines. [[huang-2023-mu-aec-task-energy]] (DAG scheduling), [[peng-2024-energy-time-uav-its]] (UAV-ITS), [[huang-2025-cmop-dispersed-computing]] (dispersed computing), [[xie-2026-uav-multisource-fusion]] (cooperative perception) don't have a UAV path to plan. Demoted B-spline to "trajectory-subset's shared tool, not a lineage-wide constant".
- **Overclaim: "CMOEA/D-CDP backbone in every paper".** Verified: peng-2022, huang-2023, peng-2024, huang-2025 use CMOEA/D-CDP; xie-2026 extends NSGA-II for the dynamic CMOO setting; wu-2026 uses a multi-tasking dual-population scheme with the constrained-domination principle but not strictly CMOEA/D-CDP. Softened to "CMOEA family backbone — even where the specific framework shifts" with the framework breakdown spelled out.
- **Overclaim: "Compare against the previous lineage entry plus 1-2 external baselines (typically ToP, PPS, NSGA-II, NSGA-III)".** Verified the actual baselines: peng-2022 used ToP, PPS; huang-2023 added NSGA-II; peng-2024 only PPS; huang-2025 used CCMO/BiCo/CMaO/CTAEA (none of those four); xie-2026 used NSGA-II/C-NSGA/C-MOEA; wu-2026 used CMOEMT/URCMO/ICMA/DPPPS. The lineage entries do *not* run head-to-head against each other on a common benchmark. Rewrote the template step to reflect "compare against external CMOEA baselines of the relevant generation" with explicit naming.
- **Overclaim: "All entries run 10⁴-10⁵ function evaluations".** Only [[peng-2022-cmop-uav-path-planning]] explicitly states 3×10⁴ FE. The others report only generations × population. Softened.
- **Overclaim: "all reporting Pareto-front improvements over both DRL-style and prior-CMOEA baselines".** None of the lineage papers compares against a DRL controller. Removed the "DRL-style" half. Confidence on the working thesis reduced from "high" to "medium-high" with the caveat made explicit.
- **Inheritance graph: speculative.** Verified citations: peng-2024 cites peng-2022; huang-2025 cites peng-2022 but does **not** cite peng-2024 directly. Rewrote the graph caption to mark it as interpretive (technique reuse via shared authors), not direct citation.

### `hierarchical-aerial-mec-design-space`

- **Off-by-one: "Two of five (`bao-2025`, `nabi-2025`, `peng-2025`) use DRL".** That's three sources, not two. Fixed.
- **Wrong: "[[jia-2025-dro-uav-hap-mec]] optimizes trajectory jointly with offloading via WKD pre-stage".** WKD is a one-shot UAV deployment scheme; UAVs are quasi-stationary after deployment. So jia-2025 has placement, not trajectory. Reclassified as "in between" — placement, not full trajectory — with the distinction spelled out.
- **Stale "four-source roster" / "the four sources".** The roster has five sources. Updated to "five-source roster" everywhere.
- **Misleading objective table: jia-2025 latency = (chance-constraint), energy = ✓.** The chance constraint *is* on latency, while energy is the actual sole objective. Clarified the cell to make this unambiguous.

### `drl-vs-evolutionary-vs-classical-solvers`

- **Wrong: "[[liu-2025-haps-uav-maritime-iot]]'s EMOMVO-CGD ... used to handle binary subproblems after a convex relaxation".** Verified: EMOMVO-CGD is the *whole MOP* solver for liu-2025 — same role as a CMOEA. Only [[jia-2025-dro-uav-hap-mec]]'s BWOA fits the "binary subproblem after relaxation" pattern. Split the two cases explicitly.
- **Fabricated number: "[[jia-2025-dro-uav-hap-mec]] reports ~10–20% energy overhead vs nominal solutions".** That number is not in the paper; the paper validates robustness empirically without pinning down a percentage. Removed and softened to "the paper's simulations validate the robustness benefit but don't pin down a precise overhead percentage".
- **Family-roster table cleanup.** [[jia-2025-dro-uav-hap-mec]]'s primary classification is classical (DRO + CVaR + primal decomposition + CVX). BWOA is a sub-block solver inside it, not a separate evolutionary entry. Restructured the table: 12 DRL + 7 evolutionary/metaheuristic + 5 classical (with BWOA called out as a sub-block in the classical row).

### Verified clean (no changes needed)

- **`drl-backbones-across-uav-mec-sources`.** The DDPG/TD3/DQN underperformance attribution to hybrid-action limitations matches the paper's own wording verbatim. The DOA reference (Dingo Optimization Algorithm — verified) is correct.
- **`maddpg-vs-masac-in-mec`.** The +13.16% sensing rate / −29.47% queue delay numbers are from the qin-2025 abstract — verified against the parsed paper.
- **`design-recipe-multi-uav-mec`.** Ten checklist items, all anchored to specific liu-2026 results — re-read and consistent.

### Schema and link integrity after edits

- 26 source pages, 103 concept pages, 11 entity pages, 6 synthesis pages — all schema-clean.
- 3 dangling wikilinks remain (hp-mobility-models, fairness-metrics-in-mec, purpose) — all pre-existing, none introduced or worsened by the audit.
