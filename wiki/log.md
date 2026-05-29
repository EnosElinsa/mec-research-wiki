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

## 2026-05-29 (curation pass — batch 4: 43 new sources + audit)

Curated all 43 newly-ingested raw papers (corpus 39 → 82 sources). Metadata extracted faithfully from each MinerU parse; DOIs/venues verified against the parse text. Year convention follows the existing wiki (DOI-embedded year).

- **New source pages (43):** [[he-2019-euagame-user-allocation]], [[mao-2017-mec-survey-communication]], [[wang-2025-acbft-uav-consensus]], [[wang-acve-constraint-violation-cmop]], [[sun-2023-bargain-match-vec]], [[faisal-2025-cgan-ris-isac-channel]], [[kang-2023-mappo-hierarchical-aerial]], [[du-2024-distributed-foundation-models-6g]], [[wang-2025-double-edge-samin]], [[chen-2023-dotora-air-ground-online]], [[zhang-2025-three-tier-maritime-offloading]], [[song-2022-emorl-tcto-uav]], [[he-2023-fairness-3d-multiuav-maddpg]], [[zhai-2023-fedleo-decentralized-fl]], [[zhang-2025-gan-td3-isac-active-ris]], [[khoramnejad-2025-gai-wireless-optimization-survey]], [[jia-2022-hierarchical-aerial-matching]], [[wang-2024-hybrid-oma-noma-sagin]], [[tang-2024-iscc-uav-feel]], [[you-2025-uncertain-maritime-hasac]], [[zhang-2019-uav-iot-comp-comm]], [[zhao-2024-caching-service-placement-uav]], [[wang-2019-todetas-deployment-scheduling]], [[chen-2025-swipt-mec-sac]], [[sun-2024-mvtora-postdisaster-vfc]], [[yu-2020-uav-ec-collaborative-offloading]], [[qin-2025-matd3-noma-queue-sagin]], [[du-2023-maddpg-service-placement-agin]], [[albakhrani-2025-moalf-uav-mec]], [[zhang-2024-dlrl-maritime-usv]], [[zhao-2022-matd3-multiuav-ec-offloading]], [[zhang-2024-gdmtd3-aerial-secure-cb]], [[guo-2023-mccco-multiuav-5g-offloading]], [[mao-2024-ntn-hierarchical-caching-cav]], [[yang-2022-stochastic-uav-mec-lyapunov]], [[fu-2025-otae-inference-lae-batching]], [[liu-2022-miso-uav-mec-trajectory]], [[chang-2022-marl-multiuav-trajectory]], [[li-2025-twohop-airground-drl-offloading]], [[wang-2024-twotier-satellite-marine]], [[zhang-2024-uav-task-offloading-ddpg]], [[meng-2024-uav-isac-overview]], [[yao-2025-secure-isac-dual-eavesdropping]].
- **New concept stubs (17):** [[edge-user-allocation]], [[byzantine-fault-tolerant-consensus]], [[particle-swarm-optimization]], [[constraint-violation-evaluation]], [[bargaining-game]], [[conditional-gan]], [[generative-adversarial-network]], [[mappo]], [[decentralized-federated-learning]], [[integrated-sensing-computation-communication]], [[heterogeneous-agent-rl]], [[differential-evolution]], [[vehicle-fog-computing]], [[non-terrestrial-network]], [[ant-colony-optimization]], [[over-the-air-computation]], [[distributed-foundation-models]]. All other referenced concepts reused existing slugs.
- **New entity (1):** [[geng-sun]] — Jilin University, confirmed consistent across 5 sources. Other recurring batch-4 authors (Zhen Wang / Bin Lin maritime cluster, Ziye Jia / Chao Dong / Zhu Han aerial cluster, Peng Qin / Yang Fu) deferred for human identity confirmation rather than minting/merging entities.
- **Navigation:** refreshed `wiki/index.md` (new groupings: Foundational surveys & overviews, Classical/convex optimization UAV-MEC, Game-theoretic offloading & allocation, Multi-UAV cooperative computing & deployment, Pure optimization methods, ISAC/sensing/PLS; plus GAI / maritime / hierarchical additions and the 17 new concepts) and `wiki/overview.md` (counts 39 → 82, expanded track table, corrected hardware-validated count).

### Audit (correctness-first)

- **DOI / venue / year:** verified against each parse's `Digital Object Identifier` line; year set to the DOI-embedded year per existing wiki convention.
- **`not in parse` handling:** [[wang-acve-constraint-violation-cmop]] — venue, year, and DOI genuinely absent from the parse and unconfirmable by web search (author homepage lists no matching publication); left blank / `not in parse` rather than guessed. [[du-2024-distributed-foundation-models-6g]] — DOI absent from parse; venue "IEEE Wireless Communications" web-confirmed; DOI left empty.
- **Claims:** headline numbers reproduced only where explicit in the parse (e.g. ACBFT "up to 96.2% throughput increase", FedLEO "up to 41% delay / 9.39% accuracy", three-tier maritime "39.3% energy saving"). Figure/abstract-derived numbers (e.g. MOALF percentages) flagged as indicative.
- **Wikilink integrity:** wiki-wide check shows **no NEW dangling links**. Pre-existing dangling links remain and are reported: `[[fairness-metrics-in-mec]]` (in [[peng-2025-drudm-cfg]]), `[[hp-mobility-models]]` (in [[liu-2026-jppo-en-convntm]]), `[[purpose]]` (in [[high-density-mobile-device-scenarios]]).
- **Frontmatter:** `type` / `title` / `tags` / dates / H1 validated on touched pages via diagnostics (no issues).
- **LLM Wiki API:** not queried this pass (headless shell); graph stats unavailable — not required for correctness.

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
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- A_Reinforcement_Learning-Based_Stochastic_Game_for_Energy-Efficient_UAV_Swarm-Assisted_MEC_With_Dynamic_Clustering_and_Scheduling.pdf-41f8372c-e5ff-489a-884c-bb9e2e6212c8/fbb58c1a-07f7-4252-9763-a3a929187767_origin.pdf
- A_Reinforcement_Learning-Based_Stochastic_Game_for_Energy-Efficient_UAV_Swarm-Assisted_MEC_With_Dynamic_Clustering_and_Scheduling.pdf-41f8372c-e5ff-489a-884c-bb9e2e6212c8/full.md
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- AoI_and_Energy_Tradeoff_for_Aerial-Ground_Collaborative_MEC_A_Multi-Objective_Learning_Approach.pdf-644368d2-45ce-4d10-9d8c-5072eac62adf/59a5c499-4de5-4693-94d8-c8bb910236f5_origin.pdf
- AoI_and_Energy_Tradeoff_for_Aerial-Ground_Collaborative_MEC_A_Multi-Objective_Learning_Approach.pdf-644368d2-45ce-4d10-9d8c-5072eac62adf/full.md
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- Multi-User_Task_Offloading_in_UAV-Assisted_LEO_Satellite_Edge_Computing_A_Game-Theoretic_Approach.pdf-9d8450b7-ab1d-4821-933f-ec94a1c3b84d/f0eb5d57-dc3b-4515-85dc-cf2fd20577c0_origin.pdf
- Multi-User_Task_Offloading_in_UAV-Assisted_LEO_Satellite_Edge_Computing_A_Game-Theoretic_Approach.pdf-9d8450b7-ab1d-4821-933f-ec94a1c3b84d/full.md
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- Orchestrating_Federated_Learning_in_Space-Air-_Ground_Integrated_Networks_Adaptive_Data_Offloading_and_Seamless_Handover.pdf-afd0b75a-b16e-4e44-97a0-18bbc9ace47e/5f395380-8451-4fc0-8981-b70a16f3bab0_origin.pdf
- Orchestrating_Federated_Learning_in_Space-Air-_Ground_Integrated_Networks_Adaptive_Data_Offloading_and_Seamless_Handover.pdf-afd0b75a-b16e-4e44-97a0-18bbc9ace47e/full.md
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- Traffic-Aware_Lightweight_Hierarchical_Offloading_Toward_Adaptive_Slicing-Enabled_SAGIN.pdf-45b00363-1481-4a12-bdd8-08fa0d873bdb/ca44e888-13c5-4031-abd4-7f82f289aab3_origin.pdf
- Traffic-Aware_Lightweight_Hierarchical_Offloading_Toward_Adaptive_Slicing-Enabled_SAGIN.pdf-45b00363-1481-4a12-bdd8-08fa0d873bdb/full.md
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- Two-Stage_Deep_Energy_Optimization_in_IRS-Assisted_UAV-Based_Edge_Computing_Systems.pdf-b25ba9cf-0e9d-48a8-aacb-34b513a0d19b/6c4973d7-6eea-4a44-a471-8abc8b4bfeff_origin.pdf
- Two-Stage_Deep_Energy_Optimization_in_IRS-Assisted_UAV-Based_Edge_Computing_Systems.pdf-b25ba9cf-0e9d-48a8-aacb-34b513a0d19b/full.md
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- Cost-Efficient_Computation_Offloading_in_SAGIN_A_Deep_Reinforcement_Learning_and_Perception-Aided_Approach.pdf-a4214f62-8d31-49a9-9cf8-c47d49e7a7c1/ea57119f-657f-4e9c-a621-1d58cc99cfe3_origin.pdf
- Cost-Efficient_Computation_Offloading_in_SAGIN_A_Deep_Reinforcement_Learning_and_Perception-Aided_Approach.pdf-a4214f62-8d31-49a9-9cf8-c47d49e7a7c1/full.md
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- Joint_Optimization_of_Trajectory_Offloading_Caching_and_Migration_for_UAV-Assisted_MEC.pdf-562be632-7b42-4948-a346-f9ecb7b00005/45f67a08-199f-481d-bf29-def86d9ae977_origin.pdf
- Joint_Optimization_of_Trajectory_Offloading_Caching_and_Migration_for_UAV-Assisted_MEC.pdf-562be632-7b42-4948-a346-f9ecb7b00005/full.md
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- Joint_Task_Offloading_Resource_Allocation_and_Trajectory_Design_for_Multi-UAV_Cooperative_Edge_Computing_With_Task_Priority.pdf-84f5e53a-ade3-41c5-a94b-9ddf5067c206/262c8c5f-9f79-487f-90c8-f7fe10c7a86e_origin.pdf
- Joint_Task_Offloading_Resource_Allocation_and_Trajectory_Design_for_Multi-UAV_Cooperative_Edge_Computing_With_Task_Priority.pdf-84f5e53a-ade3-41c5-a94b-9ddf5067c206/full.md
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- Optimizing_AIGC_Services_by_Prompt_Engineering_and_Edge_Computing_A_Generative_Diffusion_Model-Based_Contract_Theory_Approach.pdf-cfeae031-cf38-4e54-b0f5-5320171ef1dc/4f64765d-6919-4fa8-ac26-98022dfb6780_origin.pdf
- Optimizing_AIGC_Services_by_Prompt_Engineering_and_Edge_Computing_A_Generative_Diffusion_Model-Based_Contract_Theory_Approach.pdf-cfeae031-cf38-4e54-b0f5-5320171ef1dc/full.md
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- All-Sky_Autonomous_Computing_in_UAV_Swarm.pdf-2db13480-58a0-4e50-b698-927a64f05df4/5bbeb0cb-515b-49cf-a0d5-cc2274e3e0b3_origin.pdf
- All-Sky_Autonomous_Computing_in_UAV_Swarm.pdf-2db13480-58a0-4e50-b698-927a64f05df4/full.md
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- Deep_Reinforcement_Learning-Based_Resource_Management_for_UAV-Assisted_Mobile_Edge_Computing_Against_Jamming.pdf-0945dec6-2a96-4ba6-a135-4b97bcf692cb/61d1a406-15d3-42b7-9873-b406053311ee_origin.pdf
- Deep_Reinforcement_Learning-Based_Resource_Management_for_UAV-Assisted_Mobile_Edge_Computing_Against_Jamming.pdf-0945dec6-2a96-4ba6-a135-4b97bcf692cb/full.md
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- Service_Experience_Oriented_Cooperative_Computing_in_Cache-Enabled_UAVs_Assisted_MEC_Networks.pdf-acace601-ee7b-4913-b1e3-1364faa6d96b/22637016-68ae-4571-8474-b4efeba95c79_origin.pdf
- Service_Experience_Oriented_Cooperative_Computing_in_Cache-Enabled_UAVs_Assisted_MEC_Networks.pdf-acace601-ee7b-4913-b1e3-1364faa6d96b/full.md

## 2026-05-29 (curation pass — 13 new sources, batch 3)

User dropped 13 new folders into `raw/sources/` and asked to construct the wiki from them. Curated all 13 in one pass (4 had pre-existing extraction drafts in `.curation-out/`; the remaining 9 were extracted by sub-agents against `.curation-context.md`). Corpus grows **26 → 39 curated sources**.

**SAGIN / satellite offloading (4 new):**
- [[gao-2024-sagin-perception-offloading]] — Gao et al. 2024 (JSAC). Perception-aided SAGIN offloading; mmWave radar + YOLOv7 feed a Lyapunov + DDPG + DQN + SGHS pipeline. **First perception-driven offloading entry.**
- [[chen-2024-thoas-traffic-aware-sagin]] — Chen et al. 2024 (JSAC). THOAS: traffic-aware slicing-enabled SAGIN; probsparse-attention prediction + lightweight distilled PPO.
- [[chen-2024-ulse-game]] — Chen et al. 2024 (TMC). Multi-user UAV-LEO offloading as a potential game (LUTO-Game / JULTO).
- [[han-2024-sagin-fl-handover]] — Han et al. 2024 (JSAC). Federated learning across SAGIN with adaptive inter-layer data offloading + satellite seamless handover. **First plain-FL entry.**

**UAV-swarm collaborative computing (2 new):**
- [[sun-2024-asap-uav-swarm]] — Sun et al. 2024 (TMC). ASAP: in-swarm collaborative DL inference (model + data partition, pipeline-parallel). **Hardware-validated** (24 Jetson computers + 5 real UAVs).
- [[li-2025-stochastic-game-uav-swarm]] — Li et al. 2025 (TGCN). Energy-efficient UAV-swarm MEC as five stochastic games with dynamic clustering; RLDC multi-agent Q-learning.

**IRS / THz / anti-jamming (2 new):**
- [[wu-2025-iopo-irs-uav-thz-mec]] — Wu et al. 2025 (TMC). IRS-assisted multi-UAV THz MEC; two-stage IOPO (order-preserving offloading + WOA phases). **First IRS/THz entry.**
- [[shao-2024-drl-antijamming-mec]] — Shao et al. 2024 (TMC). Anti-jamming UAV-MEC; PER-MATD3. **Hardware-validated** (Raspberry Pi/USRP). **First anti-jamming entry.**

**Trajectory / caching / fairness / priority / AoI / AIGC (5 new):**
- [[hao-2024-clp-multiuav-priority-offloading]] — Hao et al. 2024 (TMC). Multi-UAV priority offloading; CLP (TD3 + hybrid-action latent space). Companion to [[hao-2025-priority-aware-task-driven-co]].
- [[zhao-2025-traj-offload-cache-migration]] — Zhao et al. 2025 (TMC). Joint trajectory + offloading + migration + computational-task caching; Lyapunov + BCD + QCQP-SDR.
- [[gao-2024-service-experience-cache-uav]] — Gao & Zhai 2024 (TMC). Fairness-aware cache-enabled UAV-MEC; service-experience ratio (Jain / delay); Dinkelbach + 4-stage AO.
- [[song-2024-mol-aoi-energy]] — Song et al. 2024 (TMC). AoI-vs-energy aerial-ground MEC via multi-objective RL (MOL-AET). **First AoI / MORL entry.**
- [[ye-2025-aigc-diffusion-contract]] — Ye et al. 2025 (TVT). Edge AIGC via contract theory + prompt engineering; generative diffusion model as the contract-item optimizer.

### Concept pages added (55)

- **DRL / learning:** [[td3]], [[multi-agent-td3]], [[deep-q-network]], [[multi-agent-q-learning]], [[hybrid-action-representation]], [[knowledge-distillation-for-drl]], [[dynamic-confidence-interval-clipping]], [[multi-objective-reinforcement-learning]], [[multi-objective-mdp-vectorial-reward]], [[evolutionary-reinforcement-learning]], [[generative-diffusion-model]], [[diffusion-model-as-optimizer]].
- **Game theory / optimization:** [[stochastic-game]], [[potential-game]], [[nash-equilibrium]], [[contract-theory]], [[mixed-integer-nonlinear-programming]], [[whale-optimization-algorithm]], [[self-adaptive-global-best-harmony-search]], [[order-preserving-quantization]], [[qcqp-sdr-probabilistic-mapping]].
- **Communication / sensing / channel:** [[anti-jamming-mec]], [[spectrum-sensing-channel-selection]], [[mmwave-radar-sensing]], [[yolov7-object-detection]], [[perception-aided-offloading]], [[intelligent-reflecting-surface]], [[terahertz-communication]], [[network-slicing]], [[traffic-aware-offloading]], [[probsparse-self-attention-prediction]].
- **Distributed inference (ASAP):** [[collaborative-dl-inference]], [[dnn-model-partition]], [[data-partition-parallel-inference]], [[pipeline-parallel-inference]], [[dl-inference-latency-prediction]], [[adaptive-intermediate-data-compression]], [[elastic-task-scheduling]].
- **Federation / satellite:** [[federated-learning]], [[seamless-handover]], [[adaptive-inter-layer-data-offloading]], [[privacy-sensitive-data-partitioning]], [[walker-star-constellation]], [[leo-satellite-coverage-time]].
- **Scheduling / caching / swarm:** [[computational-task-caching]], [[priority-based-delay-utility]], [[intra-swarm-task-delegation]], [[dynamic-uav-clustering]].
- **Metrics / freshness / fairness / AIGC:** [[age-of-information]], [[aoi-energy-tradeoff]], [[energy-latency-tradeoff]], [[jains-fairness-index]], [[service-experience-ratio]], [[prompt-engineering]], [[aigc-service-provider]].

### Entity pages added (1)

- [[hao-hao]] — first author of [[hao-2024-clp-multiuav-priority-offloading]] and [[hao-2025-priority-aware-task-driven-co]] (identical co-author roster), anchoring the task-priority + hybrid-action thread.

### What this changes about the corpus

- **Corpus size:** 26 → 39 curated sources.
- **New tracks:** SAGIN/satellite offloading (4), UAV-swarm collaborative computing (2), game-theoretic offloading (now spans potential/stochastic/Stackelberg games), generative-AI MEC (2), anti-jamming security-DRL (1).
- **First hardware-validated sources** enter the corpus: [[sun-2024-asap-uav-swarm]] and [[shao-2024-drl-antijamming-mec]]. The "0 hardware-validated sources" caveat in earlier syntheses is now obsolete.
- **New formulation families:** potential/stochastic games + Nash-equilibrium analysis, multi-objective RL (vectorial reward), contract theory, IRS/THz channels, in-swarm collaborative DL inference, federated learning over SAGIN.
- **Diffusion-as-optimizer** now has two sources ([[ye-2025-aigc-diffusion-contract]], [[peng-2025-drudm-cfg]]) — a real synthesis opportunity.

### Issues flagged for follow-up

- **Synthesis refresh overdue.** The synthesis/findings/thesis pages still reflect the 26-source view. The DRL-backbones synthesis should add TD3/MATD3, multi-agent Q-learning, and MORL; the solver-family synthesis should add the game-theoretic and diffusion-as-optimizer families; a dedicated SAGIN-offloading synthesis is now warranted.
- **Author entities to consider:** Xuemin Sherman Shen and Jiwei Huang (on [[chen-2024-ulse-game]]; Jiwei Huang may match the existing huang-* sources — verify identity), Dusit Niyato / Hongyang Du (generative-AI line, on [[ye-2025-aigc-diffusion-contract]]), Fuhong Song (evolutionary-MORL line, on [[song-2024-mol-aoi-energy]]). None created this pass pending recurrence confirmation.
- **Figure-derived numbers:** several magnitudes in [[li-2025-stochastic-game-uav-swarm]] and [[han-2024-sagin-fl-handover]] were read from MinerU-parsed figure tables with unlabeled axes — treat as indicative trends; verify against the PDFs before citing exactly.
- **Cross-references not yet bidirectional:** new sources link to older ones, but a few older source pages (e.g. [[peng-2025-drudm-cfg]], [[hao-2025-priority-aware-task-driven-co]]) could gain back-links to the new companions. Deferred to a link-tidy pass.

## 2026-05-29 (audit pass — batch-3 verification)

Correctness-first audit of the 13 new source pages and refreshed navigation:

- **DOIs verified against parses.** All 13 new source DOIs cross-checked against `Digital Object Identifier` lines in their `full.md`. Two needed manual confirmation because a regex first-match picked up a precursor/reference DOI: [[li-2025-stochastic-game-uav-swarm]] (parse confirms `10.1109/TGCN.2024.3424449`; the WCNC 2024 `10570678` is a conference precursor) and [[shao-2024-drl-antijamming-mec]] (parse confirms `10.1109/TMC.2024.3432491`; the GLOBECOM 2023 hit was a reference). Both page DOIs are correct.
- **Frontmatter valid** on all 39 source pages (`type/title/authors/year/venue/tags/related/created/updated` + H1 present).
- **Wikilink integrity:** no NEW dangling links introduced by this batch. The only unresolved targets remain the three pre-existing ones (`fairness-metrics-in-mec`, `hp-mobility-models`, `purpose`).
- **Counts reconciled:** 39 sources, 158 concepts, 12 entities — matches `overview.md`.
- Created a reusable workspace agent `.kiro/agents/mec-wiki-curator.md` to standardize this curate-then-audit workflow for future raw-paper drops.
## [2026-05-29] external batch delete | 108 source files

Deleted 108 source files and 0 wiki pages.

Sources:
- ACBFT_Adaptive_Chained_Byzantine_Fault-Tolerant_Consensus_Protocol_for_UAV_Ad_Hoc_Networks.pdf-bea3bbdb-b210-4313-bfeb-c98d7e4f95b2/51f1dd7a-88b5-4325-80ed-9c8336415dc9_origin.pdf
- ACBFT_Adaptive_Chained_Byzantine_Fault-Tolerant_Consensus_Protocol_for_UAV_Ad_Hoc_Networks.pdf-bea3bbdb-b210-4313-bfeb-c98d7e4f95b2/full.md
- A_Game-Theoretical_Approach_for_User_Allocation_in_Edge_Computing_Environment.pdf-6a127707-a8c8-4eb3-95db-bd84451c63bb/5805eb5a-c860-435a-a363-c7e08e58d364_origin.pdf
- A_Game-Theoretical_Approach_for_User_Allocation_in_Edge_Computing_Environment.pdf-6a127707-a8c8-4eb3-95db-bd84451c63bb/full.md
- A_Survey_on_Mobile_Edge_Computing_The_Communication_Perspective.pdf-38308eaa-ccf0-4fd8-abc2-904d6e06df92/a4df4525-9548-41ce-848a-b64ff3be183c_origin.pdf
- A_Survey_on_Mobile_Edge_Computing_The_Communication_Perspective.pdf-38308eaa-ccf0-4fd8-abc2-904d6e06df92/full.md
- An_Adaptive_Constraint_Violation_Evaluation_Framework_for_Constrained_Multiobjective_Evolutionary_Optimization.pdf-09d5418e-dc62-4524-bc97-f89ba95dfc7e/1058f15e-3289-44ba-a46f-79175aa42220_origin.pdf
- An_Adaptive_Constraint_Violation_Evaluation_Framework_for_Constrained_Multiobjective_Evolutionary_Optimization.pdf-09d5418e-dc62-4524-bc97-f89ba95dfc7e/full.md
- BARGAIN-MATCH_A_Game_Theoretical_Approach_for_Resource_Allocation_and_Task_Offloading_in_Vehicular_Edge_Computing_Networks.pdf-35b8645f-ec67-4bc8-a322-f2d67eb162f1/04bff10e-4497-45a2-a8ac-d649dc9ccda9_origin.pdf
- BARGAIN-MATCH_A_Game_Theoretical_Approach_for_Resource_Allocation_and_Task_Offloading_in_Vehicular_Edge_Computing_Networks.pdf-35b8645f-ec67-4bc8-a322-f2d67eb162f1/full.md
- Conditional_Generative_Adversarial_Networks_for_Channel_Estimation_in_RIS-Assisted_ISAC_Systems.pdf-92c33306-3b00-4a98-b7c0-b613ac6e3565/d17bf5a0-218d-4917-b746-6fc2a408824f_origin.pdf
- Conditional_Generative_Adversarial_Networks_for_Channel_Estimation_in_RIS-Assisted_ISAC_Systems.pdf-92c33306-3b00-4a98-b7c0-b613ac6e3565/full.md
- Cooperative_UAV_Resource_Allocation_and_Task_Offloading_in_Hierarchical_Aerial_Computing_Systems_A_MAPPO-Based_Approach.pdf-680ca83e-ffea-41f9-bc61-85b9b15a2b82/a6533d10-e97c-4756-a27b-ce396e62927d_origin.pdf
- Cooperative_UAV_Resource_Allocation_and_Task_Offloading_in_Hierarchical_Aerial_Computing_Systems_A_MAPPO-Based_Approach.pdf-680ca83e-ffea-41f9-bc61-85b9b15a2b82/full.md
- Distributed_Foundation_Models_for_Multi-Modal_Learning_in_6G_Wireless_Networks (1).pdf-37e49c9e-f1cf-45f8-b0ad-c274f146debb/52184245-a588-46d7-8436-664582f236ae_origin.pdf
- Distributed_Foundation_Models_for_Multi-Modal_Learning_in_6G_Wireless_Networks (1).pdf-37e49c9e-f1cf-45f8-b0ad-c274f146debb/full.md
- Distributed_Foundation_Models_for_Multi-Modal_Learning_in_6G_Wireless_Networks.pdf-cd5196f5-a52f-4b9d-82ad-c1b50996a79e/17b265eb-d64b-4b6d-9e41-bc3f6577f29b_origin.pdf
- Distributed_Foundation_Models_for_Multi-Modal_Learning_in_6G_Wireless_Networks.pdf-cd5196f5-a52f-4b9d-82ad-c1b50996a79e/full.md
- Double-Edge-Assisted_Computation_Offloading_and_Resource_Allocation_for_Space-Air-Marine_Integrated_Networks (1).pdf-101d96ec-b13f-4bc2-81ba-f99b04be10eb/3d74f158-5928-492f-a341-867a10312574_origin.pdf
- Double-Edge-Assisted_Computation_Offloading_and_Resource_Allocation_for_Space-Air-Marine_Integrated_Networks (1).pdf-101d96ec-b13f-4bc2-81ba-f99b04be10eb/full.md
- Double-Edge-Assisted_Computation_Offloading_and_Resource_Allocation_for_Space-Air-Marine_Integrated_Networks.pdf-98452b41-2b96-41cd-9223-132cf959a545/51a15428-6640-4700-b016-4294726d6ad3_origin.pdf
- Double-Edge-Assisted_Computation_Offloading_and_Resource_Allocation_for_Space-Air-Marine_Integrated_Networks.pdf-98452b41-2b96-41cd-9223-132cf959a545/full.md
- Energy_Efficient_Task_Offloading_and_Resource_Allocation_in_Air-Ground_Integrated_MEC_Systems_A_Distributed_Online_Approach (1).pdf-e9ad5584-e837-47c7-8889-5491ce20b0ad/a7af4c61-064d-406a-8b3b-f4408286873c_origin.pdf
- Energy_Efficient_Task_Offloading_and_Resource_Allocation_in_Air-Ground_Integrated_MEC_Systems_A_Distributed_Online_Approach (1).pdf-e9ad5584-e837-47c7-8889-5491ce20b0ad/full.md
- Energy_Efficient_Task_Offloading_and_Resource_Allocation_in_Air-Ground_Integrated_MEC_Systems_A_Distributed_Online_Approach (2).pdf-0e2c9ca7-5f3c-4ede-a338-873da62ae161/69f11249-178f-489a-99dd-6013be4a2178_origin.pdf
- Energy_Efficient_Task_Offloading_and_Resource_Allocation_in_Air-Ground_Integrated_MEC_Systems_A_Distributed_Online_Approach (2).pdf-0e2c9ca7-5f3c-4ede-a338-873da62ae161/full.md
- Energy_Efficient_Task_Offloading_and_Resource_Allocation_in_Air-Ground_Integrated_MEC_Systems_A_Distributed_Online_Approach.pdf-a0ebded2-6b19-49ef-82a8-a60fe98bd9a3/1bf62391-2d01-4b85-a2dd-44c3f6bfa9e9_origin.pdf
- Energy_Efficient_Task_Offloading_and_Resource_Allocation_in_Air-Ground_Integrated_MEC_Systems_A_Distributed_Online_Approach.pdf-a0ebded2-6b19-49ef-82a8-a60fe98bd9a3/full.md
- Energy_Oriented_Three-Tier_Computation_Offloading_Scheme_in_Maritime_Edge_Computing_Network (1).pdf-c507d9c3-154e-4854-a5ce-4dd59d952c35/1d881528-e07b-4227-bdd8-2c2bfcaecc08_origin.pdf
- Energy_Oriented_Three-Tier_Computation_Offloading_Scheme_in_Maritime_Edge_Computing_Network (1).pdf-c507d9c3-154e-4854-a5ce-4dd59d952c35/full.md
- Energy_Oriented_Three-Tier_Computation_Offloading_Scheme_in_Maritime_Edge_Computing_Network.pdf-226bcccd-9b0e-49f9-b0c1-cba631461523/05cc59c4-a99e-447a-9f94-9002dcc71c45_origin.pdf
- Energy_Oriented_Three-Tier_Computation_Offloading_Scheme_in_Maritime_Edge_Computing_Network.pdf-226bcccd-9b0e-49f9-b0c1-cba631461523/full.md
- Evolutionary_Multi-Objective_Reinforcement_Learning_Based_Trajectory_Control_and_Task_Offloading_in_UAV-Assisted_Mobile_Edge_Computing.pdf-01e5dcd4-c51d-4f14-9188-54506cc73225/6d675f02-2610-41f9-8d08-e81e2f69eb79_origin.pdf
- Evolutionary_Multi-Objective_Reinforcement_Learning_Based_Trajectory_Control_and_Task_Offloading_in_UAV-Assisted_Mobile_Edge_Computing.pdf-01e5dcd4-c51d-4f14-9188-54506cc73225/full.md
- Fairness-Based_3-D_Multi-UAV_Trajectory_Optimization_in_Multi-UAV-Assisted_MEC_System.pdf-bf127b65-b284-404b-8ac3-337dd3a7759a/c0f2255d-e21b-42aa-8b98-d86bd3126819_origin.pdf
- Fairness-Based_3-D_Multi-UAV_Trajectory_Optimization_in_Multi-UAV-Assisted_MEC_System.pdf-bf127b65-b284-404b-8ac3-337dd3a7759a/full.md
- FedLEO_An_Offloading-Assisted_Decentralized_Federated_Learning_Framework_for_Low_Earth_Orbit_Satellite_Networks.pdf-7cbb1edb-d3d9-4aaa-bc82-b01707e227e1/c2b3ff92-9440-484e-82ac-7c26f755903f_origin.pdf
- FedLEO_An_Offloading-Assisted_Decentralized_Federated_Learning_Framework_for_Low_Earth_Orbit_Satellite_Networks.pdf-7cbb1edb-d3d9-4aaa-bc82-b01707e227e1/full.md
- Generative-Adversarial-Network-Enhanced_DRL_for_ISAC_With_Double_Active_RISs.pdf-e50024c1-4074-48e8-95c0-fc9d69153fec/54556004-5e12-446c-a020-2ca85e5d4fb8_origin.pdf
- Generative-Adversarial-Network-Enhanced_DRL_for_ISAC_With_Double_Active_RISs.pdf-e50024c1-4074-48e8-95c0-fc9d69153fec/full.md
- Generative_AI_for_the_Optimization_of_Next-Generation_Wireless_Networks_Basics_State-of-the-Art_and_Open_Challenges.pdf-4f7173f3-facc-4451-819d-5e1664d5c20a/c848f928-34e9-426d-8306-3e39ef4ce670_origin.pdf
- Generative_AI_for_the_Optimization_of_Next-Generation_Wireless_Networks_Basics_State-of-the-Art_and_Open_Challenges.pdf-4f7173f3-facc-4451-819d-5e1664d5c20a/full.md
- Hierarchical_Aerial_Computing_for_Internet_of_Things_via_Cooperation_of_HAPs_and_UAVs.pdf-56b387f7-58b9-4a52-906e-813134bf5ffd/8011c826-f2ac-4903-afb0-d781ea9b50bb_origin.pdf
- Hierarchical_Aerial_Computing_for_Internet_of_Things_via_Cooperation_of_HAPs_and_UAVs.pdf-56b387f7-58b9-4a52-906e-813134bf5ffd/full.md
- Hybrid_OMA_NOMA_Mode_Selection_and_Resource_Allocation_in_Space-Air-Ground_Integrated_Networks.pdf-679ce336-ee6a-48b7-8df7-01515bfabee4/44d6771e-2771-4368-ad1b-636d2251d8a8_origin.pdf
- Hybrid_OMA_NOMA_Mode_Selection_and_Resource_Allocation_in_Space-Air-Ground_Integrated_Networks.pdf-679ce336-ee6a-48b7-8df7-01515bfabee4/full.md
- Integrated_Sensing_Computation_and_Communication_for_UAV-Assisted_Federated_Edge_Learning.pdf-a47cc7d0-89bb-4754-8dc3-e8116278c74c/bcf028aa-c5a5-4a9e-81e0-ab8face915e1_origin.pdf
- Integrated_Sensing_Computation_and_Communication_for_UAV-Assisted_Federated_Edge_Learning.pdf-a47cc7d0-89bb-4754-8dc3-e8116278c74c/full.md
- Joint_Computation_Offloading_and_Resource_Allocation_for_Uncertain_Maritime_MEC_via_Cooperation_of_AAVs_and_Vessels (1).pdf-91e3b716-7360-422e-b8b9-c393677b81a2/d4cfd60c-844d-4200-9959-58e733b9dd24_origin.pdf
- Joint_Computation_Offloading_and_Resource_Allocation_for_Uncertain_Maritime_MEC_via_Cooperation_of_AAVs_and_Vessels (1).pdf-91e3b716-7360-422e-b8b9-c393677b81a2/full.md
- Joint_Computation_Offloading_and_Resource_Allocation_for_Uncertain_Maritime_MEC_via_Cooperation_of_AAVs_and_Vessels.pdf-eaebb535-0215-4986-9ecb-d10ab9636d34/fbddd1eb-b302-42d7-9ec3-3b79705ca118_origin.pdf
- Joint_Computation_Offloading_and_Resource_Allocation_for_Uncertain_Maritime_MEC_via_Cooperation_of_AAVs_and_Vessels.pdf-eaebb535-0215-4986-9ecb-d10ab9636d34/full.md
- Joint_Computation_and_Communication_Design_for_UAV-Assisted_Mobile_Edge_Computing_in_IoT.pdf-44a43a9a-f78a-4bc7-8866-5a427dc2dd84/714dbdf1-14f0-4aa1-8086-94d182a61c42_origin.pdf
- Joint_Computation_and_Communication_Design_for_UAV-Assisted_Mobile_Edge_Computing_in_IoT.pdf-44a43a9a-f78a-4bc7-8866-5a427dc2dd84/full.md
- Joint_Content_Caching_Service_Placement_and_Task_Offloading_in_UAV-Enabled_Mobile_Edge_Computing_Networks.pdf-8bf88458-f2fd-409d-aeb8-95bbf7d99e02/2c7d63cc-6301-492b-b241-9d8cbb676fd1_origin.pdf
- Joint_Content_Caching_Service_Placement_and_Task_Offloading_in_UAV-Enabled_Mobile_Edge_Computing_Networks.pdf-8bf88458-f2fd-409d-aeb8-95bbf7d99e02/full.md
- Joint_Deployment_and_Task_Scheduling_Optimization_for_Large-Scale_Mobile_Users_in_Multi-UAV-Enabled_Mobile_Edge_Computing.pdf-b84a7da9-4775-4ce7-8476-a53afe2ac3a2/318c32ce-1de4-4b6e-933c-1dde4fe0af26_origin.pdf
- Joint_Deployment_and_Task_Scheduling_Optimization_for_Large-Scale_Mobile_Users_in_Multi-UAV-Enabled_Mobile_Edge_Computing.pdf-b84a7da9-4775-4ce7-8476-a53afe2ac3a2/full.md
- Joint_Resource_Management_for_Energy-Efficient_UAV-Assisted_SWIPT-MEC_A_Deep_Reinforcement_Learning_Approach (1).pdf-b7660096-a03d-41f1-95b4-6cf4ccd43277/89454a4b-6d60-4db8-bebf-117cc611ef74_origin.pdf
- Joint_Resource_Management_for_Energy-Efficient_UAV-Assisted_SWIPT-MEC_A_Deep_Reinforcement_Learning_Approach (1).pdf-b7660096-a03d-41f1-95b4-6cf4ccd43277/full.md
- Joint_Resource_Management_for_Energy-Efficient_UAV-Assisted_SWIPT-MEC_A_Deep_Reinforcement_Learning_Approach.pdf-47bc5eef-5351-4750-9de7-0a501e06f744/27aace2d-fd3d-44e6-ac23-4a2386878e16_origin.pdf
- Joint_Resource_Management_for_Energy-Efficient_UAV-Assisted_SWIPT-MEC_A_Deep_Reinforcement_Learning_Approach.pdf-47bc5eef-5351-4750-9de7-0a501e06f744/full.md
- Joint_Task_Offloading_and_Resource_Allocation_in_Aerial-Terrestrial_UAV_Networks_With_Edge_and_Fog_Computing_for_Post-Disaster_Rescue (1).pdf-fd9cea19-1e6e-485e-aca0-aee959424be4/c83b18ed-ed3b-4ee8-98d0-5f04b355c25e_origin.pdf
- Joint_Task_Offloading_and_Resource_Allocation_in_Aerial-Terrestrial_UAV_Networks_With_Edge_and_Fog_Computing_for_Post-Disaster_Rescue (1).pdf-fd9cea19-1e6e-485e-aca0-aee959424be4/full.md
- Joint_Task_Offloading_and_Resource_Allocation_in_Aerial-Terrestrial_UAV_Networks_With_Edge_and_Fog_Computing_for_Post-Disaster_Rescue.pdf-74335d9f-9e06-4894-8e8a-6509dab133ea/df69a884-40cb-4350-90d6-a800db943b8d_origin.pdf
- Joint_Task_Offloading_and_Resource_Allocation_in_Aerial-Terrestrial_UAV_Networks_With_Edge_and_Fog_Computing_for_Post-Disaster_Rescue.pdf-74335d9f-9e06-4894-8e8a-6509dab133ea/full.md
- Joint_Task_Offloading_and_Resource_Allocation_in_UAV-Enabled_Mobile_Edge_Computing.pdf-0322be8a-07c0-4a06-99bd-187903ec0903/fd834c11-797d-4d59-af05-b36b8e770e1f_origin.pdf
- Joint_Task_Offloading_and_Resource_Allocation_in_UAV-Enabled_Mobile_Edge_Computing.pdf-0322be8a-07c0-4a06-99bd-187903ec0903/full.md
- Learning-Based_NOMA-Enabled_Queue-Aware_Task_Offloading_and_AAV_3D_Trajectory_Planning_for_SAGIN.pdf-05cffc33-d988-4317-b3b9-40599b4925c3/f675e19d-5e65-4eca-b496-6ddf8afa66dc_origin.pdf
- Learning-Based_NOMA-Enabled_Queue-Aware_Task_Offloading_and_AAV_3D_Trajectory_Planning_for_SAGIN.pdf-05cffc33-d988-4317-b3b9-40599b4925c3/full.md
- MADDPG-Based_Joint_Service_Placement_and_Task_Offloading_in_MEC_Empowered_AirGround_Integrated_Networks.pdf-499bca38-d55d-47d6-800d-2457617637c7/391ad469-1677-4a96-9d65-31fc8fd0b258_origin.pdf
- MADDPG-Based_Joint_Service_Placement_and_Task_Offloading_in_MEC_Empowered_AirGround_Integrated_Networks.pdf-499bca38-d55d-47d6-800d-2457617637c7/full.md
- MOALF-UAV-MEC_Adaptive_Multiobjective_Optimization_for_UAV-Assisted_Mobile_Edge_Computing_in_Dynamic_IoT_Environments.pdf-c51ce6bd-3435-4f83-8376-d3afa6c27e23/5563cba4-a83a-4c1c-bf33-64bf581d6168_origin.pdf
- MOALF-UAV-MEC_Adaptive_Multiobjective_Optimization_for_UAV-Assisted_Mobile_Edge_Computing_in_Dynamic_IoT_Environments.pdf-c51ce6bd-3435-4f83-8376-d3afa6c27e23/full.md
- Mobile_Edge_Deployment_and_Resource_Management_for_Maritime_Wireless_Networks (1).pdf-b3cdff5e-bcb5-4b06-ab64-2c8528425226/5a91bf50-456a-46ea-b877-ad1927709055_origin.pdf
- Mobile_Edge_Deployment_and_Resource_Management_for_Maritime_Wireless_Networks (1).pdf-b3cdff5e-bcb5-4b06-ab64-2c8528425226/full.md
- Mobile_Edge_Deployment_and_Resource_Management_for_Maritime_Wireless_Networks.pdf-0e509116-0716-49db-9a8c-8435b2013eda/3de33e2c-c9c8-4276-8fd4-b9b6e4892eec_origin.pdf
- Mobile_Edge_Deployment_and_Resource_Management_for_Maritime_Wireless_Networks.pdf-0e509116-0716-49db-9a8c-8435b2013eda/full.md
- Multi-Agent_Deep_Reinforcement_Learning_for_Task_Offloading_in_UAV-Assisted_Mobile_Edge_Computing.pdf-f9e8af62-f654-406f-9d05-6a55d82e4b59/53b68eba-b73b-4572-9649-7095ccf72806_origin.pdf
- Multi-Agent_Deep_Reinforcement_Learning_for_Task_Offloading_in_UAV-Assisted_Mobile_Edge_Computing.pdf-f9e8af62-f654-406f-9d05-6a55d82e4b59/full.md
- Multi-Objective_Aerial_Collaborative_Secure_Communication_Optimization_via_Generative_Diffusion_Model-Enabled_Deep_Reinforcement_Learning.pdf-452e90cd-f3b0-4b86-ae3f-ec827a203c88/70a23b38-a360-4605-bd30-d5ae14ccd915_origin.pdf
- Multi-Objective_Aerial_Collaborative_Secure_Communication_Optimization_via_Generative_Diffusion_Model-Enabled_Deep_Reinforcement_Learning.pdf-452e90cd-f3b0-4b86-ae3f-ec827a203c88/full.md
- Multi-UAV_Cooperative_Task_Offloading_and_Resource_Allocation_in_5G_Advanced_and_Beyond (1).pdf-4b5ae9c1-7ea7-47cf-83c6-eb115da18d1b/49030327-45e9-40f6-9943-aad25ec486d1_origin.pdf
- Multi-UAV_Cooperative_Task_Offloading_and_Resource_Allocation_in_5G_Advanced_and_Beyond (1).pdf-4b5ae9c1-7ea7-47cf-83c6-eb115da18d1b/full.md
- Multi-UAV_Cooperative_Task_Offloading_and_Resource_Allocation_in_5G_Advanced_and_Beyond.pdf-7d6296bb-d664-4cbc-b5bc-15464d88f8b6/3e1c946c-3aca-4e6e-90a9-dad57bf77441_origin.pdf
- Multi-UAV_Cooperative_Task_Offloading_and_Resource_Allocation_in_5G_Advanced_and_Beyond.pdf-7d6296bb-d664-4cbc-b5bc-15464d88f8b6/full.md
- On_a_Hierarchical_Content_Caching_and_Asynchronous_Updating_Scheme_for_Non-Terrestrial_Network-Assisted_Connected_Automated_Vehicles.pdf-c776380e-4794-4255-a9d3-8f3f6e7cac8c/f75a75c7-9364-4126-8bd3-c62492c2f272_origin.pdf
- On_a_Hierarchical_Content_Caching_and_Asynchronous_Updating_Scheme_for_Non-Terrestrial_Network-Assisted_Connected_Automated_Vehicles.pdf-c776380e-4794-4255-a9d3-8f3f6e7cac8c/full.md
- Online_Trajectory_and_Resource_Optimization_for_Stochastic_UAV-Enabled_MEC_Systems.pdf-20fd4e85-7fb0-4689-b4ce-161e6bf84a78/30cc749a-4be7-47fe-8892-b46a5f122267_origin.pdf
- Online_Trajectory_and_Resource_Optimization_for_Stochastic_UAV-Enabled_MEC_Systems.pdf-20fd4e85-7fb0-4689-b4ce-161e6bf84a78/full.md
- Over-the-Air_Edge_Inference_for_Low-Altitude_Airspace_Generative_AI-Aided_Multi-Task_Batching_and_Beamforming_Design.pdf-71716721-2d3b-4111-95d2-a6af53e729df/6d668a50-906d-42d0-9e25-2095ab35fd4a_origin.pdf
- Over-the-Air_Edge_Inference_for_Low-Altitude_Airspace_Generative_AI-Aided_Multi-Task_Batching_and_Beamforming_Design.pdf-71716721-2d3b-4111-95d2-a6af53e729df/full.md
- Resource_Allocation_and_Trajectory_Design_for_MISO_UAV-Assisted_MEC_Networks.pdf-e50d30a0-5766-49c1-abc6-e1f69c842cc8/2baa483c-d5f2-4cc5-8924-3e5795ef84c3_origin.pdf
- Resource_Allocation_and_Trajectory_Design_for_MISO_UAV-Assisted_MEC_Networks.pdf-e50d30a0-5766-49c1-abc6-e1f69c842cc8/full.md
- Trajectory_Design_and_Resource_Allocation_for_Multi-UAV_Networks_Deep_Reinforcement_Learning_Approaches.pdf-0c90fd1c-4973-4db5-b6ad-ec795389037d/a578795f-48fe-44c7-8b8a-905efa289a02_origin.pdf
- Trajectory_Design_and_Resource_Allocation_for_Multi-UAV_Networks_Deep_Reinforcement_Learning_Approaches.pdf-0c90fd1c-4973-4db5-b6ad-ec795389037d/full.md
- Two-Hop_Partial_Task_Offloading_and_Resource_Allocation_in_AirGround_Integrated_Mobile_Edge_Computing_Network_A_DRL-Based_Method.pdf-ab2d992d-223a-4d34-b728-342bef620ffa/6228b26c-2629-40a4-824a-8ab71fafd31c_origin.pdf
- Two-Hop_Partial_Task_Offloading_and_Resource_Allocation_in_AirGround_Integrated_Mobile_Edge_Computing_Network_A_DRL-Based_Method.pdf-ab2d992d-223a-4d34-b728-342bef620ffa/full.md
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach (1).pdf-7e7c4eae-df09-4eba-8cf6-7cbd2c0ddb48/b895da1a-b0ce-46d1-9277-80d80bba8c58_origin.pdf
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach (1).pdf-7e7c4eae-df09-4eba-8cf6-7cbd2c0ddb48/full.md
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach (2).pdf-526772e9-23ae-4033-a337-92c254254ba5/16d5d3d1-67b2-4dd9-b065-9e963d14a649_origin.pdf
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach (2).pdf-526772e9-23ae-4033-a337-92c254254ba5/full.md
- UAV-Assisted_Task_Offloading_in_Edge_Computing.pdf-7b5a37ae-a1c8-45b0-b75f-43d8e45259fb/29225c6d-e56f-4b9d-8974-8a76c9df34b5_origin.pdf
- UAV-Assisted_Task_Offloading_in_Edge_Computing.pdf-7b5a37ae-a1c8-45b0-b75f-43d8e45259fb/full.md
- UAV-Enabled_Integrated_Sensing_and_Communication_Opportunities_and_Challenges.pdf-c4dc78f8-13e6-4e67-89e0-b02a0e841e4b/a8642c8e-2515-4841-8dc0-6d98cbff3be7_origin.pdf
- UAV-Enabled_Integrated_Sensing_and_Communication_Opportunities_and_Challenges.pdf-c4dc78f8-13e6-4e67-89e0-b02a0e841e4b/full.md
- UAV-Enabled_Secure_ISAC_Against_Dual_Eavesdropping_Threats_Joint_Beamforming_and_Trajectory_Design.pdf-1f6af962-48a0-426f-a0db-ee2a8aa1b454/b189403a-de1d-405c-839d-7c4db1c48c4b_origin.pdf
- UAV-Enabled_Secure_ISAC_Against_Dual_Eavesdropping_Threats_Joint_Beamforming_and_Trajectory_Design.pdf-1f6af962-48a0-426f-a0db-ee2a8aa1b454/full.md
## [2026-05-29] external batch delete | 108 source files

Deleted 108 source files and 0 wiki pages.

Sources:
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-01e5dcd4-c51d-4f14-9188-54506cc73225/6d675f02-2610-41f9-8d08-e81e2f69eb79_origin.pdf
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-01e5dcd4-c51d-4f14-9188-54506cc73225/full.md
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-0322be8a-07c0-4a06-99bd-187903ec0903/fd834c11-797d-4d59-af05-b36b8e770e1f_origin.pdf
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-0322be8a-07c0-4a06-99bd-187903ec0903/full.md
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-05cffc33-d988-4317-b3b9-40599b4925c3/f675e19d-5e65-4eca-b496-6ddf8afa66dc_origin.pdf
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-05cffc33-d988-4317-b3b9-40599b4925c3/full.md
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-09d5418e-dc62-4524-bc97-f89ba95dfc7e/1058f15e-3289-44ba-a46f-79175aa42220_origin.pdf
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-09d5418e-dc62-4524-bc97-f89ba95dfc7e/full.md
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-0c90fd1c-4973-4db5-b6ad-ec795389037d/a578795f-48fe-44c7-8b8a-905efa289a02_origin.pdf
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-0c90fd1c-4973-4db5-b6ad-ec795389037d/full.md
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-0e2c9ca7-5f3c-4ede-a338-873da62ae161/69f11249-178f-489a-99dd-6013be4a2178_origin.pdf
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-0e2c9ca7-5f3c-4ede-a338-873da62ae161/full.md
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-0e509116-0716-49db-9a8c-8435b2013eda/3de33e2c-c9c8-4276-8fd4-b9b6e4892eec_origin.pdf
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-0e509116-0716-49db-9a8c-8435b2013eda/full.md
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-101d96ec-b13f-4bc2-81ba-f99b04be10eb/3d74f158-5928-492f-a341-867a10312574_origin.pdf
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-101d96ec-b13f-4bc2-81ba-f99b04be10eb/full.md
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-1f6af962-48a0-426f-a0db-ee2a8aa1b454/b189403a-de1d-405c-839d-7c4db1c48c4b_origin.pdf
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-1f6af962-48a0-426f-a0db-ee2a8aa1b454/full.md
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-20fd4e85-7fb0-4689-b4ce-161e6bf84a78/30cc749a-4be7-47fe-8892-b46a5f122267_origin.pdf
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-20fd4e85-7fb0-4689-b4ce-161e6bf84a78/full.md
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-226bcccd-9b0e-49f9-b0c1-cba631461523/05cc59c4-a99e-447a-9f94-9002dcc71c45_origin.pdf
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-226bcccd-9b0e-49f9-b0c1-cba631461523/full.md
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-35b8645f-ec67-4bc8-a322-f2d67eb162f1/04bff10e-4497-45a2-a8ac-d649dc9ccda9_origin.pdf
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-35b8645f-ec67-4bc8-a322-f2d67eb162f1/full.md
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-37e49c9e-f1cf-45f8-b0ad-c274f146debb/52184245-a588-46d7-8436-664582f236ae_origin.pdf
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-37e49c9e-f1cf-45f8-b0ad-c274f146debb/full.md
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-38308eaa-ccf0-4fd8-abc2-904d6e06df92/a4df4525-9548-41ce-848a-b64ff3be183c_origin.pdf
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-38308eaa-ccf0-4fd8-abc2-904d6e06df92/full.md
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-44a43a9a-f78a-4bc7-8866-5a427dc2dd84/714dbdf1-14f0-4aa1-8086-94d182a61c42_origin.pdf
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-44a43a9a-f78a-4bc7-8866-5a427dc2dd84/full.md
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-452e90cd-f3b0-4b86-ae3f-ec827a203c88/70a23b38-a360-4605-bd30-d5ae14ccd915_origin.pdf
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-452e90cd-f3b0-4b86-ae3f-ec827a203c88/full.md
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-47bc5eef-5351-4750-9de7-0a501e06f744/27aace2d-fd3d-44e6-ac23-4a2386878e16_origin.pdf
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-47bc5eef-5351-4750-9de7-0a501e06f744/full.md
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-499bca38-d55d-47d6-800d-2457617637c7/391ad469-1677-4a96-9d65-31fc8fd0b258_origin.pdf
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-499bca38-d55d-47d6-800d-2457617637c7/full.md
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-4b5ae9c1-7ea7-47cf-83c6-eb115da18d1b/49030327-45e9-40f6-9943-aad25ec486d1_origin.pdf
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-4b5ae9c1-7ea7-47cf-83c6-eb115da18d1b/full.md
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-4f7173f3-facc-4451-819d-5e1664d5c20a/c848f928-34e9-426d-8306-3e39ef4ce670_origin.pdf
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-4f7173f3-facc-4451-819d-5e1664d5c20a/full.md
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-526772e9-23ae-4033-a337-92c254254ba5/16d5d3d1-67b2-4dd9-b065-9e963d14a649_origin.pdf
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-526772e9-23ae-4033-a337-92c254254ba5/full.md
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-56b387f7-58b9-4a52-906e-813134bf5ffd/8011c826-f2ac-4903-afb0-d781ea9b50bb_origin.pdf
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-56b387f7-58b9-4a52-906e-813134bf5ffd/full.md
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-679ce336-ee6a-48b7-8df7-01515bfabee4/44d6771e-2771-4368-ad1b-636d2251d8a8_origin.pdf
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-679ce336-ee6a-48b7-8df7-01515bfabee4/full.md
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-680ca83e-ffea-41f9-bc61-85b9b15a2b82/a6533d10-e97c-4756-a27b-ce396e62927d_origin.pdf
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-680ca83e-ffea-41f9-bc61-85b9b15a2b82/full.md
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-6a127707-a8c8-4eb3-95db-bd84451c63bb/5805eb5a-c860-435a-a363-c7e08e58d364_origin.pdf
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-6a127707-a8c8-4eb3-95db-bd84451c63bb/full.md
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-71716721-2d3b-4111-95d2-a6af53e729df/6d668a50-906d-42d0-9e25-2095ab35fd4a_origin.pdf
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-71716721-2d3b-4111-95d2-a6af53e729df/full.md
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-74335d9f-9e06-4894-8e8a-6509dab133ea/df69a884-40cb-4350-90d6-a800db943b8d_origin.pdf
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-74335d9f-9e06-4894-8e8a-6509dab133ea/full.md
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-7b5a37ae-a1c8-45b0-b75f-43d8e45259fb/29225c6d-e56f-4b9d-8974-8a76c9df34b5_origin.pdf
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-7b5a37ae-a1c8-45b0-b75f-43d8e45259fb/full.md
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-7cbb1edb-d3d9-4aaa-bc82-b01707e227e1/c2b3ff92-9440-484e-82ac-7c26f755903f_origin.pdf
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-7cbb1edb-d3d9-4aaa-bc82-b01707e227e1/full.md
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-7d6296bb-d664-4cbc-b5bc-15464d88f8b6/3e1c946c-3aca-4e6e-90a9-dad57bf77441_origin.pdf
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-7d6296bb-d664-4cbc-b5bc-15464d88f8b6/full.md
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-7e7c4eae-df09-4eba-8cf6-7cbd2c0ddb48/b895da1a-b0ce-46d1-9277-80d80bba8c58_origin.pdf
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-7e7c4eae-df09-4eba-8cf6-7cbd2c0ddb48/full.md
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-8bf88458-f2fd-409d-aeb8-95bbf7d99e02/2c7d63cc-6301-492b-b241-9d8cbb676fd1_origin.pdf
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-8bf88458-f2fd-409d-aeb8-95bbf7d99e02/full.md
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-91e3b716-7360-422e-b8b9-c393677b81a2/d4cfd60c-844d-4200-9959-58e733b9dd24_origin.pdf
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-91e3b716-7360-422e-b8b9-c393677b81a2/full.md
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-92c33306-3b00-4a98-b7c0-b613ac6e3565/d17bf5a0-218d-4917-b746-6fc2a408824f_origin.pdf
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-92c33306-3b00-4a98-b7c0-b613ac6e3565/full.md
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-98452b41-2b96-41cd-9223-132cf959a545/51a15428-6640-4700-b016-4294726d6ad3_origin.pdf
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-98452b41-2b96-41cd-9223-132cf959a545/full.md
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-a0ebded2-6b19-49ef-82a8-a60fe98bd9a3/1bf62391-2d01-4b85-a2dd-44c3f6bfa9e9_origin.pdf
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-a0ebded2-6b19-49ef-82a8-a60fe98bd9a3/full.md
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-a47cc7d0-89bb-4754-8dc3-e8116278c74c/bcf028aa-c5a5-4a9e-81e0-ab8face915e1_origin.pdf
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-a47cc7d0-89bb-4754-8dc3-e8116278c74c/full.md
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-ab2d992d-223a-4d34-b728-342bef620ffa/6228b26c-2629-40a4-824a-8ab71fafd31c_origin.pdf
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-ab2d992d-223a-4d34-b728-342bef620ffa/full.md
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-b3cdff5e-bcb5-4b06-ab64-2c8528425226/5a91bf50-456a-46ea-b877-ad1927709055_origin.pdf
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-b3cdff5e-bcb5-4b06-ab64-2c8528425226/full.md
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-b7660096-a03d-41f1-95b4-6cf4ccd43277/89454a4b-6d60-4db8-bebf-117cc611ef74_origin.pdf
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-b7660096-a03d-41f1-95b4-6cf4ccd43277/full.md
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-b84a7da9-4775-4ce7-8476-a53afe2ac3a2/318c32ce-1de4-4b6e-933c-1dde4fe0af26_origin.pdf
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-b84a7da9-4775-4ce7-8476-a53afe2ac3a2/full.md
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-bea3bbdb-b210-4313-bfeb-c98d7e4f95b2/51f1dd7a-88b5-4325-80ed-9c8336415dc9_origin.pdf
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-bea3bbdb-b210-4313-bfeb-c98d7e4f95b2/full.md
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-bf127b65-b284-404b-8ac3-337dd3a7759a/c0f2255d-e21b-42aa-8b98-d86bd3126819_origin.pdf
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-bf127b65-b284-404b-8ac3-337dd3a7759a/full.md
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-c4dc78f8-13e6-4e67-89e0-b02a0e841e4b/a8642c8e-2515-4841-8dc0-6d98cbff3be7_origin.pdf
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-c4dc78f8-13e6-4e67-89e0-b02a0e841e4b/full.md
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-c507d9c3-154e-4854-a5ce-4dd59d952c35/1d881528-e07b-4227-bdd8-2c2bfcaecc08_origin.pdf
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-c507d9c3-154e-4854-a5ce-4dd59d952c35/full.md
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-c51ce6bd-3435-4f83-8376-d3afa6c27e23/5563cba4-a83a-4c1c-bf33-64bf581d6168_origin.pdf
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-c51ce6bd-3435-4f83-8376-d3afa6c27e23/full.md
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-c776380e-4794-4255-a9d3-8f3f6e7cac8c/f75a75c7-9364-4126-8bd3-c62492c2f272_origin.pdf
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-c776380e-4794-4255-a9d3-8f3f6e7cac8c/full.md
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-cd5196f5-a52f-4b9d-82ad-c1b50996a79e/17b265eb-d64b-4b6d-9e41-bc3f6577f29b_origin.pdf
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-cd5196f5-a52f-4b9d-82ad-c1b50996a79e/full.md
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-e50024c1-4074-48e8-95c0-fc9d69153fec/54556004-5e12-446c-a020-2ca85e5d4fb8_origin.pdf
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-e50024c1-4074-48e8-95c0-fc9d69153fec/full.md
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-e50d30a0-5766-49c1-abc6-e1f69c842cc8/2baa483c-d5f2-4cc5-8924-3e5795ef84c3_origin.pdf
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-e50d30a0-5766-49c1-abc6-e1f69c842cc8/full.md
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-e9ad5584-e837-47c7-8889-5491ce20b0ad/a7af4c61-064d-406a-8b3b-f4408286873c_origin.pdf
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-e9ad5584-e837-47c7-8889-5491ce20b0ad/full.md
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-eaebb535-0215-4986-9ecb-d10ab9636d34/fbddd1eb-b302-42d7-9ec3-3b79705ca118_origin.pdf
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-eaebb535-0215-4986-9ecb-d10ab9636d34/full.md
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-f9e8af62-f654-406f-9d05-6a55d82e4b59/53b68eba-b73b-4572-9649-7095ccf72806_origin.pdf
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-f9e8af62-f654-406f-9d05-6a55d82e4b59/full.md
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-fd9cea19-1e6e-485e-aca0-aee959424be4/c83b18ed-ed3b-4ee8-98d0-5f04b355c25e_origin.pdf
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-fd9cea19-1e6e-485e-aca0-aee959424be4/full.md
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- UAV-Enabled_Integrated_Sensing_and_Communication_Opportunities_and_Challenges.pdf-c4dc78f8-13e6-4e67-89e0-b02a0e841e4b/a8642c8e-2515-4841-8dc0-6d98cbff3be7_origin.pdf
- UAV-Enabled_Integrated_Sensing_and_Communication_Opportunities_and_Challenges.pdf-c4dc78f8-13e6-4e67-89e0-b02a0e841e4b/full.md
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- UAV-Enabled_Secure_ISAC_Against_Dual_Eavesdropping_Threats_Joint_Beamforming_and_Trajectory_Design.pdf-1f6af962-48a0-426f-a0db-ee2a8aa1b454/b189403a-de1d-405c-839d-7c4db1c48c4b_origin.pdf
- UAV-Enabled_Secure_ISAC_Against_Dual_Eavesdropping_Threats_Joint_Beamforming_and_Trajectory_Design.pdf-1f6af962-48a0-426f-a0db-ee2a8aa1b454/full.md
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- Conditional_Generative_Adversarial_Networks_for_Channel_Estimation_in_RIS-Assisted_ISAC_Systems.pdf-92c33306-3b00-4a98-b7c0-b613ac6e3565/d17bf5a0-218d-4917-b746-6fc2a408824f_origin.pdf
- Conditional_Generative_Adversarial_Networks_for_Channel_Estimation_in_RIS-Assisted_ISAC_Systems.pdf-92c33306-3b00-4a98-b7c0-b613ac6e3565/full.md
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- Cooperative_UAV_Resource_Allocation_and_Task_Offloading_in_Hierarchical_Aerial_Computing_Systems_A_MAPPO-Based_Approach.pdf-680ca83e-ffea-41f9-bc61-85b9b15a2b82/a6533d10-e97c-4756-a27b-ce396e62927d_origin.pdf
- Cooperative_UAV_Resource_Allocation_and_Task_Offloading_in_Hierarchical_Aerial_Computing_Systems_A_MAPPO-Based_Approach.pdf-680ca83e-ffea-41f9-bc61-85b9b15a2b82/full.md
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- Distributed_Foundation_Models_for_Multi-Modal_Learning_in_6G_Wireless_Networks (1).pdf-37e49c9e-f1cf-45f8-b0ad-c274f146debb/52184245-a588-46d7-8436-664582f236ae_origin.pdf
- Distributed_Foundation_Models_for_Multi-Modal_Learning_in_6G_Wireless_Networks (1).pdf-37e49c9e-f1cf-45f8-b0ad-c274f146debb/full.md
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- Double-Edge-Assisted_Computation_Offloading_and_Resource_Allocation_for_Space-Air-Marine_Integrated_Networks (1).pdf-101d96ec-b13f-4bc2-81ba-f99b04be10eb/3d74f158-5928-492f-a341-867a10312574_origin.pdf
- Double-Edge-Assisted_Computation_Offloading_and_Resource_Allocation_for_Space-Air-Marine_Integrated_Networks (1).pdf-101d96ec-b13f-4bc2-81ba-f99b04be10eb/full.md
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- Generative-Adversarial-Network-Enhanced_DRL_for_ISAC_With_Double_Active_RISs.pdf-e50024c1-4074-48e8-95c0-fc9d69153fec/54556004-5e12-446c-a020-2ca85e5d4fb8_origin.pdf
- Generative-Adversarial-Network-Enhanced_DRL_for_ISAC_With_Double_Active_RISs.pdf-e50024c1-4074-48e8-95c0-fc9d69153fec/full.md
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach (2).pdf-526772e9-23ae-4033-a337-92c254254ba5/16d5d3d1-67b2-4dd9-b065-9e963d14a649_origin.pdf
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach (2).pdf-526772e9-23ae-4033-a337-92c254254ba5/full.md
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- Energy_Efficient_Task_Offloading_and_Resource_Allocation_in_Air-Ground_Integrated_MEC_Systems_A_Distributed_Online_Approach (2).pdf-0e2c9ca7-5f3c-4ede-a338-873da62ae161/69f11249-178f-489a-99dd-6013be4a2178_origin.pdf
- Energy_Efficient_Task_Offloading_and_Resource_Allocation_in_Air-Ground_Integrated_MEC_Systems_A_Distributed_Online_Approach (2).pdf-0e2c9ca7-5f3c-4ede-a338-873da62ae161/full.md
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- Generative_AI_for_the_Optimization_of_Next-Generation_Wireless_Networks_Basics_State-of-the-Art_and_Open_Challenges.pdf-4f7173f3-facc-4451-819d-5e1664d5c20a/c848f928-34e9-426d-8306-3e39ef4ce670_origin.pdf
- Generative_AI_for_the_Optimization_of_Next-Generation_Wireless_Networks_Basics_State-of-the-Art_and_Open_Challenges.pdf-4f7173f3-facc-4451-819d-5e1664d5c20a/full.md
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- Joint_Computation_and_Communication_Design_for_UAV-Assisted_Mobile_Edge_Computing_in_IoT.pdf-44a43a9a-f78a-4bc7-8866-5a427dc2dd84/714dbdf1-14f0-4aa1-8086-94d182a61c42_origin.pdf
- Joint_Computation_and_Communication_Design_for_UAV-Assisted_Mobile_Edge_Computing_in_IoT.pdf-44a43a9a-f78a-4bc7-8866-5a427dc2dd84/full.md
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- Joint_Computation_Offloading_and_Resource_Allocation_for_Uncertain_Maritime_MEC_via_Cooperation_of_AAVs_and_Vessels (1).pdf-91e3b716-7360-422e-b8b9-c393677b81a2/d4cfd60c-844d-4200-9959-58e733b9dd24_origin.pdf
- Joint_Computation_Offloading_and_Resource_Allocation_for_Uncertain_Maritime_MEC_via_Cooperation_of_AAVs_and_Vessels (1).pdf-91e3b716-7360-422e-b8b9-c393677b81a2/full.md
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- Multi-Objective_Aerial_Collaborative_Secure_Communication_Optimization_via_Generative_Diffusion_Model-Enabled_Deep_Reinforcement_Learning.pdf-452e90cd-f3b0-4b86-ae3f-ec827a203c88/70a23b38-a360-4605-bd30-d5ae14ccd915_origin.pdf
- Multi-Objective_Aerial_Collaborative_Secure_Communication_Optimization_via_Generative_Diffusion_Model-Enabled_Deep_Reinforcement_Learning.pdf-452e90cd-f3b0-4b86-ae3f-ec827a203c88/full.md
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- Energy_Oriented_Three-Tier_Computation_Offloading_Scheme_in_Maritime_Edge_Computing_Network (1).pdf-c507d9c3-154e-4854-a5ce-4dd59d952c35/1d881528-e07b-4227-bdd8-2c2bfcaecc08_origin.pdf
- Energy_Oriented_Three-Tier_Computation_Offloading_Scheme_in_Maritime_Edge_Computing_Network (1).pdf-c507d9c3-154e-4854-a5ce-4dd59d952c35/full.md
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- Joint_Deployment_and_Task_Scheduling_Optimization_for_Large-Scale_Mobile_Users_in_Multi-UAV-Enabled_Mobile_Edge_Computing.pdf-b84a7da9-4775-4ce7-8476-a53afe2ac3a2/318c32ce-1de4-4b6e-933c-1dde4fe0af26_origin.pdf
- Joint_Deployment_and_Task_Scheduling_Optimization_for_Large-Scale_Mobile_Users_in_Multi-UAV-Enabled_Mobile_Edge_Computing.pdf-b84a7da9-4775-4ce7-8476-a53afe2ac3a2/full.md
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- Joint_Resource_Management_for_Energy-Efficient_UAV-Assisted_SWIPT-MEC_A_Deep_Reinforcement_Learning_Approach (1).pdf-b7660096-a03d-41f1-95b4-6cf4ccd43277/89454a4b-6d60-4db8-bebf-117cc611ef74_origin.pdf
- Joint_Resource_Management_for_Energy-Efficient_UAV-Assisted_SWIPT-MEC_A_Deep_Reinforcement_Learning_Approach (1).pdf-b7660096-a03d-41f1-95b4-6cf4ccd43277/full.md
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- Mobile_Edge_Deployment_and_Resource_Management_for_Maritime_Wireless_Networks (1).pdf-b3cdff5e-bcb5-4b06-ab64-2c8528425226/5a91bf50-456a-46ea-b877-ad1927709055_origin.pdf
- Mobile_Edge_Deployment_and_Resource_Management_for_Maritime_Wireless_Networks (1).pdf-b3cdff5e-bcb5-4b06-ab64-2c8528425226/full.md
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- Multi-UAV_Cooperative_Task_Offloading_and_Resource_Allocation_in_5G_Advanced_and_Beyond (1).pdf-4b5ae9c1-7ea7-47cf-83c6-eb115da18d1b/49030327-45e9-40f6-9943-aad25ec486d1_origin.pdf
- Multi-UAV_Cooperative_Task_Offloading_and_Resource_Allocation_in_5G_Advanced_and_Beyond (1).pdf-4b5ae9c1-7ea7-47cf-83c6-eb115da18d1b/full.md
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- Evolutionary_Multi-Objective_Reinforcement_Learning_Based_Trajectory_Control_and_Task_Offloading_in_UAV-Assisted_Mobile_Edge_Computing.pdf-01e5dcd4-c51d-4f14-9188-54506cc73225/6d675f02-2610-41f9-8d08-e81e2f69eb79_origin.pdf
- Evolutionary_Multi-Objective_Reinforcement_Learning_Based_Trajectory_Control_and_Task_Offloading_in_UAV-Assisted_Mobile_Edge_Computing.pdf-01e5dcd4-c51d-4f14-9188-54506cc73225/full.md
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- Online_Trajectory_and_Resource_Optimization_for_Stochastic_UAV-Enabled_MEC_Systems.pdf-20fd4e85-7fb0-4689-b4ce-161e6bf84a78/30cc749a-4be7-47fe-8892-b46a5f122267_origin.pdf
- Online_Trajectory_and_Resource_Optimization_for_Stochastic_UAV-Enabled_MEC_Systems.pdf-20fd4e85-7fb0-4689-b4ce-161e6bf84a78/full.md
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- Resource_Allocation_and_Trajectory_Design_for_MISO_UAV-Assisted_MEC_Networks.pdf-e50d30a0-5766-49c1-abc6-e1f69c842cc8/2baa483c-d5f2-4cc5-8924-3e5795ef84c3_origin.pdf
- Resource_Allocation_and_Trajectory_Design_for_MISO_UAV-Assisted_MEC_Networks.pdf-e50d30a0-5766-49c1-abc6-e1f69c842cc8/full.md
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- Energy_Efficient_Task_Offloading_and_Resource_Allocation_in_Air-Ground_Integrated_MEC_Systems_A_Distributed_Online_Approach (1).pdf-e9ad5584-e837-47c7-8889-5491ce20b0ad/a7af4c61-064d-406a-8b3b-f4408286873c_origin.pdf
- Energy_Efficient_Task_Offloading_and_Resource_Allocation_in_Air-Ground_Integrated_MEC_Systems_A_Distributed_Online_Approach (1).pdf-e9ad5584-e837-47c7-8889-5491ce20b0ad/full.md
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- Hierarchical_Aerial_Computing_for_Internet_of_Things_via_Cooperation_of_HAPs_and_UAVs.pdf-56b387f7-58b9-4a52-906e-813134bf5ffd/8011c826-f2ac-4903-afb0-d781ea9b50bb_origin.pdf
- Hierarchical_Aerial_Computing_for_Internet_of_Things_via_Cooperation_of_HAPs_and_UAVs.pdf-56b387f7-58b9-4a52-906e-813134bf5ffd/full.md
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- Joint_Task_Offloading_and_Resource_Allocation_in_Aerial-Terrestrial_UAV_Networks_With_Edge_and_Fog_Computing_for_Post-Disaster_Rescue (1).pdf-fd9cea19-1e6e-485e-aca0-aee959424be4/c83b18ed-ed3b-4ee8-98d0-5f04b355c25e_origin.pdf
- Joint_Task_Offloading_and_Resource_Allocation_in_Aerial-Terrestrial_UAV_Networks_With_Edge_and_Fog_Computing_for_Post-Disaster_Rescue (1).pdf-fd9cea19-1e6e-485e-aca0-aee959424be4/full.md
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- Multi-Agent_Deep_Reinforcement_Learning_for_Task_Offloading_in_UAV-Assisted_Mobile_Edge_Computing.pdf-f9e8af62-f654-406f-9d05-6a55d82e4b59/53b68eba-b73b-4572-9649-7095ccf72806_origin.pdf
- Multi-Agent_Deep_Reinforcement_Learning_for_Task_Offloading_in_UAV-Assisted_Mobile_Edge_Computing.pdf-f9e8af62-f654-406f-9d05-6a55d82e4b59/full.md
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- Trajectory_Design_and_Resource_Allocation_for_Multi-UAV_Networks_Deep_Reinforcement_Learning_Approaches.pdf-0c90fd1c-4973-4db5-b6ad-ec795389037d/a578795f-48fe-44c7-8b8a-905efa289a02_origin.pdf
- Trajectory_Design_and_Resource_Allocation_for_Multi-UAV_Networks_Deep_Reinforcement_Learning_Approaches.pdf-0c90fd1c-4973-4db5-b6ad-ec795389037d/full.md
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach (1).pdf-7e7c4eae-df09-4eba-8cf6-7cbd2c0ddb48/b895da1a-b0ce-46d1-9277-80d80bba8c58_origin.pdf
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach (1).pdf-7e7c4eae-df09-4eba-8cf6-7cbd2c0ddb48/full.md
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- A_Survey_on_Mobile_Edge_Computing_The_Communication_Perspective.pdf-38308eaa-ccf0-4fd8-abc2-904d6e06df92/a4df4525-9548-41ce-848a-b64ff3be183c_origin.pdf
- A_Survey_on_Mobile_Edge_Computing_The_Communication_Perspective.pdf-38308eaa-ccf0-4fd8-abc2-904d6e06df92/full.md
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- ACBFT_Adaptive_Chained_Byzantine_Fault-Tolerant_Consensus_Protocol_for_UAV_Ad_Hoc_Networks.pdf-bea3bbdb-b210-4313-bfeb-c98d7e4f95b2/51f1dd7a-88b5-4325-80ed-9c8336415dc9_origin.pdf
- ACBFT_Adaptive_Chained_Byzantine_Fault-Tolerant_Consensus_Protocol_for_UAV_Ad_Hoc_Networks.pdf-bea3bbdb-b210-4313-bfeb-c98d7e4f95b2/full.md
## [2026-05-29] external delete | Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-06d6b36c-df8c-4a15-b409-1bb529f57e89/870fe0f8-bcb9-4139-95ef-9aecd3daea78_origin.pdf

Deleted 1 source file and 0 wiki pages.
## [2026-05-29] external delete | Double-Edge-Assisted_Computation_Offloading_and_Resource_Allocation_for_Space-Air-Marine_Integrated_Networks.pdf-98452b41-2b96-41cd-9223-132cf959a545/51a15428-6640-4700-b016-4294726d6ad3_origin.pdf

Deleted 1 source file and 0 wiki pages.
## [2026-05-29] external delete | Double-Edge-Assisted_Computation_Offloading_and_Resource_Allocation_for_Space-Air-Marine_Integrated_Networks.pdf-98452b41-2b96-41cd-9223-132cf959a545/full.md

Deleted 1 source file and 0 wiki pages.
## [2026-05-29] external delete | Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach.pdf-06d6b36c-df8c-4a15-b409-1bb529f57e89/full.md

Deleted 1 source file and 0 wiki pages.
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- Integrated_Sensing_Computation_and_Communication_for_UAV-Assisted_Federated_Edge_Learning.pdf-a47cc7d0-89bb-4754-8dc3-e8116278c74c/bcf028aa-c5a5-4a9e-81e0-ab8face915e1_origin.pdf
- Integrated_Sensing_Computation_and_Communication_for_UAV-Assisted_Federated_Edge_Learning.pdf-a47cc7d0-89bb-4754-8dc3-e8116278c74c/full.md
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- Joint_Content_Caching_Service_Placement_and_Task_Offloading_in_UAV-Enabled_Mobile_Edge_Computing_Networks.pdf-8bf88458-f2fd-409d-aeb8-95bbf7d99e02/2c7d63cc-6301-492b-b241-9d8cbb676fd1_origin.pdf
- Joint_Content_Caching_Service_Placement_and_Task_Offloading_in_UAV-Enabled_Mobile_Edge_Computing_Networks.pdf-8bf88458-f2fd-409d-aeb8-95bbf7d99e02/full.md
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- On_a_Hierarchical_Content_Caching_and_Asynchronous_Updating_Scheme_for_Non-Terrestrial_Network-Assisted_Connected_Automated_Vehicles.pdf-c776380e-4794-4255-a9d3-8f3f6e7cac8c/f75a75c7-9364-4126-8bd3-c62492c2f272_origin.pdf
- On_a_Hierarchical_Content_Caching_and_Asynchronous_Updating_Scheme_for_Non-Terrestrial_Network-Assisted_Connected_Automated_Vehicles.pdf-c776380e-4794-4255-a9d3-8f3f6e7cac8c/full.md
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- UAV-Assisted_Task_Offloading_in_Edge_Computing.pdf-7b5a37ae-a1c8-45b0-b75f-43d8e45259fb/29225c6d-e56f-4b9d-8974-8a76c9df34b5_origin.pdf
- UAV-Assisted_Task_Offloading_in_Edge_Computing.pdf-7b5a37ae-a1c8-45b0-b75f-43d8e45259fb/full.md
## [2026-05-29] external delete | Energy_Oriented_Three-Tier_Computation_Offloading_Scheme_in_Maritime_Edge_Computing_Network.pdf-226bcccd-9b0e-49f9-b0c1-cba631461523/05cc59c4-a99e-447a-9f94-9002dcc71c45_origin.pdf

Deleted 1 source file and 0 wiki pages.
## [2026-05-29] external delete | Energy_Oriented_Three-Tier_Computation_Offloading_Scheme_in_Maritime_Edge_Computing_Network.pdf-226bcccd-9b0e-49f9-b0c1-cba631461523/full.md

Deleted 1 source file and 0 wiki pages.
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- Joint_Computation_Offloading_and_Resource_Allocation_for_Uncertain_Maritime_MEC_via_Cooperation_of_AAVs_and_Vessels.pdf-eaebb535-0215-4986-9ecb-d10ab9636d34/fbddd1eb-b302-42d7-9ec3-3b79705ca118_origin.pdf
- Joint_Computation_Offloading_and_Resource_Allocation_for_Uncertain_Maritime_MEC_via_Cooperation_of_AAVs_and_Vessels.pdf-eaebb535-0215-4986-9ecb-d10ab9636d34/full.md
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- Joint_Task_Offloading_and_Resource_Allocation_in_UAV-Enabled_Mobile_Edge_Computing.pdf-0322be8a-07c0-4a06-99bd-187903ec0903/fd834c11-797d-4d59-af05-b36b8e770e1f_origin.pdf
- Joint_Task_Offloading_and_Resource_Allocation_in_UAV-Enabled_Mobile_Edge_Computing.pdf-0322be8a-07c0-4a06-99bd-187903ec0903/full.md
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- Two-Hop_Partial_Task_Offloading_and_Resource_Allocation_in_AirGround_Integrated_Mobile_Edge_Computing_Network_A_DRL-Based_Method.pdf-ab2d992d-223a-4d34-b728-342bef620ffa/6228b26c-2629-40a4-824a-8ab71fafd31c_origin.pdf
- Two-Hop_Partial_Task_Offloading_and_Resource_Allocation_in_AirGround_Integrated_Mobile_Edge_Computing_Network_A_DRL-Based_Method.pdf-ab2d992d-223a-4d34-b728-342bef620ffa/full.md
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- MADDPG-Based_Joint_Service_Placement_and_Task_Offloading_in_MEC_Empowered_AirGround_Integrated_Networks.pdf-499bca38-d55d-47d6-800d-2457617637c7/391ad469-1677-4a96-9d65-31fc8fd0b258_origin.pdf
- MADDPG-Based_Joint_Service_Placement_and_Task_Offloading_in_MEC_Empowered_AirGround_Integrated_Networks.pdf-499bca38-d55d-47d6-800d-2457617637c7/full.md
## [2026-05-29] external delete | Joint_Resource_Management_for_Energy-Efficient_UAV-Assisted_SWIPT-MEC_A_Deep_Reinforcement_Learning_Approach.pdf-47bc5eef-5351-4750-9de7-0a501e06f744/27aace2d-fd3d-44e6-ac23-4a2386878e16_origin.pdf

Deleted 1 source file and 0 wiki pages.
## [2026-05-29] external delete | Joint_Resource_Management_for_Energy-Efficient_UAV-Assisted_SWIPT-MEC_A_Deep_Reinforcement_Learning_Approach.pdf-47bc5eef-5351-4750-9de7-0a501e06f744/full.md

Deleted 1 source file and 0 wiki pages.
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- FedLEO_An_Offloading-Assisted_Decentralized_Federated_Learning_Framework_for_Low_Earth_Orbit_Satellite_Networks.pdf-7cbb1edb-d3d9-4aaa-bc82-b01707e227e1/c2b3ff92-9440-484e-82ac-7c26f755903f_origin.pdf
- FedLEO_An_Offloading-Assisted_Decentralized_Federated_Learning_Framework_for_Low_Earth_Orbit_Satellite_Networks.pdf-7cbb1edb-d3d9-4aaa-bc82-b01707e227e1/full.md
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- Distributed_Foundation_Models_for_Multi-Modal_Learning_in_6G_Wireless_Networks.pdf-cd5196f5-a52f-4b9d-82ad-c1b50996a79e/17b265eb-d64b-4b6d-9e41-bc3f6577f29b_origin.pdf
- Distributed_Foundation_Models_for_Multi-Modal_Learning_in_6G_Wireless_Networks.pdf-cd5196f5-a52f-4b9d-82ad-c1b50996a79e/full.md
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- Energy_Efficient_Task_Offloading_and_Resource_Allocation_in_Air-Ground_Integrated_MEC_Systems_A_Distributed_Online_Approach.pdf-a0ebded2-6b19-49ef-82a8-a60fe98bd9a3/1bf62391-2d01-4b85-a2dd-44c3f6bfa9e9_origin.pdf
- Energy_Efficient_Task_Offloading_and_Resource_Allocation_in_Air-Ground_Integrated_MEC_Systems_A_Distributed_Online_Approach.pdf-a0ebded2-6b19-49ef-82a8-a60fe98bd9a3/full.md
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- An_Adaptive_Constraint_Violation_Evaluation_Framework_for_Constrained_Multiobjective_Evolutionary_Optimization.pdf-09d5418e-dc62-4524-bc97-f89ba95dfc7e/1058f15e-3289-44ba-a46f-79175aa42220_origin.pdf
- An_Adaptive_Constraint_Violation_Evaluation_Framework_for_Constrained_Multiobjective_Evolutionary_Optimization.pdf-09d5418e-dc62-4524-bc97-f89ba95dfc7e/full.md
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- BARGAIN-MATCH_A_Game_Theoretical_Approach_for_Resource_Allocation_and_Task_Offloading_in_Vehicular_Edge_Computing_Networks.pdf-35b8645f-ec67-4bc8-a322-f2d67eb162f1/04bff10e-4497-45a2-a8ac-d649dc9ccda9_origin.pdf
- BARGAIN-MATCH_A_Game_Theoretical_Approach_for_Resource_Allocation_and_Task_Offloading_in_Vehicular_Edge_Computing_Networks.pdf-35b8645f-ec67-4bc8-a322-f2d67eb162f1/full.md
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- Fairness-Based_3-D_Multi-UAV_Trajectory_Optimization_in_Multi-UAV-Assisted_MEC_System.pdf-bf127b65-b284-404b-8ac3-337dd3a7759a/c0f2255d-e21b-42aa-8b98-d86bd3126819_origin.pdf
- Fairness-Based_3-D_Multi-UAV_Trajectory_Optimization_in_Multi-UAV-Assisted_MEC_System.pdf-bf127b65-b284-404b-8ac3-337dd3a7759a/full.md
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- Hybrid_OMA_NOMA_Mode_Selection_and_Resource_Allocation_in_Space-Air-Ground_Integrated_Networks.pdf-679ce336-ee6a-48b7-8df7-01515bfabee4/44d6771e-2771-4368-ad1b-636d2251d8a8_origin.pdf
- Hybrid_OMA_NOMA_Mode_Selection_and_Resource_Allocation_in_Space-Air-Ground_Integrated_Networks.pdf-679ce336-ee6a-48b7-8df7-01515bfabee4/full.md
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- Joint_Task_Offloading_and_Resource_Allocation_in_Aerial-Terrestrial_UAV_Networks_With_Edge_and_Fog_Computing_for_Post-Disaster_Rescue.pdf-74335d9f-9e06-4894-8e8a-6509dab133ea/df69a884-40cb-4350-90d6-a800db943b8d_origin.pdf
- Joint_Task_Offloading_and_Resource_Allocation_in_Aerial-Terrestrial_UAV_Networks_With_Edge_and_Fog_Computing_for_Post-Disaster_Rescue.pdf-74335d9f-9e06-4894-8e8a-6509dab133ea/full.md
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- Learning-Based_NOMA-Enabled_Queue-Aware_Task_Offloading_and_AAV_3D_Trajectory_Planning_for_SAGIN.pdf-05cffc33-d988-4317-b3b9-40599b4925c3/f675e19d-5e65-4eca-b496-6ddf8afa66dc_origin.pdf
- Learning-Based_NOMA-Enabled_Queue-Aware_Task_Offloading_and_AAV_3D_Trajectory_Planning_for_SAGIN.pdf-05cffc33-d988-4317-b3b9-40599b4925c3/full.md
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- MOALF-UAV-MEC_Adaptive_Multiobjective_Optimization_for_UAV-Assisted_Mobile_Edge_Computing_in_Dynamic_IoT_Environments.pdf-c51ce6bd-3435-4f83-8376-d3afa6c27e23/5563cba4-a83a-4c1c-bf33-64bf581d6168_origin.pdf
- MOALF-UAV-MEC_Adaptive_Multiobjective_Optimization_for_UAV-Assisted_Mobile_Edge_Computing_in_Dynamic_IoT_Environments.pdf-c51ce6bd-3435-4f83-8376-d3afa6c27e23/full.md
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- Mobile_Edge_Deployment_and_Resource_Management_for_Maritime_Wireless_Networks.pdf-0e509116-0716-49db-9a8c-8435b2013eda/3de33e2c-c9c8-4276-8fd4-b9b6e4892eec_origin.pdf
- Mobile_Edge_Deployment_and_Resource_Management_for_Maritime_Wireless_Networks.pdf-0e509116-0716-49db-9a8c-8435b2013eda/full.md
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- Multi-UAV_Cooperative_Task_Offloading_and_Resource_Allocation_in_5G_Advanced_and_Beyond.pdf-7d6296bb-d664-4cbc-b5bc-15464d88f8b6/3e1c946c-3aca-4e6e-90a9-dad57bf77441_origin.pdf
- Multi-UAV_Cooperative_Task_Offloading_and_Resource_Allocation_in_5G_Advanced_and_Beyond.pdf-7d6296bb-d664-4cbc-b5bc-15464d88f8b6/full.md
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- Over-the-Air_Edge_Inference_for_Low-Altitude_Airspace_Generative_AI-Aided_Multi-Task_Batching_and_Beamforming_Design.pdf-71716721-2d3b-4111-95d2-a6af53e729df/6d668a50-906d-42d0-9e25-2095ab35fd4a_origin.pdf
- Over-the-Air_Edge_Inference_for_Low-Altitude_Airspace_Generative_AI-Aided_Multi-Task_Batching_and_Beamforming_Design.pdf-71716721-2d3b-4111-95d2-a6af53e729df/full.md
## [2026-05-29] external batch delete | 2 source files

Deleted 2 source files and 0 wiki pages.

Sources:
- Joint_Task_Offloading_and_Resource_Allocation_in_UAV-Enabled_Mobile_Edge_Computing.pdf/fd834c11-797d-4d59-af05-b36b8e770e1f_origin.pdf
- Joint_Task_Offloading_and_Resource_Allocation_in_UAV-Enabled_Mobile_Edge_Computing.pdf/full.md
