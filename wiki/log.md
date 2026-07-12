# Research Log

## [2026-07-13] Curated distributed coverage, rechargeable crowdsensing, Dubins collection, heterogeneous grouping, and multimodal backhaul

Added five source pages, four concept pages, and one author entity:

- [[liu-2020-distributed-uav-coverage-navigation]] - Liu et al. 2020, *IEEE TMC*, DOI `10.1109/TMC.2019.2908171`. A global critic and local deterministic actors coordinate energy-efficient multi-UAV navigation for long-term PoI coverage and Jain-style fairness.
- [[liu-2021-edivert-mobile-crowdsensing]] - Liu et al. 2021, *IEEE TMC*, DOI `10.1109/TMC.2019.2938509`. e-Divert combines CNN/LSTM state encoding, N-step returns, prioritized replay, and distributed Ape-X actors for energy-aware crowdsensing with charging stations.
- [[fu-2026-dubins-uav-data-collection]] - Fu et al. 2026, *IEEE T-ITS*, DOI `10.1109/TITS.2025.3645094`. A carrier T-UAV releases and recovers collector C-UAVs whose obstacle-aware data tours and synchronized recovery paths obey Dubins constraints.
- [[li-2026-jscfg-uav-grouping]] - Li et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2026.3708388`. Joint switches reorganize overlapping heterogeneous-UAV coalitions for ordered functional subtasks while preserving type requirements.
- [[wang-2026-multimodal-uav-coverage-backhaul]] - Wang et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2025.3606778`. Distributed potential-based control switches UAVs among exploration, minimum-spanning-tree bridge, and static service roles for coverage and air-to-air backhaul.

New concept pages: [[ape-x-actor-learner-replay]], [[releasing-collecting-recycling-uav-framework]], [[joint-switch-coalition-formation-game]], and [[multi-modal-uav-coverage-backhaul-control]]. Reciprocal links were added to the established trajectory-control, CTDE, MA-POMDP, DDPG, fairness, backhaul, mobile-crowdsensing, charging, prioritized-replay, data-collection, heterogeneous-fleet, ant-colony, coalition-game, potential-game, Nash-equilibrium, autonomous-swarm, and air-to-ground-channel pages. Matching biographies across three parses established the same BIT identity for [[chi-harold-liu]], whose roster links the 2020 coverage-navigation, 2021 e-Divert, and 2026 air-ground vehicular-crowdsensing sources.

Metadata notes: the local parses expose titles and bylines but omit or incompletely expose final publication records. Exact-title Crossref records supplied or confirmed the five final journal records: Liu 2020 and Liu 2021 in TMC, Fu 2026 in T-ITS, and Li 2026 plus Wang 2026 in TMC. The older year embedded in an online-first DOI or reference was not substituted for the final issue year. Technical claims, algorithms, assumptions, and numerical findings remain grounded in the local Markdown parses.

Evidence caveats: all five studies are simulation based. The coverage-navigation source has binary disk coverage plus inconsistent full-observation/POMDP and global-training/local-signaling descriptions. e-Divert uses synthetic city layouts, requires retraining for new cities, and compares its large network against a smaller GA representation. The Dubins planner is centralized and offline, assumes a known map and homogeneous collectors, and omits hover, damage, and recovery-operation time. The grouping source fixes routes and omits communication and energy overhead; its central preference equation is OCR-damaged. The multimodal controller has conflicting population, convergence-time, spacing, and local-versus-network-wide threshold descriptions, and its displayed centroid update omits a term described in prose.

Two independent read-only reviewers checked the source/concept groups, entity evidence, reciprocal links, index, and overview against the parses. They raised seven concerns. Six corrections were applied: carrier rather than subordinate recovery-path elongation; an unresolved local/global coverage-threshold scope; potentially overlapping rather than partition-only initial coalitions; the stale overview denominator; the exact two-source scope of the Chi Harold Liu relation; and Ape-X risks restricted to the study's documented over-replay/overfitting and rapid-buffer-replacement effects. The remaining concern was publication metadata absent from the parses; it was resolved by rechecking the five exact-title Crossref records, as allowed by the curator rule for parse-silent metadata, so no metadata rollback was made.

Validation results before commit: `python tools/wiki/tests/test_curation_status.py` passed all 6 tests, and `python tools/wiki/process_refs.py` reported 0 affected files. `python tools/wiki/corpus_counts.py --json counts-batch20-final-2026-07-13.json` reported 449 sources, 420 concepts, 74 entities, 15 findings, 15 synthesis pages, 6 comparisons, 6 methodology pages, 5 queries, 3 thesis pages, 2 reference pages, and 612 raw-source folders. `python tools/wiki/curation_status.py --dupes --json status-batch20-final-2026-07-13.json` reported 450 path/title-matched curated folders and 162 genuinely new uncurated folders; its nonzero exit is expected while the backlog remains. `python tools/wiki/linkcheck.py --orphans`, `python tools/wiki/index_audit.py`, `python tools/wiki/frontmatter_audit.py`, `python tools/wiki/entity_roster_audit.py`, and `git diff --check` were clean; index coverage was 995/995 catalogue-able pages, frontmatter coverage was 993 pages, and the entity audit reported 0 claimed-but-absent over-claims with 41 advisory present-but-unlisted omissions. LLM Wiki health and graph endpoints returned HTTP `502`, so no live node/edge counts were available. No recurring curation failure or reusable tool gap appeared, so the stable toolkit was left unchanged.

## [2026-07-13] Curated digital tides, multiscale twins, directional modulation, distance-attention navigation, and distributed video JSCC

Added five source pages and five concept pages:

- [[dong-2026-digital-tides-provisioning]] - Dong et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2026.3688690`. A fluid-dynamic model of periodic logistics-UAV demand uses information flux to activate sleeping low-altitude radio and MEC infrastructure ahead of the workload wavefront.
- [[zhou-2026-multiscale-dt-uav-delivery]] - Zhou et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2025.3626747`. Terminal-edge multiscale digital twins combine graph-matching macro assignment with competitive/cooperative Q-learning for energy- and collision-aware parcel delivery.
- [[li-2026-directional-modulation-irs-uav]] - Li et al. 2026, *IEEE TGCN*, DOI `10.1109/TGCN.2025.3572113`. Symbol-level directional modulation jointly designs digital weights, UAV position, and discrete IRS phases to preserve legitimate constellations and disrupt one non-colluding eavesdropper.
- [[zhang-2026-distance-attention-uav-navigation]] - Zhang et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2026.3668827`. Distance-attention actors and historical-feature-flow critics extend CTDE deterministic actor-critic control to continuous 3-D cooperative UAV navigation.
- [[zhang-2026-distributed-jscc-uav-video]] - Zhang et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2026.3700200`. Receiver-heavy distributed video DeepJSCC uses lightweight UAV encoders and DQN-selected direct or amplify-forward relay links to trade reconstruction quality against transmission-energy lifetime.

New concept pages: [[information-flux-triggered-infrastructure-activation]], [[terminal-edge-multiscale-digital-twin]], [[directional-modulation]], [[distance-attention-uav-navigation]], and [[distributed-joint-source-channel-coding]]. Reciprocal links were added to the established MEC, stochastic-geometry, low-altitude-network, effective-energy-efficiency, digital-twin, graph-learning, CTDE, multi-agent Q-learning, delivery, IRS, physical-layer-security, channel-model, cross-entropy, near-field, MA-POMDP, MADDPG, autonomous-swarm, trajectory, semantic-communication, DQN, residual-energy, and mobile-relaying pages. The parse biography established the same SUTD identity for [[tony-q-s-quek]], whose roster now links ten sources; no other common-name author was merged or promoted.

Metadata notes: the local parses provide titles and bylines but vary in publication detail. The Digital Tides and directional-modulation parses expose their DOIs, while the other target records are silent or incomplete. Exact-title Crossref records supplied or confirmed the 2026 venues, DOI records, volume/issue where available, and page ranges. Technical claims, algorithms, assumptions, and numerical findings remain grounded in the local Markdown parses. The distributed-video paper's JSCC means joint source-channel coding and is distinct from the MAPPO-JSCC sensing/communication/computing controller elsewhere in the corpus.

Evidence caveats: all five studies are analytical or simulation based rather than field deployments. Digital Tides assumes radial Gaussian demand, PPP infrastructure, local homogeneity, and uniform startup latency, with several proofs absent from the parse supplement. The multiscale-twin study uses Gazebo/ROS and datasets and contains two-minute/two-second and 50/55-UAV inconsistencies. Directional modulation assumes one fixed non-colluding point eavesdropper and LoS-dominant imperfect CSI. Distance-attention navigation uses three training UAVs, fixed-ray LiDAR, reward-shaped rather than guaranteed safety, and no delayed/lost communication model. Distributed video JSCC shifts complexity and the highest decoding time to the receiver; its lifetime comparison excludes propulsion and encoder-computation energy.

Two independent read-only reviewers checked all five source/concept pairs against the full parses and found five precision issues, all corrected. The fixes separate smoothing for noisy flux estimates from spatial thresholds for heterogeneous startup delays and retain longitudinal flow for corridors; restrict the digital-twin event trigger to topology-state sharing; remove a feedback dependency from the no-feedback distributed JSCC design; replace speculative navigation failure modes with the paper's physical-validation, communication, and heterogeneous-swarm limits; and restrict directional-modulation caveats to the evaluated CSI, phase-resolution, direction, and eavesdropper assumptions.

Validation results before commit: `python tools/wiki/tests/test_curation_status.py` passed all 6 tests, and `python tools/wiki/process_refs.py` reported 0 affected files. `python tools/wiki/corpus_counts.py --json counts-batch19-final-2026-07-13.json` reported 444 sources, 416 concepts, 73 entities, 15 findings, 15 synthesis pages, 6 comparisons, 6 methodology pages, 5 queries, 3 thesis pages, 2 reference pages, and 612 raw-source folders. `python tools/wiki/curation_status.py --dupes --json status-batch19-final-2026-07-13.json` reported 445 path/title-matched curated folders and 167 genuinely new uncurated folders; its nonzero exit is expected while the backlog remains. `python tools/wiki/linkcheck.py --orphans`, `python tools/wiki/index_audit.py`, `python tools/wiki/frontmatter_audit.py`, `python tools/wiki/entity_roster_audit.py`, and `git diff --check` were clean; index coverage was 985/985 catalogue-able pages, frontmatter coverage was 983 pages, and the entity audit reported 0 claimed-but-absent over-claims with 41 advisory present-but-unlisted omissions. LLM Wiki health and graph endpoints returned HTTP `200`; the graph contained 983 nodes and 9276 edges. No recurring curation failure or reusable tool gap appeared, so the stable toolkit was left unchanged.

## [2026-07-12] Curated symmetry-augmented UAV-ISAC, density-aware air traffic, omnidirectional monitoring, digital-twin deployment, and AirComp clusters

Added five source pages and five concept pages:

- [[qin-2023-symmetry-augmented-uav-isac]] - Qin et al. 2023, *IEEE TWC*, DOI `10.1109/TWC.2023.3260304`. Multi-UAV ISAC association, trajectory, and sensing/communication power control with SAC, permutation-equivariant replay augmentation, and a CTDE MASAC alternative.
- [[vitale-2026-density-aware-4d-trajectory]] - Vitale et al. 2026, *IEEE T-ITS*, DOI `10.1109/TITS.2026.3694259`. Centralized cube/time reservations and distributed robust MPC for density-aware 4-D urban UAV traffic under arrival-time QoS and probabilistic separation constraints.
- [[zhang-2026-omnidirectional-monitoring-deployment]] - Zhang et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2025.3642129`. Joint UAV and fixed-camera strategy selection for continuous omnidirectional monitoring, with submodular approximation guarantees, simulation, and a ten-UAV physical test.
- [[zhao-2026-dt-ddqn-bisd-deployment]] - Zhao et al. 2026, *IEEE TWC*, DOI `10.1109/TWC.2025.3596864`. Digital-twin-driven multi-UAV IoT deployment with balanced mission division, separate transfer/collection DDQNs, online obstacle synchronization, safety halts, and policy refresh.
- [[zhang-2026-dt-aircomp-cluster-formation]] - Zhang et al. 2026, *IEEE TWC*, DOI `10.1109/TWC.2025.3646641`. Digital-twin-empowered UAV-swarm cluster formation for AirComp through joint association, receiver scaling, device power, and trajectory optimization.

New concept pages: [[permutation-equivariant-replay-augmentation]], [[reservation-based-density-aware-4d-uav-planning]], [[continuous-omnidirectional-monitoring]], [[digital-twin-assisted-online-drl-policy-refresh]], and [[aircomp-aware-uav-device-cluster-formation]]. Reciprocal links were added to the established ISAC, trajectory-control, SAC/MASAC, CTDE, fairness, digital-twin, AirComp, Dinkelbach, data-collection, urban-air-mobility, chance-constraint, safety, visual-coverage, DDQN, AoI, and blockage-aware-channel pages. No entity page was created. The identity-confirmed USTB biography extended [[haijun-zhang]] from two to three sources, and the matching NUAA biography extended [[yuben-qu]] from two to three.

The initial allowlist contained a raw folder whose title differs from [[zhai-2026-collaborative-inference-uav-mec]] only by the OCR omission in `Offloading` -> `Ofloading`; no duplicate source page was created. `curation_status.py` now has a conservative repeated-character-omission fallback that accepts only a unique title-key match involving a doubled character. A regression test covers the case, the toolkit README documents it, and five existing source pages now point to their actual underscore-named raw folders instead of stale space-named paths.

Metadata notes: the five local parses expose titles and bylines but not complete final publication records. Exact-title Crossref checks supplied or confirmed DOI, year, venue, volume, issue where available, and pages. The density-traffic parse misspells “Traffic” and “Different”; the exact-title record supplies the corrected title. Technical claims, algorithms, assumptions, and numerical findings remain grounded in the local Markdown parses.

Evidence caveats: the UAV-ISAC, density-aware traffic, digital-twin DDQN, and AirComp studies are simulation-only. The air-traffic safety guarantee is conditional on feasibility without positive slack, and its selected cube capacity is scenario-specific. The monitoring study has a physical deployment but uses planar binary visibility and does not report repeated-trial variance. The digital-twin deployment formulation omits propulsion, inter-UAV separation, sensing errors, and update latency; ideal fully informed PSO is faster in its exact mission-time table. The AirComp model assumes LoS-dominant coherent transmission with perfect synchronization and Doppler compensation.

Two read-only reviewers checked all five source/concept pairs against the full parses and identified twelve precision issues; all were corrected. The fixes separate SAC entropy from the environment reward, qualify ICPP optimality by prior reservations, distinguish planned flight time from route length, preserve the two capacity stress-test setups, separate strategic reservation from local collision control, define the monitoring union per target-direction pair, reserve UAV return-flight energy, remove an unsupported camera manufacturer label, avoid treating no-fly obstacles as visual occluders, distinguish model-update latency from mission-transfer time, acknowledge unspecified moving-obstacle dynamics, and narrow the AirComp transferability caveat.

Validation results before commit: `python tools/wiki/tests/test_curation_status.py` passed all 6 tests, and `python tools/wiki/process_refs.py` reported 0 affected files. `python tools/wiki/corpus_counts.py --json counts-batch18-final-2026-07-12.json` reported 439 sources, 411 concepts, 73 entities, 15 findings, 15 synthesis pages, 6 comparisons, 6 methodology pages, 5 queries, 3 thesis pages, 2 reference pages, and 612 raw-source folders. `python tools/wiki/curation_status.py --dupes --json status-batch18-final-2026-07-12.json` reported 440 path/title-matched curated folders and 172 genuinely new uncurated folders; its nonzero exit is expected while the backlog remains. `python tools/wiki/linkcheck.py --orphans`, `python tools/wiki/index_audit.py`, `python tools/wiki/frontmatter_audit.py`, `python tools/wiki/entity_roster_audit.py`, and `git diff --check` were clean; index coverage was 975/975 catalogue-able pages, frontmatter coverage was 973 pages, and the entity audit reported 0 claimed-but-absent over-claims with 41 advisory present-but-unlisted omissions. The LLM Wiki health and graph endpoints returned HTTP `502`, so no live graph node/edge counts were available.

## [2026-07-12] Curated wireless-powered fairness, energy-constrained collection, active-RIS control, AoI, and predictive beamforming

Added five source pages and five concept pages:

- [[wang-2026-wutf-fair-communication]] - Wang et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2026.3664292`. WUTF uses CNN-GRU actors, a centralized critic, and sequential PPO-style multi-agent updates for wireless-powered UAV trajectories under throughput, Jain fairness, energy, collision, and depletion terms.
- [[li-2023-energy-constrained-uav-data-collection]] - Li et al. 2023, *IEEE TMC*, DOI `10.1109/TMC.2021.3084972`. Full and partial IoT collection are modeled as energy-constrained depot-returning tours, with an ILP, no-overlap orienteering approximations, and overlap-aware marginal-gain heuristics.
- [[morshed-2026-active-ris-uav-noma-mappo]] - Morshed et al. 2026, *IEEE TGCN*, DOI `10.1109/TGCN.2026.3696806`. BS, UAV, and active-RIS MAPPO actors jointly control NOMA power, platform motion, and element gain/phase under a shared rate, energy, fairness, outage, and airspace reward.
- [[wang-2026-glint-aoi-wireless-powered-edge]] - Wang et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2026.3688661`. GLINT decomposes wireless-powered multi-UAV AoI control into position/association and WPT-time/transmission stages with local critics and monotonic value mixing.
- [[xu-2026-hecta-predictive-beamforming]] - Xu et al. 2026, *IEEE TWC*, DOI `10.1109/TWC.2026.3664980`. HECTA-Net predicts BS transmit and UAV receive beams directly from historical matched-filtered ISAC echoes through CNN, dilated causal TCN, and temporal attention.

New concept pages: [[wireless-powered-uav-fair-service-control]], [[energy-constrained-uav-data-collection-orienteering]], [[decentralized-active-ris-uav-noma-control]], [[dual-network-sequential-aoi-control]], and [[historical-echo-predictive-beamforming]]. Updated reciprocal links for WPT/RF harvesting, Jain fairness, MA-POMDP, CTDE, MAPPO/MADDPG, sequential policy generation, rotary-wing energy, trajectory control, UAV data collection, active/UAV-mounted RIS, NOMA, NTN, AoI, device association, ISAC, CSI uncertainty, mmWave sensing, cellular-connected UAVs, and control-assisted beam tracking. No author entity was created or merged because the current entity pages do not establish an unambiguous recurring-author identity for these bylines.

Metadata notes: all five parses expose title and byline, but only the GLINT parse names its TMC venue; they do not provide complete target-paper publication records. Exact DOI lookups against the live Crossref API revalidated the five titles, author lists, years, venues, and available volume/issue/page fields. The active-RIS parse misspells "Efficient"; the exact-title Crossref record supplies the corrected title. Technical claims, methods, assumptions, and numerical findings remain grounded in the local Markdown parses.

Evidence caveats: WUTF uses fixed users/altitude, idealized charging and channel models, and a separate hard-coded WCT-outage safeguard rather than learned tower availability; its `GA`/KM-GA result label inconsistency is preserved. The collection study is synthetic, gives guarantees only for the non-overlap branch, and prints a runtime multiplier inconsistent with its stated times. The active-RIS study assumes perfect CSI/SIC and simplified propulsion; DDPG, not MAPPO, has the highest raw spectral efficiency in its reported table. GLINT uses an approximate two-stage decomposition, perfect CSI, and an association appendix absent from the parse. HECTA-Net is trained and evaluated on synthetic single-BS/single-UAV trajectories without over-the-air validation and uses sensing echoes for a communication-beam objective rather than an independent sensing task.

Review and validation results before commit: the first broad reviewer exceeded its bounded window and was stopped without a report. Two focused reviewers that had already read the assigned parses in full completed independent page checks and identified seven items: six wording/evidence corrections were applied, while the external-metadata item was resolved by the live Crossref recheck. The fixes distinguish WUTF from direct MAPPO, keep WCT availability outside the base policy, preserve the `GA`/KM-GA label mismatch, remove an unsupported active-RIS dynamic-noise claim, treat MADDPG as GLINT's design foundation rather than an evaluated baseline, and identify GLINT's evaluated mobility action as discrete. `python tools/wiki/tests/test_curation_status.py` passed all 5 tests, and `python tools/wiki/process_refs.py` reported 0 affected files. `python tools/wiki/corpus_counts.py --json counts-batch17-final-2026-07-12.json` reported 434 sources, 406 concepts, 73 entities, 15 findings, 15 synthesis pages, 6 comparisons, 6 methodology pages, 5 queries, 3 thesis pages, 2 reference pages, and 612 raw-source folders. `python tools/wiki/curation_status.py --dupes --json status-batch17-final-2026-07-12.json` reported 430 path/title-matched curated folders and 182 genuinely new uncurated folders; its nonzero exit is expected while uncurated folders remain. `python tools/wiki/linkcheck.py --orphans`, `python tools/wiki/index_audit.py`, `python tools/wiki/frontmatter_audit.py`, `python tools/wiki/entity_roster_audit.py`, and `git diff --check` were clean; index coverage was 965/965 catalogue-able pages, frontmatter coverage was 963 pages, and entity audit reported 0 claimed-but-absent over-claims with 41 advisory present-but-unlisted omissions. LLM Wiki health was OK; the current graph contained 963 nodes and 9111 edges.

## [2026-07-12] Curated UAV-ISAC correction, cooperative charging, persistent emergency service, content delivery, and DFF-SLAM

Added five source pages and four concept pages:

- [[meng-2026-uav-isac-corrections]] - Meng et al. 2026, *IEEE TWC*, DOI `10.1109/TWC.2025.3634306`. Corrects a duplicated association factor and an omitted auxiliary-variable/Taylor transformation in periodic UAV-ISAC throughput optimization; the original simulations already used the repaired convex formulation.
- [[wu-2026-parallel-cooperative-charging]] - Wu et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2026.3664259`. CSAU jointly forms shared-cost charging-station groups and schedules UAVs over unequal-power parallel RF facilities through uniform-machine approximation and greedy set cover.
- [[liu-2026-usp-nfrp-emergency-communication]] - Liu et al. 2026, *IEEE TGCN*, DOI `10.1109/TGCN.2025.3649278`. USP-NFRP combines periodic UAV replacement loops, dynamic tree backhaul repair, and max-min ant-system planning for persistent emergency communication.
- [[hua-2026-ddrl-content-delivery]] - Hua et al. 2026, *IEEE TWC*, DOI `10.1109/TWC.2026.3677068`. CNN-GRU clipped PPO controls multi-BS UAV movement/transmission behavior while PSO tunes cache replacement for lower content-acquisition delay.
- [[li-2026-dff-slam]] - Li et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2025.3600661`. YOLOv3 semantic filtering, multiscale optical flow, and epipolar geometry remove moving features before ORB-SLAM2 pose estimation, with TUM RGB-D accuracy tests and Jetson Xavier NX runtime evidence.

New concept pages: [[parallel-cooperative-uav-charging]], [[persistent-emergency-uav-swarm-service]], [[uav-content-caching]], and [[dynamic-feature-filtering-vslam]]. Updated reciprocal links for ISAC, association, SCA convexification, charging scheduling, WPT, assignment, trajectory privacy/control, post-disaster networking, autonomous swarms, mobile/substitution relaying, ACO, fixed-/rotary-wing energy, PPO, PSO, wireless backhaul, edge intelligence, RSS localization, and the [[tony-q-s-quek]] and [[qingqing-wu]] entity rosters.

Metadata notes: all five local parses expose title and byline; only the correction parse exposes its own DOI. Exact-title Crossref records supplied final 2026 year, venue, volume/issue/page, and DOI metadata where the parses are silent. The correction's Crossref DOI record supplies its 2026 single-page publication metadata. Its Qingqing Wu entity link was made only after the original article's parsed biography established the same NUS-to-University-of-Macau career identity; unrelated advisory roster omissions remain untouched. Technical claims, algorithms, assumptions, and numerical findings remain grounded in the local Markdown parses.

Evidence caveats: the correction adds no experiment and depends on definitions in the original article. Charging percentages are narrative-supported, while damaged tables were not transcribed. The emergency-network results are deterministic distance-link simulations with instantaneous recharge and no throughput/interference model. DDRL's power action conflicts with a fixed-power simulation statement, and its abstract's `8%`/`5%` gains lack a machine-readable result table. DFF-SLAM's physical UAV test establishes embedded runtime and qualitative filtering, while ground-truth trajectory accuracy remains TUM RGB-D dataset-based; internally inconsistent extracted table rows were excluded.

Validation results before commit: the independent read-only review identified seven issues, each checked against the parses; six wording/evidence fixes were applied directly, and the author-link recommendation was implemented only after identity evidence was found in the original article's raw biography. `python tools/wiki/tests/test_curation_status.py` passed all 5 tests, and `python tools/wiki/process_refs.py` reported 0 affected files. `python tools/wiki/corpus_counts.py --json counts-batch16-final-2026-07-12.json` reported 429 sources, 401 concepts, 73 entities, 15 findings, 15 synthesis pages, 6 comparisons, 6 methodology pages, 5 queries, 3 thesis pages, 2 reference pages, and 612 raw-source folders. `python tools/wiki/curation_status.py --dupes --json status-batch16-final-2026-07-12.json` reported 425 path/title-matched curated folders and 187 genuinely new uncurated folders; its nonzero exit is expected while uncurated folders remain. `python tools/wiki/linkcheck.py --orphans`, `python tools/wiki/index_audit.py`, `python tools/wiki/frontmatter_audit.py`, and `git diff --check` were clean; index coverage was 955/955 catalogue-able pages and frontmatter coverage was 953 pages. `python tools/wiki/entity_roster_audit.py` reported 0 claimed-but-absent over-claims and 41 advisory present-but-unlisted omissions. LLM Wiki health was OK; the current graph contained 953 nodes and 9014 edges.

## [2026-07-12] Curated HAP-UAV efficiency, medical delivery, pursuit-evasion, relay substitution, and asynchronous collection

Added five source pages and five concept pages:

- [[fan-2026-hap-uav-iort-oee]] - Fan et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2026.3664906`. HAP-UAV IoRT collection with whole-chain overall energy efficiency, moving HAP/UAV trajectories, HAP selection, UAV power, bandwidth allocation, meteorological fading, and Dinkelbach/BCD/SCA optimization.
- [[chen-not-in-parse-uav-human-medical-delivery]] - Chen et al. Cooperative emergency medical pickup-delivery scheduling with UAVs and human couriers, using type-specific attention decoders, feasibility masks, and a vehicle coordinator for near-real-time heterogeneous routing. *(Parsed metadata lacks DOI/venue/year.)*
- [[yang-2025-hcdrl-pursuit-evasion]] - Yang et al. 2025, *IEEE Globecom Workshops*, DOI `10.1109/GCWkshps68340.2025.11591106`. Hierarchical cooperative DRL for counter-UAV pursuit, with learned selection among five encirclement subtasks and CTDE continuous maneuver policies.
- [[zhang-2022-uav-relay-substitution]] - Zhang et al. 2022, *IEEE TGCN*, DOI `10.1109/TGCN.2021.3108147`. HUS/SEUS relay substitution extends service beyond one UAV's flight duration and jointly controls trajectories and source/relay powers under overlapping-link interference.
- [[le-2026-asynchronous-uav-data-collection]] - Le et al. 2026, *IEEE TWC*, DOI `10.1109/TWC.2026.3656853`. Dec-POSMDP remote collection with Asynchronous-QMIX, event-driven action completion, range-limited completion-map exchange, and local imperfect-CSI bandwidth optimization.

New concept pages: [[overall-energy-efficiency]], [[cooperative-uav-human-courier-delivery]], [[cooperative-uav-pursuit-evasion]], [[uav-substitution-relaying]], and [[asynchronous-qmix]]. Updated reciprocal links for HAPS, UAV data collection, fractional/alternating optimization, delivery, heterogeneous-agent learning, hierarchical RL, autonomous swarms, low-altitude networks, CTDE, mobile relaying, information causality, QMIX, semi-Markov control, and MA-POMDPs. The exact NTU identity match extended the [[dusit-niyato]] roster to 44 linked sources. The Qingqing Wu byline in the 2022 relay paper is affiliated with the University of Macau, while the existing entity page intentionally tracks an SJTU-affiliated roster and flags earlier affiliation changes; the new match remains an advisory omission pending human identity confirmation.

Metadata notes: the Fan, Yang, and Le parses expose title/authors but no top-level publication record, so exact-title Crossref records supplied their 2026 TMC, 2025 Globecom Workshops, and 2026 TWC metadata. The relay parse explicitly states DOI and August 2021 online publication; the DOI record supplies its final 2022 TGCN issue, volume, and pages. No authoritative exact-title record was available for the medical-delivery paper, so year, venue, DOI, and URL remain blank rather than being inferred from its IEEE styling, references, case-study date, or author biographies. Technical claims and numerical findings remain grounded in the local parses.

Evidence caveats: the HAP-UAV source reports qualitative figure rankings rather than exact OEE gains and contains an inconsistent speed description. The medical study uses synthetic requests plus Shenzhen geography/route data, not live dispatch, and excludes battery, weather, no-fly-zone, and online-demand dynamics. The pursuit source is planar simulation with ideal communication despite its wireless-network framing; its reported capture-rate advantage is a percentage-point difference, not a relative percentage. The substitution-relay source assumes deterministic LoS channels and exogenous flight duration, with figure-only throughput ordinates. The asynchronous-collection source uses fixed-altitude grid motion, orthogonal UAV bands, abstract immediate in-range map exchange, and propulsion-only energy efficiency.

Validation results before commit: `python tools/wiki/tests/test_curation_status.py` passed all 5 tests. `python tools/wiki/corpus_counts.py --json counts-batch15-final-2026-07-12.json` reported 424 sources, 397 concepts, 73 entities, 15 findings, 15 synthesis pages, 6 comparisons, 6 methodology pages, 5 queries, 3 thesis pages, 2 reference pages, and 612 raw-source folders. `python tools/wiki/curation_status.py --dupes --json status-batch15-final-2026-07-12.json` reported 420 path/title-matched curated folders and 192 genuinely new uncurated folders; the nonzero exit is expected while uncurated folders remain. `python tools/wiki/linkcheck.py --orphans`, `python tools/wiki/process_refs.py`, `python tools/wiki/index_audit.py`, `python tools/wiki/frontmatter_audit.py`, and `git diff --check` were clean; index coverage was 946/946 catalogue-able pages and frontmatter coverage was 944 pages. `python tools/wiki/entity_roster_audit.py` reported 0 claimed-but-absent over-claims and 41 advisory present-but-unlisted omissions. LLM Wiki graph health was OK; `/api/v1/projects/current/graph?limit=5000` reported 944 nodes and 8937 edges.

## [2026-07-12] Curated collaborative UAV communication, hybrid FL, beam tracking, delivery, and anti-UAV ISAC

Added five source pages and five concept pages:

- [[javaid-2023-collaborative-uav-communication-control]] - Javaid et al. 2023, *IEEE T-ITS*, DOI `10.1109/TITS.2023.3248841`. Survey of collaborative multi-UAV communication/control requirements, tasking, urban applications, use cases, and open problems.
- [[chen-2026-sdhfl-completion-time]] - Chen et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2025.3634664`. Semi-decentralized hybrid FL with D2D cluster consensus, asynchronous UAV aggregation, Lyapunov cluster selection, and joint mobility/resource optimization for completion time.
- [[zhang-2026-control-assisted-beam-tracking]] - Zhang et al. 2026, *IEEE TWC*, DOI `10.1109/TWC.2026.3668082`. Control-assisted BS-UAV mmWave beam prediction using PID flight state, Bayesian DNN uncertainty, and kinematic position tracking, evaluated in Gazebo and with real F450 flight data.
- [[gao-2026-air-ground-instant-delivery]] - Gao et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2025.3634430`. Cooperative UAV-taxi instant delivery with delivery-gap station placement, demand-driven repositioning, courier-preference transfer, generalized assignment, and Shanghai trace evaluation.
- [[zhang-2025-cooperative-anti-uav-isac]] - Zhang et al. 2025, *IEEE TWC*, DOI `10.1109/TWC.2024.3519351`. Multi-cell anti-UAV ISAC transceiver beamforming with centralized AO/SCA/Dinkelbach and primal-decomposition distributed solvers.

New concept pages: [[collaborative-uav-communication]], [[semi-decentralized-hybrid-federated-learning]], [[control-assisted-uav-beam-tracking]], [[cooperative-uav-taxi-delivery]], and [[cooperative-isac-transceiver-beamforming]]. Updated reciprocal links for autonomous swarms, cellular-connected UAVs, D2D communication, federated learning, air-to-ground channels, UAV delivery, weighted K-means deployment, networked ISAC, integrated sensing/communication, and the AO/Dinkelbach solver family. No author entity was created or merged because no exact identity was already established for these authors.

Metadata notes: the Javaid survey and both beamforming papers expose DOI or dated publication evidence in their parses; Crossref supplied or confirmed the full venue, volume, pages, and year. The SDHFL and cooperative-delivery parses contain no top-level publication metadata, so exact-title Crossref records supplied their 2026 TMC metadata. The shorter 2024 ICDE cooperative-delivery paper found in the references was kept distinct from the journal article. All technical claims and numerical results remain grounded in the local parses.

Evidence caveats: the collaborative-UAV paper is a narrative survey with secondary numerical examples, not an original experiment. SDHFL contains conflicting noise-density values and opposite textual descriptions of one device-count trend. The beam-tracking paper validates embedded prediction with real F450 flight-state data but not an over-the-air mmWave radio. The delivery study combines real Shanghai traces with simulated mode-specific labels and counterfactual delivery assignments. The anti-UAV ISAC study is Monte Carlo simulation and reaches a KKT point; its lower distributed signaling is per subgradient iteration rather than a total-run guarantee.

Validation results before commit: `python tools/wiki/corpus_counts.py --json counts-batch14-final-2026-07-12.json` reported 419 sources, 392 concepts, 73 entities, 15 findings, 15 synthesis pages, 6 comparisons, 6 methodology pages, 5 queries, 3 thesis pages, 2 reference pages, and 612 raw-source folders. `python tools/wiki/curation_status.py --dupes --json status-batch14-final-2026-07-12.json` reported 415 path/title-matched curated folders, 197 genuinely new uncurated folders, 86 title-matched curated folders, and 93 stale referenced-name/no-matching-folder advisories; the nonzero exit is expected while uncurated folders remain. `python tools/wiki/linkcheck.py --orphans`, `python tools/wiki/process_refs.py`, `python tools/wiki/index_audit.py`, `python tools/wiki/frontmatter_audit.py`, and `git diff --check` were clean; index coverage was 936/936 catalogue-able pages and frontmatter coverage was 934 pages. `python tools/wiki/entity_roster_audit.py` reported 0 claimed-but-absent over-claims and 40 advisory present-but-unlisted omissions. LLM Wiki graph health was OK; `/api/v1/projects/current/graph?limit=5000` reported 934 nodes and 8840 edges.

## [2026-07-12] Curated mobility security, UAV-to-X, dynamic IRS, and adaptive traffic prediction

Added five source pages and five concept pages:

- [[li-not-in-parse-movable-antenna-pls]] - Li et al. Physical-layer-security comparison of movable-antenna micro-mobility and UAV macro-mobility, using projected-gradient/AdaGrad antenna-position control and AO/SCA UAV trajectory optimization. *(Parsed metadata lacks DOI/venue/year.)*
- [[zhang-not-in-parse-cellular-uav-to-x]] - Zhang et al. Cellular UAV-to-X communication with cooperative UAV-to-network and UAV-to-UAV sense-and-send operation; ISASOA combines linear programming, branch-and-bound channel decisions, and convex speed control. *(Parsed metadata lacks DOI/venue/year.)*
- [[ning-2025-channel-aware-irs-uav]] - Ning et al. 2025. Multi-IRS/multi-UAV NOMA communication with geometric blockage judgment, partitioned dynamic IRS-user association, MAPPO trajectory/association control, and SCA power allocation. *(DOI/venue not in parse.)*
- [[he-not-in-parse-cipc-covert-uav]] - He et al. Multi-user secret and covert UAV communication using Bob's confidential NOMA signal as cover and truncated channel-inversion power control, with analytical rotary-wing and AO/SCA fixed-wing designs. *(Parsed metadata lacks DOI/venue/year.)*
- [[ma-not-in-parse-reinforced-traffic-prediction]] - Ma et al. Cell-level traffic prediction with FFT feature characterization and value-based reinforced meta-learning that adapts the DNN structure, evaluated on real traffic traces and in a numerical UAV-offloading case study. *(Parsed metadata lacks DOI/venue/year.)*

New concept pages: [[micro-macro-mobility-security]], [[uav-to-x-communication]], [[dynamic-irs-user-association]], [[channel-inversion-power-control]], and [[cell-level-mobile-traffic-prediction]]. Updated reciprocal links for movable antennas, physical-layer security, cellular-connected UAVs, D2D/overlay-underlay access, UAV relaying, IRSs, MAPPO, blockage-aware channels, covert communication, secrecy outage, CSI uncertainty, traffic-aware offloading, and meta-DRL. Exact-match recurring-author rosters were extended for [[zhiyong-feng]], [[jingjing-wang]], and [[chunxiao-jiang]]; no new entity pages were created for unresolved common-name identities. The existing cargo-UAV source's raw pointer was aligned with its actual underscore-named folder.

The curation planner was corrected before selecting this allowlist. `curation_status.py` now discovers `full.md`, title-named parses, and a sole top-level Markdown parse; a normalized raw-H1/source-title fallback recognizes curated pages whose historical raw paths are stale. Duplicate scans use the same parse discovery and title-prefilter near comparisons, while `wikilib.read_text` closes files deterministically. Five regression tests cover parse discovery, title reconciliation, exact duplicates, unrelated-title pruning, and similar-title near duplicates. This changed the pre-curation backlog from the old path-only count of 294 to 207 genuinely uncurated folders without creating duplicate source pages; curating these five leaves 202.

Metadata notes: the Ning parse states publication on 9 December 2025 but does not expose a reliable venue or DOI; the other four parses expose title/authors but no reliable publication year, venue, or DOI. Those fields remain blank rather than being inferred from references or biographies. Technical claims and numerical findings remain grounded in the local parsed Markdown; figure-associated prose, corrupted equations, inconsistent learning-rate text, and simulation-only evidence are identified on the affected source pages.

Validation results before commit: `python tools/wiki/tests/test_curation_status.py` passed all 5 tests. `python tools/wiki/corpus_counts.py --json counts-batch13-final-2026-07-12.json` reported 414 sources, 387 concepts, 73 entities, 15 findings, 15 synthesis pages, 6 comparisons, 6 methodology pages, 5 queries, 3 thesis pages, 2 reference pages, and 612 raw-source folders. `python tools/wiki/curation_status.py --dupes --json status-batch13-final-2026-07-12.json` reported 410 path/title-matched curated folders, 202 genuinely new uncurated folders, 86 title-matched curated folders, and 93 stale referenced-name/no-matching-folder advisories; the nonzero exit is expected while uncurated folders remain. `python tools/wiki/linkcheck.py --orphans`, `python tools/wiki/process_refs.py`, `python tools/wiki/index_audit.py`, `python tools/wiki/frontmatter_audit.py`, and `git diff --check` were clean; index coverage was 926/926 catalogue-able pages and frontmatter coverage was 924 pages. `python tools/wiki/entity_roster_audit.py` reported 0 claimed-but-absent over-claims and 40 advisory present-but-unlisted omissions. LLM Wiki graph health was OK; `/api/v1/projects/current/graph?limit=5000` reported 924 nodes and 8747 edges.

## [2026-07-11] Curated spectrum mapping, multi-DT ABS deployment, 3-D cellular, UAV delivery safety, and blockage-aided interference

Added five source pages and four concept pages:

- [[wang-2026-bayesian-uav-spectrum-mapping]] - Wang et al. 2026, DOI `10.1109/TWC.2026.3694148`. Bayesian 3-D spectrum mapping with information-driven 3DIG-RRT* UAV sampling and SBDL-GP recovery over sparse measured RSS data in unknown 3-D environments. *(Venue not in parse.)*
- [[belgiovine-not-in-parse-multidt-abs-deployment]] - Belgiovine et al. Multi-digital-twin airborne base-station deployment optimization, using Sionna differentiable ray tracing for placement/orientation/power search and AODT for mobile-UE scenario validation. *(Parsed metadata lacks DOI/venue/year.)*
- [[mozaffari-not-in-parse-3d-drone-cellular-network]] - Mozaffari et al. 3-D wireless cellular network foundation with LAP drone base stations, drone user equipment, HAP/FSO backhaul, truncated-octahedron frequency reuse, KDE demand modeling, and optimal-transport association. *(Parsed metadata lacks DOI/venue/year.)*
- [[jiang-2026-bi-level-uav-delivery-safety]] - Jiang et al. 2026, DOI `10.1109/TITS.2026.3660878`. Bi-level urban low-altitude UAV delivery framework combining TC-NSGA-III order/fleet assignment with RG-FMT* trajectory planning under target-level-of-safety constraints. *(Venue not in parse.)*
- [[heo-not-in-parse-blockage-aided-multiuav-interference]] - Heo et al. Multi-UAV interference coordination that deliberately uses building blockage to keep desired links LoS while making interfering links NLoS, solved through SCA/PCCP/BCD trajectory and power control. *(Parsed metadata lacks DOI/venue/year.)*

New concept pages: [[information-driven-uav-spectrum-mapping]], [[multi-digital-twin-network-optimization]], [[target-level-of-safety]], and [[building-blockage-aided-interference-coordination]]. Updated backlinks for temporal spectrum cartography, radio-map/channel estimation, digital twins, drone-cell 3-D placement, cellular-connected UAVs, 3-D frequency reuse, optimal transport, UAV delivery, heterogeneous fleets, NSGA variants, compliance-aware trajectories, urban air mobility, blockage-aware channels, spectrum sensing, wireless backhaul, UAV trajectory control, air-to-ground channels, BSUM, low-altitude intelligent networks, and the Mozaffari/Saad/Qihui Wu entity rosters, then refreshed [[index]] and [[overview]].

Metadata notes: the Wang and Jiang parses expose title/authors plus DOI evidence, but no reliable venue banner, so DOI/year are recorded and venue remains blank. The Belgiovine, Mozaffari, and Heo parses expose title/authors but not reliable publication year, venue, or DOI; those fields remain blank rather than inferred. Technical claims remain grounded in the local parsed Markdown, with OCR/table/equation caveats recorded on affected source pages.

Validation results before commit: `python tools/wiki/corpus_counts.py --json counts-current-2026-07-11-batch12-final.json` reported 409 sources, 382 concepts, 73 entities, 15 findings, 15 synthesis pages, 6 comparisons, 6 methodology pages, 5 queries, 3 thesis pages, 2 reference pages, and 612 raw-source folders. `python tools/wiki/curation_status.py --dupes --json status-current-2026-07-11-batch12-final.json` reported 612 raw folders, 318 curated raw references, 294 genuinely new uncurated folders remaining, and 94 referenced-name/no-matching-raw-folder advisories; the nonzero exit is expected while uncurated folders remain. `python tools/wiki/linkcheck.py --orphans --json linkcheck-current-2026-07-11-batch12-final.json` reported no dangling links; orphan reporting remains informational for raw-source mirrors and parse artifacts. `python tools/wiki/process_refs.py --json process-refs-current-2026-07-11-batch12-final.json`, `python tools/wiki/index_audit.py --json index-audit-current-2026-07-11-batch12-final.json`, `python tools/wiki/frontmatter_audit.py --json frontmatter-current-2026-07-11-batch12-final.json`, and `git diff --check` were clean. `python tools/wiki/entity_roster_audit.py --json entity-roster-current-2026-07-11-batch12-final.json` reported 0 claimed-but-absent over-claims and 40 advisory present-but-unlisted omissions. LLM Wiki graph health was OK; `/api/v1/projects/current/graph?limit=5000` reported 914 nodes and 8656 edges.

## [2026-07-11] Curated AoI/FANET, air-ground VCS, ISAC feature fusion, secure content, and UAV localization

Added five source pages and four concept pages:

- [[wu-not-in-parse-aoi-sampling-buffering-routing]] - Wu et al. AoI-aware all-aerial UAV swarm monitoring with AASBR and COMH-MAPPO, jointly learning sampling, buffer scheduling, and FANET routing under leader-follower partial observability.
- [[zhou-2026-a2g-madrl-air-ground-vcs]] - Zhou et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2026.3708370`. Air-ground vehicular crowdsensing with UAV-UGV pairs, sensing capability-aware AoI, latency-weighted data collection ratio, HVGCN interaction features, and dynamically ordered masked policy generation.
- [[yan-not-in-parse-multibs-isac-uav-trajectory]] - Yan et al. Asynchronous UAV trajectory monitoring in cellular ISAC with single-BS LDFT/TO-CFO preprocessing, compressed-sensing multi-BS feature fusion, and SUKF trajectory tracking. *(Parsed metadata lacks DOI/venue/year.)*
- [[bayessa-not-in-parse-uav-isac-secure-content-hdrl]] - Bayessa et al. UAV-enabled ISAC secure content delivery with CRLB/EKF eavesdropper localization and action-masked hierarchical DDQN over caching, association, deployment, and beamforming. *(Parsed metadata lacks DOI/venue/year.)*
- [[ebrahimi-not-in-parse-autonomous-uav-localization-rl]] - Ebrahimi et al. Autonomous UAV trajectory learning for RSSI-based ground-object localization with initial scan, Q-learning waypoint selection, ATG path-loss/shadowing, and energy/time/path/waypoint constraints. *(Parsed metadata lacks DOI/venue/year.)*

New concept pages: [[sequential-multi-agent-policy-generation]], [[multi-bs-feature-fusion-isac]], [[action-masked-hierarchical-drl]], and [[rss-based-uav-localization]]. Updated backlinks for AoI, UAV-assisted mobile crowd sensing, MAPPO, MA-POMDP, CTDE, FANET routing, GNN, NOMA, ISAC, networked ISAC, CRLB, DDQN, hierarchical RL, service/secure caching, PLS, UAV trajectory control, ATG channel modeling, and multi-source fusion, then refreshed [[index]] and [[overview]].

Metadata notes: the Zhou VCS parse contains an accepted-for-publication IEEE TMC DOI banner, so DOI/year/venue are recorded from the local parse. The Wu, Yan, Bayessa, and Ebrahimi parses expose title/authors but not reliable publication year, venue, or DOI; those fields remain blank rather than inferred. Technical claims remain grounded in the local parsed Markdown; pages record OCR/table/equation caveats where the parse is visibly corrupted.

Validation results before commit: `python tools/wiki/corpus_counts.py --json counts-current-2026-07-11-batch11-final.json` reported 404 sources, 378 concepts, 73 entities, 15 findings, 15 synthesis pages, 6 comparisons, 6 methodology pages, 5 queries, 3 thesis pages, 2 reference pages, and 612 raw-source folders. `python tools/wiki/curation_status.py --dupes --json status-current-2026-07-11-batch11-final.json` reported 612 raw folders, 313 curated raw references, 299 genuinely new uncurated folders remaining, and 94 referenced-name/no-matching-raw-folder advisories; the nonzero exit is expected while uncurated folders remain. `python tools/wiki/linkcheck.py --orphans --json linkcheck-current-2026-07-11-batch11-final.json` reported no dangling links; orphan reporting remains informational for raw-source mirrors and parse artifacts. `python tools/wiki/process_refs.py --json process-refs-current-2026-07-11-batch11-final.json`, `python tools/wiki/index_audit.py --json index-audit-current-2026-07-11-batch11-final.json`, `python tools/wiki/frontmatter_audit.py --json frontmatter-current-2026-07-11-batch11-final.json`, and `git diff --check` were clean. `python tools/wiki/entity_roster_audit.py --json entity-roster-current-2026-07-11-batch11-final.json` reported 0 claimed-but-absent over-claims and 40 advisory present-but-unlisted omissions. LLM Wiki graph health was OK; `/api/v1/projects/current/graph?limit=5000` reported 905 nodes and 8572 edges.

## [2026-07-11] Curated maritime auction, 3D spectrum, spherical T-RIS, and AoI incentive/energy sources

Added five source pages and six concept pages:

- [[li-2026-online-maritime-double-auction]] - Li et al. 2026, *IEEE T-ITS*, DOI `10.1109/TITS.2026.3657174`. Online double auction for maritime network resource allocation, with OMDAM pricing ship connectivity demand against ISP antenna/UAV capacity under deadline, coverage, social-welfare, and weak-budget-balance constraints.
- [[prabhath-not-in-parse-3d-space-spectrum-utilization]] - Prabhath and Jayaweera. 3D UAV cellular spectrum-utilization analysis with truncated-octahedron frequency reuse, first-tier co-channel interference, blocking probability, and channel-shadowing sensitivity. *(Parsed metadata lacks DOI/venue/year.)*
- [[liu-2026-spherical-t-ris-bs]] - Liu et al. 2026, *IEEE TWC*, DOI `10.1109/TWC.2026.3656594`. Angle-insensitive spherical transmissive-RIS base station design with omnidirectional feed, spatial-average-gain analysis, and BCD/SCA co-optimization of UAV trajectories, phase shifts, powers, and sensor scheduling.
- [[shi-2025-aoi-energy-replenishment-multiuav]] - Shi et al. 2025, *IEEE TGCN*, DOI `10.1109/TGCN.2025.3542611`. AoI-aware multi-UAV IoT data collection and wireless energy replenishment via Dec-POMDP, VDN, and QMIX over flight, sensor/charging-station association, data collection, and UAV recharging decisions.
- [[guo-2026-aoi-uav-mcs-contract]] - Guo et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2025.3604073`. AoI-aware UAV-assisted mobile crowdsensing incentives with hierarchical platform-UAV and platform-user contracts under incomplete information.

New concept pages: [[online-maritime-double-auction]], [[spectrum-utilization-efficiency]], [[three-dimensional-frequency-reuse]], [[spherical-transmissive-ris]], [[qmix]], and [[aoi-aware-contract-incentives]]. Updated backlinks for maritime MEC, double/reverse auctions, contract theory, AoI, UAV data collection, WPT, CTDE/VDN, RIS, cellular-connected UAVs, NTN/channel modeling, and DRL-backbone synthesis, then refreshed [[index]] and [[overview]].

Metadata notes: Li, Liu, Shi, and Guo bibliographic metadata was verified against title-matched DOI/Crossref records where the local Markdown parse lacked complete top-level venue/year/DOI metadata. The Prabhath/Jayaweera 3D spectrum source remains deliberately marked as parse-metadata incomplete because no reliable DOI/venue/year record was exposed during curation. Technical claims remain grounded in the local parsed Markdown, with OCR/math corruption caveats recorded on affected source pages.

Validation results before commit: `python tools/wiki/corpus_counts.py --json counts-current-2026-07-11-batch10-final.json` reported 399 sources, 374 concepts, 73 entities, 15 findings, 15 synthesis pages, 6 comparisons, 6 methodology pages, 5 queries, 3 thesis pages, 2 reference pages, and 612 raw-source folders. `python tools/wiki/curation_status.py --dupes --json status-current-2026-07-11-batch10-final.json` reported 612 raw folders, 308 curated raw references, 304 genuinely new uncurated folders remaining, and 94 referenced-name/no-matching-raw-folder advisories; the nonzero exit is expected while uncurated folders remain. `python tools/wiki/linkcheck.py --orphans --json linkcheck-current-2026-07-11-batch10-final.json` reported no dangling links; orphan reporting remains informational for raw-source mirrors and parse artifacts. `python tools/wiki/process_refs.py --json process-refs-current-2026-07-11-batch10-final.json`, `python tools/wiki/index_audit.py --json index-audit-current-2026-07-11-batch10-final.json`, `python tools/wiki/frontmatter_audit.py --json frontmatter-current-2026-07-11-batch10-final.json`, and `git diff --check` were clean. `python tools/wiki/entity_roster_audit.py --json entity-roster-current-2026-07-11-batch10-final.json` reported 0 claimed-but-absent over-claims and 40 advisory present-but-unlisted omissions. LLM Wiki graph health was OK; `/api/v1/projects/current/graph?limit=5000` reported 896 nodes and 8465 edges.

## [2026-07-11] Curated near-field channel, RIS coverage, UAV-mmWave HetNet, ensemble MARL, and UAV FL incentives

Added five source pages and five concept pages:

- [[bai-adaptive-near-field-xl-mimo-multi-uav]] - Bai et al. Adaptive near-field channel modeling for 6G XL-MIMO UPA-to-multi-UAV cooperative communications, with selective near-field area pruning to retain spherical-wave accuracy while reducing channel-computation cost.
- [[lin-2025-energy-effective-ris-multiuav-coverage]] - Lin et al. 2025, *IEEE TGCN*, DOI `10.1109/TGCN.2024.3424980`. RIS-assisted multi-UAV coverage with K-DBSCAN initial deployment, throughput-variance fairness screening, and TDQN/DDQN/dueling-DQN trajectory learning.
- [[chakareski-2019-uav-mmwave-hetnet-ee]] - Chakareski 2019, *IEEE TGCN*, DOI `10.1109/TGCN.2019.2892141`. Energy-efficient UAV-assisted mmWave 5G heterogeneous cellular networking with UAV-BS placement/offloading and bandwidth/energy tradeoff analysis.
- [[zhang-2026-ensemble-marl-uav-target-search]] - Zhang et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2026.3656917`. Ensemble MARL for heterogeneous UAV target search in 3-D, using E-QMIX to route graph/CNN/DQN subnetwork outputs into centralized value mixing.
- [[zhao-2026-uav-fl-inspection-incentives]] - Zhao et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2026.3651590`. Contract-theoretic UAV-client assignment for federated intelligent inspection under communication-sensing-computing integration.

New concept pages: [[selective-near-field-area]], [[k-dbscan-uav-deployment]], [[triple-deep-q-network]], [[ensemble-qmix]], and [[contract-theoretic-fl-incentives]]. Updated backlinks for near-field / XL-MIMO / THz, drone-cell deployment, RIS, DQN variants, fairness metrics, FL/contract theory/ISCC, and CTDE/value-decomposition target-search concepts, then refreshed [[drl-backbones-across-uav-mec-sources]], [[index]], and [[overview]].

Metadata notes: Chakareski, Lin, Zhang, and Zhao metadata were verified against title-matched DOI/Crossref records. The Bai near-field channel parse and external title lookup did not expose reliable DOI/venue/year metadata, so those fields remain blank rather than guessed. Technical claims remain grounded in the local parsed Markdown; Bai and Lin source pages flag OCR/math corruption where it affects formula fidelity.

Validation results before commit: `python tools/wiki/corpus_counts.py --json counts-current-2026-07-11-batch9-final.json` reported 394 sources, 368 concepts, 73 entities, 15 findings, 15 synthesis pages, 6 comparisons, 6 methodology pages, 5 queries, 3 thesis pages, 2 reference pages, and 612 raw-source folders. `python tools/wiki/curation_status.py --dupes --json status-current-2026-07-11-batch9-final.json` reported 612 raw folders, 303 curated raw references, 309 genuinely new uncurated folders remaining, and 94 referenced-name/no-matching-raw-folder advisories; the nonzero exit is expected while uncurated folders remain. `python tools/wiki/linkcheck.py --orphans --json linkcheck-current-2026-07-11-batch9-final.json` reported no dangling links; orphan reporting remains informational for raw-source mirrors and parse artifacts. `python tools/wiki/process_refs.py --json process-refs-current-2026-07-11-batch9-final.json`, `python tools/wiki/index_audit.py --json index-audit-current-2026-07-11-batch9-final.json`, `python tools/wiki/frontmatter_audit.py --json frontmatter-current-2026-07-11-batch9-final.json`, and `git diff --check` were clean. `python tools/wiki/entity_roster_audit.py --json entity-roster-current-2026-07-11-batch9-final.json` reported 0 claimed-but-absent over-claims and 40 advisory present-but-unlisted omissions. LLM Wiki graph health was OK; `/api/v1/projects/current/graph?limit=5000` reported 885 nodes and 8378 edges.

## [2026-07-11] Curated covert jamming, AirComp FL, AirFogSim pointer, and active-RIS backhaul

Added four source pages and four concept pages, and repaired one existing source-to-raw pointer:

- [[zhang-2026-air-ground-covert-jamming]] - Zhang et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2026.3673234`. Air-ground cooperative covert transmission with a decode-forward UAV, UAV-mounted RIS, terrestrial jamming redirection, SDR/Dinkelbach static optimization, and DDQN trajectory/user scheduling.
- [[chen-2026-air-ground-covert]] - Chen et al. 2026, *IEEE TWC*, DOI `10.1109/TWC.2026.3687670`. Air-to-ground covert communication under Willie-location uncertainty and PPP-modeled environmental interference, with gamma interference approximation and covertness/reliability/covert-throughput analysis.
- [[huang-2026-aircomp-uav-swarms-afl]] - Huang et al. 2026, *IEEE TWC*, DOI `10.1109/TWC.2026.3693868`. AirComp-assisted asynchronous federated learning for UAV swarms with branch-and-bound/AO aggregation scheduling and layer-wise cosine-similarity staleness filtering.
- [[jeon-2026-ampli-flection-aerial-backhaul]] - Jeon and Chae 2026, *IEEE TWC*, DOI `10.1109/TWC.2026.3672500`. Active-RIS-aided aerial backhaul for full-3D UAV-BS coverage, jointly optimizing platform placement, array partitioning, phase control, and equal amplification gain.
- [[wei-2026-airfogsim-uav-vfc]] - corrected the raw artifact path to the underscore-named `AirFogSim_A_Light-Weight_and_Modular_Simulator_for_UAV-Integrated_Vehicular_Fog_Computing` folder so curation status recognizes the parsed source.

New concept pages: [[ris-assisted-directional-jamming]], [[ambient-interference-aided-covertness]], [[aircomp-assisted-asynchronous-fl]], and [[aerial-active-ris-backhaul]]. Updated backlinks for [[covert-communication]], [[cooperative-jamming]], [[physical-layer-security]], [[stochastic-geometry-network-analysis]], [[air-to-ground-channel-model]], [[uav-mounted-ris]], [[finite-blocklength-urllc]], [[ddqn]], [[fractional-programming-dinkelbach]], [[effective-energy-efficiency]], [[over-the-air-computation]], [[federated-learning]], [[autonomous-uav-swarms]], [[active-ris]], [[wireless-backhaul]], and [[drone-cell-3d-placement]], then refreshed `wiki/index.md` and `wiki/overview.md`.

Metadata notes: the local Markdown parses for the four newly curated papers were silent or incomplete on final DOI/venue headers, so DOI/venue/year metadata was verified against exact-title DOI records. Technical claims and numeric findings remain grounded in the local parsed Markdown; the Zhang source page avoids detailed formula claims because the parse corrupts several equations, and the Chen source page records the manuscript's apparent case-comparison inconsistency rather than smoothing it over. The AirFogSim source already existed; only its raw artifact path and update date changed.

Validation results before commit: `python tools/wiki/corpus_counts.py --json counts-current-2026-07-11-batch8-final.json` reported 389 sources, 363 concepts, 73 entities, 15 findings, 15 synthesis pages, 6 comparisons, 6 methodology pages, 5 queries, 3 thesis pages, 2 reference pages, and 612 raw-source folders. `python tools/wiki/curation_status.py --dupes --json status-current-2026-07-11-batch8-final.json` reported 612 raw folders, 298 curated raw references, 314 genuinely new uncurated folders remaining, and 94 referenced-name/no-matching-raw-folder advisories; the nonzero exit is expected while uncurated folders remain. `python tools/wiki/linkcheck.py --orphans --json linkcheck-current-2026-07-11-batch8-final.json` reported no dangling links; orphan reporting remains informational for raw-source mirrors and parse artifacts. `python tools/wiki/process_refs.py --json process-refs-current-2026-07-11-batch8-final.json`, `python tools/wiki/index_audit.py --json index-audit-current-2026-07-11-batch8-final.json`, `python tools/wiki/frontmatter_audit.py --json frontmatter-current-2026-07-11-batch8-final.json`, and `git diff --check` were clean. `python tools/wiki/entity_roster_audit.py --json entity-roster-current-2026-07-11-batch8-final.json` reported 0 claimed-but-absent over-claims and 40 advisory present-but-unlisted omissions. LLM Wiki graph health was OK; `/api/v1/projects/current/graph?limit=5000` reported 875 nodes and 8278 edges.

## [2026-07-10] Curated aerial RIS, UAV fault detection, covert AoI, and UAV-ISAC freshness

Added four source pages and four concept pages, repaired one existing source-to-raw pointer, and updated two existing author rosters:

- [[li-2026-aerial-ris-trajectory-phase]] - Li et al. 2026, *IEEE TWC*, DOI `10.1109/TWC.2025.3621306`. Aerial RIS-enhanced communication with tilt/Euler-angle-aware UAV-mounted RIS control, SAC-PER attitude/phase learning, and ZF/water-filling BS beamforming.
- [[li-2026-aeroguard-uav-fault-detection]] - Li et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2026.3653674`. AeroGuard real-time UAV fault detection with hybrid LSTM/ARX residual fusion, Z-score/SPRT testing, real UAV logs/outdoor flights, and Raspberry Pi latency measurements.
- [[hosseini-2026-aoi-covert-uav]] - Hosseini et al. 2026, *IEEE TWC*, DOI `10.1109/TWC.2026.3681697`. UAV-assisted covert communication with AoI minimization, PD-NOMA public cover traffic, aerial Eve detection, and AO/SCA/SDR trajectory-beamforming design.
- [[bai-2026-aoi-uav-isac]] - Bai et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2026.3709576`. AoI-centric UAV-enabled ISAC with SAC trajectory/beam activation, Kalman target prediction, and RZF communication beam synthesis.
- [[shi-2026-aoi-active-ris-noma-agmec]] - corrected the raw artifact path to the underscore-named raw folder so curation status recognizes the parsed source.
- [[dusit-niyato]] and [[zhu-han]] - updated exact-match rosters for the aerial-RIS and UAV-ISAC sources.

New concept pages: [[tilt-aware-aerial-ris-control]], [[hybrid-uav-flight-data-fault-detection]], [[freshness-aware-covert-uav-communication]], and [[aoi-centric-uav-isac-beam-control]]. Updated backlinks for [[uav-mounted-ris]], [[soft-actor-critic]], [[prioritized-experience-replay]], [[noma]], [[age-of-information]], [[covert-communication]], [[integrated-sensing-and-communication]], [[uav-trajectory-control]], [[alternating-optimization-sdr-sca]], and [[edge-intelligence]], then refreshed `wiki/index.md` and `wiki/overview.md`.

Metadata notes: the aerial-RIS, covert-AoI, and UAV-ISAC parses were silent or incomplete on final DOI/venue headers, so bibliographic metadata was verified against title-matched DOI records. The AeroGuard parse contains DOI/publication-date evidence and Crossref was used for venue/pages. Technical claims and numeric findings remain grounded in the local parsed Markdown. The Shi AoI/active-RIS/NOMA source already existed; only its raw artifact path and update date changed.

Validation results before commit: `python tools/wiki/corpus_counts.py --json counts-current-2026-07-10-batch7-final.json` reported 385 sources, 359 concepts, 73 entities, 15 findings, 15 synthesis pages, 6 comparisons, 6 methodology pages, 5 queries, 3 thesis pages, 2 reference pages, and 612 raw-source folders. `python tools/wiki/curation_status.py --dupes --json status-current-2026-07-10-batch7-final.json` reported 612 raw folders, 293 curated raw references, 319 genuinely new uncurated folders remaining, and 95 referenced-name/no-matching-raw-folder advisories; the nonzero exit is expected while uncurated folders remain. `python tools/wiki/linkcheck.py --orphans --json linkcheck-current-2026-07-10-batch7-final.json` reported no dangling links; orphan reporting remains informational for raw-source mirrors and parse artifacts. `python tools/wiki/process_refs.py --json process-refs-current-2026-07-10-batch7-final.json`, `python tools/wiki/index_audit.py --json index-audit-current-2026-07-10-batch7-final.json`, `python tools/wiki/frontmatter_audit.py --json frontmatter-current-2026-07-10-batch7-final.json`, and `git diff --check` were clean. `python tools/wiki/entity_roster_audit.py --json entity-roster-current-2026-07-10-batch7-final.json` reported 0 claimed-but-absent over-claims and 40 advisory present-but-unlisted omissions. LLM Wiki graph health was OK; `/api/v1/projects/current/graph?limit=5000` reported 867 nodes and 8198 edges.

## [2026-07-10] Curated active UAV search, FANET routing, clustered LEO access, and surface-air control

Added four source pages and four concept pages, and repaired one existing source-to-raw pointer:

- [[zheng-2026-active-search-low-altitude-uav]] - Zheng and Chen 2026, *IEEE TMC*, DOI `10.1109/TMC.2026.3689691`. Online low-altitude UAV sensing/communication search under unknown user locations and unknown blockage, with equipotential-surface search and local LoS channel estimation.
- [[deng-2026-eret-fanet-routing]] - Deng et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2026.3694704`. eRET adaptive FANET routing that evolves route expiration time so UAV swarms shift between host-centric route reuse and content-centric discovery.
- [[yang-2026-clustered-leo-adaptive-selection]] - Yang et al. 2026, *IEEE TWC*, DOI `10.1109/TWC.2026.3660891`. Clustered LEO direct/cooperative communication with UAV assistance, spherical stochastic geometry, shadowed-Rician fading, and adaptive signal selection.
- [[zhang-2026-fuzzy-observer-harbor-approach]] - Zhang et al. 2026, *IEEE T-ITS*, DOI `10.1109/TITS.2026.3705994`. Surface-air harbor-approach guidance/control with an adaptive event-triggered fuzzy state observer for heterogeneous USV-UAV dynamics.
- [[li-2023-adaptive-digital-twin-uav-iscc]] - corrected the raw artifact path to the underscore-named raw folder so curation status recognizes the parsed source.

New concept pages: [[equipotential-surface-uav-search]], [[evolvable-route-expiration-time]], [[clustered-leo-adaptive-selection]], and [[event-triggered-fuzzy-state-observer]]. Updated backlinks for [[radio-map-assisted-channel-estimation]], [[drone-cell-3d-placement]], [[stateless-geographic-fanet-routing]], [[directional-fanet-link-maintenance]], [[uav-usv-cooperative-mec]], [[leo-satellite-edge-computing]], [[stochastic-geometry-network-analysis]], and [[wireless-backhaul]], then refreshed `wiki/index.md` and `wiki/overview.md`.

Metadata notes: the active-search and eRET parses are silent on final DOI/venue headers, so bibliographic metadata was verified against title-matched IEEE Computer Society records. The clustered-LEO and harbor-approach parses contain DOI evidence in the local Markdown. Technical claims and numeric findings remain grounded in the local parsed Markdown; OCR/math corruption and simulation-only caveats are recorded on the source pages.

Validation results before commit: `python tools/wiki/corpus_counts.py --json counts-current-2026-07-10-batch6-final.json` reported 381 sources, 355 concepts, 73 entities, 15 findings, 15 synthesis pages, 6 comparisons, 6 methodology pages, 5 queries, 3 thesis pages, 2 reference pages, and 612 raw-source folders. `python tools/wiki/curation_status.py --dupes --json status-current-2026-07-10-batch6-final.json` reported 612 raw folders, 288 curated raw references, 324 genuinely new uncurated folders remaining, and 96 referenced-name/no-matching-raw-folder advisories; the nonzero exit is expected while uncurated folders remain. `python tools/wiki/linkcheck.py --orphans` reported no dangling links; orphan reporting remains informational for raw-source mirrors and parse artifacts. `python tools/wiki/process_refs.py`, `python tools/wiki/index_audit.py`, `python tools/wiki/frontmatter_audit.py`, and `git diff --check` were clean for this batch. `python tools/wiki/entity_roster_audit.py --json entity-roster-current-2026-07-10-batch6-final.json` reported 0 claimed-but-absent over-claims and 40 advisory present-but-unlisted omissions. LLM Wiki graph health was OK; `/api/v1/projects/current/graph?limit=5000` reported 859 nodes and 8119 edges.

## [2026-07-10] Curated UAV anti-jamming, swarm autonomy, CAV coordination, crowd sensing, and visual coverage

Added five source pages and five concept pages:

- [[chen-2026-maddpg-uav-swarm-antijamming]] - Chen et al. 2026, *IEEE T-ITS*, DOI `10.1109/TITS.2025.3584216`. MADDPG-based multi-domain UAV-swarm anti-jamming for urban ITS traffic monitoring, with joint channel/power actions under fixed, swept, and random jamming.
- [[du-2025-autonomous-intelligent-uav-swarms]] - Du et al. 2025, *IEEE T-ITS*, DOI `10.1109/TITS.2025.3569500`. Survey of autonomous and intelligent UAV swarms across planning, coordination, task assignment, control, localization, perception, communication, and applications.
- [[zang-2026-uav-ev-priority-cav-speed]] - Zang et al. 2026, *IEEE T-ITS*, DOI `10.1109/TITS.2026.3651592`. UAV-assisted emergency-vehicle priority and CAV speed coordination through rolling speed-coordinated robust optimization control.
- [[gao-2023-uav-mcs-uma]] - Gao et al. 2023, *IEEE TMC*, DOI `10.1109/TMC.2022.3147871`. UMA UAV-assisted mobile crowd sensing with participant incentives, quality prediction, UAV coverage, sensor calibration, and MADDPG scheduling.
- [[gong-2026-uav-3d-visual-coverage]] - Gong et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2025.3646339`. Path-aware 3-D object visual coverage with viewpoint generation, informed RRT*-SA routing, B-spline SE(3) smoothing, and propulsion-energy optimization.

New concept pages: [[multi-domain-uav-anti-jamming]], [[autonomous-uav-swarms]], [[speed-coordinated-robust-optimization-control]], uav-assisted-mobile-crowd-sensing, and [[path-aware-3d-visual-coverage]]. Updated backlinks for [[uav-enabled-its]], [[anti-jamming-mec]], [[uav-data-collection]], [[particle-swarm-optimization]], [[maddpg]], [[centralized-training-decentralized-execution]], [[ma-pomdp]], [[uav-trajectory-control]], [[b-spline-trajectory]], and [[rotary-wing-propulsion-energy-model]], then refreshed `wiki/index.md` and `wiki/overview.md`.

Metadata notes: the local parses for the five new source pages are silent or incomplete on top-level venue/year/DOI metadata. Chen, Du, and Zang metadata came from local PDF metadata/first-page evidence; Gao and Gong metadata were verified through title-matched DOI records. Technical claims and numeric findings remain grounded in the local parsed Markdown, with OCR conflicts or malformed tables called out on the source pages.

Validation results before commit: `python tools/wiki/corpus_counts.py --json counts-current-2026-07-10-batch5-final.json` reported 377 sources, 351 concepts, 73 entities, 15 findings, 15 synthesis pages, 6 comparisons, 6 methodology pages, 5 queries, 3 thesis pages, 2 reference pages, and 612 raw-source folders. `python tools/wiki/curation_status.py --dupes --json status-current-2026-07-10-batch5-final.json` reported 612 raw folders, 283 curated raw references, 329 genuinely new uncurated folders remaining, and 97 referenced-name/no-matching-raw-folder advisories; the nonzero exit is expected while uncurated folders remain. `python tools/wiki/linkcheck.py --orphans` reported no dangling links; orphan reporting remains informational for raw-source mirrors and parse artifacts. `python tools/wiki/process_refs.py`, `python tools/wiki/index_audit.py`, `python tools/wiki/frontmatter_audit.py`, and `git diff --check` were clean for this batch. `python tools/wiki/entity_roster_audit.py --json entity-roster-current-2026-07-10-batch5-final.json` reported 0 claimed-but-absent over-claims and 40 advisory present-but-unlisted omissions. LLM Wiki graph health was OK; `/api/v1/projects/current/graph?limit=5000` reported 851 nodes and 8045 edges.

## [2026-07-10] Curated UAV tracking, vehicular ISAC, and directional FANET maintenance

Added four source pages and four concept pages, repaired one existing source-to-raw pointer, and updated two existing author rosters:

- [[li-2026-la4h-uav-active-tracking]] - Li, Zhou, and Wu 2026, *IEEE TMC*, DOI `10.1109/TMC.2026.3666656`. LA4H expert-assisted anomaly-aware UAV active target tracking with cross-modal anomaly cognition, assistance decisions, and teacher-student distillation for occlusion/distractor recovery.
- [[wang-2026-rmaddpg-dda-uav-isac-vehicular]] - Wang et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2025.3591259`. UAV-enabled vehicular ISAC with RMADDPG-DDA, RND novelty, parameter sharing, dynamic data augmentation, and multi-objective sensing/communication/energy rewards.
- [[hazarika-2026-dynamo-uav-vehicle-tracking]] - Hazarika and Rahmati 2026, *IEEE T-ITS*, DOI `10.1109/TITS.2025.3639545`. Predictive UAV fast-vehicle tracking with DynaMo, DTPM, CRLB/FIM optimization, and POMDP-MADDPG.
- [[song-2026-albpd-directional-fanet]] - Song et al. 2026, *IEEE TWC*, DOI `10.1109/TWC.2025.3627301`. ALBP-D directional FANET link maintenance via distance/angular breakage-probability prediction and beamwidth/range adjustment.
- [[xu-2026-prizty-uav-mec-auction]] - corrected the raw artifact path to the underscore-named raw folder so curation status recognizes the parsed source.

New concept pages: [[expert-assisted-anomaly-aware-tracking]], [[rmaddpg-dda-uav-isac-control]], [[dynamic-target-prioritization-metric]], and [[directional-fanet-link-maintenance]]. Updated backlinks for [[integrated-sensing-and-communication]], [[age-of-information]], [[stateless-geographic-fanet-routing]], [[cramer-rao-bound]], [[maddpg]], [[uav-enabled-its]], and [[expert-guided-warm-start-rl]]. Updated author rosters for [[qihui-wu]] and [[dusit-niyato]], then refreshed `wiki/index.md` and `wiki/overview.md`.

Metadata notes: the local parses for the four new source pages are silent on DOI/venue/year, so DOI/venue/year metadata was verified against title-matched DOI records; technical claims and numeric findings are grounded in the local parses. [[hazarika-2026-dynamo-uav-vehicle-tracking]] reports conflicting DynaMo RMSE values between Table I and narrative text, so the source page records both instead of merging them. [[xu-2026-prizty-uav-mec-auction]] already had a source page; only its artifact pointer and curation date changed.

Validation results before commit: `python tools/wiki/corpus_counts.py --json counts-current-2026-07-10-batch4-final.json` reported 372 sources, 346 concepts, 73 entities, 15 findings, 15 synthesis pages, 6 comparisons, 6 methodology pages, 5 queries, 3 thesis pages, 2 reference pages, and 612 raw-source folders. `python tools/wiki/curation_status.py --dupes --json status-current-2026-07-10-batch4-final.json` reported 612 raw folders, 278 curated raw references, 334 genuinely new uncurated folders remaining, and 97 referenced-name/no-matching-raw-folder advisories; the nonzero exit is expected while uncurated folders remain. `python tools/wiki/linkcheck.py --orphans` reported no dangling links; orphan reporting remains informational for raw-source mirrors and parse artifacts. `python tools/wiki/process_refs.py`, `python tools/wiki/index_audit.py`, `python tools/wiki/frontmatter_audit.py`, and `git diff --check` were clean for this batch. `python tools/wiki/entity_roster_audit.py --json entity-roster-current-2026-07-10-batch4-final.json` reported 0 claimed-but-absent over-claims and 40 advisory present-but-unlisted omissions. LLM Wiki graph health was OK; `/api/v1/projects/current/graph?limit=5000` reported 841 nodes and 7956 edges.

## [2026-07-10] Curated TN-NTN incentives and UAV channel-modeling foundations

Added four source pages and four concept pages, and repaired one existing source-to-raw pointer:

- [[huang-2025-fedx-ris-uav-trajectory]] - Huang et al. 2025, *IEEE TMC*, DOI `10.1109/TMC.2025.3544903`. RIS-assisted UAV trajectory planning with the FedX acceleration framework, multi-threaded SAC rollouts, and federated aggregation across environment agents.
- [[seid-2026-mafdrl-tn-ntn-incentive]] - Seid et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2025.3608291`. Hierarchical MAFDRL resource allocation and incentive mechanism for 6G TN-NTN using HFL, MEC-side task-offloading control, CTDE training, and double-auction participation incentives.
- [[bai-2026-multimodal-uav-vehicle-channel]] - Bai et al. 2026, *IEEE TWC*, DOI `10.1109/TWC.2025.3630319`. Multi-modal intelligent channel model for 6G multi-UAV-to-multi-vehicle links, joining geometric stochastic modeling, sensing/environment modalities, and data-driven channel prediction.
- [[hussain-2026-unet-uav-mmwave-pathloss]] - Hussain et al. 2026, *IEEE TWC*, DOI `10.1109/TWC.2026.3670373`. Multi-scale feature extraction and fusion U-Net for UAV-assisted mmWave pathloss prediction, using elevation maps, building occupancy maps, and UAV/receiver geometry.
- [[liu-2026-lyapunov-diffusion-uav-vehicular]] - corrected the raw artifact path to the underscore-named raw folder so curation status recognizes the parsed source.

New concept pages: [[fedx-training-acceleration]], [[hierarchical-federated-drl]], [[multi-modal-intelligent-channel-modeling]], and [[multi-scale-unet-pathloss-prediction]]. Updated backlinks for [[federated-reinforcement-learning]], double-auction, [[air-to-ground-channel-model]], and [[uav-trajectory-control]], then refreshed `wiki/index.md` and `wiki/overview.md`.

Metadata notes: [[liu-2026-lyapunov-diffusion-uav-vehicular]] already had a source page; only its artifact pointer and curation date changed. DOI/venue/year metadata for the parse-silent entries were verified against title-matched Crossref records. The multi-modal channel parse includes DOI `10.1109/TWC.2025.3630319`; Crossref's issued year is 2026. The MAFDRL parse asserts secure MPC, but the source page records that the parse does not provide protocol, threat-model, overhead, or privacy-experiment detail.

Validation results before commit: `python tools/wiki/corpus_counts.py --json counts-current-2026-07-10-batch3-after.json` reported 368 sources, 342 concepts, 73 entities, 15 findings, 15 synthesis pages, 6 comparisons, 6 methodology pages, 5 queries, 3 thesis pages, 2 reference pages, and 612 raw-source folders. `python tools/wiki/curation_status.py --dupes --json status-current-2026-07-10-batch3-after.json` reported 612 raw folders, 273 curated raw references, 339 genuinely new uncurated folders remaining, and 98 referenced-name/no-matching-raw-folder advisories; the nonzero exit is expected while uncurated folders remain. `python tools/wiki/linkcheck.py --orphans` reported no dangling links; orphan reporting remains informational for raw-source mirrors and parse artifacts. `python tools/wiki/process_refs.py`, `python tools/wiki/index_audit.py`, `python tools/wiki/frontmatter_audit.py`, and `git diff --check` were clean for this batch. `python tools/wiki/entity_roster_audit.py --json entity-roster-current-2026-07-10-batch3-after.json` reported 0 claimed-but-absent over-claims and 40 advisory present-but-unlisted omissions.

## [2026-07-10] Curated 5 UAV relay / ARIS V2X / FANET routing / ISAC control sources

Added five source pages and five concept pages:

- [[huang-2026-aim-uav-relay-aor]] - Huang et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2025.3630751`. Angle-of-radiation-aware UAV relay deployment with joint 3-D position and heading choices, AIM reachability search, and quantified relay/success-rate tradeoffs.
- [[cui-2026-aris-v2x-icac]] - Cui et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2026.3682488`. Active-RIS-aided multi-UAV V2X integrated communication and computation allocation with effective-energy-efficiency maximization, Dinkelbach reformulation, and BCD/ECCRA updates.
- [[he-2026-lscr-uav-relay-tracking]] - He et al. 2026, *IEEE T-ITS*, DOI `10.1109/TITS.2026.3677037`. LSCR collaborative UAV relay tracking using Delaunay-neighbor target graph representation, Twin-GRCN selection, and low-overhead relay handover.
- [[bujari-2018-stateless-fanet-routing]] - Bujari, Palazzi, and Ronzani 2018, *IEEE TMC*, DOI `10.1109/TMC.2018.2811490`. Stateless geographic FANET routing comparison across progress, randomized, face, hybrid, and flooding families under 3-D mobility.
- [[li-2026-control-based-uav-isac]] - Li et al. 2026, *IEEE TWC*, DOI `10.1109/TWC.2025.3604344`. Control-based UAV-ISAC design coupling SCA/SDR beamforming with control-parameterized 3-DoF and 6-DoF trajectory optimization.

New concept pages: [[angle-of-radiation-uav-relay]], [[effective-energy-efficiency]], [[target-graph-representation]], [[stateless-geographic-fanet-routing]], and [[control-parameterized-uav-trajectory]]. Updated backlinks for [[uav-mobile-relaying]], [[active-ris]], [[graph-neural-network]], [[integrated-sensing-and-communication]], [[uav-trajectory-control]], [[vehicular-mec]], [[fractional-programming-dinkelbach]], [[alternating-optimization-sdr-sca]], and [[integrated-sensing-computation-communication]]. Updated [[zhu-han]] with the control-based UAV-ISAC paper and refreshed `wiki/index.md` plus `wiki/overview.md` counts and cross-track summaries.

Metadata notes: [[huang-2026-aim-uav-relay-aor]] and [[li-2026-control-based-uav-isac]] had DOI evidence in the local parses. The local parses for [[cui-2026-aris-v2x-icac]], [[he-2026-lscr-uav-relay-tracking]], and [[bujari-2018-stateless-fanet-routing]] were silent or incomplete on top-level DOI/venue/year metadata, so DOI, venue, year, volume/issue/pages where used were verified against title-matched Crossref/IEEE DOI metadata. Technical claims and numeric findings are grounded in the local parses. Extractor subagents were attempted for this pass but hit 429/stream-disconnect failures, so extraction and synthesis were completed locally from the parsed Markdown.

Validation results before commit: `python tools/wiki/corpus_counts.py --json counts-batch2-final.json` reported 364 sources, 338 concepts, 73 entities, 15 findings, 15 synthesis pages, 6 comparisons, 6 methodology pages, 5 queries, 3 theses, 2 reference pages, and 612 raw-source folders. `python tools/wiki/curation_status.py --dupes --json status-batch2-final.json` reported 612 raw folders, 268 curated raw references, 344 genuinely new uncurated folders remaining, and 99 referenced-name/no-matching-raw-folder advisories; the nonzero exit is expected while uncurated folders remain. `python tools/wiki/linkcheck.py --orphans`, `python tools/wiki/process_refs.py`, `python tools/wiki/index_audit.py`, `python tools/wiki/frontmatter_audit.py`, and `git diff --check` were clean for this batch, with the link checker reporting no dangling links. `python tools/wiki/entity_roster_audit.py --json entity-roster-batch2-final.json` reported 0 claimed-but-absent over-claims and 40 advisory present-but-unlisted omissions. LLM Wiki graph health was probed, but the local `127.0.0.1:19828` service was not reachable during this run.

## [2026-07-07] Curated 5 UAV localization / semantic deployment / Rician data-harvesting / delivery sources

Added five source pages and five concept pages:

- [[cao-2026-uav-self-tracking-ms-mm]] - Cao et al. 2026, *IEEE TWC*, DOI `10.1109/TWC.2026.3686429`. GNSS-independent 3-D UAV self-tracking via EAIP minor-subspace updates, continuous MM position iteration, KF/MA smoothing, and CRLB benchmarking.
- [[li-2026-uav-bs-semantic-mfmaddpg-kde]] - Li et al. 2026, *IEEE TWC*, DOI `10.1109/TWC.2025.3641947`. Semantic-communication UAV-BS deployment using MF-MADDPG-KDE and a BLEU-derived reward under SINR/interference constraints.
- [[you-2019-rician-uav-data-harvesting]] - You & Zhang 2019, *IEEE TWC*, DOI `10.1109/TWC.2019.2911939`. UAV-enabled WSN data harvesting under angle-dependent Rician fading with outage-aware effective-fading-power regression and BCD/SCA 3-D trajectory optimization.
- [[lee-2026-uav-delivery-time-energy]] - Lee & Chae 2026, *IEEE T-ITS*, DOI `10.1109/TITS.2025.3628828`. UAV parcel pickup/drop-off under payload, no-fly-zone, variable-slot, and 3-D trajectory constraints, exposing the completion-time/propulsion-energy tradeoff.
- [[zhu-2026-uav-localization-jamming]] - Zhu et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2025.3628889`. UAV localization under jamming with GAN/TDOA mode selection, passive-measurement subset selection, and mixture-Gaussian collaborative RL.

New concept pages: [[minor-subspace-tracking]], [[kernel-density-mean-field-marl]], [[angle-dependent-rician-fading]], [[uav-delivery-pickup-dropoff]], and [[uav-localization-under-jamming]]. Updated backlinks for [[majorization-minimization]], [[cramer-rao-bound]], [[semantic-communication]], [[maddpg]], [[mean-field-game]], [[drone-cell-3d-placement]], [[uav-data-collection]], [[air-to-ground-channel-model]], [[alternating-optimization-sdr-sca]], [[rotary-wing-propulsion-energy-model]], [[energy-latency-tradeoff]], [[distributional-reinforcement-learning]], [[value-decomposition-network]], [[anti-jamming-mec]], [[uav-trajectory-control]], and [[mixed-integer-nonlinear-programming]]. Updated parse-confirmed author rosters for [[qihui-wu]] and [[tony-q-s-quek]]; no new one-off author entities were created.

Metadata notes: [[cao-2026-uav-self-tracking-ms-mm]] had DOI evidence in the local parse. The local parses for [[li-2026-uav-bs-semantic-mfmaddpg-kde]], [[you-2019-rician-uav-data-harvesting]], [[lee-2026-uav-delivery-time-energy]], and [[zhu-2026-uav-localization-jamming]] were silent or incomplete on top-level DOI/venue/year metadata, so DOI, venue, and year were verified against title-matched Crossref/IEEE DOI metadata. Technical claims and numeric findings are grounded in the local parses.

Validation results before commit: `python tools/wiki/corpus_counts.py --json counts-batch1-final.json` reported 359 sources, 333 concepts, 73 entities, 15 findings, 15 synthesis pages, 6 comparisons, 6 methodology pages, 5 queries, 3 theses, 2 reference pages, and 612 raw-source folders. `python tools/wiki/curation_status.py --dupes --json status-batch1-final.json` reported 612 raw folders, 263 curated raw references, 349 genuinely new uncurated folders remaining, and 99 referenced-name/no-matching-raw-folder advisories. `python tools/wiki/linkcheck.py --orphans`, `python tools/wiki/process_refs.py`, `python tools/wiki/index_audit.py`, `python tools/wiki/frontmatter_audit.py`, and `git diff --check` were clean for this batch, with the link checker reporting no dangling links. `python tools/wiki/entity_roster_audit.py --json entity-roster-batch1-final.json` reported 0 claimed-but-absent over-claims and 40 advisory present-but-unlisted omissions. LLM Wiki graph health was OK; `/api/v1/projects/current/graph?limit=5000` reported 815 nodes and 7721 edges.

## [2026-07-07] Synthesized LLM-assisted MEC optimization control-plane pattern

Added one methodology page and one finding page:

- [[llm-assisted-mec-optimization-control-plane]] - cross-source methodology for using LLMs as MEC optimization control-plane helpers: HybridRAG formulation ([[wen-2026-hybridrag-low-carbon-lae]]), LLM teacher policies with distillation ([[wang-2026-llm-qos-multiuav-resource]]), DRL state/reward/simulator design ([[cai-2026-llm-drl-secure-lae-data]]), and long-tail resource repair around DRL/LP checks ([[ji-2026-llm-iov-uav-offloading]]).
- [[llm-state-reward-secure-lae-data]] - finding page for the parse-reported secure-LAE result in [[cai-2026-llm-drl-secure-lae-data]]: about 35% faster convergence, 89%-85% lower AoI versus manual TD3 across secrecy-threshold settings, 88.02% AoI reduction at idle-channel ratio 0.4, and lower objective values than state-only or reward-only LLM baselines.

Connections refreshed: added backlinks from [[cai-2026-llm-drl-secure-lae-data]], [[wang-2026-llm-qos-multiuav-resource]], [[ji-2026-llm-iov-uav-offloading]], [[wen-2026-hybridrag-low-carbon-lae]], [[llm-assisted-resource-allocation]], [[generative-ai-for-mec]], [[hybridrag-network-optimization]], and [[knowledge-distillation-for-drl]]. Updated `wiki/index.md` and `wiki/overview.md` so the analytical layer now reports 15 findings and 6 methodology pages. No new entity page was created; candidate namesake/entity roster work is deferred to a separate parse-affiliation pass.

Validation results: `python tools/wiki/corpus_counts.py` reported 354 sources, 328 concepts, 73 entities, 15 findings, 15 synthesis pages, 6 comparisons, 6 methodology pages, 5 queries, 3 theses, 2 reference pages, and 345 raw-source folders. `python tools/wiki/curation_status.py --dupes` reported 345 raw folders, 345 curated raw references, 0 genuinely new uncurated folders, and 12 referenced-name/no-matching-raw-folder advisories. `python tools/wiki/linkcheck.py --orphans`, `python tools/wiki/process_refs.py`, `python tools/wiki/index_audit.py`, `python tools/wiki/frontmatter_audit.py`, and `git diff --check` were clean. LLM Wiki health was OK; `/api/v1/projects/current/graph?limit=5000` reported 805 nodes and 7631 edges.

## [2026-07-07] Curated final 5 UAV-swarm / ISCC / secure VEC / CPN / movable-antenna sources

Added five source pages and five concept pages:

- [[li-2026-tspf-forest-fire-uav-swarm]] - Li et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2025.3599384`. Two-tier submodel partition for robust UAV-swarm forest-fire detection with graph-colored groups, intragroup backup, Dynamic Server Selection, and two-tier federated aggregation.
- [[wen-2026-uav-edge-inference-iscc]] - Wen et al. 2026, *IEEE TWC*, DOI `10.1109/TWC.2026.3669999`. UAV-assisted ISCC edge inference with Hamiltonian-cycle access ordering plus AO/SA trajectory/resource optimization under discriminant-gain accuracy constraints.
- [[ren-2026-security-aware-vec-td3]] - Ren et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2026.3709174`. Security-aware UAV-assisted vehicular edge computing with TD3-controlled UAV movement, offloading ratios, and VUE-UAV association under passive-eavesdropper secure-rate degradation.
- [[deng-2026-uav-cpn-energy]] - Deng et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2026.3655118`. UAV-enabled Computing Power Network analysis using stochastic geometry and altitude/power optimization under fuel and battery constraints.
- [[lu-2026-uav-swarm-two-level-ma]] - Lu et al. 2026, *IEEE TWC*, DOI `10.1109/TWC.2026.3689048`. Low-altitude UAV-swarm two-level movable-antenna communication with joint swarm placement, local antenna positioning, and receive beamforming.

New concept pages: [[two-tier-submodel-partition]], [[uav-forest-fire-detection]], [[uav-assisted-edge-inference]], [[uav-enabled-computing-power-network]], and [[two-level-movable-antenna]]. Updated backlinks for [[integrated-sensing-computation-communication]], [[discriminant-gain]], [[vehicular-mec]], [[td3]], [[physical-layer-security]], [[task-redundancy-for-reliability]], [[federated-learning]], [[stochastic-geometry-network-analysis]], [[low-altitude-intelligent-network]], and [[movable-antenna]]. Updated parse-confirmed author rosters for [[yong-zeng]] and [[yuguang-fang]]; no one-off author entities were created.

Metadata notes: [[wen-2026-uav-edge-inference-iscc]], [[deng-2026-uav-cpn-energy]], and [[lu-2026-uav-swarm-two-level-ma]] had DOI evidence in the local parses and were cross-checked against title-matched DOI metadata. [[li-2026-tspf-forest-fire-uav-swarm]] and [[ren-2026-security-aware-vec-td3]] were parse-silent on top-level DOI/venue/year metadata, so DOI, venue, year, volume/issue/pages where used were verified against title-matched Crossref/IEEE DOI records. Technical claims and numeric findings are grounded in the local parses; hardware feasibility language for [[li-2026-tspf-forest-fire-uav-swarm]] is kept separate from full hardware validation.

Validation results: `python tools/wiki/corpus_counts.py` reported 354 sources, 328 concepts, 73 entities, 14 findings, 15 synthesis pages, 6 comparisons, 5 methodology pages, 5 queries, 3 theses, 2 reference pages, and 345 raw-source folders. `python tools/wiki/curation_status.py --dupes` reported 345 raw folders, 345 curated raw references, 0 genuinely new uncurated folders, and 12 referenced-name/no-matching-raw-folder advisories. `python tools/wiki/linkcheck.py --orphans`, `python tools/wiki/process_refs.py`, `python tools/wiki/index_audit.py`, `python tools/wiki/frontmatter_audit.py`, and `git diff --check` were clean before committing. `python tools/wiki/entity_roster_audit.py --json entity-roster-final-all-curated.json` reported 0 claimed-but-absent over-claims and 40 advisory present-but-unlisted omissions. LLM Wiki health was OK; `/graph` returned `{"error":"Not found","ok":false}` rather than graph node/edge counts.

## [2026-07-07] Curated 5 WDC / UAV analytics / cluster authentication / ISCAC / target-search sources

Added five source pages and five concept pages:

- [[zhao-2026-adaptive-wdc-wet-lae]] - Zhao et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2026.3664903`. Low-altitude multi-UAV wireless data collection and wireless energy transfer with adaptive AoI/HoE service balancing and MA2HDRL control.
- [[wang-2026-scalable-multiuav-analytics]] - Wang et al. 2026, *IEEE TGCN*, DOI `10.1109/TGCN.2025.3625726`. Scalable collaborative multi-UAV video analytics with DAG-aware centralized optimization and distributed MAPPO-based partitioning.
- [[gong-2026-lp2-casku-uav-clusters]] - Gong et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2026.3676757`. LP2-CASKU dynamic UAV-cluster authentication and session-key update for low-altitude economy networks.
- [[zhou-2026-radar-energy-iscac]] - Zhou and Zhou 2026, *IEEE TGCN*, DOI `10.1109/TGCN.2025.3587751`. UAV/HAP ISCAC radar-data collection with sensing scheduling, transmit-power, and trajectory optimization under an energy tradeoff.
- [[zhu-2026-hab-mappo-target-search]] - Zhu et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2025.3614596`. Multi-UAV cooperative target search with charging, image offloading, and HAB-MAPPO two-level attention control.

New concept pages: [[adaptive-wdc-wet-service-balancing]], [[scalable-uav-video-analytics]], [[uav-cluster-authentication]], [[radar-sensing-energy-tradeoff]], and [[attention-based-uav-target-search]]. Updated backlinks for [[uav-data-collection]], [[wireless-power-transfer]], [[age-of-information]], [[aoi-energy-tradeoff]], [[interdependent-tasks-dag]], [[dynamic-uav-clustering]], [[integrated-sensing-computation-communication]], [[collaborative-dl-inference]], [[multi-uav-assisted-mec]], [[uav-trajectory-control]], [[mappo]], [[video-analytics-offloading]], [[hierarchical-aerial-mec]], [[beta-policy-drl]], [[uav-charging-scheduling]], [[low-altitude-intelligent-network]], and [[deep-q-network]]. Updated parse-confirmed author rosters for [[victor-c-m-leung]] and [[dusit-niyato]].

Metadata notes: [[zhu-2026-hab-mappo-target-search]] had DOI evidence in the local parse. [[zhao-2026-adaptive-wdc-wet-lae]], [[wang-2026-scalable-multiuav-analytics]], [[gong-2026-lp2-casku-uav-clusters]], and [[zhou-2026-radar-energy-iscac]] were parse-silent or incomplete on top-level DOI/venue/year metadata, so DOI, venue, year, volume, issue, and page fields where used were verified against title-matched Crossref/IEEE DOI records. Technical claims and numeric findings are grounded in the local parses.

Validation results: `python tools/wiki/corpus_counts.py` reported 349 sources, 323 concepts, 73 entities, 14 findings, 15 synthesis pages, 6 comparisons, 5 methodology pages, 5 queries, 3 theses, 2 reference pages, and 345 raw-source folders before final audit. `python tools/wiki/curation_status.py --dupes` is expected to report 5 genuinely new folders still uncurated after this pass.

## [2026-07-07] Curated 5 LEO / NOMA near-field / rescue / spectrum cartography / THz relay sources

Added five source pages and three concept pages:

- [[diallo-2026-system-cost-uav-leo-offloading]] - Diallo et al. 2026, *IEEE TGCN*, DOI `10.1109/TGCN.2026.3654247`. UAV-assisted LEO task offloading with task dropping cost, UAV trajectory, transmit power, and offloading/computing schedules solved through a four-block classical decomposition.
- [[bui-2025-noma-near-far-offloading]] - Bui et al. 2025, *IEEE TGCN*, DOI `10.1109/TGCN.2024.3417697`. UAV-aided NOMA MEC with near-field/far-field coexistence, optimizing association/offloading, transmit powers, and UAV computing allocation for latency minimization.
- [[tang-2026-hg-maddpg-uav-rescue]] - Tang et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2025.3594188`. Low-altitude UAV rescue with UAVs, ground embedded robots, and airship support; HG-MADDPG combines Hungarian assignment, Lyapunov energy queues, and diffusion-enhanced MADDPG.
- [[zhao-2026-temporal-spectrum-cartography]] - Zhao et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2025.3647029`. Temporal spectrum cartography for LAE networks; RecMAE reconstructs sparse RF power maps and MADP plans mobile UAV sensor placement with a multi-agent diffusion policy.
- [[song-2026-thz-multiuav-mec]] - Song et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2026.3708383`. THz multi-UAV relay MEC with direct/relay offloading paths, molecular absorption/blockage modeling, M/M/s MEC queues, and PDD-based relay/resource/deployment optimization.

New concept pages: [[ground-embedded-robot]], [[temporal-spectrum-cartography]], and [[multi-agent-diffusion-policy]]. Updated backlinks for [[task-offloading]], [[low-altitude-intelligent-network]], [[terahertz-communication]], [[maddpg]], [[generative-diffusion-model]], [[generative-ai-for-mec]], [[multi-uav-assisted-mec]], [[noma]], [[near-field-communications]], [[leo-satellite-edge-computing]], [[penalty-dual-decomposition]], [[queueing-theory]], [[uav-mobile-relaying]], [[space-air-ground-integrated-network]], [[uav-trajectory-control]], [[lyapunov-optimization]], and [[spectrum-sensing-channel-selection]]. Updated parse-confirmed author rosters for [[geng-sun]], [[dusit-niyato]], and [[jiacheng-wang]].

Metadata notes: [[bui-2025-noma-near-far-offloading]], [[tang-2026-hg-maddpg-uav-rescue]], and [[zhao-2026-temporal-spectrum-cartography]] had DOI evidence in the local parses and were cross-checked against title-matched DOI metadata. [[diallo-2026-system-cost-uav-leo-offloading]] had a parse title typo ("Ofloading") and DOI/venue/page metadata were verified against title-matched Crossref/IEEE DOI metadata. [[song-2026-thz-multiuav-mec]] was parse-silent on top-level DOI, so DOI/venue/year were verified against title-matched Crossref/IEEE DOI metadata. Technical claims and numeric findings are grounded in the local parses; ambiguous extracted units were not over-claimed.

Validation results: `python tools/wiki/curation_status.py --dupes` reported 345 raw folders, 335 curated raw references, 10 genuinely new folders still uncurated after this pass, and 12 referenced-name/no-matching-raw-folder advisories. `python tools/wiki/corpus_counts.py` reported 344 sources, 318 concepts, 73 entities, 14 findings, 15 synthesis pages, 6 comparisons, 5 methodology pages, 5 queries, 3 theses, 2 reference pages, and 345 raw-source folders. `python tools/wiki/linkcheck.py --orphans`, `python tools/wiki/process_refs.py`, `python tools/wiki/index_audit.py`, `python tools/wiki/frontmatter_audit.py`, and `git diff --check` were clean before committing. `python tools/wiki/entity_roster_audit.py --json entity-roster-leo-noma-rescue-spectrum-thz.json` reported 0 claimed-but-absent over-claims and 40 advisory present-but-unlisted omissions. LLM Wiki health was OK; `/graph` returned `{"error":"Not found","ok":false}` rather than graph node/edge counts.

## [2026-07-07] Curated 5 battery / secure caching / service migration / QoS NOMA / LAE compliance sources

Added five source pages and four concept pages:

- [[ye-2026-flight-speed-battery-swapping]] - Ye et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2025.3601743`. Flight-speed scheduling, battery swapping, and offloading for UAV-enabled MEC patrol inspection; virtual-node graph reformulation and ATC heuristic.
- [[hu-2026-ertatd3-secure-caching]] - Hu et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2026.3709182`. UAV-assisted vehicular MEC with secure task-result caching and ERTATD3 twin-actor reward shaping over trajectory/offloading/resource/caching decisions.
- [[feng-2026-prediction-service-migration]] - Feng et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2026.3700894`. Prediction-assisted multi-UAV service migration and trajectory control for vehicular MEC using stacked LSTM, Lyapunov migration-cost control, and MADDPG.
- [[chen-2026-qos-noma-multiuav]] - Chen et al. 2026, *IEEE TWC*, DOI `10.1109/TWC.2025.3593884`. QoS-oriented NOMA multi-UAV MEC offloading with explicit task priorities, Lagrange-dual constraint handling, and improved SAC.
- [[gong-2026-safe-economic-lae-trajectory]] - Gong et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2026.3668209`. Hybrid SAC-LLM low-altitude UAV trajectory planning with obstacle avoidance, no-fly-zone/residential-zone compliance, landing, and energy constraints.

New concept pages: [[battery-swapping-uav-mec]], [[analytical-target-cascading]], [[secure-caching-uav-mec]], and [[compliance-aware-uav-trajectory]]. Updated backlinks for [[task-offloading]], [[service-caching-mec]], [[uav-trajectory-control]], [[privacy-sensitive-data-partitioning]], [[vehicular-mec]], [[service-migration]], [[lyapunov-optimization]], [[maddpg]], [[noma]], [[task-priority-in-mec]], [[dynamic-qos-constraints]], [[soft-actor-critic]], [[td3]], [[safe-reinforcement-learning]], [[llm-assisted-resource-allocation]], [[generative-ai-for-mec]], and [[low-altitude-intelligent-network]]. Updated existing parse-confirmed author rosters for [[dusit-niyato]], [[jiawen-kang]], [[shengli-xie]], [[weifeng-zhong]], [[xumin-huang]], and [[tony-q-s-quek]]; no new author entities were created.

Metadata notes: [[ye-2026-flight-speed-battery-swapping]] had DOI evidence in the local parse. The parses for [[hu-2026-ertatd3-secure-caching]], [[feng-2026-prediction-service-migration]], [[chen-2026-qos-noma-multiuav]], and [[gong-2026-safe-economic-lae-trajectory]] were silent or incomplete on top-level DOI/venue/year, so DOI/venue/year were verified against title-matched Crossref/IEEE DOI records. Technical claims and numeric findings are grounded in the local parses.

Validation results: `python tools/wiki/curation_status.py --dupes` reported 345 raw folders, 325 curated raw references, 20 genuinely new folders still uncurated after this pass, and 12 referenced-name/no-matching-raw-folder advisories. `python tools/wiki/corpus_counts.py` reported 334 sources, 312 concepts, 73 entities, 14 findings, 15 synthesis pages, 6 comparisons, 5 methodology pages, 5 queries, 3 theses, 2 reference pages, and 345 raw-source folders. `python tools/wiki/linkcheck.py --orphans`, `python tools/wiki/process_refs.py`, `python tools/wiki/index_audit.py`, `python tools/wiki/frontmatter_audit.py`, and `git diff --check` were clean before committing. `python tools/wiki/entity_roster_audit.py --json entity-roster-current-batch-postroster.json` reported 0 claimed-but-absent over-claims and 40 advisory present-but-unlisted omissions. LLM Wiki health was OK; `/graph` returned `{"error":"Not found","ok":false}` rather than graph node/edge counts.

## [2026-07-07] Curated 5 MODE / parallel caching / semantic IoV / networked ISAC / RIS-online sources

Added five source pages and four concept pages:

- [[ye-2026-mode-lae-isac]] - Ye et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2026.3693366`. Multi-objective LAE ISAC with MODE, a DDPG plus mixture-of-experts multi-task controller for communication/sensing objective-preference tradeoffs over GBS beamforming and authorized-UAV trajectories.
- [[fan-2026-parallel-caching-uav-mec]] - Fan et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2026.3674329`. Multi-task parallel execution in UAV-assisted MEC; RLTL combines lower-layer DQN caching/offloading with upper-layer regret-minimization channel allocation.
- [[liu-2025-multimodal-semantic-iov-jamming]] - Liu et al. 2025, *IEEE TMC*, DOI `10.1109/TMC.2025.3550965`. Multi-UAV-assisted IoV MEC under jamming with multi-modal semantic communication; SC-MA-TD3 jointly controls trajectories, user association, and channels.
- [[zhao-2025-networked-isac-uav-handover]] - Zhao et al. 2025, *IEEE TWC*, DOI `10.1109/TWC.2025.3562396`. Networked ISAC UAV tracking and handover for LAE using virtual sensing cells, MUSIC estimation, centralized EKF fusion, PBS handover, and VSC handover.
- [[sheng-2025-ris-online-uav-mec]] - Sheng et al. 2025, *IEEE TGCN*, DOI `10.1109/TGCN.2024.3503687`. RIS-empowered online UAV-MEC trajectory/resource allocation with Lyapunov/Dinkelbach/BCD/SCA under mobile users, random arrivals, queue stability, outage constraints, and finite UAV energy.

New concept pages: [[mixture-of-experts-drl]], [[multi-modal-semantic-communication]], [[networked-isac]], and [[regret-minimization-learning]]. Updated backlinks for [[integrated-sensing-and-communication]], [[low-altitude-intelligent-network]], [[semantic-communication]], [[anti-jamming-mec]], [[multi-agent-td3]], [[parallel-vs-serial-processing]], [[service-caching-mec]], [[stochastic-game]], [[lyapunov-optimization]], [[intelligent-reflecting-surface]], and [[uav-trajectory-control]].

Metadata notes: [[ye-2026-mode-lae-isac]] had DOI/venue evidence in the local parse. The parses for [[fan-2026-parallel-caching-uav-mec]], [[liu-2025-multimodal-semantic-iov-jamming]], [[zhao-2025-networked-isac-uav-handover]], and [[sheng-2025-ris-online-uav-mec]] were silent on top-level DOI/venue/year, so DOI, year, venue, volume, issue, and page fields where used were verified against title-matched Crossref/IEEE DOI records. Technical claims and numeric findings are grounded in the local parses.

Validation results: `python tools/wiki/curation_status.py --dupes` reported 345 raw folders, 320 curated raw references, 25 genuinely new folders still uncurated after this pass, and 12 referenced-name/no-matching-raw-folder advisories. `python tools/wiki/corpus_counts.py` reported 329 sources, 308 concepts, 73 entities, 14 findings, 15 synthesis pages, 6 comparisons, 5 methodology pages, 5 queries, 3 theses, 2 reference pages, and 345 raw-source folders. `python tools/wiki/linkcheck.py --orphans`, `python tools/wiki/process_refs.py`, `python tools/wiki/index_audit.py`, `python tools/wiki/frontmatter_audit.py`, and `git diff --check` were clean before committing. `python tools/wiki/entity_roster_audit.py --json entity-roster-current-batch-prelog.json` reported 0 claimed-but-absent over-claims and 40 advisory present-but-unlisted omissions. LLM Wiki health was OK; `/graph` and `/api/graph` returned `{"error":"Not found","ok":false}` rather than graph node/edge counts.

## [2026-07-07] Curated 5 hybrid UAV-MEC / LAE imaging / Air-ISCC / SAGIN / movable-antenna sources

Added five source pages and one concept page:

- [[hu-2026-latency-hybrid-uav-mec]] - Hu et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2026.3667786`. Wireless-powered hybrid UAV-GBS MEC with TDMA/NOMA access; double-loop AO/bisection optimizes slot count, time scheduling, CPU frequency, transmit power, and 3D UAV trajectory for latency minimization.
- [[huang-2026-offgrid-lae-imager]] - Huang et al. 2026, *IEEE TWC*, DOI `10.1109/TWC.2025.3603255`. Cooperative ISAC low-altitude wireless imaging; CS/PSF analysis and a physics-embedded DNN with OHEM reconstruct off-grid targets from CSI.
- [[hou-2025-pbia-air-iscc-uav-its]] - Hou et al. 2025, *IEEE TGCN*, DOI `10.1109/TGCN.2024.3492028`. UAV-swarm Air-ISCC for intelligent transportation systems; PBIA/PPO jointly controls sensing time, power, service association, and computation allocation.
- [[chen-2026-pddqn-sagin-mec]] - Chen et al. 2026, *IEEE TWC*, DOI `10.1109/TWC.2026.3706356`. MEC-enabled SAGIN with local/UAV/LEO partial offloading; P-DDQN combines discrete association decisions with continuous transmit power, task ratios, and UAV trajectory control under LEO coverage-time constraints.
- [[zeng-2026-movable-antenna-u2u-channel]] - Zeng et al. 2026, *IEEE TWC*, DOI `10.1109/TWC.2025.3649584`. Movable-antenna-aided MIMO wideband UAV-to-UAV channel modeling for LAE; derives STF-CF/SD-PSD/PSDS expressions and optimizes antenna positions.

New concept page: [[movable-antenna]]. Updated backlinks for WPT/NOMA/A2G channels, ISAC/ISCC, wireless perception, low-altitude intelligent networks, SAGIN/LEO edge computing, hybrid-action/P-DQN, UAV-enabled ITS, and device association. Updated parse-confirmed author rosters for [[dusit-niyato]] and [[victor-c-m-leung]].

Metadata notes: [[huang-2026-offgrid-lae-imager]] and [[hou-2025-pbia-air-iscc-uav-its]] had DOI/date evidence in the local parses and were also title-matched against DOI metadata. [[hu-2026-latency-hybrid-uav-mec]], [[chen-2026-pddqn-sagin-mec]], and [[zeng-2026-movable-antenna-u2u-channel]] had parse-silent top-level DOI fields, so DOI/venue/year were verified against title-matched Crossref/IEEE DOI records. Technical claims and numeric findings are grounded in the local parses.

Validation results: `python tools/wiki/curation_status.py --dupes` reported 345 raw folders, 315 curated raw references, 30 genuinely new folders still uncurated after this pass, and 12 referenced-name/no-matching-raw-folder advisories. `python tools/wiki/corpus_counts.py` reported 324 sources, 304 concepts, 73 entities, 14 findings, 15 synthesis pages, 6 comparisons, 5 methodology pages, 5 queries, 3 theses, 2 reference pages, and 345 raw-source folders. `python tools/wiki/linkcheck.py --orphans`, `python tools/wiki/process_refs.py`, `python tools/wiki/index_audit.py`, `python tools/wiki/frontmatter_audit.py`, and `git diff --check` were clean before committing. `python tools/wiki/entity_roster_audit.py --json entity-roster-current-pass-final.json` reported 0 claimed-but-absent over-claims and 40 advisory present-but-unlisted omissions. LLM Wiki health was OK; `/graph` and `/api/graph` returned `{"error":"Not found","ok":false}` rather than graph node/edge counts.

## [2026-07-07] Curated 4 LLM / GAT / AoI UAV-MEC sources and reconciled 1 RIS-ISAC raw path

Added four source pages:

- [[zhan-2026-gatd3qn-dependent-offloading]] - Zhan et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2025.3628608`. Joint UAV placement, UAV-GU association, and dependent-task DAG offloading in multi-UAV MEC; JSPO uses SCA/PDD for placement/association, and GAT-enhanced D3QN handles binary dependent-subtask offloading.
- [[liao-2026-aoi-ris-uav-usv-mec]] - Liao et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2025.3611808`. AoI-aware RIS-assisted UAV-USV MEC for inland waterways; TUAV-mounted RIS, RUAV service durations, RIS phase shifts, TUAV altitude, RUAV trajectories, and Lyapunov plus enhanced WOA/AO optimization.
- [[cai-2026-llm-drl-secure-lae-data]] - Cai et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2026.3665241`. LLM-enhanced DRL for secure LAE data collection; the LLM acts as state processor, reward designer, and simulator for DDPG/TD3 control with a data-collection UAV and a jamming UAV.
- [[wang-2026-llm-qos-multiuav-resource]] - Wang et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2026.3683128`. LLM teacher-student QoS-aware resource allocation for multi-UAV cooperative edge computing; NKG/R-GAT/LoRA/Tree-of-Thoughts teacher policies are distilled into MAPPO UAV students.

Raw-reference reconciliation: [[chu-2024-secure-ris-isac]] now references the current `Joint_Beamforming_and_Reflection_Design_for_Secure_RIS-ISAC_Systems` raw folder instead of the stale `.pdf/full.md` path. The source page already existed and matched DOI `10.1109/TVT.2023.3328192`, so no duplicate source page was created.

Updated backlinks and track pages for [[interdependent-tasks-dag]], [[graph-neural-network]], [[dueling-dqn]], [[penalty-dual-decomposition]], [[task-offloading]], [[multi-uav-assisted-mec]], [[uav-trajectory-control]], [[age-of-information]], [[aoi-energy-tradeoff]], [[uav-usv-cooperative-mec]], [[uav-mounted-ris]], [[intelligent-reflecting-surface]], [[lyapunov-optimization]], [[whale-optimization-algorithm]], [[maritime-mec]], [[low-altitude-intelligent-network]], [[generative-ai-for-mec]], [[llm-assisted-resource-allocation]], [[prompt-engineering]], [[td3]], [[ddpg]], [[physical-layer-security]], [[friendly-jamming-uav]], [[uav-data-collection]], [[knowledge-distillation-for-drl]], [[mappo]], [[graph-based-resource-management]], [[task-migration]], [[jains-fairness-index]], [[fairness-metrics-in-mec]], and [[device-association]]. Updated parse-confirmed existing author rosters for [[dusit-niyato]] and [[jiacheng-wang]]. No new concept or entity pages were created.

Metadata notes: DOI/venue/year fields for the four new source pages were verified through title-matched Crossref metadata because the local parses were incomplete or draft-like at top-level metadata. Technical claims and numeric findings are grounded in the local parses. [[chu-2024-secure-ris-isac]] had already been curated; only its raw-artifact path was corrected.

Validation results: `python tools/wiki/curation_status.py --dupes` reported 345 raw folders, 310 curated raw references, and 35 genuinely new folders still uncurated after this pass, plus 12 referenced-name/no-matching-raw-folder advisories. `python tools/wiki/corpus_counts.py` reported 319 sources, 303 concepts, 73 entities, 14 findings, 15 synthesis pages, 6 comparisons, 5 methodology pages, 5 queries, 3 theses, 2 reference pages, and 345 raw-source folders. `python tools/wiki/linkcheck.py --orphans`, `python tools/wiki/process_refs.py`, `python tools/wiki/index_audit.py`, `python tools/wiki/frontmatter_audit.py`, and `git diff --check` were clean before committing. `python tools/wiki/entity_roster_audit.py --json entity-roster-llm-gat-aoi-prelog.json` reported 0 claimed-but-absent over-claims and 40 advisory present-but-unlisted omissions. LLM Wiki health was OK; `/graph` and `/api/graph` returned `{"error":"Not found","ok":false}` rather than graph node/edge counts.

## [2026-07-07] Curated 5 UAV positioning / inspection / RIS / association / THz-SAG sources

Added five source pages and four concept pages:

- [[wang-2025-ppo-uav-positioning-offloading]] - Wang et al. 2025, *IEEE TMC*, DOI `10.1109/TMC.2025.3562806`. PPO-based joint UAV positioning and partial task offloading in multi-UAV MEC; BS/UAV task splitting, access/backhaul links, latency minimization, energy balance, and UAV-failure resilience.
- [[guo-2026-aot-uav-inspection-offloading]] - Guo et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2025.3636717`. AGI-oriented Transformer for UAV-assisted railway inspection; shared encoder with trajectory-planning and task-offloading heads for sensor/UAV/hive execution decisions.
- [[wu-2026-model-based-ppo-ris-uav-mec]] - Wu et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2026.3679344`. Decentralized model-based PPO for RIS-assisted urban multi-UAV MEC; k-hop local observations, RIS phase proposals, local dynamics models, and short-horizon branched rollouts.
- [[gao-2026-fmad3qn-uav-gd-association]] - Gao et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2026.3656412`. Heterogeneous multi-UAV MEC with no-fly zones; closed-form UAV-GD association via Lagrangian duality and optimal transport, then federated multi-agent dueling DDQN for 3D deployment.
- [[tun-2025-thz-sag-mec-resource-allocation]] - Tun et al. 2025, *IEEE TMC*, DOI `10.1109/TMC.2024.3516655`. THz-assisted MEC-enabled SAG networks; BCD decomposes device offloading, THz sub-band/power control, UAV deployment, and UAV-to-UAV/LEO task forwarding.

New concept pages: [[transformer-encoder]], [[model-based-marl]], [[optimal-transport-theory]], and [[block-successive-upper-bound-minimization]]. Updated concept backlinks for [[ppo]], [[dueling-dqn]], [[terahertz-communication]], [[multi-uav-assisted-mec]], [[uav-trajectory-control]], [[device-association]], [[intelligent-reflecting-surface]], [[space-air-ground-integrated-network]], [[federated-reinforcement-learning]], and [[task-offloading]]. Updated parse-confirmed [[xuemin-shen]] roster with [[guo-2026-aot-uav-inspection-offloading]]. No other author entity pages were created or merged.

Metadata notes: all five DOI/venue/year fields were verified through title-matched Crossref metadata because the parses were silent or incomplete at the top-level metadata fields. [[guo-2026-aot-uav-inspection-offloading]] also had the DOI visible in the parse. Technical claims and numeric findings are grounded in the local parses.

Validation results: `python tools/wiki/curation_status.py --dupes` reported 345 raw folders, 305 curated raw references, and 40 genuinely new folders still uncurated after this pass, plus 13 referenced-name/no-matching-raw-folder advisories. `python tools/wiki/corpus_counts.py` reported 315 sources, 303 concepts, 73 entities, 14 findings, 15 synthesis pages, 6 comparisons, 5 methodology pages, 5 queries, 3 theses, 2 reference pages, and 345 raw-source folders. `python tools/wiki/linkcheck.py --orphans`, `python tools/wiki/process_refs.py`, `python tools/wiki/index_audit.py`, `python tools/wiki/frontmatter_audit.py`, and `git diff --check` were clean. `python tools/wiki/entity_roster_audit.py --json entity-roster-uav-positioning-inspection-ris-thz.json` reported 0 claimed-but-absent over-claims and 40 advisory present-but-unlisted omissions; no new over-claim was introduced. LLM Wiki health was OK; `/graph` and `/api/graph` returned 404 rather than graph node/edge counts.

## [2026-07-07] Curated 5 SAGIN / HAP / RIS / JSCC / IoV optimization sources

Added five source pages and four concept pages:

- [[zhao-2026-hcdrl-ga-sagin-sar]] — Zhao et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2026.3709181`. Multi-UAV search and rescue in SAGINs; HCDRL/HCSAC jointly handles trajectory and offloading with CNN+GCN state encoding, while GA searches UAV deployment under NOAA-derived wind fields.
- [[li-2026-uav-hap-ddqn-ppo-offloading]] — Li et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2026.3683404`. Multi-UAV and HAP cooperative offloading; DDQN selects single-UAV / multi-UAV / HAP mode and PPO assigns cooperative task ratios for latency-energy weighted system consumption.
- [[qin-2023-ris-uav-mec-ee]] — Qin et al. 2023, *IEEE TGCN*, DOI `10.1109/TGCN.2023.3287604`. RIS-assisted UAV-MEC energy-efficiency optimization with NOMA and imperfect CSI; Dinkelbach plus BCD/DC/SCA optimize offloaded bits, power, RIS phase shifts, and UAV trajectory.
- [[zhao-2026-mappo-jscc-aec]] — Zhao et al. 2026, *IEEE TWC*, DOI `10.1109/TWC.2025.3590253`. HAP-assisted collaborative multi-UAV aerial edge computing; JSCC couples sensing repeat times, NOMA/OMA communication, local/U2U/U2H computation, Lyapunov stability, and MAPPO-JSCC with embedded convex sub-solvers.
- [[ji-2026-llm-iov-uav-offloading]] — Ji et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2026.3700664`. Multi-UAV-assisted IoV offloading; SOCP handles 3D trajectory, DRL+LLM schedules resource allocation, and LP computes task-offloading ratios for latency/energy/task-success tradeoffs.

New concept pages: [[genetic-algorithm]], [[second-order-cone-programming]], [[linear-programming]], and [[llm-assisted-resource-allocation]]. Updated concept backlinks for [[space-air-ground-integrated-network]], [[uav-trajectory-control]], [[high-altitude-platform-station]], [[hierarchical-aerial-mec]], [[intelligent-reflecting-surface]], [[fractional-programming-dinkelbach]], [[integrated-sensing-computation-communication]], [[mappo]], [[vehicular-mec]], [[uav-enabled-its]], and [[energy-latency-tradeoff]]. No author entity pages were created or merged; [[haijun-zhang]] remains an advisory roster omission for [[li-2026-uav-hap-ddqn-ppo-offloading]] because the available parse/PDF text confirmed the name and IEEE Fellow status but did not expose the affiliation/email block needed for identity-safe roster merging.

Metadata notes: the local parses were silent or incomplete on top-level DOI/venue/year, so DOI, year, and venue were verified through title-matched Crossref/IEEE metadata before writing the source pages. Technical claims and numeric findings are grounded in the local parses.

Validation results: `python tools/wiki/curation_status.py --dupes` reported 345 raw folders, 300 curated raw references, and 45 genuinely new folders still uncurated after this pass, plus 13 referenced-name/no-matching-raw-folder advisories. `python tools/wiki/corpus_counts.py` reported 310 sources, 299 concepts, 73 entities, 14 findings, 15 synthesis pages, 6 comparisons, 5 methodology pages, 5 queries, 3 theses, 2 reference pages, and 345 raw-source folders. `python tools/wiki/linkcheck.py --orphans`, `python tools/wiki/process_refs.py`, `python tools/wiki/index_audit.py`, `python tools/wiki/frontmatter_audit.py`, and `git diff --check` were clean. `python tools/wiki/entity_roster_audit.py --json entity-roster-after-llm-iov.json` reported 0 claimed-but-absent over-claims and 40 advisory present-but-unlisted omissions, with the new unresolved advisory being [[haijun-zhang]] for [[li-2026-uav-hap-ddqn-ppo-offloading]]. LLM Wiki health was OK; `/graph` and `/api/graph` returned `{"error":"Not found","ok":false}` rather than graph node/edge counts.

## [2026-07-07] Curated 3 LAE-ISAC / ISAC-VEC sources and reconciled 2 raw duplicates

Added three source pages and three concept pages:

- [[ye-2026-meta-deepesc-lae-isac]] — Ye et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2026.3678893`. Meta-DeepESC for energy-efficient LAE ISAC; TD3-style constrained action selection, episodic replay, and meta-learning jointly optimize GBS beamforming and authorized-UAV trajectories under sensing, mission, collision, and power constraints.
- [[ye-2026-deeplsc-lae-isac]] — Ye et al. 2026, *IEEE TWC*, DOI `10.1109/TWC.2025.3583950`. DeepLSC for LAE ISAC communication sum-rate; DDPG-based beamforming/trajectory control with constrained noise exploration, hierarchical experience replay, and symmetric experience augmentation.
- [[li-2026-isac-vec-beamforming-deployment]] — Li et al. 2026, *IEEE TWC*, DOI `10.1109/TWC.2026.3694912`. ISAC-enhanced UAV-assisted VEC; refraction-based sparrow search optimizes UAV deployment, while SCA/Taylor convexification handles beamforming for road-hotspot coverage, sensing, and energy tradeoffs.

New concept pages: [[episodic-experience-replay]], [[meta-deep-reinforcement-learning]], and [[sparrow-search-algorithm]]. Updated concept backlinks for [[integrated-sensing-and-communication]], [[low-altitude-intelligent-network]], [[uav-trajectory-control]], [[vehicular-mec]], [[ddpg]], [[td3]], [[prioritized-experience-replay]], [[alternating-optimization-sdr-sca]], [[weighted-kmeans-uav-deployment]], [[cramer-rao-bound]], and [[integrated-sensing-computation-communication]]. Updated [[swarm-metaheuristics-in-uav-mec]] for the sparrow-search roster entry. Updated parse-confirmed [[jie-xu]] roster with [[ye-2026-deeplsc-lae-isac]].

Raw-reference reconciliation: [[tang-2024-iscc-uav-feel]] now also references the `Integrated Sensing- Computation- and Communication for UAV-Assisted Federated Edge Learning` raw folder, and [[nabi-2025-jour-hierarchical-aerial]] now also references the `Joint Offloading Decision- User Association- and Resource Allocation in Hierarchical Aerial Computing Collaboration of UAVs and HAP` raw folder. These titles matched already-curated pages, so no duplicate source pages were created.

Metadata notes: [[ye-2026-deeplsc-lae-isac]] includes a parse DOI line. The local parses for [[ye-2026-meta-deepesc-lae-isac]] and [[li-2026-isac-vec-beamforming-deployment]] were silent on top-level DOI/venue/year, so DOI, venue, and year were verified through title-matched Crossref metadata. Technical claims and numeric findings are grounded in the local parses.

Validation results: `python tools/wiki/curation_status.py --dupes` reported 345 raw folders, 295 curated raw references, and 50 genuinely new folders still uncurated after this pass, plus 13 referenced-name/no-matching-raw-folder advisories. `python tools/wiki/corpus_counts.py` reported 305 sources, 295 concepts, 73 entities, 14 findings, 15 synthesis pages, 6 comparisons, 5 methodology pages, 5 queries, 3 theses, 2 reference pages, and 345 raw-source folders. `python tools/wiki/linkcheck.py --orphans`, `python tools/wiki/process_refs.py`, `python tools/wiki/index_audit.py`, `python tools/wiki/frontmatter_audit.py`, and `git diff --check` were clean. `python tools/wiki/entity_roster_audit.py` reported 0 claimed-but-absent over-claims and 39 advisory present-but-unlisted omissions; the remaining [[jie-xu]] advisory is the explicitly documented Guangdong-University-of-Technology namesake in [[wang-2018-wpt-mec-joint-offloading]]. LLM Wiki health was OK; `/graph` and `/api/graph` returned `{"error":"Not found","ok":false}` rather than graph node/edge counts.

## [2026-07-07] Curated 5 LAE / spatiotemporal-DRL / vehicle-twin sources

Added five source pages and five concept pages:

- [[yang-2026-generative-radio-map-lae]] — Yang et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2026.3665545`. CVCGAN-assisted generative radio map for LAE air-corridor channel estimation; grid-labeled CSI, pretrained estimator, label-MSE regularization, WGAN-GP stabilization, and CNN integration over generated/estimated CSI.
- [[teng-2026-gstrl-sequential-offloading]] — Teng et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2025.3635085`. Graph-based spatiotemporal RL for sequential task offloading in multi-UAV MEC; heterogeneous UAV/task graph encoding, LSTM temporal context, masked PPO, and linear task-chain constraints.
- [[zhao-2026-heuristic-supervised-drl]] — Zhao et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2026.3681665`. Heuristic-supervised DRL with TTSSA convergence analysis; a PSO-MARL UAV-MEC case study links heuristic planning, supervised policy prediction, and DRL control.
- [[chen-2026-hc-mappo-vehicle-twin-migration]] — Chen et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2026.3674825`. Hierarchical-control MAPPO for vehicle-twin migration in UAV-assisted vehicular metaverses; ACB-LSTM workload prediction feeds upper-layer UAV/RSU selection and deterministic lower-layer migration mapping.
- [[wen-2026-hybridrag-low-carbon-lae]] — Wen et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2025.3637120`. HybridRAG-based LLM agents formulate low-carbon LAE network optimization; R^2DSAC uses double regularization and diffusion-enhanced SAC for rotary-wing UAV-MEC offloading/resource decisions.

New concept pages: [[radio-map-assisted-channel-estimation]], [[sequential-task-offloading]], [[heuristic-supervised-drl]], [[vehicle-twin-migration]], and [[hybridrag-network-optimization]]. Updated concept backlinks for [[generative-adversarial-network]], [[low-altitude-intelligent-network]], [[task-offloading]], [[graph-neural-network]], [[particle-swarm-optimization]], [[two-timescale-optimization]], [[task-migration]], [[vehicular-mec]], [[digital-twin]], [[diffusion-model-as-optimizer]], [[soft-actor-critic]], and [[mappo]]. Updated parse-confirmed author rosters for [[jiawen-kang]], [[dusit-niyato]], and [[nei-kato]]. [[wei-zhang]] remains an advisory namesake: the Wei Zhang in [[yang-2026-generative-radio-map-lae]] is listed with UNSW, while the existing entity page tracks a Shandong University author cluster.

Metadata notes: the local parses were silent on top-level DOI/venue/year, so DOI, year, and *IEEE Transactions on Mobile Computing* venue fields were verified through title-matched Crossref metadata. Technical claims and numeric findings are grounded in the local parses.

Validation results: `python tools/wiki/curation_status.py --dupes` reported 345 raw folders, 290 curated raw references, and 55 genuinely new folders still uncurated after this pass, plus 13 referenced-name/no-matching-raw-folder advisories. `python tools/wiki/corpus_counts.py` reported 302 sources, 292 concepts, 73 entities, 14 findings, 15 synthesis pages, 6 comparisons, 5 methodology pages, 5 queries, 3 theses, 2 reference pages, and 345 raw-source folders. `python tools/wiki/linkcheck.py --orphans`, `python tools/wiki/process_refs.py`, `python tools/wiki/index_audit.py`, `python tools/wiki/frontmatter_audit.py`, and `git diff --check` were clean. `python tools/wiki/entity_roster_audit.py` reported 0 claimed-but-absent over-claims and 39 advisory present-but-unlisted omissions, including the unresolved Wei Zhang namesake. LLM Wiki health was OK; `/graph` and `/api/graph` returned `{"error":"Not found","ok":false}` rather than graph node/edge counts.

## [2026-07-07] Curated 5 secure / storage / identification / Pareto-offloading sources

Added five source pages and three concept pages:

- [[wang-2026-secure-reliable-uav-mec]] — Wang et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2025.3629147`. Energy-efficient UAV-assisted MEC with secure and reliable data transmission; user-side artificial noise, secrecy-outage chance constraints, fixed-wing trajectory/resource allocation, and augmented-Lagrangian secure-energy-efficiency optimization.
- [[li-2025-energy-latency-uav-vec]] — Li et al. 2025, *IEEE TGCN*, DOI `10.1109/TGCN.2024.3433457`. UAV-assisted vehicular edge computing for FL participant selection and bandwidth/compute allocation; AB-DDQN with AdamW and BOA hyperparameter tuning optimizes an energy-latency tradeoff.
- [[huang-2026-erasure-coded-uav-storage]] — Huang et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2025.3594283`. Erasure-coded UAV edge storage for post-disaster data access; ME-HDRL combines CNN+ConvLSTM trajectory prediction, DDQN UAV placement agents, a PPO edge access agent, and action filtering.
- [[zeng-2026-fmcw-isibc-lae]] — Zeng & Liang 2026, *IEEE TWC*, DOI `10.1109/TWC.2025.3650197`. FMCW-enabled integrated sensing, identification, and backscatter communication for LAE; UAV-mounted BDs carry identity symbols on FMCW echoes, with SVD-based estimation and CRLB analysis.
- [[yang-2025-generalizable-pareto-offloading]] — Yang et al. 2025, *IEEE TSC*, DOI `10.1109/TSC.2025.3604371`. Generalizable Pareto-optimal MEC offloading; context-conditioned Discrete-SAC learns one delay/energy policy across preference vectors, edge-server counts, and CPU-frequency profiles.

New concept pages: [[erasure-coded-edge-storage]], [[uav-backscatter-identification]], and [[contextual-momdp]]. Updated concept backlinks for [[physical-layer-security]], [[multi-objective-reinforcement-learning]], [[backscatter-communication]], [[post-disaster-mec]], [[energy-latency-tradeoff]], [[vehicular-mec]], and [[mmwave-radar-sensing]]. No author entity pages were created; parse-confirmed authors were not merged into existing author entities without a specific identity-confirmation need.

Metadata notes: DOI/venue/year for [[li-2025-energy-latency-uav-vec]] were present in the parse. The local parses for [[wang-2026-secure-reliable-uav-mec]], [[huang-2026-erasure-coded-uav-storage]], [[zeng-2026-fmcw-isibc-lae]], and [[yang-2025-generalizable-pareto-offloading]] were silent on top-level DOI/venue/year, so those fields were verified through title-matched Crossref metadata. Technical claims are grounded in the local parses.

Validation results: `python tools/wiki/curation_status.py --dupes` reported 345 raw folders, 285 curated raw references, and 60 genuinely new folders still uncurated after this pass, plus 13 referenced-name/no-matching-raw-folder advisories. `python tools/wiki/corpus_counts.py` reported 297 sources, 287 concepts, 73 entities, 14 findings, 15 synthesis pages, 6 comparisons, 5 methodology pages, 5 queries, 3 theses, 2 reference pages, and 345 raw-source folders. `python tools/wiki/linkcheck.py --orphans`, `python tools/wiki/process_refs.py`, `python tools/wiki/index_audit.py`, `python tools/wiki/frontmatter_audit.py`, and `git diff --check` were clean. `python tools/wiki/entity_roster_audit.py` reported 0 claimed-but-absent over-claims and 38 advisory present-but-unlisted omissions, all outside the newly curated source authors. LLM Wiki health was OK; `/graph/current` returned `{"ok":false,"error":"Not found"}` rather than graph node/edge counts.

## [2026-07-07] Curated 5 low-altitude / semantic / green-AEC sources

Added five source pages and two concept pages:

- [[wang-2026-blockchain-lae-fl-mappo]] — Wang et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2026.3709198`. Blockchain-assisted low-altitude edge-intelligence network; UEs/TUAVs/SUAVs/BS four-layer offloading, caching, FL, PV-aware throttling, M/M/1 queueing, and blockchain-supported cache cooperation.
- [[zhao-2025-probabilistic-semantic-sagin]] — Zhao et al. 2025, *IEEE TWC*, DOI `10.1109/TWC.2025.3569102`. SAGIN-enabled probabilistic semantic communication; satellite-UAV-GT relay model with shared probabilistic graphs and compression/computation energy tradeoff.
- [[xiao-2025-star-ris-bidirectional-uav-mec]] — Xiao et al. 2025, *IEEE TWC*, DOI `10.1109/TWC.2025.3529252`. STAR-RIS-enhanced UAV-MEC with same-slot bidirectional offloading to BS-MEC and UAV-MEC servers; Dinkelbach/SCA BCD energy-efficiency maximization.
- [[wang-2026-secure-lae-uav-scheduling]] — Wang et al. 2026, *IEEE TWC*, DOI `10.1109/TWC.2026.3680053`. Secure low-altitude aerial communications; UAVs dynamically switch between communication and artificial-noise jamming roles while optimizing scheduling, power, 3D trajectory, and velocity.
- [[ma-2026-mean-field-green-aec]] — Ma et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2026.3698303`. Green aerial edge computing for metaverse users; mean-field-game task allocation plus Lyapunov energy valuation across CE-UAVs and energy-harvesting EF-UAVs, with Raspberry Pi5/A100 hardware-in-the-loop validation.

New concept pages: [[probabilistic-semantic-communication]] and [[mean-field-game]]. Updated concept backlinks for [[semantic-communication]], [[space-air-ground-integrated-network]], [[star-ris]], [[uav-mounted-ris]], [[task-offloading]], [[low-altitude-intelligent-network]], [[energy-harvesting-mec]], [[blockchain-for-fl-aggregation]], [[federated-learning]], [[mappo]], [[physical-layer-security]], [[friendly-jamming-uav]], [[lyapunov-optimization]], [[uav-trajectory-control]], [[alternating-optimization-sdr-sca]], and [[fractional-programming-dinkelbach]]. No author entity pages were created; parse-confirmed authors were not merged into existing author entities without a specific identity-confirmation need.

Metadata notes: DOI/venue/year for [[wang-2026-blockchain-lae-fl-mappo]], [[zhao-2025-probabilistic-semantic-sagin]], and [[xiao-2025-star-ris-bidirectional-uav-mec]] were present in the parses. [[wang-2026-secure-lae-uav-scheduling]] and [[ma-2026-mean-field-green-aec]] had silent top-level parse metadata, so DOI/venue/year were verified through title-matched DOI metadata. Technical claims are grounded in the local parses; hardware evidence for [[ma-2026-mean-field-green-aec]] is recorded as hardware-in-the-loop emulation, not real UAV flight.

Validation results: `python tools/wiki/curation_status.py --dupes` reported 345 raw folders, 280 curated raw references, and 65 genuinely new folders still uncurated after this pass, plus 13 referenced-name/no-matching-raw-folder advisories. `python tools/wiki/corpus_counts.py` reported 292 sources, 284 concepts, 73 entities, 14 findings, 15 synthesis pages, 6 comparisons, 5 methodology pages, 5 queries, 3 theses, 2 reference pages, and 345 raw-source folders. `python tools/wiki/linkcheck.py --orphans`, `python tools/wiki/process_refs.py`, `python tools/wiki/index_audit.py`, `python tools/wiki/frontmatter_audit.py`, and `git diff --check` were clean. `python tools/wiki/entity_roster_audit.py` reported 0 claimed-but-absent over-claims and 38 advisory present-but-unlisted omissions, all outside the newly curated source authors. LLM Wiki health was OK; `/graph/current` returned `{"ok":false,"error":"Not found"}` rather than graph node/edge counts.

## [2026-07-07] Curated 5 deployment / RIS / terrain MEC sources

Added five source pages and three concept pages:

- [[ning-2023-uav-mec-offloading-deployment]] — Ning et al. 2023, *IEEE TMC*, DOI `10.1109/TMC.2021.3129785`. Dynamic UAV-MEC computation offloading and server deployment; UE offloading and UAV location selection are modeled as coupled stochastic games with probability-based learning and chess-like asynchronous updates.
- [[gong-2023-edge-intelligence-its-survey]] — Gong et al. 2023, *IEEE T-ITS*, DOI `10.1109/TITS.2023.3275741`. Edge intelligence for intelligent transportation systems; end-edge-cloud architecture, seven-level EI taxonomy, enabling technologies, autonomous-driving/VEC/UAV/rail applications, platforms, datasets, and open challenges.
- [[mohammadi-2026-star-ris-uav-mec-noma]] — Mohammadi et al. 2026, *IEEE TGCN*, DOI `10.1109/TGCN.2026.3694177`. STAR-RIS-assisted UAV-MEC with NOMA; weighted energy minimization over task-bit allocation, transmit power, STAR-RIS phase shifts, and UAV trajectory using BCD/SCA/MRT-style updates.
- [[liao-2025-ris-uav-usv-resource-allocation]] — Liao et al. 2025, *IEEE TGCN*, DOI `10.1109/TGCN.2025.3545458`. RIS-assisted UAV-USV cooperative MEC for inland waterways; bidirectional USV tasks with hard time windows, UAV route/arrival choices, hovering coordinates, and RIS phase design.
- [[tong-2026-uneven-terrain-uav-mec]] — Tong et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2026.3695882`. Uneven-terrain UAV-MEC with service coverage, partial UAV/BS task allocation, propulsion energy efficiency, and PH-DRL for safe 3D flight plus task-allocation control.

New concept pages: [[edge-intelligence]], [[star-ris]], and [[uav-usv-cooperative-mec]]. Updated concept backlinks for [[task-offloading]], [[uav-trajectory-control]], [[stochastic-game]], [[noma]], [[uav-mounted-ris]], [[intelligent-reflecting-surface]], [[maritime-mec]], [[terrain-aware-channel-model]], [[hierarchical-reinforcement-learning]], [[differential-evolution]], and [[alternating-optimization-sdr-sca]]. No author entity pages were created; the parse-confirmed source authors were not merged into existing author entities.

Metadata notes: DOI/venue/year for all five source pages were verified through title-matched DOI metadata where the parse was silent or incomplete. Technical claims are grounded in the local parses; figure-derived numeric comparisons are phrased as parse-reported results rather than independent measurements.

Validation results: `python tools/wiki/curation_status.py --dupes` reported 345 raw folders, 275 curated raw references, and 70 genuinely new folders still uncurated after this pass, plus 13 referenced-name/no-matching-raw-folder advisories. `python tools/wiki/corpus_counts.py` reported 287 sources, 282 concepts, 73 entities, 14 findings, 15 synthesis pages, 6 comparisons, 5 methodology pages, 5 queries, 3 theses, 2 reference pages, and 345 raw-source folders. `python tools/wiki/linkcheck.py --orphans`, `python tools/wiki/process_refs.py`, `python tools/wiki/index_audit.py`, `python tools/wiki/frontmatter_audit.py`, and `git diff --check` were clean. `python tools/wiki/entity_roster_audit.py` reported 0 claimed-but-absent over-claims and 38 advisory present-but-unlisted omissions, all outside the newly curated source authors. LLM Wiki health was OK; `/graph/current` returned `{"ok":false,"error":"Not found"}` rather than graph node/edge counts.

## [2026-07-06] Curated 5 digital-twin / robust / aerial-VEC sources

Added five source pages and two concept pages:

- [[he-2026-dt-sagimec-lae]] — He et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2025.3623636`. DT-assisted SAGIMEC for low-altitude economy; ISD/UAV/LEO/cloud architecture, Lyapunov per-slot control, satellite-latency learning, and Stackelberg-game decentralized decisions.
- [[li-2025-dt-uav-swarm-resource-management]] — Li et al. 2025, *IEEE T-ITS*, DOI `10.1109/TITS.2025.3531120`. Digital-twin-based task-driven UAV-swarm resource management for search and rescue; MADRL task crowdsourcing plus stochastic-network-calculus traffic-flow delay bounds.
- [[li-2026-cdto-inland-waterways]] — Li et al. 2026, *IEEE T-ITS*, DOI `10.1109/TITS.2026.3683451`. UAV-assisted inland-waterway edge offloading; USV D2D computation-sharing clusters, UAV cluster-head positioning, exact-potential-game CDTO, and graph-based MARL.
- [[jia-2026-dro-lawn-trajectory]] — Jia et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2026.3688525`. Distributionally robust task-size offloading and UAV-trajectory optimization in a UAV/HAP low-altitude wireless network; L1/L-infinity/Fortet-Mourier ambiguity sets plus Benders/SCA.
- [[zhang-2026-dwell-time-aerial-vec]] — Zhang et al. 2026, *IEEE T-ITS*, DOI `10.1109/TITS.2026.3692669`. Multi-layer aerial VEC with UAV/HAP service and a dwell-time feasibility constraint for high-speed vehicles; weighted latency+economic cost minimized via BCD/Lagrangian/ADMM-style allocation.

New concept pages: [[stochastic-network-calculus]] and [[dwell-time-constrained-offloading]]. Updated concept backlinks for [[digital-twin]], [[distributionally-robust-optimization]], [[potential-game]], [[graph-neural-network]], [[device-to-device-communication]], [[vehicular-mec]], [[maritime-mec]], [[space-air-ground-integrated-network]], [[low-altitude-intelligent-network]], [[high-altitude-platform-station]], [[alternating-direction-method-of-multipliers]], [[lyapunov-optimization]], [[stackelberg-game]], and [[multi-uav-assisted-mec]]. Updated recurring author entities where the parse supported the identity: [[geng-sun]], [[zemin-sun]], [[jiacheng-wang]], [[dusit-niyato]], [[victor-c-m-leung]], [[ziye-jia]], [[qihui-wu]], and [[zhu-han]]. No new author entity pages were created for names not already confirmed in the wiki.

Metadata notes: [[he-2026-dt-sagimec-lae]] includes a parse DOI and Crossref-confirmed TMC issue/page metadata. [[li-2025-dt-uav-swarm-resource-management]], [[li-2026-cdto-inland-waterways]], and [[zhang-2026-dwell-time-aerial-vec]] used Crossref title/DOI lookup where the parse was silent or incomplete. [[jia-2026-dro-lawn-trajectory]] used DOI/IEEE metadata lookup because the parse lacked venue/DOI lines. Technical claims on all five pages are grounded in the local parses.

Validation results: `python tools/wiki/curation_status.py --dupes` reported 345 raw folders, 270 curated raw references, and 75 genuinely new folders still uncurated after this pass, plus 13 referenced-name/no-matching-raw-folder advisories. `python tools/wiki/corpus_counts.py` reported 282 sources, 279 concepts, 73 entities, 14 findings, 15 synthesis pages, 6 comparisons, 5 methodology pages, 5 queries, 3 theses, 2 reference pages, and 345 raw-source folders. `python tools/wiki/linkcheck.py --orphans`, `python tools/wiki/process_refs.py`, `python tools/wiki/index_audit.py`, and `python tools/wiki/frontmatter_audit.py` were clean. `python tools/wiki/entity_roster_audit.py` reported 0 claimed-but-absent over-claims and 38 advisory present-but-unlisted omissions, all outside the newly curated author rosters. LLM Wiki health was OK; `/graph/current` returned `{"ok":false,"error":"Not found"}` rather than graph node/edge counts.

## [2026-07-06] Curated 5 semantic / SAGIN / demand-aware MEC sources

Added five source pages and one concept page:

- [[wang-2026-lifelong-semantic-content-reuse]] — Wang et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2026.3664868`. Semantic-aware content reuse for UAV-assisted Metaverse services; DC-ELLA combines lifelong multi-task learning with semantic / location-aware reuse decisions.
- [[zhou-2021-delay-sagin-task-scheduling]] — Zhou et al. 2021, *IEEE TWC*, DOI `10.1109/TWC.2020.3029143`. Delay-oriented IoT task scheduling in space-air-ground integrated networks; DOTS uses risk-sensitive deep reinforcement learning over local, UAV, satellite, and cloud execution choices.
- [[zhai-2026-collaborative-inference-uav-mec]] — Zhai et al. 2026, *IEEE T-ITS*, DOI `10.1109/TITS.2025.3629117`. Collaborative DNN inference in UAV-assisted MEC; DPDTS separates DNN partitioning, task-server matching, and TD3 UAV trajectory control.
- [[peng-2026-demand-aware-multiuav-mec]] — Peng et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2026.3697839`. Demand-aware multi-area multi-UAV MEC; cooperative segmented regional retrieval supplies Pareto solutions for energy-delay tradeoffs under dynamic area demand.
- [[wang-2026-diffusion-semantic-uav-edge]] — Wang et al. 2026, *IEEE TWC*, DOI `10.1109/TWC.2026.3657387`. UAV-assisted semantic edge computing; H-DDPG and H-D3PG optimize semantic compression, offloading, and UAV trajectory under semantic-relevance constraints.

New concept page: [[semantic-content-reuse]]. Updated concept backlinks for [[semantic-communication]], [[diffusion-model-as-optimizer]], [[collaborative-dl-inference]], [[dnn-model-partition]], [[constrained-multi-objective-evolutionary-algorithm]], and [[safe-reinforcement-learning]]. Updated recurring author entities where the parse supported the identity: [[chaoda-peng]], [[xumin-huang]], [[yuan-wu]], [[dusit-niyato]], [[zhu-han]], [[xuemin-shen]], and [[chao-dong]]. [[zexiong-wu]] remains an advisory roster omission for [[peng-2026-demand-aware-multiuav-mec]] because that parse gives the author name but no affiliation or biography to confirm same-person identity.

Validation results: `python tools/wiki/curation_status.py --dupes` reported 345 raw folders, 265 curated raw references, and 80 genuinely new folders still uncurated after this pass. `python tools/wiki/corpus_counts.py` reported 277 sources, 277 concepts, 73 entities, 14 findings, 15 synthesis pages, 6 comparisons, 5 methodology pages, 5 queries, 3 theses, 2 reference pages, and 345 raw-source folders. `python tools/wiki/entity_roster_audit.py` reported 0 claimed-but-absent over-claims and 38 advisory present-but-unlisted omissions; the new unresolved advisory omission is [[zexiong-wu]] for [[peng-2026-demand-aware-multiuav-mec]]. LLM Wiki health was OK; the previously used graph probes returned `{"ok":false,"error":"Not found"}` rather than node/edge counts.

## [2026-07-06] Curated 5 game / satellite / green-UAV sources

Added five source pages and two concept pages:

- [[zhang-2026-uav-task-path-lu-its]] — Zhang et al. 2026, *IEEE T-ITS*, DOI `10.1109/TITS.2026.3667967`. Cooperative multi-UAV task allocation and collision-free path planning for low-altitude urban intelligent transportation systems; ILLA potential-game allocation plus CBMBA A-Star path search.
- [[huang-2026-amappo-satellite-edge]] — Huang et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2025.3645456`. Cost-aware dependent-task offloading for UAV-assisted satellite edge computing; direct IoTD-to-LEO in spacious regions, UAV relay in obstructive regions, MATS DAG sequencing, and asynchronous GNN-augmented MAPPO.
- [[panahi-2026-uav-green-iot-offloading]] — Panahi & Panahi 2026, *IEEE TGCN*, DOI `10.1109/TGCN.2025.3580453`. Cost-aware green-IoT UAV offloading with Q-learning region trajectory, laser / renewable energy procurement, and COF/WPT service-compensation accounting.
- [[chen-2026-dart-hap-uav-mec]] — Chen et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2026.3676417`. HAP-UAV-MEC with NOMA and WPT; DART combines Lyapunov decomposition, DDPG-attention trajectory/offloading, and convex resource allocation.
- [[jia-2026-ufsp-rail-inspection]] — Jia et al. 2026, *IEEE T-ITS*, DOI `10.1109/TITS.2026.3695610`. Multi-UAV rail-line inspection under imperfect information; stochastic potential game plus U-FSP belief-augmented Q-learning / policy averaging, with small-scale real-world deployment evidence.

New concept pages: [[fictitious-self-play]] and [[energy-procurement-compensation]]. Updated ying-chen after the DART parse confirmed the same Beijing Information Science and Technology University identity. Metadata notes: DOI/venue/year for all five papers were verified with Crossref/DOI lookup where the parse was silent or incomplete; technical claims are grounded in the local parses.

Validation results: `python tools/wiki/curation_status.py --dupes` reported 345 raw folders, 260 curated raw references, and 85 genuinely new folders still uncurated after this pass. `python tools/wiki/corpus_counts.py` reported 272 sources, 276 concepts, 73 entities, 14 findings, 15 synthesis pages, 6 comparisons, 5 methodology pages, 5 queries, 3 theses, 2 reference pages, and 345 raw-source folders. `python tools/wiki/linkcheck.py --orphans`, `python tools/wiki/process_refs.py`, `python tools/wiki/index_audit.py`, `python tools/wiki/frontmatter_audit.py`, and `git diff --check` were clean; `python tools/wiki/entity_roster_audit.py` reported 0 claimed-but-absent over-claims and 37 advisory present-but-unlisted omissions. LLM Wiki API health was OK; graph probe reported 669 nodes and 6264 edges.

## [2026-07-06] Curated 5 low-altitude / UAV-MEC sources

Added five source pages and two concept pages:

- [[chen-2026-cargo-uav-pickup-lae]] — Chen et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2025.3647000`. Cellular-connected cargo-UAV pickup for LAE; CACMO combines D3QN trajectory learning, simulated annealing sequence planning, and collision-aware refinement under communication, energy, and time-window constraints.
- [[huang-2026-coded-caching-uav-marine]] — Huang et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2026.3708365`. Coded caching-enabled D2D content delivery in UAV-assisted marine edge networks; OJC3D uses Lyapunov online optimization over UAV trajectory, caching placement, and request decisions.
- [[zhou-2026-cpsfl-uav-foundation-models]] — Zhou et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2026.3697889`. Communication-pipelined split federated LoRA fine-tuning for UAV foundation models; sequential downlink gradient transmission plus attention-based DRL split/resource decisions.
- [[qi-2026-drone-vehicle-mec-inspection]] — Qi et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2026.3698194`. Cooperative drone-vehicle MEC for low-altitude inspection; route planning, battery swapping, detached-drone in-flight processing, and speed optimization minimize mission completion time.
- [[tang-2025-cooperative-isac-lae]] — Tang et al. 2025, *IEEE TWC*, DOI `10.1109/TWC.2025.3542399`. Cooperative ISAC for LAE; tensor-decomposition monostatic estimation plus MST association, Pareto position fusion, and residual-weighted velocity estimation.

New concept pages: [[coded-caching]] and [[split-federated-learning]]. Updated existing author rosters for [[dusit-niyato]], [[jiawen-kang]], [[shengli-xie]], [[weifeng-zhong]], and [[xumin-huang]]. Metadata notes: DOI/venue/year for all five papers were verified with Crossref/DOI lookup where the parse was silent or incomplete; technical claims are grounded in the local parses.

Validation results: `python tools/wiki/curation_status.py --dupes` reported 345 raw folders, 255 curated raw references, and 90 genuinely new folders still uncurated after this pass. `python tools/wiki/corpus_counts.py` reported 267 sources, 274 concepts, 73 entities, 14 findings, 15 synthesis pages, 6 comparisons, 5 methodology pages, 5 queries, 3 theses, 2 reference pages, and 345 raw-source folders. `python tools/wiki/linkcheck.py --orphans`, `python tools/wiki/process_refs.py`, `python tools/wiki/index_audit.py`, `python tools/wiki/frontmatter_audit.py`, and `git diff --check` were clean; `python tools/wiki/entity_roster_audit.py` reported 0 claimed-but-absent over-claims and 37 advisory present-but-unlisted omissions. LLM Wiki API health was OK; graph probe reported 662 nodes and 6176 edges.

## [2026-07-06] Curated 5 newly imported MEC sources

Added five source pages and one tool entity:

- [[liu-2026-lyapunov-diffusion-uav-vehicular]] — Liu et al. 2026, *IEEE TWC*, DOI `10.1109/TWC.2026.3680987`. Lyapunov-guided diffusion actor DDPG (D3PG) for UAV-assisted vehicular networks with delayed CSI feedback; joint V2V channel reuse, V2U/V2V power control, UAV altitude, and long-term UAV energy.
- [[xu-2026-prizty-uav-mec-auction]] — Xu et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2025.3609202`. Prizty privacy-preserving reverse auction for UAV-assisted MEC offloading/resource allocation; UE location obfuscation + trajectory-aware feasible service sets + winner/payment selection.
- [[li-2023-adaptive-digital-twin-uav-iscc]] — Li et al. 2023, *IEEE TGCN*, DOI `10.1109/TGCN.2023.3298039`. Adaptive digital twin for UAV-assisted ISCC; DT-aware CTDE with ATB-MAPPO (Beta-policy actors + attention critics) balancing radar beampattern and weighted energy.
- [[shi-2026-aoi-active-ris-noma-agmec]] — Shi et al. 2026, *IEEE TWC*, DOI `10.1109/TWC.2026.3686114`. AoI-aware active-RIS and NOMA-assisted air-ground MEC; joint UAV trajectory, active-RIS beamforming, and task offloading via AADDPG.
- [[wei-2026-airfogsim-uav-vfc]] — Wei et al. 2026, *IEEE TMC*, DOI `10.1109/TMC.2025.3641373`. AirFogSim lightweight modular simulator for UAV-integrated vehicular fog computing; added [[airfogsim]] as a tool entity.

Metadata notes: DOI/venue/year for the two TWC papers came from parse DOI/date lines and Crossref DOI lookup. The privacy-auction, digital-twin, and AirFogSim pages had missing DOI/year/venue in the parses, so Crossref title/DOI lookup supplied publication metadata; all technical claims came from the local parses. Updated backlinks in [[diffusion-model-as-optimizer]], [[reverse-auction-incentive]], [[digital-twin]], [[age-of-information]], [[active-ris]], [[vehicle-fog-computing]], and recurring author entities [[dusit-niyato]], [[xuemin-shen]], and [[ning-zhang]].

Validation results: `python tools/wiki/curation_status.py --dupes` reported 345 raw folders, 250 curated raw references, and 95 genuinely new folders still uncurated after this five-source pass. `python tools/wiki/corpus_counts.py`, `python tools/wiki/linkcheck.py --orphans`, `python tools/wiki/process_refs.py`, `python tools/wiki/index_audit.py`, `python tools/wiki/frontmatter_audit.py`, and `git diff --check` were run before commit; the file-level graph has no dangling links, no process-narration leaks outside this log, complete index coverage with zero duplicate primary listings, and zero frontmatter errors. LLM Wiki health was reachable with unauthenticated read access; the read-only graph API for `current` reported 655 nodes and 6098 edges.

## 2026-06-09 - Audit concept pages: batch 18 slice E

- Audited these five concept pages only: [[binary-vs-partial-offloading]], [[binary-whale-optimization]], [[blockage-aware-channel-model]], [[blockchain-for-fl-aggregation]], and [[byzantine-fault-tolerant-consensus]]. Verified frontmatter shape, H1/title consistency, tags, related links, absence of self-references, dangling-link status, evergreen wording, and source-grounded claims against linked local wiki evidence and targeted raw parses where a source-specific claim needed grounding.
- Content-page fixes: [[binary-whale-optimization]] now matches the parse-grounded [[jia-2025-dro-uav-hap-mec]] baseline list: exhaustive search, greedy offloading, and simulated annealing. [[binary-vs-partial-offloading]], [[blockage-aware-channel-model]], [[blockchain-for-fl-aggregation]], and [[byzantine-fault-tolerant-consensus]] were already grounded and consistent.
- Validation results: `python tools/wiki/curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers, with 1 referenced-name mismatch entry (`Untouched primary documents (PDFs, parsed markdown, images`) that did not indicate an uncurated paper. `python tools/wiki/process_refs.py`, `python tools/wiki/linkcheck.py --orphans`, `python tools/wiki/index_audit.py`, `python tools/wiki/frontmatter_audit.py --type concept`, and `git diff --check` were run before commit.
- LLM Wiki health endpoint was reachable with unauthenticated read access; the read-only graph API for `current` was reachable and reported 649 nodes and 6008 edges.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded concept-page audit.

## 2026-06-09 - Audit concept pages: batch 18 slice D

- Audited these five concept pages only: [[b-spline-trajectory]], [[backscatter-communication]], [[bang-bang-control]], [[bargaining-game]], and [[beta-policy-drl]]. Verified frontmatter shape, H1/title consistency, tags, related links, absence of self-references, dangling-link status, evergreen wording, and source-grounded claims against linked local wiki evidence and targeted raw parses where a source-specific claim needed grounding.
- Content-page fixes: [[b-spline-trajectory]] now avoids an over-specific continuity claim not stated in the linked local evidence, while retaining the parse-grounded control-point and low-dimensional B-spline trajectory framing. [[backscatter-communication]], [[bang-bang-control]], [[bargaining-game]], and [[beta-policy-drl]] were already grounded and consistent.
- Validation results: `python tools/wiki/curation_status.py --dupes` was run as the no-new-papers guard. `python tools/wiki/process_refs.py`, `python tools/wiki/linkcheck.py --orphans`, `python tools/wiki/index_audit.py`, `python tools/wiki/frontmatter_audit.py --type concept`, and `git diff --check` were run before commit.
- LLM Wiki health endpoint was reachable with unauthenticated read access; the read-only graph API for `current` was reachable and reported 649 nodes and 6008 edges.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded concept-page audit.

## 2026-06-09 - Audit concept pages: batch 18 slice C

- Audited these five concept pages only: [[alternating-optimization-sdr-sca]], [[ant-colony-optimization]], [[ant-lion-optimizer]], [[anti-jamming-mec]], and [[aoi-energy-tradeoff]]. Verified frontmatter shape, H1/title consistency, tags, related links, absence of self-references, dangling-link status, evergreen wording, and source-grounded claims against linked local wiki evidence.
- Content-page fixes: none. All five audited concept pages were already grounded and consistent.
- Validation results: `python tools/wiki/curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers, with 1 referenced-name mismatch entry (`Untouched primary documents (PDFs, parsed markdown, images`) that did not indicate an uncurated paper. `python tools/wiki/process_refs.py`, `python tools/wiki/linkcheck.py --orphans`, `python tools/wiki/index_audit.py`, `python tools/wiki/frontmatter_audit.py --type concept`, and `git diff --check` were run before commit.
- LLM Wiki health endpoint was reachable with unauthenticated read access; the read-only graph API for `current` was reachable and reported 649 nodes and 6008 edges.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded concept-page audit.

## 2026-06-09 - Audit concept pages: batch 18 slice B

- Audited these five concept pages only: [[age-of-information]], [[aigc-service-provider]], [[air-ground-integrated-network]], [[air-to-ground-channel-model]], and [[alternating-direction-method-of-multipliers]]. Verified frontmatter shape, H1/title consistency, tags, related links, absence of self-references, dangling-link status, evergreen wording, and source-grounded claims against linked local wiki evidence.
- Content-page fixes: [[air-ground-integrated-network]] now includes the body-linked [[mao-2025-bcsa-frl]] source in `related:` for frontmatter/body consistency. [[age-of-information]], [[aigc-service-provider]], [[air-to-ground-channel-model]], and [[alternating-direction-method-of-multipliers]] were already grounded and consistent.
- Validation results: `python tools/wiki/curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers, with 1 referenced-name mismatch entry (`Untouched primary documents (PDFs, parsed markdown, images`) that did not indicate an uncurated paper. `python tools/wiki/process_refs.py`, `python tools/wiki/linkcheck.py --orphans`, `python tools/wiki/index_audit.py`, `python tools/wiki/frontmatter_audit.py --type concept`, and `git diff --check` were run before commit.
- LLM Wiki health endpoint was reachable with unauthenticated read access; the read-only graph API for `current` was reachable and reported 649 nodes and 6008 edges.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded concept-page audit.

## 2026-06-09 - Audit concept pages: batch 18 slice A

- Audited these five concept pages only: [[action-space-explosion-in-multi-uav-mec]], [[active-ris]], [[adaptive-entropy-priority-replay]], [[adaptive-inter-layer-data-offloading]], and [[adaptive-intermediate-data-compression]]. Verified frontmatter shape, H1/title consistency, tags, related links, absence of self-references, dangling-link status, evergreen wording, and source-grounded claims against linked local wiki evidence.
- Content-page fixes: none. All five audited concept pages were already grounded and consistent. Spot-checks confirmed [[active-ris]] against [[sun-2024-active-passive-ris-receiver]], [[adaptive-entropy-priority-replay]] against [[peng-2025-drudm-cfg]], [[adaptive-inter-layer-data-offloading]] against [[han-2024-sagin-fl-handover]], and [[adaptive-intermediate-data-compression]] against [[sun-2024-asap-uav-swarm]].
- Validation results: `python tools/wiki/curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers, with 1 referenced-name mismatch entry (`Untouched primary documents (PDFs, parsed markdown, images`) that did not indicate an uncurated paper. `python tools/wiki/frontmatter_audit.py --type concept` was supported and reported 272 concept pages checked with 0 errors. `python tools/wiki/process_refs.py`, `python tools/wiki/linkcheck.py --orphans`, and `python tools/wiki/index_audit.py` were clean before commit.
- LLM Wiki health endpoint was reachable with unauthenticated read access; the read-only graph API was reachable and reported 649 nodes and 6008 edges.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded concept-page audit.

## 2026-06-09 - Audit source pages: batch 17 slice D

- Audited these two source pages only: [[zhu-2024-zdrl-uav-tracking]] and [[zhu-2025-lycnn-drl-wpt-mec]]. Verified title / authors / year / venue / DOI, key numeric claims, method and system-model claims, related-link sanity, evergreen wording, frontmatter, and raw artifact pointers against the linked parses.
- Content-page fixes: both source pages were already substantively grounded. Corrected mojibake artifacts in parse-grounded prose (`->`, active-target-passive, passive-BS, ranges, `>=`, `~250x`), and aligned [[zhu-2025-lycnn-drl-wpt-mec]]'s H1 with its full frontmatter title. No related-link or index reconciliation was required.
- Validation results: `python tools/wiki/curation_status.py --dupes`, `python tools/wiki/process_refs.py`, `python tools/wiki/linkcheck.py --orphans`, `python tools/wiki/frontmatter_audit.py --type source`, and `git diff --check` were run before commit.
- LLM Wiki health endpoint was reachable with unauthenticated read access; the read-only graph API reported 649 nodes and 6008 edges.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded source-page audit.

## 2026-06-09 - Audit source pages: batch 17 slice C

- Audited these five source pages only: [[zhou-2018-uav-wireless-powered-mec]], [[zhou-2024-jdl-abs-postdisaster-rescue]], [[zhou-2024-mco-satellite-edge-offloading]], [[zhu-2024-crb-active-ris-isac]], and [[zhu-2024-sensing-comm-doppler-uav-swarm]]. Verified title / authors / year / venue / DOI where present, key numeric claims, method and system-model claims, related-link sanity, evergreen wording, frontmatter, and raw artifact pointers against the linked parses.
- Content-page fixes: [[zhou-2018-uav-wireless-powered-mec]] now records the parse-stated multiple-antenna future-work direction. [[zhou-2024-mco-satellite-edge-offloading]] now records the parse-stated future-work directions on inter-task dependencies, resource-allocation optimization, GEO-satellite collaboration, and distributed-algorithm latency. [[zhu-2024-sensing-comm-doppler-uav-swarm]] now records the parse-stated follow-up direction on resource utilization and energy efficiency. [[zhou-2024-jdl-abs-postdisaster-rescue]] and [[zhu-2024-crb-active-ris-isac]] were already grounded and needed no content-page edits.
- Verification scope: `python tools/wiki/curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers, with 1 referenced-name mismatch entry (`Untouched primary documents (PDFs, parsed markdown, images`) that did not indicate an uncurated paper. The remaining gates were run before commit.
- LLM Wiki health endpoint was reachable with unauthenticated read access; the read-only graph API reported 649 nodes and 6008 edges.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded source-page audit.

## 2026-06-09 - Audit source pages: batch 17 slice B

- Audited these five source pages only: [[zhao-2024-caching-service-placement-uav]], [[zhao-2025-gai-pls-survey]], [[zhao-2025-traj-offload-cache-migration]], [[zheng-2024-recmop-uav-cb]], and [[zheng-2024-semcom-sec-offloading]]. Verified title / authors / year / venue / DOI where present, key numeric claims, method and system-model claims, related-link sanity, evergreen wording, frontmatter, and raw artifact pointers against the linked parses.
- Content-page fixes: [[zhao-2025-traj-offload-cache-migration]] now uses ASCII range markers for the parse-grounded scheduling-cost and execution-time reductions in the key findings and records the original-PDF / figures raw-artifact note. [[zhao-2024-caching-service-placement-uav]], [[zhao-2025-gai-pls-survey]], [[zheng-2024-recmop-uav-cb]], and [[zheng-2024-semcom-sec-offloading]] were already grounded and needed no content-page edits.
- Verification scope: `python tools/wiki/curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers, with 1 referenced-name mismatch entry (`Untouched primary documents (PDFs, parsed markdown, images`) that did not indicate an uncurated paper. The remaining gates were run before commit.
- LLM Wiki health endpoint was reachable with unauthenticated read access; the read-only graph API reported 649 nodes and 6008 edges.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded source-page audit.

## 2026-06-09 - Audit source pages: batch 17 slice A

- Audited these five source pages only: [[zhang-2025-three-tier-maritime-offloading]], [[zhang-2025-vnf-sgin-dql]], [[zhao-2018-caching-uav-ia-secure]], [[zhao-2019-uav-emergency-disasters]], and [[zhao-2022-matd3-multiuav-ec-offloading]]. Verified title / authors / year / venue / DOI where present, key numeric claims, method and system-model claims, related-link sanity, evergreen wording, frontmatter, and raw artifact pointers against the linked parses.
- Content-page fixes: [[zhang-2025-vnf-sgin-dql]] now records the parse-stated earth-station deployment future-work direction. [[zhao-2018-caching-uav-ia-secure]] now records the parse-stated CSI estimation and feedback future-work direction. [[zhao-2019-uav-emergency-disasters]] now uses `not in parse` for venue, volume/issue, and pages instead of retaining externally confirmed bibliographic details not present in the raw parse. [[zhang-2025-three-tier-maritime-offloading]] and [[zhao-2022-matd3-multiuav-ec-offloading]] were already grounded and needed no content-page edits.
- Verification scope: `python tools/wiki/curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers, with 1 referenced-name mismatch entry (`Untouched primary documents (PDFs, parsed markdown, images`) that did not indicate an uncurated paper. The remaining gates were run before commit.
- LLM Wiki health endpoint was reachable with unauthenticated read access; the read-only graph API reported 649 nodes and 6008 edges.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded source-page audit.

## 2026-06-09 - Audit source pages: batch 16 slice D

- Audited these five source pages only: [[zhang-2024-uav-task-offloading-ddpg]], [[zhang-2025-gan-td3-isac-active-ris]], [[zhang-2025-gsc-diffusion-semcom]], [[zhang-2025-mcma-task-migration]], and [[zhang-2025-ssac-mgi-heterogeneous-uav]]. Verified title / authors / year / venue / DOI where present, key numeric claims, method and system-model claims, related-link sanity, evergreen wording, frontmatter, and raw artifact pointers against the linked parses.
- Content-page fixes: [[zhang-2025-gan-td3-isac-active-ris]] now states the parse-grounded GAN-TD3 trade-off: better performance and stability, but higher computational complexity and slower convergence speed. [[zhang-2025-ssac-mgi-heterogeneous-uav]] now avoids treating a fixed-service-capability inference as an explicit limitation and says live re-provisioning is not discussed in the parse. [[zhang-2024-uav-task-offloading-ddpg]], [[zhang-2025-gsc-diffusion-semcom]], and [[zhang-2025-mcma-task-migration]] were already grounded and needed no content-page edits.
- Verification scope: `python tools/wiki/curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers, with 1 referenced-name mismatch entry (`Untouched primary documents (PDFs, parsed markdown, images`) that did not indicate an uncurated paper. The remaining gates were run before commit.
- LLM Wiki health endpoint was reachable with unauthenticated read access; the read-only graph API reported 649 nodes and 6008 edges.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded source-page audit.

## 2026-06-09 - Audit source pages: batch 16 slice C

- Audited these five source pages only: [[zhang-2024-coma-satellite-offloading]], [[zhang-2024-dlrl-maritime-usv]], [[zhang-2024-gdmtd3-aerial-secure-cb]], [[zhang-2024-mhspo-satellite-peer-offloading]], and [[zhang-2024-qos-vne-sagoin]]. Verified title / authors / year / venue / DOI where present, key numeric claims, method and system-model claims, related-link sanity, evergreen wording, frontmatter, and raw artifact pointers against the linked parses.
- Content-page fixes: none. All five audited source pages were already grounded in their linked raw parses and needed no content-page edits.
- Verification scope: the LLM Wiki health endpoint was reachable with unauthenticated read access; the read-only graph API reported 649 nodes and 6008 edges. The required validation gates were run before commit.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded source-page audit.

## 2026-06-09 - Audit source pages: batch 16 slice B

- Audited these five source pages only: [[zhang-2013-energy-optimal-mcc-stochastic]], [[zhang-2019-stochastic-offloading-uav-mec]], [[zhang-2019-uav-iot-comp-comm]], [[zhang-2020-response-delay-uav-swarm]], and [[zhang-2023-three-tier-satellite-offloading]]. Verified title / authors / year / venue / DOI where present, key numeric claims, method and system-model claims, related-link sanity, evergreen wording, frontmatter, and raw artifact pointers against the linked parses.
- Content-page fixes: [[zhang-2020-response-delay-uav-swarm]] now links the existing [[zhu-han]] entity in `related:` and in its relation-to-corpus note. [[zhang-2013-energy-optimal-mcc-stochastic]], [[zhang-2019-stochastic-offloading-uav-mec]], [[zhang-2019-uav-iot-comp-comm]], and [[zhang-2023-three-tier-satellite-offloading]] were already grounded and needed no content-page edits.
- Verification scope: `python tools/wiki/curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers, with 1 referenced-name mismatch entry (`Untouched primary documents (PDFs, parsed markdown, images`) that did not indicate an uncurated paper. The remaining gates were run before commit.
- LLM Wiki health endpoint was reachable with unauthenticated read access; the read-only graph API reported 649 nodes and 6008 edges.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded source-page audit.

## 2026-06-09 - Audit source pages: batch 16 slice A

- Audited these five source pages only: [[zeng-2024-usv-fleet-collaborative-offloading]], [[zhai-2023-fedleo-decentralized-fl]], [[zhan-2011-uav-relay-heading-optimization]], [[zhan-2018-uav-wsn-data-collection]], and [[zhan-2020-completion-time-energy-uav-mec]]. Verified title / authors / year / venue / DOI where present, key numeric claims, method and system-model claims, related-link sanity, evergreen wording, frontmatter, and raw artifact pointers against the linked parses.
- Content-page fixes: [[zeng-2024-usv-fleet-collaborative-offloading]] now links the existing [[zhou-su]] entity in `related:` and records the parse-stated future-work direction on joint caching, communication, and computation allocation. [[zhan-2018-uav-wsn-data-collection]] now links the existing [[yong-zeng]] entity in `related:` and records the parse-stated multi-UAV / UAV-sensor association / co-channel-interference future-work direction. [[zhai-2023-fedleo-decentralized-fl]], [[zhan-2011-uav-relay-heading-optimization]], and [[zhan-2020-completion-time-energy-uav-mec]] were already grounded and needed no content-page edits.
- Verification scope: `python tools/wiki/curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers, with 1 referenced-name mismatch entry (`Untouched primary documents (PDFs, parsed markdown, images`) that did not indicate an uncurated paper. The remaining gates were run before commit.
- LLM Wiki health endpoint was reachable with unauthenticated read access; the read-only graph API reported 649 nodes and 6007 edges.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded source-page audit.

## 2026-06-09 - Audit source pages: batch 15 slice D

- Audited these five source pages only: [[zeng-2016-throughput-relaying]], [[zeng-2016-uav-comm-opportunities-challenges]], [[zeng-2017-energy-efficient-uav-trajectory]], [[zeng-2019-rotary-wing-energy-min]], and [[zeng-2019-uav-comm-tutorial-5g]]. Verified title / authors / year / venue / DOI where present, key numeric claims, method and system-model claims, related-link sanity, evergreen wording, frontmatter, and raw artifact pointers against the linked parses.
- Content-page fixes: [[zeng-2017-energy-efficient-uav-trajectory]], [[zeng-2019-rotary-wing-energy-min]], and [[zeng-2019-uav-comm-tutorial-5g]] now include the existing [[yong-zeng]] entity link in `related:` for consistency with their Zeng-authored source pages. [[zeng-2016-throughput-relaying]] and [[zeng-2016-uav-comm-opportunities-challenges]] were already grounded and needed no content-page edits.
- Verification scope: `python tools/wiki/curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers, with 1 referenced-name mismatch entry (`Untouched primary documents (PDFs, parsed markdown, images`) that did not indicate an uncurated paper. The remaining gates were run before commit.
- LLM Wiki health endpoint was reachable with unauthenticated read access; the read-only graph API reported 649 nodes and 6007 edges.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded source-page audit.

## 2026-06-09 - Audit source pages: batch 15 slice C

- Audited these five source pages only: [[ye-2021-ran-slicing-offloading]], [[ye-2025-aigc-diffusion-contract]], [[you-2017-meco-resource-allocation]], [[you-2025-uncertain-maritime-hasac]], and [[yu-2020-uav-ec-collaborative-offloading]]. Verified title / authors / year / venue / DOI where present, key numeric claims, method and system-model claims, related-link sanity, evergreen wording, frontmatter, and raw artifact pointers against the linked parses.
- Content-page fixes: [[ye-2025-aigc-diffusion-contract]] now includes the parse-grounded citation section with DOI and publication timeline. [[ye-2021-ran-slicing-offloading]], [[you-2017-meco-resource-allocation]], [[you-2025-uncertain-maritime-hasac]], and [[yu-2020-uav-ec-collaborative-offloading]] were already grounded and needed no content-page edits.
- Verification scope: `python tools/wiki/curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers, with 1 referenced-name mismatch entry (`Untouched primary documents (PDFs, parsed markdown, images`) that did not indicate an uncurated paper. The remaining gates were run before commit.
- LLM Wiki health endpoint was reachable with unauthenticated read access; the read-only graph API reported 649 nodes and 6007 edges.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded source-page audit.

## 2026-06-09 - Audit source pages: batch 15 slice B

- Audited these five source pages only: [[yang-2019-sum-power-uav-mec]], [[yang-2020-loadbalance-multiuav-iot]], [[yang-2022-stochastic-uav-mec-lyapunov]], [[yang-2024-taco-human-digital-twin-edge]], and [[yao-2025-secure-isac-dual-eavesdropping]]. Verified title / authors / year / venue / DOI where present, key numeric claims, method and system-model claims, related-link sanity, evergreen wording, frontmatter, and raw artifact pointers against the linked parses.
- Content-page fixes: [[yang-2019-sum-power-uav-mec]] now records the parse-stated future-work direction (UAV-enabled MEC networks where UAVs are served as UEs) instead of `not in parse`, and its citation note avoids process-style arrow wording. [[yang-2020-loadbalance-multiuav-iot]] now uses the same evergreen citation / `not in parse` punctuation style. [[yang-2022-stochastic-uav-mec-lyapunov]], [[yang-2024-taco-human-digital-twin-edge]], and [[yao-2025-secure-isac-dual-eavesdropping]] were already grounded and needed no content-page edits.
- Verification scope: `python tools/wiki/curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers, with 1 referenced-name mismatch entry (`Untouched primary documents (PDFs, parsed markdown, images`) that did not indicate an uncurated paper. The remaining gates were run before commit.
- LLM Wiki health endpoint was reachable with unauthenticated read access; the read-only graph API reported 649 nodes and 6007 edges.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded source-page audit.

## 2026-06-09 - Audit source pages: batch 15 slice A

- Audited these five source pages only: [[xie-2025-stin-delay-offloading]], [[xie-2026-uav-multisource-fusion]], [[xu-2018-uav-wpt-trajectory]], [[xu-2021-secure-uav-mec-dual-uav]], and [[xu-2024-mobile-aigc-survey]]. Verified title / authors / year / venue / DOI where present, key numeric claims, method and system-model claims, related-link sanity, evergreen wording, frontmatter, and raw artifact pointers against the linked parses.
- Content-page fixes: [[xie-2026-uav-multisource-fusion]] now has explicit Parse / Origin PDF / Figures raw-artifact bullets and grounded solver-family wording. [[xu-2018-uav-wpt-trajectory]] and [[xu-2021-secure-uav-mec-dual-uav]] now have explicit Parse / Origin PDF / Figures raw-artifact bullets. [[xie-2025-stin-delay-offloading]] and [[xu-2024-mobile-aigc-survey]] were already grounded and needed no content-page edits.
- Verification scope: `python tools/wiki/curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers, with 1 referenced-name mismatch entry (`Untouched primary documents (PDFs, parsed markdown, images`) that did not indicate an uncurated paper. The remaining gates were run before commit.
- LLM Wiki health endpoint was reachable with unauthenticated read access; the read-only graph API reported 649 nodes and 6007 edges.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded source-page audit.

## 2026-06-09 - Audit source pages: batch 14 slice D

- Audited these five source pages only: [[wu-2024-urllc-uav-mec-latency]], [[wu-2025-gai-ris-resource-management]], [[wu-2025-iopo-irs-uav-thz-mec]], [[wu-2026-terrain-aware-uav-mec]], and [[xiang-sac-mapless-robot-navigation]]. Verified title / authors / year / venue / DOI where present, key numeric claims, method and system-model claims, related-link sanity, evergreen wording, frontmatter, and raw artifact pointers against the linked parses.
- Content-page fixes: [[wu-2024-urllc-uav-mec-latency]], [[wu-2025-iopo-irs-uav-thz-mec]], and [[wu-2026-terrain-aware-uav-mec]] now use explicit original-PDF / figures raw-artifact notes. [[wu-2025-gai-ris-resource-management]] and [[xiang-sac-mapless-robot-navigation]] were already grounded and needed no content-page edits.
- Verification scope: `python tools/wiki/curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers, with 1 referenced-name mismatch entry (`Untouched primary documents (PDFs, parsed markdown, images`) that did not indicate an uncurated paper. The remaining gates were run before commit.
- LLM Wiki health endpoint was reachable with unauthenticated read access; the read-only graph API reported 649 nodes and 6007 edges.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded source-page audit.

## 2026-06-09 - Audit source pages: batch 14 slice C

- Audited these five source pages only: [[wang-gai-isac-physical-layer]], [[wen-2024-iscc-edge-ai]], [[wu-2018-multiuav-minrate-trajectory]], [[wu-2019-irs-joint-beamforming]], and [[wu-2024-satellite-maritime-spectrum-sharing]]. Verified title / authors / year / venue / DOI where present, key numeric claims, method and system-model claims, related-link sanity, evergreen wording, frontmatter, and raw artifact pointers against the linked parses.
- Content-page fixes: [[wu-2019-irs-joint-beamforming]] now uses the parse's AP/IRS notation (`M` AP antennas, `N` IRS elements), softens the massive-MIMO comparison to a simulation result, and replaces an overstated SDR-tightness sentence with the parse-grounded SDR/randomization plus alternating-optimization description. [[wang-gai-isac-physical-layer]], [[wen-2024-iscc-edge-ai]], [[wu-2018-multiuav-minrate-trajectory]], and [[wu-2024-satellite-maritime-spectrum-sharing]] were already grounded and needed no content-page edits.
- Index reconciliation: [[wu-2019-irs-joint-beamforming]] now describes the asymptotic gain in terms of the number of IRS elements and frames the massive-MIMO comparison as simulation-supported.
- Verification scope: `python tools/wiki/curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers, with 1 referenced-name mismatch entry (`Untouched primary documents (PDFs, parsed markdown, images`) that did not indicate an uncurated paper. The remaining gates were run before commit.
- LLM Wiki health endpoint was reachable with unauthenticated read access; the read-only graph API reported 649 nodes and 6007 edges.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded source-page audit.

## 2026-06-09 - Audit source pages: batch 14 slice B

- Audited these five source pages only: [[wang-2025-maddpg-lc-dynamic-trajectory]], [[wang-2025-sac-tma-mec-dc]], [[wang-2025-uav-swarm-stackelberg]], [[wang-2026-aerial-marine-msar]], and [[wang-acve-constraint-violation-cmop]]. Verified title / authors / year / venue / DOI where present, key numeric claims, method and system-model claims, related-link sanity, evergreen wording, frontmatter, and raw artifact pointers against the linked parses.
- Content-page fixes: [[wang-2025-uav-swarm-stackelberg]] now removes an over-narrow single-leader limitation and uses an explicit original-PDF / figures raw-artifact note. [[wang-2026-aerial-marine-msar]] now removes stale wiki-positioning wording and uses an explicit original-PDF / figures raw-artifact note. [[wang-2025-maddpg-lc-dynamic-trajectory]], [[wang-2025-sac-tma-mec-dc]], and [[wang-acve-constraint-violation-cmop]] were already grounded and needed no content-page edits.
- Index reconciliation: [[wang-acve-constraint-violation-cmop]] now has its index listing aligned with the source page's TEVC 2025 / DOI grounding note rather than the older `not in parse` summary.
- Verification scope: `python tools/wiki/curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers, with 1 referenced-name mismatch entry (`Untouched primary documents (PDFs, parsed markdown, images`) that did not indicate an uncurated paper. The remaining gates were run before commit.
- LLM Wiki health endpoint was reachable with unauthenticated read access; the read-only graph API reported 649 nodes and 6007 edges.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded source-page audit.

## 2026-06-09 - Audit source pages: batch 14 slice A

- Audited these five source pages only: [[wang-2025-acbft-uav-consensus]], [[wang-2025-airground-laser-mec]], [[wang-2025-ctmig-task-migration-uav]], [[wang-2025-double-edge-samin]], and [[wang-2025-lae-network-survey]]. Verified title / authors / year / venue / DOI where present, key numeric claims, method and system-model claims, related-link sanity, evergreen wording, frontmatter, and raw artifact pointers against the linked parses.
- Content-page fixes: [[wang-2025-ctmig-task-migration-uav]] now corrects the A2G-rate example to the parse-stated 14 Mbps to 2 Mbps over 300 to 325 meters, removes dated "relative to today" wording, and uses explicit Parse / Origin PDF / Figures raw-artifact bullets. [[wang-2025-lae-network-survey]] now uses explicit Parse / Origin PDF / Figures raw-artifact bullets. [[wang-2025-acbft-uav-consensus]], [[wang-2025-airground-laser-mec]], and [[wang-2025-double-edge-samin]] were already grounded and needed no content-page edits.
- Verification scope: `python tools/wiki/curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers, with 1 referenced-name mismatch entry (`Untouched primary documents (PDFs, parsed markdown, images`) that did not indicate an uncurated paper. The remaining gates were run before commit.
- LLM Wiki health endpoint was reachable with unauthenticated read access; the read-only graph API reported 649 nodes and 6007 edges.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded source-page audit.

## 2026-06-09 - Audit source pages: batch 13 slice D

- Audited these five source pages only: [[wang-2024-satellite-terrestrial-computing]], [[wang-2024-ttw-amd-localization]], [[wang-2024-twotier-satellite-marine]], [[wang-2024-wipe-gai]], and [[wang-2024-xl-mimo-tutorial]]. Verified title / authors / year / venue / DOI where present, key numeric claims, method and system-model claims, related-link sanity, evergreen wording, frontmatter, and raw artifact pointers against the linked parses.
- Content-page fixes: none. All five audited source pages were already grounded and needed no content-page edits.
- Verification scope: `python tools/wiki/curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers, with 1 referenced-name mismatch entry (`Untouched primary documents (PDFs, parsed markdown, images`) that did not indicate an uncurated paper. The remaining gates were run before commit.
- LLM Wiki health endpoint was reachable with unauthenticated read access; the read-only graph API reported 649 nodes and 6007 edges.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded source-page audit.

## 2026-06-09 - Audit source pages: batch 13 slice C

- Audited these five source pages only: [[wang-2022-cat-rat-fmec-trajectory]], [[wang-2024-blockchain-uav-mec-dpos]], [[wang-2024-hfrl-decentralized-navigation]], [[wang-2024-hybrid-oma-noma-sagin]], and [[wang-2024-maritime-eh-jcora]]. Verified title / authors / year / venue / DOI where present, key numeric claims, method and system-model claims, related-link sanity, evergreen wording, frontmatter, and raw artifact pointers against the linked parses.
- Content-page fixes: [[wang-2022-cat-rat-fmec-trajectory]] now states the parse-supported RAT-vs-CAT result without understating Section 7's RAT advantage; [[wang-2024-hfrl-decentralized-navigation]] now records the parse-stated future-work directions. [[wang-2024-blockchain-uav-mec-dpos]], [[wang-2024-hybrid-oma-noma-sagin]], and [[wang-2024-maritime-eh-jcora]] were already grounded and needed no content-page edits.
- Verification scope: `python tools/wiki/curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers, with 1 referenced-name mismatch entry (`Untouched primary documents (PDFs, parsed markdown, images`) that did not indicate an uncurated paper. The remaining gates were run before commit.
- LLM Wiki health endpoint was reachable with unauthenticated read access; the read-only graph API reported 649 nodes and 6007 edges.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded source-page audit.

## 2026-06-09 - Audit source pages: batch 13 slice B

- Audited these five source pages only: [[van-hasselt-2016-double-dqn]], [[wang-2016-partial-offloading-dvs]], [[wang-2018-wpt-mec-joint-offloading]], [[wang-2019-todetas-deployment-scheduling]], and [[wang-2021-maddpg-multiuav-trajectory]]. Verified title / authors / year / venue / DOI where present, key numeric claims, method and system-model claims, related-link sanity, evergreen wording, frontmatter, and raw artifact pointers against the linked parses.
- Content-page fixes: [[van-hasselt-2016-double-dqn]] now keeps its venue and citation strictly at `not in parse` rather than carrying web-confirmed AAAI narration in published prose; [[wang-2021-maddpg-multiuav-trajectory]] now records the parse-stated constrained-UAV-computing-resource / matching-algorithm future-work note. [[wang-2016-partial-offloading-dvs]], [[wang-2018-wpt-mec-joint-offloading]], and [[wang-2019-todetas-deployment-scheduling]] were already grounded and needed no content-page edits.
- Verification scope: `python tools/wiki/curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers, with 1 referenced-name mismatch entry (`Untouched primary documents (PDFs, parsed markdown, images`) that did not indicate an uncurated paper. The remaining gates were run before commit.
- LLM Wiki health endpoint was reachable with unauthenticated read access; the read-only graph API reported 649 nodes and 6007 edges.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded source-page audit.

## 2026-06-09 - Audit source pages: batch 13 slice A

- Audited these five source pages only: [[sun-2025-emoppo-vlh-aerial-cb]], [[sun-2025-tjcct-twotimescale-uav-mec]], [[tang-2021-cecls-hybrid-cloud-edge]], [[tang-2024-iscc-uav-feel]], and [[ullah-2026-mec-drl-ntn-survey]]. Verified title / authors / year / venue / DOI where present, key numeric claims, method and system-model claims, related-link sanity, evergreen wording, frontmatter, and raw artifact pointers against the linked parses.
- Content-page fixes: [[tang-2024-iscc-uav-feel]] now uses the parse-grounded 2025 publication/current-version year while retaining the DOI stem `TWC.2024.3523381`; its index listing was reconciled to Tang et al. 2025. The other four audited source pages were already grounded and needed no content-page edits.
- Verification scope: `python tools/wiki/curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers, with 1 referenced-name mismatch entry (`Untouched primary documents (PDFs, parsed markdown, images`) that did not indicate an uncurated paper. The remaining gates were run before commit.
- LLM Wiki health endpoint was reachable with unauthenticated read access; the read-only graph API reported 649 nodes and 6007 edges.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded source-page audit.

## 2026-06-09 - Audit source pages: batch 12 slice D

- Audited these five source pages only: [[spampinato-2025-uabs-v2x-3dqn-ilp]], [[sun-2024-imssa-uav-secure-cb]], [[sun-2024-mfris-semantic-antijamming]], [[sun-2024-mvtora-postdisaster-vfc]], and [[sun-2024-ues-video-analytics-disaster]]. Verified title / authors / year / venue / DOI where present, key numeric claims, method and system-model claims, related-link sanity, evergreen wording, frontmatter, and raw artifact pointers against the linked parses.
- Content-page fixes: all five pages now have audit-current `updated` dates and encoding-clean punctuation in the audited prose. [[spampinato-2025-uabs-v2x-3dqn-ilp]], [[sun-2024-mvtora-postdisaster-vfc]], and [[sun-2024-ues-video-analytics-disaster]] now include explicit original-PDF filenames in Raw artifacts. [[sun-2024-mvtora-postdisaster-vfc]] now records parse-grounded received/publication/current-version dates, the conference precursor DOI note, and the discussion-section limitation about three-layer hardware overhead / latency-weighted energy tradeoff. [[sun-2024-imssa-uav-secure-cb]] now clarifies that the Raspberry-Pi result is an optimizer implementation rather than a full UAV/UVAA deployment.
- Verification scope: `python tools/wiki/curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers, with 1 referenced-name mismatch entry (`Untouched primary documents (PDFs, parsed markdown, images`) that did not indicate an uncurated paper. The remaining gates were run before commit.
- LLM Wiki health endpoint was reachable with unauthenticated read access; the read-only graph API reported 649 nodes and 6007 edges.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded source-page audit.

## 2026-06-09 - Audit source pages: batch 12 slice C

- Audited these five source pages only: [[su-2024-sensing-aided-isac-pls]], [[sun-2021-temcmop-uav-cb]], [[sun-2023-bargain-match-vec]], [[sun-2024-active-passive-ris-receiver]], and [[sun-2024-asap-uav-swarm]]. Verified title / authors / year / venue / DOI where present, key numeric claims, method and system-model claims, related-link sanity, evergreen wording, frontmatter, and raw artifact pointers against the linked parses.
- Content-page fixes: [[sun-2024-asap-uav-swarm]] now carries the standard Citation section, explicit original-PDF / images raw-artifact note, and an audit-current `updated` date. [[su-2024-sensing-aided-isac-pls]], [[sun-2021-temcmop-uav-cb]], [[sun-2023-bargain-match-vec]], and [[sun-2024-active-passive-ris-receiver]] were already grounded and needed no content-page edits.
- Verification scope: `python tools/wiki/curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers, with 1 referenced-name mismatch entry (`Untouched primary documents (PDFs, parsed markdown, images`) that did not indicate an uncurated paper. The remaining gates were run before commit.
- LLM Wiki health endpoint was reachable with unauthenticated read access; the read-only graph API reported 649 nodes and 6007 edges.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded source-page audit.

## 2026-06-09 - Audit source pages: batch 12 slice B

- Audited these five source pages only: [[seid-2021-madrl-multiuav-iot-edge]], [[shao-2024-drl-antijamming-mec]], [[shi-2023-two-timescale-migration-rerouting]], [[song-2022-emorl-tcto-uav]], and [[song-2024-mol-aoi-energy]]. Verified title / authors / year / venue / DOI where present, key numeric claims, method and system-model claims, related-link sanity, evergreen wording, frontmatter, and raw artifact pointers against the linked parses.
- Content-page fixes: [[shao-2024-drl-antijamming-mec]] and [[song-2024-mol-aoi-energy]] now carry explicit original-PDF / images raw-artifact notes and audit-current `updated` dates. [[seid-2021-madrl-multiuav-iot-edge]], [[shi-2023-two-timescale-migration-rerouting]], and [[song-2022-emorl-tcto-uav]] were already grounded and needed no content-page edits.
- Verification scope: `python tools/wiki/curation_status.py --dupes` reported no genuinely new papers before commit. The remaining gates were run before commit.
- LLM Wiki health endpoint was reachable with unauthenticated read access; the read-only graph API reported 649 nodes and 6007 edges.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded source-page audit.

## 2026-06-09 - Audit source pages: batch 12 slice A

- Audited these five source pages only: [[qin-2025-matd3-noma-queue-sagin]], [[qin-2025-urllc-noma-uav-iscc]], [[qu-ecoei-uav-swarm]], [[raivi-2024-jdaco-postdisaster-iot]], and [[schulman-2017-ppo]]. Verified title / authors / year / venue / DOI where present, key numeric claims, method and system-model claims, related-link sanity, evergreen wording, frontmatter, and raw artifact pointers against the linked parses.
- Content-page fixes: [[qin-2025-matd3-noma-queue-sagin]] now records parse-supported system-cost, queue-backlog, and AAV-compute-capacity numeric findings; [[raivi-2024-jdaco-postdisaster-iot]] now records the parse-stated future-work directions; [[schulman-2017-ppo]] now avoids web-narrated venue/DOI wording while keeping the 2017 year grounded in the raw sidecar arXiv date line. [[qin-2025-urllc-noma-uav-iscc]] and [[qu-ecoei-uav-swarm]] were already grounded and needed no content-page edits.
- Verification scope: `python tools/wiki/curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers, with 1 referenced-name mismatch entry (`Untouched primary documents (PDFs, parsed markdown, images`) that did not indicate an uncurated paper. The remaining gates were run before commit.
- LLM Wiki health endpoint was reachable with unauthenticated read access; the read-only graph API reported 649 nodes and 6007 edges.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded source-page audit.

## 2026-06-08 - Audit source pages: batch 11 slice D

- Audited these five source pages only: [[pervez-2024-acm-multiuav-mec]], [[qi-2024-msar-minmax-latency]], [[qian-2022-uav-maritime-iot-noma]], [[qian-2024-marine-fl-dt-secrecy]], and [[qin-2025-bcuav-masac]]. Verified title / authors / year / venue / DOI where present, key numeric claims, method and system-model claims, related-link sanity, evergreen wording, frontmatter, and raw artifact pointers against the linked parses.
- Content-page fixes: [[qin-2025-bcuav-masac]] now states the parse-supported queue-delay result as "more than 29.47% queue-delay reduction" rather than terse signed shorthand, and carries an audit-current `updated` date. [[pervez-2024-acm-multiuav-mec]], [[qi-2024-msar-minmax-latency]], [[qian-2022-uav-maritime-iot-noma]], and [[qian-2024-marine-fl-dt-secrecy]] were already grounded and needed no content-page edits.
- Verification scope: `python tools/wiki/curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers, with 1 referenced-name mismatch entry (`Untouched primary documents (PDFs, parsed markdown, images`) that did not indicate an uncurated paper. The remaining gates were run before commit.
- LLM Wiki health endpoint was reachable with unauthenticated read access; the read-only graph API reported 649 nodes and 6007 edges.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded source-page audit.

## 2026-06-08 - Audit source pages: batch 11 slice C

- Audited these five source pages only: [[pan-2025-uav-ris-energy-efficient-comm]], [[peng-2020-maddpg-uav-vehicular]], [[peng-2022-cmop-uav-path-planning]], [[peng-2024-energy-time-uav-its]], and [[peng-2025-drudm-cfg]]. Verified title / authors / year / venue / DOI where present, key numeric claims, method and system-model claims, related-link sanity, evergreen wording, frontmatter, and raw artifact pointers against the linked parses.
- Content-page fixes: [[pan-2025-uav-ris-energy-efficient-comm]] carries the parse-stated 10-GU energy reduction of 13.60% and now has an audit-current `updated` date; [[peng-2022-cmop-uav-path-planning]], [[peng-2024-energy-time-uav-its]], and [[peng-2025-drudm-cfg]] now use explicit Parse / Origin PDF / Figures raw-artifact bullets. [[peng-2020-maddpg-uav-vehicular]] was already grounded and needed no content-page edits.
- Verification scope: `python tools/wiki/curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers, with 1 referenced-name mismatch entry (`Untouched primary documents (PDFs, parsed markdown, images`) that did not indicate an uncurated paper. The remaining gates were run before commit.
- LLM Wiki health endpoint was reachable with unauthenticated read access; the read-only graph API reported 649 nodes and 6007 edges.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded source-page audit.

## 2026-06-08 - Audit source pages: batch 11 slice B

- Audited these five source pages only: [[mozaffari-2019-drone-antenna-array]], [[mozaffari-2019-uav-wireless-tutorial]], [[nabi-2025-jour-hierarchical-aerial]], [[niazmand-2025-jopa-dnn-pruning-iiot]], and [[ning-2023-madrl-uav-trajectory-differentiated-services]]. Verified title / authors / year / venue / DOI where present, key numeric claims, method and system-model claims, related-link sanity, evergreen wording, frontmatter, and raw artifact pointers against the linked parses.
- Content-page fixes: [[nabi-2025-jour-hierarchical-aerial]] now records the parse-stated multi-HAP/satellite future-work direction and carries the standard original-PDF / images raw-artifact note; [[niazmand-2025-jopa-dnn-pruning-iiot]] now replaces a stale read-range caveat with the parse-stated dynamic radio-resource-scheduling future-work direction. [[mozaffari-2019-drone-antenna-array]], [[mozaffari-2019-uav-wireless-tutorial]], and [[ning-2023-madrl-uav-trajectory-differentiated-services]] were already grounded and needed no content-page edits.
- Verification scope: `python tools/wiki/curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers, with 1 referenced-name mismatch entry (`Untouched primary documents (PDFs, parsed markdown, images`) that did not indicate an uncurated paper. The remaining gates were run before commit.
- LLM Wiki health endpoint was reachable with unauthenticated read access; the read-only graph API reported 649 nodes and 6007 edges.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded source-page audit.

## 2026-06-08 - Audit source pages: ADM DT migration and Mozaffari UAV placement foundations

- Audited these five source pages only: [[mou-2025-adm-dt-migration]], [[mozaffari-2015-drone-small-cells]], [[mozaffari-2016-efficient-multi-uav-coverage]], [[mozaffari-2016-uav-underlaid-d2d]], and [[mozaffari-2017-uav-iot-energy-efficient]]. Verified title / authors / year / venue / DOI where present, key numeric claims, method and system-model claims, related-link sanity, evergreen wording, frontmatter, and raw artifact pointers against the linked parses.
- Content-page fixes: [[mou-2025-adm-dt-migration]] now records the parse-stated future-work directions; the four Mozaffari pages now use explicit Parse / Origin PDF / Figures raw-artifact bullets. The audited DOI / venue / year and headline numeric claims were already grounded in the parses.
- Verification scope: `python tools/wiki/curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers, with 1 referenced-name mismatch entry (`Untouched primary documents (PDFs, parsed markdown, images`) that did not indicate an uncurated paper; `python tools/wiki/process_refs.py` reported 0 hits; `python tools/wiki/linkcheck.py --orphans` reported zero dangling links and 5 orphans (`MinerU_markdown_202605072001035_dfcfcb28`, `MinerU_markdown_202605131927481_3b25f7d3`, `README`, `full`, `schema`); `python tools/wiki/frontmatter_audit.py --type source` reported 257 pages checked and 0 errors.
- LLM Wiki health endpoint was reachable with unauthenticated read access; the read-only graph API reported 649 nodes and 6007 edges.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded source-page audit.

## 2026-06-08 - Audit source pages: drone swarm GAGLPP, secure RIS-UAV MEC-IoT, MCC energy efficiency, DQN Atari, ground-satellite UAM

- Audited these five source pages only: [[miao-2022-gaglpp-drone-swarm-iiot]], [[michailidis-2024-secure-ris-uav-mec-iot]], [[miettinen-2010-mcc-energy-efficiency]], [[mnih-2015-dqn-atari]], and [[moon-2024-ground-satellite-uam-scheduling]]. One content-page fix was required: the [[miettinen-2010-mcc-energy-efficiency]] citation no longer narrates web verification in published prose and now stays evergreen. The other four pages were already grounded in their linked parses for DOI / venue / year where present, title / H1 consistency, key numeric claims, related-link sanity, and evergreen wording, so no additional content-page edits were required.
- Verification scope: `python tools/wiki/curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers; `python tools/wiki/process_refs.py` reported 0 hits; `python tools/wiki/linkcheck.py --orphans` reported zero dangling links and 5 orphans (`MinerU_markdown_202605072001035_dfcfcb28`, `MinerU_markdown_202605131927481_3b25f7d3`, `README`, `full`, `schema`); `python tools/wiki/frontmatter_audit.py --type source` reported 257 pages checked and 0 errors.
- LLM Wiki health endpoint was reachable with unauthenticated read access, and the read-only graph API reported 649 nodes and 6007 edges.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded source-page audit.

## 2026-06-08 - Audit source pages: hierarchical routing, NTN caching, BCSA-FRL, IRS-NOMA secrecy, UAV-ISAC overview

- Audited these five source pages only: [[mao-2024-fso-leo-hierarchical-routing]], [[mao-2024-ntn-hierarchical-caching-cav]], [[mao-2025-bcsa-frl]], [[mao-2025-irs-noma-fl-secrecy]], and [[meng-2024-uav-isac-overview]]. One content-page fix was required: [[mao-2025-bcsa-frl]] now matches its frontmatter title with an evergreen H1. The other four pages were already grounded in their linked parses for DOI / venue / year where present, title / H1 consistency, key numeric claims, related-link sanity, and evergreen wording, so no additional content-page edits were required.
- Verification scope: `python tools/wiki/curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers; `python tools/wiki/process_refs.py` reported 0 hits; `python tools/wiki/linkcheck.py --orphans` reported zero dangling links and 5 orphans (`MinerU_markdown_202605072001035_dfcfcb28`, `MinerU_markdown_202605131927481_3b25f7d3`, `README`, `full`, `schema`); `python tools/wiki/frontmatter_audit.py --type source` reported 257 pages checked and 0 errors.
- LLM Wiki health endpoint was reachable with unauthenticated read access, and the read-only graph API reported 649 nodes and 6007 edges.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded source-page audit.

## 2026-06-08 - Audit source pages: vehicular P-DQN, MEC architecture survey, AI-NTN survey, EH-MEC offloading, MEC communication survey

- Audited these five source pages only: [[ma-2025-pdqn-vehicular-mec]], [[mach-2017-mec-survey-architecture]], [[mahboob-2024-ai-ntn-survey]], [[mao-2016-lodco-eh-mec-offloading]], and [[mao-2017-mec-survey-communication]]. All five pages were already grounded in their linked parses for DOI / venue / year where present, title / H1 consistency, key numeric claims, related-link sanity, and evergreen wording, so no content-page edits were required.
- Verification scope: `python tools/wiki/curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers; `python tools/wiki/process_refs.py` reported 0 hits; `python tools/wiki/linkcheck.py --orphans` reported zero dangling links and 5 orphans (`MinerU_markdown_202605072001035_dfcfcb28`, `MinerU_markdown_202605131927481_3b25f7d3`, `README`, `full`, `schema`); `python tools/wiki/frontmatter_audit.py --type source` reported 257 pages checked and 0 errors.
- LLM Wiki health endpoint was reachable with unauthenticated read access, and the read-only graph API reported 649 nodes and 6007 edges.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded source-page audit.

## 2026-06-08 - Audit source pages: maritime secure relay, UAV MBS placement, cellular hotspot offloading, marine NOMA emergency offloading, covert mmWave

- Audited these five source pages only: [[lu-2023-uav-relay-secure-maritime-mec]], [[lyu-2017-spiral-mbs-placement]], [[lyu-2018-uav-hotspot-offloading]], [[lyu-2023-noma-marine-emergency-offloading]], and [[ma-2024-covert-mmwave-finite-blocklength]]. All five pages were already grounded in their linked parses for DOI / venue / year where present, title / H1 consistency, key numeric claims, related-link sanity, and evergreen wording, so no content-page edits were required.
- Verification scope: `python tools/wiki/curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers; `python tools/wiki/process_refs.py` reported 0 hits; `python tools/wiki/linkcheck.py --orphans` reported zero dangling links and 5 orphans (`MinerU_markdown_202605072001035_dfcfcb28`, `MinerU_markdown_202605131927481_3b25f7d3`, `README`, `full`, `schema`); `python tools/wiki/frontmatter_audit.py --type source` reported 257 pages checked and 0 errors.
- LLM Wiki health endpoint was reachable with unauthenticated read access; the read-only graph API was reachable and reported 649 nodes and 6007 edges.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded source-page audit.

## 2026-06-08 - Audit source pages: HAP-UAV maritime IoT, MAD2RL VEC, j-PPO+EN-ConvNTM

- Audited these three source pages only: [[liu-2025-haps-uav-maritime-iot]], [[liu-2025-mad2rl-dnn-vec]], and [[liu-2026-jppo-en-convntm]]. All three pages were already grounded in their linked parses for DOI / venue / year where present, title / H1 consistency, key numeric claims, related-link sanity, and evergreen wording, so no content-page edits were required.
- Verification scope: `python tools/wiki/curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers; `python tools/wiki/process_refs.py` reported 0 hits; `python tools/wiki/linkcheck.py --orphans` reported zero dangling links and 5 orphans (`MinerU_markdown_202605072001035_dfcfcb28`, `MinerU_markdown_202605131927481_3b25f7d3`, `README`, `full`, `schema`); `python tools/wiki/frontmatter_audit.py --type source` reported 257 pages checked and 0 errors.
- LLM Wiki health endpoint was reachable with unauthenticated read access; the read-only graph API was reachable and reported 649 nodes and 6007 edges.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded source-page audit.

## 2026-06-08 - Audit source pages: HATRPO-UCB collaborative beamforming, SAGIN spherical SG connectivity

- Audited these two source pages only: [[liu-2024-hatrpo-ucb-cb]] and [[liu-2024-sagin-spherical-sg-connectivity]]. Both pages were already grounded in their linked parses for DOI / venue / year, title / H1 consistency, key numeric claims, related-link sanity, and evergreen wording, so no content-page edits were required.
- Verification scope: `python tools/wiki/curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers; `python tools/wiki/process_refs.py` reported 0 hits; `python tools/wiki/linkcheck.py --orphans` reported zero dangling links and 5 orphans (`MinerU_markdown_202605072001035_dfcfcb28`, `MinerU_markdown_202605131927481_3b25f7d3`, `README`, `full`, `schema`); `python tools/wiki/frontmatter_audit.py --type source` reported 257 pages checked and 0 errors.
- LLM Wiki health endpoint was reachable with unauthenticated read access; the read-only graph API was reachable and reported 649 nodes and 6007 edges.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded source-page audit.

## 2026-06-08 - Audit source pages: cooperative UAV power IoT, wireless-powered cooperative MEC, maritime UAV virtualization, MISO UAV MEC, SAGECN offloading

- Audited these five source pages only: [[liu-2020-cooperative-uav-mec-power-iot]], [[liu-2020-wpt-cooperative-uav-mec]], [[liu-2022-maritime-uav-mec-virtualization]], [[liu-2022-miso-uav-mec-trajectory]], and [[liu-2023-sagecn-online-offloading]]. The pages were already grounded in their linked parses for DOI / venue / year, title / H1 consistency, key numeric claims, related-link sanity, and evergreen wording; I made only small wording cleanups to remove process narration from the published prose.
- Verification scope: `python tools/wiki/curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers; `python tools/wiki/process_refs.py` reported 0 hits; `python tools/wiki/linkcheck.py --orphans` reported zero dangling links and 5 orphans (`MinerU_markdown_202605072001035_dfcfcb28`, `MinerU_markdown_202605131927481_3b25f7d3`, `README`, `full`, `schema`); `python tools/wiki/frontmatter_audit.py --type source` reported 257 pages checked and 0 errors.
- LLM Wiki health endpoint was reachable with unauthenticated read access; the read-only graph API was reachable and reported 649 nodes and 6007 edges.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded source-page audit.

## 2026-06-08 - Audit source pages: hybrid THz UM-MIMO CE, two-hop air-ground DRL offloading, collaborative beamforming energy, GAI SemCom survey, DDPG

- Audited these five source pages only: [[li-2025-thz-um-mimo-ce-hybrid-field]], [[li-2025-twohop-airground-drl-offloading]], [[liang-2024-hmecmop-uav-cb]], [[liang-2025-gai-semcom-survey]], and [[lillicrap-2016-ddpg-continuous-control]]. One source page was corrected for evergreen wording and citation grounding: the DDPG page now states the venue/year without process narration and no longer mentions web verification in the published prose. The other four source pages were already grounded in their linked parses for DOI / venue / year, title / H1 consistency, key numeric claims, related-link sanity, and evergreen wording.
- Verification scope: `python tools/wiki/curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers, with 1 referenced-name mismatch entry (`Untouched primary documents (PDFs, parsed markdown, images`) that did not indicate an uncurated paper; `python tools/wiki/process_refs.py` reported 0 hits; `python tools/wiki/linkcheck.py --orphans` reported zero dangling links and 5 orphans (`MinerU_markdown_202605072001035_dfcfcb28`, `MinerU_markdown_202605131927481_3b25f7d3`, `README`, `full`, `schema`); `python tools/wiki/frontmatter_audit.py --type source` reported 257 pages checked and 0 errors.
- LLM Wiki health endpoint was reachable with unauthenticated read access; the read-only graph API was reachable and reported 649 nodes and 6007 edges.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded source-page audit.

## 2026-06-08 - Audit source pages: robust b-MAPPO multi-UAV, SMDRL resource-constrained MEC, two-hop packet scheduling, OMRP CB IoT, UAV swarm stochastic game

- Audited these five source pages only: [[li-2024-robust-bmappo-multiuav-mec]], [[li-2024-smdrl-resource-constrained-mec]], [[li-2024-twohop-iort-packet-scheduling]], [[li-2025-omrp-cb-iot]], and [[li-2025-stochastic-game-uav-swarm]]. No content-page edits were required; each page was already grounded in its linked parse for DOI / venue / year, title / H1 consistency, key numeric claims, related-link sanity, and evergreen wording.
- Verification scope: `python tools/wiki/curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers; `python tools/wiki/process_refs.py` reported 0 hits; `python tools/wiki/linkcheck.py --orphans` reported zero dangling links and 5 orphans (`MinerU_markdown_202605072001035_dfcfcb28`, `MinerU_markdown_202605131927481_3b25f7d3`, `README`, `full`, `schema`); `python tools/wiki/frontmatter_audit.py --type source` reported 257 pages checked and 0 errors; `python tools/wiki/index_audit.py` reported 651 catalogue-able pages, 651 distinct slugs linked from `index.md`, and 0 duplicate primary listings.
- LLM Wiki health endpoint was reachable with unauthenticated read access; the read-only graph API was reachable and reported 649 nodes and 6007 edges.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded source-page audit.

## 2026-06-08 - Audit source pages: air-ground VEC offloading, ground-space EMODRL, UAV swarm AVAA, IRS secure WPMEC, UAV swarm clustering

- Audited these five source pages only: [[li-2024-airground-vec-offloading]], [[li-2024-emodrl-ground-space-cb]], [[li-2024-emssa-uav-swarm-vaa]], [[li-2024-irs-secure-wpmec]], and [[li-2024-rldc-uav-swarm-clustering]]. No content-page edits were required; each page was already grounded in its linked parse for DOI / venue / year, title / H1 consistency, key numeric claims, related-link sanity, and evergreen wording.
- Verification scope: `python tools/wiki/curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers, with 1 referenced-name mismatch entry (`Untouched primary documents (PDFs, parsed markdown, images`) that did not indicate an uncurated paper; `python tools/wiki/process_refs.py` reported 0 hits; `python tools/wiki/linkcheck.py --orphans` reported zero dangling links and 5 orphans (`MinerU_markdown_202605072001035_dfcfcb28`, `MinerU_markdown_202605131927481_3b25f7d3`, `README`, `full`, `schema`); `python tools/wiki/frontmatter_audit.py --type source` reported 257 pages checked and 0 errors.
- LLM Wiki health endpoint was reachable with unauthenticated read access; the read-only graph API was reachable and reported 649 nodes and 6007 edges.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded source-page audit.

## 2026-06-08 - Audit source pages: LEO handover, maritime SAR HVMAPPO, UAV MEC ADMM, maritime coverage, marine IoT jamming

- Audited these five source pages only: [[lee-2024-dho-leo-handover]], [[lei-2024-hvmappo-maritime-sar]], [[li-2020-energy-efficient-uav-mec-admm]], [[li-2020-maritime-uav-satellite-coverage]], and [[li-2023-secure-marine-iot-jamming]]. No content-page edits were required; each page was already grounded in its linked parse for DOI / venue / year, title / H1 consistency, key numeric claims, related-link sanity, and evergreen wording.
- Verification scope: `python tools/wiki/curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers; `python tools/wiki/process_refs.py` reported 0 hits; `python tools/wiki/linkcheck.py --orphans` reported zero dangling links and 5 orphans (`MinerU_markdown_202605072001035_dfcfcb28`, `MinerU_markdown_202605131927481_3b25f7d3`, `README`, `full`, `schema`); `python tools/wiki/frontmatter_audit.py --type source` reported 257 pages checked and 0 errors.
- LLM Wiki health endpoint was reachable with unauthenticated read access; the read-only graph API was reachable and reported 649 nodes and 6007 edges.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded source-page audit.

## 2026-06-08 - Audit source pages: DRO aerial MEC, UAV heading SDMA, LAE ISAC overview, hierarchical aerial MAPPO, GAI wireless optimization survey

- Audited these five source pages only: [[jia-2025-dro-uav-hap-mec]], [[jiang-2012-uav-heading-sdma]], [[jiang-2025-isac-lae-overview]], [[kang-2023-mappo-hierarchical-aerial]], and [[khoramnejad-2025-gai-wireless-optimization-survey]]. No content-page edits were required; each page was already grounded in its linked parse for DOI / venue / year, title / H1 consistency, key numeric claims, related-link sanity, and evergreen wording.
- Verification scope: `python tools/wiki/curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers, with 1 referenced-name mismatch entry (`Untouched primary documents (PDFs, parsed markdown, images`) that did not indicate an uncurated paper; `python tools/wiki/process_refs.py` reported 0 hits; `python tools/wiki/linkcheck.py --orphans` reported zero dangling links and 5 orphans (`MinerU_markdown_202605072001035_dfcfcb28`, `MinerU_markdown_202605131927481_3b25f7d3`, `README`, `full`, `schema`); `python tools/wiki/frontmatter_audit.py --type source` reported 257 pages checked and 0 errors.
- LLM Wiki health endpoint was reachable with unauthenticated read access; the read-only graph API was reachable and reported 649 nodes and 6007 edges.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded source-page audit.

## 2026-06-08 - Audit source pages: generative AI physical layer, DCBF survey, UAV cloudlet bit allocation, UAV MEC energy minimization, hierarchical aerial computing

- Audited these five source pages only: [[huynh-2024-gai-physical-layer-survey]], [[jayaprakasam-2017-dcbf-wsn-survey]], [[jeong-2018-uav-cloudlet-bit-allocation]], [[ji-2021-uav-mec-noma-oma-energy-min]], and [[jia-2022-hierarchical-aerial-matching]]. No content-page edits were required; each page was already grounded in its linked parse for DOI / venue / year, title / H1 consistency, key numeric claims, related-link sanity, and evergreen wording.
- Verification scope: `python tools/wiki/curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers; `python tools/wiki/process_refs.py` reported 0 hits; `python tools/wiki/linkcheck.py --orphans` reported zero dangling links and 5 orphans (`MinerU_markdown_202605072001035_dfcfcb28`, `MinerU_markdown_202605131927481_3b25f7d3`, `README`, `full`, `schema`); `python tools/wiki/frontmatter_audit.py --type source` reported 257 pages checked and 0 errors.
- LLM Wiki health endpoint was reachable with unauthenticated read access; the read-only graph API was reachable and reported 649 nodes and 6007 edges.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded source-page audit.

## 2026-06-08 - Audit source pages: UAV relaying, MU-AEC task energy, IoV caching, dispersed computing, maritime secure CB

- Audited these five source pages only: [[hu-2019-uav-relay-edge-computing]], [[huang-2023-mu-aec-task-energy]], [[huang-2024-fed-idcco-iov-caching]], [[huang-2025-cmop-dispersed-computing]], and [[huang-2025-dual-aav-maritime-secure-cb]]. No content-page edits were required; each page was already grounded in its linked parse for DOI / venue / year, title / H1 consistency, key numeric claims, related-link sanity, and evergreen wording.
- Verification scope: `python tools/wiki/curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers; `python tools/wiki/process_refs.py` reported 0 hits; `python tools/wiki/linkcheck.py --orphans` reported zero dangling links and 5 orphans (`MinerU_markdown_202605072001035_dfcfcb28`, `MinerU_markdown_202605131927481_3b25f7d3`, `README`, `full`, `schema`); `python tools/wiki/frontmatter_audit.py --type source` reported 257 pages checked and 0 errors.
- LLM Wiki health endpoint was reachable with unauthenticated read access; the read-only graph API was reachable and reported 649 nodes and 6007 edges.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded source-page audit.

## 2026-06-08 - Audit source pages: fairness multi-UAV, backscatter WPMEC, HAP NOMA, ETSI MEC white paper, UAV MEC PDD

- Audited these five source pages only: [[he-2023-fairness-3d-multiuav-maddpg]], [[he-2024-backscatter-wpmec-cooperation]], [[hsu-2025-drl-hues-hap-noma]], [[hu-2015-mec-5g-etsi-whitepaper]], and [[hu-2019-pdd-uav-mec-offloading]]. No content-page edits were required; DOI / venue / year, title / H1 consistency, grounded numeric claims, related-link sanity, and evergreen wording were already aligned with the corresponding parses.
- Verification scope: `python tools/wiki/curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers; `python tools/wiki/process_refs.py` reported 0 hits; `python tools/wiki/linkcheck.py --orphans` reported zero dangling links and 5 orphans (`MinerU_markdown_202605072001035_dfcfcb28`, `MinerU_markdown_202605131927481_3b25f7d3`, `README`, `full`, `schema`); `python tools/wiki/frontmatter_audit.py --type source` reported 257 pages checked and 0 errors.
- LLM Wiki health endpoint was reachable with unauthenticated read access; the read-only graph API was reachable and reported 649 nodes and 6007 edges.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded source-page audit.

## 2026-06-08 - Audit source pages: SAGIN FL handover, multi-UAV priority offloading, task-driven priority offloading, UAV altitude/beamwidth, EUA game

- Audited these five source pages only: [[han-2024-sagin-fl-handover]], [[hao-2024-clp-multiuav-priority-offloading]], [[hao-2025-priority-aware-task-driven-co]], [[he-2018-uav-altitude-beamwidth]], and [[he-2019-euagame-user-allocation]]. No content-page edits were required; DOI / venue / year, title / H1 consistency, grounded numeric claims, related-link sanity, and evergreen wording were already aligned with the corresponding parses.
- Verification scope: `python tools/wiki/curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers; `python tools/wiki/process_refs.py` reported 0 hits; `python tools/wiki/linkcheck.py --orphans` reported zero dangling links and 5 orphans (`MinerU_markdown_202605072001035_dfcfcb28`, `MinerU_markdown_202605131927481_3b25f7d3`, `README`, `full`, `schema`); `python tools/wiki/frontmatter_audit.py --type source` reported 257 pages checked and 0 errors.
- LLM Wiki health endpoint was reachable with unauthenticated read access; the read-only graph API was reachable and reported a baseline of 649 nodes and 6007 edges.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded source-page audit.

## 2026-06-08 - Audit source pages: SAGIN perception offloading, cache-enabled UAV service experience, multi-UAV 5G offloading, proactive eavesdropping, ground-satellite FL

- Audited these five source pages only: [[gao-2024-sagin-perception-offloading]], [[gao-2024-service-experience-cache-uav]], [[guo-2023-mccco-multiuav-5g-offloading]], [[guo-2024-multiuav-proactive-eavesdropping]], and [[han-2024-ground-satellite-fl]]. No content-page edits were required; DOI / venue / year, title / H1 consistency, key grounded numeric claims, related-link sanity, and evergreen wording were already aligned with the corresponding parses.
- Verification scope: `python tools/wiki/curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers; `python tools/wiki/process_refs.py` reported 0 hits; `python tools/wiki/linkcheck.py --orphans` reported zero dangling links and 5 orphans (`MinerU_markdown_202605072001035_dfcfcb28`, `MinerU_markdown_202605131927481_3b25f7d3`, `README`, `full`, `schema`); `python tools/wiki/frontmatter_audit.py --type source` reported 257 pages checked and 0 errors.
- LLM Wiki health endpoint was reachable with unauthenticated read access; the read-only graph API was reachable and the current baseline remained 649 nodes and 6007 edges.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded source-page audit.

## 2026-06-08 - Audit source pages: duan MOTO, faisal CGAN-RIS-ISAC, fu OTAE batching, fujimoto TD3, gao UAV mobile GT

- Audited these five source pages only: [[duan-2023-moto-smallcell-offloading]], [[faisal-2025-cgan-ris-isac-channel]], [[fu-2025-otae-inference-lae-batching]], [[fujimoto-2018-td3-actor-critic]], and [[gao-2024-d3qn-uav-mec-mobile-gt]]. No content-page edits were required; DOI / venue / year, title / H1 consistency, key grounded numeric claims, related-link sanity, and evergreen wording were all already aligned with the corresponding parses.
- Verification scope: `python tools/wiki/curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers; `python tools/wiki/process_refs.py` reported 0 hits; `python tools/wiki/linkcheck.py --orphans` reported zero dangling links and 5 orphans (`MinerU_markdown_202605072001035_dfcfcb28`, `MinerU_markdown_202605131927481_3b25f7d3`, `README`, `full`, `schema`); `python tools/wiki/frontmatter_audit.py --type source` reported 257 pages checked and 0 errors.
- LLM Wiki health endpoint was reachable with unauthenticated read access; the read-only graph API reported 649 nodes and 6007 edges.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded source-page audit.

## 2026-06-08 - Audit source pages: MADDPG service placement, D2SAC ASP selection, distributed foundation models, GDM tutorial, YOLO SemCom digital twin

- Audited these five source pages only: [[du-2023-maddpg-service-placement-agin]], [[du-2024-d2sac-aigc-asp-selection]], [[du-2024-distributed-foundation-models-6g]], [[du-2024-gdm-network-optimization-tutorial]], and [[du-2024-yolo-semcom-digital-twin]]. Corrected evergreen wording and grounding on the source pages where needed: removed parse/process narration from source prose, normalized parse-referenced wording into evergreen factual statements, and kept DOI / venue / year / title / H1 consistency intact.
- Verification scope: `python tools/wiki/curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers; `python tools/wiki/process_refs.py` reported 0 hits; `python tools/wiki/linkcheck.py --orphans` reported zero dangling links and 5 orphans (`MinerU_markdown_202605072001035_dfcfcb28`, `MinerU_markdown_202605131927481_3b25f7d3`, `README`, `full`, `schema`); `python tools/wiki/frontmatter_audit.py --type source` reported 257 pages checked and 0 errors; the LLM Wiki health endpoint was reachable and returned `allowUnauthenticated:true`; the read-only graph API was reachable.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded source-page audit.

## 2026-06-08 - Audit source pages: marine offloading, graph-resource-management survey, vehicular offloading

- Audited these five source pages only: [[dai-2023-hybrid-noma-fdma-marine]], [[dai-2024-graph-rm-survey-learning]], [[dai-2024-graph-rm-survey-optimization]], [[dai-2024-multiuav-marine-welfare]], and [[dai-2024-uav-vehicular-offloading-lyapunov]]. No content-page edits were required; each page was already grounded in its linked parse for DOI / venue / year, title / H1 consistency, key numeric claims, related-link sanity, and evergreen wording.
- Verification scope: `python tools/wiki/curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers; `python tools/wiki/process_refs.py` reported 0 hits; `python tools/wiki/linkcheck.py --orphans` reported zero dangling links and 5 orphans (`MinerU_markdown_202605072001035_dfcfcb28`, `MinerU_markdown_202605131927481_3b25f7d3`, `README`, `full`, `schema`); `python tools/wiki/frontmatter_audit.py --type source` reported 257 pages checked and 0 errors; the LLM Wiki health endpoint was reachable and the read-only graph API was reachable.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded source-page audit.

## 2026-06-08 - Audit source pages: SAGIN offloading, satellite SEC, IRS-SWIPT, secure RIS-ISAC, marine multi-access

- Audited these five source pages only: [[cheng-2019-sagin-iot-offloading-rl]], [[cheng-2025-dos-satellite-edge-computing]], [[chhea-2025-irs-uav-swipt-drl]], [[chu-2024-secure-ris-isac]], and [[dai-2023-hybrid-marine-mmwl]]. The pages were already grounded in their parses on DOI / venue / year, title / H1 consistency, key numeric claims, related-link sanity, and evergreen wording; the only source-page change was non-substantive line-ending normalization in [[chu-2024-secure-ris-isac]].
- Verification scope: `python tools/wiki/curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers; `python tools/wiki/process_refs.py` reported 0 hits; `python tools/wiki/linkcheck.py --orphans` reported zero dangling links and 5 orphans (`MinerU_markdown_202605072001035_dfcfcb28`, `MinerU_markdown_202605131927481_3b25f7d3`, `README`, `full`, `schema`); `python tools/wiki/frontmatter_audit.py --type source` reported 257 pages checked and 0 errors; the LLM Wiki health endpoint was reachable and the read-only graph API was available.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded source-page audit.

## 2026-06-08 - Audit source pages: video caching, THOAS, PLS game, ULSE game, SWIPT-MEC SAC

- Audited these five source pages only: [[chen-2024-dro-video-caching]], [[chen-2024-thoas-traffic-aware-sagin]], [[chen-2024-three-party-hierarchical-game-pls]], [[chen-2024-ulse-game]], and [[chen-2025-swipt-mec-sac]]. No content-page edits were required; each page was already grounded in its linked parse with DOI / venue / year, title / H1 consistency, key numeric claims, related-link sanity, and evergreen wording intact for this bounded slice.
- Verification scope: `python tools/wiki/curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers; `python tools/wiki/process_refs.py` reported 0 hits; `python tools/wiki/linkcheck.py --orphans` reported zero dangling links and 5 orphans (`MinerU_markdown_202605072001035_dfcfcb28`, `MinerU_markdown_202605131927481_3b25f7d3`, `README`, `full`, `schema`); `python tools/wiki/frontmatter_audit.py --type source` reported 257 pages checked and 0 errors; the LLM Wiki health endpoint was reachable and unauthenticated in this shell.
- Read-only graph baseline from the local API remained 649 nodes / 6007 edges.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded source-page audit.

## 2026-06-08 - Audit source pages: decentralized offloading, QoE game, AIoT association, DOTORA

- Audited these five source pages only: [[chen-2015-decentralized-offloading-game]], [[chen-2016-multiuser-offloading-game-mec]], [[chen-2022-qoe-game-end-edge-cloud]], [[chen-2023-aiot-device-association]], and [[chen-2023-dotora-air-ground-online]]. No content-page edits were required; each page was already grounded in its linked parse with DOI / venue / year, title / H1 consistency, numeric claims, related-link sanity, and evergreen wording intact for this bounded slice.
- Verification scope: `python tools/wiki/curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers; `python tools/wiki/process_refs.py` reported 0 hits; `python tools/wiki/linkcheck.py --orphans` reported zero dangling links and 5 orphans (`MinerU_markdown_202605072001035_dfcfcb28`, `MinerU_markdown_202605131927481_3b25f7d3`, `README`, `full`, `schema`); `python tools/wiki/frontmatter_audit.py --type source` reported 257 pages checked and 0 errors; the LLM Wiki health endpoint was reachable.
- Read-only graph baseline from the local API remained 649 nodes / 6007 edges.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded source-page audit.

## 2026-06-08 - Audit source pages: batch 05 slice B

- Audited these five source pages only: [[bao-2025-ddpg-video-offloading]], [[benaya-2025-aerial-isac-haps]], [[bi-2025-sg-mapg]], [[bor-yaliniz-2016-3d-abs-placement]], and [[chang-2022-marl-multiuav-trajectory]]. No content-page edits were required; all five pages were already grounded in their linked parses, with DOI / venue / year, title / H1 consistency, and related-link sanity intact for this bounded slice.
- Verification scope: `python tools/wiki/curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers; `python tools/wiki/process_refs.py` reported 0 hits; `python tools/wiki/linkcheck.py --orphans` reported zero dangling links and 5 orphans (`MinerU_markdown_202605072001035_dfcfcb28`, `MinerU_markdown_202605131927481_3b25f7d3`, `README`, `full`, `schema`); `python tools/wiki/frontmatter_audit.py --type source` reported 257 pages checked and 0 errors; the LLM Wiki project API health endpoint was reachable.
- Graph stats from the read-only API remained available; the latest recorded project graph baseline in this audit thread is 649 nodes / 6005 edges.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded source-page audit.

## 2026-06-08 - Audit source pages: LAP altitude, MOALF-UAV-MEC, HAP-SWIPT, prospect-theory offloading, delay-aware edge-cloud

- Audited these five source pages only: [[al-hourani-2014-optimal-lap-altitude]], [[albakhrani-2025-moalf-uav-mec]], [[an-2024-multilayer-ris-hap-swipt]], [[apostolopoulos-2021-prospect-theory-uav-offloading]], and [[bai-2024-delay-aware-cooperative-edge-cloud]]. All five were already grounded, evergreen, and frontmatter-valid against their linked parses; the only source-page change was non-substantive line-ending normalization in [[al-hourani-2014-optimal-lap-altitude]].
- Verification scope: `python tools/wiki/curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers; `python tools/wiki/process_refs.py` reported 0 hits; `python tools/wiki/linkcheck.py --orphans` reported zero dangling links and 5 orphans (`MinerU_markdown_202605072001035_dfcfcb28`, `MinerU_markdown_202605131927481_3b25f7d3`, `README`, `full`, `schema`); `python tools/wiki/frontmatter_audit.py --type source` reported 257 pages checked and 0 errors.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded source-page audit.

## 2026-06-08 - Audit thesis pages: decomposition, constraints, hybrid-action memory

- Audited these three thesis pages only: [[decomposition-beats-end-to-end-drl-in-mec]], [[explicit-constraints-beat-reward-shaping-in-mec-drl]], and [[hybrid-action-memory-augmented-drl-wins-uav-mec]]. No content-page edits were required; all three were already evergreen, frontmatter-valid, and grounded in their linked source parses.
- Verification scope: `python tools/wiki/curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers; `python tools/wiki/process_refs.py` reported 0 hits; `python tools/wiki/linkcheck.py --orphans` reported zero dangling links and 5 orphans (`MinerU_markdown_202605072001035_dfcfcb28`, `MinerU_markdown_202605131927481_3b25f7d3`, `README`, `full`, `schema`); `python tools/wiki/frontmatter_audit.py --type thesis` reported 3 pages checked and 0 errors; the LLM Wiki health endpoint was reachable, and the graph endpoint reported 649 nodes / 6005 edges.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded thesis-page audit.

## 2026-06-08 - Audit synthesis pages: safety and robustness, swarm metaheuristics, solver-family comparison

- Audited these three synthesis pages only: [[safety-and-robustness-mechanisms-in-mec]], [[swarm-metaheuristics-in-uav-mec]], and [[drl-vs-evolutionary-vs-classical-solvers]]. The first two were already parse-grounded; the solver-family comparison page needed evergreen wording cleanup in its scope note, and the swarm page needed a small count wording fix so its opener matches the roster it presents.
- Verification scope: `python tools/wiki/curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers; `python tools/wiki/process_refs.py` reported 0 hits; `python tools/wiki/linkcheck.py --orphans` reported zero dangling links and 5 orphans (`MinerU_markdown_202605072001035_dfcfcb28`, `MinerU_markdown_202605131927481_3b25f7d3`, `README`, `full`, `schema`); `python tools/wiki/frontmatter_audit.py --type synthesis` reported 15 pages checked and 0 errors; the LLM Wiki health endpoint was reachable, and the graph endpoint was reachable in read-only mode.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded synthesis-page audit.

## 2026-06-08 - Audit synthesis pages: maritime architectures and SAGIN / satellite-offloading landscape

- Audited these two synthesis pages only: [[maritime-mec-architectures]] and [[sagin-satellite-offloading-landscape]]. No content-page edits were required; both pages were already evergreen, frontmatter-valid, and grounded in their linked source parses.
- Verification scope: `python tools/wiki/curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers; `python tools/wiki/process_refs.py` reported 0 hits; `python tools/wiki/linkcheck.py --orphans` reported zero dangling links and 5 orphans (`MinerU_markdown_202605072001035_dfcfcb28`, `MinerU_markdown_202605131927481_3b25f7d3`, `README`, `full`, `schema`); `python tools/wiki/frontmatter_audit.py --type synthesis` reported 15 pages checked and 0 errors; the LLM Wiki API health endpoint was reachable and the graph endpoint was reachable in read-only mode.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded synthesis-page audit.

## 2026-06-08 - Audit synthesis pages: ISAC sensing and MADDPG vs MASAC

- Audited these two synthesis pages only: [[isac-sensing-in-aerial-mec]] and [[maddpg-vs-masac-in-mec]]. No content-page edits were required; both pages were already evergreen, frontmatter-valid, and grounded in their linked source parses.
- Verification scope: `python tools/wiki/curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers; `python tools/wiki/process_refs.py` reported 0 hits; `python tools/wiki/linkcheck.py --orphans` reported zero dangling links and 5 orphans (`MinerU_markdown_202605072001035_dfcfcb28`, `MinerU_markdown_202605131927481_3b25f7d3`, `README`, `full`, `schema`); `python tools/wiki/frontmatter_audit.py --type synthesis` reported 15 pages checked and 0 errors; the LLM Wiki API health endpoint was reachable and the graph endpoint reported 649 nodes / 6005 edges.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded synthesis-page audit.

## 2026-06-08 - Audit synthesis pages: GAI-role split, hardware validation, hierarchical aerial MEC

- Audited these three synthesis pages only: [[gai-generator-vs-optimizer-in-isac]], [[hardware-validation-and-sim-to-real-in-mec]], and [[hierarchical-aerial-mec-design-space]]. No content-page edits were required; all three were already evergreen, frontmatter-valid, and grounded in their linked source parses.
- Verification scope: `python tools/wiki/curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers; `python tools/wiki/process_refs.py` reported 0 hits; `python tools/wiki/linkcheck.py --orphans` reported zero dangling links and 5 orphans (`MinerU_markdown_202605072001035_dfcfcb28`, `MinerU_markdown_202605131927481_3b25f7d3`, `README`, `full`, `schema`); `python tools/wiki/frontmatter_audit.py --type synthesis` reported 15 pages checked and 0 errors; the LLM Wiki API health endpoint was reachable and the graph endpoint was reachable in read-only mode.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded synthesis-page audit.

## 2026-06-08 - Audit synthesis pages: blockchain, CMOP lineage, collaborative beamforming, DRL recipe, DRL backbones

- Audited the five synthesis pages in this slice: [[blockchain-on-edge-trust-layer]], [[cmop-evolutionary-uav-mec-lineage]], [[collaborative-beamforming-in-aerial-mec]], [[design-recipe-multi-uav-mec]], and [[drl-backbones-across-uav-mec-sources]]. No content-page edits were required; all five were already evergreen, frontmatter-valid, and grounded in the corresponding source parses.
- Verification scope: `python tools/wiki/curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers; `python tools/wiki/process_refs.py` reported 0 hits; `python tools/wiki/linkcheck.py --orphans` reported zero dangling links and 5 orphans (`MinerU_markdown_202605072001035_dfcfcb28`, `MinerU_markdown_202605131927481_3b25f7d3`, `README`, `full`, `schema`); `python tools/wiki/frontmatter_audit.py --type synthesis` reported 15 pages checked and 0 errors; LLM Wiki API health was reachable and graph stats were 649 nodes / 6005 edges.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded synthesis-page audit.

## 2026-06-08 - Audit query pages: rich-media shape and CSI-robustness anchors

- Audited the five query pages in this slice: [[end-to-end-drl-feasibility-large-scale-mec]], [[query-does-en-convntm-generalize-beyond-uav-mec]], [[query-real-world-validation-of-jppo-en-convntm]], [[query-video-vs-cooperative-perception-offloading-shape]], and [[query-when-does-dro-beat-drl-for-csi-uncertainty]]. The first three were already evergreen and required no content-page edits; the last two had process-narration in their closing sentences and were rewritten to evergreen corpus-facing wording.
- Verification scope: `python tools/wiki/curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers; `python tools/wiki/frontmatter_audit.py --type query` reported 5 pages checked and 0 errors; `python tools/wiki/process_refs.py` reported 0 hits; `python tools/wiki/linkcheck.py --orphans` reported zero dangling links and 5 orphans (`MinerU_markdown_202605072001035_dfcfcb28`, `MinerU_markdown_202605131927481_3b25f7d3`, `README`, `full`, `schema`); LLM Wiki API health was reachable and graph stats were 649 nodes / 6005 edges.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded query-page audit.

## 2026-06-08 - Audit methodology page: Lyapunov-guided DRL

- Audited [[lyapunov-guided-drl]] against the raw parses for [[qin-2025-bcuav-masac]], [[zhu-2025-lycnn-drl-wpt-mec]], [[zhou-2024-jdl-abs-postdisaster-rescue]], [[gao-2024-sagin-perception-offloading]], [[qin-2025-matd3-noma-queue-sagin]], and [[you-2025-uncertain-maritime-hasac]]. The page is parse-grounded and evergreen as written, so no content-page edits were required.
- Verification scope: `curation_status.py --dupes` reported 257 raw folders / 257 curated references / 0 genuinely new papers; `frontmatter_audit.py --type methodology` reported 5 pages checked, 0 errors; `process_refs.py` reported 0 hits; `linkcheck.py --orphans` reported zero dangling links and 5 orphans (`MinerU_markdown_202605072001035_dfcfcb28`, `MinerU_markdown_202605131927481_3b25f7d3`, `README`, `full`, `schema`). LLM Wiki API graph check (`projects/current/graph?limit=5000`) reported 649 nodes and 6005 edges.
- Routing to mec-wiki-synthesizer: no new coverage gap surfaced in this bounded one-page audit.

## 2026-06-07 - Audit methodology page: DRL simulation with POMDP formulation

- Audited [[drl-simulation-with-pomdp-formulation]] against the raw parse for [[liu-2026-jppo-en-convntm]]. The page's POMDP framing, 3-channel observation, reward shaping, training/evaluation procedure, and hardware line are parse-grounded; the only correction was to remove process-narration from the lead sentence and make it evergreen.
- Verification scope: `curation_status.py --dupes` remained clean at 257 raw folders / 257 curated references / 0 genuinely new papers; `frontmatter_audit.py --type methodology` reported 5 pages checked, 0 errors; `process_refs.py` and `linkcheck.py --orphans` were run as the evergreen and link-integrity gates, with no issues reported in the audited scope; LLM Wiki API graph stats were unavailable in this shell due a transient local API call failure, so the audit relied on file-grounded verification.
- Routing to mec-wiki-synthesizer: no new synthesizer coverage gap surfaced in this bounded one-page audit.

## 2026-06-07 - Audit methodology page: discrete-continuous two-stage decomposition

- Audited [[discrete-continuous-two-stage-decomposition]] against its cited source pages and raw parses for [[wang-2026-aerial-marine-msar]], [[nabi-2025-jour-hierarchical-aerial]], [[jia-2025-dro-uav-hap-mec]], [[zhang-2025-mcma-task-migration]], [[ma-2025-pdqn-vehicular-mec]], and [[liu-2026-jppo-en-convntm]]. The stage table, solver labels, seam descriptions, and native-hybrid contrast are parse-grounded.
- Corrections: softened the page's continuous-stage premise so it distinguishes conditionally convex classical residuals from DRL continuous-control stages conditioned on a discrete decision. No DOI, venue, year, numeric-result, wikilink, or frontmatter corrections were needed.
- Verification scope: `log.md` line count 2715 -> 2722; raw/curated reconciliation clean at 257 raw folders / 257 curated references / 0 genuinely new papers; LLM Wiki API reachable on project `current` with graph 649 nodes / 6005 edges; `process_refs.py` 0 hits; `linkcheck.py --orphans` no dangling links; `frontmatter_audit.py --type methodology` 5 pages checked, 0 errors.
- Routing to mec-wiki-synthesizer: no new synthesizer coverage gap surfaced in this bounded one-page audit.

## 2026-06-07 - Audit methodology page: CTDE multi-agent DRL protocol

- Audited [[ctde-multi-agent-drl-protocol]] against its cited source pages and raw parses for [[zhang-2025-mcma-task-migration]], [[peng-2025-drudm-cfg]], [[kang-2023-mappo-hierarchical-aerial]], [[qin-2025-bcuav-masac]], and [[zhang-2025-ssac-mgi-heterogeneous-uav]]. The explicit CTDE claims, local-actor/global-critic split, action-space backbone mapping, DTDE contrast, and dense-fleet critic absence note are parse-grounded.
- Corrections: tightened the [[qin-2025-bcuav-masac]] wording so its AGIN-MASAC role is treated as a related Lyapunov-decomposed MASAC instantiation, not as a parse-labeled CTDE proof point. No DOI, venue, year, numeric-result, wikilink, or frontmatter corrections were needed on the methodology page.
- Verification scope: `log.md` line count 2708 -> 2715; raw/curated reconciliation clean at 257 raw folders / 257 curated references / 0 genuinely new papers; LLM Wiki API reachable on project `current` with graph 649 nodes / 6005 edges; `process_refs.py` 0 hits; `linkcheck.py --orphans` no dangling links; `frontmatter_audit.py --type methodology` 5 pages checked, 0 errors.
- Routing to mec-wiki-synthesizer: no new synthesizer coverage gap surfaced in this bounded one-page audit.

## 2026-06-07 - Audit methodology page: AO SDR SCA pipeline

- Audited [[ao-sdr-sca-convex-pipeline]] against the relevant source pages and raw parses for [[benaya-2025-aerial-isac-haps]], [[yao-2025-secure-isac-dual-eavesdropping]], [[tang-2024-iscc-uav-feel]], [[zhang-2019-uav-iot-comp-comm]], and [[liu-2022-miso-uav-mec-trajectory]]. Tightened the page so Tang is described as adjacent AO-only BBPO rather than a full SDR/SCA beamforming instance, clarified Yao's rank-one recovery wording, softened overbroad "de-facto / always" phrasing, and removed mojibake from the audited page.
- Verification scope: raw/curated reconciliation clean at 257 raw folders / 257 curated references / 0 genuinely new papers; LLM Wiki API reachable on project `current` with graph 649 nodes / 6005 edges. No new synthesizer routing gap surfaced in this one-page audit.

Reverse-chronological activity log (newest first). Curation and audit passes are kept in full; the LLM-Wiki desktop app's automated raw-file deletion events are consolidated under [Raw-source housekeeping](#raw-source-housekeeping) at the foot of this file.

## 2026-06-07 — Batch 02 derived-page audit, slice 1

### Scope audited

- Audited 20 derived pages: 6 comparisons and 14 findings in `wiki/comparisons/` and `wiki/findings/`.
- Source grounding checked against the relevant raw parses for headline numeric claims, including ACBFT 96.2%, ASAP 92.66%, BCSA-FRL 50% / 5% / 6 ms, BC-UAV-MASAC 15.41% / 30.73%, FedLEO 41% / 9.39%, j-PPO EN-ConvNTM ablation and hyperparameter values, maritime three-tier 39.3%, and DCB 30% handover reduction.

### Corrections

- Removed a dated correction note from [[masac-beats-maddpg-sensing-queue]] while preserving the parse-grounded MADDPG and PSO margins.
- Rewrote small process-facing wording in [[bcsa-frl-vs-bc-uav-masac]] and [[game-theoretic-offloading-formulations]] into evergreen comparison wording.
- Retitled [[neuralmap-loses-spatial-info]]'s "Implication for future work" section to a present-tense design implication.

### Verification

- Raw/curated reconciliation: `curation_status.py --dupes` = 257 raw folders, 257 curated references, 0 genuinely new uncurated papers.
- LLM Wiki API reachable on project `current`; graph 649 nodes / 6005 edges.
- `process_refs.py`: 0 files affected, 0 hits.
- `linkcheck.py`: no dangling links.
- `frontmatter_audit.py --type comparison`: 6 pages checked, 0 errors.
- `frontmatter_audit.py --type finding`: 14 pages checked, 0 errors.
- `corpus_counts.py`: 257 sources / 272 concepts / 72 entities / 14 findings / 15 synthesis / 6 comparisons / 5 methodology / 5 queries / 3 thesis; `raw/sources` 257.

### Routing to mec-wiki-synthesizer

- No new synthesizer coverage gaps surfaced in this bounded slice.

## 2026-06-07 — Meta-doc audit batch (log/index/overview)

### Meta-doc cleanups

- `log.md`: normalized the top 2026-06-07 header to `## YYYY-MM-DD — <title>` and moved the 2026-06-04 synthesis entry above the 2026-06-03 entries so reverse chronology is strict; Raw-source housekeeping remains consolidated at the foot. Line count: 2657 → 2676.
- `overview.md`: reconciled the hardware-validation observation to the exact current source count (257 curated sources).
- `index.md`: audited through `index_audit.py`; no edits needed.

### Audit results

- Raw/curated reconciliation: `curation_status.py --dupes` = 257 raw folders, 257 curated references, 0 genuinely new uncurated papers.
- Counts: `corpus_counts.py` = 257 sources / 272 concepts / 72 entities / 14 findings / 15 synthesis / 6 comparisons / 5 methodology / 5 queries / 3 thesis; `raw/sources` 257.
- Wording/index/frontmatter/link gates clean: `process_refs.py` 0 hits; `index_audit.py` 651/651 indexed, 0 missing, 0 duplicate primary listings; `frontmatter_audit.py` 649 pages, 0 errors; `linkcheck.py --orphans` no dangling links (5 orphans reported: MinerU_markdown_202605072001035_dfcfcb28, MinerU_markdown_202605131927481_3b25f7d3, README, full, schema).
- LLM Wiki API reachable on project `current`; graph 649 nodes / 6005 edges.

### Routing to mec-wiki-synthesizer

- No new synthesizer coverage gaps surfaced in this meta-doc-only batch.

## 2026-06-07 — Synthesize CTDE multi-agent DRL methodology

### Coverage added

- Methodology: [[ctde-multi-agent-drl-protocol]] maps the centralized-training / decentralized-execution engineering protocol across [[zhang-2025-mcma-task-migration]], [[peng-2025-drudm-cfg]], and [[kang-2023-mappo-hierarchical-aerial]], with [[qin-2025-bcuav-masac]] treated as a related MASAC/Lyapunov instantiation rather than a parse-labeled CTDE source.

### Connections and refreshes

- Added the new methodology page to `wiki/index.md` and refreshed `wiki/overview.md` analytical-layer counts from 4 to 5 methodology pages.
- Linked the CTDE concept page, CTDE backbone comparison, and the three explicit CTDE source pages to the new protocol page.
- Clarified the overview's CTDE observation so [[zhang-2025-ssac-mgi-heterogeneous-uav]] is correctly treated as the DTDE contrast case.

### Verification

- `python tools/wiki/curation_status.py --dupes`: 257 raw folders, 257 curated, 0 genuinely new uncurated papers.
- `python tools/wiki/corpus_counts.py`: sources 257, concepts 272, entities 72, findings 14, synthesis 15, comparisons 6, methodology 5, queries 5, thesis 3, raw/sources 257.
- `python tools/wiki/linkcheck.py`: no dangling links.
- `python tools/wiki/process_refs.py`: 0 files affected, 0 hits.
- `python tools/wiki/frontmatter_audit.py --type methodology`: 5 pages checked, 0 errors.
- `python tools/wiki/index_audit.py`: 651 catalogue-able pages, 651 indexed, 0 missing, 0 duplicate primary listings.
- LLM Wiki graph: 649 nodes, 6005 edges.

## 2026-06-04 — Curate 1 new source (batch 8/8): URLLC-NOMA-UAV-ISCC + audit

### Curated (1 source)

- [[qin-2025-urllc-noma-uav-iscc]] — Qin et al. 2025, *IEEE TVT*, DOI `10.1109/TVT.2024.3460813`. NOMA-aided UAV ISCC network: joint sensing + communication + edge computing with URLLC constraints. Lyapunov extreme-value tail-constraint decoupling + SAC-TPBD DRL for trajectory + beamforming; convex resource allocation. Comparable to SCA/SDR baselines with higher efficiency; significant queue-backlog reduction; SAC faster convergence + lower variance than baseline DRL.

### New concepts

None — all referenced concepts mapped to existing slugs ([[integrated-sensing-computation-communication]], [[finite-blocklength-urllc]], [[lyapunov-optimization]], [[soft-actor-critic]], [[uav-trajectory-control]]).

### Audit notes

- DOI verified in parse: TVT.2024.3460813 confirmed.
- Venue confirmed: IEEE TVT.
- `linkcheck.py` → NO DANGLING LINKS. `process_refs.py` → clean.
- Source count updated in `overview.md`: 256 → 257.

## 2026-06-04 — Curate 6 new sources (batch 7/8): marine-FL-DT-secrecy, GAI-diffusion-SemCom, SAGIN-spherical-SG, SAGIN-IoT-RL, TTW-AMD-localization, UAV-hotspot-offloading + audit

### Curated (6 sources)

- [[qian-2024-marine-fl-dt-secrecy]] — Qian et al. 2024, *IEEE IoT-J*, DOI `10.1109/JIOT.2023.3305711`. FL-assisted marine digital twin with secrecy; USV NOMA model-upload to HAP + chaotic spread-spectrum HAP broadcast; energy minimization via layered decomposition; NOMA > TDMA.
- [[zhang-2025-gsc-diffusion-semcom]] — Zhang et al. 2025, *IEEE TCCN*, DOI `10.1109/TCCN.2025.3526839`. GAI Semantic Communication (GSC): Swin Transformer encoder + diffusion model decoder for image; +17.75% PSNR in AWGN / +20.84% in Rayleigh vs DeepJSCC; MU-GSC multi-user extension.
- [[liu-2024-sagin-spherical-sg-connectivity]] — Liu et al. 2024, *IEEE JSAC*, DOI `10.1109/JSAC.2024.3365891`. Spherical stochastic geometry model for SAGIN uplink path connectivity; three connectivity metrics; first such analytical model; simulations confirm accuracy.
- [[cheng-2019-sagin-iot-offloading-rl]] — Cheng et al. 2019, *IEEE JSAC*, DOI `10.1109/JSAC.2019.2906789`. First SAGIN computing-offloading paper for remote IoT; UAV edge + satellite cloud; MDP + actor-critic RL; near-optimal VM allocation heuristic.
- [[wang-2024-ttw-amd-localization]] — Wang et al. 2024, *IEEE JSAC*, DOI `10.1109/JSAC.2023.3322819`. Through-the-wall passive AMD detection + localization via CSI; T-DeLo system: reference-channel SSI cancellation + 2D matrix pencil ToF/PLCR estimation; hardware-validated (glass: 0.964 detection, 1.65 m median error; brick: 0.952, 2.05 m).
- [[lyu-2018-uav-hotspot-offloading]] — Lyu et al. 2018, *IEEE TWC*, DOI `10.1109/TWC.2018.2818734`. UAV-aided cellular hotspot offloading: cyclical trajectory + bandwidth + user partitioning for max-min throughput; spectrum reuse > orthogonal; outperforms small-cell baseline.

### New concepts

None — all referenced concepts mapped to existing slugs.

### Audit notes

- DOIs verified in parse for all 6 sources.
- Venues confirmed: IEEE IoT-J, IEEE TCCN, IEEE JSAC (×3), IEEE TWC — all confirmed.
- `linkcheck.py` → NO DANGLING LINKS. `process_refs.py` → clean.
- Source count updated in `overview.md`: 250 → 256.

## 2026-06-04 — Curate 6 new sources (batch 6/8): Fed-IDCCO-IoV, WPT-MEC, dual-UAV-secure-MEC, CTMiG-task-migration, UABS-V2X-3DQN, UAV-heading-SDMA + audit

### Curated (6 sources)

- [[huang-2024-fed-idcco-iov-caching]] — Huang et al. 2024, *IEEE TVT*, DOI `10.1109/TVT.2024.3429507`. Joint data caching + computation offloading in UAV-assisted IoV; **DRL + federated learning** (Fed-IDCCO); minimizes delay + maximizes cache hit ratio; FL accelerates convergence + protects privacy.
- [[wang-2018-wpt-mec-joint-offloading]] — Wang et al. 2018, *IEEE TWC*, DOI `10.1109/TWC.2017.2785305`. **Wireless-powered MEC**: joint energy beamforming + partial offloading + CPU freq + TDMA time allocation; minimizes AP energy; local computing always beneficial at optimum; semi-closed-form optimal solution.
- [[xu-2021-secure-uav-mec-dual-uav]] — Xu et al. 2021, *IEEE TCOMM*, DOI `10.1109/TCOMM.2020.3025910`. **Dual-UAV secure MEC** (server + jammer UAV); first secure-computing-capacity metric in UAV-MEC; TDMA (BCD) + NOMA (P-BCD); NOMA > TDMA for security; partial offloading best.
- [[wang-2025-ctmig-task-migration-uav]] — Wang et al. 2025, *IEEE TSC*, DOI `10.1109/TSC.2025.3576644`. **CTMiG/ILCTS** — joint task offloading + migration in multi-UAV MEC; improved PPO for expert data + GAIL online refinement; large-result A2G delivery latency as primary concern.
- [[spampinato-2025-uabs-v2x-3dqn-ilp]] — Spampinato et al. 2025, *IEEE TVT*, DOI `10.1109/TVT.2024.3454955`. UABS trajectory (**3DQN**) + **ILP** RRM for V2X extended-sensing in urban Bologna scenario; SUMO mobility; coverage-limited + capacity-limited scenarios evaluated.
- [[jiang-2012-uav-heading-sdma]] — Jiang & Swindlehurst 2012, *IEEE JSAC*, DOI `10.1109/JSAC.2012.120614`. Multi-antenna fixed-wing UAV **heading optimization** for ground-to-air SDMA uplink; ergodic sum rate + prediction filter; SDMA >> TDMA; asymptotic low/high-SNR simplified algorithms.

### New concepts

None — all referenced concepts mapped to existing slugs.

### Audit notes

- DOIs verified in parse for all 6 sources.
- Venues confirmed: IEEE TVT (×2), IEEE TWC, IEEE TCOMM, IEEE TSC, IEEE JSAC — all confirmed.
- wang-2025-ctmig publication date 8 August 2025 is future relative to today; flagged as indicative.
- 1 residual dangling link in log.md fixed (hybrid_near_far_field reference in batch-5 audit note removed wikilink markup).
- `linkcheck.py` → NO DANGLING LINKS. `process_refs.py` → clean.
- Source count updated in `overview.md`: 244 → 250.

## 2026-06-04 — Curate 6 new sources (batch 5/8): DQN, GAI-SemCom-survey, GAI-PLS-survey, THz-UM-MIMO-CE, IRS-beamforming, UAV-altitude-beamwidth + audit

### Curated (6 sources)

- [[mnih-2015-dqn-atari]] — Mnih et al. 2015, *Nature*. DOI not in parse. Foundational **DQN** paper: deep convolutional Q-learning + experience replay + target network; human-level control across 49 Atari games with a single algorithm/architecture.
- [[liang-2025-gai-semcom-survey]] — Liang et al. 2025, *IEEE TCCN*, DOI `10.1109/TCCN.2024.3435524`. Survey of **GAI-driven SemCom networks**: three-plane architecture, multimodal transceiver design, information-effectiveness metrics, knowledge management (construction/update/sharing), use cases.
- [[zhao-2025-gai-pls-survey]] — Zhao et al. 2025, *IEEE TCCN*, DOI `10.1109/TCCN.2024.3438379`. Survey of **GAI for physical-layer security**: GANs/AEs/VAEs/diffusion models applied to confidentiality, authentication, availability, resilience, integrity.
- [[li-2025-thz-um-mimo-ce-hybrid-field]] — Li & Madhukumar 2025, *IEEE TWC*, DOI `10.1109/TWC.2024.3514141`. **Hybrid near- and far-field THz UM-MIMO CE**: BD-ODL dictionary learning + Bayesian CSCE + BCRB; significant NMSE improvement; converges within ~10 iterations.
- [[wu-2019-irs-joint-beamforming]] — Wu & Zhang 2019, *IEEE TWC*, DOI `10.1109/TWC.2019.2936025`. Foundational **IRS paper**: joint active AP + passive IRS beamforming for power minimization; asymptotic O(M²) gain; IRS matches massive MIMO with far fewer RF chains.
- [[he-2018-uav-altitude-beamwidth]] — He et al. 2018, *IEEE LCOMM*, DOI `10.1109/LCOMM.2017.2772254`. Joint **UAV altitude + beamwidth optimization** for multiuser communications (MC/BC/MAC); fly-hover-and-communicate; optimal pair differs by communication model.

### New concepts

None — all referenced concepts mapped to existing slugs.

### Audit notes

- DOIs verified in parse: TCCN.2024.3435524, TCCN.2024.3438379, TWC.2024.3514141, TWC.2019.2936025, LCOMM.2017.2772254 — all confirmed. Nature DQN paper: DOI not in parse.
- Venues confirmed in parse: Nature, IEEE TCCN (×2), IEEE TWC (×2), IEEE LCOMM.
- One dangling link fixed (hybrid_near_far_field removed from THz page).
- One process-narration leak fixed ("batch 7/8" in liang-2025 Relation section, replaced with evergreen phrasing).
- `linkcheck.py` → NO DANGLING LINKS. `process_refs.py` → clean.
- Source count updated in `overview.md`: 238 → 244.

## 2026-06-04 — Curate 6 new sources (batch 4/8): multi-user-offloading-game, UAV-WSN-data-collection, UAV-MEC-ADMM, UAV-MEC-NOMA-OMA, IRS-UAV-SWIPT-DRL, GAI-RIS-resource-mgmt + audit

### Curated (6 sources)

- [[chen-2016-multiuser-offloading-game-mec]] — Chen et al. 2016, *IEEE/ACM ToN*, DOI `10.1109/TNET.2015.2487344`. Multi-user offloading game for mobile-edge cloud computing in multi-channel wireless interference + contention environments; NP-hard centrally; **potential game** → NE always exists; distributed algorithm with bounded convergence time.
- [[zhan-2018-uav-wsn-data-collection]] — Zhan et al. 2018, *IEEE WCL*, DOI `10.1109/LWC.2017.2776922`. UAV mobile data collector for WSN; joint wake-up schedule + trajectory to minimize max SN energy; general fading channel + outage constraint; SCA iterative algorithm; significant savings vs. static/straight-line benchmarks.
- [[li-2020-energy-efficient-uav-mec-admm]] — Li et al. 2020, *IEEE TVT*, DOI `10.1109/TVT.2020.2968343`. UAV-mounted cloudlet EE maximization; Dinkelbach + SCA + **ADMM** distributed decomposition; Gaussian KDE user-mobility prediction.
- [[ji-2021-uav-mec-noma-oma-energy-min]] — Ji et al. 2021, *IEEE IoT-J*, DOI `10.1109/JIOT.2020.3046788`. UAV-MEC weighted-sum energy minimization under partial offloading with OMA and NOMA; block alternating descent + SCA; OMA achieves lower total energy than NOMA in this setting.
- [[chhea-2025-irs-uav-swipt-drl]] — Chhea et al. 2025, *IEEE TVT*, DOI `10.1109/TVT.2024.3519591`. IRS-aided UAV SWIPT network; **DRL** with SINR-map bivariate-normal reward; maximizes average EE over trajectory + IRS phase shifts + transmit power + PS ratio.
- [[wu-2025-gai-ris-resource-management]] — Wu et al. 2025, *IEEE TCCN*, DOI `10.1109/TCCN.2024.3519384`. **GAI + distributional RL (DBRL)** with GAN-modeled distributional Q-function for RIS-aided 6G resource management; CDL cascade channel estimation; maximizes joint EE + QoSSR.

### New concepts

None — all referenced concepts mapped to existing slugs ([[potential-game]], [[nash-equilibrium]], [[uav-data-collection]], [[uav-trajectory-control]], [[alternating-direction-method-of-multipliers]], [[task-offloading]], [[binary-vs-partial-offloading]], [[simultaneous-wireless-information-and-power-transfer]], [[active-ris]], [[distributional-reinforcement-learning]], [[generative-diffusion-model]]).

### Audit notes

- DOIs verified in parse for all 6 sources.
- Venues verified: IEEE/ACM ToN, IEEE WCL, IEEE TVT (×2), IEEE IoT-J, IEEE TCCN — all confirmed.
- Haijun Zhang in [[wu-2025-gai-ris-resource-management]] shares affiliation/name with [[wang-2025-maddpg-lc-dynamic-trajectory]] — flagged for human confirmation before entity page creation.
- `linkcheck.py` → NO DANGLING LINKS.
- `process_refs.py` → clean.
- Source count updated in `overview.md`: 232 → 238.

## 2026-06-04 — Curate 6 new sources (batch 3/8): DNN-VEC-diffusion, decentralized-offloading-game, DCBF-WSN-survey, drone-small-cells, multi-UAV-coverage, dynamic-trajectory-flight-dynamics + audit

### Curated (6 sources)

- [[liu-2025-mad2rl-dnn-vec]] — Liu et al. 2025, *IEEE TMC*, DOI `10.1109/TMC.2024.3486728`. DNN partitioning + task offloading in vehicular edge computing (VEC); **MAD2RL** = Lyapunov decoupling + diffusion-model-based MARL (first integration of diffusion model in MARL, claimed) + convex resource-allocation subroutine; simulated on OpenStreetMap/SUMO with VGG16/ResNet18.
- [[chen-2015-decentralized-offloading-game]] — Chen 2015, *IEEE TPDS*, DOI `10.1109/TPDS.2014.2316834`. Mobile cloud computing; decentralized computation offloading game; **potential-game** structure → NE always exists; decentralized mechanism converges in O(N log N); PoA ≤ ~10% vs centralized optimum.
- [[jayaprakasam-2017-dcbf-wsn-survey]] — Jayaprakasam et al. 2017, *IEEE COMST*, DOI `10.1109/COMST.2017.2720690`. Survey of **distributed and collaborative beamforming (DCBF)** in WSNs: four research directions (beampattern, power/lifetime, synchronization, prototypes); N²-fold received-power gain anchor.
- [[mozaffari-2015-drone-small-cells]] — Mozaffari et al. 2015, *IEEE GLOBECOM*. DOI not in parse. Drone-small-cell optimal altitude (proven unique analytically) + two-DSC optimal distance in interference-free and full-interference scenarios.
- [[mozaffari-2016-efficient-multi-uav-coverage]] — Mozaffari et al. 2016, *IEEE LCOMM*, DOI `10.1109/LCOMM.2016.2578312`. Multi-UAV coverage probability + **circle-packing** deployment for M UAVs; non-overlap altitude upper bound; minimum-UAV-count formula.
- [[wang-2025-maddpg-lc-dynamic-trajectory]] — Wang et al. 2025, *IEEE TVT*, DOI `10.1109/TVT.2024.3485182`. Multi-UAV MEC with explicit **UAV flight-dynamics** constraints; **MADDPG-LC** = MADDPG desired-trajectory + LQR tracking control + CVXPY resource allocation + blockchain security.

### New concepts

None — all referenced concepts mapped to existing slugs ([[vehicular-mec]], [[dnn-model-partition]], [[lyapunov-optimization]], [[diffusion-model-as-optimizer]], [[potential-game]], [[nash-equilibrium]], [[collaborative-beamforming]], [[drone-cell-3d-placement]], [[air-to-ground-channel-model]], [[maddpg]], [[centralized-training-decentralized-execution]], [[blockchain-for-fl-aggregation]], [[uav-trajectory-control]]).

### Audit notes

- DOIs verified in parse: TMC.2024.3486728, TPDS.2014.2316834, COMST.2017.2720690, LCOMM.2016.2578312, TVT.2024.3485182. GLOBECOM 2015 DOI not in parse — left as `not in parse`.
- Venues verified in parse: IEEE TMC, IEEE TPDS, IEEE COMST, IEEE GLOBECOM, IEEE LCOMM, IEEE TVT — all confirmed.
- `linkcheck.py` → NO DANGLING LINKS.
- `process_refs.py` → clean.
- Source count updated in `overview.md`: 226 → 232.

## 2026-06-04 — Synthesis pass (no new papers): +1 methodology + 2 theses (grow the thin types) + cross-links

Coverage-growth pass over the **current** corpus (no new raw papers), targeting the chronically under-grown derived types — **methodology** (was 3) and **thesis** (was 1) — per the updated Phase A page-type-balance / thesis-gap guidance (agent file `4e967a9`). Phase 0 reconciliation (`curation_status.py --dupes`): **214 raw folders = 214 curated, 0 uncurated, 0 genuinely-new, 0 duplicate MinerU ingests** — nothing to route to `mec-wiki-curator`. Tree clean at `4e967a9`; LLM Wiki API reachable (`/health` ok, v0.4.16, `allowUnauthenticated`); baseline graph **592 nodes / 5487 edges**. Built on the prior pass's two new pages (`swarm-metaheuristics-in-uav-mec`, `ctde-actor-critic-backbones-in-mec`, committed `0515997`) rather than re-deriving them. Candidates mined from existing synthesis/comparison pages (the protocols/positions described *in passing* there but lacking their own page).

### Coverage added (3 derived pages)

- **methodology [[discrete-continuous-two-stage-decomposition]]** — the discrete-then-continuous solver protocol generalizing [[two-stage-decomposition]] from concept to engineering protocol: Stage-1 solver menu (matching / metaheuristic / discrete-policy), Stage-2 menu (convex/quasi-convex/PGD / continuous-policy), the two information-seam styles (frozen hand-off vs CTDE conditioned observation), and the limitations. Grounded in [[wang-2026-aerial-marine-msar]] (matching + quasi-convex/PGD/convex), [[nabi-2025-jour-hierarchical-aerial]] (Gale-Shapley GOUA + ESAC), [[jia-2025-dro-uav-hap-mec]] (BWOA + CVX), [[zhang-2025-mcma-task-migration]] (MAPPO + MADDPG, conditioned). Third solver-protocol methodology alongside [[ao-sdr-sca-convex-pipeline]] and [[lyapunov-guided-drl]].
- **thesis [[decomposition-beats-end-to-end-drl-in-mec]]** (`confidence: medium`, `status: supported`) — design-philosophy position that decomposition-based solvers beat truly end-to-end DRL for joint MEC optimization. Supporting evidence: the high-confidence absence finding [[no-true-end-to-end-drl-in-corpus]], the [[end-to-end-vs-decomposition-in-drl-mec]] structural argument, the two decomposition methodology pages, and [[hybrid-action-beats-pure-drl]]. Not `settled`: no counterfactual experiment (the open question in [[end-to-end-drl-feasibility-large-scale-mec]]), corpus predates transformer-policy wave. Refutation conditions named.
- **thesis [[explicit-constraints-beat-reward-shaping-in-mec-drl]]** (`confidence: medium`, `status: supported`) — position that explicit constraint-handling (gated safety override, Lyapunov virtual queue, DRO/robust reformulation) beats folding constraints into the reward. Supporting evidence: the [[safety-and-robustness-mechanisms-in-mec]] "reward shaping is the rejected baseline twice over" reading, [[collision-avoidance-mgi|MGI]] hard-safety ([[zhang-2025-ssac-mgi-heterogeneous-uav]]), the six [[lyapunov-guided-drl]] sources, the robustness sources ([[li-2024-robust-bmappo-multiuav-mec]], [[jia-2025-dro-uav-hap-mec]]), and the [[drl-backbones-across-uav-mec-sources]] distilled recommendation. Not `settled`: structural not head-to-head, single-source anchors for the strongest claims. Refutation conditions named.

### Connections added (bidirectional)

- Methodology page wired reciprocally into [[two-stage-decomposition]] (concept), [[ao-sdr-sca-convex-pipeline]] + [[lyapunov-guided-drl]] (sibling methodology cross-refs), [[drl-vs-evolutionary-vs-classical-solvers]] + [[drl-backbones-across-uav-mec-sources]] (See-also / related), and its four instantiating source pages ([[wang-2026-aerial-marine-msar]], [[nabi-2025-jour-hierarchical-aerial]], [[jia-2025-dro-uav-hap-mec]], [[zhang-2025-mcma-task-migration]]).
- `decomposition-beats-end-to-end` wired into [[no-true-end-to-end-drl-in-corpus]], [[end-to-end-vs-decomposition-in-drl-mec]], [[end-to-end-drl-feasibility-large-scale-mec]], [[two-stage-decomposition]], [[hybrid-action-beats-pure-drl]], and [[drl-vs-evolutionary-vs-classical-solvers]].
- `explicit-constraints-beat-reward-shaping` wired into [[safety-and-robustness-mechanisms-in-mec]], [[lyapunov-guided-drl]], [[collision-avoidance-mgi]], and [[drl-backbones-across-uav-mec-sources]] (recommendation 3). `updated` bumped only on pages actually edited.

### Grounding (correctness-first)

- Every methodology roster row cross-checked against the source pages (audited-clean) and, for the seam claim, the parse phrasing: [[zhang-2025-mcma-task-migration]]'s "keeps each stage's action space homogeneous (all-discrete vs all-continuous)" and its MAPPO-then-MADDPG-conditioned split; [[nabi-2025-jour-hierarchical-aerial]]'s GOUA + ESAC frozen hand-off; [[wang-2026-aerial-marine-msar]]'s four-subproblem JCORA (matching + quasi-convex + PGD + convex); [[jia-2025-dro-uav-hap-mec]]'s BWOA-after-primal-decomposition + CVX. The [[zhu-2025-lycnn-drl-wpt-mec]] ">97% of LyCD utility while significantly reducing execution time" claim re-verified verbatim in its parse (referenced via the Lyapunov page, not re-stated as a new number).
- **Deliberately left out for lack of support:** (1) an *evolutionary design-recipe* methodology page (counterpart to [[design-recipe-multi-uav-mec]]) — the CMOEA lineage is one research group and the recipe would over-generalize from a single author network; deferred. (2) A *"DRL vs evolutionary head-to-head"* thesis — the corpus has **no** source running both families on one instance (the standing biggest evidentiary gap), so a thesis would be speculation, not an earned position; left as the existing open question. (3) A *"MASAC beats MADDPG"* thesis — already covered by the [[maddpg-vs-masac-in-mec]] synthesis's working-thesis section; promoting it to a `thesis/` page would duplicate, not add. (4) New entity pages — no clearly-recurring unrepresented author surfaced in this slice; not forced. No tag-vocabulary normalizations (standing family-tag-fragmentation notes remain deferred, better batched on their own).

### Counts

`corpus_counts.py`: methodology **3→4**, thesis **1→3** (sources 214 / concepts 260 / entities 71 / findings 14 / synthesis 15 / comparisons 6 / queries 5 unchanged). [[overview]] Snapshot + analytical-layer line + observation #4 and [[index]] Methodology + Thesis sections updated to match.

### Gates

`linkcheck.py` = **NO DANGLING LINKS**; `process_refs.py` = **0 files / 0 hits**; `index_audit.py` = 594/594 indexed, 0 unindexed / 0 duplicate primaries (45 cross-ref mentions informational); `frontmatter_audit.py` = 592 pages, 0 errors. New pages + edited meta docs mojibake-free at byte level (`fs_write`/`str_replace`, no shell redirection; em-dash byte check clean). Graph 592 nodes / 5487 edges baseline (the 3 new pages + reciprocal links register on the next rescan).

### Toolkit

No ratchet needed — `curation_status.py`, `corpus_counts.py`, `linkcheck.py`, `process_refs.py`, `index_audit.py`, and `frontmatter_audit.py` covered Phase 0 state detection, count reconciliation, and all commit gates. No reusable one-off arose; the toolkit is stable and unchanged this pass.

## 2026-06-03 — Curate 6 new sources (batch 2/8): resumed interrupted run — hybrid cloud-edge LEO offloading, communication-constrained MARL, MEC+DRL-in-NTN survey, ground-satellite UAM scheduling, cooperative UAV-RIS, covert mmWave + audit

**Resumed an interrupted curation run** (a prior batch-2 invocation was cut off by a network issue, leaving uncommitted partial work in the tree). This is **batch 2/8** of the 43-paper run (`make_batches.py` plan in `.curation-out/batches.json`); batch 1 committed at `dd019c9`. Resume reconciliation: HEAD still at `dd019c9`; `git status` showed the in-flight set = the 6 source pages of `batches.json["batch2"]` + 5 concept pages + 2 modified entity rosters. The stale `.curation-out/batch2of8-decisions.md` describes a *different* paper set (an old `batches-remaining.json` plan) and was ignored in favor of `batches.json` + the on-disk in-flight pages; `.curation-out/batch2-actual-decisions.md` is the authoritative record.

### Reconciliation of the in-flight (uncommitted) work

The interrupted invocation had already written, correctly and groundedly: all 6 source pages, 5 concept pages ([[covert-communication]], [[urban-air-mobility]], [[communication-constrained-marl]], [[non-dominated-sorting-genetic-algorithm]], [[uav-mounted-ris]]), and had bumped 2 author rosters ([[geng-sun]], [[yanheng-liu]]). It had **not** finished: 3 more author rosters ([[dusit-niyato]], [[qingqing-wu]], [[zhu-han]] — flagged by `entity_roster_audit.py` as present-but-unlisted omissions), `index.md` cataloguing (6 sources + 5 concepts), the [[overview]] Snapshot counts + track tables, or this log entry. This pass verified the in-flight pages against their parses and completed the unfinished roster/navigation/log work rather than re-curating. No new entity pages warranted (all genuinely-new authors appear once; foundational-method conservatism preserved).

### Curated (6 sources)

- [[tang-2021-cecls-hybrid-cloud-edge]] — Tang et al. 2021, *IEEE IoT-J*, DOI `10.1109/JIOT.2021.3056569`. Hybrid cloud-and-edge LEO satellite (**CECLS**) three-tier (user / LEO-edge / cloud) sum-energy minimization under coverage-time + LEO-compute caps; binary nonconvex → binary-relaxation LP → distributed **ADMM**.
- [[li-2024-smdrl-resource-constrained-mec]] — Li et al. 2024, *IEEE TMC*, DOI `10.1109/TMC.2024.3383041`. Computation offloading in bandwidth-constrained multi-access MEC; **SMDRL** (learned message encoding + TopK self-scheduling) + a virtual energy-deficit queue → per-slot QoE-max MDP.
- [[ullah-2026-mec-drl-ntn-survey]] — Ullah et al. 2026, *IEEE COMST*, DOI `10.1109/COMST.2025.3576571`. Survey of **DRL for MEC-empowered non-terrestrial wireless networks (MeNT-WiNs)**: AAV + LEO/GEO satellite + HAP; DRL fundamentals, offloading models (binary / partial / task-call-graph), and DRL across satellite autonomy, AAV-swarm management, resource/spectrum/energy allocation, routing, security.
- [[moon-2024-ground-satellite-uam-scheduling]] — Moon & Chae 2024, *IEEE JSAC*, DOI `10.1109/JSAC.2024.3460031`. Cooperative ground-satellite downlink scheduling + power allocation for **urban air mobility** in a 6G NTN; satellite absorbs high-interference UAMs, GS link association as a **minimum-cost max-flow** graph problem + SCA power allocation (MINLP). Communication-layer, not offloading.
- [[pan-2025-uav-ris-energy-efficient-comm]] — Pan et al. 2025, *IEEE TMC*, DOI `10.1109/TMC.2025.3579597`. Cooperative multiple **UAV-mounted RISs**; three-objective EEComm-MOF (max-min rate / max total rate / min energy) over BS beamforming + UAV-RIS 3D location + discrete phase shifts via **INSGA-II-CDC**.
- [[ma-2024-covert-mmwave-finite-blocklength]] — Ma et al. 2024, *IEEE IoT-J*, DOI `10.1109/JIOT.2023.3296414`. Covert **mmWave** with finite blocklength vs spatially-random wardens (PPP); stochastic-geometry covertness + AECT for PA/LFDA beamforming; jointly optimizes transmit power + blocklength.

### New vocabulary (5 concepts, no new entities)

- Concepts: [[covert-communication]] (hiding a transmission's *existence*; anchors [[ma-2024-covert-mmwave-finite-blocklength]]), [[urban-air-mobility]] (UAM as SAGIN edge user; anchors [[moon-2024-ground-satellite-uam-scheduling]]), [[communication-constrained-marl]] (inter-agent channel as a scarce resource; anchors [[li-2024-smdrl-resource-constrained-mec]]), [[non-dominated-sorting-genetic-algorithm]] (NSGA-II MOEA; anchors [[pan-2025-uav-ris-energy-efficient-comm]]), [[uav-mounted-ris]] (RIS carried by a UAV for 3D/opportunistic deployment; anchors [[pan-2025-uav-ris-energy-efficient-comm]]). Each grounded in its source(s) and cross-linked to existing vocabulary; no near-synonym duplicates created.
- Entities: none. All genuinely-new authors (Tang, Fei, Bin Li, Kexin Li, Moon, Chae, Pan, Gong, P. Wang, Ma, et al.) appear once → not promoted, consistent with house conservatism.

### Rosters / navigation finished this pass

- Author rosters updated to add the new sources: [[dusit-niyato]] (27→28), [[qingqing-wu]] (10→11), [[zhu-han]] (7→8) — completing the 3 the interrupted run had missed ([[geng-sun]] and [[yanheng-liu]] were already bumped in the in-flight tree). Affiliations re-verified against the parses (Niyato→NTU, Wu→SJTU, Han→Univ. of Houston / Kyung Hee). `entity_roster_audit.py` now reports **0 over-claims / 0 omissions**.
- [[index]]: all 6 sources filed (Foundational surveys; SAGIN/satellite ×2; IRS/sensing; Energy efficiency & WPT; MEC/MCC fundamentals) + 5 concepts catalogued (Aerial architectures ×2; DRL backbones; Optimization techniques; Sensing & security). `index_audit.py` = 619/619 indexed.
- [[overview]]: Snapshot counts updated + track tables (Foundational surveys 24→25, SAGIN/satellite, ISAC/sensing/PLS 14→15, Energy efficiency & WPT, MEC/MCC fundamentals 8→9).

### Counts

`corpus_counts.py`: sources **220→226**, concepts **267→272**, entities **72** unchanged (findings 14 / synthesis 15 / comparisons 6 / methodology 4 / queries 5 / thesis 3 unchanged). `raw/sources` 257.

### Grounding (correctness-first)

- All 6 DOIs verified verbatim against the parse `Digital Object Identifier` lines. Years recorded per the date-of-current-version convention in each Citation block: tang-2021 (current version May 2021), li-2024 (Oct 2024), ullah **2026** (current version 2 Jan 2026, COMST early-access in 2025), moon-2024 (Dec 2024), pan-2025 (Sep 2025), ma-2024 (current version 8 Jan 2024). [[pan-2025-uav-ris-energy-efficient-comm]] headline numbers cross-checked verbatim against the parse abstract + conclusion + Tables III/IV (5-GU: +74.62% / +64.45% / −10.55%; 10-GU: +43.75% / +89.57% / −13.60%), flagged as best-benchmark-relative Pareto advantage rather than absolute optimality. Figure-derived magnitudes flagged indicative on the source pages.

### Gates

`linkcheck.py` = **NO DANGLING LINKS**; `process_refs.py` = **0 files / 0 hits**; `index_audit.py` = 619/619 indexed, 0 unindexed / 0 duplicate primaries; `frontmatter_audit.py` = 617 pages, 0 errors; `entity_roster_audit.py` = 0 over-claims / 0 omissions.

### Toolkit

No ratchet needed — `curation_status.py`, `corpus_counts.py`, `linkcheck.py`, `process_refs.py`, `index_audit.py`, `frontmatter_audit.py`, and `entity_roster_audit.py` covered resume-state reconciliation, count reconciliation, and all commit gates. No reusable one-off arose; the toolkit is stable and unchanged this pass.

### Remaining

Batches **3/8 – 8/8** (31 sources) remain uncurated, one batch per fresh invocation. Next invocation should curate **batch 3** from `.curation-out/batches.json`: `DNN_Partitioning_Task_Offloading_and_Resource_Allocation_in_Dynamic_Vehicular_Networks_A_Lyapunov-Guided_Diffusion-Based_Reinforcement_Learning_Approach`, `Decentralized_Computation_Offloading_Game_for_Mobile_Cloud_Computing`, `Distributed_and_Collaborative_Beamforming_in_Wireless_Sensor_Networks_Classifications_Trends_and_Research_Directions`, `Drone_Small_Cells_in_the_Clouds_Design_Deployment_and_Performance_Analysis`, `Dynamic_Trajectory_Design_for_Multi-UAV-Assisted_Mobile_Edge_Computing`, `Efficient_Deployment_of_Multiple_Unmanned_Aerial_Vehicles_for_Optimal_Wireless_Coverage`.

## 2026-06-03 — Curate 6 new sources (batch 1/8): resumed interrupted run — graph-RM survey (I+II), data-driven IoT CB, DT migration, laser air-ground MEC, STIN delay offloading + audit

**Resumed an interrupted curation run** (a prior invocation was cut off by a network issue, leaving uncommitted partial work in the tree). A new batch of **43 genuinely-new raw sources** is being curated across **8 invocations** (`make_batches.py --size 6` plan in `.curation-out/batches.json`); this entry is **batch 1/8**. Resume reconciliation at `c29d71d`: `curation_status.py --dupes` reported 37 uncurated / 0 duplicate MinerU ingests *after* counting the 6 in-flight source pages already on disk, confirming the in-flight set = batch 1 of the plan (the stale `batches-remaining.json` is from the *previous* completed 43-paper run and was ignored in favor of `batches.json`).

### Reconciliation of the in-flight (uncommitted) work

The interrupted invocation had already written, correctly and groundedly: 6 source pages, 7 concept pages, 1 entity page, and had bumped the [[overview]] Snapshot counts (214→220 / 260→267 / 71→72) + 4 author rosters ([[geng-sun]], [[hui-kang]], [[jiahui-li]], [[yuan-wu]]). It had **not** finished: `index.md` cataloguing (14 new pages), 4 more author rosters, the [[overview]] track tables, or this log entry. This pass verified the in-flight pages against their parses and completed the unfinished navigation/roster/log work rather than re-curating.

### Curated (6 sources)

- [[dai-2024-graph-rm-survey-optimization]] — Dai et al. 2024, *IEEE TCCN*, DOI `10.1109/TCCN.2024.3508783`. **Part I** of the two-part graph-based-resource-management survey: graph-optimization tools (coloring / max-independent-set / max-flow / bipartite-stable matching) across cellular, D2D, multi-hop, multi-antenna, edge caching/computing, NTN.
- [[dai-2024-graph-rm-survey-learning]] — Dai et al. 2024, *IEEE TCCN*, DOI `10.1109/TCCN.2024.3508777`. **Part II**: GNN families for power control, spectrum, beamforming, scheduling, aerial coverage + consolidated challenges/future directions.
- [[li-2025-omrp-cb-iot]] — Li et al. 2025, *IEEE IoT-J*, DOI `10.1109/JIOT.2025.3553288`. Data-driven collaborative beamforming for **static ground IoT** (corpus's only ground-IoT CB entry): overlap-based routing (OMRP) + SoftPPO-LSTM CB-node selection; +17% lifetime / +8.3% throughput (parse-confirmed), Raspberry Pi 4B deployment.
- [[mou-2025-adm-dt-migration]] — Mou et al. 2025, *IEEE TVT*, DOI `10.1109/TVT.2024.3492349`. Adaptive digital-twin migration in vehicular edge networks; off-policy actor-critic warm-started on expert (Greedy) demonstrations; ~39% avg migration-latency reduction on Cologne traces (parse-confirmed).
- [[wang-2025-airground-laser-mec]] — Wang et al. 2025, *IEEE TVT*, DOI `10.1109/TVT.2024.3486036`. Laser-powered air-ground coordinated MEC (UAV = MEC server + relay, ground AP laser-charges it); LP task/EH-time allocation + DDPG trajectory (**LP-DDPG**).
- [[xie-2025-stin-delay-offloading]] — Xie et al. 2025, *IEEE TMC*, DOI `10.1109/TMC.2024.3479243`. LEO satellite-terrestrial offloading with **system state delay** as a first-class object: stochastic-delay MDP → augmented-state double DQN + RAMLFQ CPU queue; MINLP energy minimization.

### New vocabulary (7 concepts + 1 entity)

- Concepts: [[graph-based-resource-management]], [[graph-neural-network]], [[omrp-overlap-routing]], [[softppo-lstm]], [[hot-spot-problem-iot]], [[first-order-radio-energy-model]], [[expert-guided-warm-start-rl]] — each grounded in its source(s) and cross-linked to existing vocabulary ([[collaborative-beamforming]], [[ppo]], [[ddpg]], [[matching-theory-for-resource-allocation]], [[drl-backbones-across-uav-mec-sources]], [[service-migration]], [[vehicular-mec]], etc.). No near-synonym duplicates created.
- Entity: [[shuguang-cui]] (CUHK-Shenzhen; 7 sources across graph-RM survey, XL-MIMO, GAI/ISAC physical-layer, ISCC edge-AI, GDM tutorial).

### Rosters / navigation finished this pass

- Author rosters updated to add the new sources: [[dusit-niyato]] (26→27), [[jiacheng-wang]] (10→11), [[zemin-sun]] (6→7), [[xuemin-shen]] (9→11, both Dai surveys) — completing the 4 the interrupted run had missed (the other 4 — [[geng-sun]], [[hui-kang]], [[jiahui-li]], [[yuan-wu]] — were already bumped in the in-flight tree). `entity_roster_audit.py` now reports **0 over-claims / 0 omissions**.
- [[index]]: all 6 sources filed (Foundational surveys; Collaborative beamforming; Vehicular MEC; SAGIN/satellite; Energy efficiency & WPT), 7 concepts + 1 entity catalogued. `index_audit.py` = 608/608 indexed.
- [[overview]]: track tables updated (Foundational surveys 22→24, SAGIN, Vehicular MEC 8→9, Collaborative beamforming 10→11, Energy efficiency & WPT) to stay evergreen; Snapshot counts already reconciled in the in-flight tree.

### Counts

`corpus_counts.py`: sources **214→220**, concepts **260→267**, entities **71→72** (findings 14 / synthesis 15 / comparisons 6 / methodology 4 / queries 5 / thesis 3 unchanged). `raw/sources` 257.

### Grounding (correctness-first)

- All 6 DOIs verified verbatim against the parse `Digital Object Identifier` lines. Years: Part I/II = 2024; the four 2024-DOI TVT/TMC/IoT-J papers carry **date-of-current-version 2025** (Feb/Mar 2025) and are dated 2025 per the corpus convention, recorded explicitly in each Citation block. Headline numbers cross-checked against the parses ([[li-2025-omrp-cb-iot]] 17% / 8.3% in the abstract; [[mou-2025-adm-dt-migration]] ~39% in the abstract/contributions). Figure-derived magnitudes flagged indicative on the [[wang-2025-airground-laser-mec]] and [[xie-2025-stin-delay-offloading]] pages.

### Gates

`linkcheck.py` = **NO DANGLING LINKS**; `process_refs.py` = **0 files / 0 hits**; `index_audit.py` = 608/608 indexed, 0 unindexed / 0 duplicate primaries; `frontmatter_audit.py` = 606 pages, 0 errors; `entity_roster_audit.py` = 0 over-claims / 0 omissions. LLM Wiki API reachable (`/health` ok, v0.4.16, `allowUnauthenticated`) but the `/graph/stats` route returned `Not found` on this build — graph node/edge counts not captured this pass (not a correctness blocker).

### Toolkit

No ratchet needed — `curation_status.py`, `make_batches.py`, `corpus_counts.py`, `linkcheck.py`, `process_refs.py`, `index_audit.py`, `frontmatter_audit.py`, and `entity_roster_audit.py` covered resume-state reconciliation, count reconciliation, and all commit gates. No reusable one-off arose; the toolkit is stable and unchanged this pass.

### Remaining

Batches **2/8 – 8/8** (37 sources) remain uncurated, one batch per fresh invocation. Next invocation should curate **batch 2** from `.curation-out/batches.json`: `Computation_Offloading_in_LEO_Satellite_Networks_With_Hybrid_Cloud_and_Edge_Computing`, `Computation_Offloading_in_Resource-Constrained_Multi-Access_Edge_Computing`, `Convergence_of_MEC_and_DRL_in_Non-Terrestrial_Wireless_Networks_Key_Innovations_Challenges_and_Future_Pathways`, `Cooperative_Ground-Satellite_Scheduling_and_Power_Allocation_for_Urban_Air_Mobility_Networks`, `Cooperative_UAV-Mounted_RISs-Assisted_Energy-Efficient_Communications`, `Covert_mmWave_Communications_With_Finite_Blocklength_Against_Spatially_Random_Wardens`.

## 2026-06-03 — Synthesis pass (no new papers): +1 solver-family synthesis + 1 CTDE comparison + cross-links

Coverage-growth pass over the **current** corpus (no new raw papers). Phase 0 reconciliation (`curation_status.py --dupes`): **214 raw folders = 214 curated, 0 uncurated, 0 genuinely-new, 0 duplicate MinerU ingests** — nothing to route to `mec-wiki-curator`. Tree clean at `628627a`; LLM Wiki API reachable (`/health` ok, v0.4.16, `allowUnauthenticated`); baseline graph **589 nodes / 5436 edges**. This pass acted on the two strongest standing concept-layer routing notes accumulated across the audit batches (recorded in `.curation-out/audit-coverage.md`): the **swarm-metaheuristic family** (reinforced in nearly every concept audit batch) and the **multi-agent actor-critic / CTDE family** (flagged in concept batches 7/10/11).

### Coverage added (2 derived pages)

- **synthesis [[swarm-metaheuristics-in-uav-mec]]** — ties together the corpus's nine swarm-intelligence metaheuristic concept pages ([[particle-swarm-optimization|PSO]], [[whale-optimization-algorithm|WOA]], [[binary-whale-optimization|BWOA]], [[salp-swarm-algorithm|SSA]], [[multi-verse-optimizer|MVO]], [[ant-lion-optimizer|ALO]], [[gravitational-search-algorithm|GSA]], [[ant-colony-optimization|ACO]], [[self-adaptive-global-best-harmony-search|SGHS]]) plus the single-source mayfly (IMOMA in [[huang-2025-dual-aav-maritime-secure-cb]]), across ~14 sources. Maps the **two roles** (standalone multi-objective Pareto solver — almost all collaborative-beamforming, [[geng-sun]]-group concentrated; vs embedded single-objective sub-solver after a convex/Lyapunov/DRL layer), the **shared improved-variant toolkit** (chaos/OBL init + discrete/hybrid update operator + EC-style archive refinement), and the sources' own rationale for swarm-over-DRL/convex (grounded verbatim in [[zheng-2024-recmop-uav-cb]]). The metaheuristic deep-dive that [[drl-vs-evolutionary-vs-classical-solvers]] referenced but had no home for.
- **comparison [[ctde-actor-critic-backbones-in-mec]]** — the corpus's explicitly multi-agent CTDE cluster (11 sources): 5 MADDPG ([[seid-2021-madrl-multiuav-iot-edge]], [[peng-2020-maddpg-uav-vehicular]], [[wang-2021-maddpg-multiuav-trajectory]], [[he-2023-fairness-3d-multiuav-maddpg]], [[du-2023-maddpg-service-placement-agin]]), 2 MATD3 ([[zhao-2022-matd3-multiuav-ec-offloading]], [[shao-2024-drl-antijamming-mec]]'s PER-MATD3), MASAC ([[qin-2025-bcuav-masac]]), MAPPO ([[kang-2023-mappo-hierarchical-aerial]]), tabular MA-Q ([[li-2025-stochastic-game-uav-swarm]]), and value-decomposition VD3QN ([[raivi-2024-jdaco-postdisaster-iot]]). Maps backbone choice to action space + policy class + game structure. Distinct from the two-way [[maddpg-vs-masac-in-mec]] thesis (generalizes it to the whole family) and the [[drl-backbones-across-uav-mec-sources]] synthesis (which covers a different, mostly single-agent 2025–2026 roster). The +15.41%/−30.73%-vs-MADDPG figures carry the audited correct margins (not the PSO-baseline misquote).

### Connections added

- Reciprocal `related` links from all 8 swarm concept pages → [[swarm-metaheuristics-in-uav-mec]]; from the 6 CTDE concept pages ([[maddpg]], [[multi-agent-td3]], [[masac]], [[mappo]], [[multi-agent-q-learning]], [[centralized-training-decentralized-execution]]) → [[ctde-actor-critic-backbones-in-mec]].
- Cross-links + See-also entries wiring the two new pages into their sibling derived pages: swarm synthesis ↔ [[drl-vs-evolutionary-vs-classical-solvers]] / [[collaborative-beamforming-in-aerial-mec]] / [[cmop-evolutionary-uav-mec-lineage]]; CTDE comparison ↔ [[maddpg-vs-masac-in-mec]] / [[drl-backbones-across-uav-mec-sources]]. `updated` bumped only on pages actually edited.

### Grounding (correctness-first)

- Every roster row + claim cross-checked against audited-clean concept/source pages and, where a specific number or mechanism is cited, against the parse: the swarm two-role split and the "swarm over DRL/convex" rationale (verbatim in [[zheng-2024-recmop-uav-cb]]); the IMOMA-mayfly identification in [[huang-2025-dual-aav-maritime-secure-cb]] (not ALO — corrected against the parse before rostering); the MASAC vs MADDPG +15.41%/−30.73% margins (audited-correct, PSO-baseline distinction preserved); MATD3/PER-MATD3 framings ([[zhao-2022-matd3-multiuav-ec-offloading]], [[shao-2024-drl-antijamming-mec]]); VD3QN = VDN + dueling-double-DQN ([[raivi-2024-jdaco-postdisaster-iot]]).
- **Deliberately left out for lack of support:** [[albakhrani-2025-moalf-uav-mec]] kept as APSO-as-one-ingredient (multi-technique framework, not a standalone swarm result); [[mao-2025-bcsa-frl]] excluded from the CTDE roster (it is FRL parameter-aggregation, not a centralized critic). No tag-vocabulary normalizations performed this pass (the standing evolutionary-/generative-/CSI-/PLS-family tag-fragmentation notes are deferred — they touch many pages and are better batched on their own). Standing candidates not yet acted on: LEO/NTN concept cluster synthesis, caching cluster, channel-model cluster, game-theory-mechanisms synthesis, video-analytics cluster, secure-aggregation cluster, `j-ppo-vs-pdqn` already exists.

### Counts

`corpus_counts.py`: synthesis **14→15**, comparisons **5→6** (sources 214 / concepts 260 / entities 71 / findings 14 / methodology 3 / queries 5 / thesis 1 unchanged). [[overview]] Snapshot + analytical-layer line and [[index]] Synthesis + Comparisons sections updated to match.

### Gates

`linkcheck.py` = **NO DANGLING LINKS**; `process_refs.py` = **0 files / 0 hits**; `index_audit.py` = 591/591 indexed, 0 unindexed / 0 duplicate primaries (45 cross-ref mentions informational); `frontmatter_audit.py` = 589 pages, 0 errors. Both new pages + edited meta docs mojibake-free at byte level (`fs_write`, no shell redirection). Graph 589 nodes / 5436 edges baseline (the 2 new pages + reciprocal links register on the next rescan).

### Toolkit

No ratchet needed — `curation_status.py`, `corpus_counts.py`, `linkcheck.py`, `process_refs.py`, `index_audit.py`, and `frontmatter_audit.py` covered Phase 0 state detection, count reconciliation, and all commit gates. No reusable one-off arose; the toolkit is stable and unchanged this pass.

## 2026-06-03 — Audit pass (no new papers): close standing roster advisory + verify corpus

No-new-papers quality pass. Phase 0 reconciliation (`curation_status.py --dupes`): **214 raw folders = 214 curated, 0 uncurated, 0 genuinely-new** — nothing to route to `mec-wiki-curator`. Working tree opened with three uncommitted entity edits left from the prior session (the `wang-2024-wipe-gai` roster additions on [[jiacheng-wang]] / [[jiawen-kang]] / [[xuemin-shen]]); verified them against the parse and committed.

### Roster correctness (parse-grounded)

- [[jiacheng-wang]] (10), [[jiawen-kang]] (15), [[xuemin-shen]] (9) each gained [[wang-2024-wipe-gai]] in `related:` + the body roster, with the stated co-authored-source counts re-reconciled to the bullet lists. The WiPe-GAI parse author block grounds all three: Jiacheng Wang (NTU, first author, `jiacheng.wang@ntu.edu.sg`), Jiawen Kang (GDUT, **corresponding author**, `kavinkang@gdut.edu.cn`), Xuemin Shen (Waterloo, `sshen@uwaterloo.ca`). This clears the **3 standing present-but-unlisted advisories** that `entity_roster_audit.py` had been reporting on `wang-2024-wipe-gai` since the batch-1 curation; the source page's `related:` and [[dusit-niyato]]'s roster already carried the link, so this only completes the symmetry.

### Audit results

- **Raw/curated reconciliation:** 214 = 214, 0 uncurated, 0 duplicate MinerU ingests.
- **Meta docs:** `log.md` / `index.md` / `overview.md` reviewed — date headers, ordering, and the consolidated [Raw-source housekeeping](#raw-source-housekeeping) section are intact; Snapshot counts already exact (`corpus_counts.py`: 214 sources / 260 concepts / 71 entities / 14 findings / 14 synthesis / 5 comparisons / 3 methodology / 5 queries / 1 thesis). No meta-doc edits needed (idempotent — prior passes left them clean).
- **Correctness spot-checks (freshest sources):** [[du-2024-yolo-semcom-digital-twin]] re-verified against its parse — DOI 10.1109/JIOT.2023.3317629 verbatim; the 595.2 MB → 55.4 MB (54.8 MB image + 0.6 MB text) / **91%** communication-cost reduction and the η = 0.5/0.75/1 at 10/20/30 m crossover are verbatim; figure-derived MIST/SSIM/BER magnitudes correctly flagged indicative. [[wang-2024-wipe-gai]] DOI 10.1109/TMC.2024.3377226 + corresponding-author claim confirmed in-parse. No ungrounded numbers found.
- **Wording/evergreen:** `process_refs.py` = 0 files / 0 hits (no process-narration leaked into any non-`log.md` page).
- **Gates:** `linkcheck.py` = **NO DANGLING LINKS**; `process_refs.py` = 0/0; `index_audit.py` = 589/589 indexed, 0 unindexed / 0 duplicate primaries; `frontmatter_audit.py` = 587 pages, 0 errors (entity-typed 71, 0 errors); `entity_roster_audit.py` = **0 over-claims / 0 present-but-unlisted** (the 3 prior advisories now cleared). `corpus_counts.py` counts unchanged (audit-only, no new pages).
- **LLM Wiki API:** unreachable this pass (`/health` connection refused — desktop app not running). Degraded gracefully to local file/search tools per the read-only-optimization contract; graph node/edge stats not enumerated. Correctness was grounded in the parses and committed files throughout, not the index.

### Toolkit

No ratchet needed — `curation_status.py`, `corpus_counts.py`, `linkcheck.py`, `process_refs.py`, `index_audit.py`, `frontmatter_audit.py`, and `entity_roster_audit.py` covered the whole pass. No reusable one-off arose; the toolkit is stable and unchanged.

### Routing to mec-wiki-synthesizer

No new gaps surfaced this pass beyond the standing consolidation/synthesis candidates already recorded across the source/concept/entity audit batches in `.curation-out/audit-coverage.md` (swarm-metaheuristic family synthesis, hybrid-action family, game-theory-mechanisms, LEO/NTN cluster, caching cluster, channel-model cluster, multi-agent actor-critic comparison, and the standing tag-vocabulary normalizations). These remain `mec-wiki-synthesizer`'s to act on — not filled here.

## 2026-06-02 — Curation pass (SOURCE layer — multi-batch run batch 8/8: 1 new source; +1 concept) — RUN COMPLETE

Eighth and **final** batch of the multi-invocation curation run over the 37 papers planned in `.curation-out/batches-remaining.json` (the `batch7` key there — a single paper). Phase 0 reconciliation (`curation_status.py --dupes`): **214 raw folders, 213 curated, 1 uncurated, 0 duplicate MinerU ingests**; HEAD synced with origin/main (`e937338`), working tree clean apart from the one uncurated raw folder + app-generated `wiki/media/`. The batch paper had no existing source page. `.curation-context.md` was absent this session, so the extraction format was reconstructed from the live `wiki/sources/` schema (mirroring `du-2024-d2sac-aigc-asp-selection` / `sun-2024-mfris-semantic-antijamming`). Every metadata field and headline claim verified against `raw/sources/<Folder>/full.md`. After this batch: **214 curated, 0 uncurated, 0 batches remain — all 43 papers in the run are curated.**

### Source page created (1)

- **[[du-2024-yolo-semcom-digital-twin]]** — *YOLO-Based Semantic Communication With Generative AI-Aided Resource Allocation for Digital Twins Construction* (IEEE Internet of Things Journal, DOI 10.1109/JIOT.2023.3317629; manuscript received 23 Jun 2023, accepted 10 Sep 2023, date of publication 20 Sep 2023, date of current version 21 Feb 2024 → year 2024; vol/issue/pages **not in parse**). A [[semantic-communication]] framework that builds a [[digital-twin|digital twin]] of an apple orchard from UAV imagery while cutting transmission cost: a slimmed [[yolov7-object-detection|YOLOv7-X]] detector ("YOLOv7-HS" via an ELAN-H/HorNet module + a parameter-free SimAM 3-D attention module) extracts only the semantic content (cropped apples + confidence + position), then transmission power is allocated by per-object importance ($W_i=c_i^\sigma$). Two allocation schemes — a confidence-based rule (Conf-SemCom) and a **diffusion-model-generated** scheme ([[diffusion-model-as-optimizer]], double-Q-trained, 5 inference denoising steps) — are compared against average allocation (Avg-SemCom) under a Fisher–Snedecor $\mathcal{F}$ fading channel, optimizing the authors' MIST (metric for image semantic transmission). First author Baoxia Du (Jilin), distinct from corpus-recurring co-author Hongyang Du.

### Concept page created (1)

- **[[digital-twin]]** — continuously-synchronized virtual replica of a physical object/process; the synchronization data stream is the recurring edge-transmission workload that motivates [[semantic-communication]] and importance-aware allocation. Anchors [[du-2024-yolo-semcom-digital-twin]] and relates to the human-digital-twin edge-deployment paper [[yang-2024-taco-human-digital-twin-edge]]. No dedicated page had existed (the term previously appeared only inline in [[generative-ai-for-mec]]).

### Entities

No new entity pages. One roster updated for a confirmed authored source: **[[dusit-niyato]]** 25→26 (+[[du-2024-yolo-semcom-digital-twin]], NTU — consistent with his confirmed affiliation across the corpus). Flagged for human confirmation, **not** created (consistent with the house deferral): lead author **Baoxia Du** and co-authors **Haifeng Liu**, **Peng Xin**, **Jun Yu**, **Mingyang Qi**, **You Tang** (Jilin Agricultural Science & Technology University / Jilin Institute of Chemical Technology / Yanbian University) — each 1 corpus appearance; and **Hongyang Du**, who recurs across the corpus but **remains intentionally un-promoted** pending affiliation disambiguation (the standing deferral noted on [[du-2024-gdm-network-optimization-tutorial]] and [[wang-2024-wipe-gai]]).

### Meta-docs

- **[[index]]** — +1 source entry (Generative-AI MEC) and +1 concept entry (MEC fundamentals: [[digital-twin]]).
- **[[overview]]** — Snapshot sources **213→214**, concepts **259→260** (entities 71 / derived layers unchanged). Generative-AI MEC track row +[[du-2024-yolo-semcom-digital-twin]]; simulation-only count line 213→214 (hardware-validated count unchanged at 3).

### Metadata verification (correctness-first)

DOI JIOT.2023.3317629 read directly from the parse's Digital Object Identifier line; venue (IEEE Internet of Things Journal) and the dual publication dates likewise from the parse front matter. Year set to 2024 (date of current version, matching the corpus convention for early-access/current-version splits). Volume/issue/pages are not in the parse and were **omitted rather than guessed** (a web search did not surface the article record directly; the parse remains authoritative). Quantitative claims preserved as stated in the parse and attributed to their tables/figures: detector ablation (Table III: 70.7M→53.5M params, 188.0G→152.6G FLOPs, AP@0.5 87.8%→89.1%→89.8%, with the authors' "+1.3%/+1.7% AP, −24% params, −19% FLOPs" and "+0.8% AP" deltas), detector comparison (Table IV, best AP@0.5 + 34 FPS among 8 detectors on MinneApple), and the 595.2 MB → 55.4 MB / **91% communication-cost reduction** over 331 test images. MIST/SSIM/BER-vs-η/distance curve readings and the ~500-iteration diffusion-crossover were flagged as figure-derived/indicative. Positioning claims (importance-aware semantic allocation; replaceable detector module) attributed as the paper's own.

### Toolkit

No ratchet needed — `curation_status.py --dupes`, `linkcheck.py`, `process_refs.py`, `frontmatter_audit.py`, `index_audit.py`, `entity_roster_audit.py`, and `corpus_counts.py` covered state detection, every commit gate, roster cross-checking, and count reconciliation. No reusable one-off arose; the toolkit is stable and unchanged this pass.

### Gates

**`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits. **`frontmatter_audit.py`** = 587 pages, 0 errors. **`index_audit.py`** = 589/589 indexed, 0 unindexed / 0 duplicate primaries. **`entity_roster_audit.py`** = 0 over-claims (3 pre-existing present-but-unlisted advisories, all on `wang-2024-wipe-gai`, unrelated to this batch). Counts reconciled via `corpus_counts.py`: sources **213→214**, concepts **259→260** (entities 71 unchanged); `raw/sources` 214 = curated 214 (zero uncurated). LLM Wiki API reachable (`/health` ok, v0.4.16); graph node/edge stats not enumerated (the `/graph` endpoint shape returned errors in prior passes and is not required for correctness). Untracked `wiki/media/` (app-generated) left unstaged.

### Run summary (multi-batch curation run, batches 1/8–8/8)

The multi-invocation run is **complete**: 43 papers curated across 8 batches (batch 1/8 covered earlier groundwork; batches 2/8–8/8 worked the `batches-remaining.json` plan = 6+6+6+6+6+6+1 = 37 papers). Final corpus: **214 sources, 260 concepts, 71 entities**, 0 uncurated raw folders, 0 duplicate MinerU ingests. `.curation-out/batches-remaining.json` now has an empty `batches` object (the `batch7` key moved into `completed`).

## 2026-06-02 — Curation pass (SOURCE layer — multi-batch run batch 7/8: 6 new sources; +5 concepts)

Seventh batch of the multi-invocation curation run over the 37 papers planned in `.curation-out/batches-remaining.json` (the `batch6` key there). Phase 0 reconciliation (`curation_status.py --dupes`): **214 raw folders, 207 curated, 7 uncurated, 0 duplicate MinerU ingests**; HEAD synced with origin/main (`5000c0d`), working tree clean apart from the uncurated raw folders + app-generated `wiki/media/`. None of the 6 batch papers had an existing source page. `.curation-context.md` was absent this session, so the extraction format was reconstructed from the live `wiki/sources/` schema (mirroring `lyu-2017-spiral-mbs-placement` / `chen-2022-qoe-game-end-edge-cloud`). Every metadata field and headline claim verified against `raw/sources/<Folder>/full.md`, with Crossref used to confirm venue/volume/page/year where the parse was silent. After this batch: **213 curated, 1 uncurated, 1 batch remains** (the `batch7` key: a single YOLO-semantic-communication digital-twins paper).

### Source pages created (6)

- **[[wen-2024-iscc-edge-ai]]** — *Task-Oriented Sensing, Computation, and Communication Integration for Multi-Device Edge AI* (IEEE TWC, vol 23(3), 2486–2502, 2024, DOI 10.1109/TWC.2023.3303232). Multi-device ISAC edge-AI **inference** system: DFRC devices radar-sense multi-view data, quantize + offload features to an edge server running **split inference**; maximize **discriminant gain** (KL-divergence accuracy surrogate) over sensing/transmit power + comm time + quantization bits; non-convex but solved **optimally** by the **sum-of-ratios** method. The inference-side counterpart to the FEEL-training ISCC paper [[tang-2024-iscc-uav-feel]]; co-author [[jie-xu]] (CUHK-Shenzhen).
- **[[sun-2021-temcmop-uav-cb]]** — *Time and Energy Minimization Communications Based on Collaborative Beamforming for UAV Networks: A Multi-Objective Optimization Method* (IEEE JSAC, vol 39(11), 3555–3572, 2021, DOI 10.1109/JSAC.2021.3088720). The **earliest collaborative-beamforming entry** in the corpus and seed of the [[geng-sun]]-group CB thread: UAVs form a virtual antenna array to serve remote BSs; multi-objective **TEMCMOP** (transmission time / VAA-performing time / motion+hovering energy) over positions + speeds + excitation weights + BS-serving order; NP-hard, energy-optimal-speed reformulation + **improved multi-objective ant lion optimizer (IMOALO)**.
- **[[gao-2024-d3qn-uav-mec-mobile-gt]]** — *UAV-Assisted MEC System With Mobile Ground Terminals: DRL-Based Joint Terminal Scheduling and UAV 3D Trajectory Design* (IEEE TVT, vol 73(7), 10164–10180, 2024, DOI 10.1109/TVT.2024.3367624). 3D UAV-MEC in a **post-disaster urban** scenario with **mobile** GTs; collect→compute→deliver total-time minimization over UAV 3D trajectory + GT scheduling under **obstacle avoidance** among buildings + **probabilistic-LoS** channel; MDP + **multi-step dueling DDQN (D3QN)**; 3D beats 2D, robust across GT mobility/height limits.
- **[[mozaffari-2016-uav-underlaid-d2d]]** — *Unmanned Aerial Vehicle With Underlaid Device-to-Device Communications: Performance and Tradeoffs* (IEEE TWC, 2016, DOI 10.1109/TWC.2016.2531652). UAV downlink base station coexisting with an **underlaid D2D** network; **stochastic-geometry** coverage/sum-rate analysis (static + mobile UAV); optimal altitude (decreasing in D2D density), **disk-covering** minimum stop-points, and the coverage-vs-delay / D2D-outage tradeoff. Virginia Tech (Wireless@VT) thread of [[mohammad-mozaffari]] / [[walid-saad]]. Volume/issue/pages **not in parse** (omitted rather than guessed).
- **[[zhan-2011-uav-relay-heading-optimization]]** — *Wireless Relay Communications with Unmanned Aerial Vehicles: Performance and Optimization* (IEEE TAES, vol 47(3), 2068–2085, 2011, DOI 10.1109/TAES.2011.5937283 — DOI/volume/pages Crossref-confirmed; parse gives only "0018-9251/11" + IEEE Log No. T-AES/47/3/941781). The **earliest UAV-comms source** in the corpus: multi-UAV relays connect ground APs to a BTS on the uplink; defines the **ENTR**, approximates it as a **sinusoid** in UAV heading → closed-form optimal heading, + an adaptive **handoff** algorithm + new-relay deployment.
- **[[zeng-2016-uav-comm-opportunities-challenges]]** — *Wireless Communications with Unmanned Aerial Vehicles: Opportunities and Challenges* (IEEE Communications Magazine, vol 54(5), 36–42, 2016, DOI 10.1109/MCOM.2016.7470933). Widely-cited **magazine overview** of UAV-aided wireless communications (NUS [[yong-zeng]] / Rui Zhang / Teng Joon Lim): architecture, air-to-ground LoS channel characteristics, three use cases (ubiquitous coverage / relaying / data collection), design challenges (CNPC, dynamic topology, SWAP, interference). Conceptual umbrella over the group's concrete formulations; no quantitative evaluation.

### Concept pages created (5)

- **[[discriminant-gain]]** — KL-divergence-derived class-separability surrogate for classification inference accuracy; anchors [[wen-2024-iscc-edge-ai]]. No dedicated page had existed.
- **[[task-oriented-communication]]** — optimizing for downstream task success (inference accuracy/latency) rather than throughput; anchors [[wen-2024-iscc-edge-ai]]; relates to [[semantic-communication]] / [[over-the-air-computation]].
- **[[sum-of-ratios-optimization]]** — fractional-programming method for a sum of quasi-linear ratios over a convex region (optimal iterative solution); anchors [[wen-2024-iscc-edge-ai]]; distinct from single-ratio [[fractional-programming-dinkelbach|Dinkelbach]].
- **[[ant-lion-optimizer]]** (ALO/MOALO) — antlion-prey swarm-intelligence metaheuristic; anchors [[sun-2021-temcmop-uav-cb]] (IMOALO); sits with [[salp-swarm-algorithm]] / [[multi-verse-optimizer]] / [[gravitational-search-algorithm]].
- **[[device-to-device-communication]]** (D2D) — direct device-pair communication, typically underlaid spectrum reuse; anchors [[mozaffari-2016-uav-underlaid-d2d]]; relates to [[overlay-underlay-spectrum-access]] / [[stochastic-geometry-network-analysis]].

### Entities

No new entity pages. Rosters updated for confirmed authored sources only: **[[geng-sun]]** 16→17, **[[jiahui-li]]** 13→14, **[[yanheng-liu]]** 2→3, **[[shuang-liang]]** 7→8, **[[hui-kang]]** 2→3 (all +[[sun-2021-temcmop-uav-cb]], the Jilin-University CB group, emails `sungeng@jlu.edu.cn` / `lijiahui0803@foxmail.com` / `yhliu@jlu.edu.cn` / `liangshuang@nenu.edu.cn` / `kanghui@jlu.edu.cn`); **[[mohammad-mozaffari]]** 3→4, **[[walid-saad]]** 3→4 (both +[[mozaffari-2016-uav-underlaid-d2d]], Virginia Tech Wireless@VT, `mmozaff@vt.edu` / `walids@vt.edu`); **[[yong-zeng]]** 7→8 (+[[zeng-2016-uav-comm-opportunities-challenges]], NUS, with Rui Zhang / Teng Joon Lim); **[[jie-xu]]** 2→3 (+[[wen-2024-iscc-edge-ai]], CUHK-Shenzhen SSE+FNii per Crossref affiliation — matches the existing ISAC identity, distinct from the GDUT "Jie Xu" namesake already flagged on his page).

  Flagged for human confirmation, **not** created (consistent with the house deferral of single-appearance / unresolved-identity co-authors): the ISCC co-authors **Dingzhu Wen**, **Peixi Liu**, **Guangxu Zhu**, **Yuanming Shi**, **Yonina C. Eldar**, **Shuguang Cui** (Shenzhen Research Institute of Big Data / ShanghaiTech / Weizmann / CUHK-Shenzhen); the D3QN co-authors **Yunfei Gao**, **Xiaopeng Yuan**, **Dingcheng Yang**, **Yulin Hu**, **Yue Cao**, **Anke Schmeink** (Wuhan University / Nanchang University / RWTH Aachen); the D2D co-authors **Mehdi Bennis** (Oulu), **Mérouane Debbah** (Huawei France / CentraleSupélec); the relay co-authors **Pengcheng Zhan** (Quantenna), **Kai Yu** (Ericsson), **A. Lee Swindlehurst** (UC Irvine); and the magazine-survey co-authors **Rui Zhang**, **Teng Joon Lim** (NUS) — each with 1 corpus appearance (or, for Rui Zhang / Teng Joon Lim, recurring only as deferred co-authors of existing Zeng/Lyu entries).

### Meta-docs

- **[[index]]** — +6 source entries (ISAC, sensing & physical-layer security ×1 [ISCC edge-AI]; Collaborative beamforming & aerial communications ×1 [TEMCMOP/IMOALO]; Compute offloading & DRL → post-disaster cluster ×1 [D3QN mobile-GT]; UAV communications & deployment foundations ×3 [UAV-comms magazine overview, UAV-relay heading/ENTR, UAV-underlaid-D2D]) and +5 concept entries (MEC fundamentals: [[task-oriented-communication]], [[discriminant-gain]], [[device-to-device-communication]]; Optimization techniques: [[ant-lion-optimizer]], [[sum-of-ratios-optimization]]).
- **[[overview]]** — Snapshot sources **207→213**, concepts **254→259** (entities 71 / derived layers unchanged). Track rows refreshed: Foundational surveys 19→22 (+UAV-comms magazine overview, +UAV-relay heading, +UAV-D2D), ISAC/sensing/PLS 13→14 (+ISCC edge-AI), Collaborative beamforming 9→10 (+TEMCMOP), Post-disaster MEC 6→7 (+D3QN mobile-GT); simulation-only count line 207→213.

### Metadata verification (correctness-first)

All 6 source pages carry a DOI line where one exists, each cross-checked against the parse and/or Crossref: TWC.2023.3303232 (vol 23(3), pp 2486–2502, pub Mar 2024 → year 2024), JSAC.2021.3088720 (vol 39(11), pp 3555–3572, pub Nov 2021 → 2021), TVT.2024.3367624 (vol 73(7), pp 10164–10180, pub Jul 2024 → 2024), TWC.2016.2531652 (pub 18 Feb 2016 → 2016; vol/issue/pages **not in parse**, omitted), TAES.2011.5937283 (vol 47(3), pp 2068–2085, 2011 — DOI/vol/pages Crossref-confirmed, parse silent), MCOM.2016.7470933 (vol 54(5), pp 36–42, 2016). Quantitative claims were checked against the parse and flagged figure-derived/indicative where not stated numerically (wen-2024 SVM/MLP accuracy curves, sun-2021 baseline margins, gao-2024 3D-vs-2D margins); the stated-in-parse numbers were preserved verbatim (mozaffari-2016's stop-point figures 5→23 / 20→55 and d0 8m→5m ×3; zhan-2011's ~20 kbit/s heading gain). Analytical/positioning claims (e.g. "first comprehensive analysis of UAV+underlaid-D2D coexistence", "first task-oriented ISCC for edge-AI inference") attributed as the papers' own.

### Toolkit

No ratchet needed — `curation_status.py --dupes`, `linkcheck.py`, `process_refs.py`, `frontmatter_audit.py`, `index_audit.py`, `entity_roster_audit.py`, and `corpus_counts.py` covered state detection, every commit gate, roster cross-checking, and count reconciliation. No reusable one-off arose; toolkit stable.

### Gates

**`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits. **`frontmatter_audit.py`** = 585 pages, 0 errors. **`index_audit.py`** = 587/587 indexed, 0 unindexed / 0 duplicate primaries. **`entity_roster_audit.py`** = 0 over-claims (3 pre-existing present-but-unlisted advisories, all on `wang-2024-wipe-gai`, unrelated to this batch). Counts reconciled via `corpus_counts.py`: sources **207→213**, concepts **254→259** (entities 71 unchanged). LLM Wiki API reachable (`/health` ok, v0.4.16); the `/graph` + `/projects` endpoints returned `Not found` for the attempted shapes, so graph node/edge stats were not enumerated this pass (not required for correctness). Untracked `wiki/media/` (app-generated) left unstaged.

## 2026-06-02 — Curation pass (SOURCE layer — multi-batch run batch 6/8: 6 new sources; +5 concepts)

Sixth batch of the multi-invocation curation run over the 37 papers planned in `.curation-out/batches-remaining.json` (the `batch5` key there). Phase 0 reconciliation (`curation_status.py --dupes`): **214 raw folders, 201 curated, 13 uncurated, 0 duplicate MinerU ingests**; HEAD synced with origin/main (`4cdbcd7`), working tree clean apart from the uncurated raw folders + app-generated `wiki/media/`. None of the 6 batch papers had an existing source page. `.curation-context.md` was absent this session, so the extraction format was reconstructed from the live `wiki/sources/` schema (mirroring `zhou-2024-mco-satellite-edge-offloading` / `chen-2024-ulse-game`). Every metadata field and headline claim verified against `raw/sources/<Folder>/full.md`. After this batch: **207 curated, 7 uncurated, 2 batches remain**.

### Source pages created (6)

- **[[zhang-2023-three-tier-satellite-offloading]]** — *Partial Computation Offloading in Satellite-Based Three-Tier Cloud-Edge Integration Networks* (IEEE TWC, 2023, DOI 10.1109/TWC.2023.3282630). Remote ground UEs offload (data-partition **partial offloading**) to a LEO-edge server and further to a ground cloud; min system energy over **user association + power + task scheduling + fronthaul/backhaul bandwidth assignment**; NOMA-SIC fronthaul + quadratic-transform power + CVX bandwidth, in a convergent joint iterative algorithm. Distinct from the maritime three-tier scheme [[zhang-2025-three-tier-maritime-offloading]] (different first author).
- **[[lyu-2017-spiral-mbs-placement]]** — *Placement Optimization of UAV-Mounted Mobile Base Stations* (IEEE Communications Letters, 2017, DOI 10.1109/LCOMM.2016.2633248). Minimum-count UAV-MBS coverage as the NP-hard **Geometric Disk Cover** problem; polynomial-time **spiral** algorithm (convex-hull-perimeter sequential placement, nudged inward); near core-sets-optimal on small instances, beats strip-based/K-means/random. *(Aerial-base-station deployment anchor, not MEC.)* Volume/issue/pages `not in parse` (web search did not confirm; left out rather than guessed).
- **[[chen-2022-qoe-game-end-edge-cloud]]** — *QoE-Aware Decentralized Task Offloading and Resource Allocation for End-Edge-Cloud Systems: A Game-Theoretical Approach* (IEEE TMC, 2022, DOI 10.1109/TMC.2022.3223119). Multi-user end-edge-cloud offloading as a **potential game** (MUTO-Game); proven NE existence + distributed GDTO algorithm + a convergence-time bound and a **Price-of-Anarchy** lower bound. Same first author/co-author group (ying-chen / [[yuan-wu]] / [[xuemin-shen]]) as [[chen-2024-ulse-game]].
- **[[zhang-2024-qos-vne-sagoin]]** — *QoS Aware Virtual Network Embedding in Space-Air-Ground-Ocean Integrated Network* (IEEE TSC, 2024, DOI 10.1109/TSC.2024.3357707). QoS-aware multi-domain **virtual network embedding** over a three-layer SAGOI-Net substrate; K-means classifies VNRs (compute/bandwidth/delay) to switch the RL agent's reward; convolutional policy network node mapping + k-shortest-path link mapping. SDN/NFV resource-orchestration sibling of [[zhang-2025-vnf-sgin-dql]]; corresponding author [[chunxiao-jiang]].
- **[[lu-2023-uav-relay-secure-maritime-mec]]** — *Resource and Trajectory Optimization for UAV-Relay-Assisted Secure Maritime MEC* (IEEE TCOM, 2023, DOI 10.1109/TCOMM.2023.3330884). UAV-relay (amplify-and-forward) maritime MEC with a **flying eavesdropper** + a **coastal jammer**; **max-min secure computing capacity** over transmit power + time-slot + local-computation + UAV trajectory; non-convex → **BCD + SCA**. The shore-based single-jammer counterpart to the multi-USV cooperative jamming of [[li-2023-secure-marine-iot-jamming]].
- **[[shi-2023-two-timescale-migration-rerouting]]** — *Service Migration or Task Rerouting: A Two-Timescale Online Resource Optimization for MEC* (IEEE TWC, 2023, DOI 10.1109/TWC.2023.3290005). First corpus entry to balance **service migration vs task rerouting** at MEC handovers; slow access/migration/rerouting + fast resource allocation, minimizing long-term average service delay; improved **Lyapunov** + randomized rounding (JASTO) + Lagrange-dual (OASTR), asymptotically optimal.

### Concept pages created (5)

- **[[geometric-disk-cover]]** (GDC) — minimum-disk coverage / p-center NP-hard problem; anchors [[lyu-2017-spiral-mbs-placement]]; the count-minimization complement to [[drone-cell-3d-placement]]. No dedicated page had existed.
- **[[price-of-anarchy]]** (PoA) — worst-NE-vs-centralized-optimum efficiency ratio for offloading games; anchors [[chen-2022-qoe-game-end-edge-cloud]], reused by [[chen-2024-ulse-game]]'s [[equilibrium-efficiency-metric]] framing.
- **[[virtual-network-embedding]]** (VNE) — mapping a VNR graph onto a physical substrate (node + link mapping); anchors [[zhang-2024-qos-vne-sagoin]]; relates to [[network-function-virtualization]] / [[network-slicing]].
- **[[space-air-ground-ocean-integrated-network]]** (SAGOI-Net) — SAGIN extended with an ocean/maritime segment; anchors [[zhang-2024-qos-vne-sagoin]]; ocean-augmented relative of [[space-air-ground-integrated-network]].
- **[[service-migration]]** — moving a long-lived service application between edge servers on handover (vs task rerouting / [[task-migration]] / compute-state [[seamless-handover]]); anchors [[shi-2023-two-timescale-migration-rerouting]].

### Entities

No new entity pages. Rosters updated for confirmed authored sources only: **[[haijun-zhang]]** 1→2 (+[[zhang-2023-three-tier-satellite-offloading]], USTB, `haijunzhang@ieee.org`); **[[victor-c-m-leung]]** 6→7 (+[[zhang-2023-three-tier-satellite-offloading]], `vleung@ieee.org`); **[[yong-zeng]]** 6→7 (+[[lyu-2017-spiral-mbs-placement]], NUS, co-author with Jiangbin Lyu / Rui Zhang / Teng Joon Lim); **ying-chen** 2→3, **[[yuan-wu]]** 13→14, **[[xuemin-shen]]** 7→8 (all +[[chen-2022-qoe-game-end-edge-cloud]] — `chenying@bistu.edu.cn` / `yuanwu@um.edu.mo` / `sshen@uwaterloo.ca`, the same group as their UAV-LEO game paper); **[[chunxiao-jiang]]** 4→5 (+[[zhang-2024-qos-vne-sagoin]], Tsinghua BNRist, `jchx@tsinghua.edu.cn`, corresponding author).

  Flagged for human confirmation, **not** created (consistent with the house deferral of single-appearance co-authors): the spiral-MBS co-authors **Jiangbin Lyu**, **Rui Zhang**, **Teng Joon Lim** (NUS); the satellite three-tier co-authors **Yaomin Zhang**, **Kai Sun**, **Jiahao Huo**, **Ning Wang** (USTB / Inner Mongolia Univ. / Zhengzhou Univ.); the QoE-game co-author **Jie Zhao** and **Jiwei Huang** (BISTU / China Univ. of Petroleum); the SAGOI-Net co-authors **Yi Zhang**, **Peiying Zhang**, **Shangguang Wang**, **Hongxia Zhang**, **Chunming Rong** (China Univ. of Petroleum / BUPT / Univ. of Stavanger); the secure-maritime authors **Fangwei Lu**, **Gongliang Liu**, **Weidang Lu**, **Yuan Gao**, **Jiang Cao**, **Nan Zhao** (a namesake watch — HIT-Weihai / ZJUT / AMS / Dalian Univ. of Tech.), **Arumugam Nallanathan** (QMUL); and the service-migration authors **You Shi**, **Changyan Yi**, **Ran Wang**, **Qiang Wu**, **Bing Chen** (NUAA), **Jun Cai** (Concordia) — each 1 corpus appearance.

### Meta-docs

- **[[index]]** — +6 source entries (Foundational surveys & overviews ×1 [spiral-MBS]; Game-theoretic offloading & allocation ×1 [QoE end-edge-cloud]; SAGIN/satellite offloading ×2 [satellite three-tier + SAGOI-Net VNE]; Maritime MEC ×1 [UAV-relay secure]; MEC fundamentals ×1 [two-timescale migration/rerouting]) and +5 concept entries (MEC fundamentals: [[service-migration]], [[virtual-network-embedding]]; aerial/network architectures: [[space-air-ground-ocean-integrated-network]], [[geometric-disk-cover]]; game theory: [[price-of-anarchy]]).
- **[[overview]]** — Snapshot sources **201→207**, concepts **249→254** (entities 71 / derived layers unchanged). Track rows refreshed: Foundational surveys 18→19 (+spiral-MBS), SAGIN/satellite offloading (+satellite three-tier, +SAGOI-Net VNE), Maritime MEC 18→19 (+UAV-relay secure), Game-theoretic offloading (+QoE end-edge-cloud PoA), MEC/MCC fundamentals 7→8 (+two-timescale migration/rerouting); simulation-only count line 201→207.

### Metadata verification (correctness-first)

All 6 source pages carry a DOI line, each verbatim-confirmed against the parse: TWC.2023.3282630, LCOMM.2016.2633248, TMC.2022.3223119, TSC.2024.3357707, TCOMM.2023.3330884, TWC.2023.3290005 — along with venues and publication-date→year mappings (pub 9 Jun 2023 → 2023; pub 29 Nov 2016 → 2017; pub 18 Nov 2022 → 2022; pub 24 Jan 2024 → 2024; pub 7 Nov 2023 → 2023; pub 5 Jul 2023 → 2023). The spiral-MBS paper's volume/issue/pages are **not in parse** and a web search did not confirm them, so they are omitted rather than guessed. Quantitative claims were checked against the parse and flagged figure-derived/indicative where not stated numerically (e.g. zhang-2023 convergence/energy margins, lyu-2017 Table-I MBS counts, chen-2022 large-scale baselines, lu-2023 benchmark margins); analytical/positioning claims (zhou-style "first to model LEO movement" has no analogue here; lu-2023's max-min secure-capacity-vs-T relationship and shi-2023's V-dependent delay/energy tradeoff are stated theorems) attributed as the papers' own.

### Toolkit

No ratchet needed — `curation_status.py --dupes`, `make_batches.py` (plan already persisted), `linkcheck.py`, `process_refs.py`, `frontmatter_audit.py`, `index_audit.py`, `entity_roster_audit.py`, and `corpus_counts.py` covered state detection, every commit gate, roster cross-checking, and count reconciliation. No reusable one-off arose; toolkit stable.

### Gates

**`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits. **`frontmatter_audit.py`** = 574 pages, 0 errors. **`index_audit.py`** = 576/576 indexed, 0 unindexed / 0 duplicate primaries. **`entity_roster_audit.py`** = 0 over-claims (3 pre-existing present-but-unlisted advisories, all on `wang-2024-wipe-gai`, unrelated to this batch). Counts reconciled via `corpus_counts.py`: sources **201→207**, concepts **249→254** (entities 71 unchanged). LLM Wiki API reachable (`/health` ok, v0.4.16); graph-stats endpoint not enumerated this pass (not required for correctness). Untracked `wiki/media/` (app-generated) left unstaged.

## 2026-06-02 — Curation pass (SOURCE layer — multi-batch run batch 5/8: 6 new sources; +1 concept)

Fifth batch of the multi-invocation curation run over the 37 papers planned in `.curation-out/batches-remaining.json` (the `batch4` key there). Phase 0 reconciliation (`curation_status.py --dupes`): **214 raw folders, 195 curated, 19 uncurated, 0 duplicate MinerU ingests**; HEAD synced with origin/main (`5fc633a`), working tree clean apart from the uncurated raw folders + app-generated `wiki/media/`. None of the 6 batch papers had an existing source page. `.curation-context.md` was absent this session, so the extraction format was reconstructed from the live `wiki/sources/` schema (mirroring `li-2024-airground-vec-offloading` / `ye-2021-ran-slicing-offloading`). Every metadata field and headline claim verified against `raw/sources/<Folder>/full.md`. After this batch: **201 curated, 13 uncurated, 2 batches remain**.

### Source pages created (6)

- **[[hu-2015-mec-5g-etsi-whitepaper]]** — *Mobile Edge Computing — A key technology towards 5G* (ETSI White Paper No. 11, first edition Sept 2015, ISBN 979-10-92620-08-5; no DOI). The corpus's **standardization anchor** for MEC itself: defines MEC as IT/cloud capabilities at the RAN edge, market drivers, business value, service scenarios (AR, intelligent video acceleration, connected cars, IoT gateway), deployment locations, and the ETSI ISG MEC + Proof-of-Concept framework; positions MEC complementary to NFV/SDN. *(Standardization/positioning document, no quantitative evaluation.)*
- **[[wang-2016-partial-offloading-dvs]]** — *Mobile-Edge Computing: Partial Computation Offloading Using Dynamic Voltage Scaling* (IEEE TCOM, 2016, DOI 10.1109/TCOMM.2016.2599530). Joint optimization of SMD computational speed + transmit power + offloading ratio under DVS, for energy minimization (ECM) and latency minimization (LM); ECM recast convex via variable substitution → closed-form **EPCO**, LM via univariate search; multi-cloud closed-form extension; proves **total offloading is never optimal under DVS**. *(MEC fundamentals anchor.)*
- **[[li-2020-maritime-uav-satellite-coverage]]** — *Maritime Coverage Enhancement Using UAVs Coordinated With Hybrid Satellite-Terrestrial Networks* (IEEE TCOM, 2020, DOI 10.1109/TCOMM.2020.2966715). Fixed-wing UAV coverage enhancement in a hybrid satellite-UAV-terrestrial maritime network; max-min ergodic rate over pre-planned trajectory + in-flight power using **only large-scale CSI** (AIS-derived ship positions); spectrum sharing UAV/satellite + TBS/satellite backhaul; non-convex → decomposition + SCA + bisection. Presented in part at IEEE WOCC 2019. *(Maritime communication-layer coverage, not MEC offloading.)*
- **[[zhou-2024-mco-satellite-edge-offloading]]** — *Mobility-Aware Computation Offloading in Satellite Edge Computing Networks* (IEEE TMC, 2024, DOI 10.1109/TMC.2024.3359759). Three-layer SECN (GEO cloud / LEO edge / ground); first to model LEO high-speed movement (coverage-time model + four mobility scenarios) on the offloading decision; min weighted latency+energy; discrete non-convex → continuous convex relaxation (proved feasible) → **MCO-A**, an ADMM-based distributed algorithm (convergence proved) scaling to large co-existing-user offloading.
- **[[ning-2023-madrl-uav-trajectory-differentiated-services]]** — *Multi-Agent Deep Reinforcement Learning Based UAV Trajectory Optimization for Differentiated Services* (IEEE TMC, 2023, DOI 10.1109/TMC.2023.3312276). Distributed multi-UAV trajectory control across multiple SPs offering differentiated services with non-binary, time-varying user preferences; min short-term user + long-term UAV computational cost; proves a unique Nash Equilibrium (complete info) then a Markov-game multi-agent DRL controller using local observations only.
- **[[liu-2023-sagecn-online-offloading]]** — *Online Computation Offloading for Collaborative Space/Aerial-Aided Edge Computing Toward 6G System* (IEEE TVT, 2023, DOI 10.1109/TVT.2023.3312676). Collaborative SAGECN where LEO satellites are both servers and users; a satellite offloads its own tasks one hop to a nearby aircraft or multi-hop to the cloud; min long-term completion delay via Lyapunov drift-plus-penalty + delayed online learning predicting task arrivals + queue lengths (per-slot bounded integer program).

### Concept pages created (1)

- **[[dynamic-voltage-scaling]]** (DVS) — varies supply voltage + clock frequency with load ($P=kf^3$); makes the device's local computational speed a continuous decision variable in offloading; anchors the EPCO/ECM result of [[wang-2016-partial-offloading-dvs]] ("total offloading is never optimal under DVS"); also a decision knob in [[zhang-2013-energy-optimal-mcc-stochastic]] and [[mao-2016-lodco-eh-mec-offloading]] (DVFS). No dedicated page had existed.

### Entities

No new entity pages. Roster updated for one confirmed authored source: **[[shengli-xie]]** 3→4 (+[[liu-2023-sagecn-online-offloading]]) — Yi Liu / Li Jiang / Kan Xie / Shengli Xie all at Guangdong University of Technology with `@gdut.edu.cn` emails; Shengli Xie's existing page lists the identical `shlxie@gdut.edu.cn`, confirming the same identity (not a namesake).

  Flagged for human confirmation, **not** created (consistent with the house deferral of single-appearance co-authors): the ETSI white-paper authors **Yun Chao Hu** (Huawei; note: a namesake distinct from the corpus's UAV-MEC "Hu" of [[hu-2019-pdd-uav-mec-offloading]]/[[hu-2019-uav-relay-edge-computing]]), **Milan Patel**, **Dario Sabella**, **Nurit Sprecher**, **Valerie Young**; the DVS-paper authors **Yanting Wang**, **Min Sheng**, **Xijun Wang**, **Liang Wang**, **Jiandong Li** (Xidian); the maritime-coverage authors **Xiangling Li**, **Wei Feng**, **Yunfei Chen**, **Cheng-Xiang Wang**, **Ning Ge**; the SECN-offloading authors **Jian Zhou**, **Qi Yang**, **Lu Zhao**, **Haipeng Dai**, **Fu Xiao** (NJUPT / Nanjing Univ.); and the differentiated-services authors **Zhaolong Ning**, **Yuxuan Yang**, **Xiaojie Wang**, **Qingyang Song**, **Lei Guo** (CQUPT), **Abbas Jamalipour** (Univ. of Sydney) — each 1 corpus appearance.

### Meta-docs

- **[[index]]** — +6 source entries (Foundational surveys & overviews ×1 [ETSI white paper]; MEC/MCC fundamentals ×1; Maritime MEC ×1 [communication-layer note]; SAGIN/satellite offloading ×2; Multi-agent UAV-MEC ×1) and +1 concept entry (MEC fundamentals: [[dynamic-voltage-scaling]]).
- **[[overview]]** — Snapshot sources **195→201**, concepts **248→249** (entities 71 / derived layers unchanged). Track rows refreshed: Foundational surveys 17→18 (+ETSI), MEC/MCC fundamentals 5→7 (+DVS partial-offloading, +ETSI white paper), SAGIN/satellite offloading (+mobility-aware ADMM, +LEO-as-server-and-user online offloading), Maritime MEC (+li-2020 communication-layer coverage adjacency), Game-theoretic offloading (+multi-SP NE-then-Markov-game MADRL); simulation-only count line 195→201.

### Metadata verification (correctness-first)

All 5 IEEE source pages carry a DOI line, each verbatim-confirmed against the parse: TCOMM.2016.2599530, TCOMM.2020.2966715, TMC.2024.3359759, TMC.2023.3312276 (stated via the supplementary-material DOI line in the parse), TVT.2023.3312676 — along with venues and publication-date→year mappings (pub 11 Aug 2016 → 2016; pub 15 Jan 2020 → 2020; pub 29 Jan 2024 → 2024; pub 5 Sept 2023 → 2023; pub 7 Sept 2023 → 2023). The ETSI white paper correctly carries an empty `url` (no DOI present in parse); its year (2015), ISBN, and venue (ETSI White Paper No. 11) are stated verbatim from the parse front matter. Quantitative claims were checked against the parse and flagged figure-derived/indicative where not stated numerically; the wang-2016 "total offloading is never optimal under DVS" is a stated analytical result, and zhou-2024's "first to model LEO movement" / ning-2023's "first multi-SP distributed trajectory" are the papers' own positioning claims.

### Toolkit

No ratchet needed — `curation_status.py --dupes`, `linkcheck.py`, `process_refs.py`, `frontmatter_audit.py`, `index_audit.py`, `entity_roster_audit.py`, and `corpus_counts.py` covered state detection, every commit gate, roster cross-checking, and count reconciliation. No reusable one-off arose; toolkit stable.

### Gates

**`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits. **`frontmatter_audit.py`** = 563 pages, 0 errors. **`index_audit.py`** = 565/565 indexed, 0 unindexed / 0 duplicate primaries. **`entity_roster_audit.py`** = 0 over-claims (3 pre-existing present-but-unlisted advisories, all on `wang-2024-wipe-gai`, unrelated to this batch). Counts reconciled via `corpus_counts.py`: sources **195→201**, concepts **248→249** (entities 71 unchanged). LLM Wiki API reachable (`/health` ok, v0.4.16); graph-stats endpoint not enumerated this pass (not required for correctness). Untracked `wiki/media/` (app-generated) left unstaged.

## 2026-06-02 — Curation pass (SOURCE layer — multi-batch run batch 4/8: 6 new sources; +2 concepts)

Fourth batch of the multi-invocation curation run over the 37 papers planned in `.curation-out/batches-remaining.json` (the `batch3` key there). Phase 0 reconciliation (`curation_status.py --dupes`): **214 raw folders, 189 curated, 25 uncurated, 0 duplicate MinerU ingests**; HEAD synced with origin/main (`670a5a0`), working tree clean apart from the uncurated raw folders + app-generated `wiki/media/`. None of the 6 batch papers had an existing source page. Every metadata field and headline claim verified against `raw/sources/<Folder>/full.md`. After this batch: **195 curated, 19 uncurated, 3 batches remain**.

### Source pages created (6)

- **[[huynh-2024-gai-physical-layer-survey]]** — *Generative AI for Physical Layer Communications: A Survey* (IEEE TCCN, 2024, DOI 10.1109/TCCN.2024.3384500). Survey of five GAI model families (GANs, **VAEs**, normalizing flows, diffusion, transformers) across physical-layer problems (modulation/signal classification, channel estimation/equalization, PLS, IRS, beamforming, JSCC, CSI feedback); GAI-vs-traditional-AI comparison + open issues (security/privacy, model-driven GAI, resource-efficient learning, real-time adaptation). *(Physical-layer GAI survey, not MEC.)*
- **[[li-2024-irs-secure-wpmec]]** — *Intelligent Reflecting Surface Assisted Secure Computation of Wireless Powered MEC System* (IEEE TMC, 2024, DOI 10.1109/TMC.2023.3269791). IRS-assisted WPT-MEC with a passive eavesdropper; harvest-then-offload (TDMA) + partial offloading; sum secure-computation-task-bits max over AP energy beamforming + IRS phase shifts + power + time + local frequency; non-convex → 3 subproblems via Taylor expansion + SDR + Lagrange-duality/KKT, iterative AO; >45% secure-bits gain at max AP power (abstract).
- **[[wu-2024-satellite-maritime-spectrum-sharing]]** — *Intelligent Spectrum Sharing Strategy for Integrated Satellite-Maritime Heterogeneous Mobile Networks* (IEEE TVT, 2024, DOI 10.1109/TVT.2023.3343720). VDES satellite-maritime spectrum sharing (VDE-SAT + VDE-TER co-frequency under ITU uplink/downlink interference constraints); satellite-centralized allocation maximizing combined throughput with task-priority weighting; partial observability → POMDP solved with SCA-D3QN (Double + Dueling DQN), offline-train/online-deploy. *(Satellite-maritime spectrum/comms, not MEC offloading.)*
- **[[li-2024-airground-vec-offloading]]** — *Joint Computation Offloading and Multidimensional Resource Allocation in Air–Ground Integrated Vehicular Edge Computing Network* (IEEE IoT-J, 2024, DOI 10.1109/JIOT.2024.3441236). Air-ground integrated VEC (HAP + UAVs + RSU, each w/ MEC; UAVs/RSU also relay to HAP); min total offloading delay (JCESRA) via BCD — many-to-one matching + coalition game (equipment selection) + CVX (bandwidth/compute) + SCA (UAV trajectory), then HAP as a knapsack solved by dynamic programming + compute reallocation.
- **[[qian-2022-uav-maritime-iot-noma]]** — *Joint Multi-Domain Resource Allocation and Trajectory Optimization in UAV-Assisted Maritime IoT Networks* (IEEE IoT-J, 2022, DOI 10.1109/JIOT.2022.3201017). NOMA-based UAV-assisted M-IoT MEC; USVs offload via uplink power-domain NOMA (SIC) to a UAV-MEC; total-energy min (USV tx/compute + UAV compute + UAV propulsion) over offload ratio + power + UAV compute allocation + trajectory; NP-hard (TSP-equivalent trajectory) → vertical two-layer decomposition: DDPG trajectory (top) + Lagrangian closed-form resource allocation (underlying).
- **[[ye-2021-ran-slicing-offloading]]** — *Joint RAN Slicing and Computation Offloading for Autonomous Vehicular Networks: A Learning-Assisted Hierarchical Approach* (IEEE OJVT, 2021, DOI 10.1109/OJVT.2021.3089083). Two-timescale RAN slicing + computation offloading for a C-AVN; small-timescale task scheduling for computation load balancing with minimal offloading variation via cooperative multi-agent deep Q-learning (fingerprint); large-timescale RAN slicing as a convex program with statistical (delay-violation) QoS; learning-assisted hierarchical loop. Presented in part at IEEE ICC 2021.

### Concept pages created (2)

- **[[variational-autoencoder]]** (VAE) — probabilistic encoder/latent/decoder generative model; anchors the GAI families catalogued by [[huynh-2024-gai-physical-layer-survey]]; sibling to [[generative-adversarial-network]] / [[generative-diffusion-model]] / [[conditional-gan]]. No dedicated page had existed.
- **[[dueling-dqn]]** — value/advantage two-stream DQN architecture; anchors the Double + Dueling DQN (SCA-D3QN) backbone of [[wu-2024-satellite-maritime-spectrum-sharing]]; sibling to [[deep-q-network]] / [[ddqn]].

### Entities

No new entity pages. Rosters updated for confirmed authored sources only: **[[dusit-niyato]]** 24→25 and **[[jiacheng-wang]]** 8→9 (+[[huynh-2024-gai-physical-layer-survey]], both NTU, verbatim-confirmed); the air-ground VEC co-authors **[[shichao-li]]** 2→3, **[[hongbin-chen]]** 3→4, **[[tony-q-s-quek]]** 5→6, **[[ning-zhang]]** 2→3, **[[mianxiong-dong]]** 3→4, **[[kaoru-ota]]** 2→3 (all +[[li-2024-airground-vec-offloading]]); the maritime-IoT-NOMA co-authors **[[liping-qian]]** 4→5 (first/corresponding author; "Li Ping Qian" respacing == Liping Qian, noted on the page), **[[yuan-wu]]** 12→13, **[[bin-lin]]** 9→10 (all +[[qian-2022-uav-maritime-iot-noma]]); and the RAN-slicing co-authors **[[xuemin-shen]]** 6→7 and **[[qiang-ye]]** 6→7 (+[[ye-2021-ran-slicing-offloading]]).

  - **Affiliation-history note ([[qiang-ye]]):** the 2021 RAN-slicing paper lists Qiang Ye at **Minnesota State University, Mankato**, whereas his entity page (built from later papers) records **University of Calgary**. Confirmed same person, not a namesake — the paper is co-authored with his documented Waterloo collaborators [[xuemin-shen]] + Weihua Zhuang and Waterloo students (Kaige Qu, Weisen Shi). The entity page now records the affiliation history rather than overwriting it.

  Flagged for human confirmation, **not** created (consistent with the house deferral of single-appearance co-authors): **Yonghui Li** (Univ. Sydney, Fellow; li-2024-irs-secure-wpmec), **Dong In Kim** / **Khaled B. Letaief** / **Nguyen Van Huynh** / **Dinh Thai Hoang** / **Diep N. Nguyen** (huynh-2024), and **Weihua Zhuang** (Waterloo, Fellow; ye-2021) — each 1 corpus appearance.

### Meta-docs

- **[[index]]** — +6 source entries (Foundational surveys & overviews ×1; Energy efficiency & WPT ×1; Vehicular MEC ×2; Maritime MEC ×1; Architectural/spectrum/governance ×1) and +2 concept entries (DRL backbones: [[dueling-dqn]]; generative-AI: [[variational-autoencoder]]).
- **[[overview]]** — Snapshot sources **189→195**, concepts **246→248** (entities 71 / derived layers unchanged). Track rows refreshed: Foundational surveys 16→17, Vehicular MEC 6→8, Maritime MEC 17→18 (+ a satellite-maritime-spectrum adjacency note), Generative-AI MEC (+physical-layer survey), Energy efficiency & WPT (+IRS-secure-WPMEC); simulation-only count line 189→195.

### Metadata verification (correctness-first)

All 6 source pages carry a DOI line, each verbatim-confirmed against the parse: TCCN.2024.3384500, TMC.2023.3269791, TVT.2023.3343720, JIOT.2024.3441236, JIOT.2022.3201017, OJVT.2021.3089083 — along with venues and publication-date→year mappings (current-version dates → 2024 / 2024 / 2024 / 2024; pub date 23 Aug 2022 → 2022; current version 1 Jul 2021 → 2021). Quantitative claims were checked against the parse and flagged as figure-derived/indicative where not stated numerically; the li-2024-irs-secure-wpmec ">45%" and the qian-2022 NOMA-energy-reduction headline claims are stated verbatim from the abstracts. Survey-level conclusions in huynh-2024 are attributed to the surveyed works rather than the survey itself.

### Toolkit

No ratchet needed — `curation_status.py --dupes`, `linkcheck.py`, `process_refs.py`, `frontmatter_audit.py`, `index_audit.py`, `entity_roster_audit.py`, and `corpus_counts.py` covered state detection, every commit gate, roster cross-checking, and count reconciliation. No reusable one-off arose; toolkit stable.

### Gates

**`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits. **`frontmatter_audit.py`** = 556 pages, 0 errors. **`index_audit.py`** = 558/558 indexed, 0 unindexed / 0 duplicate primaries. **`entity_roster_audit.py`** = 0 over-claims (3 pre-existing present-but-unlisted advisories, all on `wang-2024-wipe-gai`, unrelated to this batch). Counts reconciled via `corpus_counts.py`: sources **189→195**, concepts **246→248** (entities 71 unchanged). LLM Wiki API reachable (`/health` ok, v0.4.16); graph-stats endpoint not enumerated this pass (not required for correctness). Untracked `wiki/media/` (app-generated) left unstaged.

## 2026-06-02 — Curation pass (SOURCE layer — multi-batch run batch 3/8: 6 new sources; +4 concepts)

Third batch of the multi-invocation curation run over the 37 papers planned in `.curation-out/batches-remaining.json` (the `batch2` key there). Phase 0 reconciliation (`curation_status.py --dupes`): **214 raw folders, 183 curated, 31 uncurated, 0 duplicate MinerU ingests**; HEAD synced with origin/main (`83984bb`), working tree clean apart from the uncurated raw folders + app-generated `wiki/media/`. None of the 6 batch papers had an existing source page. Every metadata field and headline claim verified against `raw/sources/<Folder>/full.md`. After this batch: **189 curated, 25 uncurated, 4 batches remain**.

### Source pages created (6)

- **[[wang-2024-satellite-terrestrial-computing]]** — *Energy-Efficient Design of Satellite-Terrestrial Computing in 6G Wireless Networks* (IEEE TCOMM, 2024, DOI 10.1109/TCOMM.2023.3334813). BSs + LEO satellites with MEC serve GUEs + SUEs; min weighted total energy under delay via joint offloading-selection (relaxation mapping) + receive beamforming (SDR) + resource allocation; NP-hard → 3 subproblems solved by AO; NOMA-SIC uplinks + FSO inter-satellite links.
- **[[you-2017-meco-resource-allocation]]** — *Energy-Efficient Resource Allocation for Mobile-Edge Computation Offloading* (IEEE TWC, 2017, DOI 10.1109/TWC.2016.2633522). Multiuser MECO over TDMA + OFDMA; min weighted-sum mobile energy under a latency constraint; optimal TDMA policy is threshold-based on a derived offloading priority function (complete vs minimum offloading); finite-capacity + low-complexity OFDMA extensions. *(MEC fundamentals anchor.)*
- **[[he-2024-backscatter-wpmec-cooperation]]** — *Energy Efficiency Maximization of Backscatter-Assisted Wireless-Powered MEC With User Cooperation* (IEEE TMC, 2024, DOI 10.1109/TMC.2023.3243161). SN + helper-relay + HAP-with-MEC; integrated BackCom + active communication; user-EE maximization via Dinkelbach fractional programming + convex transform to semi-closed-form solutions.
- **[[miettinen-2010-mcc-energy-efficiency]]** — *Energy Efficiency of Mobile Clients in Cloud Computing* (USENIX HotCloud '10, Boston, June 2010). Corpus's earliest anchor; mobile-cloud-computing energy measurement/analysis — offloading saves energy only when E_cloud < E_local, governed by the computing-to-communication ratio; WLAN-vs-3G + traffic-pattern sensitivity. Venue/year `not in parse` (web-confirmed HotCloud '10); no DOI (USENIX workshop). *(Measurement study.)*
- **[[chen-2023-aiot-device-association]]** — *Enhancing AIoT Device Association With Task Offloading in Aerial MEC Networks* (IEEE IoT-J, 2023, DOI 10.1109/JIOT.2023.3300011). Distributed multi-UAV + GBS MEC; QoE (avg response time + IoTD cache-queue length) max via joint device association (greedy recursive RSRT) + task offloading (0-1 knapsack-with-variable-value backtracking BTO) + MADDPG UAV trajectory.
- **[[an-2024-multilayer-ris-hap-swipt]]** — *Exploiting Multi-Layer Refracting RIS-Assisted Receiver for HAP-SWIPT Networks* (IEEE TWC, 2024, DOI 10.1109/TWC.2024.3394214). Multi-layer refracting RIS-receiver enabling SWIPT over long-distance HAP links; worst-case sum-rate max under imperfect angular CSI + non-linear EH; scalable toolbox-free robust optimization (CSI discretization + LogSumExp-dual precoder + M-CCD RIS coefficients + closed-form PS/decoder). Earlier version GLOBECOM 2023. *(PHY RIS-receiver / SWIPT anchor, not MEC offloading.)*

### Concept pages created (4)

- **[[backscatter-communication]]** — passive reflect-and-modulate transmission vs active comm; BackCom/AC energy-throughput trade-off; anchors [[he-2024-backscatter-wpmec-cooperation]].
- **[[simultaneous-wireless-information-and-power-transfer]]** (SWIPT) — joint information + energy delivery via power splitting; anchors [[an-2024-multilayer-ris-hap-swipt]], reused by [[chen-2025-swipt-mec-sac]] (no dedicated page had existed).
- **[[device-association]]** — device↔serving-node/subchannel association as a distinct (combinatorial) decision dimension in aerial MEC; anchors [[chen-2023-aiot-device-association]].
- **[[computation-to-communication-ratio]]** — foundational MCC offload-decision crossover (cycles per byte); anchors [[miettinen-2010-mcc-energy-efficiency]].

### Entities

No new entity pages. Roster updated for one confirmed authored source: **[[dusit-niyato]]** 23→24 (+[[an-2024-multilayer-ris-hap-swipt]] as Fellow at NTU `dniyato@ntu.edu.sg`, verbatim-confirmed). Flagged for human confirmation rather than promoted (consistent with the house deferral of single-cluster co-authors): **Mohsen Guizani** (now 4 corpus appearances — zhu-2025-lycnn, he-2023-fairness, chen-2024-three-party, he-2024-backscatter; MBZUAI, identity unambiguous but promotion is a style call), **Kai-Kit Wong** (3 appearances), and the **Kang An / Yifu Sun / Zhi Lin / Yonggang Zhu** NUDT cluster (2 appearances each via sun-2024-mfris + an-2024).

### Meta-docs

- **[[index]]** — +6 source entries (MEC/MCC fundamentals ×2; Energy efficiency & WPT; SAGIN/satellite offloading; Multi-agent UAV-MEC; ISAC/sensing & PLS) and +4 concept entries (MEC fundamentals ×2 + ×2 in the energy area).
- **[[overview]]** — Snapshot sources **183→189**, concepts **242→246**; entities 71 / derived unchanged. Track rows refreshed: MEC/MCC fundamentals 3→5 (+earliest-source note), Energy efficiency & WPT, SAGIN/satellite, ISAC/sensing/PLS 12→13, and UAV-MEC + DRL; simulation-only count line 171→189.

### Metadata verification (correctness-first)

The 5 source pages carrying a DOI line had it verbatim-confirmed against the parse (TCOMM.2023.3334813, TWC.2016.2633522, TMC.2023.3243161, JIOT.2023.3300011, TWC.2024.3394214) along with venues and each publication-date→year mapping (current-version dates → 2024 / 2017 / 2024 / 2023 / 2024). The Miettinen-Nurminen workshop paper carries no venue/year/DOI in the parse — the page states `not in parse` and attributes HotCloud '10 (Boston, June 2010) as web-confirmed. Quantitative claims (You's 30-user/200-realization sim; He's −16/−22 dB BackCom-vs-AC thresholds; An's ~15-iteration convergence, N_Tot<468 / N_E<6×6 / potential-gain scaling) were checked against the parse and flagged as figure-derived/indicative where not stated numerically.

### Toolkit

No ratchet needed — `curation_status.py --dupes`, `linkcheck.py`, `process_refs.py`, `frontmatter_audit.py`, `index_audit.py`, `entity_roster_audit.py`, and `corpus_counts.py` covered state detection, every commit gate, roster cross-checking, and count reconciliation. No reusable one-off arose; toolkit stable.

### Gates

**`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits. **`frontmatter_audit.py`** = 548 pages, 0 errors. **`index_audit.py`** = 550/550 indexed, 0 unindexed / 0 duplicate primaries. **`entity_roster_audit.py`** = 0 over-claims (3 pre-existing present-but-unlisted namesake advisories, unrelated to this batch). Counts reconciled via `corpus_counts.py`: sources **183→189**, concepts **242→246** (entities 71 unchanged). LLM Wiki API reachable (`/health` ok, v0.4.16); graph-stats endpoint not enumerated this pass (not required for correctness). Untracked `wiki/media/` (app-generated) left unstaged.

## 2026-06-02 — Curation pass (SOURCE layer — multi-batch run batch 2/8: 6 new sources; +2 concepts)

Second batch of the multi-invocation curation run over the 37 papers planned in `.curation-out/batches-remaining.json` (the `batch1` key there). This invocation **recovered an interrupted batch**: 5 source pages had been drafted on disk (uncommitted, no log entry) before an external usage-limit interruption, and `index.md`/`overview.md` had **not** yet been touched. Per the resume-don't-duplicate rule, the 5 drafts were reviewed for correctness/completeness (kept as-is), the 6th paper of the batch (`Cramr-Rao_Bound_Optimization_for_Active_RIS-Empowered_ISAC_Systems`) was extracted and written, the needed concept stubs were created, and navigation was refreshed. Phase 0 reconciliation (`curation_status.py --dupes`) after recognizing the 5 drafts: **214 raw folders, 182 curated, 32 uncurated, 0 duplicate MinerU ingests**. Every metadata field and headline claim verified against `raw/sources/<Folder>/full.md`. After this batch: **183 curated, 31 uncurated, 5 batches remain**.

### Source pages created (6 — 5 recovered drafts + 1 new)

- **[[lillicrap-2016-ddpg-continuous-control]]** — *Continuous Control with Deep Reinforcement Learning* (ICLR 2016; arXiv:1509.02971). DDPG origin paper; off-policy actor-critic bringing DQN's replay + target networks to deterministic continuous control. DOI/venue/date `not in parse` (web-confirmed ICLR 2016). *(Foundational DRL method.)*
- **[[van-hasselt-2016-double-dqn]]** — *Deep Reinforcement Learning with Double Q-learning* (AAAI 2016; arXiv:1509.06461). Double DQN origin paper; decouples selection from evaluation (reuse target net) to curb DQN over-estimation; Atari median 93.5%→114.7% / mean 241.1%→330.3% (Table 1, parse). DOI/venue `not in parse` (web-confirmed AAAI 2016). *(Foundational DRL method.)*
- **[[mozaffari-2019-drone-antenna-array]]** — *Communications and Control for Wireless Drone-Based Antenna Array* (IEEE TCOMM, 2019, DOI 10.1109/TCOMM.2018.2871453). Minimum-service-time design via perturbation-theory drone-spacing directivity + **bang-bang** closed-form minimum control time; +32% spectral efficiency vs fixed uniform array. *(UAV-communications / aerial-beamforming anchor, not MEC.)*
- **[[zhan-2020-completion-time-energy-uav-mec]]** — *Completion Time and Energy Optimization in the UAV-Enabled MEC System* (IEEE IoT-J, 2020, DOI 10.1109/JIOT.2020.2993260). Fixed-wing UAV-MEC; separate UAV-energy and completion-time minimization + their Pareto tradeoff; path discretization + AO + SCA.
- **[[zhang-2024-mhspo-satellite-peer-offloading]]** — *Energy-Efficient Computation Peer Offloading in Satellite Edge Computing Networks* (IEEE TMC, 2024, DOI 10.1109/TMC.2023.3269801). Multi-hop satellite peer offloading (MHSPO) for load balancing; weighted delay+energy min via Lyapunov + delayed online learning + per-satellite distributed decomposition.
- **[[zhu-2024-crb-active-ris-isac]]** — *Cramér-Rao Bound Optimization for Active RIS-Empowered ISAC Systems* (IEEE TWC, 2024, DOI 10.1109/TWC.2024.3384501). Derives the DoA CRB for active-RIS ISAC and minimizes it over BS precoding + active-RIS reflection beamforming via AO + SDR + MM; >30 dB CRB reduction vs passive RIS. *(PHY active-RIS ISAC anchor, not MEC.)*

### Concept pages created (2)

- **[[computation-peer-offloading]]** — horizontal edge-to-edge (peer) offloading for load balancing; anchors [[zhang-2024-mhspo-satellite-peer-offloading]].
- **[[bang-bang-control]]** — time-optimal full-on/full-off control; anchors the minimum-control-time derivation in [[mozaffari-2019-drone-antenna-array]].

(The 5 recovered drafts already carried their concept dependencies on [[ddpg]], [[ddqn]], [[cramer-rao-bound]], [[active-ris]], [[lyapunov-optimization]], [[alternating-optimization-sdr-sca]], etc., which existed from prior passes; only the two stubs above were genuinely new vocabulary.)

### Entities

No new entity pages. Rosters updated for confirmed authored sources surfaced by `entity_roster_audit.py`: **[[mohammad-mozaffari]]** 2→3 and **[[walid-saad]]** 2→3 (both +[[mozaffari-2019-drone-antenna-array]], Virginia Tech / Wireless@VT, identities already confirmed); **[[dusit-niyato]]** 20→23 (+[[zhan-2020-completion-time-energy-uav-mec]] as Fellow at NTU `dniyato@ntu.edu.sg`, verbatim-confirmed; plus two previously-omitted batch-1 sources [[wang-2024-wipe-gai]] and [[wang-2024-xl-mimo-tutorial]] that the roster audit flagged as present-but-unlisted). No identities promoted on uncertainty.

### Meta-docs

- **[[index]]** — +6 source entries (Foundational DRL methods ×2; Classical/convex UAV-MEC; SAGIN/satellite; ISAC/sensing/PLS; UAV-communications-foundations) and +2 concept entries (MEC fundamentals; UAV control & decisions).
- **[[overview]]** — Snapshot sources **177→183**, concepts **240→242**; entities 71 / derived unchanged. Track rows refreshed: Foundational DRL methods 3→5, ISAC/sensing/PLS 11→12, plus the satellite and classical-convex rows.

### Metadata verification (correctness-first)

The 4 source pages with a DOI line had it verbatim-confirmed against the parse (TCOMM.2018.2871453, JIOT.2020.2993260, TMC.2023.3269801, TWC.2024.3384501) along with venues and the publication-date→year mapping. The two DeepMind method papers carry no DOI/venue/date line in the parse — both pages state `not in parse` and attribute the ICLR-2016 / AAAI-2016 venues as web-confirmed. Double DQN's Atari score deltas and DDPG's ">20 tasks" were verified against the parse; the CRB >30 dB / 36 dB and figure-curve margins flagged as figure-derived/indicative.

### Toolkit

No ratchet needed — `curation_status.py --dupes`, `linkcheck.py`, `process_refs.py`, `frontmatter_audit.py`, `index_audit.py`, `entity_roster_audit.py`, and `corpus_counts.py` covered state detection, every commit gate, roster cross-checking, and count reconciliation. No reusable one-off arose; toolkit stable.

### Gates

**`linkcheck.py`** = NO DANGLING LINKS (the 2 dangling targets the drafts introduced — `bang-bang-control`, `computation-peer-offloading` — were resolved by creating those concept pages). **`process_refs.py`** = 0 files / 0 hits. **`frontmatter_audit.py`** = 538 pages, 0 errors. **`index_audit.py`** = 540/540 indexed, 0 unindexed / 0 duplicate primaries. Counts reconciled via `corpus_counts.py`: sources **177→183**, concepts **240→242** (entities 71 unchanged). LLM Wiki API not queried this pass (not required for correctness). Untracked `wiki/media/` (app-generated) left unstaged.

## 2026-06-02 — Curation pass (SOURCE layer — multi-batch run batch 1/8: 6 new sources; +6 concepts)

First batch of a multi-invocation curation run over **43 newly-added raw papers**. Phase 0 reconciliation (`curation_status.py --dupes`) found **214 raw folders, 177 now-curated, 37 still uncurated, 0 duplicate MinerU ingests**. This invocation recovered and finalized an interrupted in-progress batch: 6 source pages + 6 concept pages were already drafted on disk (uncommitted, no log entry, `index.md`/`overview.md` already edited), so per the resume-don't-duplicate rule this batch audited and committed them rather than re-extracting. The remaining 37 papers are planned into 7 further batches (`make_batches.py --size 6` → `.curation-out/batches-remaining.json`) for subsequent invocations. Every metadata field and headline claim re-verified against `raw/sources/<Folder>/full.md`.

### Source pages created (6)

- **[[wang-2024-xl-mimo-tutorial]]** — *A Tutorial on Extremely Large-Scale MIMO for 6G* (IEEE COMST, 2024, DOI 10.1109/COMST.2023.3349276). Physical-layer / near-field survey anchor; four XL-MIMO hardware designs + near-field channel modeling + DL-empowered signal processing. *(PHY anchor, not MEC.)*
- **[[wang-2024-wipe-gai]]** — *A Unified Framework for Guiding Generative AI With Wireless Perception…* (IEEE TMC, 2024, DOI 10.1109/TMC.2024.3377226). WiPe-GAI: sequential multi-scale perception predicts user skeleton → guides GAI; diffusion model generates the optimal pricing incentive.
- **[[chen-2024-dro-video-caching]]** — *Adaptive Bitrate Video Caching in UAV-Assisted MEC Networks Based on DRO* (IEEE TMC, 2024, DOI 10.1109/TMC.2023.3304624). ζ-structure-metric confidence set + convex DRO latency minimizer under an energy budget; real YouTube traces.
- **[[zhang-2024-coma-satellite-offloading]]** — *Collaborative Task Offloading… for Satellite MEC Using MADRL* (IEEE TVT, 2024, DOI 10.1109/TVT.2024.3405642). Distributed LEO SMEC; POMDP solved with COMA (CTDE) + attention-BiLSTM actor; STK constellation.
- **[[zhao-2018-caching-uav-ia-secure]]** — *Caching UAV Assisted Secure Transmission in Hyper-Dense Networks Based on Interference Alignment* (IEEE TCOMM, 2018, DOI 10.1109/TCOMM.2018.2792014). IA for single-antenna caching UAVs + idle SBSs as zero-forced friendly jammers. *(Caching + IA-PLS anchor, not MEC offloading.)*
- **[[zhu-2024-zdrl-uav-tracking]]** — *Collaborative RL Based UAV Trajectory Design for 3D UAV Tracking* (IEEE TMC, 2024, DOI 10.1109/TMC.2024.3382913). One active + four passive UAVs, TDOA/TSWLS; Z-function-decomposition RL (distributional RL); up to 39.4%/64.6% lower positioning error vs VD-RL / independent DRL (abstract-verbatim). *(Localization + trajectory, not MEC offloading.)*

### Concept pages created (6)

- **[[counterfactual-multi-agent-policy-gradient]]** (COMA) — credit-assignment via centralized-critic counterfactual baseline; anchors [[zhang-2024-coma-satellite-offloading]].
- **[[distributional-reinforcement-learning]]** — learns the return distribution, not just its expectation; anchors [[zhu-2024-zdrl-uav-tracking]].
- **[[extremely-large-scale-mimo]]** and **[[near-field-communications]]** — 6G PHY pair anchored by [[wang-2024-xl-mimo-tutorial]].
- **[[interference-alignment]]** — MIMO precoding-subspace interference management; anchors [[zhao-2018-caching-uav-ia-secure]].
- **[[wireless-perception]]** — CSI-based sensing to guide GAI; anchors [[wang-2024-wipe-gai]].

### Entities

No new entity pages this batch. Recurring identities flagged for human confirmation rather than promoted: **Hongyang Du** (appears on both new TMC/COMST papers with differing affiliations — intentionally un-promoted), **Nan Zhao** (lead of the 2018 caching-UAV paper, shares an author neighborhood with [[zhao-2019-uav-emergency-disasters]]). Confirmed existing entities cross-linked from [[wang-2024-wipe-gai]]: [[jiacheng-wang]], [[dusit-niyato]], [[jiawen-kang]], [[xuemin-shen]].

### Meta-docs

- **[[index]]** — +6 source entries (placed under UAV-comms anchor / caching-offloading / satellite-offloading / generative-AI / secure-ISAC sections per topic) and +6 concept entries (DRL-methods + PHY/security groups).
- **[[overview]]** — Snapshot sources **171→177**, concepts **234→240**; entities 71 and derived 42 unchanged.

### Metadata verification (correctness-first)

All 6 DOIs verbatim-confirmed against the `Digital Object Identifier` line of each parse (COMST.2023.3349276, TMC.2024.3377226, TMC.2023.3304624, TVT.2024.3405642, TCOMM.2018.2792014, TMC.2024.3382913). All venues/years confirmed. ZD-RL's 39.4%/64.6% headline numbers verified verbatim in the abstract; figure-derived margins on the other five were flagged as indicative rather than stated as exact.

### Toolkit

No ratchet needed — `curation_status.py --dupes`, `make_batches.py`, `linkcheck.py`, `process_refs.py`, `frontmatter_audit.py`, `index_audit.py`, and `corpus_counts.py` covered state detection, batch planning, grounding discovery, and every commit gate. No reusable one-off arose; toolkit stable.

### Gates

**`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits. **`frontmatter_audit.py --type source`** = 177 pages, 0 errors; **`--type concept`** = 240 pages, 0 errors. **`index_audit.py`** = 532/532 indexed, 0 unindexed / 0 duplicate primaries. Counts reconciled via `corpus_counts.py`: sources **171→177**, concepts **234→240** (entities 71 / derived 42 unchanged). LLM Wiki API healthy (v0.4.16) but the `/graph` endpoint returned `Not found` in this headless shell — graph stats skipped (not required for correctness). Untracked `wiki/media/` (app-generated, hash-suffixed, unreferenced by any page) left unstaged.

## 2026-06-02 — Synthesis-expansion pass (DERIVED layer — THEME B: solver-selection decision aid + sim-to-real; no new papers)

Second follow-up coverage-growth batch (synthesizer, not auditor): no new raw papers, addressed the solver-selection and hardware-validation leads the prior synthesis pass deferred. Phase 0 reconciled clean: **171 raw = 171 curated, 0 uncurated**. Every claim grounded against the parses before writing.

### Pages created (1)

- **`synthesis/hardware-validation-and-sim-to-real-in-mec`** (lead 7) — inventories the few non-simulation sources on a 4-rung depth ladder: **full algorithm on real devices** ([[sun-2024-asap-uav-swarm]] 24 airborne computers [20 Nano/2 TX2/2 NX] + 5 real quad-rotors; [[shao-2024-drl-antijamming-mec]] Raspberry Pi 4B + USRP N210/X310; [[zhang-2020-response-delay-uav-swarm]] 2 DJI M100 + 5G NR mmWave 28 GHz, 89.9% packet cut), **proof-of-concept** ([[qu-ecoei-uav-swarm]] 4 Jetson; year not in parse), **practicality demo** ([[sun-2024-imssa-uav-secure-cb]] Raspberry Pi CB), and **model verification** ([[bai-2024-delay-aware-cooperative-edge-cloud]] real UAV-edge platform verifies model, algorithm in sim). All hardware specs verbatim-verified against parses. Distils only parse-grounded sim-to-real challenges (idealized/indoor testbeds, small/tethered scale, unmodelled flight+channel dynamics, single-failure-only fault tests, DRL training never on hardware). Connects to [[query-real-world-validation-of-jppo-en-convntm]] and [[drl-simulation-with-pomdp-formulation]].

### Pages refreshed / cross-links densified

- **[[drl-vs-evolutionary-vs-classical-solvers]] extended (lead 6 — converged into the existing synthesis, no standalone tree).** Added a **"problem features → recommended family" decision aid** table that annotates each boundary as **empirically-supported** (within-family / sub-block-role) vs **inferred** (the headline DRL-vs-evolutionary boundary, which no source measures head-to-head). Converged rather than duplicated the page's existing "When to pick each family" guide; a standalone decision-tree page judged unnecessary (would near-duplicate).
- **`related:` links added** (bidirectional) on [[query-real-world-validation-of-jppo-en-convntm]], [[drl-simulation-with-pomdp-formulation]], and the 6 hardware sources ([[sun-2024-asap-uav-swarm]], [[shao-2024-drl-antijamming-mec]], [[zhang-2020-response-delay-uav-swarm]], [[qu-ecoei-uav-swarm]], [[sun-2024-imssa-uav-secure-cb]], [[bai-2024-delay-aware-cooperative-edge-cloud]]).
- **Meta-docs:** [[index]] — +1 Synthesis entry. [[overview]] — synthesis tally 13→14 + refreshed observation #8 (added the imssa practicality demo + a pointer to the new sim-to-real synthesis).

### Leads resolved this batch

- **Lead 7 (hardware-validation / sim-to-real)** — promoted to the new synthesis page; all hardware claims re-verified verbatim against parses.
- **Lead 6 (solver-selection decision aid)** — converged into [[drl-vs-evolutionary-vs-classical-solvers]] as a feature→family table with empirically-supported-vs-inferred annotations; no standalone page (no padding).

### Entities / concepts

Re-checked for THEME B: no new recurring author or concept needed — the sim-to-real and solver-selection material reuses existing slugs.

### Toolkit

No ratchet needed — the maintained scripts covered state detection, grounding, and all gates. No reusable one-off arose; toolkit stable.

### Gates (THEME B)

**`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits. **`frontmatter_audit.py --type synthesis`** = 14 pages, 0 errors. **`index_audit.py`** = 520/520 indexed, 0 unindexed / 0 duplicate primaries. New page + edited meta-docs verified mojibake-free. Counts reconciled via `corpus_counts.py`: synthesis **13→14** (171 sources / 234 concepts / 71 entities / 42 derived).

## 2026-06-02 — Synthesis-expansion pass (DERIVED layer — THEME A: ISAC / generative-AI roles; no new papers)

Follow-up coverage-growth batch (synthesizer, not auditor): no new raw papers, grew the *derived* layer over the existing corpus from the ISAC-themed leads the prior synthesis pass deferred. Tree clean at `48e95cb` before starting. Phase 0 reconciled clean: `curation_status.py --dupes` = **171 raw = 171 curated, 0 uncurated, 0 genuinely-new** (no routing to `mec-wiki-curator`). Every claim grounded against the parses (`raw/sources/<Folder>/full.md`) and the committed source pages before writing.

### Pages created (1)

- **`synthesis/gai-generator-vs-optimizer-in-isac`** (lead 8) — maps the 4 ISAC GAI sources into two architectural roles for the generative model: **physical-layer generator** ([[wang-gai-isac-physical-layer]] diffusion SSG, DoA MSE ~1.03° / CSI-compression −7.05 vs −2.46 dB at CR 1/64 — both verbatim in parse; year **not in parse**; [[faisal-2025-cgan-ris-isac-channel]] CGAN channel estimation) vs **decision-layer optimizer** ([[zhang-2024-gdmtd3-aerial-secure-cb]] diffusion-as-policy/actor; [[zhang-2025-gan-td3-isac-active-ris]] GAN-as-critic-regularizer — "boost the estimation accuracy of Q-value" + "performance and stability at the cost of computational complexity" verbatim). Identifies the architectural fusion gap (no source uses GAI at BOTH layers in one system) and ties it to the learning-first-vs-convex-first split in [[isac-sensing-in-aerial-mec]].

### Pages refreshed / cross-links densified

- **[[isac-sensing-in-aerial-mec]] refreshed (lead 4 — resolved by converging into the existing synthesis, not a near-duplicate page).** Added a **function-coupling matrix** distinguishing sensing+communication (two-function) sources from the **sole genuine tri-function ISCC source** [[tang-2024-iscc-uav-feel]]; grounded [[zhu-2024-sensing-comm-doppler-uav-swarm]] as sensing+comm with **no MEC offloading** (min-max CRLB under SNR-loss). States the tri-function coupling gap (ISAC and MEC remain largely separate threads; compute welded onto sensing in exactly one source) and mirrors it to the collaborative-beamforming no-compute-objective observation. Added the new GAI-roles cross-link.
- **`related:` links added** (all bidirectional, none self-referential) on the 4 source pages ([[wang-gai-isac-physical-layer]], [[faisal-2025-cgan-ris-isac-channel]], [[zhang-2024-gdmtd3-aerial-secure-cb]], [[zhang-2025-gan-td3-isac-active-ris]]), the 2 concept pages ([[generative-ai-for-mec]], [[diffusion-model-as-optimizer]]), and [[collaborative-beamforming-in-aerial-mec]].
- **Meta-docs:** [[index]] — +1 Synthesis entry. [[overview]] — analytical-layer synthesis tally 12→13 + named the GAI-role synthesis.

### Leads resolved this batch

- **Lead 8 (physical-layer GAI generator vs decision-layer optimizer)** — promoted to the new synthesis page (was deferred from the prior pass as "viable but lower-leverage"; grounded cleanly this batch).
- **Lead 4 (sensing-comm-compute tri-function coupling gap)** — judged **not** to warrant a standalone page (would near-duplicate the two existing track maps); converged the explicit coupling matrix into [[isac-sensing-in-aerial-mec]] instead. No padding.

### Toolkit

No ratchet needed — `curation_status`, `linkcheck`, `process_refs`, `frontmatter_audit`, `corpus_counts` covered state detection, grounding discovery, and all commit gates. No reusable one-off arose; toolkit stable.

### Gates (THEME A)

**`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits. **`frontmatter_audit.py --type synthesis`** = 13 pages, 0 errors. New page + edited meta-docs verified mojibake-free. Counts reconciled via `corpus_counts.py`: synthesis **12→13** (171 sources / 234 concepts / 71 entities / 41 derived).

## 2026-06-02 — Synthesis-expansion pass (DERIVED layer — DRL solver-design & constraint-handling theme; no new papers)

A coverage-growth pass (synthesizer, not auditor): no new raw papers, grew the *derived* layer over the existing corpus from leads surfaced in a user exploration conversation. Tree clean at `faecd50` before starting. Phase 0 reconciled clean: `curation_status.py --dupes` = **171 raw = 171 curated, 0 uncurated, 0 genuinely-new** (no routing to `mec-wiki-curator`). LLM Wiki API reachable (`allowUnauthenticated:true`, v0.4.16); baseline graph **513 nodes / 4481 edges** → **516 / 4534** after the pass (+3 nodes, +53 edges).

### Batch scope

Took the three best-grounded, audit-flagged leads, which form one coherent theme — **DRL solver-design & constraint-handling** — and left the other five conversation leads for later batches (rationale below). Every claim was grounded against the parses (`raw/sources/<Folder>/full.md`) and the committed source pages before writing.

### Pages created (3)

- **`methodology/lyapunov-guided-drl`** (lead 1, the conversation's highest-priority lead) — the Lyapunov drift-plus-penalty + per-slot DRL hybrid as a cross-source design pattern. Roster grounded across 6 sources: [[qin-2025-bcuav-masac]] (Lyapunov + MASAC + CVX + DOA; "drift-plus-penalty" + balancing weight λ verbatim in parse §B), [[zhu-2025-lycnn-drl-wpt-mec]] (Lyapunov + CNN actor; >97% of LyCD utility), [[zhou-2024-jdl-abs-postdisaster-rescue]] (Lyapunov + SCA-in-the-critic + two-timescale), [[gao-2024-sagin-perception-offloading]] (Lyapunov + DDPG/DQN/SGHS; V balancing param explicit), [[qin-2025-matd3-noma-queue-sagin]] (Lyapunov + MATD3 + CVX/GSCRA), [[you-2025-uncertain-maritime-hasac]] (Lyapunov + heterogeneous-agent SAC; "yields small-scale problems" verbatim). Complements the [[lyapunov-optimization]] concept (mechanics) and [[ao-sdr-sca-convex-pipeline]] (classical sibling).
- **`comparisons/j-ppo-vs-pdqn`** (lead 2; flagged as a genuine new-page candidate in derived-batch-2/3 audit routing notes and in [[drl-backbones-across-uav-mec-sources]] / [[ma-2025-pdqn-vehicular-mec]]) — native-hybrid-action head-to-head: on-policy stochastic [[j-ppo|j-PPO]] ([[liu-2026-jppo-en-convntm]]) vs off-policy value-based [[parameterized-dqn|P-DQN]] ([[ma-2025-pdqn-vehicular-mec]]). Explicit method-shape (not shared-instance) framing; "secures a higher reward" / "severe performance degradation" attributions grounded verbatim.
- **`synthesis/safety-and-robustness-mechanisms-in-mec`** (lead 3) — cross-family map of 4 mechanism families by threat / guarantee / cost: hard per-state safe-RL ([[zhang-2025-ssac-mgi-heterogeneous-uav]] MGI), distributionally-robust ([[jia-2025-dro-uav-hap-mec]] DRO+CVaR), bounded-uncertainty robust ([[li-2024-robust-bmappo-multiuav-mec]] Beta-policy MAPPO; [[sun-2024-mfris-semantic-antijamming]] + [[sun-2024-active-passive-ris-receiver]] worst-case RIS anti-jamming), and structural side-step ([[wang-2026-aerial-marine-msar]] known routes; [[wu-2026-terrain-aware-uav-mec]] terrain geometry). DRO conservatism margin correctly marked `not in parse`.

### Pages refreshed / cross-links densified

- **Resolved standing "future page" promises:** [[drl-backbones-across-uav-mec-sources]] (the `j-ppo-vs-pdqn` placeholder → live link + rewritten contrast), [[jia-2025-dro-uav-hap-mec]] (the "future robustness synthesis" promise → [[safety-and-robustness-mechanisms-in-mec]]), [[ma-2025-pdqn-vehicular-mec]] (the "motivate a j-ppo-vs-pdqn page" note → live link), [[query-when-does-dro-beat-drl-for-csi-uncertainty]] (added the synthesis map).
- **`related:`/in-body links added** on [[lyapunov-optimization]], [[qin-2025-bcuav-masac]], [[zhu-2025-lycnn-drl-wpt-mec]], [[zhou-2024-jdl-abs-postdisaster-rescue]], [[gao-2024-sagin-perception-offloading]], [[qin-2025-matd3-noma-queue-sagin]], [[you-2025-uncertain-maritime-hasac]], [[zhang-2025-ssac-mgi-heterogeneous-uav]], [[li-2024-robust-bmappo-multiuav-mec]], [[ddpg-vs-jppo]], [[drl-vs-evolutionary-vs-classical-solvers]] — all bidirectional, none self-referential. Fixed two transient duplicate-`updated` keys introduced mid-edit (gao-2024, qin-2025-matd3) before gating.
- **Meta-docs:** [[index]] — +3 entries (Methodology / Comparisons / Synthesis sections). [[overview]] — analytical-layer tally (findings 14 / synthesis 11→12 / comparisons 4→5 / methodology 2→3) and cross-cutting observations #1 (Lyapunov+DRL → methodology page + 6-source roster), #4 (hybrid-action → j-ppo-vs-pdqn), #6 (CSI uncertainty → robustness synthesis).

### Leads rejected / deferred (with reason)

- **Lead 5 (swarm-intelligence vs evolutionary-MORL vs diffusion-DRL in collaborative beamforming)** — already substantially covered by the existing [[collaborative-beamforming-in-aerial-mec]] synthesis (its "Solver split" section + single-author-group caveat). A dedicated comparison would largely duplicate it; **deferred** to avoid padding.
- **Leads 4 & 8 (sensing-comm-compute tri-function coupling gap; physical-layer GAI vs decision-layer DRL fusion)** — partially grounded ([[zhu-2024-sensing-comm-doppler-uav-swarm]] is sensing+comm with **no MEC offloading**; [[wang-gai-isac-physical-layer]] has **no year in parse** and is a magazine overview), and the gap is already noted in [[collaborative-beamforming-in-aerial-mec]] ("no CB source carries a compute/offloading objective") and [[isac-sensing-in-aerial-mec]]. A standalone gap-analysis page is viable but lower-leverage than the constraint-handling theme; **deferred** to a future ISAC-themed batch.
- **Leads 6 & 7 (classical-solver applicability decision-tree; hardware-validation / sim-to-real synthesis)** — viable but belong to different themes (solver-selection; sim-to-real). To keep this batch context-coherent and well-grounded, **deferred**; the hardware-validation roster is already captured in [[overview]] and several source pages.

### Toolkit

No ratchet needed — the five maintained scripts (`curation_status`, `linkcheck`, `process_refs`, `frontmatter_audit`, `index_audit`, `corpus_counts`) plus the read-only LLM Wiki search/graph API covered state detection, grounding discovery, and all four commit gates. No reusable one-off arose; toolkit stable.

### Gates

**`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits. **`frontmatter_audit.py`** = 516 pages, 0 errors. **`index_audit.py`** = 518/518 indexed, 0 unindexed / 0 duplicate primaries (45 cross-ref mentions informational). New pages + edited meta-docs verified mojibake-free at the byte level. Counts reconciled via `corpus_counts.py`: **171 sources + 234 concepts + 71 entities + 40 derived (14 findings / 12 synthesis / 5 comparisons / 5 queries / 3 methodology / 1 thesis) = 516 typed pages**. Graph **516 nodes / 4534 edges**.

## 2026-06-02 — Audit pass (DERIVED layer — comparisons + methodology + queries + thesis, batch 3/3 FINAL; no new papers)

The **final derived batch** closes Phase B across all layers: **derived batch 3 = comparisons 4 + methodology 2 + queries 5 + thesis 1 = 12 pages**. Tree clean at `772a2b3` (apart from a pre-existing untouched `.kiro/agents/**` edit, left alone). Phase 0 reconciled clean: `curation_status.py --dupes` = **171 raw = 171 curated, 0 uncurated, 0 genuinely-new** (no routing to `mec-wiki-curator`). LLM Wiki API reachable (`allowUnauthenticated:true`, v0.4.16); baseline graph **513 nodes / 4477 edges**. Git + toolkit run through Windows PowerShell (no WSL credential workaround needed).

### Correctness & consistency audit (Phase B — derived batch 3)

Four of twelve pages carried a correctness defect — all four were comparisons (the claim-densest type); the two methodology, five query, and one thesis page verified clean. Every fix is parse-grounded.

- **[[bcsa-frl-vs-bc-uav-masac]] — ungrounded mechanism (same defect as the batch-2 synthesis fix).** The "Where they agree" bullet claimed both papers "acknowledge this contention" and that [[mao-2025-bcsa-frl]] handles it "by leaving the consensus rounds asynchronous to the FRL rounds" — **not in the BCSA-FRL parse** (§V L160+: "we combine the consensus mechanism with FRL model parameter aggregation"; the consensus vote `Rate` (Eq. 12) doubles as the FRL aggregation base weight — consensus is *coupled* per round, not asynchronous), and contradicted by the source page's own "no analysis of blockchain compute overhead" limitation. Rewrote to credit only BC-UAV-MASAC's explicit DOA CPU split (task-compute / block-generation / block-verification under a block-creation-delay constraint, parse-confirmed) and state BCSA-FRL leaves the overhead unquantified — matching the already-corrected [[blockchain-on-edge-trust-layer]].
- **[[ddpg-vs-jppo]] — ungrounded failure mode.** Stated as fact that DDPG "lands in a bad local optimum where it almost never charges … or always charges" — the liu-2026 parse (§V-4 L645) attributes DDPG/TD3/DQN "severe performance degradation" generically to the inability of continuous-/discrete-only frameworks to handle joint continuous-discrete actions; the specific charge-behavior local optimum is **not characterized**. Rewrote to the grounded degradation result + flagged the local-optimum behavior as a plausible-but-uncharacterized mechanism.
- **[[game-theoretic-offloading-formulations]] — stale exhaustiveness claim.** "**Eight** curated sources cast MEC offloading … as a game" reads as a census; at least [[zeng-2024-usv-fleet-collaborative-offloading]] (Stackelberg) and [[you-2025-uncertain-maritime-hasac]] (Markov/stochastic game) also use game formulations and are not in the roster. Softened to "a cluster … using the eight tabulated below as representatives" + named the two extras, without expanding the comparison roster (broadening → synthesizer). In-table game-family assignments spot-checked grounded (he-2019 potential-game/decentralized-NE verbatim; others carried from clean source-batch audits).
- **[[j-ppo-baselines]] — indicative-ranking caveat.** The 5-row encoder ranking is grounded at the top (EN-ConvNTM best; ConvNTM runner-up — the parse quotes EN-ConvNTM's gains *relative to ConvNTM*) and the NeuralMap/raw weaknesses are verbatim (identity-collision, 76.2% gain at 2 UAVs, no-spatial-mechanism), but the exact 3-4-5 total order (ConvLSTM/NeuralMap/raw) is read from the Fig. 4–6 box-plots, not a stated numeric order. Added a one-line indicative caveat.
- **Verified clean (8):**
  - **methodology:** [[ao-sdr-sca-convex-pipeline]] — benaya-2025 "AO, SDR, SCA" verbatim (3 sub-problems, rank-one/SDR+CVX, SCA+first-order-Taylor all parse-confirmed); yao-2025 / tang-2024 / zhang-2019 / liu-2022-miso attributions carried from clean source batches. [[drl-simulation-with-pomdp-formulation]] — liu-2026 hardware (2× RTX 4090, PyTorch 2.1.0, Matplotlib 3.8.4, Ubuntu 20.04), procedure (500 steps/episode, 3000 iters, Ñ=8, K=5), and reward-penalty shaping all verbatim; 3-channel POMDP observation grounded.
  - **queries (5):** [[end-to-end-drl-feasibility-large-scale-mec]] (research-gap framing; idempotent w/ [[no-true-end-to-end-drl-in-corpus]]), [[query-does-en-convntm-generalize-beyond-uav-mec]], [[query-real-world-validation-of-jppo-en-convntm]] (sim-to-real gap flagged in liu-2026 conclusion, grounded), [[query-video-vs-cooperative-perception-offloading-shape]] (bao-2025 transcoding/DDPG/QoE + xie-2026 compression/CMOO + gao-2024 perception-as-state all match clean source pages), [[query-when-does-dro-beat-drl-for-csi-uncertainty]] (jia-2025 DRO+CVaR + wang-2026/wu-2026 structure-side-step grounded from clean source batches).
  - **thesis:** [[hybrid-action-memory-augmented-drl-wins-uav-mec]] — single-source liu-2026 thesis at `confidence: medium / status: supported`; supporting findings ([[en-convntm-beats-baselines]], [[hybrid-action-beats-pure-drl]]) carried from clean derived-batch-1; refutation conditions evergreen.

### Toolkit

No ratchet — the four gate scripts plus targeted parse greps covered the comparison/methodology/query/thesis checks, and the defects were content fixes (ungrounded mechanism, ungrounded failure mode, stale census, indicative-ranking caveat), not new reusable checks. Toolkit stable across the whole audit.

### Gates (derived batch 3)

**`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits. **`index_audit.py`** = 0 unindexed / 0 duplicate primaries (45 cross-ref mentions informational). **`frontmatter_audit.py`** = 513 pages, 0 errors. All four edited pages mojibake-free at the byte level. Graph **513 nodes / 4479 edges** (prose-only edits to already-present nodes; node count unchanged).

### Phase B COMPLETE across all layers

With derived batch 3, the entire wiki has been audited: **171 sources + 234 concepts + 71 entities + 37 derived = 513 typed pages**. Total Phase-B corrections reconstructed from the coverage tracker: ~30 pages corrected across the run (source batches 1/3/4/5/6/7/9/11/12, the synthesis batch, the findings batch, and this comparisons batch), spanning the recurring defect classes — ungrounded numbers, false cross-corpus "first"/negatives/counts, stale counts, mischaracterized mechanisms, and the baseline-margin-misquote — plus corpus-wide consistency sweeps (26-page `source`-tag fix; process-narration → evergreen rewrites) and three toolkit ratchets to `process_refs.py` / `index_audit.py`.

### Routing to `mec-wiki-synthesizer` (derived batch 3 — recorded, not filled)

- **`j-ppo-vs-pdqn` comparison** remains a genuine new-page candidate (flagged in [[drl-backbones-across-uav-mec-sources]] and implied by [[ddpg-vs-jppo]]'s P-DQN caveat) — not minted here.
- **Stale track censuses** (`hierarchical-aerial-mec-design-space` maps 5 of ≥9; `maritime-mec-architectures` 7 of 18; `sagin-satellite-offloading-landscape` 8 and misses [[zheng-2024-semcom-sec-offloading]]) and the game-theory comparison roster (8 representatives of a broader game-theoretic track incl. [[zeng-2024-usv-fleet-collaborative-offloading]], [[you-2025-uncertain-maritime-hasac]]) are candidates for roster refresh as coverage grows. Auditor only softened wording; expanding rosters is broadening.
- Standing concept-layer consolidation notes (swarm-metaheuristic family, hybrid-action family, LEO/NTN cluster, multi-agent actor-critic family, game-theory family, caching cluster, channel-model cluster, video-analytics cluster, trust/secure-aggregation cluster; evolutionary-/generative-/CSI-/PLS-family tag fragmentation) remain open from prior batches.

## 2026-06-02 — Audit pass (DERIVED layer — synthesis batch 2/3; no new papers)

The most cross-source-claim-dense batch in Phase B: **derived batch 2 = all 11 synthesis pages** (alphabetical blockchain-on-edge-trust-layer → sagin-satellite-offloading-landscape). Each synthesis page reasons over many parses at once, so this is the highest-value correctness batch. Tree clean at `ca9a36d` (apart from a pre-existing untouched `.kiro/agents/**` edit, left alone). Phase 0 reconciled clean: `curation_status.py --dupes` = **171 raw = 171 curated, 0 uncurated, 0 genuinely-new** (no routing to `mec-wiki-curator`). LLM Wiki API reachable (`allowUnauthenticated:true`, v0.4.16); baseline graph **513 nodes / 4473 edges**. Synthesis frontmatter valid (11/11, `synthesis` tag present).

### Correctness & consistency audit (Phase B — derived batch 2: synthesis)

Six of eleven synthesis pages carried a correctness defect; five verified clean. Every fix is parse-grounded; the recurring defect classes (stale cross-corpus counts, false negatives, mischaracterized mechanisms, baseline-margin misquotes) all showed up.

- **[[blockchain-on-edge-trust-layer]] — ungrounded mechanism.** Cross-cutting bullet claimed all three sources "acknowledge consensus eats the CPU/energy budget" and that [[mao-2025-bcsa-frl]] handles it "by keeping consensus rounds asynchronous to FL rounds" — **not in the BCSA-FRL parse** (consensus is *coupled* with FRL aggregation each round, §V L178; no "asynchronous" mechanism) and contradicted by the source page's own "blockchain overhead unanalyzed" limitation. Rewrote to credit only the two sources that model the cost (ACBFT `O(n)` vs `O(n²)` broadcast BFT, verbatim; BC-UAV-MASAC block-creation-delay constraint + DOA CPU split) and note BCSA-FRL leaves it unquantified. ACBFT `N=3f+1` + qin-2025 DOA verified grounded.
- **[[cmop-evolutionary-uav-mec-lineage]] — citation overstatement.** "[[huang-2025-cmop-dispersed-computing]] only cites the lineage seed peng-2022" — its REFERENCES cite **both** peng-2022 (ref [38]) and [[huang-2023-mu-aec-task-energy]] (ref [25]), not peng-2024 (confirmed absent). Rewrote. peng-2024→peng-2022 (ref [29]) verified; author rosters confirmed both ways (yuan-wu ×6, jiawen-kang ×4).
- **[[drl-backbones-across-uav-mec-sources]] — false cross-corpus negative.** Claimed the corpus has no "value-decomposition (Qmix/VDN)" source — **false**: [[raivi-2024-jdaco-postdisaster-iot]] uses **VD3QN = VDN + dueling-double-DQN** (parse §V-B, verbatim). Rewrote to acknowledge it (still no mean-field/QMIX, no ~20+ agent regime). Also softened the unverifiable "first HAP-energy-constrained DRL source" → "clearest".
- **[[hierarchical-aerial-mec-design-space]] — stale mechanism + count.** (1) Objective table labelled [[nabi-2025-jour-hierarchical-aerial]]'s third term "UAV-load **variance**"; the parse term is per-UAV **load** (cycles ÷ capacity, Eq. 25a) reported as **average load** — corrected to "UAV load balancing" (matches the batch-6 source fix + [[load-balancing-uav-mec]] concept). (2) "track is now **five** sources strong" undercounts (≥9 tagged `hierarchical-aerial-mec`); reframed as "a representative five".
- **[[maritime-mec-architectures]] — stale count + false negative.** (1) "**Seven** curated sources target the maritime setting" → **18** are tagged `maritime-mec`; reframed as the architecture/tiering subset of a broader track. (2) Gap "no maritime source addresses jamming…" is a **false negative** — [[li-2023-secure-marine-iot-jamming]] (cooperative jamming, parse-confirmed), [[dai-2023-hybrid-noma-fdma-marine]], [[huang-2025-dual-aav-maritime-secure-cb]] all do PLS/jamming; rewrote to scope the gap to the architecture roster + name the PLS sources, keeping the genuine blockchain/zero-trust absence. Added the three to `related`.
- **[[sagin-satellite-offloading-landscape]] — census not exhaustive.** "**Eight** curated sources put a satellite into the offloading hierarchy" omits [[zheng-2024-semcom-sec-offloading]] (LEO + offloading); softened to "a cluster … the eight mapped below" rather than expanding the roster (broadening → synthesizer; recorded as routing note).
- **Verified clean (5):** [[collaborative-beamforming-in-aerial-mec]] (all five CB sources = Geng-Sun group + venue/year verbatim; EMSSA "into IoTs and UAVs simultaneously" verbatim), [[design-recipe-multi-uav-mec]] (single-source liu-2026 recipe; Ω + c₁/c₂/c₃ grounded — idempotent w/ findings), [[drl-vs-evolutionary-vs-classical-solvers]] (explicit 26-source partial-snapshot scope note intact; MISOCP + DRO-overhead caveats consistent — idempotent), [[isac-sensing-in-aerial-mec]] (7-source roster matches tags; AO+SDR+SCA + GenAI-channel split grounded), [[maddpg-vs-masac-in-mec]] (carries the corrected +15.41%/−30.73% vs MADDPG, +13.16%/−29.47% vs PSO — baseline-margin-misquote already fixed).

### Toolkit

No ratchet — the four gate scripts plus targeted parse greps covered the synthesis checks, and the defects were content fixes (stale counts, false negatives, ungrounded mechanisms), not new reusable checks. Toolkit stable for the derived layer.

### Gates (derived batch 2)

**`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits. **`index_audit.py`** = 0 unindexed / 0 duplicate primaries (45 cross-ref mentions informational). **`frontmatter_audit.py`** = 513 all-types + 11 synthesis, 0 errors. All six edited pages mojibake-free at the byte level. Graph **513 nodes / 4473 edges** baseline (prose-only edits + maritime page gained 3 `related` links to already-present nodes; node count unchanged, edges refresh on next rescan).

### Routing to `mec-wiki-synthesizer` (derived batch 2 — recorded, not filled)

- **Stale track censuses are accumulating** — the auditor softened the count claims to non-stale wording, but expanding the track-map rosters is broadening: `hierarchical-aerial-mec-design-space` maps 5 of ≥9 sources; `maritime-mec-architectures` maps 7 of 18; `sagin-satellite-offloading-landscape` maps 8 and misses [[zheng-2024-semcom-sec-offloading]]. The synthesizer may want to refresh these rosters as coverage grows.
- The `j-ppo-vs-pdqn` comparison page flagged inside [[drl-backbones-across-uav-mec-sources]] is a genuine new-page candidate for the synthesizer (not minted here).
- Standing concept-layer consolidation notes (swarm-metaheuristic family, hybrid-action family, LEO/NTN cluster, multi-agent actor-critic family, game-theory family, caching cluster, channel-model cluster, video-analytics cluster, trust/secure-aggregation cluster; evolutionary-/generative-/CSI-/PLS-family tag fragmentation) remain open from prior batches.

### Next: comparisons + methodology + queries + thesis (derived batch 3)

**25 of 37 derived pages audited (findings + synthesis complete).** Remaining: **comparisons 4 + methodology 2 + queries 5 + thesis 1 = 12 pages** in derived batch 3 (resumes at `comparisons/bcsa-frl-vs-bc-uav-masac`). After derived batch 3, the entire non-source layer + all 171 sources will be audited — completing Phase B.

## 2026-06-02 — Audit pass (DERIVED layer — findings batch 1/3; no new papers)

Opens the **derived layer** — the final Phase B layer (37 pages: findings 14 / synthesis 11 / comparisons 4 / methodology 2 / queries 5 / thesis 1) — with **derived batch 1 = all 14 findings** (alphabetical acbft-throughput-increase → uav-count-inverted-u-energy). Findings are the lightest derived type (single-source, one headline number each), so the whole findings set fits one batch; the claim-dense synthesis/comparison/methodology/query pages get smaller subsequent batches. Tree clean at `e3f6acb` (apart from a pre-existing untouched `.kiro/agents/**` edit, left alone). Phase 0 reconciled clean: `curation_status.py --dupes` = **171 raw = 171 curated, 0 uncurated, 0 genuinely-new** (no routing to `mec-wiki-curator`). LLM Wiki API reachable (`allowUnauthenticated:true`, v0.4.16); baseline graph **513 nodes / 4465 edges**.

### Derived-layer batch plan

Slugs in `.curation-out/derived_slugs.txt` (type-grouped); `make_batches.py --size 9 --input` as the mechanical split, hand-adjusted to type-coherent batches sized to the window (derived pages are the most cross-source-claim-dense in the wiki, so smaller than concept batches): **batch 1 = 14 findings**; **batch 2 ≈ 11 synthesis**; **batch 3 = 4 comparisons + 2 methodology + 5 queries + 1 thesis**. Recorded under the new DERIVED section of `.curation-out/audit-coverage.md`.

### Correctness & consistency audit (Phase B — derived batch 1: findings)

Derived-finding checks: type frontmatter (`source`/`confidence`/`replicated`); every headline number grounded in the cited parse; `source`/`related` slugs resolve, non-self-referential, and support the attributed claim; evergreen wording.

- **Correctness fix (stale cross-corpus undercount):** [[asap-swarm-inference-speedup]] still asserted ASAP "is one of only **two** hardware-validated sources in the corpus (the other is [[shao-2024-drl-antijamming-mec]])" — the same undercount the **source-page batch 7** audit already corrected on [[sun-2024-asap-uav-swarm]] (and that `overview.md` records). The corpus has **3 fully hardware-validated** sources — ASAP (24 Jetson + 5 real UAVs), [[shao-2024-drl-antijamming-mec]] (Raspberry Pi/USRP), [[zhang-2020-response-delay-uav-swarm]] (DJI UAVs + 5G NR mmWave testbed) — plus [[qu-ecoei-uav-swarm]] as an airborne proof-of-concept. Rewrote to "one of the few hardware-validated sources … alongside [shao-2024, zhang-2020], with [qu-ecoei] adding an airborne proof-of-concept", matching the source-page/overview wording; `updated`→2026-06-02. The finding (dated 2026-05-30) predated the batch-7 fix and was never refreshed — caught by the cross-corpus-count check.
- **All 14 findings otherwise verified clean** — type frontmatter valid; every headline number grounded verbatim in the cited parse (or flagged figure-derived indicative); `source`/`related` slugs resolve, non-self-referential, and support the claim. Grounding highlights (verbatim against parses):
  - **liu-2026-jppo-en-convntm cluster (6 findings):** [[en-convntm-beats-baselines]] (ΔΩ 9.91/8.06/17.60/14.95/21.21% over ConvNTM + 7.34/11.30/7.62/11.65/6.14% station sweep), [[neuralmap-loses-spatial-info]] (76.2% higher than NeuralMap @2 UAVs), [[finding-optimal-loss-entropy-weight-coefs]] (Table I c₁=0.1→0.9849 / c₂=0.01→0.9891 / c₃=0.5→0.9827; c₂=0 collapse 0.6178; c₃=0.7→0.6148), [[hybrid-action-beats-pure-drl]] (Fig. 6 DDPG/A2C/TD3/DQN; A2C closest, others "severe degradation"), [[uav-count-inverted-u-energy]] (energy "inverted U-shaped trend, initially decreasing then increasing"), [[charging-stations-improve-efficiency]] (Fig. 5 monotonic Ω/fairness/data-collection up, energy down).
  - [[masac-beats-maddpg-sensing-queue]] — per-baseline margins verbatim (vs NT-MASAC/NP-MASAC/**MADDPG**/PSO: sensing +27.59/+36.27/**+15.41**/+13.16%, queue −30.77/−35.71/**−30.73**/−29.47%). The page's own correctness note (an earlier [[maddpg-vs-masac-in-mec]] draft mis-quoted the **PSO** figures as the MADDPG margin) is **accurate** — converges, no change.
  - [[fedleo-delay-accuracy-tradeoff]] (up to 41% delay / 9.39% accuracy headline + MNIST 31.7%/3.643%, CIFAR-10 45.05%/9.39% breakdown), [[bcsa-frl-tolerates-up-to-half-malicious-satellites]] (≈5%/≈6 ms flat across 10–50% malicious; baseline table 6.16%/5.95ms vs 20.05%/7.40ms vs 40.54%/9.31ms; >51% consensus capture), [[acbft-throughput-increase]] ("up to 96.2%" verbatim L35 — the genuine-grounded 96.2%, not the fabricated-96.2% anti-pattern), [[dcb-cuts-satellite-handover-frequency]] ("save 30% handover frequency … vs the rate greedy method" verbatim), [[maritime-three-tier-energy-saving]] ("saves 39.3% of system energy" verbatim), [[no-true-end-to-end-drl-in-corpus]] (idempotent re-check of the source-batch-1 cluster — converges, no change).
- **Pages:** acbft-throughput-increase, asap-swarm-inference-speedup, bcsa-frl-tolerates-up-to-half-malicious-satellites, charging-stations-improve-efficiency, dcb-cuts-satellite-handover-frequency, en-convntm-beats-baselines, fedleo-delay-accuracy-tradeoff, finding-optimal-loss-entropy-weight-coefs, hybrid-action-beats-pure-drl, maritime-three-tier-energy-saving, masac-beats-maddpg-sensing-queue, neuralmap-loses-spatial-info, no-true-end-to-end-drl-in-corpus, uav-count-inverted-u-energy.

### Toolkit

No ratchet needed — the four gate scripts (`linkcheck`, `process_refs`, `index_audit`, `frontmatter_audit`) covered the findings-layer checks, and the cross-corpus-count defect was a content fix, not a new reusable check. Toolkit stable for the derived layer.

### Gates (derived batch 1)

- **`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits. **`index_audit.py`** = 515/515, 0 unindexed / 0 duplicate primaries (45 cross-ref mentions informational). **`frontmatter_audit.py`** = 513 pages, 0 errors. Graph **513 nodes / 4465 edges** baseline (the asap fix added 2 intra-corpus wikilinks to already-present nodes; node count unchanged, edges refresh on next rescan). Meta-doc edits (this log + tracker) verified mojibake-free at the byte level.

### Routing to `mec-wiki-synthesizer` (derived batch 1 — recorded, not filled)

- No new synthesizer gaps from the findings layer — every finding is anchored to a curated source with a grounded headline result, and its cross-links into the synthesis/comparison layer resolve. The standing concept-layer consolidation/synthesis notes (swarm-metaheuristic family, hybrid-action family, LEO/NTN cluster, multi-agent actor-critic family, game-theory family, caching cluster, channel-model cluster, video-analytics cluster, trust/secure-aggregation cluster; evolutionary-/generative-/CSI-/PLS-family tag fragmentation) remain open from prior batches.

### Next: synthesis pages (derived batch 2)

**14 of 37 derived pages audited.** Remaining: **synthesis (11)** in derived batch 2 (resumes at `synthesis/blockchain-on-edge-trust-layer`), then **comparisons 4 + methodology 2 + queries 5 + thesis 1 (12)** in derived batch 3. **23 derived pages remain.** After the derived layer, the entire non-source layer + all 171 sources will be audited — completing Phase B.

## 2026-06-02 — Audit pass (non-source layer — entity batch 4, FINAL entities; no new papers)

Completes the entities-layer audit with **entity batch 4** (11 pages, alphabetical yuben-qu → ziye-jia, positions 61–71 of `.curation-out/entity_slugs.txt`) — the **final entity batch**, so **all 71 entity pages (70 author + the `pytorch` tool) are now audited**. Tree clean at `2a7e38d` (apart from a pre-existing untouched `.kiro/agents/**` edit, left alone). Phase 0 reconciled clean: `curation_status.py --dupes` = **171 raw = 171 curated, 0 uncurated, 0 genuinely-new** (no routing to `mec-wiki-curator`). LLM Wiki API reachable (`allowUnauthenticated:true`, v0.4.16); baseline graph **513 nodes / 4465 edges**.

### Correctness & consistency audit (Phase B — entity batch 4)

Entity-page checks: `author` tag + frontmatter valid; roster reconciles in BOTH directions against source `authors:` lists; affiliation grounded in the parse(s); namesake handling correct; `related`/wikilinks resolve and are non-self-referential; evergreen wording.

- **All 11 pages verified clean — no corrections needed.** Third all-clean entity-layer outcome (after batch 1 and several concept batches); the layer converges rather than churning. `entity_roster_audit.py` flagged **0 claimed-but-absent / 0 present-but-unlisted** across all 70 author entities, so no roster over-claims or omissions to adjudicate this batch.
- **Affiliation grounding spot-checks (in-parse email/affiliation lines, verbatim):** yuben-qu (`quyuben@nuaa.edu.cn`, NUAA — eCoEI bio + ASAP author block); yuguang-fang (`my.fang@cityu.edu.hk`, Dept of Computer Science, City University of Hong Kong — confirmed in MSAR + Maritime-EH parses; in-parse bio Qufu-Normal MS / Case-Western PhD / Boston-U 2nd PhD / U-Florida 2000→Distinguished-2019 / CityU-since-Aug-2022 grounded verbatim); zemin-sun (`sunzemin@jlu.edu.cn`, College of CS&T + KLSCKE, Jilin University); zexiong-wu (`zexiongwu@stu.scau.edu.cn`, College of Mathematics and Informatics, SCAU — across all 4 CMOP parses); zhidu-li (`lizd@cqupt.edu.cn`, CQUPT) + zhuwei-wang (`wangzhuwei@bjut.edu.cn`, Beijing University of Technology) — both in the liu-2026 high-density-MEC author block; zhiyong-feng (`fengzy@bupt.edu.cn`, BUPT + **director, Key Laboratory of Universal Wireless Communications, MoE** — directorship + research interests grounded verbatim in the ISAC-overview + response-delay bios); zhou-su (`zhousu@ieee.org`, School of Cyber Science and Engineering, Xi'an Jiaotong University); ziye-jia (`jiaziye@nuaa.edu.cn`, College of EIE NUAA + National Mobile Communications Research Lab, Southeast University).
- **Namesake / single-identity handling (correct, intact):** zhen-wang — though "Zhen Wang" is a common name, the page's single-identity argument is grounded: identical email (`wangzhen\_jsj@neusoft.edu.cn`, MinerU-escaped underscore) + Dalian-Maritime-University / Dalian-Neusoft-University-of-Information dual affiliation (verbatim in 3 of 4 parses; the 4th lists Dalian Neusoft only) + all four papers supervised by corresponding-author [[bin-lin]] in the maritime/space-air-marine line. No merge/split on a name match alone; documented note intact. No new namesake issues in the batch.
- **Editorial Contributions cross-mentions verified accurate** (all resolve; linkcheck 0 dangling): yuguang-fang↔[[zhen-wang]]/[[qiang-ye]] on the Maritime-EH JCORA paper; zhou-su↔[[minghui-dai]] on the dai-2023 marine line; zhu-han↔[[ziye-jia]]/[[chao-dong]]/[[qihui-wu]] on the NUAA aerial-computing cluster; zemin-sun↔[[geng-sun]]/[[jiahui-li]] on the Jilin aerial-MEC cluster; zexiong-wu↔[[chaoda-peng]]/[[xumin-huang]]/[[yuan-wu]] on the SCAU evolutionary-computation cluster.
- **Pages:** yuben-qu, yuguang-fang, zemin-sun, zexiong-wu, zhen-wang, zhidu-li, zhiyong-feng, zhou-su, zhu-han, zhuwei-wang, ziye-jia.

### Toolkit

No ratchet needed — `entity_roster_audit.py` (with the batch-2 `respaced` match + roster-region scoping) re-ran **0/0 both directions** across all 70 author entities. The toolkit is stable for the entities layer; no new reusable need surfaced this batch.

### Gates (entity batch 4)

- **`linkcheck.py`** = NO DANGLING LINKS (5 orphans are non-wiki files: README/schema/full/MinerU parses — not entity pages). **`process_refs.py`** = 0 files / 0 hits. **`index_audit.py`** = 515/515, 0 unindexed / 0 duplicate primaries (45 cross-ref mentions informational). **`frontmatter_audit.py --type entity`** = 71 pages, 0 errors. **`entity_roster_audit.py`** = 0/0 both directions. Graph **513 nodes / 4465 edges** (no page edits this batch — audit-only). Meta-doc edits (this log + tracker) verified mojibake-free at the byte level.

### Routing to `mec-wiki-synthesizer` (entity batch 4 — recorded, not filled)

- No new synthesizer gaps from this batch. Every co-author named in the batch-4 rosters already has an entity page or is correctly left unlinked. The standing concept-layer consolidation/synthesis notes (swarm-metaheuristic family, hybrid-action family, LEO/NTN cluster, multi-agent actor-critic family, evolutionary-/generative-/CSI-family tag fragmentation) remain open from prior batches.

### Next: the DERIVED layer (final non-source layer)

**All 171 source + 234 concept + 71 entity pages are now audited.** The only non-source layer remaining is the **derived layer** — findings 14 / synthesis 11 / comparisons 4 / methodology 2 / queries 5 / thesis 1 = **37 pages** — across subsequent batched invocations.

## 2026-06-02 — Audit pass (non-source layer — entity batch 3; no new papers)

Continues the entities-layer audit with **entity batch 3** (20 pages, alphabetical qingqing-wu → yuan-wu, positions 41–60 of `.curation-out/entity_slugs.txt`), the batch carrying the four adjudicated present-but-unlisted roster hits surfaced in batches 1–2. Tree clean at `ab0bdce` (apart from a pre-existing untouched `.kiro/agents/**` edit, left alone). Phase 0 reconciled clean: `curation_status.py --dupes` = **171 raw = 171 curated, 0 uncurated, 0 genuinely-new** (no routing to `mec-wiki-curator`). LLM Wiki API reachable (`allowUnauthenticated:true`, v0.4.16); baseline graph **513 nodes / 4459 edges**.

### Correctness & consistency audit (Phase B — entity batch 3)

Entity-page checks: `author` tag + frontmatter valid; roster reconciles in BOTH directions against source `authors:` lists; affiliation grounded in the parse(s); namesake / career-move handling correct; `related`/wikilinks resolve and are non-self-referential; evergreen wording.

- **Roster corrections (all 4 carried hits adjudicated against the source `authors:` frontmatter and the parse author/affiliation block before editing — all confirmed GENUINE same-author omissions, 0 over-claims):**
  - [[xuemin-shen]] — **2 genuine omissions ADDED.** [[chen-2024-ulse-game]] (parse: "Xuemin Sherman Shen … University of Waterloo … sshen@uwaterloo.ca", Fellow) and [[wang-gai-isac-physical-layer]] (parse: "Xuemin (Sherman) Shen is with University of Waterloo, Canada"; bio "XUEMIN (SHERMAN) SHEN [F] (sshen@uwaterloo.ca)") — identical Waterloo affiliation + email confirm the same person. Count 4→6.
  - [[yuan-wu]] — **2 genuine omissions ADDED.** [[chen-2023-dotora-air-ground-online]] (parse: "Yuan Wu is with the State Key Lab of Internet of Things for Smart City, University of Macau … yuanwu@um.edu.mo", corresponding author) and [[chen-2024-ulse-game]] (parse: same Macau lab + `yuanwu@um.edu.mo`, corresponding author) — identical University-of-Macau affiliation + email confirm the same person; both are air-ground / UAV-LEO game-theoretic offloading papers in the ying-chen group. Count 10→12.
  - Reciprocal cross-links are already present on the source pages (chen-2024-ulse-game / chen-2023-dotora / wang-gai-isac all sit in the relevant clusters); the additions are author→source links between already-present nodes.
- **Evergreen-wording fix:** [[qiqi-xie]] Contributions said the identity was "previously listed as a lower-priority candidate in the 2026-05-29 follow-up log and now confirmed" — a dated-run / process-narration reference. Dropped it; the grounded single-identity statement (identical SCAU College of Mathematics and Informatics affiliation across both sources) stands on its own. `updated`→2026-06-02.
- **Affiliation grounding spot-checks (in-parse affiliation/email lines, verbatim):** qingqing-wu (`qingqingwu@sjtu.edu.cn`, Dept of Electronic Engineering, Shanghai Jiao Tong University — confirmed in the URLLC parse; the documented NUS-`elewuqq@nus.edu.sg` earlier-career namesake note on zeng-2019-tutorial / wu-2018-multiuav is grounded and left pending human confirmation, not merged); Shen→Waterloo and Wu→Macau as above.
- **Verified clean** (frontmatter valid; affiliation grounded via in-parse email/affiliation lines; rosters reconcile both directions; links resolve & non-self-referential; evergreen wording): qingqing-wu (SJTU; NUS namesake documented), qiqi-xie (SCAU — wording-fixed), shengli-xie (GDUT), shichao-li (GUET), shuang-liang (NENU + Jilin U), tony-q-s-quek (SUTD), victor-c-m-leung (Shenzhen MSU-BIT / Shenzhen U / UBC), walid-saad (Virginia Tech / Wireless@VT), wei-zhang (Shandong CSC / NSCC-Jinan — common name, disambiguated by identical lab + co-author roster), weifeng-zhong (GDUT), xumin-huang (GDUT + U Macau), yang-fu (NCEPU), yangbo-liu (NWPU), yanheng-liu (Jilin U), yijie-xun (NWPU), ying-chen (BISTU), yong-wang (Central South U — common name, disambiguated by `ywang@csu.edu.cn`; wang-acve venue/year correctly `not in parse`), yong-zeng (NUS — UAV-comms foundations). (Plus the three corrected: xuemin-shen, yuan-wu, qiqi-xie.)

### Toolkit

No ratchet needed — `entity_roster_audit.py` (with the batch-2 `respaced` match + roster-region scoping) flagged exactly the 4 carried hits as `strict` full-name matches with 0 false positives, and re-ran post-edit to **0 claimed-but-absent / 0 present-but-unlisted** across all 70 author entities. The toolkit is stable for the entities layer.

### Gates (entity batch 3)

- **`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits. **`index_audit.py`** = 0 unindexed / 0 duplicate primaries (45 cross-ref mentions informational). **`frontmatter_audit.py --type entity`** = 71 pages, 0 errors. **`entity_roster_audit.py`** = 0/0 both directions. Edited pages (xuemin-shen, yuan-wu, qiqi-xie) verified mojibake-free at the byte level. Graph **513 nodes / 4459 edges** baseline (the three corrected pages net +4 intra-corpus author→source links between already-present nodes; node count unchanged, edge count refreshes on next rescan).

### Routing to `mec-wiki-synthesizer` (entity batch 3 — recorded, not filled)

- No new synthesizer gaps from this batch. Every co-author named in the batch-3 rosters either already has an entity page or is correctly left unlinked; the qingqing-wu NUS-vs-SJTU namesake question is a documented identity note (left pending human confirmation, not a coverage gap). The standing concept-layer consolidation/synthesis notes (swarm-metaheuristic family, hybrid-action family, LEO/NTN cluster, multi-agent actor-critic family, evolutionary-/generative-/CSI-family tag fragmentation) remain open from prior batches.

### Next: entity batch 4 (final entities), then derived (37)

With entity batches 1–3 done (60 of 71), **11 entity pages remain** (batch 4: yuben-qu → ziye-jia, positions 61–71), then the **derived layer** (findings 14 / synthesis 11 / comparisons 4 / methodology 2 / queries 5 / thesis 1 = 37) — ≈ **48 non-source pages** across subsequent batched invocations.

## 2026-06-02 — Audit pass (non-source layer — entity batch 2; no new papers)

Continues the entities-layer audit with **entity batch 2** (20 pages, alphabetical jiacheng-wang → qihui-wu, positions 21–40 of `.curation-out/entity_slugs.txt`), the batch carrying the real roster signal flagged by batch 1. Tree clean at `3ac1a37` (apart from a pre-existing untouched `.kiro/agents/**` edit, left alone). Phase 0 reconciled clean: `curation_status.py --dupes` = **171 raw = 171 curated, 0 uncurated, 0 genuinely-new** (no routing to `mec-wiki-curator`). LLM Wiki API reachable (`allowUnauthenticated:true`, v0.4.16); baseline graph **513 nodes / 4456 edges**.

### Correctness & consistency audit (Phase B — entity batch 2)

Entity-page checks: `author`/`tool` tag + frontmatter valid; roster reconciles in BOTH directions against source `authors:` lists; affiliation grounded in the parse(s); namesake / career-move handling correct; `related`/wikilinks resolve and are non-self-referential; evergreen wording.

- **Roster corrections (every flag adjudicated against the source `authors:` frontmatter and the parse author/affiliation block before editing):**
  - [[jiawen-kang]] — **2 genuine omissions ADDED.** [[du-2023-maddpg-service-placement-agin]] (parse: "Jiawen Kang is with the School of Automation, Guangdong University of Technology … kavinkang@gdut.edu.cn", Senior Member) and [[ye-2025-aigc-diffusion-contract]] (parse: "Dongdong Ye, Shuting Cai, Jiawen Kang, and Rong Yu are with the School of Automation, GDUT … kavinkang@gdut.edu.cn") — identical affiliation+email confirm the same person; both fit the CMOP-evolutionary / generative-AI threads. Count 12→14. The batch-1-flagged "claimed-but-absent" mao-2025-bcsa-frl / qin-2025-bcuav-masac were **tool false positives** (Kang is correctly NOT an author of either — they appear only as a prose contrast-mention in the editorial Contributions section); fixed at the tool level.
  - [[jingjing-wang]] — **1 genuine omission ADDED.** [[yang-2020-loadbalance-multiuav-iot]] (parse: Jingjing Wang at Dept of Electronic Engineering, Tsinghua University, Shuimu Tsinghua Scholar; co-author [[chunxiao-jiang]]). Web-confirmed Tsinghua-PhD → Beihang-faculty career move in the same AI/ML-wireless + swarm-intelligence niche; shared co-author Chunxiao Jiang → same person (documented, mirrors batch-1 [[haixia-peng]]). Count 2→3.
  - [[qiang-ye]] — **1 genuine over-claim REMOVED.** [[dai-2023-hybrid-marine-mmwl]] author list (Minghui Dai / Ning Huang / Yuan Wu / Liping Qian / Bin Lin / Zhou Su / Rongxing Lu) has **no Qiang Ye**; removed from roster + the matching Contributions mention, fixing the stale count (body said "6 sources" but listed 7). Remaining 6 all confirmed to list him.
  - [[jie-xu]] — **namesake split kept distinct + documented.** The strict "Jie Xu" hits on [[xu-2018-uav-wpt-trajectory]] / [[zeng-2019-rotary-wing-energy-min]] are the **GDUT Jie Xu** (`jiexu@gdut.edu.cn`, School of Information Engineering, WPT/rotary-wing with Yong Zeng + Rui Zhang) — distinct from the entity's **CUHK-Shenzhen ISAC** Jie Xu (IEEE Fellow). Added an explicit disambiguation note + cross-links (mirrors batch-1 hao-sun/geng-sun); NOT added to the roster.
  - [[liping-qian]] — the "claimed-but-absent li-2023-secure-marine-iot-jamming" was a **tool false positive**, not a page defect: the parse + frontmatter spell the name "Li Ping Qian" (corresponding author, `lpqian@zjut.edu.cn` = entity). Roster claim is CORRECT; fixed at the tool level. No page change.
- **Verified clean** (frontmatter valid; affiliation grounded via in-parse email/affiliation lines; rosters reconcile; links resolve & non-self-referential; evergreen): jiacheng-wang (NTU CCDS), jiadai-wang (NWPU), jiahui-li (Jilin U + SUTD), jiajia-liu (NWPU), kaoru-ota (Muroran IT), kezhi-wang (Northumbria), lihan-liu (Beijing Wuzi U), liping-qian (ZJUT), mianxiong-dong (Muroran IT), minghui-dai (U Macau), mohammad-mozaffari (Virginia Tech), nei-kato (Tohoku U), ning-zhang (U Windsor), peng-qin (NCEPU), **pytorch** (`tool` tag, no author roster — correct), qihui-wu (NUAA). (Plus the four corrected.)

### Toolkit ratchet (entity batch 2 — `entity_roster_audit.py`)

Two principled refinements (README table updated), both regression-checked across all 70 author entities:

- **`respaced` match strength** — treats "Li Ping Qian" ≡ "Liping Qian" (identical once interior spaces are removed; guarded so two single-token names cannot collapse). As strong as `strict` for over-claim suppression; cannot create new namesake merges. Cleared the liping-qian false over-claim.
- **Roster-region scoping** — roster *claims* are read only from the region before the first `## Contributions` heading (frontmatter `related:` + intro + bulleted source list); the free-form Contributions commentary (which deliberately contrast-mentions sources an author did NOT write) is no longer mis-counted as a claim. Cleared the jiawen-kang mao/qin false over-claims. Present-but-unlisted still suppresses on the whole-page link set.
- Post-edit tool state: **0 claimed-but-absent**; present-but-unlisted down to the 4 batch-3 items.

### Gates (entity batch 2)

- **`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits. **`index_audit.py`** = 515 catalogue-able, 0 unindexed / 0 duplicate primaries (45 cross-ref mentions informational). **`frontmatter_audit.py --type entity`** = 71 pages, 0 errors (all-types 513, 0). Edited pages verified mojibake-free at the byte level. Graph **513 nodes / 4456→4459 edges** (the four corrected pages net +3 intra-corpus author→source links between already-present nodes; node count unchanged).

### Routing to `mec-wiki-synthesizer` (entity batch 2 — recorded, not filled)

- The remaining present-but-unlisted hits — [[xuemin-shen]] (chen-2024-ulse-game, wang-gai-isac-physical-layer) and [[yuan-wu]] (chen-2023-dotora-air-ground-online, chen-2024-ulse-game) — are **correctness items for entity batch 3**, not synthesizer gaps. No clearly-recurring author within batch 2's rosters lacks an entity page.

### Next: entity batches 3–4, then derived (37)

With entity batches 1–2 done, **31 entity pages remain** (batch 3: qingqing-wu → yuan-wu, 20; batch 4: yuben-qu → ziye-jia, 11), then the **derived layer** (findings 14 / synthesis 11 / comparisons 4 / methodology 2 / queries 5 / thesis 1 = 37) — ≈ **68 non-source pages** across subsequent batched invocations.

## 2026-06-01 — Audit pass (non-source layer — entity batch 1; no new papers)

Opens the **entities-layer** audit with **entity batch 1** (20 pages, alphabetical bin-lin → hui-kang, positions 1–20 of `.curation-out/entity_slugs.txt`). All 171 source pages and all 234 concept pages were audited in prior passes; the 71-page entity layer (70 author + 1 tool `pytorch`) splits into 4 batches of 20/20/20/11 via `make_batches.py --size 20`. Tree clean at `6402403` (apart from a pre-existing untouched `.kiro/agents/**` edit). Phase 0 reconciled clean: `curation_status.py --dupes` = **171 raw = 171 curated, 0 uncurated, 0 genuinely-new** (no routing to `mec-wiki-curator`). LLM Wiki API reachable (`allowUnauthenticated:true`, v0.4.16); baseline graph **513 nodes / 4456 edges**.

### Correctness & consistency audit (Phase B — entity batch 1)

Entity-page checks: `author`/`tool` tag + frontmatter valid; roster of authored sources reconciles in BOTH directions against source `authors:` lists; affiliation grounded in the parse(s); namesake / affiliation-move handling correct; `related`/wikilinks resolve and are non-self-referential; evergreen wording.

- **All 20 verified clean — no corrections needed.** Frontmatter valid (`author` tag present on all 20). Rosters reconcile in both directions: `entity_roster_audit.py` reports **0 claimed-but-absent and 0 present-but-unlisted** for every batch-1 entity, confirmed against the source `authors:` frontmatter and the parses.
- **Affiliation grounding spot-checks (in-parse email/affiliation lines, verbatim):** [[bin-lin]] (`binlin@dlmu.edu.cn`, Dalian Maritime University — confirmed across the two-tier-marine / hybrid-NOMA-FDMA / secure-marine-IoT / DLRL-maritime / MSAR parses); [[bomin-mao]] (`maobomin@nwpu.edu.cn`, NWPU School of Cybersecurity + Aero-Space-Ground-Ocean lab — lead/corresponding author across the NTN-caching / IRS-NOMA-FL / FSO-LEO-routing parses); [[hao-sun]] (`sunhaosn@nuaa.edu.cn`) + [[chao-dong]] (`dch@nuaa.edu.cn`), both NUAA, confirmed in the ASAP parse author block (Hao Sun / Yuben Qu / Chao Dong / Qihui Wu — roster reconciles); [[hui-kang]] (`kanghui@jlu.edu.cn`) + [[boxiong-wang]] (`wangbx0320@163.com`), both Jilin University, confirmed in the SWIPT-MEC acknowledgment block.
- **Namesake / affiliation-move handling (correct, intact):** [[fuhong-song]] — SWJTU→Guizhou-Univ-of-Finance student→faculty move, identity confirmed via shared co-author Huanlai Xing + shared niche (note intact, not a namesake); [[haixia-peng]] — Waterloo→Xi'an Jiaotong move documented in both parses (note intact); [[hao-sun]] — explicit "distinct from the Jilin/NTU [[geng-sun]]; surname-only collision" disambiguation intact; [[dusit-niyato]] — "most frequently recurring author … 20 sources" headline confirmed exactly (roster tool: niyato 20 = corpus max, then [[geng-sun]] 16, [[jiawen-kang]] 14, [[jiahui-li]] 13, [[qingqing-wu]] 12).
- **Pages:** bin-lin, bomin-mao, boxiong-wang, chao-dong, chaoda-peng, christopher-brinton, chunhui-qu, chunxiao-jiang, dong-jun-han, dusit-niyato, fuhong-song, geng-sun, haijun-zhang, haixia-peng, hao-hao, hao-sun, hongbin-chen, hongrui-miao, hongzhi-guo, hui-kang.

### Toolkit ratchet (entity batch 1)

- Added **`tools/wiki/entity_roster_audit.py`** (README table updated): reconciles author-entity rosters against source `authors:` lists in both directions — **claimed-but-absent** (entity links a source whose author list lacks a matching name) and **present-but-unlisted** (a source lists a matching author the entity does not link) — with `strict` (full-name) vs `loose` (first+last token) match strengths. Advisory-only (always exit 0); it never decides identity. Fixed its `authors:` parser during this batch to handle BOTH YAML styles (inline flow list + block list), which cleared 5 false-positive over-claims (multi-line block lists had been read as empty). Net real signal carried forward to batches 2–3: [[jiawen-kang]] 2 genuine claimed-but-absent (mao-2025-bcsa-frl, qin-2025-bcuav-masac) + omissions to confirm (du-2023, ye-2025); plus jie-xu (known GDUT/CUHK-Shenzhen namesake split), jingjing-wang, qiang-ye, liping-qian, xuemin-shen, yuan-wu present-but-unlisted hits to adjudicate against the parses before any edit.

### Gates (entity batch 1)

- **`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits. **`index_audit.py`** = 515 catalogue-able, 0 unindexed / 0 duplicate primaries (45 cross-ref mentions informational). **`frontmatter_audit.py --type entity`** = 71 pages, 0 errors (all-types 513, 0 errors). Graph baseline **513 / 4456** (no page edits this batch — audit-only). `log.md` edited with file tools, verified mojibake-free.

### Routing to `mec-wiki-synthesizer` (entity batch 1 — recorded, not filled)

- The roster-reconciliation signal above (candidate omissions on jiawen-kang / jingjing-wang / qiang-ye / liping-qian / xuemin-shen / yuan-wu, and the jie-xu namesake split) is a set of **correctness items for entity batches 2–3**, not synthesizer gaps. No clearly-recurring author lacks an entity page within batch 1's roster — every co-author named in these 20 pages either already has an entity page or is correctly left unlinked.

### Next: entity batches 2–4, then derived (37)

With entity batch 1 done, **51 entity pages remain** (batches 2–4: 20 + 20 + 11), then the **derived layer** (findings 14 / synthesis 11 / comparisons 4 / methodology 2 / queries 5 / thesis 1 = 37) — ≈ **88 non-source pages** across subsequent batched invocations.

## 2026-06-01 — Audit pass (non-source layer — concept batch 12, FINAL; no new papers)

Closes the concept-layer audit with **concept batch 12** (14 pages, alphabetical unicast-multicast-cooperation → zero-trust-architecture, positions 221–234 of `.curation-out/concept_slugs.txt`). **All 234 concept pages are now audited** (concept batches 1–12); all 171 source pages were audited in source batches 1–12. Tree clean at `8114aff`. Phase 0 reconciled clean: `curation_status.py --dupes` = **171 raw = 171 curated, 0 uncurated, 0 genuinely-new** (no routing to `mec-wiki-curator`). LLM Wiki API reachable (`allowUnauthenticated:true`, v0.4.16); baseline graph **513 nodes / 4456 edges**.

### Correctness & consistency audit (Phase B — concept batch 12)

Concept-page checks: definition grounded in the source(s)/parse it cites, no invented numbers/overclaims, `related`/wikilinks resolve and are non-self-referential, tags reused, evergreen wording.

- **Correctness fix (mischaracterized link model):** [[wireless-backhaul]] described the [[ma-2025-pdqn-vehicular-mec]] inter-RSU link as "a fixed-rate link" — the parse models no rate for it. It models a **fixed, small per-hop transmission delay between adjacent RSUs** ($t^{inter}$, propagation-dominated, scaled by the number of road segments $\Delta x$ a relayed task crosses; the relay is needed because adjacent-RSU or cloud offload is routed via the vehicle's directly-connected RSU). Rewrote to the grounded delay model. The page's other flavor — HAP-as-backhaul in [[liu-2025-haps-uav-maritime-iot]] — is grounded verbatim ("HAP provides … wireless backhaul links for UAVs"). `updated`→2026-06-01.
- **Grounding spot-checks (verbatim against parses):** [[unicast-multicast-cooperation]] (liu-2025-haps L39/41/205: HAP provides H2V unicast + backhaul to UAVs, UAVs are multicast access terminals; "performance of multicast transmission is hampered by the worst channel conditions among the covered vessels"; SIC decodes multicast first, then unicast via the residual signal — verbatim); [[value-decomposition-network]] (raivi-2024 contribution 3 + §V-B: VD3QN = VDN + D3QN, $Q_{tot}=\sum_\eta Q_\eta(s_\eta,a_\eta;\delta)$, cooperative learning to minimize energy+delay while maximizing IoT coverage — verbatim); [[virtual-machine-multiplexing]] (liu-2022 L25/contribution-2: VM multiplexing on a shared PM, degradation factor $D>0$ as the percentage increase in expected service time under I/O interference, "no works … with different amount of data in different VMs" → optimizes the number of VMs — verbatim); [[whale-optimization-algorithm]] (wu-2025-iopo §V-E: WOA as the stage-2 solver for the non-convex IRS phase-shift subproblem given the fixed offloading decision, 50% spiral-route/shrink-wrap, continuous — verbatim, $f_{WOA}(\cdot)$); [[video-transcoding-tradeoff]] + [[video-analytics-offloading]] (bao-2025: jointly optimize offloading ratio + transcoding ratio + HAP computation-resource allocation via DDPG; bitrate compression degrades analytics accuracy — verbatim three knobs); [[walker-star-constellation]] (han-2024-sagin §VI: walkerStar function in MATLAB, 80 LEO sats / 5 orbits / 800 km / 85° inclination / 15° min elevation — verbatim); [[wireless-power-transfer]] (zhu-2025: per-slot harvest-then-compute/offload + long-term energy efficiency under queue stability — grounded); [[yolov7-object-detection]] (gao-2024-sagin: YOLOv7 type/behavior recognition fused with mmWave radar into the DRL state — grounded); [[zero-trust-architecture]] (mao-2025-bcsa-frl: blockchain/consensus + reputation aggregation against adversarial votes — grounded).
- **Verified clean** (definition grounded, no invented numbers/overclaims, links resolve & non-self-referential, tags reused, evergreen): unicast-multicast-cooperation, value-decomposition-network, vehicle-fog-computing, vehicular-mec, video-analytics-offloading, video-transcoding-tradeoff, virtual-machine-multiplexing, walker-star-constellation, whale-optimization-algorithm, wireless-power-transfer, yolov7-object-detection, zero-trust-architecture (plus the one corrected: wireless-backhaul).

### Gates (concept batch 12)

- **`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits. **`index_audit.py`** = 515 catalogue-able, 0 unindexed / 0 duplicate primaries (45 cross-ref mentions informational). **`frontmatter_audit.py --type concept`** = 234 pages, 0 errors. Graph baseline **513 / 4456** (the wireless-backhaul edit was prose-only on already-present wikilinks; node/edge counts unchanged). `log.md` edited with file tools, verified mojibake-free.

### Routing to `mec-wiki-synthesizer` (concept batch 12 — recorded, not filled)

- **Swarm/metaheuristic-family synthesis (standing, final reinforcement).** [[whale-optimization-algorithm]] closes out the standing swarm/metaheuristic family ([[binary-whale-optimization]], [[multi-verse-optimizer]], [[salp-swarm-algorithm]], [[particle-swarm-optimization]], [[gravitational-search-algorithm]], [[ant-colony-optimization]], [[self-adaptive-global-best-harmony-search]]); the family synthesis/comparison page remains the strongest standing concept-layer routing candidate (not a merge).
- **Video-analytics cluster.** [[video-analytics-offloading]] / [[video-transcoding-tradeoff]] / [[qoe-modeling-mec]] / [[yolov7-object-detection]] form a tight workload-class cluster around [[bao-2025-ddpg-video-offloading]] + [[sun-2024-ues-video-analytics-disaster]]; candidate for a short synthesis tie.
- **Trust/secure-aggregation cluster.** [[zero-trust-architecture]] / [[blockchain-for-fl-aggregation]] / [[csra-cold-start-reputation-aggregation]] / [[ccvm-correction-voting]] / [[byzantine-fault-tolerant-consensus]] / [[fl-poisoning-attacks]] form a comparable secure-FL/consensus cluster around [[mao-2025-bcsa-frl]]; candidate for a secure-aggregation synthesis.
- No new tag fragmentation introduced this batch.

### Concept layer complete — next: entities (71), then derived (37)

With concept batch 12 done, **all 234 concept pages and all 171 source pages are audited.** The non-source layer remaining is **entities (71: 70 author + pytorch)** — next — then **derived pages (findings 14 / synthesis 11 / comparisons 4 / methodology 2 / queries 5 / thesis 1 = 37)**, ≈ **108 pages** across subsequent batched invocations.

## 2026-06-01 — Audit pass (non-source layer — concept batch 11; no new papers)

Continues the non-source-layer audit into **concept batch 11** (20 pages, alphabetical stochastic-geometry-network-analysis → uav-trajectory-control, positions 201–220 of `.curation-out/concept_slugs.txt`). Tree clean at `7e2cc77`. Phase 0 reconciled clean: `curation_status.py --dupes` = **171 raw = 171 curated, 0 uncurated, 0 genuinely-new** (no routing to `mec-wiki-curator`). LLM Wiki API reachable (`allowUnauthenticated:true`, v0.4.16); baseline graph **513 nodes / 4455 edges**.

### Correctness & consistency audit (Phase B — concept batch 11)

Concept-page checks: definition grounded in the source(s)/parse it cites, no invented numbers/overclaims, `related`/wikilinks resolve and are non-self-referential, tags reused, evergreen wording.

- **Correctness fix (math-clarity inversion):** [[task-redundancy-for-reliability]] said the redundancy success probability "$1 - \prod_j \varphi_j$ … **falls** geometrically with $k$" — backwards. The huang-2025 parse (Eq. 1) defines $P_i = 1 - \prod_{j=1}^J \rho_{i,j}\varphi_j$ as the **success** probability; what falls geometrically with the redundancy count is the *joint failure* product $\prod_j \varphi_j$ (→0), which drives $P_i$ **up** toward 1. Rewrote to make the success/failure direction correct and dropped the unsupported "(or a quorum, depending on verification)" aside — the parse's reliability constraint $C_3: P_i \ge R_i$ is at-least-one-success, not quorum. `updated`→2026-06-01.
- **Soft-overclaim fix (unverifiable cross-corpus "first"):** [[terrain-aware-channel-model]] ended "the wiki's **first** deterministic-geometric channel model" — the same unverifiable cross-corpus superlative pattern softened in batches 5/6/7/9/10. Rewrote to a grounded contrast ("a deterministic-geometric channel model — distinct from the statistical LoS-probability models used across most aerial-MEC sources, see [[blockage-aware-channel-model]]") without the corpus-wide "first" claim. The companion [[blockage-aware-channel-model]] page already frames wu-2026 as "a geometric variant" without a "first" — now consistent. `updated`→2026-06-01.
- **Grounding spot-checks (verbatim against parses):** [[stochastic-geometry-network-analysis]] (jiang-2025: 2D homogeneous PPP for BSs + stationary point processes for CUs/STs; area communication coverage probability under SIR + area radar detection coverage probability under CFAR — "stochastic geometry"/"PPP Modelling" verbatim); [[successive-hover-and-fly-trajectory]] (xu-2018 §V-A: hover at Γ optimal locations + fly at max speed along a min-distance TSP tour, SCP refinement, closed-form K=2, asymptotic optimality as charging duration grows — verbatim); [[three-tier-cloud-edge-end]] (ma-2025: "three-layer task offloading architecture … local computation, edge server, and cloud layers", N vehicles / M RSU-MEC / 1 cloud — verbatim); [[terahertz-communication]] (wu-2025: THz 200–400 GHz in the sim setup; "severe THz wave propagation attenuation and insufficient diffraction" + water-vapor absorption + IRS remedy — verbatim); [[task-offloading]] / [[uav-charging-scheduling]] / [[uav-trajectory-control]] (liu-2026: $h_u=35$ m, $v_u=10$ m/s, $q=0.25$, $K=5$, hybrid clip $c_1=0.1/c_2=0.01/c_3=0.5$ — verbatim source setup); [[theil-fairness-index]] (peng-2025 §3.6: coverage fairness index $\bar{TL}(t)$ based on the Theil coefficient, entropy-based, "lower Theil coefficient indicates greater fairness" — verbatim); [[trust-region-policy-optimization]] (liu-2024: HATRPO backbone + HATRPO-UCB, Beta-policy actor — matches source page); [[two-timescale-optimization]] (sun-2025-tjcct: short-timescale price-incentive + matching / long-timescale convex trajectory, stability + polynomial complexity proved — grounded); [[task-migration]] (zhang-2025-mcma two-stage MA-DRL + Informer prediction — matches the source-batch-11 correction); [[uav-mobile-relaying]] (zeng-2016 staircase water-filling + info-causality; hu-2019 relay+edge-server; zhao-2019 multihop AF/DF — all match audited source pages).
- **Verified clean** (definition grounded, no invented numbers/overclaims, links resolve & non-self-referential, tags reused, evergreen): stochastic-geometry-network-analysis, successive-hover-and-fly-trajectory, task-migration, task-offloading, task-priority-in-mec, td3, terahertz-communication, three-tier-cloud-edge-end, theil-fairness-index, traffic-aware-offloading, trust-region-policy-optimization, two-stage-decomposition, two-timescale-optimization, uav-charging-scheduling, uav-data-collection, uav-enabled-its, uav-mobile-relaying, uav-trajectory-control (plus the two corrected: task-redundancy-for-reliability, terrain-aware-channel-model).

### Gates (concept batch 11)

- **`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits. **`index_audit.py`** = 515 catalogue-able, 0 unindexed / 0 duplicate primaries (45 cross-ref mentions informational). **`frontmatter_audit.py --type concept`** = 234 pages, 0 errors. Graph baseline **513 / 4455** (prose-only edits on already-present wikilinks; node/edge counts unchanged). `log.md` edited with file tools, verified mojibake-free.

### Routing to `mec-wiki-synthesizer` (concept batch 11 — recorded, not filled)

- **Channel-model cluster.** [[terrain-aware-channel-model]] / [[blockage-aware-channel-model]] / [[air-to-ground-channel-model]] / [[terahertz-communication]] / [[csi-estimation-error]] span statistical-LoS / geometric / THz channel families with no single synthesis page; candidate for a channel-modeling synthesis.
- **TRPO/PPO trust-region family (standing, reinforced).** [[trust-region-policy-optimization]] joins the on-policy [[ppo]] / [[mappo]] / [[heterogeneous-agent-rl]] cluster and the multi-agent actor-critic comparison candidate flagged in batch 7.
- **Decomposition-pattern pair.** [[two-stage-decomposition]] + [[two-timescale-optimization]] are distinct but adjacent solver-structure patterns (spatial-stage vs temporal-scale decoupling); a short synthesis tie may help.
- **Fairness-metric set.** [[theil-fairness-index]] + [[jains-fairness-index]] + [[spatial-equity-index]] + [[fairness-metrics-in-mec]] form a comparable fairness-metric set; [[fairness-metrics-in-mec]] may already be the natural synthesis home (synthesizer to confirm).
- No new tag fragmentation introduced this batch.

## 2026-06-01 — Audit pass (non-source layer — concept batch 10; no new papers)

Continues the non-source-layer audit into **concept batch 10** (20 pages, alphabetical rotary-wing-propulsion-energy-model → stochastic-game, positions 181–200 of `.curation-out/concept_slugs.txt`). Tree clean at `4797ddd`. Phase 0 reconciled clean: `curation_status.py --dupes` = **171 raw = 171 curated, 0 uncurated, 0 genuinely-new** (no routing to `mec-wiki-curator`). LLM Wiki API reachable (`allowUnauthenticated:true`, v0.4.16); baseline graph **513 nodes / 4455 edges**.

### Correctness & consistency audit (Phase B — concept batch 10)

Concept-page checks: definition grounded in the source(s)/parse it cites, no invented numbers/overclaims, `related`/wikilinks resolve and are non-self-referential, tags reused, evergreen wording.

- **Correctness fix (ungrounded mechanism — recurring MGI overclaim):** [[safe-reinforcement-learning]] described the Markov Game of Intervention as a "game-theoretic intervention that asymmetrically assigns one UAV as the deflector when two UAVs threaten collision … avoids the symmetric-swerve failure mode" — **not in the [[zhang-2025-ssac-mgi-heterogeneous-uav]] parse**, the same inter-UAV-deflection mischaracterization already corrected on [[collision-avoidance-mgi]] (concept batch 2) and the source page (source batch 11). MGI is a **per-UAV** two-agent design: a stochastic reward-maximizing **Standard Agent** paired with a deterministic **Safety Agent** and a binary gating policy $\mathbf{g}(s)\in\{0,1\}$ that *overrides* the Standard Agent on trigger ($\tilde a=\mathbf{g}\cdot a^{\mathrm{safe}}+(1-\mathbf{g})\cdot a$), with a per-intervention cost keeping overrides selective. Rewrote both the "In this wiki" paragraph and the standard-formulations table row (was "Game-theoretic intervention / asymmetric — can break symmetry"). `updated`→2026-06-01.
- **Correctness fix (false cross-corpus negative):** [[service-caching-mec]] claimed "None of the other wiki sources currently model service caching explicitly." **False** — service/content caching is explicitly modeled in [[gao-2024-service-experience-cache-uav]] (each UAV caches a service subset via a priority-based placement heuristic), [[zhao-2024-caching-service-placement-uav]] (joint content caching + service placement via Gibbs sampling), and [[mao-2024-ntn-hierarchical-caching-cav]] (hierarchical content caching). Rewrote to name those sources and cross-link [[computational-task-caching]]; added the four pages to `related`. `updated`→2026-06-01.
- **Soft-overclaim fix (unverifiable cross-corpus "first"):** [[semantic-communication]] called [[sun-2024-mfris-semantic-antijamming]] "the corpus's first multi-antenna semantic-MEC source" — the parse grounds only the paper's **own** literature positioning (prior semantic-MEC limited to single-antenna; prior RIS-MEC bit-level), not a corpus-wide first. Rewrote to that grounded self-positioning (same precedent as the dropped "first" claims in batches 5/6/7). `updated`→2026-06-01.
- **Grounding spot-checks (verbatim against parses):** [[self-adaptive-global-best-harmony-search]] (gao-2024-sagin: SGHS solves subproblem P3, DDPG solves P1; Fig. 2(b) four-config HMCR∈{0.4,0.9}/PAR∈{0.1,0.4} study, HMCR=0.9 advantageous — verbatim); [[spectrum-sensing-channel-selection]] (shao-2024 Fig. 7: jammers 1→5 at 8 UAVs/users, PER-MATD3-JSC latency ~flat ~11.2 — verbatim); [[service-experience-ratio]] (gao-2024-service: Jain/avg-delay ratio + 19–34% / +78.6% U4→U6 — verbatim); [[rotary-wing-propulsion-energy-model]] (zeng-2019 three-term model; li-2024-rldc applies $P^{pro}(v)$ to leader+follower, "description follows [10]" — grounded); [[stochastic-game]] (li-2025: five interconnected stochastic games + NE via stage-game reduction — verbatim); [[stackelberg-game]] (wang-2025-uav-swarm single-leader, multi-leader noted as the paper's own future work — matches source limitation); [[secrecy-outage-probability]] + [[secure-computation-efficiency]] (michailidis-2024: min-SCE max over Nakagami-m SOP — grounded).
- **Verified clean** (definition grounded, no invented numbers/overclaims, links resolve & non-self-referential, tags reused, evergreen): rotary-wing-propulsion-energy-model, salp-swarm-algorithm, seamless-handover, secrecy-outage-probability, secure-computation-efficiency, self-adaptive-global-best-harmony-search, semi-markov-decision-process, service-experience-ratio, service-function-chaining, small-cell-mec, soft-actor-critic, space-air-ground-integrated-network, spatial-equity-index, spectrum-sensing-channel-selection, stackelberg-game, stn, stochastic-game (plus the three corrected: safe-reinforcement-learning, service-caching-mec, semantic-communication).

### Gates (concept batch 10)

- **`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits. **`index_audit.py`** = 515 catalogue-able, 0 unindexed / 0 duplicate primaries (45 cross-ref mentions informational). **`frontmatter_audit.py --type concept`** = 234 pages, 0 errors. Graph baseline **513 / 4455** (service-caching-mec gained four `related` links to already-present pages; node count unchanged, edge count refreshes on next rescan). `log.md` edited with file tools, verified mojibake-free.

### Routing to `mec-wiki-synthesizer` (concept batch 10 — recorded, not filled)

- **Swarm/metaheuristic-family synthesis (standing, reinforced).** [[salp-swarm-algorithm]] + [[self-adaptive-global-best-harmony-search]] rejoin the standing swarm/metaheuristic family ([[whale-optimization-algorithm]], [[binary-whale-optimization]], [[multi-verse-optimizer]], [[particle-swarm-optimization]], [[gravitational-search-algorithm]], [[ant-colony-optimization]]); a family synthesis/comparison page may be worth minting (not a merge).
- **Game-theory family (standing, reinforced).** [[stackelberg-game]] + [[stochastic-game]] join [[nash-equilibrium]] / [[potential-game]] / [[bargaining-game]] / coalition-formation-game / double-auction / [[contract-theory]] / [[prospect-theory]] / [[reverse-auction-incentive]]; standing game-theory-mechanisms synthesis/comparison candidate.
- **Caching cluster.** [[service-caching-mec]] + [[computational-task-caching]] + content-caching across [[gao-2024-service-experience-cache-uav]] / [[zhao-2024-caching-service-placement-uav]] / [[zhao-2025-traj-offload-cache-migration]] / [[mao-2024-ntn-hierarchical-caching-cav]] / [[peng-2024-energy-time-uav-its]] form a comparable caching/placement/migration cluster with no single synthesis page; candidate for a synthesizer synthesis page.
- **SAC / safe-RL family.** [[soft-actor-critic]] + [[safe-reinforcement-learning]] + [[masac]] tie into the multi-agent actor-critic comparison candidate flagged in batch 7.
- No new tag fragmentation introduced this batch.

## 2026-06-01 — Audit pass (non-source layer — concept batch 9; no new papers)

Continues the non-source-layer audit into **concept batch 9** (20 pages, alphabetical perception-aided-offloading → robust-offloading, positions 161–180 of `.curation-out/concept_slugs.txt`). Tree clean at `4bb87a5`. Phase 0 reconciled clean: `curation_status.py --dupes` = **171 raw = 171 curated, 0 uncurated, 0 genuinely-new** (no routing to `mec-wiki-curator`). LLM Wiki API reachable (`allowUnauthenticated:true`, v0.4.16); baseline graph **513 nodes / 4455 edges**.

### Correctness & consistency audit (Phase B — concept batch 9)

Concept-page checks: definition grounded in the source(s)/parse it cites, no invented numbers/overclaims, `related`/wikilinks resolve and are non-self-referential, tags reused, evergreen wording.

- **Correctness fix (ungrounded ranking):** [[perception-aided-offloading]] claimed [[gao-2024-sagin-perception-offloading]]'s "Perception-Free" ablation is "consistently second-worst" — not grounded. In the parse, the consistently-worst scheme is **Complete-Offloading** (Fig. 3 cost 120, Fig. 4 ~79, Fig. 6 ~112); the Perception-Free method's rank varies (second-worst only in Fig. 4: 51 vs Random 50; in Fig. 3 it is 55 vs Random 75 and in Fig. 6 it is 82 vs Random 112, beating Random there). Rewrote to the grounded statement that Perception-Free (the same scheme with mmWave radar + visual sensors removed) consistently underperforms the full perception-aided approach on network cost and processed data size. `updated`→2026-06-01.
- **Correctness fix (wrong reward form):** [[qoe-modeling-mec]] stated [[bao-2025-ddpg-video-offloading]] uses $QoE=-\alpha\cdot\text{delay}-\beta\cdot(1-\text{bitrate}/\text{original})$ (two weights, linear bitrate term) — the parse (Eqs. 18/19/23) defines $QoE(i)=Q(i)-\alpha T^{\text{sys}}(i)$ with a **single** weight α and $Q(i)$ a **natural-logarithm** function of the transcoding ratio (α=0.05 in sims). Rewrote to the grounded single-weight log form. `updated`→2026-06-01.
- **Soft-overclaim fix:** [[physical-layer-security]] said [[benaya-2025-aerial-isac-haps]] "combines all three" secrecy levers (beamforming + jamming + cooperative relays) — the parse uses only **two** (transmit/receive beamforming nulls + a friendly-jamming AAV), with ISAC sensing as the eavesdropper-detection mechanism (no source-masking cooperative relay). Rewrote to "combines two of these levers". `updated`→2026-06-01.
- **Grounding spot-checks (verbatim against parses):** [[priority-based-delay-utility]] (hao-2024 Eqs. 24–25: high-priority $U^H=\log_2(1+v-T)$ on-time / $-P^H$ penalty; low-priority $U^L=P^L$ on-time / $P^L e^{-\rho(T-v)}$ decaying — exact); [[prioritized-experience-replay]] (nabi-2025: "Prioritized experience replay (PER) with soft actor-critic" inside the ESAC algorithm — grounded, ESAC naming confirmed); [[privacy-sensitive-data-partitioning]] (han-2024 §II: $\alpha_k=|D_k^o|/|D_k|$ non-sensitive portion, α=0.8 baseline + α sweep — exact); [[potential-game]] (chen-2024-ulse Theorem 2: LUTO-Game proved a potential game, potential function given, distributed JULTO → NE, PoA defined — exact); [[probsparse-self-attention-prediction]] (chen-2024-thoas: "combines probsparse self-attention and self-attention distillation" for traffic prediction + adaptive slicing — verbatim); [[proactive-eavesdropping]] (guo-2024 abstract: multiple full-duplex legitimate UAVs jam multiple suspicious UAV→destination links, joint jamming-power + trajectory — exact); [[robust-offloading]] (li-2024-robust §II: robust design "classified into three types: scheduling / channel / computation robustness" — verbatim taxonomy; Beta-policy b-MAPPO grounded); [[reverse-auction-incentive]] (zeng-2024: "first-price sealed reverse auction with reserve price", reserve = UAV benefit guarantee, symmetric equilibrium bids derived — verbatim); [[prompt-engineering]] (ye-2025: prompt-optimization level as one of four resource dimensions; +8%/+2% quality, +22% latency — verbatim, audited clean in source batch 10).
- **Verified clean** (definition grounded, no invented numbers/overclaims, links resolve & non-self-referential, tags reused, evergreen): perception-aided-offloading (corrected), physical-layer-security (corrected), pipeline-parallel-inference, pomdp, post-disaster-mec, potential-game, ppo, prioritized-experience-replay, priority-based-delay-utility, privacy-sensitive-data-partitioning, proactive-eavesdropping, probsparse-self-attention-prediction, prompt-engineering, prospect-theory, qcqp-sdr-probabilistic-mapping, qoe-modeling-mec (corrected), queueing-theory, reverse-auction-incentive, rf-energy-harvesting, robust-offloading.

### Gates (concept batch 9)

- **`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits. **`index_audit.py`** = 515 catalogue-able, 0 unindexed / 0 duplicate primaries (45 cross-ref mentions informational). **`frontmatter_audit.py --type concept`** = 234 pages, 0 errors (513 all-types, 0 errors). Graph **513 / 4455** (prose-only edits on already-present wikilinks; node/edge counts unchanged). `log.md` edited with file tools, verified mojibake-free.

### Routing to `mec-wiki-synthesizer` (concept batch 9 — recorded, not filled)

- **Security/PLS tag fragmentation.** [[physical-layer-security]] tags `security`/`secrecy-rate`/`eavesdropper`, [[proactive-eavesdropping]] tags `physical-layer-security`, and [[privacy-sensitive-data-partitioning]] tags `privacy`; the PLS/secrecy/privacy family would benefit from a one-slug tag normalization (pick one). Left for the synthesizer.
- **Game-theory family (standing, reinforced).** [[potential-game]], [[reverse-auction-incentive]], and [[prospect-theory]] join [[nash-equilibrium]] / [[stackelberg-game]] / [[stochastic-game]] / [[bargaining-game]] / coalition-formation-game / double-auction / [[contract-theory]]; a game-theory-mechanisms synthesis/comparison page may be worth minting (not a merge).
- **Prediction-engine pair.** [[probsparse-self-attention-prediction]] + [[informer-trajectory-prediction]] share the Informer lineage with different targets (traffic vs trajectory); candidate for a short synthesis tie.
- No new tag fragmentation introduced this batch.

## 2026-06-01 — Audit pass (non-source layer — concept batch 8; no new papers)

Continues the non-source-layer audit into **concept batch 8** (20 pages, alphabetical multi-functional-ris → penalty-dual-decomposition, positions 141–160 of `.curation-out/concept_slugs.txt`). Tree clean at `98aeb4d`. Phase 0 reconciled clean: `curation_status.py --dupes` = **171 raw = 171 curated, 0 uncurated, 0 genuinely-new** (no routing to `mec-wiki-curator`). LLM Wiki API reachable (`allowUnauthenticated:true`, v0.4.16); baseline graph **513 nodes / 4455 edges**.

### Correctness & consistency audit (Phase B — concept batch 8)

Concept-page checks: definition grounded in the source(s)/parse it cites, no invented numbers/overclaims, `related`/wikilinks resolve and are non-self-referential, tags reused, evergreen wording.

- **All 20 pages verified clean — no corrections needed.** Definitions accurately reflect how each concept is used in the referencing source(s)/parse; no invented numbers, overclaims, false cross-corpus "first" claims, or stale counts; `related`/wikilinks resolve and are non-self-referential; tags reused; wording already evergreen. This is the second all-clean concept batch (like batch 3) — the audit converges rather than churns.
- **Grounding spot-checks (verbatim against parses):**
  - [[multi-objective-reinforcement-learning]] — [[song-2024-mol-aoi-energy]] parse: **MOL-AET** is a multi-objective PPO trained over uniformly-spread preference-weight vectors then refined with policy-network genetic operators, maintaining a nondominated set Q* (verbatim, incl. the m=2 / β=29 → 30-weights initialization).
  - [[noma]] — [[qin-2025-bcuav-masac]] §III channel model: "we adopt the NOMA method and the spectrum resources between UAVs are orthogonal", SINR $\gamma_{j,k}$ with intra-cluster interference $I_j^k=\sum_{i\ne j}a_{i,k}p_{i,k}g_{i,k}$ and per-slot transmit power $p_{j,k}(t)$ as a decision variable — matches the page verbatim (NOMA within a UAV cluster, orthogonal between UAVs).
  - [[multi-uav-assisted-mec]] — [[liu-2026-jppo-en-convntm]]: "j-PPO+EN-ConvNTM" jointly controls UAV flight trajectory, task-offloading strategy, and **charging indicators** to minimize energy / maximize data-collection / ensure fairness in high-density mobile-device scenarios (verbatim contributions list); the hybrid continuous-discrete action framing motivating [[j-ppo]] is grounded.
  - [[multi-tasking-evolutionary-algorithm]] — [[wu-2026-terrain-aware-uav-mec]] title + body: "task-adaptive mechanism" that retains historically-effective genetic operators per individual (bandit-style operator selection) — grounded.
  - [[particle-swarm-optimization]] — APSO verbatim in [[albakhrani-2025-moalf-uav-mec]] (Algorithm 4 + §IV-G "Adaptive Particle Swarm Optimization (APSO) for Dynamic Resource Allocation"); chain-ordering PSO in [[wang-2025-acbft-uav-consensus]]; IPSO in [[zhang-2024-uav-task-offloading-ddpg]].
  - [[order-preserving-quantization]] (wu-2025 OPPO extends the DROO order-preserving candidate-generation, each candidate scored after WOA phase optimization), [[parameterized-dqn]] ([[ma-2025-pdqn-vehicular-mec]] hybrid discrete-server + continuous-power), [[over-the-air-computation]] ([[fu-2025-otae-inference-lae-batching]] superposition aggregation + spatial-correlation-aware beamforming), [[network-function-virtualization]] ([[zhang-2025-vnf-sgin-dql]] SDN/NFV 6G satellite-ground VNF selection+chaining via DQL), and [[penalty-dual-decomposition]] ([[hu-2019-pdd-uav-mec-offloading]] inner CCCP / outer multiplier+penalty with binary-to-equality conversion) — all grounded.
- **Verified clean** (full list): multi-functional-ris, multi-objective-mdp-vectorial-reward, multi-objective-reinforcement-learning, multi-source-data-fusion, multi-tasking-evolutionary-algorithm, multi-uav-assisted-mec, multi-verse-optimizer, nash-equilibrium, network-function-virtualization, network-slicing, noma, non-terrestrial-network, ntm, order-preserving-quantization, over-the-air-computation, overlay-underlay-spectrum-access, parallel-vs-serial-processing, parameterized-dqn, particle-swarm-optimization, penalty-dual-decomposition.

### Gates (concept batch 8)

- **`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits. **`index_audit.py`** = 515 catalogue-able, 0 unindexed / 0 duplicate primaries (45 cross-ref mentions informational). **`frontmatter_audit.py --type concept`** = 234 pages, 0 errors. Graph unchanged **513 / 4455** (no page edits this batch). `log.md` edited with file tools, verified mojibake-free.

### Routing to `mec-wiki-synthesizer` (concept batch 8 — recorded, not filled)

- **Swarm/metaheuristic-family synthesis (standing, reinforced).** [[multi-verse-optimizer]] and [[particle-swarm-optimization]] join the standing swarm/metaheuristic family ([[whale-optimization-algorithm]], [[binary-whale-optimization]], [[salp-swarm-algorithm]], [[gravitational-search-algorithm]], [[ant-colony-optimization]], self-adaptive-global-best-harmony-search). A family synthesis/comparison page tying these distinct-but-comparable derivative-free metaheuristics together may be worth minting (not a merge).
- **Hybrid-action family (standing, reinforced).** [[parameterized-dqn]] joins [[hybrid-action-decision-making]] / [[hybrid-action-representation]] / [[j-ppo]] / [[soft-actor-critic]] as another way to handle coupled discrete-continuous actions; same standing hybrid-action synthesis candidate flagged in batch 6.
- **NTN/LEO cluster (standing).** [[non-terrestrial-network]] joins the LEO/NTN concept cluster flagged in batch 6 ([[leo-satellite-edge-computing]] / [[leo-satellite-coverage-time]] / [[leo-handover-protocol]] / [[space-air-ground-integrated-network]]); candidate for a synthesizer synthesis page.
- No new tag fragmentation introduced this batch.

## 2026-06-01 — Audit pass (non-source layer — concept batch 7; no new papers)

Continues the non-source-layer audit into **concept batch 7** (20 pages, alphabetical low-altitude-intelligent-network → multi-agent-td3, positions 121–140 of `.curation-out/concept_slugs.txt`). Tree clean at `d5adff0`. Phase 0 reconciled clean: `curation_status.py --dupes` = **171 raw = 171 curated, 0 uncurated, 0 genuinely-new** (no routing to `mec-wiki-curator`). LLM Wiki API reachable (`allowUnauthenticated:true`, v0.4.16); baseline graph **513 nodes / 4455 edges**.

### Correctness & consistency audit (Phase B — concept batch 7)

Concept-page checks: definition grounded in the source(s)/parse it cites, no invented numbers/overclaims, `related`/wikilinks resolve and are non-self-referential, tags reused, evergreen wording.

- **Correctness fix (stale cross-corpus undercount):** [[maritime-mec]] stated "The wiki has **two** maritime sources" and listed only [[wang-2026-aerial-marine-msar]] + [[liu-2025-haps-uav-maritime-iot]] — a stale undercount. The corpus carries a substantial maritime track (**18 sources** tagged `maritime-mec`) and already has a [[maritime-mec-architectures]] synthesis page mapping seven of them. Rewrote to describe the track without a hard count (kept the two as representative communication/compute endpoints) and cross-linked the synthesis page; added [[maritime-mec-architectures]] to `related`. `updated`→2026-06-01.
- **Evergreen-wording fix:** [[lyapunov-optimization]] ended its "In this wiki" note with "Expect more sources to use the same template" (forward-looking process-narration). Rewrote to the evergreen fact that the drift-plus-penalty template recurs across the corpus's online-control sources, with named cross-links ([[dai-2024-uav-vehicular-offloading-lyapunov]], [[yang-2022-stochastic-uav-mec-lyapunov]], [[wang-2024-maritime-eh-jcora]], [[mao-2016-lodco-eh-mec-offloading]] — all `lyapunov`-tagged). `updated`→2026-06-01. (Soft case `process_refs.py` does not pattern-match; fixed by hand.)
- **Grounding spot-checks (verbatim against parses):** [[majorization-minimization]] (chu-2024 parse §III-C: MM pursues "a convex surrogate function that locally lower bounds it … Utilizing the first-order Taylor expansion" for the RIS-reflection term, alongside SDR + FP — verbatim); [[monotonic-optimization]] (sun-2024-mfris parse §III + abstract: "fast-converging monotonic optimization … combined with decoupling second-order cone programming (MO-DSOCP) … globally optimal solution with fewer feasibility evaluations" over a quasi-convex objective with MINLP constraints — verbatim); [[masac]] (qin-2025 Findings: MASAC chosen over MADDPG, entropy-regularized objective gives more stable convergence + higher final sensing rate — grounded); [[mappo]] (kang-2023: MAPPO under CTDE solves the UAV+HAP offloading POMDP with state normalization + action masking — grounded); [[markov-reward-process]] (niazmand-2025: stochastic IIoT problem recast as an MRP with per-time-slot delay/accuracy constraints, solved by hybrid-action SAC — grounded); [[markov-approximation]] (dai-2024: per-slot Markov-chain search after Lyapunov decoupling of the long-term UAV-energy constraint — grounded); [[multi-agent-q-learning]] (li-2025-stochastic-game: RLDC tabular multi-agent Q-learning with Q-value exchange, NE via contraction-mapping — matches the source page); [[makespan-minimization]] (huang-2023: makespan as one of two CMOP objectives over DAG dependencies — grounded).
- **Verified clean** (definition grounded, no invented numbers/overclaims, links resolve & non-self-referential, tags reused, evergreen): the remaining 18 batch-7 concepts (low-altitude-intelligent-network [idempotent — batch-9 wording fix intact], ma-pomdp, maddpg, majorization-minimization, makespan-minimization, mappo, markov-approximation, markov-reward-process, masac, matching-theory-for-resource-allocation, mixed-integer-nonlinear-programming, mmwave-radar-sensing, mobile-aigc-network, mobile-edge-computing, mobility-aware-offloading, monotonic-optimization, multi-agent-q-learning, multi-agent-td3).

### Gates (concept batch 7)

- **`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits. **`index_audit.py`** = 515 catalogue-able, 0 unindexed / 0 duplicate primaries (45 cross-ref mentions informational). **`frontmatter_audit.py --type concept`** = 234 pages, 0 errors. Graph baseline **513 / 4455** (the two corrected pages added a few intra-corpus wikilinks between already-present pages; node count unchanged, edge count refreshes on next rescan). `log.md` edited with file tools, verified mojibake-free.

### Routing to `mec-wiki-synthesizer` (concept batch 7 — recorded, not filled)

- **Maritime track is well-covered** — [[maritime-mec-architectures]] synthesis + [[maritime-three-tier-energy-saving]] finding already exist; that synthesis page's own "Gaps" note (no maritime security/trust source, CSI-uncertainty mostly side-stepped, no classical-vs-DRL head-to-head on a maritime benchmark) is the standing maritime routing note. No new maritime page needed from this batch.
- **Multi-agent actor-critic family.** [[maddpg]], [[multi-agent-td3]], [[masac]], [[mappo]], and [[multi-agent-q-learning]] each have a clean per-method concept page with overlapping rosters and explicit "vs siblings" prose, but there is no single synthesis/comparison page tying the CTDE actor-critic family (deterministic MADDPG/MATD3 vs stochastic MASAC vs on-policy MAPPO vs value-based multi-agent Q-learning) together across the corpus. Candidate for a synthesizer comparison page (not a merge).



Continues the non-source-layer audit into **concept batch 6** (20 pages, alphabetical hybrid-action-decision-making → local-search-evolutionary, positions 101–120 of `.curation-out/concept_slugs.txt`). Tree clean at `539f30a`. Phase 0 reconciled clean: `curation_status.py --dupes` = **171 raw = 171 curated, 0 uncurated, 0 genuinely-new** (no routing to `mec-wiki-curator`). LLM Wiki API reachable (`allowUnauthenticated:true`, v0.4.16); baseline graph **513 nodes / 4455 edges**.

### Correctness & consistency audit (Phase B — concept batch 6)

Concept-page checks: definition grounded in the source(s)/parse it cites, no invented numbers/overclaims, `related`/wikilinks resolve and are non-self-referential, tags reused, evergreen wording.

- **Correctness fix (ungrounded number — same overclaim caught in the batch-6 source audit):** [[load-balancing-uav-mec]] claimed [[nabi-2025-jour-hierarchical-aerial]] "shows that the max-min UAV-load gap shrinks substantially vs greedy baselines" — **not in the parse**, which reports **average load per UAV** (Fig. 8: JOUR 0.30 vs GOUA+SAC/PPO/DDPG/HA 0.32/0.40/0.41/0.44 at 30 GUs), not a max-min gap. Rewrote to the grounded average-load result with the verbatim figures; the per-UAV-load reward term (cycles ÷ capacity, Eq. 25a) and GU-capping-by-capacity (parse L107/125) are confirmed grounded.
- **Correctness fix (false cross-corpus "first"):** [[intelligent-reflecting-surface]] ended "This is the corpus's first IRS entry" — **false**: the corpus carries many IRS/RIS sources. Replaced with a grounded cross-link to the anti-jamming / secure-beamforming IRS family ([[sun-2024-active-passive-ris-receiver]], [[sun-2024-mfris-semantic-antijamming]], [[michailidis-2024-secure-ris-uav-mec-iot]], [[mao-2025-irs-noma-fl-secrecy]], [[zhang-2025-gan-td3-isac-active-ris]]).
- **Ungrounded-number fix:** [[informer-trajectory-prediction]] illustrated the attention-cost argument with "$O(H^2)$ for $H = 24$ h history × thousands of vehicles" for [[zhang-2025-mcma-task-migration]] — the **24 h / thousands-of-vehicles** scale is **not in that parse** (which states only an Informer-based multi-step vehicular trajectory predictor). Rewrote to the grounded mechanism (ProbSparse keeps long-sequence attention tractable as the horizon grows). Informer's own architecture facts (ProbSparse top-$\log L$, distilling encoder, $O(L\log L)$, $L=720$+) are correct general ML facts about Zhou et al. AAAI 2021 and left intact.
- **Soft-superlative fix (unverifiable cross-corpus "first"):** [[knowledge-distillation-for-drl]] called [[chen-2024-thoas-traffic-aware-sagin]] "the corpus's first explicit treatment of on-platform model-size constraints" — softened to "brings on-platform model-size constraints into the corpus as a first-class design concern" + cross-link to the DNN-pruning angle in [[niazmand-2025-jopa-dnn-pruning-iiot]] (consistent with the batch-5/7 precedent). The distillation numbers (~6%/73%, ~90%@12%, ~97%@50%) are grounded (verbatim in the chen-2024 parse + source page).
- **Grounding spot-checks (verbatim against parses):** [[interdependent-tasks-dag]] (huang-2023 intro: "According to the statistic of the Alibaba data trace, more than 75% of 4 million applications contain interdependent tasks [8]"; DAG examples face recognition + vehicular navigation grounded L91); [[impala]] (lee-2024 L29/398: IMPALA + V-trace, parallel actor-learners + importance sampling, "stable training … large state and action spaces", advantages over DQN/A3C/PPO — verbatim); [[j-ppo]]/[[j-ppo-en-convntm]]/[[hybrid-action-decision-making]] (liu-2026 hybrid clip $g^{hybrid}=c_3·\text{cont}+(1-c_3)·\text{disc}$, $c_1=0.1$/$c_2=0.01$/$c_3=0.5$ Table I); [[information-causality-constraint]] (zeng-2016 staircase water-filling consequence).
- **Verified clean** (definition grounded, no invented numbers/overclaims, links resolve & non-self-referential, tags reused, evergreen): the remaining 16 batch-6 concepts (hybrid-action-decision-making, hybrid-action-representation, impala, infeasible-individual-utilization, information-causality-constraint, integrated-sensing-and-communication, integrated-sensing-computation-communication, interdependent-tasks-dag, intra-swarm-task-delegation, j-ppo-en-convntm, j-ppo, jains-fairness-index, leo-handover-protocol, leo-satellite-coverage-time, leo-satellite-edge-computing, local-search-evolutionary).

### Gates (concept batch 6)

- **`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits. **`index_audit.py`** = 515 catalogue-able, 0 unindexed / 0 duplicate primaries (45 cross-ref mentions informational). **`frontmatter_audit.py --type concept`** = 234 pages, 0 errors (513 all-types, 0 errors). Graph baseline **513 / 4455** (the four corrected pages added a few intra-corpus wikilinks between already-present pages; node count unchanged, edge count refreshes on next rescan). `log.md` edited with file tools, verified mojibake-free.

### Routing to `mec-wiki-synthesizer` (concept batch 6 — recorded, not filled)

- **Hybrid-action family synthesis.** [[hybrid-action-decision-making]], [[hybrid-action-representation]] (HyAR latent space), [[j-ppo]] (dual-head PPO), [[parameterized-dqn]], and (cross-batch) [[soft-actor-critic]] + niazmand's SAC hybrid action describe distinct ways to handle coupled discrete-continuous action spaces. A synthesis/comparison page tying the hybrid-action family together may be worth minting (not a merge).
- **LEO-satellite / NTN concept cluster.** [[leo-satellite-edge-computing]], [[leo-satellite-coverage-time]], [[leo-handover-protocol]], [[walker-star-constellation]], [[seamless-handover]], [[free-space-optical-isl]], [[non-terrestrial-network]] form a dense, comparable LEO/NTN cluster with no single synthesis page; candidate for a synthesizer synthesis page.
- **Evolutionary-family tag fragmentation (standing).** infeasible-individual-utilization + local-search-evolutionary tag `evolutionary`, while [[differential-evolution]]/[[constraint-violation-evaluation]] use `evolutionary-algorithm`. Same standing normalization flagged in batches 2/4; no new fragmentation introduced this batch.

## 2026-06-01 — Audit pass (non-source layer — concept batch 5; no new papers)

Continues the non-source-layer audit into **concept batch 5** (20 pages, alphabetical finite-blocklength-urllc → high-density-mobile-device-scenarios, positions 81–100 of `.curation-out/concept_slugs.txt`). Tree clean at `7584c2a`. Phase 0 reconciled clean: `curation_status.py --dupes` = **171 raw = 171 curated, 0 uncurated, 0 genuinely-new** (no routing to `mec-wiki-curator`). LLM Wiki API reachable (`allowUnauthenticated:true`, v0.4.16); baseline graph **513 nodes / 4455 edges**.

### Correctness & consistency audit (Phase B — concept batch 5)

Concept-page checks: definition grounded in the source(s)/parse it cites, no invented numbers/overclaims, `related`/wikilinks resolve and are non-self-referential, tags reused, evergreen wording.

- **Correctness fix (ungrounded architectural detail):** [[heterogeneous-uav-fleet]] described [[zhang-2025-ssac-mgi-heterogeneous-uav]]'s **SSAC** as a "(shared backbone + per-UAV head)" architecture and called it "the first source explicitly addressing heterogeneity" — the per-UAV-head split is **not in the parse**, which defines SSAC (Shared Soft Actor-Critic) as a **policy-sharing** design that extracts *dimension-invariant* features so heterogeneous UAVs (varying service type / resource capacity) learn a **unified** policy (three shared SAC modules: standard/safety/intervention). Rewrote to the grounded policy-sharing mechanism and dropped the unverifiable cross-corpus "first" claim.
- **Evergreen-wording fix:** [[high-density-mobile-device-scenarios]] ended with "Subsequent sources should be tagged for whether they assume static, low-mobility, or high-density conditions" — a forward-looking instruction to a later curation run. Rewrote to the evergreen fact "Sources in the corpus differ in whether they assume static, low-mobility, or high-density conditions."
- **Grounding spot-checks (verbatim against parses):** [[finite-blocklength-urllc]] (wu-2024 parse: short packets "20 or 32 bytes", Shannon overstates rate, **angle-dependent Rician fading**, logarithmic rate approximation — all verbatim); [[fractional-programming-dinkelbach]] (zhu-2025 parse: fractional-programming theory + Lyapunov transform the **LSEM** EE-max into a per-slot MINLP — acronym and combination grounded); [[gale-shapley-matching]] (nabi-2025 parse: GOUA is a "matching-game-based algorithm inspired by the Gale-Shapley algorithm" for GU-UAV association by mutual preference scores); [[gauss-markov-mobility-model]] (liu-2026 parse §III-A + ref [31]: GM speed/direction first-order chains, **256** IoT devices in a **160 m × 160 m** arena); [[friendly-jamming-uav]] (benaya-2025 parse: jamming AAV degrades eavesdropper reception; transmit/receive beamforming + AAV trajectory jointly optimized via **alternating optimization** with HAPS); [[gravitational-search-algorithm]] (zheng-2024 IMOGSA: quasi-opposition learning + discrete update + NSGA-II-style archive, chosen vs DRL/convex).
- **Verified clean** (definition grounded, no invented numbers/overclaims, links resolve & non-self-referential, tags reused, evergreen): the remaining 18 batch-5 concepts (finite-blocklength-urllc, fixed-wing-propulsion-energy-model, fl-poisoning-attacks, fractional-programming-dinkelbach, free-space-optical-isl, friendly-jamming-uav, gae, gale-shapley-matching, gauss-markov-mobility-model, generalized-assignment-problem, generative-adversarial-network, generative-ai-for-mec, generative-diffusion-model, gravitational-search-algorithm, heterogeneous-agent-rl, hierarchical-aerial-mec [idempotent — batch-9 wording fix intact], hierarchical-reinforcement-learning, high-altitude-platform-station).

### Toolkit ratchet (concept batch 5)

- Generalized `process_refs.py`'s forward-looking-placement pattern from `future …` only to also catch `subsequent | later | upcoming | forthcoming … sources/pages/entity-pages should/will/must/land/belong/be tagged`, so the [[high-density-mobile-device-scenarios]] leak above is caught by the tool going forward. README updated. Regression-checked: still does **not** flag a paper's own "future work" / "future research directions" (noun = work/research, not curation vocabulary).

### Gates (concept batch 5)

- **`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits. **`index_audit.py`** = 515 catalogue-able, 0 unindexed / 0 duplicate primaries (45 cross-ref mentions informational). **`frontmatter_audit.py --type concept`** = 234 pages, 0 errors. Graph unchanged **513 / 4455** (prose-only edits, no new links/pages). `log.md` edited with file tools, verified mojibake-free.

### Routing to `mec-wiki-synthesizer` (concept batch 5 — recorded, not filled)

- **Swarm/metaheuristic family synthesis (standing, reinforced).** [[gravitational-search-algorithm]] joins the spread of distinct mixed-variable aerial metaheuristics ([[multi-verse-optimizer]], [[salp-swarm-algorithm]], [[whale-optimization-algorithm]], [[binary-whale-optimization]], [[particle-swarm-optimization]], [[ant-colony-optimization]], [[self-adaptive-global-best-harmony-search]]) — all chosen to emit a one-run Pareto set for NP-hard MINLP collaborative-beamforming/CB problems, explicitly motivated against DRL (no training) and convex (no space distortion). These are genuinely different algorithms (not duplicates); a synthesis/comparison page tying the swarm-metaheuristic family together remains worth minting (flagged in concept batch 1; not a merge).
- **Tag fragmentation in the generative-AI family.** [[generative-adversarial-network]]/[[generative-diffusion-model]] tag `generative-ai`, while [[generative-ai-for-mec]] tags `gai` and [[generative-diffusion-model]]/[[diffusion-model-as-optimizer]] also use `diffusion`. A tag-vocabulary normalization (pick one umbrella slug, e.g. `generative-ai`) would de-fragment the family. Flagged only — no merge/delete/retag here.

## 2026-06-01 — Audit pass (non-source layer — concept batch 4; no new papers)

Continues the non-source-layer audit into **concept batch 4** (20 pages, alphabetical dual-population-evolutionary-algorithm → federated-reinforcement-learning, positions 61–80 of `.curation-out/concept_slugs.txt`). Tree clean at `8f0b593`. Phase 0 reconciled clean: `curation_status.py --dupes` = **171 raw = 171 curated, 0 uncurated, 0 genuinely-new** (no routing to `mec-wiki-curator`). LLM Wiki API reachable (`allowUnauthenticated:true`, v0.4.16); baseline graph **513 nodes / 4455 edges**.

### Correctness & consistency audit (Phase B — concept batch 4)

Concept-page checks: definition grounded in the source(s)/parse it cites, no invented numbers/overclaims, `related`/wikilinks resolve and are non-self-referential, tags reused, evergreen wording.

- **Correctness fix (ungrounded mechanism / misclassification):** [[energy-balancing-uav]] had two defects vs the parses. (1) It described [[huang-2023-mu-aec-task-energy]]'s energy-balancing index as a "sum of pairwise differences"; the parse Eq. 13 defines it as a **sum of squared normalized deviations** from the swarm mean, $G_2=\sum_j((TE_j-\overline{TE})/\psi)^2$ — matching the batch-3 source-page correction. Rewrote with the actual formula. (2) It listed [[nabi-2025-jour-hierarchical-aerial]] as an energy-balancing "Variance / max-min penalty in DRL reward"; the batch-6 source audit established nabi-2025's third SAC-reward term is per-UAV **load** (computed cycles ÷ compute capacity, Eq. 25a) — i.e. **load balancing**, not energy balancing. Moved nabi-2025 to the load-balancing contrast and corrected the framing.
- **Evergreen-wording fix:** [[federated-learning]] called itself "the base concept underlying the wiki's **prior**, narrower [[federated-reinforcement-learning]]/[[blockchain-for-fl-aggregation]] pages" — "prior" narrates page-creation order; dropped to "the wiki's narrower …". (Soft case fixed by hand; not added to `process_refs.py` to avoid false-positives on a paper's own "prior work".)
- **Grounding spot-checks (verbatim against parses):** [[dual-population-evolutionary-algorithm]] (huang-2025 parse: "dual-population cooperative mechanism between two populations and a repairing constraint-handling technique" — attribution + repairing-CH correct); [[dynamic-confidence-interval-clipping]] (chen-2024-thoas Eq. 31–32: two-layer confidence interval, dynamic factor α_t scaled by κ adapting to the **sign** of the TD error δ — fully grounded); [[elastic-task-scheduling]] (sun-2024-asap §IV-C + Table IV: ECLB/ICLB online reschedule on cluster-head cutoff/recovery, rescheduling latency "within 1 second", latency returns to baseline after recovery).
- **Verified clean** (definition grounded, no invented numbers/overclaims, links resolve & non-self-referential, tags reused, evergreen): the remaining 18 batch-4 concepts (dual-population-evolutionary-algorithm, dynamic-confidence-interval-clipping, dynamic-constrained-multi-objective-optimization, dynamic-qos-constraints, dynamic-uav-clustering, edge-user-allocation, elastic-task-scheduling, en-convntm, end-to-end-vs-decomposition-in-drl-mec [idempotent — batch-1 wording fix intact], energy-expenditure-coefficient, energy-harvesting-mec, energy-latency-tradeoff, equilibrium-efficiency-metric, event-driven-vs-slot-driven-offloading, evolutionary-reinforcement-learning, fairness-metrics-in-mec, fault-tolerant-relay-network, federated-reinforcement-learning).

### Gates (concept batch 4)

- **`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits. **`index_audit.py`** = 515 catalogue-able, 0 unindexed / 0 duplicate primaries (45 cross-ref mentions informational). **`frontmatter_audit.py --type concept`** = 234 pages, 0 errors. Graph unchanged **513 / 4455** (prose-only edits, no new links/pages). `log.md` edited with file tools, verified mojibake-free.

### Routing to `mec-wiki-synthesizer` (concept batch 4 — recorded, not filled)

- **Tag fragmentation in the evolutionary-algorithm family (standing).** The same fragmentation flagged in concept batch 2 recurs here — `dual-population-evolutionary-algorithm`, `dynamic-constrained-multi-objective-optimization`, and `evolutionary-reinforcement-learning` tag `evolutionary`, while [[differential-evolution]]/[[constraint-violation-evaluation]] use `evolutionary-algorithm`. A tag-vocabulary normalization (pick one slug) would de-fragment the family. Flagged only — no merge/delete/retag here; no new fragmentation introduced this batch.

## 2026-06-01 — Audit pass (non-source layer — concept batch 3; no new papers)

Continues the non-source-layer audit into **concept batch 3** (20 pages, alphabetical cooperative-perception → drone-cell-3d-placement, positions 41–60 of `.curation-out/concept_slugs.txt`). Tree clean at `18dc945`. Phase 0 reconciled clean: `curation_status.py --dupes` = **171 raw = 171 curated, 0 uncurated, 0 genuinely-new** (no routing to `mec-wiki-curator`). LLM Wiki API reachable (`allowUnauthenticated:true`, v0.4.16); baseline graph **513 nodes / 4455 edges**.

### Correctness & consistency audit (Phase B — concept batch 3)

Concept-page checks: definition grounded in the source(s)/parse it cites, no invented numbers/overclaims, `related`/wikilinks resolve and are non-self-referential, tags reused, evergreen wording.

- **All 20 verified clean — no corrections needed.** Definitions reflect how each concept is used in the source(s) they cite; no invented numbers/overclaims; `related`/wikilinks resolve and are non-self-referential; tags reused; evergreen wording (no process-narration). Grounding spot-checks against the parses: [[cross-entropy-method]] (li-2023 "Code bAsed croSs Entropy (CASE-Algorithm)" + Polyblock-Approximation/bisection "PAS-Algorithm" solving the bottom problem via canonical [[monotonic-optimization]] — verbatim); [[cooperative-perception]] (xie-2026 abstract: cooperative perception fuses multi-source observations over V2X, vehicle-based suffers occlusion, infrastructure-based has coverage gaps — matches the V2V/V2I/V2U platform table). The batch-1 evergreen-wording fix on [[cooperative-perception]] ("is the wiki's source bringing cooperative perception in") is intact — idempotent re-check, no change.
- Pages: cooperative-perception, cramer-rao-bound, cross-entropy-method, csi-estimation-error, csra-cold-start-reputation-aggregation, data-partition-parallel-inference, ddpg, ddqn, decentralized-federated-learning, deep-q-network, delegated-proof-of-stake, differential-evolution, diffusion-model-as-optimizer, dispersed-computing, distributed-foundation-models, distributionally-robust-optimization, dl-inference-latency-prediction, dnn-model-partition, double-auction, drone-cell-3d-placement.

### Gates (concept batch 3)

- **`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits. **`index_audit.py`** = 515 catalogue-able, 0 unindexed / 0 duplicate primaries (45 cross-ref mentions informational). **`frontmatter_audit.py --type concept`** = 234 pages, 0 errors. Graph unchanged **513 / 4455** (no page edits this batch). `log.md` edited with file tools, verified mojibake-free.

### Routing to `mec-wiki-synthesizer` (concept batch 3 — recorded, not filled)

- **Tag fragmentation in the CSI/robust-optimization family.** [[csi-estimation-error]] tags `channel-state-information` while [[robust-offloading]] and [[distributionally-robust-optimization]] tag `csi` (and `robust` vs `robust-optimization` across the same cluster). A tag-vocabulary normalization (pick one slug each) would de-fragment the family. Flagged only — no merge/delete/retag here.

## 2026-06-01 — Audit pass (non-source layer — concept batch 2; no new papers)

Continues the non-source-layer audit into **concept batch 2** (20 pages, alphabetical blockchain-for-fl-aggregation → cooperative-jamming, positions 21–40 of `.curation-out/concept_slugs.txt`). Tree clean at `cb14bb1`. Phase 0 reconciled clean: `curation_status.py --dupes` = **171 raw = 171 curated, 0 uncurated, 0 genuinely-new** (no routing to `mec-wiki-curator`). LLM Wiki API reachable (`allowUnauthenticated:true`, v0.4.16); baseline graph **513 nodes / 4455 edges**.

### Correctness & consistency audit (Phase B — concept batch 2)

Concept-page checks: definition grounded in the source(s)/parse it cites, no invented numbers/overclaims, `related`/wikilinks resolve and are non-self-referential, tags reused, evergreen wording.

- **Correctness fix (ungrounded mechanism):** [[collision-avoidance-mgi]] described MGI as a *two-agent inter-UAV* "intervention agent vs non-intervention agent" game with a "symmetric-swerve collision" failure mode, a Nash-equilibrium "stable separation maneuver", and role assignment "by UAV ID / speed / heading" — **none of which is in the parse**. This is the same mischaracterization the batch-11 source audit corrected on [[zhang-2025-ssac-mgi-heterogeneous-uav]]: the parse (§V-B, Eqs. 32–34) defines MGI as a **per-UAV** two-agent game — a stochastic reward-maximizing **Standard Agent** plus a deterministic **Safety Agent** with a **binary gating policy** g(s)∈{0,1} that *overrides* the Standard Agent when an intervention triggers (ã = g·a_safe + (1−g)·a), giving safety guarantees during and after training. Rewrote the body to the grounded gating mechanism + the constant-altitude (2-D, 500×500) scope; dropped the invented Nash/symmetric-swerve story.
- **Consistency fix (grounding):** [[chance-constraint]] said the [[jia-2025-dro-uav-hap-mec]] reformulation "yields a tractable second-order cone program"; the parse reformulates the chance constraint into a **mixed-integer** SOCP (**MISOCP**), matching the [[conditional-value-at-risk]] page. Tightened to MISOCP.
- **Verified clean** (definition grounded, no invented numbers, links resolve & non-self-referential, tags reused, evergreen): the remaining 18 batch-2 concepts (blockchain-for-fl-aggregation, byzantine-fault-tolerant-consensus, ccvm-correction-voting, cellular-connected-uav, centralized-training-decentralized-execution, cmoea-d-cdp, coalition-formation-game, collaborative-beamforming, collaborative-dl-inference, completion-time-difference, computational-task-caching, conditional-gan, conditional-value-at-risk, constrained-multi-objective-evolutionary-algorithm, constraint-violation-evaluation, contract-theory, convlstm, cooperative-jamming).

### Gates (concept batch 2)

- **`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits. **`index_audit.py`** = 515 catalogue-able, 0 unindexed / 0 duplicate primaries (45 cross-ref mentions informational). **`frontmatter_audit.py --type concept`** = 234 pages, 0 errors. Graph unchanged **513 / 4455** (prose-only edits, no new links/pages). `log.md` edited with file tools, verified mojibake-free.

### Routing to `mec-wiki-synthesizer` (concept batch 2 — recorded, not filled)

- **Tag fragmentation in the evolutionary-algorithm family.** Most pages use the tag `evolutionary` (cmoea-d-cdp, constrained-multi-objective-evolutionary-algorithm, dual-population-evolutionary-algorithm, infeasible-individual-utilization, local-search-evolutionary, multi-tasking-evolutionary-algorithm, evolutionary-reinforcement-learning, salp-swarm-algorithm, dynamic-constrained-multi-objective-optimization) while [[differential-evolution]] and [[constraint-violation-evaluation]] use `evolutionary-algorithm`. A tag-vocabulary normalization (pick one) would de-fragment the family. Flagged only — no merge/delete here.

## 2026-06-01 — Audit pass (non-source layer — concept batch 1; no new papers)

First invocation of the **non-source-layer** audit, beginning the concept pages now that all 171 source pages are audited (batches 1–12 below). Phase 0 reconciled clean: `curation_status.py --dupes` reports **171 raw = 171 curated, 0 uncurated, 0 genuinely-new** (no routing to `mec-wiki-curator`). Tree clean at `159bd17`; `corpus_counts.py` confirms 171 / **234 concepts** / 71 entities / 14 findings / 11 synthesis / 4 comparisons / 2 methodology / 5 queries / 1 thesis. LLM Wiki API reachable (`allowUnauthenticated:true`, v0.4.16); baseline graph **513 nodes / 4455 edges**.

### Non-source coverage plan

- Split the non-source layer into **concepts (234) → entities (71) → derived (37)** ≈ 342 pages. Concept list (`.curation-out/concept_slugs.txt`) batched with `make_batches.py --size 20` → **12 concept batches** of 20 (last 14). Tracker: `.curation-out/audit-coverage.md`.

### Correctness & consistency audit (Phase B — concept batch 1)

Audited **concept batch 1** (20 pages, alphabetical action-space-explosion-in-multi-uav-mec → blockage-aware-channel-model). Concept-page checks: definition grounded in the source(s)/parse it cites, no invented numbers/overclaims, `related`/wikilinks resolve and are non-self-referential, tags reused, evergreen wording.

- **Evergreen-wording fixes (forward-looking curation-workflow placement → fact):**
  - [[air-ground-integrated-network]] — dropped trailing "Future cross-layer sources should land here."
  - [[cooperative-perception]] — "[[xie-2026-uav-multisource-fusion]] is the **first** source … Future curated perception-class sources should land here." → "is the wiki's source bringing cooperative perception in" (placement instruction removed).
  - synthesis [[drl-backbones-across-uav-mec-sources]] — dropped trailing "Future sources should treat it as the default."
  - `index.md` Tools note — "Future entity pages should land here as more authors recur." → dropped (kept the evergreen "entity pages exist for the central recurring contributors").
- **Grounding spot-checks (verbatim against parses):** [[active-ris]] scaling (Theorem 5: receive power ∝ N_A²·N_P², asymptotic SINR ∝ N_A·N_P, vs (N_P+N_A)² / (N_P+N_A) for single-layer active RIS); [[adaptive-intermediate-data-compression]] (ASAP 8-bit quantization + gzip lossless; 87.2%–92.7% data-size reduction, accuracy reduction within 0.15%); [[b-spline-trajectory]] (3λ control-point parameterization). All confirmed grounded.
- **Verified clean** (definition grounded, no invented numbers, links resolve & non-self-referential, tags reused): the remaining 16 batch-1 concepts (action-space-explosion-in-multi-uav-mec, adaptive-entropy-priority-replay, adaptive-inter-layer-data-offloading, age-of-information, aigc-service-provider, air-to-ground-channel-model, alternating-direction-method-of-multipliers, alternating-optimization-sdr-sca, ant-colony-optimization, anti-jamming-mec, aoi-energy-tradeoff, bargaining-game, beta-policy-drl, binary-vs-partial-offloading, binary-whale-optimization, blockage-aware-channel-model).

### Toolkit

- **Extended `process_refs.py`** (+ README) with two forward-looking-placement patterns (`(should|will|would) land here`; `future … sources/pages/entity-pages (should|will|would|land|belong)`). Regression-checked: it does **not** flag the legit evergreen "## Limitations / future work" sections on source pages (a paper's own future work is domain content). Caught exactly the 4 leaks above; all fixed → tool exits 0.

### Gates (concept batch 1)

- **`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits. **`index_audit.py`** = 515 catalogue-able, 0 unindexed / 0 duplicate primaries (45 cross-ref mentions informational). **`frontmatter_audit.py`** = 513 pages, 0 errors (`--type concept`: 234, 0 errors). Graph unchanged **513 / 4455** (prose-only edits, no link changes). Meta docs (`index.md`, `log.md`) edited with file tools, verified mojibake-free.

### Routing to `mec-wiki-synthesizer` (concept batch 1 — recorded, not filled)

- **Swarm-metaheuristic family** is spread across distinct algorithm pages (binary-whale-optimization, whale-optimization-algorithm, multi-verse-optimizer, salp-swarm-algorithm, particle-swarm-optimization, ant-colony-optimization, gravitational-search-algorithm, self-adaptive-global-best-harmony-search). These are genuinely different algorithms (no merge), but a synthesis/comparison page tying the swarm-metaheuristic family together — when each is used and against what baselines — may be worth minting.

## 2026-06-01 — Audit pass (meta-doc cleanup + correctness batches 1–12/12; no new papers)

First invocation of a multi-invocation batched audit over the fully-curated 171-source corpus. Phase 0 reconciled clean: `curation_status.py --dupes` reports **171 raw = 171 curated, 0 uncurated, 0 genuinely-new** (no routing to `mec-wiki-curator` needed). Tree clean at `f81cbb4`. LLM Wiki API reachable (`allowUnauthenticated:true`, v0.4.16); baseline graph **513 nodes / 4449 edges**.

### Meta-doc cleanup (Phase A)

- **`index.md`** — added 6 concept pages that existed on disk but were uncatalogued ([[value-decomposition-network]], [[impala]] under DRL backbones; [[majorization-minimization]] under optimization techniques; [[proactive-eavesdropping]] under sensing & security; [[leo-handover-protocol]] + [[fault-tolerant-relay-network]] under aerial/network architectures). Fixed the stale reference-DB count (2981 → **5054**, matching the scout-owned [[reference-database]]). Every catalogue-able wiki page is now indexed exactly once (verified with the new `index_audit.py`); the remaining multi-listed slugs are deliberate entity-roster / `>` cross-reference mentions, not duplicate bullets.
- **`overview.md`** — added the previously-missing 5th query ([[end-to-end-drl-feasibility-large-scale-mec]]) to Open questions. Snapshot counts re-verified exact via `corpus_counts.py` (171 / 234 / 71 / 14 findings / 11 synthesis / 4 comparisons / 2 methodology / 5 queries / 1 thesis); the "70 author pages + [[pytorch]] = 71" split confirmed (70 author-tagged + 1 tool).
- **`log.md`** — already consolidated (single [Raw-source housekeeping](#raw-source-housekeeping) section, strict reverse-chronological order, normalized `## YYYY-MM-DD — <title>` headers); this pass only prepended this entry. Meta docs edited with the file tools (never PowerShell redirection); verified mojibake-free at the byte level.

### Correctness & consistency audit (Phase B — batch 1/12)

Audited the just-converted **end-to-end-DRL English cluster** + **source-page batch 1** (15 pages, alphabetical al-hourani-2014 → cheng-2025; batch plan tracked in `.curation-out/audit-coverage.md`).

- **Ungrounded-number fix:** [[albakhrani-2025-moalf-uav-mec]] claimed "92.8% efficiency at double-scale / 83.5% at ten-fold scale" — **92.8% is absent from the parse** and 83.5% is a single per-system-load figure datapoint, not a scale-multiplier result. Rewrote to the parse's actual scalability framing (IoT devices 50→500, UAVs 5→50; figure-derived degradation), keeping the grounded 94.50% / 1890 / 96% / 38% / 55% claims.
- **DOI provenance fix:** [[bao-2025-ddpg-video-offloading]] cited `10.1007/s40747-025-02106-1` as if parse-grounded, but the Springer parse carries no DOI line. Added a metadata note marking the DOI + venue **web-confirmed** (Springer record), parse supplies only title/dates/year.
- **Evergreen-wording fix:** [[drl-vs-evolutionary-vs-classical-solvers]] scope note said "not a current census of all **134**" — a stale hardcoded corpus size. Rewrote to "not a current census of the full corpus" (evergreen).
- **Verified clean** (DOI/venue/year against parse; headline numbers grounded; frontmatter valid; slugs/tags/`related` consistent): the 4 end-to-end-DRL cluster pages, al-hourani-2014, apostolopoulos-2021, bai-2024, benaya-2025, bi-2025 (empty url/venue correct — no pub metadata in parse), bor-yaliniz-2016 (web-confirmed note already present), chang-2022, chen-2023, chen-2024-thoas, chen-2024-three-party, chen-2024-ulse, chen-2025. Spot-checked precise numbers verbatim: cheng-2025 "5.72% / >1.88× / 37.4% vs GE", chen-2024-ulse execution-time magnitudes.

### Toolkit

- Added **`tools/wiki/index_audit.py`** (+ README entry) — reconciles the wiki page inventory against `index.md`: reports pages on disk not catalogued and slugs linked more than once; exit non-zero on either. Promoted from what would otherwise be an ad-hoc one-off, per the toolkit ratchet.

### Gates

- **`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits. **`index_audit.py`** = 0 pages unindexed. Frontmatter diagnostics clean on every touched page.

### Routing to `mec-wiki-synthesizer` (coverage gaps — recorded, not filled)

- **Stale roster needs re-tally:** [[drl-vs-evolutionary-vs-classical-solvers]] still reasons over a 26-source family roster; a full re-census across the 171-source corpus is owed (wording made evergreen here, but the analytical broadening is the synthesizer's job).
- **Candidate synthesis:** the "multi-agent-policy-gradient as a Stackelberg-equilibrium solver" pattern appears in [[bi-2025-sg-mapg]] and relates to [[wang-2025-uav-swarm-stackelberg]] / the [[game-theoretic-offloading-formulations]] comparison — worth a synthesis page if a third source uses it.
- **Remaining audit scope:** 11 source-page batches (~156 pages) plus concepts/entities/most derived pages are unaudited; later invocations continue from `.curation-out/audit-coverage.md`.

### Correctness & consistency audit (Phase B — batch 2/12)

Audited **source-page batch 2** (15 pages, alphabetical chu-2024 → gao-2024-service-experience-cache-uav). Phase 0 re-reconciled clean (`curation_status.py --dupes`: **171 raw = 171 curated, 0 uncurated, 0 genuinely-new**); tree clean at `ecc04aa`; baseline graph **513 nodes / 4455 edges**.

- **All 15 pages verified clean** — DOIs/venues/years confirmed against each parse; headline numbers grounded against the parse text, no ungrounded numbers found. Spot-checked verbatim: [[gao-2024-service-experience-cache-uav]] "19–34% higher / 78.6% (U=4→6) / average service delay [24.1, 40.4] s (mean 33.4) / 54%·32%·23% vs GCR·FRA·NCOA"; [[dai-2023-hybrid-marine-mmwl]] "≤3% gap / >90% time saving vs LINGO"; [[chu-2024-secure-ris-isac]] "2 dB radar SNR gain w/ RIS"; [[du-2024-d2sac-aigc-asp-selection]] "seven DRL baselines (DQN/DRQN/Prioritized-DQN/Rainbow/REINFORCE/PPO/SAC)"; [[du-2024-gdm-network-optimization-tutorial]] "WoS GDM papers 12 (2014) → 257 (2023)"; [[duan-2023-moto-smallcell-offloading]] "29,284,966 records / 21,725 users / 4,045 APs". [[gao-2024-sagin-perception-offloading]] numeric setup/curves are figure-derived and already marked indicative on the page.
- **Tag-vocabulary consistency fix (corpus-wide sweep):** added the required `source` tag to **26** source pages that `frontmatter_audit.py` flagged as missing it (`updated` bumped to 2026-06-01 on each). `frontmatter_audit.py` now exits 0 over all 513 typed pages.

### Toolkit

- **Sharpened `tools/wiki/index_audit.py`** (+ README) to separate true **duplicate primary listings** (a slug that leads more than one bullet — a real defect) from deliberate cross-reference mentions (entity rosters, finding/methodology bullets citing their source, explicit `>` cross-refs). The previous "any slug linked >1x" heuristic flagged 45 deliberate cross-refs and could never reach exit 0; the refined check surfaced exactly **one genuine defect** — [[liu-2020-wpt-cooperative-uav-mec]] had a full primary bullet under both *Energy efficiency & WPT* and *Classical / convex / optimization-based UAV-MEC*. Gave it one primary home (the convex/optimization section) and a `>` cross-ref note under WPT.

### Gates (batch 2)

- **`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits. **`index_audit.py`** = 0 unindexed / 0 duplicate primary listings (45 cross-ref mentions reported informationally). **`frontmatter_audit.py`** = 0 errors over 513 pages. `index.md` verified mojibake-free at the byte level after the cross-ref edit.

### Routing to `mec-wiki-synthesizer` (batch 2 — recorded, not filled)

- **Candidate comparison:** the marine multi-access offloading pair [[dai-2023-hybrid-marine-mmwl]] (FDMA-offshore + NOMA-aerial, min-max latency, IEEE TCOMM) and [[dai-2023-hybrid-noma-fdma-marine]] (NOMA-underwater + FDMA-aerial, energy + secrecy, IEEE TNSE) align on a comparable hybrid-multiple-access marine-MEC setup validated vs the LINGO solver — worth a comparison page.
- **Candidate synthesis:** the **diffusion-model-as-optimizer / GDM-for-network-optimization** thread is now dense ([[du-2024-d2sac-aigc-asp-selection]], [[du-2024-gdm-network-optimization-tutorial]], [[fu-2025-otae-inference-lae-batching]], [[ye-2025-aigc-diffusion-contract]], [[peng-2025-drudm-cfg]], survey [[khoramnejad-2025-gai-wireless-optimization-survey]]) — a cross-source synthesis page would consolidate it.
- **Foundational-method finding:** [[fujimoto-2018-td3-actor-critic]] is the TD3 method ancestor of a large in-corpus lineage but has no finding page capturing its three overestimation-bias fixes as the grounding for downstream TD3/MATD3/CLP claims.

### Correctness & consistency audit (Phase B — batch 3/12)

Audited **source-page batch 3** (15 pages, alphabetical guo-2023-mccco-multiuav-5g-offloading → jeong-2018-uav-cloudlet-bit-allocation). Phase 0 re-reconciled clean (`curation_status.py --dupes`: **171 raw = 171 curated, 0 uncurated, 0 genuinely-new**); tree clean at `0973591`; baseline graph **513 nodes / 4455 edges**.

- **Ungrounded-number fix:** [[huang-2023-mu-aec-task-energy]] Findings claimed "one UAV's energy hits zero ~25% earlier than the others; here, all UAVs land within ~5%" — **absent from the parse**, which reports IGD/HV Pareto metrics over a makespan-vs-energy-balancing-index front (Table I, Fig. 5), not any energy-depletion-timing margin. Rewrote to the parse's actual IGD/HV result and marked the timing margin `not in parse`. Also corrected the G₂ energy-balancing-index formula: the page wrote a pairwise `Σ|E_j−E_j'|`, but parse Eq. 13 defines `Σ_j ((TE_j−mean)/ψ)²` (sum of squared normalized deviations from the swarm mean).
- **Evergreen-wording fix:** [[hu-2019-pdd-uav-mec-offloading]] relation note said [[wu-2018-multiuav-minrate-trajectory]] "is curated in this same batch" → rewrote to "is also in the corpus". `process_refs.py` had no "same batch" pattern; **extended the tool** to catch `same batch` / `in this|that|the same batch` process-narration (regression-checked it leaves domain "batch processing" / "in a batch" untouched).
- **Verified clean** (DOI/venue/year confirmed against each paper's own parse; headline numbers grounded verbatim; frontmatter valid; slugs/tags/`related` consistent): guo-2023 (`TWC.2023.3277801`), guo-2024 (`TMC.2023.3311484`), han-2024-ground-satellite (`JSAC.2024.3365901`), han-2024-sagin (`JSAC.2024.3459090`; config K=50/1200 m/N=5/20 km, 80 sats / 5 orbits / 800 km / 85° / 15°, α=0.8 all verbatim), hao-2024-clp (`TMC.2024.3350078`; system gains 78/70/64/58/54, ablation 84/80/63, 600/1500 episodes, 183→141 ms verbatim), hao-2025 (`TWC.2025.3564356`; 10–100 ms coherence-time slot grounded), he-2019 (`TPDS.2019.2938944`), he-2023 (`JIOT.2023.3241087`), hsu-2025 (`TCCN.2025.3629973`), hu-2019-pdd (`JIOT.2018.2878876`; dates→2019), hu-2019-relay (`TWC.2019.2928539`; vol 18(10) 4738–4752 web-consistent with in-parse Oct-2019 current-version), huang-2025-cmop-dispersed (venue/DOI correctly `not in parse`, misattribution note intact), huang-2025-dual-aav (`JIOT.2024.3521977`; SINR 20.75/−39.9, 64 370 J, 43.20%, 50–90% verbatim), jeong-2018 (`TVT.2017.2706308`; dates→2018).

### Toolkit (batch 3)

- Extended **`process_refs.py`** with a `same batch` / `in this|that|the same batch` process-narration pattern (+ README update); caught the leaked phrasing in [[hu-2019-pdd-uav-mec-offloading]] that the prior pattern set missed.

### Gates (batch 3)

- **`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits. **`index_audit.py`** = 0 unindexed / 0 duplicate primaries (515 catalogue-able). **`frontmatter_audit.py`** = 513 pages, 0 errors. Diagnostics clean on the edited page.

### Routing to `mec-wiki-synthesizer` (batch 3 — coverage gaps, recorded not filled)

- **Candidate finding:** [[huang-2023-mu-aec-task-energy]] is the corpus's canonical **DAG-aware multi-UAV-MEC** source (interdependent-task scheduling + energy balancing) yet has no finding page; pairs with the [[peng-2022-cmop-uav-path-planning]] → [[huang-2025-cmop-dispersed-computing]] CMOP-evolutionary lineage.
- **Candidate synthesis:** the **ground/space FL-over-satellite** thread is now several sources deep ([[han-2024-ground-satellite-fl]], [[han-2024-sagin-fl-handover]], [[zhai-2023-fedleo-decentralized-fl]], [[mao-2025-bcsa-frl]]) — a cross-source synthesis page on satellite/SAGIN federated learning would consolidate it.
- **Candidate comparison:** the early classical/convex single-UAV-MEC offloading sources ([[jeong-2018-uav-cloudlet-bit-allocation]], [[hu-2019-pdd-uav-mec-offloading]], [[hu-2019-uav-relay-edge-computing]], [[zhang-2019-uav-iot-comp-comm]], [[yu-2020-uav-ec-collaborative-offloading]]) align on objective family (energy/delay) and solver (SCA/PDD/AO) and could anchor a methodology or comparison page.

### Correctness & consistency audit (Phase B — batch 4/12)

Audited **source-page batch 4** (15 pages, alphabetical jia-2022-hierarchical-aerial-matching → li-2025-twohop-airground-drl-offloading). Phase 0 re-reconciled clean (`curation_status.py --dupes`: **171 raw = 171 curated, 0 uncurated, 0 genuinely-new**); tree clean at `f37a5ce`; baseline graph **513 nodes / 4455 edges**.

- **Correctness fixes:** [[jia-2025-dro-uav-hap-mec]] carried four ungrounded/incorrect claims against its own parse. (1) Findings "robust solutions cost ~10–20% more energy than nominal" — **not in parse** (Fig. 7 states only qualitatively that CSI errors raise energy vs the ideal-CSI case); rewrote and marked the margin `not in parse`. (2) "WKD beats vanilla **K-means**" — parse Fig. 6 compares WKD vs random-deploy+random-connect (**R&R**), not K-means; corrected. (3) "scales to ~50 UAVs / ~200 users on commodity hardware" — **not in parse**; the evaluated scales are 30 GUs / 6 UAVs (Fig. 3) and M(GUs)=10, N(UAVs)=2–5 (Figs. 4–5), HAP capacity H=10; replaced. (4) BWOA "justified vs greedy and pure **GA**" — parse compares BWOA vs exhaustive-optimal, greedy, and **simulated annealing (SAA)** (Fig. 4); corrected. DOI `TMC.2025.3571023` / year 2025 verified.
- **Ungrounded-number fix:** [[li-2024-robust-bmappo-multiuav-mec]] Findings stated a UE-agent reward ≈ −3.05; parse Fig. 3 converges to ≈ **−3.1**; softened to −3.1 (figure-read, indicative). Config K=20 / M=5 / 1000 m / 3.5–4.5 Mb / 300 episodes / γ=0.98 verified verbatim.
- **Verified clean** (DOI/venue/year against each paper's own parse; headline numbers grounded verbatim; frontmatter valid; slugs/tags/`related` consistent): jia-2022 (`JIOT.2022.3151639`), jiang-2025 (`MCOM.001.2400685`; IAGN/MBCM/CNPC/PC/ACCP/ARDCP verbatim), kang-2023 (`JIOT.2023.3240173`), khoramnejad-2025 (`COMST.2025.3535554`), lee-2024 (`TWC.2023.3342975`; 6.86×/4.18× verbatim from abstract, dates→2024), lei-2024 (`TVT.2024.3388499`), li-2023-secure-marine (`TVT.2022.3231295`; 27.32% + 0.28 W verbatim), li-2024-emodrl (`JSAC.2024.3459029`; "saves 30% handover frequency" verbatim from abstract), li-2024-emssa (`TMC.2023.3298888`), li-2024-rldc (WCNC 2024 DOI grounded via the journal cross-reference; figure values flagged as trends), li-2024-twohop-iort (`JIOT.2024.3393444`), li-2025-stochastic-game (`TGCN.2024.3424449`; five games + NE proof verbatim; figure values flagged trends), li-2025-twohop-airground (`JIOT.2025.3548088`).

### Gates (batch 4)

- **`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits. **`index_audit.py`** = 0 unindexed / 0 duplicate primaries (515 catalogue-able, 45 cross-ref mentions informational). **`frontmatter_audit.py`** = 513 pages, 0 errors. Diagnostics clean on both edited pages.

### Routing to `mec-wiki-synthesizer` (batch 4 — coverage gaps, recorded not filled)

- **Candidate synthesis:** the **collaborative-beamforming / virtual-antenna-array** thread from the Geng Sun / Jiahui Li group is now dense ([[li-2024-emssa-uav-swarm-vaa]], [[li-2024-emodrl-ground-space-cb]], [[sun-2025-emoppo-vlh-aerial-cb]], [[song-2022-emorl-tcto-uav]], [[zhang-2024-gdmtd3-aerial-secure-cb]]) — a cross-source synthesis on aerial/ground CB and its evolutionary-multi-objective-RL line would consolidate it.
- **Candidate comparison:** the two-hop air-ground IoRT pair from the same Guilin group — [[li-2024-twohop-iort-packet-scheduling]] (packet-queue delay, MADDPG + MADDQN + adaptive PER) and [[li-2025-twohop-airground-drl-offloading]] (partial-offloading delay, MADDPG-IPER + NV-IPPO) — align on a comparable two-hop UAV+HAP setup and could anchor a comparison page.
- **Candidate finding:** [[li-2025-stochastic-game-uav-swarm]] (and its conference precursor [[li-2024-rldc-uav-swarm-clustering]]) is the corpus's canonical **dynamic-clustering UAV-swarm stochastic-game** source with a Nash-equilibrium proof, but has no finding page capturing the RLDC energy-efficiency result.
- **Entity gap:** Ziye Jia recurs as lead/co-author across [[jia-2022-hierarchical-aerial-matching]], [[jia-2025-dro-uav-hap-mec]], and (co-author) [[you-2025-uncertain-maritime-hasac]]; worth an entity page (note possible affiliation drift to confirm, not resolved here).

### Correctness & consistency audit (Phase B — batch 5/12)

Audited **source-page batch 5** (15 pages, alphabetical liang-2024-hmecmop-uav-cb → mao-2024-fso-leo-hierarchical-routing). Phase 0 re-reconciled clean (`curation_status.py --dupes`: **171 raw = 171 curated, 0 uncurated, 0 genuinely-new**); tree clean at `220eaaa`; baseline graph **513 nodes / 4455 edges**.

- **Correctness fixes:** [[liu-2025-haps-uav-maritime-iot]] carried two ungrounded claims against its own parse. (1) Findings "EMOMVO-CGD beats baseline MVO and **NSGA-II** on Pareto-front quality" — **NSGA-II is not in the parse** (the evolutionary benchmarks are MOJS / MOSMA / MOEA/D / conventional MOMVO, plus the C-C-O / P-A-O / P-O / Fixed C-P-P ablations), and the page's own "Why this matters" already noted the paper does not compare against NSGA-II; rewrote the finding to the parse's actual Table II–III result (EMOMVO-CGD best on sum-backhaul-rate f₂; JCCPAPO best on sum-access-rate f₁; similar UAV energy f₃; values indicative). (2) "Backhaul rate scales much faster with UAV altitude than with HAP transmit power once a coverage threshold is crossed — placement, not power, is the bottleneck" — **not in parse**; UAVs are fixed at 100 m altitude with no altitude/power sweep, so the claim was removed. Removed the matching "doesn't head-to-head compare against them [BWOA/NSGA-II]" tail in observation 3 (kept the grounded BWOA note).
- **Verified clean** (DOI/venue/year confirmed against each paper's own parse; headline numbers grounded verbatim; frontmatter valid; slugs/tags/`related` consistent): liang-2024-hmecmop (`JIOT.2023.3315708`; HMECMOP + NP-hard-via-TSP + IMOMVO verbatim; dates→2024), liu-2020-cooperative-power-iot (`TVT.2020.3016840`; dates→2020), liu-2020-wpt (`JIOT.2019.2958975`; SCA/DAI convergence + trajectory-dominance verbatim; dates→2020), liu-2022-maritime-virtualization (`TVT.2022.3141799`; DDPG ">37%" / DQN "31%" vs center-hover baseline verbatim from conclusion), liu-2022-miso (`TVT.2022.3140833`), liu-2024-hatrpo (`TMC.2024.3419915`; 750 vs ~1,400 epochs + Table III energy 13,401/10,261 J + MADDPG 22,319 J verbatim), liu-2026-jppo (no DOI/venue — correctly empty; 21.21% energy-eff @5 UAVs + 76.2% vs NeuralMap @2 UAVs verbatim), lyu-2023 (`JIOT.2023.3348164`; CGTO vs LC/OCG/HOCO/IOJRA/DDPG + ground-disaster scalability grounded), ma-2025 (`TVT.2025.3574783`; P-DQN vs DQN/DDPG/convex + handoff-cost grounded), mach-2017 (`COMST.2017.2682318`; AR latency "up to 88%" / UE energy "up to 93%" correctly attributed to the survey's cited testbed reference), mahboob-2024 (`COMST.2023.3347145`; 1 Tbps peak / µs latency / GEO 35,786 km ~270 ms / LEO ~600 km verbatim; dates→2024), mao-2016 (`JSAC.2016.2611964`; vol 34(12) 3590–3605 web-consistent; LODCO asymptotic optimality + monotonic CPU/power-vs-battery grounded), mao-2017 (`COMST.2017.2745201`), mao-2024-fso (`JSAC.2024.3365880`; dual-layer MEO/LEO + MO-DRL routing + APT-terminal adaptivity grounded; dates→2024).

### Gates (batch 5)

- **`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits. **`index_audit.py`** = 0 unindexed / 0 duplicate primaries (515 catalogue-able, 45 cross-ref mentions informational). **`frontmatter_audit.py`** = 513 pages, 0 errors. Diagnostics clean on the edited page; graph unchanged at **513 nodes / 4455 edges**.

### Routing to `mec-wiki-synthesizer` (batch 5 — coverage gaps, recorded not filled)

- **Candidate synthesis — `hap-roles-in-mec`:** [[liu-2025-haps-uav-maritime-iot]] (HAP-as-backhaul) joins HAP-as-compute ([[peng-2025-drudm-cfg]], [[wang-2026-aerial-marine-msar]]) and HAP-as-relay-with-NOMA ([[hsu-2025-drl-hues-hap-noma]]); all three distinct HAP roles are now in the corpus and warrant a synthesis page (the page itself flags this).
- **Candidate comparison — hybrid-action DRL:** [[ma-2025-pdqn-vehicular-mec]] (P-DQN, value-based) and [[liu-2026-jppo-en-convntm]] (j-PPO, policy-gradient) solve the same discrete-destination + continuous-power/ratio hybrid-action MEC problem from opposite corners; both pages already call for a `j-ppo-vs-pdqn` comparison once a deciding factor emerges.
- **Candidate finding — foundational green-MEC anchor:** [[mao-2016-lodco-eh-mec-offloading]] originates the Lyapunov-per-slot online-offloading pattern that recurs corpus-wide but has no finding page capturing LODCO's asymptotic-optimality + monotonic-structure result as the grounding for downstream Lyapunov-MEC claims.
- **Foundational-survey cluster:** the four MEC/NTN survey anchors ([[mach-2017-mec-survey-architecture]], [[mao-2017-mec-survey-communication]], [[mahboob-2024-ai-ntn-survey]], [[wang-2025-lae-network-survey]]) span terrestrial→aerial→non-terrestrial and could anchor a methodology/synthesis page on how the corpus's MEC scope has migrated skyward.
- **Entity gap:** Yong Zeng recurs (co-author of [[liu-2020-wpt-cooperative-uav-mec]] and lead/co-author across the zeng-2016/2017/2019 trajectory lineage); flagged for an entity page on a later batch that covers those sources.

### Correctness & consistency audit (Phase B — batch 6/12)

Audited **source-page batch 6** (15 pages, alphabetical mao-2024-ntn-hierarchical-caching-cav → pervez-2024-acm-multiuav-mec). Phase 0 re-reconciled clean (`curation_status.py --dupes`: **171 raw = 171 curated, 0 uncurated, 0 genuinely-new**); tree clean at `61e435a`; baseline graph **513 nodes / 4455 edges**.

- **Correctness fixes:** [[nabi-2025-jour-hierarchical-aerial]] carried several claims unsupported by its own parse. (1) Findings cited baselines "DDPG, **MAPPO**, and **SAC-no-PER**" — the parse's learning baselines are GOUA+SAC / GOUA+PPO / GOUA+DDPG plus a GOUA+heuristic (HA); **MAPPO appears only as related work [8], and there is no SAC-no-PER ablation**. Rewrote to the parse's actual baseline set and Fig. 5–13 results. (2) "Load-balancing variance reduction… max-min UAV energy gap shrinks ~30% vs greedy baselines" — **not in parse**; the third objective term (Eq. 25a) is per-UAV **load = computed cycles / compute capacity**, not remaining-energy variance, and no ~30%/greedy metric exists; replaced with the grounded objective + average-per-UAV-load result. (3) "stable associations even under highly **heterogeneous UAV capacities**" — parse states UAVs are **homogeneous** (identical capacity within a scenario); corrected the Method/Findings and added the homogeneous-UAV limitation. (4) Limitation "GUs do not move" **contradicts** the parse ("the GUs are not static; however, the UAVs and HAP positions are static"); rewrote to fixed UAV/HAP positions with mobile GUs and recomputed-each-slot association.
- **Verified clean** (DOI/venue/year confirmed against each paper's own parse; headline numbers grounded verbatim; frontmatter valid; slugs/tags/`related` consistent): mao-2024-ntn-hierarchical-caching-cav (`JSAC.2024.3460063`; WMVC→TSP NP-hard + DM-ACO + MADRL-HCAU + qualitative CHR/delay vs popularity/LIFO grounded; dates→2024), mao-2025-bcsa-frl (`JSAC.2025.3560003`; drop/delay 6.16%/5.95 ms @150, 8.29%/6.08 ms @450, Avg-Task-Burden 20.05%/7.40 ms, Random 40.54%/9.31 ms, ≈5%/≈6 ms ≤50% malicious, CCVM ablation reward <10 vs ~25, optimal reward 26 all verbatim; >51% majority breaks consensus), mao-2025-irs-noma-fl-secrecy (`TCCN.2024.3454256`; max-min secrecy-rate + DDPG + IRS-improves-secrecy grounded, gains correctly indicative; dates→2025), meng-2024-uav-isac-overview (`MWC.131.2200442`; overview, no original numbers — correctly stated), miao-2022-gaglpp-drone-swarm-iiot (`TII.2022.3196392`; GAGLPP global+local split + energy-efficiency result grounded; dates→2023), michailidis-2024-secure-ris-uav-mec-iot (`TCOMM.2024.3372877`; SOP-over-Nakagami-m + Dinkelbach/BCD/bisection + ~57/~60-element thresholds figure-derived/indicative; dates→2024), mozaffari-2017-uav-iot-energy-efficient (`TWC.2017.2751045`; 45% transmit-power + 28% reliability verbatim from abstract; dates→2017), mozaffari-2019-uav-wireless-tutorial (`COMST.2019.2902862`; HAP>17 km, US 122 m/Australia 120 m regulatory table verbatim), niazmand-2025-jopa-dnn-pruning-iiot (`TCCN.2025.3529688`; JOPA/JOPAV1/AGDM + <1% drop + p=0.7 pruning grounded), peng-2020-maddpg-uav-vehicular (`JSAC.2020.3036962`; converges within 200 episodes + higher delay/QoS satisfaction vs SADDPG/random verbatim; dates→2020), peng-2022-cmop-uav-path-planning (`LWC.2022.3149007`; ToP/PPS baselines, 3×10⁴ function evals, I=1 device, IGD/HV Table I verbatim), peng-2024-energy-time-uav-its (`TITS.2024.3395993`; CMOEA/D-CDP + completion-time-difference + service-caching grounded), peng-2025-drudm-cfg (no DOI/venue — correctly empty; only reference-list DOIs present), pervez-2024-acm-multiuav-mec (`TWC.2023.3291692`; potential-game NE + GWF + SCA + ~9 iterations + ~12%/~10% vs two prior methods verbatim; dates→2024).

### Gates (batch 6)

- **`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits. **`index_audit.py`** = 0 unindexed / 0 duplicate primaries (515 catalogue-able, 45 cross-ref mentions informational). **`frontmatter_audit.py`** = 513 pages, 0 errors. Diagnostics clean on the edited page; graph unchanged at **513 nodes / 4455 edges**.

### Routing to `mec-wiki-synthesizer` (batch 6 — coverage gaps, recorded not filled)

- **Candidate finding — synchronization-as-objective:** the "everyone-finish-together" objective recurs across [[peng-2024-energy-time-uav-its]] (pairwise completion-time-difference), [[mao-2025-bcsa-frl]] (FRL round synchronization), and [[xie-2026-uav-multisource-fusion]] (multi-source fusion timing). A [[completion-time-difference]] concept exists but no finding/synthesis ties the cross-source pattern together.
- **Candidate finding — Bomin Mao NWPU non-terrestrial/security cluster:** [[mao-2024-ntn-hierarchical-caching-cav]], [[mao-2025-bcsa-frl]], and [[mao-2025-irs-noma-fl-secrecy]] (all on [[bomin-mao]]'s roster, with [[nei-kato]]) form a coherent LEO/NTN caching+offloading+security thread with no cross-source synthesis page yet.
- **Entity gap:** Walid Saad and Mérouane Debbah recur across [[mozaffari-2017-uav-iot-energy-efficient]] and [[mozaffari-2019-uav-wireless-tutorial]] (and the broader UAV-comms foundational anchors); [[walid-saad]] and [[mohammad-mozaffari]] entity pages exist, but a Debbah page does not — flagged, not created.
- **Entity gap:** Qiang Ye recurs as the cross-cutting author of [[niazmand-2025-jopa-dnn-pruning-iiot]], [[wang-2024-maritime-eh-jcora]], and [[zhang-2025-vnf-sgin-dql]]; worth an entity page on a later pass.

### Correctness & consistency audit (Phase B — batch 7/12)

Audited **source-page batch 7** (15 pages, alphabetical qi-2024-msar-minmax-latency → sun-2024-imssa-uav-secure-cb). Phase 0 re-reconciled clean (`curation_status.py --dupes`: **171 raw = 171 curated, 0 uncurated, 0 genuinely-new**); tree clean at `efe92e4`; baseline graph **513 nodes / 4455 edges**.

- **Correctness fix (cross-corpus count):** [[sun-2024-asap-uav-swarm]] claimed it was "one of only **two** hardware-validated sources in the corpus (with [[shao-2024-drl-antijamming-mec]])". This undercounts: the corpus has at least four hardware-validated sources — ASAP (24 Jetson computers + 5 real UAVs), [[shao-2024-drl-antijamming-mec]] (Raspberry Pi 4B / USRP testbed), [[zhang-2020-response-delay-uav-swarm]] (real DJI M100 UAVs + 5G NR mmWave testbed; itself tagged `hardware-validated` and already enumerating this exact 4-source set), and [[qu-ecoei-uav-swarm]] (airborne Jetson Nano/TX2 proof-of-concept) — and [[sun-2024-imssa-uav-secure-cb]] adds a Raspberry Pi implementation. Rewrote to "one of the few hardware-validated sources … alongside [shao-2024, zhang-2020, qu-ecoei]"; `updated` → 2026-06-01.
- **Verified clean** (DOI/venue/year confirmed against each paper's own parse; headline numbers grounded verbatim; figure-/abstract-derived numbers marked indicative; frontmatter valid; slugs/tags/`related` consistent): qi-2024-msar (`TVT.2024.3384570`; min-max-latency S-UAV/R-UAV, linearization+SCA+BnB; dates→2024), qin-2025-bcuav (`TWC.2025.3582151`; **13.16%↑ sensing rate / 29.47%↓ queue delay vs the strongest baseline PSO** — verbatim, MinerU rendered the digits spaced as `$1 3 . 1 6 \%$`; NT-MASAC/NP-MASAC/MADDPG/PSO baselines + DOA + DPoS/PBFT all grounded; dates→2025), qin-2025-matd3 (`TVT.2025.3552807`; MATD3 + Lyapunov + MTDTO/GSCRA qualitative), qu-ecoei (`MCOM.002.2300129`; year correctly `not in parse`; 0.8→2.9 FPS scaling + 3→2 FPS failover + Jetson PoC verbatim), raivi-2024 (`JIOT.2024.3354950`; 20% / 11.4% / 5.6% / 11.2% / 98% all verbatim incl. Qmix/COMA/HGA baselines; dates→2024), schulman-2017-ppo (arXiv:1707.06347; DOI/venue correctly `not in parse` + web-confirmed note; ε=0.2 clip, 0.82 vs −0.39 surrogate scores; MuJoCo/Atari curves indicative), seid-2021 (`TNSM.2021.3096673`; 38.643% / 55.621% / 58.289% / 85.289% verbatim from abstract+conclusion; dates→2021), shao-2024 (`TMC.2024.3432491`; PER-MATD3, ξ=0.5; Raspberry Pi/USRP testbed magnitudes figure-derived/indicative), song-2022-emorl (`TMC.2022.3208457`; EMORL-TCTO vs NSGA-II/MOEA-D/EDDPG/ETD3/EMORL grounded; pub Sept-2022 / current-version Nov-2023 → 2022 defensible), song-2024-mol (`TMC.2024.3394568`; 39.8% / 2.1% / 15.3% + AAoI 50.6/46.3/52.2/45.9/39.9% + AEC/AC sequences all verbatim; dates→2024), su-2024 (`TWC.2023.3306029`; sensing-aided-PLS CRB/secrecy mutual-benefit qualitative; pub Aug-2023 / current-version Apr-2024 → 2024 defensible), sun-2023-bargain-match (`TMC.2023.3239339`; bargaining+matching, stable/weak-Pareto/polynomial verbatim), sun-2024-active-passive-ris (`TWC.2023.3325813`; PSR 32.8% vs 75.9% / 2.78× / ~0 dB vs −10 dB SINR / −50 dB jammer all verbatim; pub Oct-2023 / current-version Jun-2024 → 2024), sun-2024-asap (`TMC.2024.3427420`; 92.66% / 98.50% / 95.35% / 96.84% / 83.37% all verbatim — see correctness fix above), sun-2024-imssa (`TMC.2023.3273293`; IMSSA vs MOPSO/NSGA-II/MODE/MSSA/IMODACH + Raspberry Pi impl + ISCC-2022 precursor noted; pub May-2023 / current-version Mar-2024 → 2024).

### Gates (batch 7)

- **`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits. **`index_audit.py`** = 0 unindexed / 0 duplicate primaries (515 catalogue-able, 45 cross-ref mentions informational). **`frontmatter_audit.py`** = 513 pages, 0 errors. Diagnostics clean on the edited page; graph unchanged at **513 nodes / 4455 edges**.

### Routing to `mec-wiki-synthesizer` (batch 7 — coverage gaps, recorded not filled)

- **Candidate finding — hardware-validated reality check:** four corpus sources carry real-hardware validation ([[sun-2024-asap-uav-swarm]], [[shao-2024-drl-antijamming-mec]], [[zhang-2020-response-delay-uav-swarm]], [[qu-ecoei-uav-swarm]]) in a heavily simulation-only literature; a finding/synthesis page consolidating what the testbeds actually demonstrate (and where they diverge from simulation) would be valuable.
- **Candidate synthesis — in-swarm collaborative DL inference:** [[sun-2024-asap-uav-swarm]] (ASAP) and [[qu-ecoei-uav-swarm]] (eCoEI) are the same NUAA group's system + architecture pair on swarm-internal DNN partition/pipeline inference, siblings of [[huang-2025-cmop-dispersed-computing]]; no cross-source synthesis page ties the collaborative-inference thread together.
- **Candidate synthesis — multi-objective evolutionary-vs-RL for UAV trajectory/energy:** [[song-2022-emorl-tcto-uav]] and [[song-2024-mol-aoi-energy]] (Fuhong Song lineage; EMORL/MOL hybrids) sit alongside the pure-CMOP [[peng-2022-cmop-uav-path-planning]] / [[peng-2024-energy-time-uav-its]] and feed the existing [[drl-vs-evolutionary-vs-classical-solvers]] comparison — a focused multi-objective-RL synthesis could deepen that thread.
- **Entity gap:** the Geng Sun / Zemin Sun / Jiahui Li Jilin-University collaborative-beamforming cluster recurs across [[sun-2024-imssa-uav-secure-cb]], [[sun-2023-bargain-match-vec]], [[sun-2024-mvtora-postdisaster-vfc]], [[liu-2024-hatrpo-ucb-cb]] and more; [[geng-sun]] exists but Zemin Sun / Jiahui Li entity pages were not checked-for/created here.

### Correctness & consistency audit (Phase B — batch 8/12)

Audited **source-page batch 8** (15 pages, alphabetical sun-2024-mfris-semantic-antijamming → wang-2025-acbft-uav-consensus). Phase 0 re-reconciled clean (`curation_status.py --dupes`: **171 raw = 171 curated, 0 uncurated, 0 genuinely-new**); tree clean at `986512d`; baseline graph **513 nodes / 4455 edges**.

- **All 15 pages verified clean** — every DOI/venue/year confirmed against the paper's own parse; headline numbers grounded verbatim or marked figure-/abstract-derived indicative; frontmatter valid; slugs/tags/`related` consistent (no self-references). No ungrounded numbers found this batch.
- **Headline-number cross-check focus — [[wang-2025-acbft-uav-consensus]] "96.2% throughput":** the value is **genuinely grounded** — stated verbatim in the paper's contributions list ("ACBFT achieves an increase in throughput of up to 96.2%", parse L35) and the page already carries a metadata note distinguishing it from the per-node-count Fig. 6 curves (which remain indicative). This is a real paper-stated number, **not** the fabricated-96.2% anti-pattern; left as-is.
- **Verified verbatim / grounded:** sun-2024-mfris (`JSAC.2024.3459028`; MF-RIS + semantic anti-jamming + MO-DSOCP/GPI; benchmarks qualitative; WCSP-Hefei-2024 precursor + dates→2024 grounded), sun-2024-mvtora (`TMC.2024.3350886`; MVTORA game+convex+evolutionary, NP-hard, MSN-2022 precursor in parse), sun-2024-ues (`TVT.2023.3344281`; "doubling of the system's lifetime" verbatim abstract; pub Dec-2023 / current-version 16 May 2024 → 2024 convention correct), sun-2025-emoppo (`TMC.2025.3536093`; EMOPPO-VLH IGD/HV qualitative; the in-paper "MOPPO-PLE" naming-inconsistency note is accurate), sun-2025-tjcct (`TMC.2024.3505155`; two-timescale price-incentive+matching+convex; INFOCOM-2024 precursor DOI `10.1109/INFOCOM52122.2024.10621095` grounded verbatim; dates→2025), tang-2024-iscc (`TWC.2024.3523381`; ISCC + FEEL + BBPO alternating-opt), wang-2019-todetas (`TCYB.2019.2935466`; ToDeTaS two-layer DE+greedy, up to 1000 users), wang-2021-maddpg (`TCCN.2020.3027695`; MADDPG dual-fairness+energy; pub Sept-2020 / current-version Mar-2021 → 2021), wang-2022-cat-rat (`TMC.2021.3059691`; CAT/BCD + RAT/twin-DQN+PER; pub Feb-2021 / current-version Aug-2022 → 2022), wang-2024-blockchain (`TVT.2023.3306740`; consortium DPoS + Stackelberg + SCA; pub Aug-2023 / current-version Jan-2024 → 2024), wang-2024-hfrl (`TMC.2024.3439696`; SHDRLN+DFRL; 2.7 KB/J @100/200/300-ep + 2.4 KB/J @50/100-ep all figure-read from Table II curves and flagged indicative), wang-2024-hybrid-oma-noma (`TVT.2024.3452477`; SCA+Lagrange / DQN mode-selection; pub Aug-2024 → 2024), wang-2024-maritime-eh (`JIOT.2024.3371049`; JCORA Lyapunov drift-plus-penalty + [O(1/V),O(V)] tradeoff + FRA/LRA/PRA/TRA baselines qualitative), wang-2024-twotier (`JIOT.2024.3523527`; Stackelberg+bargaining marine NOMA/FDMA), wang-2025-acbft (`TVT.2025.3548281`; PSO chain-ordering + 96.2% throughput grounded — see above).

### Gates (batch 8)

- **`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits. **`index_audit.py`** = 515 catalogue-able, 0 unindexed / 0 duplicate primaries (45 cross-ref mentions informational). **`frontmatter_audit.py`** = 513 pages, 0 errors. No pages required edits this batch, so graph is unchanged at **513 nodes / 4455 edges**.

### Routing to `mec-wiki-synthesizer` (batch 8 — coverage gaps, recorded not filled)

- **Candidate comparison — convex-baseline-vs-learned-solver UAV-MEC trajectory:** [[wang-2022-cat-rat-fmec-trajectory]] explicitly pairs a convex solver (CAT/BCD) with a DRL solver (RAT/twin-DQN+PER) on the same energy-minimization problem; it aligns closely with [[zhang-2024-uav-task-offloading-ddpg]] (decomposition + DDPG) and [[liu-2022-miso-uav-mec-trajectory]] (alternating optimization) for a focused comparison page.
- **Candidate synthesis — blockchain/trust layer for aerial MEC:** the [[blockchain-on-edge-trust-layer]] thread now spans the consensus-protocol layer ([[wang-2025-acbft-uav-consensus]]), DPoS-secured offloading ([[wang-2024-blockchain-uav-mec-dpos]]), secure UAV-MEC ([[qin-2025-bcuav-masac]]), and FRL aggregation ([[mao-2025-bcsa-frl]]) — dense enough that a synthesis page consolidating the consensus-vs-aggregation-vs-offloading uses would help.
- **Candidate synthesis — game-theoretic maritime offloading:** the Wang/Lin/Ye maritime cluster ([[wang-2024-twotier-satellite-marine]] Stackelberg+bargaining, [[wang-2024-maritime-eh-jcora]] Lyapunov-EH, [[wang-2025-double-edge-samin]] optimization, [[you-2025-uncertain-maritime-hasac]] DRL) covers the same satellite-marine offloading problem with four different solver families — a comparison/synthesis page is warranted.
- **Entity gaps (recurring authors, not created here):** Geng Sun / Zemin Sun anchor four batch-8 Jilin sources ([[sun-2024-mvtora-postdisaster-vfc]], [[sun-2025-emoppo-vlh-aerial-cb]], [[sun-2025-tjcct-twotimescale-uav-mec]], plus co-authorship on [[wang-2024-hfrl-decentralized-navigation]]); [[zemin-sun]] is now referenced by `sun-2025-tjcct` but its entity page was not checked-for here. Kezhi Wang corresponds on both [[wang-2021-maddpg-multiuav-trajectory]] and [[wang-2022-cat-rat-fmec-trajectory]] ([[kezhi-wang]] referenced). Qiang Ye recurs across [[wang-2024-maritime-eh-jcora]] + [[wang-2024-twotier-satellite-marine]] (re-flagged from batch 6).

### Correctness & consistency audit (Phase B — batch 9/12)

Audited **source-page batch 9** (15 pages, alphabetical wang-2025-double-edge-samin → xu-2024-mobile-aigc-survey). Phase 0 re-reconciled clean (`curation_status.py --dupes`: **171 raw = 171 curated, 0 uncurated, 0 genuinely-new**); tree clean at `e5157e2`; baseline graph **513 nodes / 4455 edges**.

- **Correctness/consistency fix — [[wang-acve-constraint-violation-cmop]] self-contradictory metadata.** The page's frontmatter, Citation, and metadata note correctly ground venue/year/DOI **cross-corpus** (`TEVC.2025.3569722`, cited verbatim as reference [8] in [[huang-2025-cmop-dispersed-computing]]), but its Limitations section still claimed the metadata "could not be confirmed … left as `not in parse`". Rewrote Limitations to agree with the grounded note (the paper's own parse has no publication line; metadata grounded cross-corpus).
- **Evergreen-wording fixes — curation ingest-order narration removed corpus-wide.** Six leaks rewritten into statements of fact about the corpus: [[wang-2025-uav-swarm-stackelberg]] ("recurring in the queue … upcoming low-altitude-economy paper" + "upcoming paper #10 (Toward Low-Altitude Economy)" → named links to [[wang-2025-lae-network-survey]]); [[peng-2025-drudm-cfg]] and concept [[hierarchical-aerial-mec]] ("paper #8 SG-MAPG, paper #10 low-altitude economy" → [[bi-2025-sg-mapg]] / [[wang-2025-lae-network-survey]]); concept [[low-altitude-intelligent-network]] (heading "(likely covered by paper #10)" dropped); [[zhang-2025-mcma-task-migration]] ("later in the queue" → track-fit statement); [[jiang-2025-isac-lae-overview]] ("upcoming LAE-MEC papers" → "LAE-MEC work across the corpus"). `updated` bumped to 2026-06-01 on the edited pages.
- **All 15 source pages verified clean** — DOI/venue/year confirmed against each paper's own parse (or correctly `not in parse` with cross-corpus/web-confirmed provenance); headline numbers grounded verbatim or flagged figure-/abstract-derived indicative; frontmatter valid; slugs/tags/`related` consistent (no self-refs). Spot-checked verbatim: wang-gai-isac 1.03° DoA MSE + NMSE −7.05 vs −2.46 dB @ CR 1/64; wu-2025-iopo 32.8% vs DDPG / 823.32 vs 1225.47 / OPPO 1247.98 vs 1408.36 / 127,966 improved decisions; xu-2018-uav-wpt D≤5.77 m threshold + β₀=−30 dB/H=5 m/P=40 dBm (near-far ~0.19 vs ~0.013 mW figure-derived, indicative). DOIs confirmed: `TVT.2025.3561346`, `TCCN.2025.3601015`, `JIOT.2025.3542025`, `TVT.2025.3595972`, `TCCN.2025.3642113`, `MWC.013.2300485`, `TWC.2017.2789293`, `TWC.2023.3307154`, `TMC.2024.3461719`, `TVT.2025.3604250`, `TWC.2026.3676831`, `TWC.2018.2838134`, `COMST.2024.3353265`. `wang-gai-isac` and `xiang-sac-mapless` carry correct `not in parse` year/venue notes (the latter with an IEEE Xplore doc-8996652 note, no guess).

### Toolkit (batch 9)

- **Extended `process_refs.py`** with a `paper\s+#\d+` pattern — curation ingest-order references ("paper #8", "paper #10") that the prior pattern set missed. It surfaced 4 leaks across 4 pages; all fixed, tool now exits 0. The "queue"/"upcoming" phrasing was deliberately **not** added to the tool (too much domain overlap with priority/task-queue and ordinary "upcoming" usage) and was fixed by hand instead.

### Gates (batch 9)

- **`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits (after the fixes). **`index_audit.py`** = 515 catalogue-able, 0 unindexed / 0 duplicate primaries (45 cross-ref mentions informational). **`frontmatter_audit.py`** = 513 pages, 0 errors. Prose-only edits, no new pages — graph unchanged at **513 nodes / 4455 edges** (API re-pulled post-edit to confirm). Edited pages verified mojibake-free at the byte level (file tools, never PowerShell redirection).

### Routing to `mec-wiki-synthesizer` (batch 9 — coverage gaps, recorded not filled)

- **Candidate comparison — UAV-MEC solver families on the maritime offloading problem:** the Wang/Lin/Ye maritime cluster is now four-deep with distinct solvers — [[wang-2025-double-edge-samin]] (alternating optimization), [[wang-2026-aerial-marine-msar]] (matching + convex + PGD), [[wang-2024-twotier-satellite-marine]] (Stackelberg + bargaining), [[you-2025-uncertain-maritime-hasac]] (HASAC DRL) — reinforcing the batch-8 routing note that a comparison/synthesis page across these solver families is warranted.
- **Candidate comparison — CMOP-evolutionary UAV trajectory lineage:** [[wu-2026-terrain-aware-uav-mec]] (multi-tasking CMOEA, DEM terrain-aware), [[peng-2022-cmop-uav-path-planning]], [[peng-2024-energy-time-uav-its]], [[huang-2025-cmop-dispersed-computing]] (dual-population), and the methods anchor [[wang-acve-constraint-violation-cmop]] (ACVE/DDCo) form a tight constrained-multi-objective family; the existing [[cmop-evolutionary-uav-mec-lineage]] synthesis may be due a re-census as this lineage has grown.
- **Candidate finding — foundational UAV-comm/WPT anchors:** [[wu-2018-multiuav-minrate-trajectory]] (max-min-rate BCD+SCA) and [[xu-2018-uav-wpt-trajectory]] (single-location-hover-optimal sum-energy + successive hover-and-fly) are heavily-cited foundational anchors with no finding page capturing their canonical results.
- **Entity ambiguity (noted, not resolved):** [[xu-2018-uav-wpt-trajectory]] first author **Jie Xu** (Guangdong University of Technology) is flagged on-page as distinct from the existing [[jie-xu]] entity (CUHK-Shenzhen, ISAC); namesake disambiguation is the synthesizer's call. Bin Lin / Qiang Ye (maritime cluster) already have entity pages.

### Correctness & consistency audit (Phase B — batch 10/12)

Audited **source-page batch 10** (15 pages, alphabetical yang-2019-sum-power-uav-mec → zhang-2013-energy-optimal-mcc-stochastic). Phase 0 re-reconciled clean (`curation_status.py --dupes`: **171 raw = 171 curated, 0 uncurated, 0 genuinely-new**); tree clean at `25a9c54`; baseline graph **513 nodes / 4455 edges**.

- **All 15 source pages verified clean** — no corrections needed. DOI/venue/year confirmed against each paper's own parse; headline numbers grounded verbatim or flagged figure-/abstract-derived indicative; frontmatter valid; slugs/tags/`related` consistent (no self-refs). DOIs confirmed: `TWC.2019.2927313`, `JIOT.2020.2971645`, `TWC.2022.3142365`, `TMC.2024.3406607`, `LWC.2025.3588758`, `TVT.2024.3463420`, `TVT.2025.3581970`, `JIOT.2020.2965898`, `TCOMM.2016.2611512`, `TWC.2017.2688328`, `TWC.2019.2902559`, `JPROC.2019.2952892`, `TVT.2024.3359310`, `TMC.2023.3304988`, `TWC.2013.072513.121842`.
- **Headline numbers spot-checked verbatim against parses:** yang-2019 IACL/SCAFAH/ECC/EXH, fuzzy-c-means initializer, ">1000 W initial → ~420 W after three iterations" (figure-read, flagged indicative on-page); yang-2020 400×400 m / B=1 MHz / H=100 m / N=5 UAVs / K=100 IoT, DRL vs FCFS/SJF/RR; ye-2025 ρ-coefficients (9.7417/0.0978/0.7647/0.5158/3497.8463/0.0307), s^A,min=4, prompt-opt +8%/+2% quality and +22% latency-reduction, 380% correctly attributed to cited work [7]; zeng-2024 participation degree +28.27%/+25.74% (vs RBS/GBS over task size) and +27.84%/+21.14% (over fleet count), convergence ~1500 iter (sharpest first ~800); zhai-2023 FedLEO up-to-41% lower delay / up-to-9.39% higher accuracy; zhang-2013 κ=10⁻¹¹, λ=1.5 → κ/λ=6.67×10⁻¹² (correctly computed). yang-2022 / yang-2024-taco / yao-2025 / you-2025 / yu-2020 / zeng-2016 / zeng-2017 / zeng-2019-rotary / zeng-2019-tutorial verified clean (DOI/method/qualitative results grounded; figure values flagged indicative). Year-disambiguation re-confirmed against publication dates (e.g. yao-2025 LWC pub 15 Jul 2025; zeng-2016 TCOMM date-of-current-version Dec 2016; zeng-2019-rotary current version Apr 2019).

### Gates (batch 10)

- **`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits. **`index_audit.py`** = 515 catalogue-able, 0 unindexed / 0 duplicate primaries (45 cross-ref mentions informational). **`frontmatter_audit.py`** = 513 pages, 0 errors. No page edits this batch — graph unchanged at **513 nodes / 4455 edges**.

### Routing to `mec-wiki-synthesizer` (batch 10 — coverage gaps, recorded not filled)

- **Candidate findings — foundational Zeng/Zhang UAV-communications anchors:** [[zeng-2016-throughput-relaying]] (UAV mobile relaying + "staircase" water-filling + information-causality), [[zeng-2017-energy-efficient-uav-trajectory]] (first fixed-wing propulsion-energy model + bits/Joule), and [[zeng-2019-rotary-wing-energy-min]] (canonical rotary-wing propulsion model) are heavily-cited foundational anchors with no finding page capturing their canonical results; [[zeng-2019-uav-comm-tutorial-5g]] is a foundational survey similarly without a finding/synthesis tie.
- **Candidate synthesis — propulsion-energy model lineage:** the fixed-wing ([[fixed-wing-propulsion-energy-model]], zeng-2017) vs rotary-wing ([[rotary-wing-propulsion-energy-model]], zeng-2019) split is referenced widely across the energy-aware [[uav-trajectory-control]] sources; a short synthesis tying which corpus sources adopt which model would consolidate a recurring thread.
- **Candidate comparison — LEO-satellite + federated learning:** [[zhai-2023-fedleo-decentralized-fl]] (server-free decentralized aggregation + offloading), [[mao-2025-bcsa-frl]] (blockchain-aggregated FRL), and [[han-2024-sagin-fl-handover]] (FL over SAGIN with handover) form a 3-source FL-over-satellite cluster with no comparison/synthesis page.
- **Candidate comparison — maritime AAV/USV offloading solver families (reinforced):** [[you-2025-uncertain-maritime-hasac]] (Lyapunov → Markov game → heterogeneous-agent SAC) and [[zeng-2024-usv-fleet-collaborative-offloading]] (reverse-auction + ADMM/BCD) add two more solver styles to the Wang/Lin/Ye maritime cluster flagged in batches 8–9; the comparison page remains owed.

### Correctness & consistency audit (Phase B — batch 11/12)

Audited **source-page batch 11** (15 pages, alphabetical zhang-2019-stochastic-offloading-uav-mec → zhao-2025-traj-offload-cache-migration). Phase 0 re-reconciled clean (`curation_status.py --dupes`: **171 raw = 171 curated, 0 uncurated, 0 genuinely-new**); tree clean at `c3bc07c`; baseline graph **513 nodes / 4455 edges**.

- **Correctness fix — [[zhang-2025-mcma-task-migration]]** had two method-level errors vs its parse. (1) The two-stage decision framework was described as "Stage 1 (coarse) discrete migration target — naturally Q-style" + "Stage 2 (fine) offloading + resource allocation"; the parse (Sec. IV-C) states both stages are policy-gradient — **MAPPO** for the discrete migration-assisted *offloading* decision (stage 1) and **MADDPG** for the continuous *resource allocation* (stage 2), neither Q-style. Rewrote TL;DR + Method to match, and folded the base-model-agnostic note (MADDQN/Qmix/MATD3/COMA) into stage 3. (2) Findings cited a "**MADDPG-only** and migration-without-prediction" baseline pair that is **not in the parse**; the actual baselines are heuristics (VE/EO/PO-x/RE), DRL methods (M-DRL, AB-MAPPO, MADDQN, MATD3), and ablations (w/o-{m&p}/{a}/{co}). Rewrote Findings to the grounded baselines + ablations.
- **Correctness fix — [[zhang-2025-ssac-mgi-heterogeneous-uav]]** mischaracterized the MGI mechanism. The page framed MGI as an *inter-UAV* subgame ("when two UAVs are on a near-collision trajectory, one acts as intervention agent and the other non-intervention", with a "symmetric-deflection failure mode" and a "Nash equilibrium guarantees collision avoidance"). The parse (Sec. V-B) defines MGI as a **per-UAV** two-agent game: each UAV is jointly controlled by a stochastic **Standard Agent** (reward-maximizing) and a deterministic **Safety Agent** with a binary gating policy `g(s)` that overrides the standard action when triggered (Eq. 32–34), giving safety guarantees during and after training. Rewrote the MGI description (TL;DR + Method) accordingly. Also corrected Findings — the real baselines are SSAC, STRPO, SCPO, SSAC-MGI-FCFS, and a MANUAL trajectory policy (not "vanilla MASAC and MADDPG"; the "symmetric collision-avoidance heuristics" claim was removed) — and the Limitations (UAVs fly at constant altitude so the trajectory is effectively 2-D, which **is** grounded; parse future work is multi-modal perception + online fine-tuning).
- **Verified clean** (DOI/venue/year against own parse; headline numbers grounded verbatim or flagged figure-/abstract-derived indicative; frontmatter valid; slugs/tags/`related` consistent, no self-refs): zhang-2019-stochastic-offloading (JIOT.2018.2890133; MAES/MAEU benchmarks + Lyapunov/ADMM/interior-point/CVX verbatim), zhang-2019-uav-iot-comp-comm (TII.2019.2948406; Lagrangian-duality + SCA, "dozen iterations" verbatim), zhang-2020-response-delay-uav-swarm (TVT.2020.2964821; 10%–20% delay decrease + 89.9% packet reduction + 7.84 Mbit→775.9 kbit + DJI M100/28 GHz/64-element testbed all verbatim; hardware-validated), zhang-2024-dlrl-maritime-usv (TVT.2024.3521393; DLRL = outer DDPG + inner Q-learning, PSO-G/PSO-DDQN/DQN baselines verbatim), zhang-2024-gdmtd3-aerial-secure-cb (TMC.2024.3502685; ASCEE-MOP + GDMTD3, four deployment policies + five DRL benchmarks grounded; "GDMDRL" appears verbatim in the parse conclusion), zhang-2024-uav-task-offloading-ddpg (JIOT.2024.3488210; UTOM = KKT + IPSO + DDPG verbatim), zhang-2025-gan-td3-isac-active-ris (JIOT.2025.3527441; GAN-TD3 better/stabler at higher complexity + slower convergence verbatim), zhang-2025-three-tier-maritime-offloading (TVT.2025.3526213; "saves 39.3% of system energy" verbatim, four-subproblem MINLP decomposition grounded), zhang-2025-vnf-sgin-dql (TVT.2024.3454438; <6% earth-surface coverage + VSCP/SR/DDVSC verbatim; dates→2025), zhao-2019-uav-emergency-disasters (MWC.2018.1800160; DOI in parse, venue/vol/pages web-confirmed note intact; AF/DF Nakagami-m + SOCP + SPR D2D grounded), zhao-2022-matd3-multiuav-ec-offloading (TWC.2022.3153316; cooperative MATD3 under CTDE, 2 ECs/30 UEs/400×400 m grounded), zhao-2024-caching-service-placement-uav (JSAC.2024.3460049; average-QoE = cache-hit + delay-shrinkage, Gibbs-sampling + matching-game, "especially when caching/computation limited" verbatim), zhao-2025-traj-offload-cache-migration (TMC.2024.3486995; throughput +10%–45% / scheduling cost −15%–30% / exec time −8%–37% all verbatim; Table I running-times 1000-user PA 3.72 / RSA 0.36 / K-B&B 18.85 / K-GA 9.34 / TSOUD-B&B 18.54 / TSOUD-GA 8.30 verbatim).

### Gates (batch 11)

- **`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits. **`index_audit.py`** = 515 catalogue-able, 0 unindexed / 0 duplicate primaries (45 cross-ref mentions informational). **`frontmatter_audit.py`** = 513 pages, 0 errors. The two corrected pages re-validated clean (no diagnostics); edits were prose-only (no new wikilinks) — graph unchanged at **513 nodes / 4455 edges**.

### Routing to `mec-wiki-synthesizer` (batch 11 — coverage gaps, recorded not filled)

- **Candidate findings — Zhao caching/migration anchors:** [[zhao-2024-caching-service-placement-uav]] (average-QoE = cache-hit + delay-shrinkage via Gibbs + matching) and [[zhao-2025-traj-offload-cache-migration]] (the corpus's clearest **computational task caching** + joint trajectory/offload/migration source, with concrete +10–45% / −15–30% / −8–37% results) are headline-rich sources with no finding page.
- **Candidate comparison — UAV task-migration cluster:** [[zhang-2025-mcma-task-migration]] (Informer-prediction + MAPPO/MADDPG two-stage), [[zhao-2025-traj-offload-cache-migration]] (Lyapunov + QCQP/SDR), and the vehicular/aerial migration sources already in the corpus could anchor a task-migration comparison page.
- **Candidate synthesis — safe-RL / collision-aware UAV control:** [[zhang-2025-ssac-mgi-heterogeneous-uav]]'s intervention-based safety layer (Standard + Safety agent) is a distinctive safe-RL pattern with no synthesis tie to the other multi-UAV trajectory-control sources.
- **Entity gaps (recurring authors, not created here):** **Geng Sun / Jiahui Li / Qingqing Wu / Dusit Niyato** anchor [[zhang-2024-gdmtd3-aerial-secure-cb]] (existing entities, rosters not re-tallied here). **Nan Zhao** is first author of both [[zhao-2019-uav-emergency-disasters]] and [[zhao-2022-matd3-multiuav-ec-offloading]] — two corpus sources, no entity page yet (namesake check vs other "Zhao" authors advised). **Chunxiao Jiang** (three-tier maritime) and **Qiang Ye** (VNF-SGIN; re-flagged from batches 6/9) recur across the aerial/space and maritime clusters.

### Correctness & consistency audit (Phase B — batch 12/12, final source batch)

Audited the **final source-page batch 12** (6 pages, alphabetical zheng-2024-recmop-uav-cb → zhu-2025-lycnn-drl-wpt-mec). Phase 0 re-reconciled clean (`curation_status.py --dupes`: **171 raw = 171 curated, 0 uncurated, 0 genuinely-new**); tree clean at `13cf2de`; baseline graph **513 nodes / 4455 edges**. With this batch **all 171 source pages are audited.**

- **Ungrounded-number + baseline fix — [[zhu-2025-lycnn-drl-wpt-mec]]** Findings claimed LyCNN-DRL beats classical MINLP solvers "by orders of magnitude (**sub-millisecond inference** vs seconds per iteration)" — **not in the parse**, which consistently reports execution latency of **~50 ms** (ten-WD) up to **137 ms (0.137 s)** at $N=40$, ≈two orders of magnitude / ~250× below LyCD's **35.184 s** (Table III + conclusion, verbatim). Rewrote to the grounded latency figures and the **97%-of-LyCD-utility** result. Also corrected the DRL-baseline claim: the page said it "beats prior DRL approaches (e.g. the OFDMA-based scheme)", but the OFDMA scheme (ref. [26]) is cited as motivating *prior work*, not benchmarked; the actual DRL baselines are **HA2C** (non-convergent for $N\ge10$) and **LyPG-DRL** (≈47.8% worse $\eta$ at $N=10$, non-convergent for $N\ge30$) — rewrote to these.
- **Evergreen-wording fix — [[zhu-2025-lycnn-drl-wpt-mec]]** cross-link note said "Future curated UAV+WPT papers will fold cleanly into this thread" (process-narration) → rewrote to an evergreen tie to the classical/convex WPT-MEC anchor [[zhou-2018-uav-wireless-powered-mec]] (same computation-rate problem solved without learning). Added the reciprocal `[[zhou-2018-uav-wireless-powered-mec]]` link to `related` (zhou-2018 already linked here — fixed the asymmetry); `updated`→2026-06-01.
- **Verified clean** (DOI/venue/year against own parse; headline numbers grounded verbatim or flagged figure-/abstract-derived indicative; frontmatter valid; slugs/tags/`related` consistent, no self-refs): zheng-2024-recmop-uav-cb (TWC.2024.3400523; ISCC-2022 precursor DOI 10.1109/ISCC55528.2022.9912883 grounded; RECMOP NP-hard/non-convex + IMOGSA with QBL/discrete-update/archive-optimization; results qualitative, Fig. 13 phase-error γ trend figure-derived), zheng-2024-semcom-sec-offloading (JSAC.2024.3365879; ICC-2022 DDINS Workshop precursor DOI 10.1109/ICCWorkshops53468.2022.9814494 grounded; PSFed saves **40.50%** communication + reduces privacy risk **51.43%** verbatim from conclusion+Fig.5/6; CTPS = Rubinstein bargaining + Lagrangian dual decomposition), zhou-2018-uav-wireless-powered-mec (JSAC.2018.2864426; "first work" on UAV-enabled WPT-MEC computation-rate maximization verbatim; partial two-stage + binary three-stage algorithms grounded), zhou-2024-jdl-abs-postdisaster-rescue (TWC.2024.3479709; JDL = Lyapunov + actor-critic with model-based SCA critic; 2.5 km circular-trajectory benchmark + SDQN baseline grounded; figure-read curves flagged indicative), zhu-2024-sensing-comm-doppler-uav-swarm (TVT.2023.3315868; sensing accuracy **>30%** + communication **>20%** verbatim from abstract+conclusion; DE-based min-max-CRLB solver grounded).

### Gates (batch 12)

- **`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits. **`index_audit.py`** = 515 catalogue-able, 0 unindexed / 0 duplicate primaries (45 cross-ref mentions informational). **`frontmatter_audit.py`** = 513 pages, 0 errors. The corrected [[zhu-2025-lycnn-drl-wpt-mec]] re-validated clean (no diagnostics); the added reciprocal link does not change graph cardinality (target already present) — graph **513 nodes / 4455 edges**.

### Routing to `mec-wiki-synthesizer` (batch 12 — coverage gaps, recorded not filled)

- **Candidate findings — headline-rich sources with no finding page:** [[zheng-2024-semcom-sec-offloading]] (PSFed saves 40.50% communication / 51.43% privacy risk — the corpus's semantic-communication-for-satellite-offloading anchor) and [[zhu-2024-sensing-comm-doppler-uav-swarm]] (>30% sensing / >20% communication via Doppler-aware DE co-design).
- **Candidate synthesis — WPT-MEC computation-rate thread:** [[zhou-2018-uav-wireless-powered-mec]] (classical/convex, "first work") and [[zhu-2025-lycnn-drl-wpt-mec]] (Lyapunov-guided CNN-DRL) bracket the same WPT-MEC computation-rate problem across the classical→DRL solver divide — a natural synthesis tie, also linking [[qin-2025-bcuav-masac]]'s Lyapunov template.
- **Candidate comparison — collaborative-beamforming MOP solvers:** [[zheng-2024-recmop-uav-cb]] is the only corpus CB source solved with the **gravitational search algorithm** (IMOGSA); it sits alongside [[liang-2024-hmecmop-uav-cb]] (multi-verse optimizer), [[li-2024-emssa-uav-swarm-vaa]] / [[sun-2024-imssa-uav-secure-cb]] (salp-swarm) — a CB-MOP-by-metaheuristic comparison remains owed.
- **Entity gaps (recurring authors, not created here):** **Guhan Zheng** (semcom-SEC) and **Xiaoya Zheng** (RECMOP-CB, Geng-Sun group) are distinct first-author "Zheng" namesakes — neither has an entity page; flag the namesake split if entity pages are minted. **Fuhui Zhou** (zhou-2018) recurs in the WPT-MEC line. The [[geng-sun]] / [[jiahui-li]] / [[shuang-liang]] CB cluster is reinforced by [[zheng-2024-recmop-uav-cb]] (existing entities, rosters not re-tallied here).

### Audit status after batch 12

**All 171 source pages audited (batches 1–12 complete).** Remaining unaudited: the **non-source layer** — concepts (234), entities (71), and the derived pages (findings/synthesis/comparisons/methodology/queries/thesis) beyond the handful already touched (the end-to-end-DRL cluster, [[drl-vs-evolutionary-vs-classical-solvers]], and the two LAE concept pages from batch 9). Subsequent invocations continue from `.curation-out/audit-coverage.md` against that non-source layer.

## 2026-06-01 — Cleanup: duplicate-ingest removal + end-to-end-DRL derived pages converted to English

Repository hygiene pass following the 6-batch curation run.

- **Removed two duplicate MinerU re-ingests.** Deleted the space-named raw folders `Optimizing Spectrum Sharing in UAV Swarms A Stackelberg Game-Based Incentive Mechanism` and `UAV-Enabled Multi-Source Data Fusion in Vehicular Networks A Joint Optimization Approach for Reliab` — duplicate parses (different UUIDs) of papers already curated under their underscore-named originals ([[wang-2025-uav-swarm-stackelberg]], [[xie-2026-uav-multisource-fusion]]). `curation_status.py --dupes` now reports **171 raw = 171 curated, 0 uncurated, 0 duplicates**. No source page referenced the removed folders; `wiki/references/**` still carries stale provenance to those folder names, to be refreshed on the next reference-scout pass.
- **Committed missing raw artifacts** for two already-curated sources ([[wang-2025-sac-tma-mec-dc]], [[wang-2021-maddpg-multiuav-trajectory]]) whose `raw/sources/` parses/PDFs/images had never been version-controlled.
- **Converted an end-to-end-DRL analytical cluster from Chinese to English** and grounded it in the corpus: concepts [[end-to-end-vs-decomposition-in-drl-mec]] and [[action-space-explosion-in-multi-uav-mec]], finding [[no-true-end-to-end-drl-in-corpus]] (grounded in [[drl-vs-evolutionary-vs-classical-solvers]]), and query [[end-to-end-drl-feasibility-large-scale-mec]]. Two accidental chat-save files (a prompt-titled query page and a non-paper "source" page) were removed; their substance is preserved in these four evergreen pages. Indexed in `index.md`; `overview.md` snapshot reconciled to concepts 234 / findings 14 / queries 5. `linkcheck.py` and `process_refs.py` both clean.

## 2026-06-01 — Curation pass (batch 6/6: 2 new sources + audit) — FINAL BATCH, run complete

Sixth and **final** batch of the deliberately-split **6-batch** curation run over the **37 genuinely-new** raw papers. This run curated **only** the 2 assigned batch-6 folders from `.curation-out/batches.json` (`UAV-Enabled_Collaborative_Beamforming_via_Multi-Agent_Deep_Reinforcement_Learning`, `UAV-Enabled_Wireless_Power_Transfer_Trajectory_Design_and_Energy_Optimization`). Corpus grows **169 → 171 curated sources**. State reconciled clean at `05e61c6` (batch 5) before starting; `curation_status.py --dupes` re-confirmed **2 genuinely-new** remaining (the two space-named re-ingests stay correctly flagged as duplicates and were not touched). Confirmed neither paper already had a source page before writing. The stale `.curation-out/batch4-meta.md` artifact was ignored — `batches.json` is authoritative. **After this batch, `curation_status.py --dupes` reports zero genuinely-new uncurated papers — the 6-batch run is complete.**

### New source pages (2)

- [[liu-2024-hatrpo-ucb-cb]] — Saichao Liu, Geng Sun, Jiahui Li, Shuang Liang, Qingqing Wu, Pengfei Wang, Dusit Niyato 2024 (**IEEE TMC**, `10.1109/TMC.2024.3419915`). UAV **collaborative beamforming** (UVAA → remote BSs); multi-objective **UCBMOP** (max transmission rate / min UAV energy) over UAV positions + excitation-current weights, scalarized into a single weighted reward; cast as a Markov game (single-slot episodes) and solved by **HATRPO-UCB** — heterogeneous-agent trust-region MADRL with observation enhancement + agent-specific global state + Beta-distribution policy. Convergence ~750 epochs (vs ~1,400 for MADDPG/IPPO/MAPPO) stated verbatim; Table III energy/rate numbers reported (e.g. first-BS ~13,401 J at ~1.029×10⁶ bps); per-method final-reward magnitudes + phase-error robustness figure-derived (and the convergence figure's extracted table is not fully consistent with the text on final reward — flagged on the page). pub 27 Jun 2024 / current version 5 Nov 2024 → 2024.
- [[xu-2018-uav-wpt-trajectory]] — Jie Xu, Yong Zeng, Rui Zhang 2018 (**IEEE TWC**, `10.1109/TWC.2018.2838134`). Foundational **UAV-enabled WPT** trajectory design: one UAV-mounted ET charges K≥2 ground ERs over a finite period under a max-speed constraint. **Sum-energy** optimum = provably **single-location hovering** (induces near-far fairness gap; closed-form for K=2 with the 2H/√3 = 5.77 m threshold). **Min-energy (max-min)** optimum, speed ignored, = **multi-location hovering** via Lagrange dual; with speed constraint, a **successive hover-and-fly** trajectory (optimal for K=2, asymptotically optimal for K>2) + an **SCP** refinement. Sim setup verbatim (β₀=−30 dB, H=5 m, P=40 dBm); per-ER power magnitudes figure-derived. pub 25 May 2018 / current version 10 Aug 2018 → 2018. GLOBECOM-2017 / APCC-2017 workshop earlier versions noted.

### New concept stubs (2)

- [[trust-region-policy-optimization]] — KL-trust-region policy-gradient with monotonic-improvement guarantee (TRPO) + its sequential-update multi-agent extension (HATRPO); anchors [[liu-2024-hatrpo-ucb-cb]], cross-linked to the [[ppo]]/[[mappo]]/[[heterogeneous-agent-rl]] family.
- [[successive-hover-and-fly-trajectory]] — hover-at-optimal-locations + fly-at-max-speed-between-them UAV trajectory primitive; anchors [[xu-2018-uav-wpt-trajectory]], cross-linked to [[uav-trajectory-control]] / [[wireless-power-transfer]] / SCP ([[alternating-optimization-sdr-sca]]).

All other referenced concepts reused existing slugs (e.g. [[collaborative-beamforming]], [[heterogeneous-agent-rl]], [[beta-policy-drl]], [[stochastic-game]], [[centralized-training-decentralized-execution]], [[rotary-wing-propulsion-energy-model]], [[air-to-ground-channel-model]], [[mappo]], [[maddpg]], [[wireless-power-transfer]], [[rf-energy-harvesting]], [[uav-trajectory-control]], [[fairness-metrics-in-mec]]).

### Entities — 0 new + 6 roster updates

- **Roster updates (HATRPO-UCB):** [[geng-sun]] (15→16), [[jiahui-li]] (12→13), [[shuang-liang]] (6→7), [[qingqing-wu]] (9→10, SJTU-email-matched), [[dusit-niyato]] (19→20) — all +[[liu-2024-hatrpo-ucb-cb]].
- **Roster update (UAV-WPT):** [[yong-zeng]] (5→6) +[[xu-2018-uav-wpt-trajectory]] (NUS; co-author with Jie Xu and Rui Zhang).
- **Deferred / not created** (single corpus source / identity not confirmable from parse, correctness over completeness): Saichao Liu (Jilin University), Pengfei Wang (Dalian University of Technology — already a deferred co-author of [[wang-2024-hfrl-decentralized-navigation]] and the LAE survey), Rui Zhang (NUS). **Jie Xu** (first author of [[xu-2018-uav-wpt-trajectory]]) is at **Guangdong University of Technology** — explicitly **distinct** from the existing [[jie-xu]] entity (CUHK-Shenzhen, ISAC Fellow); treated as a separate identity, **no entity link embedded** for this Jie Xu (flagged on the source page). No author-entity links embedded in source-page bodies beyond the confirmed roster set (house convention).

### Duplicate / near-duplicate check

- No same-paper/different-UUID duplicate ingests among the 2 batch-6 folders.
- [[liu-2024-hatrpo-ucb-cb]] (UCBMOP, rate-vs-energy, **HATRPO-UCB trust-region MADRL**) is **distinct** from the other [[geng-sun]]-group CB sources: [[zheng-2024-recmop-uav-cb]] (RECMOP, gravitational search), [[liang-2024-hmecmop-uav-cb]] (multiverse optimizer), [[sun-2025-emoppo-vlh-aerial-cb]] (evolutionary MORL), [[zhang-2024-gdmtd3-aerial-secure-cb]] (diffusion-TD3) — different solver family + objective set — cross-linked via [[collaborative-beamforming-in-aerial-mec]], not duplicated.
- [[xu-2018-uav-wpt-trajectory]] (UAV-WPT energy-delivery trajectory, **no compute/offloading layer**) is **distinct** from the WPT-MEC sources [[zhou-2018-uav-wireless-powered-mec]] (computation-rate max) and [[liu-2020-wpt-cooperative-uav-mec]] (idle-SD cooperative WPT-MEC, SCA/DAI) — it is the WPT-only precursor — cross-linked, not duplicated.

### Audit

- **DOI/venue/year** verified verbatim against each parse: TMC `10.1109/TMC.2024.3419915` (Digital Object Identifier line + supplementary-material DOI both present; dates of publication 27 Jun 2024 / current version 5 Nov 2024 → 2024); TWC `10.1109/TWC.2018.2838134` (Digital Object Identifier line present; dates of publication 25 May 2018 / current version 10 Aug 2018 → 2018). No web lookups needed — both parses carry full metadata.
- **Headline numbers grounded**: HATRPO-UCB ~750-epoch convergence and Table III energy/rate values quoted from the parse text/table; per-method final reward + phase-error curves flagged indicative (figure-derived), with the convergence figure/text inconsistency on final reward noted on the page. UAV-WPT 5.77 m threshold and sim parameters quoted verbatim; per-ER power magnitudes flagged figure-derived.
- **Counts** reconciled: committed corpus is sources 171, concepts 232, entities 71 (no new entity). `corpus_counts.py` reports higher on-disk counts because unrelated untracked pages from a separate in-progress effort sit in the working tree; those are **not** part of this batch and were not staged. `overview.md` snapshot + CB/energy track rows + simulation-only "3 of 171" updated to the committed corpus. `index.md` updated (CB + Energy/WPT source rows; DRL-backbones + UAV-control concept lists).
- **`linkcheck.py`**: no NEW dangling links introduced by this batch (see run result below).
- **`process_refs.py`**: clean — no batch/pass process-narration leaked into any page except this log.

## 2026-06-01 — Curation pass (batch 5/6: 7 new sources + audit)

Fifth batch of the deliberately-split **6-batch** curation run over the **37 genuinely-new** raw papers (split to keep context clean and avoid misinformation). This run curated **only** the 7 assigned batch-5 folders from `.curation-out/batches.json`; the other uncurated folders are owned by separate batch runs and were left untouched. Corpus grows **162 → 169 curated sources**. (Confirmed none of the 7 already had a source page before writing.) State reconciled clean at `42c0c25` (batch 4) before starting; `curation_status.py --dupes` re-confirmed **9 genuinely-new** remaining (the two space-named re-ingests stay correctly flagged as duplicates and were not touched), leaving **batch 6 = 2 papers** after this run. The stale `.curation-out/batch4-meta.md` artifact was ignored — `batches.json` is authoritative.

### New source pages (7)

- [[zheng-2024-recmop-uav-cb]] — Xiaoya Zheng, Geng Sun, Jiahui Li, Shuang Liang, Qingqing Wu, Minghao Yin, Dusit Niyato, Victor C. M. Leung 2024 (**IEEE TWC**, `10.1109/TWC.2024.3400523`). UAV **collaborative beamforming** (UVAA relay → remote BSs) in emergency comms; multi-objective **RECMOP** (max-min BS SNR / min-max average AU SNR / min propulsion energy) over UAV locations + excitation-current weights; NP-hard non-convex mixed-variable; solved by **improved multi-objective gravitational search algorithm (IMOGSA)** (QBL + discrete-update + NSGA-II archive). "Outperforms benchmarks at both scales" + robustness under phase-error stated; magnitudes figure-derived. pub 21 May 2024 / current version 11 Oct 2024 → 2024. ISCC-2022 earlier version noted.
- [[mahboob-2024-ai-ntn-survey]] — Shadab Mahboob, Lingjia Liu 2024 (**IEEE COMST**, `10.1109/COMST.2023.3347145`). **Survey** of AI-empowered satellite-based NTN for 6G; NTN/AI background + AI-per-challenge research-thrust taxonomy (channel/Doppler estimation, beam/resource management, handover, spectrum sharing, routing, slicing, offloading, security) + distributed-learning paradigms (FL / decentralized / split) + O-RAN/RIC/SDR implementation. No original numbers (survey). pub 19 Jan 2024 / current version 23 May 2024 → 2024.
- [[zheng-2024-semcom-sec-offloading]] — Guhan Zheng, Qiang Ni, Keivan Navaie, Haris Pervaiz 2024 (**IEEE JSAC**, `10.1109/JSAC.2024.3365879`). **Semantic communication** in a LEO **satellite-borne edge cloud** (SemCom-SEC) for offloading; coders on TSTs + satellites; **PSFed** (adaptive pruning-split federated learning, coder components intact) for in-maintenance coder updating; **CTPS** (Rubinstein bargaining game → complete-info MINLP → Lagrangian dual decomposition) for in-service delay/energy under privacy + fairness. Verbatim: PSFed **saves 40.50% communication** + **reduces privacy risk 51.43%**, accuracy/convergence ~unchanged. pub 26 Feb 2024 / current version 9 May 2024 → 2024. ICC-2022 DDINS earlier version noted.
- [[zeng-2016-throughput-relaying]] — Yong Zeng, Rui Zhang, Teng Joon Lim 2016 (**IEEE TCOMM**, `10.1109/TCOMM.2016.2611512`). Foundational **UAV mobile-relaying** throughput maximization over relay trajectory + source/relay power under mobility + **information-causality** constraints; optimal power = **"staircase" water-filling** (non-increasing source / non-decreasing relay level); trajectory via SCA; closed-form free-endpoint solution (unidirectional max-speed or stationary). "Significant throughput gain vs static relaying" stated; curves figure-derived. pub 20 Sep 2016 / current version 15 Dec 2016 → 2016.
- [[zhao-2019-uav-emergency-disasters]] — Nan Zhao, Weidang Lu, Min Sheng, Yunfei Chen, Jie Tang, F. Richard Yu, Kai-Kit Wong 2019 (`10.1109/MWC.2018.1800160`). Magazine **framework** for UAV-assisted emergency networks in disasters: (1) joint trajectory + scheduling with surviving BSs; (2) SOCP transceiver + multihop **D2D** (SPR, PPP outage) coverage extension; (3) multihop UAV relaying (AF/DF, Nakagami-m) connecting disaster area to outside; NOMA discussion for single-antenna UAVs. **Metadata caveat:** parse carries the **DOI only** — year/venue/volume/pages = `not in parse`, **web-confirmed via dblp** (IEEE Wireless Communications, vol. 26, no. 1, pp. 45–51, 2019) and flagged on the page.
- [[dai-2023-hybrid-noma-fdma-marine]] — Minghui Dai, Yuan Wu, Liping Qian, Zhou Su, Bin Lin, Nan Chen 2023 (**IEEE TNSE**, `10.1109/TNSE.2022.3205303`). Two-segment **marine multi-access offloading**: USNs upload to USV via **NOMA** (underwater acoustic), USV offloads to hovering **UAVs** via **FDMA** (RF), with an eavesdropper; minimize **total USN+USV energy** over USN uploading time + USV offloading decision/time + **secrecy provisioning**; layered top/sub-problem + 2-D line search. Validated vs **LINGO** global optimum (gap stated qualitatively → figure-derived). pub 9 Sep 2022 / current version 6 Jan 2023 → 2023.
- [[hu-2019-uav-relay-edge-computing]] — Xiaoyan Hu, Kai-Kit Wong, Kun Yang, Zhongbin Zheng 2019 (**IEEE TWC**, `10.1109/TWC.2019.2928539`). First UAV-MEC where one cellular-connected UAV is an **MEC server AND a relay** to the AP simultaneously; minimize **weighted-sum energy** of UAV + UEs over computation scheduling + bandwidth allocation + trajectory under **information-causality**; alternating optimization (closed-form Lagrange-dual scheduling/bandwidth + SCA trajectory), guaranteed convergence. "Significant + more stable gains vs preset-traj/offload-only/equal-BW/local" stated; magnitudes figure-derived. pub 19 Jul 2019 / current version 9 Oct 2019 → 2019.

### New concept stubs (3)

- [[gravitational-search-algorithm]] — gravity-law population metaheuristic; anchors [[zheng-2024-recmop-uav-cb]]'s IMOGSA; cross-linked from the corpus's other mixed-variable aerial-MOP metaheuristics ([[multi-verse-optimizer]], [[salp-swarm-algorithm]], [[whale-optimization-algorithm]]).
- [[uav-mobile-relaying]] — UAV-borne high-mobility relay with trajectory as a design variable; anchors [[zeng-2016-throughput-relaying]], reused by [[hu-2019-uav-relay-edge-computing]] and [[zhao-2019-uav-emergency-disasters]].
- [[information-causality-constraint]] — forward-only-received-data buffering constraint; the information-domain analogue of energy-causality; anchors [[zeng-2016-throughput-relaying]] (staircase water-filling) and [[hu-2019-uav-relay-edge-computing]].

All other referenced concepts reused existing slugs (e.g. [[collaborative-beamforming]], [[multi-objective-reinforcement-learning]], [[rotary-wing-propulsion-energy-model]], [[mixed-integer-nonlinear-programming]], [[uav-data-collection]], [[uav-trajectory-control]], [[alternating-optimization-sdr-sca]], [[energy-latency-tradeoff]], [[non-terrestrial-network]], [[space-air-ground-integrated-network]], [[leo-satellite-edge-computing]], [[seamless-handover]], [[federated-learning]], [[decentralized-federated-learning]], [[network-slicing]], [[task-offloading]], [[semantic-communication]], [[bargaining-game]], [[privacy-sensitive-data-partitioning]], [[dnn-model-partition]], [[mobile-edge-computing]], [[maritime-mec]], [[noma]], [[two-stage-decomposition]], [[physical-layer-security]], [[multi-uav-assisted-mec]], [[post-disaster-mec]], [[air-to-ground-channel-model]]).

### Entities — 1 new + 9 roster updates

- **New:** [[yong-zeng]] — NUS UAV-communications/trajectory-optimization anchor; now at **5** sources ([[zeng-2016-throughput-relaying]] + the already-curated [[zeng-2017-energy-efficient-uav-trajectory]], [[zeng-2019-rotary-wing-energy-min]], [[zeng-2019-uav-comm-tutorial-5g]], [[wu-2018-multiuav-minrate-trajectory]]) → single identity (NUS), created rather than deferred.
- **Roster updates (RECMOP):** [[geng-sun]] (14→15), [[jiahui-li]] (11→12), [[shuang-liang]] (5→6), [[qingqing-wu]] (8→9, SJTU-email-matched), [[victor-c-m-leung]] (5→6), [[dusit-niyato]] (18→19) — all +[[zheng-2024-recmop-uav-cb]].
- **Roster updates (marine NOMA/FDMA):** [[minghui-dai]] (3→4), [[yuan-wu]] (9→10), [[liping-qian]] (3→4), [[zhou-su]] (2→3), [[bin-lin]] (8→9) — all +[[dai-2023-hybrid-noma-fdma-marine]].
- **Deferred / not created** (single corpus source each / identity not confirmable from parse, correctness over completeness): Xiaoya Zheng, Minghao Yin (Northeast Normal Univ.; 2 sources but minted via cluster leads); Rui Zhang + Teng Joon Lim (NUS); Shadab Mahboob + Lingjia Liu (Virginia Tech); Guhan Zheng + Qiang Ni + Keivan Navaie (Lancaster) + Haris Pervaiz (Essex); Xiaoyan Hu (UCL) + Kai-Kit Wong + Kun Yang + Zhongbin Zheng; Nan Zhao + Weidang Lu + Min Sheng + Yunfei Chen + Jie Tang + F. Richard Yu; Nan Chen (Tennessee Tech). No author-entity links embedded in source-page bodies (house convention).

### Duplicate / near-duplicate check

- No same-paper/different-UUID duplicate ingests among the 7 batch-5 folders.
- [[dai-2023-hybrid-noma-fdma-marine]] (**IEEE TNSE**, **total-energy minimization + secrecy provisioning**, NOMA-underwater (USN→USV) + FDMA-aerial (USV→UAV)) is **distinct** from the existing same-lead-author [[dai-2023-hybrid-marine-mmwl]] (**IEEE TCOMM**, **max-workloads-latency MMWL**, FDMA-offshore + NOMA-aerial) — different venue, objective, and access-mode assignment — cross-linked, not duplicated.
- [[hu-2019-uav-relay-edge-computing]] (first author **Xiaoyan Hu**, UCL; UAV as MEC-server + relay, weighted-sum-energy, info-causality + SCA) is **distinct** from the existing [[hu-2019-pdd-uav-mec-offloading]] (first author **Qiyu Hu**, Zhejiang University; single-UAV min-max-delay, penalty-dual-decomposition) — different author + objective + method — cross-linked, not duplicated.
- [[zheng-2024-recmop-uav-cb]] (RECMOP, AU-interference objective, IMOGSA gravitational search) is **distinct** from the other [[geng-sun]]-group CB sources [[liang-2024-hmecmop-uav-cb]] (hovering-vs-motion energy, multiverse optimizer), [[li-2024-emssa-uav-swarm-vaa]]/[[sun-2024-imssa-uav-secure-cb]] (salp-swarm) — different objective set + solver — cross-linked, not duplicated.
- [[zheng-2024-semcom-sec-offloading]] (Guhan Zheng; SemCom + satellite-borne edge cloud + PSFed + bargaining) is **distinct** from [[zheng-2024-recmop-uav-cb]] (Xiaoya Zheng; CB) despite the shared romanized surname — different author/affiliation/topic — and from the satellite-offloading sources [[cheng-2025-dos-satellite-edge-computing]] / [[wang-2025-double-edge-samin]] — cross-linked, not duplicated.
- [[zeng-2016-throughput-relaying]] is the method-ancestor of [[hu-2019-uav-relay-edge-computing]] (shared info-causality + SCA), and a communications-framing sibling of [[zeng-2017-energy-efficient-uav-trajectory]] / [[wu-2018-multiuav-minrate-trajectory]] — not duplicates.
- [[zhao-2019-uav-emergency-disasters]] (magazine emergency-network framework) is **distinct** from the optimization-heavy post-disaster sources [[zhou-2024-jdl-abs-postdisaster-rescue]] / [[raivi-2024-jdaco-postdisaster-iot]] — cross-linked, not duplicated.
- [[mahboob-2024-ai-ntn-survey]] is a high-level AI-NTN survey, complementary to (not duplicative of) the application-specific NTN sources.

### Audit (correctness-first)

- **DOI / venue / year** — 6 of 7 papers carry an explicit `Digital Object Identifier` line, **verified verbatim** against the parse (TWC `10.1109/TWC.2024.3400523`; COMST `10.1109/COMST.2023.3347145`; JSAC `10.1109/JSAC.2024.3365879`; TCOMM `10.1109/TCOMM.2016.2611512`; TNSE `10.1109/TNSE.2022.3205303`; TWC `10.1109/TWC.2019.2928539`); years follow date-of-current-version (both dates recorded). **[[zhao-2019-uav-emergency-disasters]]** is the only partial-metadata case — the parse has the **DOI** (`10.1109/MWC.2018.1800160`) but no publication date/venue/volume; year/venue/volume/pages **web-confirmed via dblp** (IEEE Wireless Communications, 26(1):45–51, 2019) and explicitly flagged on the page.
- **Grounded headline claims only:** SemCom-SEC −40.50% comm / −51.43% privacy risk (conclusion, verbatim); all RECMOP / relaying / marine / Hu-relay-edge comparative magnitudes stated qualitatively as the papers state them, with figure-derived numbers flagged indicative; the survey carries no original numbers.
- **Wikilink integrity:** `linkcheck.py` = **NO DANGLING LINKS** (Obsidian-faithful). All new wikilinks target existing slugs or pages created in this batch (7 sources + 3 concepts + 1 entity).
- **Process-narration:** `process_refs.py` = **0 files / 0 hits** outside `log.md`; sources / concepts / entities / index / overview kept evergreen.
- **Frontmatter:** `type`/`title`/`authors`/`year`/`url`/`venue`/`tags`/`related`/dates/H1 validated (no diagnostics) on all 7 source pages; `type`/`title`/`tags`/dates/H1 on the 3 new concepts + 1 new entity + index/overview.
- **Counts reconciled** (`corpus_counts.py`): **169 sources / 230 concepts / 70 author entities (+[[pytorch]] = 71 entity pages)**, 13 findings / 11 synthesis / 4 comparisons / 2 methodology / 4 queries / 1 thesis / 2 references. `index.md` and `overview.md` updated to agree.
- **LLM Wiki API:** not queried this batch (headless shell); not required for correctness.
- **Raw-folder scope:** only the 7 assigned batch-5 folders were curated; **1 batch (2 papers) remains** for a separate invocation (batch6).

## 2026-06-01 — Curation pass (batch 4/6: 7 new sources + audit)

Fourth batch of the deliberately-split **6-batch** curation run over the **37 genuinely-new** raw papers (split to keep context clean and avoid misinformation). This run curated **only** the 7 assigned batch-4 folders from `.curation-out/batches.json`; the other uncurated folders are owned by separate batch runs and were left untouched. Corpus grows **155 → 162 curated sources**. (Confirmed none of the 7 already had a source page before writing.) State reconciled clean at `0b849b2` (batch 3) before starting; `curation_status.py --dupes` re-confirmed **16 genuinely-new** remaining (the two space-named re-ingests stay correctly flagged as duplicates and were not touched). The stale `.curation-out/batch4-meta.md` artifact (a 43-folder list from an earlier planning session) does **not** match the current `batches.json` batch-4 allowlist and was ignored — `batches.json` is authoritative.

### New source pages (7)

- [[jeong-2018-uav-cloudlet-bit-allocation]] — Seongah Jeong, Osvaldo Simeone, Joonhyuk Kang 2018 (**IEEE TVT**, `10.1109/TVT.2017.2706308`). Early **UAV-mounted cloudlet** MEC; minimize total mobile energy under latency + UAV-energy budget by jointly optimizing **bit allocation** (uplink / cloudlet-compute / downlink) + UAV trajectory; FDD with orthogonal access or **NOMA**; two flying-energy models (velocity-only / +acceleration); non-convex solved by **SCA** (converges to local optimum). Headline energy-savings-vs-local/partial stated qualitatively (magnitudes are figure-derived). pub 19 May 2017 / current version 15 Mar 2018 → 2018.
- [[mozaffari-2017-uav-iot-energy-efficient]] — Mohammad Mozaffari, Walid Saad, Mehdi Bennis, Mérouane Debbah 2017 (**IEEE TWC**, `10.1109/TWC.2017.2751045`). Energy-efficient uplink **IoT data collection** via multiple mobile UAVs; joint 3D placement + device-UAV association + uplink power control (iterative decomposition) + closed-form **update-times** + energy-minimizing 3D trajectory; Beta-distribution (bursty) + periodic activation models; constrained K-means channel assignment. Abstract (verbatim): **−45%** device total transmit power and up to **+28%** reliability vs stationary ABS; update-vs-mobility-vs-power tradeoff. pub 15 Sep 2017 / current version 9 Nov 2017 → 2017.
- [[liang-2024-hmecmop-uav-cb]] — Shuang Liang, Minghao Yin, Geng Sun, Jiahui Li 2024 (**IEEE IoT-J**, `10.1109/JIOT.2023.3315708`). UAV-swarm **collaborative beamforming** (virtual antenna array) to remote BSs; **HMECMOP** simultaneously minimizes total hovering + motion energy over UAV positions + excitation-current weights + BS-communication order; proven NP-hard hybrid (continuous+discrete) MOP; solved by **improved multiobjective multiverse optimizer (IMOMVO)** (vertical-horizontal renewal + nearest-neighbor procedure). Comparative gains qualitative (figure-derived). pub 15 Sep 2023 / current version 6 Feb 2024 → 2024.
- [[mao-2024-fso-leo-hierarchical-routing]] — Bomin Mao, Xueming Zhou, Jiajia Liu, Nei Kato 2024 (**IEEE JSAC**, `10.1109/JSAC.2024.3365880`). Hierarchical **routing** for ultra-dense **free-space-optical (FSO) LEO** constellations; dual-layer MEO/LEO architecture + region division (MEO controllers compute paths, LEO forwards) + multi-objective DRL utility routing for differentiated QoS (latency / packet-loss / throughput) + reward-monotonicity **cooperative mechanism**; **adaptive to APT-terminal count** (hence FSO-link count). Networking/routing, not offloading. "Outperforms benchmarks across QoS metrics" stated qualitatively (magnitudes figure-derived). pub 19 Feb 2024 / current version 9 May 2024 → 2024.
- [[sun-2024-ues-video-analytics-disaster]] — Hui Sun, Xiuye Zhang, Bo Zhang, Kewei Sha, Weisong Shi 2024 (**IEEE TVT**, `10.1109/TVT.2023.3344281`). **Battery-aware** UAV-mounted-edge-server (UES) collaborative **video analytics** for **disaster rescue**; variable-length time slots (fly-then-hover); nested optimizations — **differential-evolution** per-slot offloading (0–1 decision + channel/resource allocation) + **DDQN** trajectory planning (MDP) — targeting the smart-camera-network **lifetime**. Headline: **doubles** the system lifetime; offloading "high accuracy / fast convergence vs 4 SOTA" (stated; curves figure-derived). pub 19 Dec 2023 / current version 16 May 2024 → 2024.
- [[mao-2025-irs-noma-fl-secrecy]] — Bomin Mao, Yingying Wu, Jiajia Liu, Hongzhi Guo, Jiadai Wang, Nei Kato 2025 (**IEEE TCCN**, `10.1109/TCCN.2024.3454256`). **IRS-assisted** physical-layer security for the **NOMA-based federated-learning** model-uploading phase; secrecy rate = device→BS minus device→Eve rate; **max-min secrecy-rate** over device transmit power + IRS phase shift under a power budget; non-convex coupled problem solved with **DDPG** (actor-critic + target nets + replay). "IRS improves secrecy rate" stated qualitatively (magnitudes figure-derived). pub 4 Sep 2024 / current version 9 Apr 2025 → 2025.
- [[schulman-2017-ppo]] — John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, Oleg Klimov 2017 (OpenAI). **Origin paper for PPO**; **clipped surrogate objective** ($\epsilon{=}0.2$) enabling multi-epoch first-order minibatch updates with TRPO-like stability; adaptive-KL variant included as a (worse) baseline; combined CLIP+VF+S loss; truncated-GAE actor-critic algorithm. Results: clipping-$\epsilon$=0.2 best (0.82 norm. score, Table 1); beats TRPO/A2C/CEM/vanilla-PG on MuJoCo (Fig. 3, figure-derived); Atari wins per Table 2. **Metadata caveat:** the parse carries **no DOI / venue / date** line — DOI/venue = `not in parse`; arXiv:1707.06347 (2017) **web-confirmed** and flagged as such on the page. Grounds the [[ppo]] concept like [[fujimoto-2018-td3-actor-critic]] grounds TD3.

### New concept stubs (1)

- [[free-space-optical-isl]] — laser inter-satellite link (high bandwidth, but APT-terminal- and visibility-limited and dynamic); anchors [[mao-2024-fso-leo-hierarchical-routing]] and backlinked from [[leo-satellite-edge-computing]].

All other referenced concepts reused existing slugs (e.g. [[ppo]], [[gae]], [[j-ppo]], [[mappo]], [[mobile-edge-computing]], [[uav-trajectory-control]], [[alternating-optimization-sdr-sca]], [[noma]], [[energy-latency-tradeoff]], [[rotary-wing-propulsion-energy-model]], [[fixed-wing-propulsion-energy-model]], [[drone-cell-3d-placement]], [[air-to-ground-channel-model]], [[uav-data-collection]], [[weighted-kmeans-uav-deployment]], [[collaborative-beamforming]], [[multi-verse-optimizer]], [[salp-swarm-algorithm]], [[mixed-integer-nonlinear-programming]], [[leo-satellite-edge-computing]], [[non-terrestrial-network]], [[walker-star-constellation]], [[multi-objective-reinforcement-learning]], [[dynamic-qos-constraints]], [[post-disaster-mec]], [[video-analytics-offloading]], [[ddqn]], [[differential-evolution]], [[task-offloading]], [[federated-learning]], [[intelligent-reflecting-surface]], [[physical-layer-security]], [[ddpg]]).

### Entities — 2 new + 6 roster updates

- **New:** [[mohammad-mozaffari]] + [[walid-saad]] — the Virginia Tech (Wireless@VT) UAV-communications cluster; each anchors **2** sources ([[mozaffari-2017-uav-iot-energy-efficient]] + the already-curated tutorial [[mozaffari-2019-uav-wireless-tutorial]]), affiliation-verified (identical Virginia Tech / Wireless@VT and email across both parses; Mozaffari-Saad-Bennis-Debbah roster stable) → single identity, created rather than deferred. The tutorial source was bumped to backlink both entities + the 2017 IoT paper.
- **Roster updates:** [[geng-sun]] (13→14), [[jiahui-li]] (10→11), [[shuang-liang]] (4→5, now lead author of the CB energy-MOP) — all +[[liang-2024-hmecmop-uav-cb]]; [[bomin-mao]] (2→4, +FSO routing +IRS-FL-secrecy), [[jiajia-liu]] (3→5), [[nei-kato]] (2→4) — +both new Mao papers; [[hongzhi-guo]] (3→4) + [[jiadai-wang]] (2→3) — +[[mao-2025-irs-noma-fl-secrecy]].
- **Deferred / not created** (single corpus source each / identity not confirmable from parse, correctness over completeness): Seongah Jeong + Osvaldo Simeone + Joonhyuk Kang (Harvard / King's College London / KAIST); Mehdi Bennis + Mérouane Debbah (Oulu / Huawei-CentraleSupélec — co-authors on the two Mozaffari papers but not minted this batch as their wiki-presence is via the cluster leads); Minghao Yin (Northeast Normal Univ.); Xueming Zhou (NWPU); Hui Sun + Xiuye Zhang + Bo Zhang + Kewei Sha + Weisong Shi (Anhui Univ. / Univ. of Houston-Clear Lake / Wayne State); Yingying Wu (NWPU); John Schulman + Filip Wolski + Prafulla Dhariwal + Alec Radford + Oleg Klimov (OpenAI). No author-entity links embedded in source-page bodies (house convention).

### Duplicate / near-duplicate check

- No same-paper/different-UUID duplicate ingests among the 7 batch-4 folders.
- [[jeong-2018-uav-cloudlet-bit-allocation]] (UAV *moving cloudlet*, bit-allocation+trajectory, SCA) is **distinct** from the other classical/convex UAV-MEC sources [[zhang-2019-uav-iot-comp-comm]] and the trajectory-optimization line — cross-linked, not duplicated. It is also a *compute-offloading* paper, unlike the *placement/relay/coverage* role surveyed in [[mozaffari-2019-uav-wireless-tutorial]].
- [[mozaffari-2017-uav-iot-energy-efficient]] (3D placement + mobility + uplink-power for IoT collection) is **distinct** from the same-group tutorial [[mozaffari-2019-uav-wireless-tutorial]] and from [[bor-yaliniz-2016-3d-abs-placement]] (coverage-max placement) — same air-to-ground channel family, different objective — cross-linked, not duplicated.
- [[liang-2024-hmecmop-uav-cb]] (hovering-vs-motion-energy MOP, multiverse optimizer) is **distinct** from the other CB sources [[li-2024-emssa-uav-swarm-vaa]] (salp-swarm, time/eavesdropper/energy) and [[sun-2025-emoppo-vlh-aerial-cb]] (evolutionary multi-objective PPO) — different objective + optimizer — cross-linked, not duplicated.
- [[mao-2024-fso-leo-hierarchical-routing]] (LEO routing, networking) is **distinct** from [[mao-2024-ntn-hierarchical-caching-cav]] (NTN caching) and [[lee-2024-dho-leo-handover]] (handover protocol) — same NWPU group / overlapping authors, different problem — cross-linked, not duplicated.
- [[sun-2024-ues-video-analytics-disaster]] (battery-aware video-analytics, DE+DDQN) is **distinct** from [[bao-2025-ddpg-video-offloading]] (UAV+HAP video offload, transcoding, DDPG) and the post-disaster sources — cross-linked, not duplicated.
- [[mao-2025-irs-noma-fl-secrecy]] (IRS PLS for FL aggregation, DDPG) is **distinct** from [[mao-2025-bcsa-frl]] (blockchain-secured FRL) and the ISAC-PLS sources — cross-linked, not duplicated.
- [[schulman-2017-ppo]] is the **method-ancestor** PPO paper, complementary to [[fujimoto-2018-td3-actor-critic]] (TD3) — both foundational-DRL-method anchors, not duplicates.

### Audit (correctness-first)

- **DOI / venue / year** — the 6 IEEE papers each carry an explicit `Digital Object Identifier` line, **verified verbatim** against the parse (TVT `10.1109/TVT.2017.2706308`; TWC `10.1109/TWC.2017.2751045`; IoT-J `10.1109/JIOT.2023.3315708`; JSAC `10.1109/JSAC.2024.3365880`; TVT `10.1109/TVT.2023.3344281`; TCCN `10.1109/TCCN.2024.3454256`); years follow date-of-current-version (both dates recorded in each citation). **[[schulman-2017-ppo]]** is the only `not in parse` metadata case — no DOI/venue/date in the parse; arXiv:1707.06347 (2017) web-confirmed and explicitly flagged on the page.
- **Grounded headline claims only:** Mozaffari-2017 −45% tx-power / +28% reliability (abstract verbatim); PPO clipping-0.2 = 0.82 (Table 1), Atari wins (Table 2), MuJoCo superiority (Fig. 3, flagged figure-derived); Sun-2024 "doubles lifetime" (abstract); Jeong/Liang/Mao-FSO/Mao-secrecy comparative magnitudes stated qualitatively as the papers state them, with figure-derived numbers flagged indicative.
- **Wikilink integrity:** `linkcheck.py` = **NO DANGLING LINKS** (Obsidian-faithful). All new wikilinks target existing slugs or pages created in this batch (7 sources + 1 concept + 2 entities).
- **Process-narration:** `process_refs.py` = **0 files / 0 hits** outside `log.md`; sources / concepts / entities / index / overview kept evergreen.
- **Frontmatter:** `type`/`title`/`authors`/`year`/`url`/`venue`/`tags`/`related`/dates/H1 validated (no diagnostics) on all 7 source pages; `type`/`title`/`tags`/dates/H1 on the new concept + 2 new entities.
- **Counts reconciled** (`corpus_counts.py`): **162 sources / 227 concepts / 69 author entities (+[[pytorch]] = 70 entity pages)**, 13 findings / 11 synthesis / 4 comparisons / 2 methodology / 4 queries / 1 thesis. `index.md` and `overview.md` updated to agree.
- **LLM Wiki API:** not queried this batch (headless shell); not required for correctness.
- **Raw-folder scope:** only the 7 assigned batch-4 folders were curated; **2 batches (9 papers) remain** for separate invocations (batch5 7 / batch6 2).

## 2026-06-01 — Curation pass (batch 3/6: 7 new sources + audit)

Third batch of the deliberately-split **6-batch** curation run over the **37 genuinely-new** raw papers (split to keep context clean and avoid misinformation). This run curated **only** the 7 assigned batch-3 folders from `.curation-out/batches.json`; the other uncurated folders are owned by separate batch runs and were left untouched. Corpus grows **148 → 155 curated sources**. (Confirmed none of the 7 already had a source page before writing.) State reconciled clean at `2e0acc9` (batch 2) before starting; `curation_status.py --dupes` re-confirmed **23 genuinely-new** remaining (the two space-named re-ingests stay correctly flagged as duplicates and were not touched).

### New source pages (7)

- [[yang-2019-sum-power-uav-mec]] — Zhaohui Yang, Cunhua Pan, Kezhi Wang, Mohammad Shikh-Bahaei 2019 (**IEEE TWC**, `10.1109/TWC.2019.2927313`). Multi-UAV-MEC **sum-power minimization** of UEs + UAVs (incl. UAV propulsion power) over user association + power control + computation-capacity allocation + UAV location/altitude/beamwidth; iterative three-subproblem algorithm — compressive-sensing $\ell_0$ association + closed-form capacity + 1-D location search — with a fuzzy-c-means feasibility initializer. Findings: IACL beats SCAFAH/ECC, approaches EXH; converges ~3 iters, init >1000 W → ~420 W (figure-read, flagged indicative). pub 16 Jul 2019 / current version 10 Sep 2019 → 2019.
- [[mach-2017-mec-survey-architecture]] — Pavel Mach, Zdenek Becvar 2017 (**IEEE COMST**, `10.1109/COMST.2017.2682318`). The **architecture + computation-offloading** MEC survey: MCC-vs-edge comparison, integrated architectures (SCC/MMC/MobiScud/FMC/CONCERT) + ETSI standardization, and the three offloading research areas (decision / resource allocation / mobility management). Survey, no original numbers. pub 15 Mar 2017 / current version 21 Aug 2017 → 2017.
- [[raivi-2024-jdaco-postdisaster-iot]] — Asif Mahmud Raivi, Sangman Moh 2024 (**IEEE IoT-J**, `10.1109/JIOT.2024.3354950`). **JDACO** — joint data aggregation + computation offloading for multi-UAV post-disaster IoT; two-tier LT-UAV/HT-UAV; minimize aggregation+offload energy/delay + max IoT coverage; **VD3QN** = dueling double DQN + value-decomposition network. Abstract (verbatim): +20% training-time reduction / +11.4% processed data / +5.6% energy efficiency / +11.2% mission duration vs conventional, up to 98% IoT devices served. pub 16 Jan 2024 / current version 25 Apr 2024 → 2024.
- [[lee-2024-dho-leo-handover]] — Ju-Hyung Lee, Chanyoung Park, Soohyun Park, Andreas F. Molisch 2024 (**IEEE TWC**, `10.1109/TWC.2023.3342975`). **DHO** — DRL-based LEO-satellite **connection-handover protocol** that skips the Measurement Report by prediction; minimizes access delay + collision rate; trained with **IMPALA** (V-trace). Up to **6.86× / 4.18×** lower access delay than conventional HO / heuristic (abstract+intro, attributed to Tables IV–V). Networking/handover, not offloading. pub 21 Dec 2023 / current version 12 Jul 2024 → 2024.
- [[chu-2024-secure-ris-isac]] — Jinjin Chu, Zhiping Lu, Rang Liu, Ming Li, Qian Liu 2024 (**IEEE TVT**, correspondence, `10.1109/TVT.2023.3328192`). **Secure RIS-ISAC**: maximize radar output SNR s.t. per-user comm SINR + eavesdropping-SINR ceiling + power budget + RIS unit-modulus; AO/BCD + SDR + Dinkelbach FP + **majorization-minimization**. **~2 dB** radar gain vs no-RIS (abstract, verbatim). PHY secure-ISAC anchor, not MEC. pub 27 Oct 2023 / current version 14 Mar 2024 → 2024.
- [[guo-2024-multiuav-proactive-eavesdropping]] — Delin Guo, Lan Tang, Xinggan Zhang, Ying-Chang Liang 2024 (**IEEE TMC**, `10.1109/TMC.2023.3311484`). **Multi-UAV proactive eavesdropping** (legitimate surveillance): full-duplex UAVs jam multiple mobile suspicious UAV→destination links while planning trajectories; MDP decoupled (proven optimality-preserving) into a non-learning **jamming-power solver** + per-UAV **decentralized RL moving policy**. Guarantees eavesdrop rate/success with fewer UAVs (qualitative). Surveillance/PLS anchor, not MEC. pub 4 Sep 2023 / current version 4 Apr 2024 → 2024.
- [[lei-2024-hvmappo-maritime-sar]] — Chengjia Lei, Shaohua Wu, Yi Yang, Jiayin Xue, Qinyu Zhang 2024 (**IEEE TVT**, `10.1109/TVT.2024.3388499`). **Heterogeneous-vehicle maritime SAR** (observation UAVs + relay UAVs + ASV MEC servers, no BS); joint trajectory + offloading + routing topology minimizing time/energy while maximizing relay **fault tolerance**; Dec-POMDP + **HVMAPPO** (MAPPO/CTDE + parameter-sharing + normalized GAE + Pop-Art + mixed-heterogeneous-reward). Outperforms baselines in efficiency + fault tolerance (qualitative). pub 15 Apr 2024 / current version 19 Sep 2024 → 2024.

### New concept stubs (6)

- [[leo-handover-protocol]] — the LEO-satellite *connection* handover signaling procedure (vs compute-state [[seamless-handover]]); anchors [[lee-2024-dho-leo-handover]].
- [[impala]] — distributed off-policy actor-learner DRL with V-trace; the trainer behind DHO.
- [[majorization-minimization]] — surrogate-bound iterative optimization (MM); used in [[chu-2024-secure-ris-isac]]'s RIS-reflection update.
- [[value-decomposition-network]] — cooperative MARL value factorization (VDN); the cooperative-learning half of JDACO's VD3QN.
- [[fault-tolerant-relay-network]] — redundant multi-hop relay topology metric; the co-equal objective in [[lei-2024-hvmappo-maritime-sar]].
- [[proactive-eavesdropping]] — jamming-assisted legitimate surveillance; anchors [[guo-2024-multiuav-proactive-eavesdropping]].

All other referenced concepts reused existing slugs (e.g. [[multi-uav-assisted-mec]], [[task-offloading]], [[edge-user-allocation]], [[binary-vs-partial-offloading]], [[energy-latency-tradeoff]], [[weighted-kmeans-uav-deployment]], [[drone-cell-3d-placement]], [[mobile-edge-computing]], [[mobility-aware-offloading]], [[small-cell-mec]], [[virtual-machine-multiplexing]], [[post-disaster-mec]], [[uav-data-collection]], [[ddqn]], [[centralized-training-decentralized-execution]], [[rotary-wing-propulsion-energy-model]], [[hierarchical-aerial-mec]], [[leo-satellite-edge-computing]], [[non-terrestrial-network]], [[walker-star-constellation]], [[ppo]], [[integrated-sensing-and-communication]], [[intelligent-reflecting-surface]], [[physical-layer-security]], [[alternating-optimization-sdr-sca]], [[fractional-programming-dinkelbach]], [[friendly-jamming-uav]], [[cooperative-jamming]], [[ma-pomdp]], [[pomdp]], [[mappo]], [[gae]], [[heterogeneous-uav-fleet]], [[maritime-mec]]).

### Entities — 0 new + 1 roster update

- **Roster update:** [[kezhi-wang]] (3→4, +[[yang-2019-sum-power-uav-mec]] multi-UAV-MEC sum-power; Northumbria identity confirmed by in-parse affiliation).
- **No new entity pages.** Deferred / not created (correctness over completeness, single corpus source each / identity not confirmable from parse): Zhaohui Yang + Cunhua Pan + Mohammad Shikh-Bahaei (King's College London / Queen Mary); Pavel Mach + Zdenek Becvar (CTU Prague); Asif Mahmud Raivi + Sangman Moh (Chosun Univ.); Ju-Hyung Lee + Chanyoung Park + Soohyun Park + Andreas F. Molisch (USC / Korea Univ.); Jinjin Chu + Zhiping Lu + Rang Liu + Ming Li + Qian Liu (Dalian Univ. of Technology / CATT — "Ming Li"/"Rang Liu"/"Qian Liu" are common names needing disambiguation); Delin Guo + Lan Tang + Xinggan Zhang + Ying-Chang Liang (Nanjing Univ. / UESTC); Chengjia Lei + Shaohua Wu + Yi Yang + Jiayin Xue + Qinyu Zhang (HIT Shenzhen / Peng Cheng Lab). No author-entity links embedded in source-page bodies (house convention).

### Duplicate / near-duplicate check

- No same-paper/different-UUID duplicate ingests among the 7 batch-3 folders.
- [[raivi-2024-jdaco-postdisaster-iot]] (Chosun Univ., joint aggregation+offload, VD3QN) is **distinct** from the other post-disaster sources [[zhou-2024-jdl-abs-postdisaster-rescue]] (single-ABS queuing-delay min, Lyapunov + SCA-critic) and [[sun-2024-mvtora-postdisaster-vfc]] (game/VFC) — cross-linked, not duplicated.
- [[lei-2024-hvmappo-maritime-sar]] (HIT/PCL, HVMAPPO + fault-tolerant relay) is **distinct** from the maritime SAR sources [[qi-2024-msar-minmax-latency]] (min-max latency, linearization+SCA+BnB) and [[wang-2026-aerial-marine-msar]] (UAV+HAPS+MASS JCORA) — different authors, objective, and solver — cross-linked, not duplicated.
- [[chu-2024-secure-ris-isac]] is **distinct** from the other RIS/ISAC sources [[zhang-2025-gan-td3-isac-active-ris]] (GAN-TD3, double active RIS) and [[su-2024-sensing-aided-isac-pls]] / [[yao-2025-secure-isac-dual-eavesdropping]] — passive-RIS radar-SNR-max via AO+SDR+FP+MM — cross-linked, not duplicated.
- [[lee-2024-dho-leo-handover]] (connection-handover protocol, networking) is **distinct** from the compute-state handover work [[han-2024-sagin-fl-handover]] (FL model/data handover) — different "handover" meaning — cross-linked, not duplicated.
- [[guo-2024-multiuav-proactive-eavesdropping]] is a **surveillance/PLS** paper (jamming for legitimate eavesdropping), distinct from the anti-jamming-MEC sources; cross-linked to the jamming concepts, not duplicated.

### Audit (correctness-first)

- **DOI / venue / year** — all 7 carry an explicit `Digital Object Identifier` line in their own parse; every DOI/venue/year above is parse-grounded from the manuscript date-of-publication / date-of-current-version lines (year follows date-of-current-version for the straddling TWC/TVT/TMC/IoT-J papers, with both dates recorded in each citation). **Zero `not in parse` metadata fields this batch.** No web lookups were needed.
- **Grounded headline claims only:** JDACO +20% / +11.4% / +5.6% / +11.2% + 98% coverage (abstract verbatim); DHO 6.86× / 4.18× access-delay (abstract+intro, attributed to Tables IV–V); Chu RIS-ISAC ~2 dB radar gain (abstract verbatim); Yang-2019 IACL-beats-SCAFAH/ECC/near-EXH stated qualitatively with the ~3-iter / >1000→~420 W convergence figure-read flagged indicative; Guo proactive-eavesdropping (guarantee rate/success with fewer UAVs) and Lei HVMAPPO (outperforms baselines, efficiency-vs-fault-tolerance trade-off) stated qualitatively as the papers state them.
- **Wikilink integrity:** `linkcheck.py` = **NO DANGLING LINKS** (Obsidian-faithful). All new wikilinks target existing slugs or pages created in this batch (7 sources + 6 concepts).
- **Process-narration:** `process_refs.py` = **0 files / 0 hits** outside `log.md`; sources/concepts/entities/index/overview kept evergreen.
- **Frontmatter:** `type`/`title`/`authors`/`year`/`url`/`venue`/`tags`/`related`/dates/H1 validated (no diagnostics) on all 7 source pages; `type`/`title`/`tags`/dates/H1 on the 6 concepts and the touched entity.
- **Counts reconciled** (`corpus_counts.py`): **155 sources / 226 concepts / 67 author entities (+[[pytorch]] = 68 entity pages)**, 13 findings / 11 synthesis / 4 comparisons / 2 methodology / 4 queries / 1 thesis. `index.md` and `overview.md` updated to agree.
- **LLM Wiki API:** not queried this batch (headless shell); not required for correctness.
- **Raw-folder scope:** only the 7 assigned batch-3 folders were curated; **3 batches (16 papers) remain** for separate invocations (batch4 7 / batch5 7 / batch6 2).

## 2026-06-01 — Curation pass (batch 2/6: 7 new sources + audit)

Second batch of the deliberately-split **6-batch** curation run over the **37 genuinely-new** raw papers (split to keep context clean and avoid misinformation). This run curated **only** the 7 assigned batch-2 folders from `.curation-out/batches.json`; the other uncurated folders are owned by separate batch runs and were left untouched. Corpus grows **141 → 148 curated sources**. (Confirmed none of the 7 already had a source page before writing.) State reconciled clean at `388dcf8` (batch 1) before starting; `curation_status.py --dupes` re-confirmed **30 genuinely-new** remaining (the two space-named re-ingests stay correctly flagged as duplicates and were not touched).

### New source pages (7)

- [[zhou-2024-jdl-abs-postdisaster-rescue]] — Chengyi Zhou et al. 2024 (**IEEE TWC**, `10.1109/TWC.2024.3479709`). Post-disaster ABS computation offloading + communication assistance; min task-queuing-delay over ABS-GU association + offloading ratio + trajectory under ABS energy; **JDL** = Lyapunov + actor-critic DRL with a **model-based SCA critic** (vs a model-free critic DNN). Two-timescale (large-timescale trajectory, small-timescale offloading). Findings figure-read & flagged indicative (vs SDQN / circular-trajectory benchmarks). pub 21 Oct 2024 / current version 12 Dec 2024 → 2024.
- [[huang-2025-dual-aav-maritime-secure-cb]] — Jiawei Huang et al. 2025 (**IEEE IoT-J**, `10.1109/JIOT.2024.3521977`). Dual AAV cluster maritime secure communications via CB: MUVAA **relay** (data to Bob) + MUVAA **jammer** (jamming to Willie); multi-objective SEMCMOP (Bob SINR / Willie SINR / flight energy) solved by **IMOMA** (improved multi-objective mayfly algorithm, chaotic init + hybrid update). Abstract: security objective improved up to **43.20%**; CB-based SINR separation (Bob ≈20.75 / Willie ≈−39.9) verbatim from Fig. 5; IMOMA lowest energy 64 370 J among 5 (verbatim table). Presented in part at IEEE CSCWD 2023. pub 23 Dec 2024 / current version 25 Apr 2025 → 2025.
- [[mao-2016-lodco-eh-mec-offloading]] — Yuyi Mao, Jun Zhang, Khaled B. Letaief 2016 (**IEEE JSAC** 34(12) 3590–3605, `10.1109/JSAC.2016.2611964`). Green MEC with **energy-harvesting** devices; execution-cost (delay + task failure) min via the **LODCO** Lyapunov online algorithm (offloading + DVFS CPU-freq + transmit power from current state only); proven asymptotically optimal; monotonic CPU-freq/power vs battery level. pub 20 Sep 2016 / current version 29 Dec 2016 → 2016.
- [[yang-2024-taco-human-digital-twin-edge]] — Yuye Yang et al. 2024 (**IEEE TMC**, `10.1109/TMC.2024.3406607`). First **human digital twin (HDT)** edge-deployment study under end-edge-cloud; two-timescale accuracy-aware online optimization (**TACO**) jointly placing/updating generic+customized virtual twins + task offloading + ES access selection; improved Lyapunov + **piecewise McCormick envelopes** + BCD; closed-form gap-to-optimum + polynomial complexity. pub 28 May 2024 / current version 5 Nov 2024 → 2024.
- [[bor-yaliniz-2016-3d-abs-placement]] — R. Irem Bor-Yaliniz, Amr El-Keyi, Halim Yanikomeroglu (**IEEE ICC 2016**, `10.1109/ICC.2016.7510820`). First **3-D placement** of a drone-cell (ABS): jointly choose altitude + coverage location/size to maximize covered users; quadratically-constrained MINLP via altitude-to-radius bisection + MOSEK interior-point. **Metadata caveat:** the parse has **no** venue/year/DOI line (refs run to 2015); venue/DOI **web-confirmed** (IEEE Xplore doc 7510820 / arXiv 1603.00300) and explicitly flagged as not-in-parse on the page.
- [[zeng-2017-energy-efficient-uav-trajectory]] — Yong Zeng, Rui Zhang 2017 (**IEEE TWC** 16(6) 3747–3760, `10.1109/TWC.2017.2688328`). Energy-efficient UAV communication via trajectory optimization; first **fixed-wing propulsion-energy model** (speed + acceleration) + bits/Joule EE; shows unconstrained rate-max/energy-min give vanishing EE; circular + generally-constrained SCA trajectories. pub 28 Mar 2017 / current version 8 Jun 2017 → 2017.
- [[zhang-2013-energy-optimal-mcc-stochastic]] — Weiwen Zhang et al. 2013 (**IEEE TWC** 12(9) 4569–4581, `10.1109/TWC.2013.072513.121842`). Energy-optimal mobile cloud computing under a **stochastic (Gilbert-Elliott) channel**; mobile vs cloud execution via DVS CPU-freq / transmission-rate scheduling; closed-form policies + a **threshold policy** on data-consumption-rate $L/T$; $\kappa/\lambda = 6.67\times10^{-12}$ example (verbatim). accepted 24 Jun 2013 → 2013.

### New concept stubs (2)

- [[drone-cell-3d-placement]] — joint altitude + coverage location/size placement of an aerial base station; anchors [[bor-yaliniz-2016-3d-abs-placement]].
- [[fixed-wing-propulsion-energy-model]] — closed-form fixed-wing propulsion power vs speed + acceleration (power → ∞ as V→0, cannot hover); the counterpart to [[rotary-wing-propulsion-energy-model]]; originates in [[zeng-2017-energy-efficient-uav-trajectory]].

All other referenced concepts reused existing slugs (e.g. [[post-disaster-mec]], [[lyapunov-optimization]], [[two-timescale-optimization]], [[energy-harvesting-mec]], [[collaborative-beamforming]], [[physical-layer-security]], [[friendly-jamming-uav]], [[cooperative-jamming]], [[salp-swarm-algorithm]], [[maritime-mec]], [[air-to-ground-channel-model]], [[mixed-integer-nonlinear-programming]], [[alternating-optimization-sdr-sca]], [[task-offloading]], [[energy-latency-tradeoff]], [[binary-vs-partial-offloading]], [[service-caching-mec]], [[task-migration]], [[three-tier-cloud-edge-end]], [[edge-user-allocation]], [[mobility-aware-offloading]], [[virtual-machine-multiplexing]], [[cellular-connected-uav]], [[high-altitude-platform-station]], [[weighted-kmeans-uav-deployment]], [[uav-trajectory-control]]).

### Entities — 0 new + 6 roster updates

- **Roster updates:** [[geng-sun]] (12→13, +dual-AAV maritime secure CB, corresponding author), [[jiahui-li]] (9→10, +dual-AAV maritime secure CB, corresponding author), [[jiacheng-wang]] (7→8, +dual-AAV maritime secure CB), [[dusit-niyato]] (16→18, +dual-AAV maritime secure CB +HDT-TACO), [[jiawen-kang]] (11→12, +HDT-TACO), [[xuemin-shen]] (3→4, +HDT-TACO).
- **No new entity pages.** Deferred / not created (correctness over completeness): Yuyi Mao + Jun Zhang + Khaled B. Letaief (LODCO, HKUST — Yuyi Mao co-authored the existing [[mao-2017-mec-survey-communication]], but identity-vs-namesake and first-author-vs-survey-author handling left for human confirmation); Yong Zeng + Rui Zhang (energy-efficient UAV trajectory — recurring across [[zeng-2017-energy-efficient-uav-trajectory]], [[zeng-2019-rotary-wing-energy-min]], [[zeng-2019-uav-comm-tutorial-5g]], [[wu-2018-multiuav-minrate-trajectory]], but "Rui Zhang" is a common name needing affiliation disambiguation — flagged for human confirmation, no entity minted); Bor-Yaliniz / El-Keyi / Yanikomeroglu (Carleton; single corpus source each); Weiwen Zhang et al. (MCC; single source); Chengyi Zhou / Junyu Liu / Min Sheng / Jiandong Li / Weihua Zhuang (Xidian/Waterloo; single source); Yuye Yang / Changyan Yi / Jun Cai (NUAA/Concordia; single source). No author-entity links embedded in source-page bodies (house convention).

### Duplicate / near-duplicate check

- No same-paper/different-UUID duplicate ingests among the 7 batch-2 folders.
- [[zhou-2024-jdl-abs-postdisaster-rescue]] (Xidian, Chengyi Zhou) is **distinct** from the other post-disaster sources [[peng-2025-drudm-cfg]] (DRUDM-CFG, generative-DRL urgency admission) and [[sun-2024-mvtora-postdisaster-vfc]] (game/VFC) — different authors, objective (queuing-delay min), and solver (Lyapunov + SCA-critic actor-critic) — cross-linked, not duplicated.
- [[huang-2025-dual-aav-maritime-secure-cb]] is **distinct** from the other secure-CB sources [[sun-2024-imssa-uav-secure-cb]] (salp-swarm, imperfect/unknown eavesdroppers) and [[zhang-2024-gdmtd3-aerial-secure-cb]] (diffusion-TD3): dual-cluster relay+jammer maritime architecture + **mayfly** metaheuristic. Same Geng-Sun cluster, cross-linked.
- [[mao-2016-lodco-eh-mec-offloading]] (EH-MEC) and [[zhang-2013-energy-optimal-mcc-stochastic]] (stochastic-channel MCC) are **distinct** early offloading-theory anchors (different author sets/venues/years), cross-linked to each other and to [[mao-2017-mec-survey-communication]].

### Audit (correctness-first)

- **DOI / venue / year** — 6 of 7 carry an explicit DOI line in their own parse; every DOI/venue/year for those 6 is parse-grounded (manuscript date-of-publication / current-version lines, with year following date-of-current-version for the straddling TWC/JSAC/TMC/IoT-J papers). The **7th** ([[bor-yaliniz-2016-3d-abs-placement]]) has **no** venue/year/DOI in the parse → recorded as **not in parse** and **web-confirmed** (IEEE ICC 2016, doc 7510820 / arXiv 1603.00300), with the caveat stated verbatim on the page. No fabricated metadata.
- **Grounded headline claims only:** Dual-AAV 43.20% security-objective improvement + Fig. 5 SINR table (Bob 20.75 / Willie −39.9) + IMOMA 64 370 J table (verbatim); LODCO "significantly outperforms greedy / reduces failures at minor delay cost" and Zhang-2013 "significant energy saved in some cases" + threshold policy quoted as stated; JDL queuing-delay-vs-SDQN/circular curves flagged figure-read/indicative; TACO accuracy/delay/energy superiority stated qualitatively.
- **Wikilink integrity:** `linkcheck.py` after the pass = **NO DANGLING LINKS** (Obsidian-faithful). All new wikilinks target existing slugs or pages created in this batch (7 sources + 2 concepts).
- **Process-narration:** `process_refs.py` = **0 hits** outside `log.md`; sources/concepts/entities/index/overview kept evergreen.
- **Frontmatter:** `type`/`title`/`authors`/`year`/`url`/`venue`/`tags`/`related`/dates/H1 validated on all 7 source pages; `type`/`title`/`tags`/dates/H1 on the 2 concepts.
- **Counts reconciled** (`corpus_counts.py`): **148 sources / 220 concepts / 67 author entities (+[[pytorch]] = 68 entity pages)**, 13 findings / 11 synthesis / 4 comparisons / 2 methodology / 4 queries / 1 thesis. `index.md` and `overview.md` updated to agree.
- **LLM Wiki API:** not queried this batch (headless shell); not required for correctness.
- **Raw-folder scope:** only the 7 assigned batch-2 folders were curated; **4 batches (23 papers) remain** for separate invocations (batch3 7 / batch4 7 / batch5 7 / batch6 2).

## 2026-06-01 — Curation pass (batch 1/6: 7 new sources + audit)

First batch of a deliberately-split **6-batch** curation run over the **37 genuinely-new** raw papers currently uncurated (split to keep context clean and avoid misinformation). This run curated **only** the 7 assigned batch-1 folders; the other uncurated folders are owned by separate batch runs and were left untouched. Corpus grows **134 → 141 curated sources**. (Confirmed none of the 7 already had a source page before writing.)

> **Scope note.** `wiki/references/recommendations.md` named two "ready to curate now" picks — *Optimizing Spectrum Sharing in UAV Swarms…* and *UAV-Enabled Multi-Source Data Fusion in Vehicular Networks…* — but `curation_status.py --dupes` correctly flagged both raw folders as **duplicate MinerU ingests** (space-named) of already-curated underscore-named papers ([[wang-2025-uav-swarm-stackelberg]] and [[xie-2026-uav-multisource-fusion]]). They were **skipped, not re-curated**; the recommendations file is stale on these two. Reconciliation: `raw/sources` 173 folders, 134 curated, 39 uncurated → 2 duplicates → **37 genuinely-new**. `make_batches.py --size 7` → 6 batches (7/7/7/7/7/2).

### New source pages (7)

- [[mozaffari-2019-uav-wireless-tutorial]] — Mozaffari et al. 2019 (**IEEE COMST**, `10.1109/COMST.2019.2902862`). Tutorial on UAVs for wireless networks: UAVs as aerial base stations vs cellular-connected UAVs; 3D deployment, channel modeling, energy efficiency; analytical toolbox (optimization, ML, stochastic geometry, transport theory, game theory). *Not MEC — UAV-communications tutorial anchor.* Manuscript pub 5 Mar 2019 / current version 20 Aug 2019 → year 2019.
- [[sun-2024-active-passive-ris-receiver]] — Yifu Sun et al. 2024 (**IEEE TWC**, `10.1109/TWC.2023.3325813`). Active-passive cascaded RIS receiver for anti-jamming; worst-case rate max under imperfect angular jammer CSI; UM-ZF (passive) + AMM/C-M-CCD (active) semi-closed-form solutions. Reports PSR 32.8% vs 75.9% (2.78×) and ~0 dB vs ~−10 dB receive SINR at the BS direction (verbatim). *Not MEC — PHY RIS-receiver anchor.* pub 25 Oct 2023 / current version 12 Jun 2024 → 2024.
- [[wang-2024-blockchain-uav-mec-dpos]] — Die Wang et al. 2024 (**IEEE TVT**, `10.1109/TVT.2023.3306740`). Blockchain-integrated UAV-assisted MEC; improved **DPoS** (UAV light nodes + reputation-voted ground full nodes) + two-stage **Stackelberg** game over UAV trajectory/comm-resources and ground compute, solved via KKT + SCA. pub 21 Aug 2023 / current version 17 Jan 2024 → 2024.
- [[han-2024-ground-satellite-fl]] — Dong-Jun Han et al. 2024 (**IEEE JSAC**, `10.1109/JSAC.2024.3365901`). Cooperative FL over ground-to-satellite networks; LEO satellites as edge-compute units + intra-cluster aggregators + ISL relays; solar-battery-aware data offloading + non-convex convergence proof + latency minimizer. pub 13 Feb 2024 / current version 9 May 2024 → 2024.
- [[liu-2020-cooperative-uav-mec-power-iot]] — Yi Liu, Shengli Xie, Yan Zhang 2020 (**IEEE TVT**, `10.1109/TVT.2020.3016840`). Cooperative UAV-enabled MEC for power IoT (UAVs help neighboring small-cells); long-term utility max as a **semi-Markov** process; two-phase centralized + Q-value-transfer distributed DRL. pub 17 Aug 2020 / current version 22 Oct 2020 → 2020.
- [[wang-2024-hfrl-decentralized-navigation]] — Pengfei Wang et al. 2024 (**IEEE TMC**, `10.1109/TMC.2024.3439696`). Decentralized navigation for **heterogeneous** UAV-MEC; soft hierarchical DRL (SHDRLN, skill abstraction) + dual-end **federated RL** (DFRL) maximizing task-offloading energy efficiency. DFRL/FedAvg reach 2.7 KB/J at 100/200 episodes = original SHDRLN at 300; DFRL eventually surpasses original SHDRLN (verbatim figure-read). pub 7 Aug 2024 / current version 5 Nov 2024 → 2024.
- [[liu-2022-maritime-uav-mec-virtualization]] — Ying Liu, Junjie Yan, Xiaohui Zhao 2022 (**IEEE TVT**, `10.1109/TVT.2022.3141799`). Two-layer maritime UAV-MEC (T-UAV MEC server over B-UAVs) with **VM-multiplexing** parallel computing under I/O interference (unequal task sizes); latency min via DQN + DDPG over T-UAV trajectory + VM count. DDPG cuts total avg latency >37%, DQN 31% vs hover-center-no-parallel-computing (verbatim). pub 11 Jan 2022 / current version 2 May 2022 → 2022.

### New concept stubs (5)

- [[active-ris]] — RIS with phase + amplitude (amplifying) control; anchors [[sun-2024-active-passive-ris-receiver]].
- [[delegated-proof-of-stake]] — DPoS voting-elected delegate consensus; the improved DPoS of [[wang-2024-blockchain-uav-mec-dpos]].
- [[hierarchical-reinforcement-learning]] — skill/option temporal abstraction; the SHDRLN of [[wang-2024-hfrl-decentralized-navigation]].
- [[virtual-machine-multiplexing]] — multiple VMs per physical edge server with I/O interference; the parallel-compute mechanism of [[liu-2022-maritime-uav-mec-virtualization]].
- [[semi-markov-decision-process]] — random-sojourn-time MDP generalization; the formulation behind [[liu-2020-cooperative-uav-mec-power-iot]].

All other referenced concepts reused existing slugs (e.g. [[intelligent-reflecting-surface]], [[anti-jamming-mec]], [[physical-layer-security]], [[csi-estimation-error]], [[alternating-optimization-sdr-sca]], [[stackelberg-game]], [[blockchain-on-edge-trust-layer]], [[federated-learning]], [[federated-reinforcement-learning]], [[soft-actor-critic]], [[heterogeneous-uav-fleet]], [[leo-satellite-edge-computing]], [[privacy-sensitive-data-partitioning]], [[leo-satellite-coverage-time]], [[makespan-minimization]], [[maritime-mec]], [[multi-uav-assisted-mec]], [[deep-q-network]], [[ddpg]], [[parallel-vs-serial-processing]], [[cellular-connected-uav]], [[air-to-ground-channel-model]], [[high-altitude-platform-station]], [[stochastic-geometry-network-analysis]], [[uav-trajectory-control]], [[task-offloading]], [[small-cell-mec]]).

### Entities — 3 new + 3 roster updates

- **Created (3):** [[kaoru-ota]] (Muroran Inst. of Technology, `ota@csse.muroran-it.ac.jp`; 2 sources — [[wang-2024-blockchain-uav-mec-dpos]] + [[li-2024-twohop-iort-packet-scheduling]], with [[mianxiong-dong]]); [[dong-jun-han]] (Purdue, `han762@purdue.edu`; 2 sources — [[han-2024-ground-satellite-fl]] + [[han-2024-sagin-fl-handover]], first author both); [[christopher-brinton]] (Purdue, `cgb@purdue.edu`; 2 sources — same two, senior author both).
- **Roster updates:** [[mianxiong-dong]] (2→3, +blockchain-DPoS, corresponding author), [[shengli-xie]] (2→3, +power-IoT cooperative MEC; GDUT, `shlxie@gdut.edu.cn` consistent — same identity), [[geng-sun]] (11→12, +decentralized-navigation co-author; Jilin Univ.).
- No author-entity links were embedded in source-page bodies (house convention).

### Duplicate / near-duplicate check

- The two recommendations picks are duplicate ingests of already-curated papers — skipped (see scope note above).
- [[han-2024-ground-satellite-fl]] is **distinct** from the same Purdue group's [[han-2024-sagin-fl-handover]]: two-tier ground-to-satellite with solar-battery-aware offloading + convergence proof vs three-tier SAGIN adding a UAV/air layer and a seamless-handover offloading optimizer — cross-linked, not duplicated.
- [[liu-2020-cooperative-uav-mec-power-iot]] (Yi Liu, GDUT), [[liu-2022-maritime-uav-mec-virtualization]] (Ying Liu, Jilin Univ.) are **distinct authors** from each other and from existing Liu entities ([[lihan-liu]], [[yangbo-liu]], [[jiajia-liu]], [[yanheng-liu]]); no entity created for either first author (each has 1 corpus source).
- [[sun-2024-active-passive-ris-receiver]] (Yifu Sun, NUDT) is a **different author** from the Geng-Sun / Zemin-Sun / Hao-Sun entities and from [[sun-2024-mfris-semantic-antijamming]]'s author — no roster change.
- No same-paper/different-UUID duplicate ingests among the 7.

### Audit (correctness-first)

- **DOI / venue / year** — all 7 carry an explicit `Digital Object Identifier` line in their own parse; every DOI, venue, and year above is grounded (manuscript date-of-publication / date-of-current-version lines). **Zero `not in parse` metadata fields this batch.** Year follows date-of-current-version for the straddling TWC/TVT/JSAC/TMC papers, with both dates recorded in each citation.
- **Grounded headline claims only:** RIS PSR 32.8%/75.9% (2.78×) and ~0 dB vs ~−10 dB SINR; maritime DDPG >37% / DQN 31% latency reduction; HFRL 2.7 KB/J at 100/200 vs 300 episodes — all quoted from the parse (figure-read curves flagged indicative). Blockchain-DPoS "superior delay", cooperative power-IoT "better than non-cooperative", and ground-satellite-FL "significantly speeds up convergence" stated qualitatively as the papers state them.
- **Wikilink integrity:** `linkcheck.py` after the pass = **NO DANGLING LINKS** (Obsidian-faithful). All new wikilinks target existing slugs or pages created in this same batch (7 sources + 5 concepts + 3 entities).
- **Process-narration:** `process_refs.py` = **0 hits** outside `log.md`; sources/concepts/entities/index/overview kept evergreen.
- **Frontmatter:** `type`/`title`/`authors`/`year`/`url`/`venue`/`tags`/`related`/dates/H1 validated on all 7 source pages; `type`/`title`/`tags`/dates/H1 on the 5 concepts and 3 entities.
- **Counts reconciled** (`corpus_counts.py`): **141 sources / 218 concepts / 67 author entities (+[[pytorch]] = 68 entity pages)**, 13 findings / 11 synthesis / 4 comparisons / 2 methodology / 4 queries / 1 thesis. `index.md` and `overview.md` updated to agree.
- **LLM Wiki API:** not queried this batch (headless shell); not required for correctness.
- **Raw-folder scope:** only the 7 assigned batch-1 folders were curated; **5 batches (30 papers) remain** for separate invocations.



## 2026-06-01 — Synthesis pass (collaborative-beamforming track: +1 synthesis, +1 finding, cross-links; no new papers)

No-new-papers coverage-growth pass over the **collaborative-beamforming (CB)** cluster. Phase 0 confirmed the corpus is fully curated: `curation_status.py --dupes` reports **0 genuinely-new** folders (the two space-vs-underscore re-ingests — *Optimizing Spectrum Sharing…* and *UAV-Enabled Multi-Source Data Fusion…* — remain correctly classified as duplicate MinerU ingests, no page needed). Tree clean at `f3c67fb`. LLM Wiki API reachable (`allowUnauthenticated:true`, v0.4.16); baseline graph **446 nodes / 3717 edges** → **448 / 3751** after this pass.

The CB track had a [[collaborative-beamforming]] concept page and 5 source pages but **no synthesis page** and an under-counted track row in `overview.md` (4 of 5 sources) — the highest-leverage, cleanly-bounded gap. Each claim was grounded in the source parses before writing (GVAA+AVAA dual-array framing verified in the EMSSA parse; "save 30% handover frequency" verified verbatim in the EMODRL ground-space parse abstract).

### New derived pages (2)

- **Synthesis** [[collaborative-beamforming-in-aerial-mec]] — maps the 5 CB sources ([[sun-2025-emoppo-vlh-aerial-cb]], [[li-2024-emodrl-ground-space-cb]], [[li-2024-emssa-uav-swarm-vaa]], [[sun-2024-imssa-uav-secure-cb]], [[zhang-2024-gdmtd3-aerial-secure-cb]]) by array→receiver geometry (aerial-to-ground / ground-to-space / dual GVAA+AVAA), multi-objective trade (rate/secrecy vs flight energy, with SLL + leakage axes for the secure variants), and solver family (pure swarm-intelligence salp-swarm vs evolutionary-MORL vs diffusion-DRL) — a tidy microcosm of the [[drl-vs-evolutionary-vs-classical-solvers]] debate. Notes the gaps: no CB source carries a compute/offloading objective; single author cluster ([[geng-sun]] group); uneven eavesdropper threat models.
- **Finding** [[dcb-cuts-satellite-handover-frequency]] — distributed CB cuts LEO handover frequency ~30% at matched uplink rate ([[li-2024-emodrl-ground-space-cb]], `confidence: medium`, parse abstract); the clearest quantified CB result in the corpus.

### Refreshed / cross-linked pages

- [[collaborative-beamforming]] concept — added the dual GVAA+AVAA flavor row (was missing [[li-2024-emssa-uav-swarm-vaa]]) and a pointer to the new synthesis.
- 5 CB source pages — added `[[collaborative-beamforming-in-aerial-mec]]` to `related` (and the new finding to the EMODRL source); bumped `updated`.
- [[drl-vs-evolutionary-vs-classical-solvers]] synthesis — added the CB microcosm to `related`.
- `overview.md` — analytical-layer tally 12→13 findings / 10→11 synthesis; CB track row corrected 4→5 sources and linked to the synthesis; new finding listed in Open/analytical layer narrative.
- `index.md` — new finding under Findings, new synthesis under Synthesis.

### Entities

None created. The CB cluster authors ([[geng-sun]], [[jiahui-li]], [[zemin-sun]], [[qingqing-wu]], [[dusit-niyato]], [[jiawen-kang]], [[victor-c-m-leung]]) already have entity pages; no new clearly-recurring author surfaced in this slice.

### Self-check

- `linkcheck.py` — **NO DANGLING LINKS** (Obsidian-faithful). `process_refs.py` — **0 files / 0 hits** (no process-narration leaked outside this log). `corpus_counts.py` — sources 134, concepts 213, entities 65, findings 13, synthesis 11, comparisons 4, methodology 2, queries 4, thesis 1.
- Frontmatter validated on both new pages (no diagnostics). Counts in `overview.md`/`index.md` reconciled to the tool output.
- Toolkit unchanged this pass — the existing scripts covered every check; nothing warranted a new flag or script.

## 2026-05-31 — Curation pass (batch 8/8: 3 new sources + audit; multi-batch run complete)

Eighth and final batch of the deliberately-split 8-batch curation run over the 52 newly-ingested raw papers (split to keep context clean and avoid misinformation). This run curated **only** the 3 assigned batch-8 folders. Corpus grows **131 → 134 curated sources**, completing the 52-paper run (the two space-vs-underscore re-ingests — *Optimizing Spectrum Sharing…* and *UAV-Enabled Multi-Source Data Fusion…* — were correctly identified as duplicates of already-curated sources and skipped). (Confirmed none of the 3 already had a source page before writing.)

> **Note (orchestration):** this batch-8 run was interrupted after writing its pages, concepts, entities, and `index.md`/roster updates but before reconciling `overview.md`/`log.md` and committing. The interrupted work was inspected and completed (overview/log reconciliation + this entry + commit) rather than re-run, to avoid duplication. All three source pages and supporting pages were verified complete and parse-grounded before finishing.

### New source pages (3)

- [[sun-2024-imssa-uav-secure-cb]] — Sun et al. 2024 (**IEEE TMC**, `10.1109/TMC.2023.3273293`). UAV-enabled **secure communications** via **collaborative beamforming** (UVAA) against **known eavesdroppers with imperfect location info + unknown eavesdroppers**; multi-objective SCMOP (maximize worst-case secrecy rate / minimize max sidelobe level / minimize flight energy) proven non-convex & NP-hard, solved by an **improved multi-objective salp swarm algorithm (IMSSA)** with circle-map init + discrete update + migration/adaptive-mutation operators; Raspberry-Pi demonstration. Earlier version at IEEE ISCC 2022. DOI pub 5 May 2023 / current version 6 Mar 2024 → year 2024.
- [[xu-2024-mobile-aigc-survey]] — Xu et al. 2024 (**IEEE COMST**, `10.1109/COMST.2024.3353265`). **Survey** of edge-cloud generative-AI / **AIGC services** in mobile networks (**mobile AIGC networks**): generative-model fundamentals, the AIGC service lifecycle (data collection → pre-training → fine-tuning → inference → product management), the collaborative cloud-edge-mobile infrastructure, applications/case studies, and implementation challenges (edge resource allocation, task/computation offloading, edge caching, mobility management, incentive mechanisms). DOI pub 12 Jan 2024 / current version 23 May 2024 → year 2024.
- [[zeng-2024-usv-fleet-collaborative-offloading]] — Zeng et al. 2024 (**IEEE TVT**, `10.1109/TVT.2024.3359310`). UAVs offload marine-monitoring tasks **to USV fleets**; a **first-price sealed reverse auction with reserve price** incentivizes fleet participation (reserve = UAV valuation; symmetric-equilibrium bidding derived with existence + uniqueness proofs), then an energy-minimization problem is decomposed by **BCD** into two subproblems each solved by an **ADMM** improved with dynamic penalty coefficients. Participation degree improves **28.27%/25.74% over RBS/GBS** across task sizes and **27.84%/21.14%** across fleet counts (verbatim). Earlier version at IWCMC 2022. DOI pub 27 Feb 2024 / current version 17 Oct 2024 → year 2024.

### New concept stubs (3)

- [[mobile-aigc-network]] — the edge-cloud architecture for *serving* AIGC as the workload (distinct from [[generative-ai-for-mec]], which uses generative models to optimize the MEC system); anchors [[xu-2024-mobile-aigc-survey]].
- [[reverse-auction-incentive]] — first-price sealed reverse auction with reserve price (single buyer, lowest-bidding seller wins); the incentive layer of [[zeng-2024-usv-fleet-collaborative-offloading]].
- [[alternating-direction-method-of-multipliers]] — the ADMM augmented-Lagrangian block-splitting solver, complementing [[two-stage-decomposition]] / [[alternating-optimization-sdr-sca]] / [[penalty-dual-decomposition]].

All other referenced concepts reused existing slugs (e.g. [[collaborative-beamforming]], [[physical-layer-security]], [[salp-swarm-algorithm]], [[uav-trajectory-control]], [[air-to-ground-channel-model]], [[generative-ai-for-mec]], [[aigc-service-provider]], [[three-tier-cloud-edge-end]], [[generative-diffusion-model]], [[task-offloading]], [[service-caching-mec]], [[mobility-aware-offloading]], [[federated-learning]], [[maritime-mec]], double-auction, [[nash-equilibrium]], [[energy-latency-tradeoff]]).

### Entities — 2 new + roster updates

- **Created (2):** [[zhou-su]] (Xi'an Jiaotong Univ., `zhousu@ieee.org`; 2 sources — [[zeng-2024-usv-fleet-collaborative-offloading]] (corresponding author) + [[dai-2023-hybrid-marine-mmwl]]); [[yanheng-liu]] (Jilin Univ., `yhliu@jlu.edu.cn`; 2 sources — [[sun-2024-imssa-uav-secure-cb]] + [[sun-2023-bargain-match-vec]], in the [[geng-sun]] cluster).
- **Roster updates (existing entities):** [[victor-c-m-leung]] (3→5, +IMSSA secure-CB +AIGC survey), [[minghui-dai]] (2→3, +USV-fleet co-author), [[dusit-niyato]] (15→16, +AIGC survey), [[jiawen-kang]] (10→11, +AIGC survey), [[zhu-han]] (6→7, +AIGC survey), [[xuemin-shen]] (2→3, +AIGC survey), plus the IMSSA secure-CB co-authors [[geng-sun]], [[zemin-sun]], [[jiahui-li]], [[qingqing-wu]] (the IMSSA paper positively **confirms** the SJTU Qingqing Wu in the Geng-Sun collaborative-beamforming cluster).
- No author-entity links were embedded in source-page bodies (matching the established house convention).

### Duplicate / near-duplicate check

- [[sun-2024-imssa-uav-secure-cb]] is **distinct** from the existing secure-CB source [[zhang-2024-gdmtd3-aerial-secure-cb]] (swarm-intelligence IMSSA optimizer + imperfect/unknown-eavesdropper modeling vs diffusion-enhanced TD3 DRL) and from the other Geng-Sun CB papers ([[sun-2025-emoppo-vlh-aerial-cb]], [[li-2024-emodrl-ground-space-cb]], [[li-2024-emssa-uav-swarm-vaa]]) — cross-linked, not duplicated.
- [[zeng-2024-usv-fleet-collaborative-offloading]] is **distinct** from the same-cluster marine papers [[dai-2024-multiuav-marine-welfare]] (double-auction OBS selection) and [[dai-2023-hybrid-marine-mmwl]] (MMWL hybrid FDMA/NOMA) — different architecture (USV-fleet-as-helper), incentive (reverse auction), and solver (BCD/ADMM).
- [[xu-2024-mobile-aigc-survey]] is the anchor **survey** for the generative-AI thread, distinct from the methodological tutorial [[du-2024-gdm-network-optimization-tutorial]] and the concrete ASP-selection source [[du-2024-d2sac-aigc-asp-selection]].
- No same-paper/different-UUID duplicate ingests found among the 3.

### Audit (correctness-first)

- **DOI / venue / year** — all 3 carry an explicit `Digital Object Identifier` line in their own parse; every DOI, venue, and year is grounded (manuscript date-of-publication / date-of-current-version lines). **Zero `not in parse` metadata fields this batch.** Year follows date-of-current-version for the straddling TMC/TVT papers, with both dates recorded in each citation.
- **Grounded headline claims only:** USV-fleet participation-degree percentages (28.27%/25.74%; 27.84%/21.14%) quoted verbatim from the parse; IMSSA "outperforms MOPSO/NSGA-II/MODE/MSSA/IMODACH" stated as the paper states it (Pareto/metric curves are figure-derived, flagged indicative); the AIGC survey's claims framed as organizing claims, not measured results.
- **Wikilink integrity:** wiki-wide check after the pass = **ZERO dangling links** introduced this batch; all new wikilinks target existing slugs or pages created in this same batch. (Two pre-existing dangling references — `hp-mobility-models` and a root-level `purpose` link inside meta-doc narrative — are tracked for the next audit pass and were not introduced here.)
- **Frontmatter:** `type`/`title`/`authors`/`year`/`url`/`venue`/`tags`/`related`/dates/H1 validated on all 3 source pages; `type`/`title`/`tags`/dates/H1 on the 3 concepts and 2 entities.
- **Counts reconciled:** **134 sources / 213 concepts / 64 author entities (+[[pytorch]] = 65 entity pages)**. `index.md` and `overview.md` updated to agree.
- **LLM Wiki API:** not queried this batch (headless shell); not required for correctness.
- **Raw-folder scope:** only the 3 assigned batch-8 folders were curated; the 52-paper multi-batch run is now complete.

## 2026-05-31 — Curation pass (batch 7/8: 7 new sources + audit)

Seventh batch of the deliberately-split 8-batch curation run over 52 newly-ingested raw papers (split to keep context clean and avoid misinformation). This run curated **only** the 7 assigned batch-7 folders; the other uncurated folders are owned by separate batch runs and were left untouched. Corpus grows **124 → 131 curated sources**. (Confirmed none of the 7 already had a source page before writing.)

### New source pages (7)

- [[su-2024-sensing-aided-isac-pls]] — Su, Liu & Masouros 2024 (**IEEE TWC**, `10.1109/TWC.2023.3306029`). **Sensing-aided physical-layer security** for ISAC: a dual-functional BS emits an omnidirectional waveform to estimate eavesdropper directions (**CAML**), then jointly minimizes the **CRB** of targets/Eves and maximizes the **AN-aided secrecy rate** via alternating optimization (maximizing the FIM determinant) + a **fractional-programming** solver; robustness via a wide main beam sized by the prior-iteration CRB. Key result: secrecy rate improves as CRB decreases (single- and multi-Eve). *Not a UAV/MEC paper* — curated as a sensing-PLS anchor. DOI pub 23 Aug 2023 / current version 11 Apr 2024 → year 2024.
- [[zhu-2024-sensing-comm-doppler-uav-swarm]] — Zhu et al. 2024 (**IEEE TVT**, `10.1109/TVT.2023.3315868`). **Sensing-communication co-design** for UAV-swarm-assisted vehicular networks in perspective of **Doppler**; models Doppler's effect on comms (SNR loss) vs sensing (velocity estimation); minimizes ground-vehicles' **maximum CRLB** under an SNR-loss constraint via a **differential-evolution** algorithm. Abstract reports >30% sensing-accuracy gain + >20% communication gain vs SOTA (verbatim). *Sensing/comms only — no MEC offloading.* DOI pub 15 Sep 2023 / current version 13 Feb 2024 → year 2024.
- [[zhang-2019-stochastic-offloading-uav-mec]] — Zhang et al. 2019 (**IEEE IoT-J**, `10.1109/JIOT.2018.2890133`). **Stochastic** computation offloading + resource allocation + trajectory scheduling for single-UAV MEC; minimizes average weighted SMD+UAV energy; **Lyapunov** decomposition into three subproblems solved by **ADMM + interior-point + CVX**; the V and w_c parameters tune the queue-stability-vs-utility compromise. DOI pub 28 Dec 2018 / current version 8 May 2019 → year 2019.
- [[sun-2025-tjcct-twotimescale-uav-mec]] — Sun et al. 2025 (**IEEE TMC**, `10.1109/TMC.2024.3505155`). **TJCCT** — a **two-timescale** approach for UAV-assisted MEC; hierarchical MD/terrestrial-edge/aerial-edge/controller architecture; non-convex NP-hard MINLP system-utility maximization solved by short-timescale **price-incentive** resource allocation + **matching** offloading and long-timescale **convex** trajectory control; stability + polynomial complexity proved. Stated trade-off: superior delay/processing-rate/completion/cost metrics at the cost of higher energy consumption. Earlier version at INFOCOM 2024. DOI pub 22 Nov 2024 / current version 6 Mar 2025 → year 2025.
- [[li-2024-twohop-iort-packet-scheduling]] — Li et al. 2024 (**IEEE IoT-J**, `10.1109/JIOT.2024.3393444`). Two-hop **packet scheduling** + resource allocation + UAV trajectory design for **IoRT** in an air-ground integrated network (HAP→UAV→device); minimizes average packet **queue** delay; MDP with hybrid action space split into continuous (**MADDPG**) and discrete (**MADDQN**) sub-actions + **adaptive PER** → **MADDPG-APER**. DOI pub 25 Apr 2024 / current version 25 Jul 2024 → year 2024.
- [[dai-2024-uav-vehicular-offloading-lyapunov]] — Dai et al. 2024 (**IEEE TMC**, `10.1109/TMC.2023.3259394`). UAV relieves **overloaded RSUs** in vehicular edge computing; minimizes time-average vehicular task delay under a long-term UAV energy budget via **Lyapunov** decoupling + a **Markov-approximation** online offloading algorithm with a proven close-to-optimal gap. First author **Xingxia** Dai (Hunan University). DOI pub 20 Mar 2023 / current version 6 Mar 2024 → year 2024.
- [[liu-2020-wpt-cooperative-uav-mec]] — Liu et al. 2020 (**IEEE IoT-J**, `10.1109/JIOT.2019.2958975`). UAV-enabled **wireless-powered cooperative** MEC (UAV energy transmitter + MEC server; **idle SDs** harvest energy and help **active SDs** compute); minimizes total UAV required energy over CPU frequencies + offloading bits + transmit power + trajectory via an **SCA**-based algorithm and a lower-complexity **decomposition-and-iteration (DAI)** alternative. Trajectory optimization is the dominant energy factor (verbatim). DOI pub 20 Dec 2019 / current version 14 Apr 2020 → year 2020.

### New concept stubs (3)

- [[cramer-rao-bound]] — the CRB/CRLB sensing figure of merit (inverse Fisher Information), anchoring the two ISAC/Doppler sources ([[su-2024-sensing-aided-isac-pls]] CRB-vs-secrecy, [[zhu-2024-sensing-comm-doppler-uav-swarm]] min-max CRLB).
- [[two-timescale-optimization]] — fast (slot-level) vs slow (trajectory) decision decomposition; the short/long-timescale split behind TJCCT ([[sun-2025-tjcct-twotimescale-uav-mec]]).
- [[markov-approximation]] — Gibbs/log-sum-exp Markov-chain search over discrete configurations; the per-slot combinatorial solver in [[dai-2024-uav-vehicular-offloading-lyapunov]].

All other referenced concepts reused existing slugs (e.g. [[mobile-edge-computing]], [[task-offloading]], [[lyapunov-optimization]], [[uav-trajectory-control]], [[integrated-sensing-and-communication]], [[physical-layer-security]], [[fractional-programming-dinkelbach]], [[alternating-optimization-sdr-sca]], [[differential-evolution]], [[vehicular-mec]], [[uav-enabled-its]], [[hierarchical-aerial-mec]], [[matching-theory-for-resource-allocation]], [[mixed-integer-nonlinear-programming]], [[air-ground-integrated-network]], [[high-altitude-platform-station]], [[maddpg]], [[ddqn]], [[hybrid-action-decision-making]], [[prioritized-experience-replay]], [[wireless-power-transfer]], [[rf-energy-harvesting]], [[rotary-wing-propulsion-energy-model]], [[energy-latency-tradeoff]]).

### Entities — 5 new + roster updates + 1 affiliation-move deferral

- **Created (5):** [[shichao-li]] (Guilin Univ. of Electronic Technology, `shichaoli@guet.edu.cn`; 2 sources — [[li-2024-twohop-iort-packet-scheduling]] + the already-curated [[li-2025-twohop-airground-drl-offloading]]); [[hongbin-chen]] (GUET, `chbscut@guet.edu.cn`; 3 sources — the two two-hop IoRT papers + [[wang-2024-hybrid-oma-noma-sagin]]); [[mianxiong-dong]] (Muroran Inst. of Technology, `mx.dong@csse.muroran-it.ac.jp`; 2 sources — IoRT packet scheduling + [[li-2024-robust-bmappo-multiuav-mec]]); [[ning-zhang]] (Univ. of Windsor, `ning.zhang@uwindsor.ca`; 2 sources — same two as Dong); [[victor-c-m-leung]] (Shenzhen MSU-BIT / Shenzhen Univ. / UBC, `vleung@ieee.org`; 3 sources — [[sun-2025-tjcct-twotimescale-uav-mec]] + [[sun-2024-mvtora-postdisaster-vfc]] + [[li-2024-emodrl-ground-space-cb]]).
- **Roster updates (existing entities):** [[geng-sun]] (9→10, +TJCCT, corresponding author), [[zemin-sun]] (4→5, +TJCCT lead author), [[qingqing-wu]] (6→7, +TJCCT, SJTU-email-matched), [[dusit-niyato]] (14→15, +TJCCT), [[shuang-liang]] (3→4, +TJCCT corresponding author).
- **Deferred — Chau Yuen affiliation move.** "Chau Yuen" co-authors [[jia-2022-hierarchical-aerial-matching]] (Singapore Univ. of Technology and Design, `yuenchau@sutd.edu.sg`) and [[sun-2025-tjcct-twotimescale-uav-mec]] (Nanyang Technological Univ., `chau.yuen@ntu.edu.sg`). Same name, different listed institution/email — a plausible affiliation move rather than a namesake, but **not** minted as an entity pending human confirmation.
- The recurring TJCCT co-authors **Long He** and **Hongyang Pan** (Jilin University) each appear in only 1–2 corpus sources via the [[geng-sun]] cluster; no standalone entity pages were created (Long He appears in MVTORA + TJCCT but has no first-author corpus source — left for a future pass).
- No author-entity links were embedded in source-page bodies (matching the established house convention).

### Duplicate / near-duplicate check (the assigned watch item)

The brief warned that an already-curated "Stochastic … UAV … MEC" paper and vehicular-edge-computing papers could be confused with these. Verified each batch-7 paper is **genuinely new** and distinct:
- [[zhang-2019-stochastic-offloading-uav-mec]] (Zhang et al., NUDT, **IoT-J 2019**, ADMM/interior-point/CVX, joint SMD+UAV energy) is **distinct** from the already-curated [[yang-2022-stochastic-uav-mec-lyapunov]] (Yang/Bi/Zhang, **TWC 2022**, two-stage-vs-joint, user energy) — different authors, venue, year, DOI, and solver, despite near-identical titles. Both reuse [[lyapunov-optimization]].
- [[li-2024-twohop-iort-packet-scheduling]] (**packet-queue** delay, MADDPG+MADDQN+adaptive PER, IoT-J 2024) is **distinct** from the same lead author's [[li-2025-twohop-airground-drl-offloading]] (**task-offloading** delay, MADDPG-IPER+NV-IPPO/JPTORAUTD, IoT-J 2025) — different objective, action-space split, algorithm, year, DOI. Not a duplicate ingest.
- [[dai-2024-uav-vehicular-offloading-lyapunov]] (**Xingxia** Dai, Hunan Univ., vehicular VEC, Lyapunov+Markov-approximation, TMC) is **distinct** from the marine-welfare paper by **Minghui** Dai ([[dai-2024-multiuav-marine-welfare]]) and from the other vehicular sources ([[ma-2025-pdqn-vehicular-mec]], [[zhang-2025-mcma-task-migration]], [[sun-2023-bargain-match-vec]], [[peng-2020-maddpg-uav-vehicular]]) — different first author, method, and framing.
- [[sun-2025-tjcct-twotimescale-uav-mec]] (two-timescale price-incentive+matching+convex, TMC 2025) is **distinct** from the same group's [[sun-2024-mvtora-postdisaster-vfc]] (post-disaster game+convex+evolutionary, TMC 2024) — different architecture, objective, method, year.
- [[liu-2020-wpt-cooperative-uav-mec]] (idle-SD **cooperative** WPT-MEC, UAV-energy min, SCA/DAI, IoT-J 2020) is **distinct** from [[zhou-2018-uav-wireless-powered-mec]] (computation-rate max, JSAC 2018) — different objective + idle-SD cooperation.
- [[su-2024-sensing-aided-isac-pls]] (sensing-aided PLS, CRB-vs-secrecy, no UAV) is **distinct** from [[yao-2025-secure-isac-dual-eavesdropping]] (UAV-trajectory secure ISAC).
- No same-paper/different-UUID duplicate ingests were found among the 7.

### Audit (correctness-first)

- **DOI / venue / year** — all 7 carry an explicit `Digital Object Identifier` line in their own parse; every DOI, venue, and year above is grounded in the parse (manuscript date-of-publication / date-of-current-version lines). **Zero `not in parse` metadata fields this batch** — all 7 source pages have full title/authors/year/url/venue. **Year convention:** for papers whose publication vs current-version dates straddle two years, year follows date-of-current-version (the wiki's established convention), with both dates recorded in each citation (2018→2019 stochastic, 2019→2020 WPT-cooperative, 2023→2024 Doppler + UAV-VEC, 2024→2025 TJCCT).
- **Grounded headline claims only:** the verbatim figures — Zhu Doppler ">30% sensing / >20% communication" gains, Liu WPT "trajectory optimization is the dominant factor" + "converge within several iterations" — are quoted from the parse. Su CRB-vs-secrecy mutual improvement, TJCCT metric set + energy-consumption trade-off, Zhang stochastic V/w_c compromise, Li MADDPG-APER delay reduction, and Dai delay-reduction + multi-UAV energy trade-off are stated **qualitatively** as the papers state them, with figure-only magnitudes flagged as indicative.
- **Wikilink integrity:** wiki-wide link check after the pass = **no NEW dangling links** introduced (verified — see below). All wikilinks introduced this batch target existing slugs or pages created in this same batch (7 sources + 3 concepts + 5 entities). Pre-existing dangling-link status unchanged.
- **Frontmatter:** `type`/`title`/`authors`/`year`/`url`/`venue`/`tags`/`related`/dates/H1 validated on all 7 source pages; `type`/`title`/`tags`/dates/H1 on the 3 concept stubs and 5 entity pages. No self-references or duplicate `related` entries.
- **Counts reconciled:** **131 sources / 210 concepts / 62 author entities (+[[pytorch]] = 63 entity pages)**. `index.md` and `overview.md` updated to agree.
- **LLM Wiki API:** not queried this batch (headless shell); not required for correctness.
- **Raw-folder scope:** only the 7 assigned batch-7 folders were curated; other untracked `raw/sources/**` folders were intentionally left for their own batch runs.


## 2026-05-31 — Curation pass (batch 6/8: 7 new sources + audit)

Sixth batch of the deliberately-split 8-batch curation run over 52 newly-ingested raw papers (split to keep context clean and avoid misinformation). This run curated **only** the 7 assigned batch-6 folders; the other uncurated folders are owned by separate batch runs and were left untouched. Corpus grows **117 → 124 curated sources**. (Clean retry: a prior attempt was cancelled before writing; confirmed none of the 7 already had a source page.)

### New source pages (7)

- [[yang-2020-loadbalance-multiuav-iot]] — Yang et al. 2020 (**IEEE IoT-J**, `10.1109/JIOT.2020.2971645`). Multi-UAV **load-balance** MEC for IoT: **differential-evolution** UAV deployment + **generalized-assignment-problem** node assignment (LP-relax + bipartite rounding) + single-agent **DQN** task scheduling minimizing average slowdown. DOI pub 4 Feb 2020 / current version 12 Aug 2020 → year 2020.
- [[dai-2024-multiuav-marine-welfare]] — Dai et al. 2024 (**IEEE TCOMM**, `10.1109/TCOMM.2024.3388501`). Multi-UAV multi-access marine MEC (UAVs + **ocean beacon stations**); maximizes **system revenue** (system welfare − energy) by jointly optimizing OBS selection, offloading ratio, transmission duration; vertical 3-layer decomposition with a **double-auction** OBS-selection game. Reported trade-off: higher revenue **and** higher energy vs DOS/ROS benchmarks (Figs. 7–9, qualitative). DOI pub 15 Apr 2024 / current version 18 Sep 2024 → year 2024.
- [[al-hourani-2014-optimal-lap-altitude]] — Al-Hourani, Kandeepan & Lardner 2014 (**IEEE WCL**, `10.1109/LWC.2014.2342736`). Foundational **air-to-ground channel** letter: closed-form sigmoid **LoS-probability vs elevation angle** (ITU P.1410 parameters) + **optimal LAP altitude** maximizing ground coverage. *Not an MEC paper* — curated as a channel-model anchor. DOI pub 24 Jul 2014 / current version 17 Dec 2014 → year 2014.
- [[michailidis-2024-secure-ris-uav-mec-iot]] — Michailidis et al. 2024 (**IEEE TCOMM**, `10.1109/TCOMM.2024.3372877`). Secure UAV-**RIS**-MEC-IoT partial offloading vs **aerial + ground eavesdroppers**; UAV is both aerial MEC server and DF relay to a MEC-AP; derives **SOP** over Nakagami-m and maximizes **min secure computation efficiency** via Dinkelbach + BCD + bisection. UAV trajectory **not** optimized (fixed straight-line). DOI pub 1 Mar 2024 / current version 19 Jul 2024 → year 2024.
- [[zhang-2020-response-delay-uav-swarm]] — Zhang et al. 2020 (**IEEE TVT**, `10.1109/TVT.2020.2964821`). **Response-delay** optimization for a MEC-enabled UAV swarm (MEC top-UAV + bottom-UAVs); **stochastic geometry** (3-D PPP) + **queueing theory** closed-form delay. **Hardware-validated** on 2 DJI M100 UAVs + 5G NR mmWave (28 GHz). Reports 10–20% response-delay cut vs no-MEC; 89.9% fewer transmitted packets via on-T-UAV video key-frame extraction (verbatim). DOI pub 8 Jan 2020 / current version 12 Mar 2020 → year 2020.
- [[li-2024-robust-bmappo-multiuav-mec]] — Li et al. 2024 (**IEEE IoT-J**, `10.1109/JIOT.2023.3300718`). **Robust** multi-UAV-MEC offloading under joint communication (imperfect CSI) + computation (task-complexity error) uncertainty; weighted-energy min via **MAPPO with a Beta-distribution actor policy (b-MAPPO)**; beats Pure-MAPPO/MADDPG/Greedy, tracks DRL+CVX (avg UE reward ≈ −3.05 verbatim). DOI pub 1 Aug 2023 / current version 24 Jan 2024 → year 2024.
- [[li-2023-secure-marine-iot-jamming]] — Li et al. 2023 (**IEEE TVT**, `10.1109/TVT.2022.3231295`). **Secure** marine-IoT offloading: **USVs** upload to a **HAP** via NOMA then provide **cooperative jamming** (PLS); system-energy min via layered decomposition — **monotonic-optimization (Polyblock) + bisection (PAS)** for the bottom problem and **cross-entropy (CASE)** for USV positions. Reduces energy by **27.32%** on average vs fixed jamming (verbatim). DOI pub 22 Dec 2022 / current version 18 May 2023 → year 2023.

### New concept stubs (10)

- [[generalized-assignment-problem]] — capacity-constrained NP-hard task-to-agent assignment (the GAP behind the load-balance node-assignment of [[yang-2020-loadbalance-multiuav-iot]]).
- double-auction — many-to-many buyer/seller market mechanism (the OBS-selection game of [[dai-2024-multiuav-marine-welfare]]).
- [[air-to-ground-channel-model]] — the LoS/NLoS mixture ATG model + sigmoid LoS-probability-vs-elevation-angle, anchored by [[al-hourani-2014-optimal-lap-altitude]].
- [[secure-computation-efficiency]] — securely-computed bits per weighted energy (the SCE objective of [[michailidis-2024-secure-ris-uav-mec-iot]]).
- [[secrecy-outage-probability]] — probability that the secrecy rate falls below target (the SOP analysis of the secure-RIS source).
- [[queueing-theory]] — delay/queue-length analysis backbone of [[zhang-2020-response-delay-uav-swarm]].
- [[beta-policy-drl]] — Beta-distribution actor output for bounded actions (the b-MAPPO refinement).
- [[robust-offloading]] — bounded-uncertainty robust offloading (scheduling/channel/computation robustness).
- [[cooperative-jamming]] — reusing network nodes as helper jammers for PLS (the USV jamming of [[li-2023-secure-marine-iot-jamming]]).
- [[cross-entropy-method]] — sampling-based stochastic metaheuristic (the CASE algorithm of the secure-marine source).

All other referenced concepts reused existing slugs (e.g. [[mobile-edge-computing]], [[task-offloading]], [[multi-uav-assisted-mec]], [[maritime-mec]], [[load-balancing-uav-mec]], [[differential-evolution]], [[deep-q-network]], [[noma]], [[physical-layer-security]], [[intelligent-reflecting-surface]], [[monotonic-optimization]], [[fractional-programming-dinkelbach]], [[alternating-optimization-sdr-sca]], [[rotary-wing-propulsion-energy-model]], [[mappo]], [[csi-estimation-error]], [[centralized-training-decentralized-execution]], [[stochastic-geometry-network-analysis]], [[mmwave-radar-sensing]], [[two-stage-decomposition]], [[high-altitude-platform-station]], [[low-altitude-intelligent-network]], [[blockage-aware-channel-model]], [[terrain-aware-channel-model]], [[post-disaster-mec]], [[energy-latency-tradeoff]], [[uav-trajectory-control]]).

### Entities — 3 new + roster updates + 1 namesake deferral

- **Created (3):** [[liping-qian]] (Zhejiang Univ. of Technology, `lpqian@zjut.edu.cn`; 3 sources — [[dai-2024-multiuav-marine-welfare]] + [[dai-2023-hybrid-marine-mmwl]] + [[li-2023-secure-marine-iot-jamming]]); [[minghui-dai]] (Univ. of Macau, `minghuidai@um.edu.mo`; first author of 2 — [[dai-2024-multiuav-marine-welfare]] + [[dai-2023-hybrid-marine-mmwl]]); [[zhiyong-feng]] (Beijing Univ. of Posts and Telecommunications, `fengzy@bupt.edu.cn`; 2 — [[zhang-2020-response-delay-uav-swarm]] + [[meng-2024-uav-isac-overview]], affiliation confirmed in both parses).
- **Roster updates (existing entities):** [[bin-lin]] (7→8, +secure-marine-jamming), [[yuan-wu]] (7→9, +marine-welfare +secure-marine-jamming), [[tony-q-s-quek]] (4→5, +marine-welfare), [[chunxiao-jiang]] (3→4, +load-balance IoT), [[zhu-han]] (5→6, +UAV-swarm response delay).
- **Deferred — Jingjing Wang namesake.** The "Jingjing Wang" co-authoring [[yang-2020-loadbalance-multiuav-iot]] is at **Tsinghua University** (`chinaeephd@gmail.com`, Shuimu Tsinghua Scholar), **not** the existing **Beihang** [[jingjing-wang]] entity (`drwangjj@buaa.edu.cn`). Different institution + email ⇒ treated as a genuine namesake and **not** merged; the Beihang entity roster was left unchanged and no Tsinghua entity was minted (the Tsinghua Jingjing Wang has only this one corpus source).
- The "Chunxiao Jiang" on [[yang-2020-loadbalance-multiuav-iot]] **is** the existing Tsinghua entity (`jchx@tsinghua.edu.cn`-matched) — roster bumped.
- No author-entity links were embedded in source-page bodies (matching the established house convention).

### Duplicate / near-duplicate check

Verified each batch-6 paper is **genuinely new** and distinct from existing pages:
- [[yang-2020-loadbalance-multiuav-iot]] (load-balance via DE+GAP+DQN, IoT-J 2020) is distinct from the other multi-UAV-MEC sources ([[seid-2021-madrl-multiuav-iot-edge]] MADDPG clustered IoT-edge, [[zhao-2022-matd3-multiuav-ec-offloading]] MATD3) — different method (classical metaheuristic + single-agent DQN), objective (load balance), authors, year.
- [[dai-2024-multiuav-marine-welfare]] (double-auction system-welfare, TCOMM 2024) and [[dai-2023-hybrid-marine-mmwl]] (hybrid FDMA/NOMA MMWL, TCOMM 2023, already curated in batch 4) are the **same group** (Minghui Dai / Yuan Wu / Liping Qian) but **distinct papers** — different objective (system-revenue vs min-max-latency), mechanism (double auction vs layered convex), year, DOI.
- [[li-2023-secure-marine-iot-jamming]] (USV cooperative jamming, TVT 2023) is distinct from the other maritime sources — unique NOMA-via-HAP + cooperative-jamming PLS framing.
- [[michailidis-2024-secure-ris-uav-mec-iot]] (secure UAV-RIS-MEC, TCOMM 2024) is distinct from [[yao-2025-secure-isac-dual-eavesdropping]] (ISAC dual-eavesdropping) — RIS + MEC + SOP-over-Nakagami-m vs ISAC secrecy/sensing.
- [[zhang-2020-response-delay-uav-swarm]] (stochastic-geometry/queueing response delay, TVT 2020) is distinct from the DRL/game-theoretic UAV-swarm sources — analytical PPP + queueing backbone, hardware-validated.
- [[li-2024-robust-bmappo-multiuav-mec]] (robust b-MAPPO, IoT-J 2024) is distinct from the other MAPPO/MADDPG UAV-MEC sources by its joint communication+computation uncertainty robustness + Beta policy.
- No same-paper/different-UUID duplicate ingests were found among the 7.

### Audit (correctness-first)

- **DOI / venue / year** — all 7 carry an explicit `Digital Object Identifier` line in their own parse; every DOI, venue, and year above is grounded in the parse (manuscript date-of-publication / date-of-current-version lines). **Zero `not in parse` metadata fields this batch** — all 7 source pages have full title/authors/year/url/venue. **Year convention:** for papers whose publication vs current-version dates straddle two years, year follows date-of-current-version (the wiki's established convention), with both dates recorded in each citation.
- **Grounded headline claims only:** the verbatim figures — Zhang 10–20% response-delay cut + 89.9% packet reduction (52 s/7.84 Mbit → 9 key frames/775.9 kbit), Li b-MAPPO avg UE reward ≈ −3.05, Li secure-marine 27.32% energy reduction vs fixed jamming — are quoted from the parse text. Dai marine-welfare revenue/energy trade-off, Michailidis SCE/SOP behavior (element-count thresholds ~57/~60), Yang DRL-vs-FCFS/SJF/RR advantage, and Al-Hourani altitude/elevation-angle results are stated **qualitatively** as the papers state them, with figure-only magnitudes flagged as indicative.
- **Wikilink integrity:** wiki-wide link check after the pass = **ZERO dangling links** (verified — see below). All wikilinks introduced this batch target existing slugs or pages created in this same batch (7 sources + 10 concepts + 3 entities). Pre-existing dangling-link status unchanged (none). Two drafting-time fragmentations were caught before audit (an over-split `line-of-sight-probability-model` folded into [[air-to-ground-channel-model]]; a `response-delay-optimization-uav-swarm` finding reference removed since no finding page was created; a stray `qixun-zhang` author wikilink converted to plain text).
- **Frontmatter:** `type`/`title`/`authors`/`year`/`url`/`venue`/`tags`/`related`/dates/H1 validated on all 7 source pages; `type`/`title`/`tags`/dates/H1 on the 10 concept stubs and 3 entity pages. No diagnostics issues; no self-references or duplicate `related` entries.
- **Counts reconciled:** **124 sources / 207 concepts / 57 author entities (+[[pytorch]] = 58 entity pages)**. `index.md` and `overview.md` updated to agree.
- **LLM Wiki API:** not queried this batch (headless shell); not required for correctness.
- **Raw-folder scope:** only the 7 assigned batch-6 folders were curated; other untracked `raw/sources/**` folders were intentionally left for their own batch runs.

## 2026-05-31 — Curation pass (batch 5/8: 7 new sources + audit)

Fifth batch of the deliberately-split 8-batch curation run over 52 newly-ingested raw papers (split to keep context clean and avoid misinformation). This run curated **only** the 7 assigned batch-5 folders; the other uncurated folders are owned by separate batch runs and were left untouched. Corpus grows **110 → 117 curated sources**. (Clean retry: a prior attempt was cancelled before writing; confirmed none of the 7 already had a source page.)

### New source pages (7)

- [[duan-2023-moto-smallcell-offloading]] — Duan et al. 2023 (**IEEE TMC**, `10.1109/TMC.2022.3220720`). **MOTO** — mobility-aware online task offloading + adaptive load balancing in terrestrial **small-cell MEC**; decomposes the intractable TOO problem into Task offloading Control (LSTM) + Server Grouping (Dueling Double DQN); trace-driven on a real WiFi dataset. DOI pub 8 Nov 2022 / current version 5 Dec 2023 → year 2023.
- [[qi-2024-msar-minmax-latency]] — Qi et al. 2024 (**IEEE TVT**, `10.1109/TVT.2024.3384570`). Multi-UAV maritime **search & rescue** (S-UAVs + R-UAV); minimizes the **maximum total latency** among S-UAVs over offloading + R-UAV deployment + S-UAV–target association; iterative decomposition: linearization + **SCA** + **Branch-and-Bound**. DOI pub 3 Apr 2024 / current version 19 Sep 2024 → year 2024.
- [[seid-2021-madrl-multiuav-iot-edge]] — Seid et al. 2021 (**IEEE TNSM**, `10.1109/TNSM.2021.3096673`). Clustered multi-UAV IoT-edge offloading + resource allocation as a **stochastic game**; **MADDPG** (MADRL) minimizing energy+delay cost. Reports (verbatim) cost ↓ 38.643% / 55.621% and reward ↑ 58.289% / 85.289% vs single-agent DRL / heuristic. DOI pub 12 Jul 2021 / current version 9 Dec 2021 → year 2021.
- [[wang-2021-maddpg-multiuav-trajectory]] — Wang et al. 2021 (**IEEE TCCN**, `10.1109/TCCN.2020.3027695`). **MADDPG** per-UAV trajectory planning for multi-UAV MEC; jointly optimizes geographical fairness + UE-load fairness + UE energy; low-complexity offloading step given trajectories. DOI pub 29 Sep 2020 / current version 8 Mar 2021 → year 2021.
- [[peng-2020-maddpg-uav-vehicular]] — Peng & Shen 2020 (**IEEE JSAC**, `10.1109/JSAC.2020.3036962`). **MADDPG** multi-dimensional resource management (vehicle association + allocation) for MEC- and UAV-assisted vehicular networks; converges within ~200 episodes (verbatim), higher delay/QoS satisfaction than SADDPG/random. DOI pub 10 Nov 2020 / current version 16 Dec 2020 → year 2020.
- [[sun-2024-mfris-semantic-antijamming]] — Sun et al. 2024 (**IEEE JSAC**, `10.1109/JSAC.2024.3459028`). **Multi-functional RIS** + **semantic** anti-jamming communication and computing for an MEC integrated aerial-ground network; worst-case imperfect-jammer-CSI; semantic-computation-rate maximization via a fast-converging **monotonic optimization + decoupling SOCP (MO-DSOCP)** (global optimum) + low-complexity **GPI**. DOI pub 12 Sep 2024 / current version 22 Nov 2024 → year 2024 (earlier WCSP 2024 version noted).
- [[li-2024-emssa-uav-swarm-vaa]] — Li et al. 2024 (**IEEE TMC**, `10.1109/TMC.2023.3298888`). **Virtual antenna arrays** for UAV-swarm-assisted IoT data harvesting/dissemination; introduces collaborative beamforming into *both* sensors (GVAA) and UAVs (AVAA); multi-objective (completion time / eavesdropper signal / UAV energy) proven NP-hard, solved by the **enhanced multi-objective salp swarm algorithm (EMSSA)**. DOI pub 26 Jul 2023 / current version 4 Apr 2024 → year 2024.

### New concept stubs (7)

- [[maddpg]] — the standalone Multi-Agent Deep Deterministic Policy Gradient backbone page (deterministic-policy CTDE), distinct from [[multi-agent-td3]] / [[masac]]; grounds the three batch-5 MADDPG papers plus the pre-existing [[he-2023-fairness-3d-multiuav-maddpg]] / [[du-2023-maddpg-service-placement-agin]].
- [[small-cell-mec]] — MEC integrated with small-cell SBS networks; uneven spatio-temporal load + mobility challenges (grounds MOTO).
- [[mobility-aware-offloading]] — offloading control that accounts for user mobility / unknown future loads via online prediction.
- [[semantic-communication]] — 6G key-information (vs bit) transmission; robustness + data compression for MEC.
- [[multi-functional-ris]] — RIS with reflection + refraction + amplification + energy harvesting (full-space, self-sustaining).
- [[monotonic-optimization]] — global-optimization framework exploiting monotonicity (the MO-DSOCP solver behind the MF-RIS source).
- [[salp-swarm-algorithm]] — leader/follower swarm-intelligence metaheuristic; EMSSA multi-objective variant grounds the VAA source.

All other referenced concepts reused existing slugs (e.g. [[mobile-edge-computing]], [[task-offloading]], [[multi-uav-assisted-mec]], [[vehicular-mec]], [[maritime-mec]], [[centralized-training-decentralized-execution]], [[stochastic-game]], [[ddqn]], [[deep-q-network]], [[ddpg]], [[collaborative-beamforming]], [[uav-data-collection]], [[physical-layer-security]], [[intelligent-reflecting-surface]], [[anti-jamming-mec]], [[air-ground-integrated-network]], [[csi-estimation-error]], [[mixed-integer-nonlinear-programming]], [[multi-objective-reinforcement-learning]], [[fairness-metrics-in-mec]], [[jains-fairness-index]], [[two-stage-decomposition]], [[uav-trajectory-control]], [[binary-vs-partial-offloading]], [[load-balancing-uav-mec]], [[dynamic-qos-constraints]], [[uav-enabled-its]], [[video-analytics-offloading]]).

### Entities — 4 new + roster updates (no deferrals this batch)

- **Created (4):** [[kezhi-wang]] (Northumbria University, `kezhi.wang@northumbria.ac.uk`; 3 sources — [[wang-2022-cat-rat-fmec-trajectory]] + [[wang-2021-maddpg-multiuav-trajectory]] + [[wang-2019-todetas-deployment-scheduling]], frequently corresponding author, anchors the Northumbria UAV-MEC group); [[xuemin-shen]] (University of Waterloo, `sshen@uwaterloo.ca`; 2 sources — [[peng-2020-maddpg-uav-vehicular]] + [[duan-2023-moto-smallcell-offloading]]); [[yuguang-fang]] (City University of Hong Kong, `my.fang@cityu.edu.hk`; 2 sources — [[wang-2024-maritime-eh-jcora]] + [[qi-2024-msar-minmax-latency]], in the [[bin-lin]] maritime cluster); [[haixia-peng]] (University of Waterloo → Xi'an Jiaotong University; 2 sources — [[peng-2020-maddpg-uav-vehicular]] + [[wang-2024-twotier-satellite-marine]], the affiliation move is documented in both parses so treated as one researcher, not a namesake).
- **Roster updates (existing entities):** [[geng-sun]] (8→9 sources, +VAA), [[jiahui-li]] (7→8, +VAA as lead author), [[qingqing-wu]] (5→6, +VAA — **confirms the SJTU [[qingqing-wu]]** `qingqingwu@sjtu.edu.cn` on this paper, unrelated to the deferred NUS namesake), [[bin-lin]] (6→7, +MSAR min-max-latency).
- No author-entity links were embedded in source-page bodies (matching the established house convention).

### Duplicate / near-duplicate check (the assigned watch item)

The brief warned that several already-curated "Multi-Agent … Multi-UAV … MEC" papers could be confused with these. Verified each batch-5 paper is **genuinely new** and distinct:
- [[wang-2021-maddpg-multiuav-trajectory]] (*…Trajectory Planning…*, **IEEE TCCN 2021**, MADDPG, dual-fairness + energy) is **distinct** from the same group's already-curated [[wang-2022-cat-rat-fmec-trajectory]] (*Dynamic Trajectory Control…*, **IEEE TMC 2022**, CAT/RAT single twin-DQN agent) — different venue, DOI, year, and single-vs-multi-agent method — and from [[chang-2022-marl-multiuav-trajectory]] (TNSE).
- [[seid-2021-madrl-multiuav-iot-edge]] (UESTC/DFKI, **TNSM 2021**, MADDPG, clustered IoT-edge) is **distinct** from [[zhao-2022-matd3-multiuav-ec-offloading]] (MATD3, TWC 2022) and [[he-2023-fairness-3d-multiuav-maddpg]] (MADDPG fairness 3D) — different authors, venue, year.
- [[peng-2020-maddpg-uav-vehicular]] (Peng/Shen, **JSAC 2020**) is a new vehicular-MEC entry distinct from the corpus's other vehicular papers ([[ma-2025-pdqn-vehicular-mec]], [[zhang-2025-mcma-task-migration]], [[sun-2023-bargain-match-vec]]).
- [[qi-2024-msar-minmax-latency]] (S-UAV/R-UAV min-max latency, TVT 2024) is **distinct** from [[wang-2026-aerial-marine-msar]] (UAV+HAPS+MASS three-tier JCORA, matching+convex+PGD) despite both being Bin-Lin-group maritime SAR papers — different architecture, objective, method, venue, year.
- [[li-2024-emssa-uav-swarm-vaa]] (salp-swarm CB virtual antenna arrays, TMC) is **distinct** from [[sun-2025-emoppo-vlh-aerial-cb]] / [[li-2024-emodrl-ground-space-cb]] (evolutionary-RL CB) — pure swarm-intelligence optimizer, IoT data-harvesting framing.
- No same-paper/different-UUID duplicate ingests were found among the 7.

### Audit (correctness-first)

- **DOI / venue / year** — all 7 carry an explicit `Digital Object Identifier` line in their own parse; every DOI, venue, and year above is grounded in the parse (manuscript date-of-publication / date-of-current-version lines). **Zero `not in parse` metadata fields this batch** — all 7 source pages have full title/authors/year/url/venue. **Year convention:** for the TMC/TVT/TCCN/JSAC/TNSM papers whose publication vs current-version dates straddle two years, year follows date-of-current-version (the wiki's established convention), with both dates recorded in each citation.
- **Grounded headline claims only:** Seid MADRL percentages (38.643% / 55.621% cost, 58.289% / 85.289% reward) and Peng "converges within 200 episodes" are verbatim from the abstracts; MOTO load-balancing/cost advantage, MSAR effectiveness, MF-RIS superiority, and EMSSA "reduce time and energy costs significantly" are stated **qualitatively** as the papers state them (no figure-only magnitudes asserted as exact). The MOTO dataset scale (29,284,966 records / 21,725 users / 4,045 APs) and the >80%-under-600 s CDF observation are from the parse (CDF flagged as read-from-figure).
- **Wikilink integrity:** wiki-wide Obsidian-faithful link check after the pass = **ZERO dangling links** (verified — see below). All wikilinks introduced this batch target existing slugs or pages created in this same batch (7 sources + 7 concepts + 4 entities). Pre-existing dangling-link status unchanged (none).
- **Frontmatter:** `type`/`title`/`authors`/`year`/`url`/`venue`/`tags`/`related`/dates/H1 validated on all 7 source pages; `type`/`title`/`tags`/dates/H1 on the 7 concept stubs and 4 entity pages. No diagnostics issues; no self-references or duplicate `related` entries.
- **Counts reconciled:** **117 sources / 197 concepts / 54 author entities (+[[pytorch]] = 55 entity pages)**. `index.md` and `overview.md` updated to agree.
- **LLM Wiki API:** not queried this batch (headless shell); not required for correctness.
- **Raw-folder scope:** only the 7 assigned batch-5 folders were curated; other untracked `raw/sources/**` folders were intentionally left for their own batch runs.

## 2026-05-31 — Curation pass (batch 4/8: 7 new sources + audit)

Fourth batch of the deliberately-split 8-batch curation run over 52 newly-ingested raw papers (split to keep context clean and avoid misinformation). This run curated **only** the 7 assigned `batch4` folders (per `.curation-out/batches.json`); the other uncurated folders are owned by separate batch runs and were left untouched. Corpus grows **103 → 110 curated sources**.

### New source pages (7)

- [[wang-2024-maritime-eh-jcora]] — Wang et al. 2024 (**IEEE IoT-J**, `10.1109/JIOT.2024.3371049`). Energy-harvesting maritime MEC: a two-tier sea-lane-monitoring network (CBS + solar/ocean-wave-powered maritime information stations / buoys serving vessels); maximizes long-term throughput under queue-stability + energy constraints via **Lyapunov** drift-plus-penalty decomposition → **JCORA**. Beats FRA/LRA/PRA/TRA benchmarks (curves read from Figs. 7–12, reported qualitatively). DOI pub 28 Feb 2024 / current version 23 May 2024 → year 2024.
- [[hu-2019-pdd-uav-mec-offloading]] — Hu et al. 2019 (**IEEE IoT-J**, `10.1109/JIOT.2018.2878876`). Single-UAV MEC; minimizes the sum of per-slot **max delay** by jointly optimizing offloading ratio + UAV trajectory + binary user scheduling via **penalty dual decomposition (PDD)** (inner CCCP, outer AL-multiplier/penalty update) + a simplified l0-norm variant. DOI pub 31 Oct 2018 / current version 8 May 2019 → year 2019.
- [[niazmand-2025-jopa-dnn-pruning-iiot]] — Niazmand & Ye 2025 (**IEEE TCCN**, `10.1109/TCCN.2025.3529688`). Joint task offloading + **DNN model pruning** + edge resource allocation (JOPA) for industrial-washing-machine fault detection; maximizes long-term resource utilization under **time-varying delay/accuracy QoS**; formulated as a **Markov reward process**, solved with a hybrid-action **SAC**. Highest utilization + lowest task-dropping (<1%) vs JOPAV1/AGDM (Figs. 9–12, qualitative). DOI pub 14 Jan 2025 / current version 8 Oct 2025 → year 2025.
- [[wu-2018-multiuav-minrate-trajectory]] — Wu, Zeng & Zhang 2018 (**IEEE TWC**, `10.1109/TWC.2017.2789293`, 17(3):2109–2121). Foundational multi-UAV-as-base-station **max-min-rate** design; joint scheduling/association + trajectory + power via **BCD + SCA** with circle-packing initialization; reveals throughput-access-delay tradeoff. DOI pub 5 Jan 2018 / current version 8 Mar 2018 → year 2018. (Vol/issue/pages from in-parse reference list entry [9].)
- [[dai-2023-hybrid-marine-mmwl]] — Dai et al. 2023 (**IEEE TCOMM**, `10.1109/TCOMM.2023.3306581`). Hybrid offshore (FDMA) + aerial-UAV (NOMA) multi-access offloading; **Minimize Maximum Workloads Latency (MMWL)** via a layered 3-subproblem decomposition. Within ~3% of LINGO's global optimum with >90% time saving (verbatim). DOI pub 18 Aug 2023 / current version 20 Nov 2023 → year 2023.
- [[wu-2024-urllc-uav-mec-latency]] — Wu et al. 2024 (**IEEE TWC**, `10.1109/TWC.2023.3307154`). First UAV-MEC study to drop the infinite-blocklength assumption: **URLLC / finite-blocklength** offloading under angle-dependent **Rician fading**; min-max latency via **BCD + SCA** over UAV 3D location + bandwidth + CPU frequency (semi-closed-form). DOI pub 28 Aug 2023 / current version 11 Apr 2024 → year 2024.
- [[zhang-2025-vnf-sgin-dql]] — Zhang et al. 2025 (**IEEE TVT**, `10.1109/TVT.2024.3454438`). **NFV/SDN service-function-chaining** for 6G satellite-ground integrated networks; dynamic VNF selection + chaining (DDVSC) via **deep Q-learning** with load-clustered greedy action space; maximizes long-term network profit (provisioning + migration cost vs performance). DOI pub 30 Sep 2024 / current version 16 Jan 2025 → year 2025.

### New concept stubs (7)

- [[energy-harvesting-mec]] — MEC powered by harvested renewable energy (solar/wind/ocean-wave), distinct from RF-harvesting/WPT; grounds the maritime-EH source.
- [[penalty-dual-decomposition]] — the PDD framework (binary→equality reformulation + augmented-Lagrangian + two-layer CCCP iteration) for non-convex coupled problems.
- [[markov-reward-process]] — MDP variant with action-independent state transitions; the formulation behind the IIoT DNN-pruning source.
- [[dynamic-qos-constraints]] — time-varying per-task delay/accuracy requirements tied to changing criticality levels.
- [[finite-blocklength-urllc]] — short-packet URLLC where the Shannon formula overstates rate; the angle-dependent-Rician finite-blocklength rate of the URLLC source.
- [[network-function-virtualization]] — NFV/SDN substrate (VNFs on commodity servers) for the SGIN VNF-chaining source.
- [[service-function-chaining]] — ordered VNF chains (SFC) + VSCP selection/mapping, with satellite-movement-driven VNF migration.

All other referenced concepts reused existing slugs (e.g. [[maritime-mec]], [[lyapunov-optimization]], [[task-offloading]], [[task-migration]], [[noma]], [[mixed-integer-nonlinear-programming]], [[two-stage-decomposition]], [[alternating-optimization-sdr-sca]], [[uav-trajectory-control]], [[multi-uav-assisted-mec]], [[binary-vs-partial-offloading]], [[soft-actor-critic]], [[hybrid-action-decision-making]], [[dnn-model-partition]], [[knowledge-distillation-for-drl]], [[deep-q-network]], [[leo-satellite-edge-computing]], [[non-terrestrial-network]], [[space-air-ground-integrated-network]], [[fairness-metrics-in-mec]], [[network-slicing]]).

### Entities — roster updates + 2 deferrals (no new entity pages)

- **Roster updates (existing entities):** [[qiang-ye]] (3→6 sources — the **cross-cutting thread of batch 4**, on 4 of the 7 papers: maritime-EH, IIoT DNN-pruning, VNF/SGIN; University of Calgary, `qiang.ye@ucalgary.ca`), [[bin-lin]] (4→6, +maritime-EH +hybrid-marine; Dalian Maritime Univ.), [[zhen-wang]] (3→4, +maritime-EH; same Dalian Maritime/Neusoft dual affiliation + `wangzhen_jsj@neusoft.edu.cn`), [[yuan-wu]] (6→7, +hybrid-marine; Univ. of Macau, corresponding author), [[qingqing-wu]] (4→5, +URLLC; **SJTU** `qingqingwu@sjtu.edu.cn`-matched).
- **Deferred — Qingqing Wu namesake (again).** The batch-4 [[wu-2018-multiuav-minrate-trajectory]] is **first-authored** by a "Qingqing Wu" at the **National University of Singapore** (`elewuqq@nus.edu.sg`), not the SJTU [[qingqing-wu]] entity (`qingqingwu@sjtu.edu.cn`). Consistent with the batch-1 deferral on the 2019 NUS tutorial, this 2018 NUS paper was **not** added to the SJTU roster — noted on the entity page; plausibly the same person earlier in his career, flagged for human confirmation.
- **Deferred — Yong Zeng / Rui Zhang entity creation.** "Yong Zeng" now recurs in 3 sources ([[wu-2018-multiuav-minrate-trajectory]], [[zeng-2019-uav-comm-tutorial-5g]], [[zeng-2019-rotary-wing-energy-min]]) and "Rui Zhang" likewise, both NUS-affiliated. They clear the recurrence bar for entity pages, but affiliation verification across all three parses was not completed this pass, so no entity was minted — flagged for a future pass / human confirmation rather than created hastily.
- No author-entity links were embedded in source-page bodies (matching the established house convention — three accidental author wikilinks introduced during drafting were caught and converted to plain text before the audit).

### Duplicate / near-duplicate check (the assigned watch item)

The batch brief warned that several already-curated "Joint … UAV … MEC" papers could be confused with these. Verified each batch-4 paper is **genuinely new** and distinct from existing pages:
- [[hu-2019-pdd-uav-mec-offloading]] (Hu/Cai/Yu, *Joint Offloading and Trajectory Design …*, IoT-J 2018/2019, PDD) is **distinct** from the already-curated [[yu-2020-uav-ec-collaborative-offloading]] (Yu/Gong, *Joint Task Offloading and Resource Allocation …*, IoT-J 2020, SCA) — different authors, DOI, year, method.
- [[wu-2018-multiuav-minrate-trajectory]] (*Joint Trajectory and Communication Design for Multi-UAV …*, TWC 2018, BCD+SCA, communications/max-min-rate) is **distinct** from [[chang-2022-marl-multiuav-trajectory]] (*Trajectory Design and Resource Allocation for Multi-UAV …*, TNSE 2022, DRL) — different title, authors, venue, year, method.
- [[wang-2024-maritime-eh-jcora]] and [[dai-2023-hybrid-marine-mmwl]] are new maritime sources distinct from the existing 8 maritime pages (different architectures: EH-buoys+Lyapunov vs FDMA/NOMA hybrid offshore+aerial).
- No same-paper/different-UUID duplicate ingests were found among the 7.

### Audit (correctness-first)

- **DOI / venue / year** — all 7 carry an explicit `Digital Object Identifier` line in their own parse; every DOI, venue, and year above is grounded in the parse (manuscript date-of-publication / date-of-current-version lines). **Zero `not in parse` metadata fields this batch** — all 7 source pages have full title/authors/year/url/venue. **Year convention:** for the five TVT/TWC/TCOMM/IoT-J papers whose publication vs current-version dates straddle two years, year follows date-of-current-version (the wiki's established convention), with both dates recorded in each citation.
- **Grounded headline claims only:** maritime-EH JCORA throughput/latency advantages stated qualitatively (Figs. 7–12 are MinerU-rendered tables, not verbatim text); hybrid-marine "≤3% from LINGO global optimum" + ">90% time saving" verbatim from the parse abstract/contributions; URLLC bottleneck insight + "finite-blocklength necessary" from the conclusion; IIoT JOPA "<1% dropping" + "p=0.7 balances" from Sec. V; PDD/min-max-rate/VNF-DQL results stated as the papers state them ("significantly outperform", "approaches the upper bound"). No figure-only magnitudes asserted as exact.
- **Wikilink integrity:** wiki-wide Obsidian-faithful check after the pass = **ZERO dangling links** (`.curation-out/linkcheck2.py`). All wikilinks introduced this batch target existing slugs or pages created in this same batch (7 sources + 7 concepts). Pre-existing dangling-link status unchanged (none).
- **Frontmatter:** `type`/`title`/`authors`/`year`/`url`/`venue`/`tags`/`related`/dates/H1 validated on all 7 source pages; `type`/`title`/`tags`/dates/H1 on the 7 concept stubs. No diagnostics issues; no self-references or duplicate `related` entries.
- **Counts reconciled:** **110 sources / 190 concepts / 50 author entities (+[[pytorch]] = 51 entity pages)**. `index.md` and `overview.md` updated to agree.
- **LLM Wiki API:** not queried this batch (headless shell); not required for correctness.
- **Raw-folder scope:** only the 7 assigned `batch4` folders were curated; other untracked `raw/sources/**` folders were intentionally left for their own batch runs.

## 2026-05-31 — Curation pass (batch 3/8: 7 new sources + audit)

Third batch of the deliberately-split 8-batch curation run over 52 newly-ingested raw papers (split to keep context clean and avoid misinformation). This run curated **only** the 7 assigned `batch3` folders (per `.curation-out/batches.json`); the other uncurated folders are owned by separate batch runs and were left untouched. Corpus grows **96 → 103 curated sources**.

### New source pages (7)

- [[qu-ecoei-uav-swarm]] — Qu et al. (**IEEE Communications Magazine**, `10.1109/MCOM.002.2300129`). **eCoEI** — OODA-loop-based elastic collaborative DL inference for UAV swarms, robust to node/A2A-link failure; proof-of-concept on 4 airborne Jetson devices (Faster R-CNN; ≈0.8→2.9 FPS with more UAVs; keeps running at ≈2 FPS when one UAV drops). **Year: not in parse** (magazine parse has no manuscript-date/volume line); DOI from parse, venue from parse.
- [[cheng-2025-dos-satellite-edge-computing]] — Cheng et al. 2025 (**IEEE TVT**, `10.1109/TVT.2024.3483203`). **DOS** — energy-constrained LEO satellite edge computing for STINs; Lyapunov + convex decomposition under satellite solar-harvest/eclipse dynamics + location-dependent stochastic task arrivals; near-optimal, beats GE/OPT/GS/DFO; 37.4% completion-time cut vs GE with UD assistance. DOI pub 17 Oct 2024 / current version 14 Feb 2025 → year 2025 (current-version convention); earlier ICC 2022 version noted.
- [[li-2024-rldc-uav-swarm-clustering]] — Li et al. 2024 (**IEEE WCNC 2024**, `10.1109/WCNC57260.2024.10570678`). **Conference precursor** of the already-curated journal paper [[li-2025-stochastic-game-uav-swarm]] (see duplicate decision). Energy-efficient UAV-swarm MEC with dynamic clustering as **six** coupled multi-agent stochastic games + RLDC Q-learning; **no** NE/convergence proof; 6 authors (NUAA+Concordia); 2500 m × 2500 m region. Own parse has **no** DOI/venue/year line — metadata grounded in the journal version's explicit WCNC-2024 cross-reference (DOI included) + web-confirmed title (arXiv:2402.18936).
- [[zeng-2019-rotary-wing-energy-min]] — Zeng, Xu & Zhang 2019 (**IEEE TWC**, `10.1109/TWC.2019.2902559`, 18(4):2329–2345). Foundational **rotary-wing UAV propulsion-energy model** + energy-minimizing trajectory; fly-hover-communicate (TSPN + convex) and communicate-while-flying (path discretization + SCA). Metadata grounded in the parse's `Digital Object Identifier` line + corpus reference DB (vol/issue/pages).
- [[pervez-2024-acm-multiuav-mec]] — Pervez et al. 2024 (**IEEE TWC**, `10.1109/TWC.2023.3291692`). Multi-UAV + BS MEC weighted energy+latency minimization via three-layer **ACM** (potential-game offloading/server-selection with proven NE + GWF power + SCA trajectory + gradient-descent CPU); ~10–12% cost cut vs two prior joint methods. DOI pub 11 Jul 2023 / current version 12 Mar 2024 → year 2024.
- [[du-2024-gdm-network-optimization-tutorial]] — Du et al. 2024 (**IEEE COMST**, `10.1109/COMST.2024.3400011`). **Tutorial** on generative diffusion models (GDMs) for network optimization, focused on enhancing DRL; case studies on DRL / incentive-mechanism / ISAC / SemCom / IoV; worked sum-rate example. DOI pub 10 May 2024 / current version 22 Nov 2024.
- [[wang-gai-isac-physical-layer]] — Wang et al. (**IEEE Wireless Communications**, `10.1109/MWC.013.2300485`). Overview of **generative AI for ISAC** from the physical-layer perspective; five GAI models (GAN/NF/VAE/DFM/Transformer) + a diffusion **SSG** near-field DoA case study (MSE ≈ 1.03°). **Year: not in parse** (magazine parse has no manuscript-date/volume line); DOI + venue from parse.

### New concept stub (1)

- [[rotary-wing-propulsion-energy-model]] — the closed-form rotary-wing propulsion power model (blade-profile + induced + parasite terms; finite hover power; neither convex nor concave) from [[zeng-2019-rotary-wing-energy-min]], reused as the propulsion reference across the corpus's UAV-MEC energy formulations (e.g. [[li-2024-rldc-uav-swarm-clustering]]).

All other referenced concepts reused existing slugs (e.g. [[stochastic-game]], [[dynamic-uav-clustering]], [[multi-agent-q-learning]], [[intra-swarm-task-delegation]], [[collaborative-dl-inference]], [[dnn-model-partition]], [[pipeline-parallel-inference]], [[elastic-task-scheduling]], [[leo-satellite-edge-computing]], [[lyapunov-optimization]], [[potential-game]], [[nash-equilibrium]], [[alternating-optimization-sdr-sca]], [[generative-diffusion-model]], [[diffusion-model-as-optimizer]], [[integrated-sensing-and-communication]], [[conditional-gan]]).

### Entities — 2 new + roster updates + 1 deferral

- **Created (2):** [[yuben-qu]] and [[hao-sun]] — both **Nanjing University of Aeronautics and Astronautics (NUAA)**, Key Laboratory of Dynamic Cognitive System of Electromagnetic Spectrum Space; each recurs in 2 corpus sources ([[qu-ecoei-uav-swarm]] + [[sun-2024-asap-uav-swarm]]) with identical `@nuaa.edu.cn` emails (`quyuben@`, `sunhaosn@`). Unambiguous, affiliation-consistent (same bar as batch-1's boxiong-wang/hui-kang). Note: Hao **Sun** (NUAA) is distinct from the Jilin/NTU [[geng-sun]] — surname-only collision, no relation implied.
- **Roster updates (existing entities):** [[chao-dong]] (4→5 sources, +eCoEI), [[qihui-wu]] (5→6, +eCoEI), [[jiawen-kang]] (7→10, +eCoEI/+GDM-tutorial/+GAI-ISAC), [[dusit-niyato]] (12→14, +GDM-tutorial/+GAI-ISAC), [[jiacheng-wang]] (5→7, +GDM-tutorial/+GAI-ISAC), [[tony-q-s-quek]] (3→4, +satellite-DOS).
- **Deferred (human confirmation, again):** **Hongyang Du** — lead author of [[du-2024-gdm-network-optimization-tutorial]] (parse defers affiliations to an acknowledgment section not present in the body) and co-author of [[wang-gai-isac-physical-layer]] (lists him at **NTU**). His affiliation has varied across the corpus (NTU vs University of Hong Kong in earlier batches), so — consistent with the batch-2 deferral — **no entity page was minted**; flagged for human confirmation.
- No author-entity links were embedded in source pages (matching the established house convention).

### Duplicate decision — folder #3 (the assigned watch item)

`Energy-Efficient_UAV_Swarm_Assisted_MEC_With_Dynamic_Clustering_and_Scheduling` is **NOT a duplicate** of the already-curated [[li-2025-stochastic-game-uav-swarm]] (raw folder `A_Reinforcement_Learning-Based_Stochastic_Game_...`). It is its **conference precursor**: the journal version (IEEE TGCN, 8 authors, **five** stochastic games, with NE-existence proof + convergence/complexity analysis) explicitly states it "was presented in part at the IEEE WCNC 2024, Dubai, UAE [DOI: 10.1109/WCNC57260.2024.10570678]." The conference paper differs materially — **6 authors** (Li, Chen, Yi, Zhang, Zhu, **Cai**; NUAA + **Concordia**), **six** games (separate leader/follower trajectory games LTSG/FTSG), a larger **2500 m × 2500 m** region, and **no** NE/convergence proof. Curated as a distinct page [[li-2024-rldc-uav-swarm-clustering]] and bidirectionally cross-linked with the journal version.

### Audit (correctness-first)

- **DOI / venue / year** verified against each parse. Five of seven carry a usable metadata line: Cheng/TVT (`Digital Object Identifier 10.1109/TVT.2024.3483203` + manuscript dates), Zeng/TWC (`10.1109/TWC.2019.2902559` + dates + corpus-DB vol/issue/pages), Pervez/TWC (`10.1109/TWC.2023.3291692` + dates), Du/COMST (`10.1109/COMST.2024.3400011` + dates), Wang/MWC (`10.1109/MWC.013.2300485`, DOI only — **no** year line), Qu/MCOM (`10.1109/MCOM.002.2300129`, DOI only — **no** year line). The two IEEE-magazine papers ([[qu-ecoei-uav-swarm]], [[wang-gai-isac-physical-layer]]) have **no manuscript-date/volume line in the parse**, so `year` is left **empty (not in parse)** with the absence noted in each citation; web search did not provide an authoritative parse-overriding year, so none was invented. [[li-2024-rldc-uav-swarm-clustering]] has **no** metadata line at all in its own parse → grounded via the journal version's in-parse WCNC-2024 cross-reference + web-confirmed title.
- **Year convention:** for the TVT/TWC papers whose date-of-publication and date-of-current-version straddle two years, the year follows the date-of-current-version (the wiki's established convention), with both dates recorded in the citation.
- **Grounded headline claims only:** eCoEI FPS figures and the drop/recover behavior are from the parsed Figs. 5–6 (flagged read-from-figure); DOS "37.4% on average vs GE" and "5.72% improvement needs >1.88× energy" are verbatim from the parse; Zeng results stated qualitatively (figure curves, no fabricated magnitudes); Pervez "~10–12% vs [39]/[40]" and "converges in ~9 iterations" verbatim from the parse; Wang SSG "MSE ≈ 1.03°" and CSI "−7.05 dB vs −2.46 dB" verbatim. UAV-swarm-clustering energy-efficiency magnitudes flagged as read from MinerU figure tables (units unlabeled).
- **Wikilink integrity:** Obsidian-faithful wiki-wide check (`.curation-out/linkcheck2.py`, root indexed + inline-code spans stripped) = **ZERO dangling links** after the pass. All wikilinks introduced this batch target existing slugs or pages created/edited in this same batch.
- **Frontmatter:** `type`/`title`/`authors`/`year`/`url`/`venue`/`tags`/`related`/dates/H1 validated via diagnostics on all 7 source pages (the two magazine pages have intentionally empty `year`/`url`-present); `type`/`title`/`tags`/dates/H1 on the 1 concept + 2 entities. No diagnostics issues.
- **Counts reconciled:** **103 sources / 183 concepts / 50 author entities (+[[pytorch]] = 51 entity pages)**. `index.md` and `overview.md` updated to agree.
- **LLM Wiki API:** not queried this batch (headless shell); not required for correctness.
- **Raw-folder scope:** only the 7 assigned `batch3` folders were curated; other untracked `raw/sources/**` folders were intentionally left for their own batch runs.

## 2026-05-31 — Curation pass (batch 2/8: 7 new sources + audit)

Second batch of the deliberately-split 8-batch curation run over 52 newly-ingested raw papers (split to keep context clean and avoid misinformation). This run curated **only** the 7 assigned `batch2` folders (per `.curation-out/batches.json`); the other uncurated folders are owned by separate batch runs and were left untouched. Corpus grows **89 → 96 curated sources**.

### New source pages (7)

- [[lyu-2023-noma-marine-emergency-offloading]] — Lyu et al. 2023 (**IEEE IoT-J**, `10.1109/JIOT.2023.3348164`). NOMA-based UAV emergency communication for marine IoT; MINLP minimizing device computation overhead (time + energy), decomposed into quasi-convex/convex resource allocation + a **coalition formation game** offloading algorithm (CGTO) reaching a Nash-stable solution.
- [[xiang-sac-mapless-robot-navigation]] — Xiang, Li, Dong & Ren (Beihang Univ.). Mapless mobile-robot navigation via **Soft Actor-Critic** with LSTM value/Q networks; laser+target→continuous velocity; Gazebo/ROS Turtlebot3. **Venue / year / DOI: not in parse** (parse has no publication line; an IEEE Xplore record exists for the title but its venue/year are not stated in the parse, so left blank rather than guessed). Foundational SAC entry.
- [[apostolopoulos-2021-prospect-theory-uav-offloading]] — Apostolopoulos et al. 2021 (**IEEE TMC**, `10.1109/TMC.2021.3069911`). Risk-aware partial data offloading across local / ground-MEC / UAV-MEC servers via **prospect theory**; non-cooperative game with proven unique Pure Nash Equilibrium. DOI grounded from an in-parse appendix link + web-confirmed (no header DOI line).
- [[wang-2022-cat-rat-fmec-trajectory]] — Wang et al. 2022 (**IEEE TMC**, `10.1109/TMC.2021.3059691`). Flying-MEC UAV trajectory + user association + resource allocation to minimize total UE energy; **CAT** (BCD convex) and **RAT** (twin-DQN actor-critic + Prioritized Experience Replay + matching). DOI publication 16 Feb 2021, current version 31 Aug 2022 → year 2022 per the current-version convention.
- [[bai-2024-delay-aware-cooperative-edge-cloud]] — Bai et al. 2024 (**IEEE TMC**, `10.1109/TMC.2022.3232375`). Delay-minimizing **cooperative** multi-UAV edge-cloud offloading; convex approximation + Lyapunov online decisions; cooperative-parallel-computing (slowest-node) delay model; model verified on a real UAV-edge platform. DOI publication 27 Dec 2022, current version 8 Jan 2024 → year 2024.
- [[du-2024-d2sac-aigc-asp-selection]] — Du et al. 2024 (**IEEE TMC**, `10.1109/TMC.2024.3356178`). Edge AIGC-as-a-Service provider selection; diffusion decision generator (AGOD) embedded in SAC → **D2SAC**; outperforms 7 DRL baselines. DOI publication 19 Jan 2024, current version 6 Aug 2024 → year 2024.
- [[miao-2022-gaglpp-drone-swarm-iiot]] — Miao et al. 2023 (**IEEE TII**, `10.1109/TII.2022.3196392`). Drone-swarm path planning for Industrial-IoT MEC; ground-station global + onboard local path planning (**GAGLPP**); priority/residual-energy/distance scheduling. DOI publication 4 Aug 2022, current version 4 May 2023 → year 2023.

### New concept stubs (2)

- [[soft-actor-critic]] — base single-agent **SAC** (maximum-entropy off-policy actor-critic), distinct from the existing multi-agent [[masac]]; grounds the navigation, D2SAC, and SAC-SK sources.
- [[prospect-theory]] — risk-aware decision-making under uncertainty (gain/loss value function, loss aversion), grounding the prospect-theoretic offloading game.

All other referenced concepts reused existing slugs (e.g. [[noma]], [[coalition-formation-game]], [[lyapunov-optimization]], [[deep-q-network]], [[prioritized-experience-replay]], [[diffusion-model-as-optimizer]], [[generative-diffusion-model]], [[nash-equilibrium]], [[two-stage-decomposition]], [[matching-theory-for-resource-allocation]], [[load-balancing-uav-mec]], [[parallel-vs-serial-processing]], [[mixed-integer-nonlinear-programming]]).

### Entities — roster updates + 1 deferral (no new entity pages)

- **Roster updates (existing entities):** [[dusit-niyato]] (11→12 sources, +[[du-2024-d2sac-aigc-asp-selection]]), [[jiawen-kang]] (6→7, +d2sac), [[zhu-han]] (4→5, +[[lyu-2023-noma-marine-emergency-offloading]]).
- **Deferred (human confirmation):** **Hongyang Du**, lead/equal-first author of [[du-2024-d2sac-aigc-asp-selection]], recurs in [[ye-2025-aigc-diffusion-contract]], but the two parses list **different affiliations** — d2sac: School of Computer Science and Engineering, **NTU** (`hongyang001@e.ntu.edu.sg`); ye-2025: Department of EEE, **University of Hong Kong** (`duhy@eee.hku.hk`, with a PhD-from-NTU bio). Plausibly the same person after a move, but to stay faithful to the house convention no entity page was minted; flagged here for human confirmation.
- No author-entity links were embedded in source pages (matching the established house convention).

### Audit (correctness-first)

- **DOI / venue / year** verified against each parse. Five of the seven carry a `Digital Object Identifier` line (Lyu/JIOT, Wang/TMC, Bai/TMC, Du/TMC, Miao/TII). [[apostolopoulos-2021-prospect-theory-uav-offloading]] has **no header DOI**, but an in-parse appendix link gives `10.1109/TMC.2021.3069911` (IEEE TMC), web-confirmed against the authors' record. [[xiang-sac-mapless-robot-navigation]] has **no venue/year/DOI in the parse at all**, web search did not authoritatively reveal the venue name/year → left **blank / not in parse** (year field empty, url/venue empty strings), with the absence noted in the citation.
- **Year convention:** for the four TMC/TII papers whose date-of-publication and date-of-current-version straddle two years, the year follows the date-of-current-version (the wiki's established convention), with both dates recorded in each citation line.
- **Grounded headline claims only:** CGTO "lowest computation overhead vs LC/OCG/HOCO/IOJRA/DDPG" (parse Section V); D2SAC "outperforms seven DRL algorithms" with the seven named (DQN/DRQN/Prioritized-DQN/Rainbow/REINFORCE/PPO/SAC) verbatim from the parse; RAT "≈ CAT, generalizes to any take-off point" (parse abstract/Sec. 7); GAGLPP "more offloading services + shorter path + greater energy efficiency" (parse abstract); Bai "near-optimal delay, platform-verified model" (parse abstract/contributions). No figure-only magnitudes were stated as exact.
- **Wikilink integrity:** all wikilinks introduced this batch target existing slugs or pages created in this same batch; two accidental self-referential `related` entries were caught and removed during writing. No NEW dangling links introduced (full wiki-wide check below).
- **Frontmatter:** `type`/`title`/`authors`/`year`/`venue`/`tags`/`related`/dates/H1 present on all 7 source pages (the navigation page's `year` is intentionally empty and `url`/`venue` empty strings = not in parse); `type`/`title`/`tags`/dates/H1 on the 2 concepts.
- **Counts reconciled:** 96 sources / 182 concepts / 48 author entities (+[[pytorch]] = 49 entity pages). `index.md` and `overview.md` updated to agree.
- **LLM Wiki API:** not queried this batch (headless shell); not required for correctness.
- **Raw-folder scope:** only the 7 assigned `batch2` folders were curated; other untracked `raw/sources/**` folders were intentionally left for their own batch runs.

## 2026-05-31 — Curation pass (batch 1/8: 7 new sources + audit)

First batch of a deliberately-split 8-batch curation run over 52 newly-ingested raw papers (split to keep context clean and avoid misinformation). This run curated **only** the 7 assigned folders; the other 45 uncurated folders are owned by separate batch runs and were left untouched. Corpus grows **82 → 89 curated sources**.

### New source pages (7)

- [[zhou-2018-uav-wireless-powered-mec]] — Zhou et al. 2018 (**IEEE JSAC**, `10.1109/JSAC.2018.2864426`). Computation-rate maximization in UAV-enabled wireless-powered MEC; partial + binary offloading; two-stage / three-stage closed-form optimization. Classical-optimization + WPT anchor.
- [[fujimoto-2018-td3-actor-critic]] — Fujimoto, van Hoof & Meger 2018 (**ICML / PMLR 80**; **no DOI in parse**). Origin paper for **TD3** (clipped double-Q, delayed policy updates, target smoothing). Foundational DRL-method entry that grounds the wiki's TD3/MATD3 lineage.
- [[zeng-2019-uav-comm-tutorial-5g]] — Zeng, Wu & Zhang 2019 (**Proceedings of the IEEE**, `10.1109/JPROC.2019.2952892`). Tutorial on UAV communications for 5G+; UAV-assisted-comms vs cellular-connected-UAV taxonomy. Foundational survey anchor.
- [[wang-2025-sac-tma-mec-dc]] — Wang et al. 2025 (**IEEE IoT-J**, `10.1109/JIOT.2025.3542025`). Joint multi-AAV MEC + data collection; SAC + two-phase matching-based association (SAC-TMA). Geng Sun / Jilin-NTU cluster.
- [[chen-2024-three-party-hierarchical-game-pls]] — Chen et al. (**IEEE TWC**, `10.1109/TWC.2023.3322776`; date of publication 16 Oct 2023, date of current version 10 May 2024). Three-party hierarchical game for PLS with dynamic trilateral coalitions; HCSF + DRL.
- [[sun-2025-emoppo-vlh-aerial-cb]] — Sun et al. 2025 (**IEEE TMC**, `10.1109/TMC.2025.3536093`). AAV-swarm collaborative beamforming to a terrestrial mobile user; evolutionary multi-objective PPO (EMOPPO-VLH). Geng Sun / Jilin cluster.
- [[li-2024-emodrl-ground-space-cb]] — Li et al. 2024 (**IEEE JSAC**, `10.1109/JSAC.2024.3459029`). Distributed collaborative beamforming for ground-space (terminal-to-LEO) uplink; EMODRL; saves 30% handover frequency. Geng Sun / Jilin cluster.

### New concept stubs (4)

- [[collaborative-beamforming]] — virtual-antenna-array beamforming (aerial UVAA / distributed DCB / secure CB), tying together the 3 CB sources.
- [[coalition-formation-game]] — cooperative/hedonic coalition games, grounded in the PLS three-party source.
- [[cellular-connected-uav]] — the "UAV as network user" paradigm from the Zeng tutorial, distinct from UAV-as-edge-server.
- [[uav-data-collection]] — UAV-as-data-sink mission pattern, paired with the MEC-DC joint source.

All other referenced concepts reused existing slugs (e.g. [[masac]], [[td3]], [[matching-theory-for-resource-allocation]], [[wireless-power-transfer]], [[binary-vs-partial-offloading]], [[multi-objective-reinforcement-learning]], [[evolutionary-reinforcement-learning]], [[physical-layer-security]], [[gauss-markov-mobility-model]]).

### New entities (2) + roster updates

- **Created:** [[boxiong-wang]] and [[hui-kang]] — both **College of Computer Science and Technology, Jilin University**; each recurs in 2 sources ([[wang-2025-sac-tma-mec-dc]] + the already-curated [[chen-2025-swipt-mec-sac]]) with identical email (`wangbx0320@163.com` / `kanghui@jlu.edu.cn`). Unambiguous, affiliation-consistent.
- **Roster updates (existing entities):** [[geng-sun]] (5→8 sources), [[jiahui-li]] (4→7), [[dusit-niyato]] (8→11), [[jiacheng-wang]] (3→5), [[jiawen-kang]] (4→6), [[zemin-sun]] (3→4), [[qingqing-wu]] (+[[li-2024-emodrl-ground-space-cb]], SJTU-email-matched).
- **Deferred (human confirmation):** a "Qingqing Wu" in [[zeng-2019-uav-comm-tutorial-5g]] is listed at **NUS** (`elewuqq@nus.edu.sg`), while the [[qingqing-wu]] entity is **SJTU** (`qingqingwu@sjtu.edu.cn`). Plausibly the same person earlier in his career, but the affiliation/email differ, so the tutorial was **not** added to his roster — noted on the entity page. No author-entity links were embedded in source pages (matching the established house convention).

### Audit (correctness-first)

- **DOI / venue / year** verified against each parse's `Digital Object Identifier` line (or, for Fujimoto, the ICML/PMLR proceedings line — that parse has no DOI, left as "not in parse"). Years follow the wiki's DOI/publication-year convention. The TWC paper's DOI embeds 2023 but its date-of-current-version is May 2024; year set to 2024 per the current-version convention, with the publication dates noted in the citation.
- **Algorithm-name inconsistency flagged, not hidden:** [[sun-2025-emoppo-vlh-aerial-cb]]'s parse names the method **EMOPPO-VLH** throughout (title/abstract/algorithm/complexity), but one intro sentence calls it "MOPPO-PLE". The page uses EMOPPO-VLH (dominant in-parse name) and notes the discrepancy rather than inventing a reconciliation.
- **Grounded headline numbers only:** the ground-space CB "saves 30% handover frequency" is stated verbatim in [[li-2024-emodrl-ground-space-cb]]'s abstract; CB received-power "∝ square of the number of AAVs" is from [[sun-2025-emoppo-vlh-aerial-cb]]; the Zeng tutorial's 3GPP link figures (60–100 kb/s CNPC, up to 50 Mbps payload, $10^{-3}$ PER, 50 ms) are from its Table 1. No figure-only numbers were stated as exact.
- **Wikilink integrity:** all wikilinks introduced this batch target existing slugs or pages created in this same batch; no NEW dangling links introduced. (Full wiki-wide Obsidian-faithful check run after writing — see verification below.)
- **Frontmatter:** `type` / `title` / `authors` / `year` / `venue` / `tags` / `related` / dates / H1 present on all 7 source pages; `type`/`title`/`tags`/dates/H1 on the 4 concepts + 2 entities.
- **Counts reconciled:** 89 sources / 180 concepts / 48 author entities (+[[pytorch]] = 49 entity pages). `index.md` and `overview.md` updated to agree.
- **LLM Wiki API:** not queried this batch (headless shell); not required for correctness.
- **Raw-folder scope:** only the 7 assigned folders were curated; the other 45 untracked `raw/sources/**` folders were intentionally left for their own batch runs.

## 2026-05-31 — Audit & coverage pass (no new raw papers)

Maintenance pass over the existing 82-source corpus. No new papers were curated. Focus: re-verify correctness end-to-end (DOIs/venues, ungrounded numbers, link integrity), broaden the analytical layer where the corpus already supports it, and reconcile a stale derived count in the meta-docs.

### Correctness audit

- **Misattributed DOI fixed (the pass's main correctness find).** [[huang-2025-cmop-dispersed-computing]] carried `url`/`venue` = `10.1109/TEVC.2025.3569722` / *IEEE Trans. Evolutionary Computation*. That DOI is **not** this paper's — it is the DOI of **reference [8]** in huang-2025's own reference list, namely the Wang/Guo/Liu/Wang **ACVE** paper (verbatim title + all four authors match; cross-checked against Bing-Chuan Wang's publication record by web search, verification-only). huang-2025's own parse has **no `Digital Object Identifier` line**, so its venue/DOI were reset to `not in parse` with a corrective note.
- **ACVE metadata now grounded within the corpus.** As a consequence, [[wang-acve-constraint-violation-cmop]] — whose own parse also lacks a DOI line and was previously `not in parse` for venue/year/DOI — is now grounded by huang-2025's reference [8]: *IEEE Transactions on Evolutionary Computation*, early access, `doi:10.1109/TEVC.2025.3569722`, 2025. Frontmatter + citation updated with a provenance note.
- **3 genuinely-missing DOIs added**, each grounded in its own parse's `Digital Object Identifier` line: [[hao-2025-priority-aware-task-driven-co]] (`10.1109/TWC.2025.3564356`, IEEE TWC), [[zhang-2025-mcma-task-migration]] (`10.1109/TMC.2025.3539945`, IEEE TMC), [[zhang-2025-ssac-mgi-heterogeneous-uav]] (`10.1109/TMC.2025.3632884`, IEEE TMC). Venues follow the wiki's DOI-prefix → journal convention (TWC/TMC), consistent with sibling pages.
- **ACBFT "96.2% throughput" restored as grounded (prior-pass correction).** The 2026-05-30 pass had softened [[wang-2025-acbft-uav-consensus]] and flagged the 96.2% figure as *not in parse*. That was wrong: the figure is stated verbatim in the paper's contributions list (parse L35 — *"ACBFT achieves an increase in throughput of up to 96.2%…"*). Restored the claim with the L35 quote + a metadata note explaining the correction.
- **Headline numbers re-verified.** The 4 findings added in the prior pass were re-checked against their parses and all hold: maritime 39.3% energy saving (L165), FedLEO 41% delay / 9.39% accuracy (L39), ASAP 92.66% latency cut (L161, hardware-validated), MASAC +15.41% sensing / −30.73% queue-delay vs MADDPG (L725/L709 — the MADDPG-vs-PSO ordering confirmed correct). Note: MinerU renders some percentages with intra-number spaces (`1 5 . 4 1 %`), which can fool naive grep — verified by reading the parse lines directly.
- **Remaining no-DOI source pages confirmed legitimately blank:** [[bi-2025-sg-mapg]], [[peng-2025-drudm-cfg]], [[liu-2026-jppo-en-convntm]], [[du-2024-distributed-foundation-models-6g]] — none has a `Digital Object Identifier` line in its parse; left `not in parse`.
- **Wikilink integrity:** Obsidian-faithful wiki-wide check (root `purpose.md` indexed; inline-code spans + table-escaped `\|` aliases stripped) = **ZERO dangling links** after the pass. Orphans = only `README.md` and `schema.md` (repo-root structural docs with no wikilinks — expected, not errors).
- **Frontmatter:** `type`/`title`/`tags`/dates/H1 + `related` validated on every touched/new page; no self-references, no duplicate `related` entries.
- **Graph stats (file-derived):** 346 nodes / 5071 resolved edges (up from 336 / 4932 at the start of the pass). The LLM Wiki API was **not** reachable for authoritative graph stats — `GET /health` returned `authConfigured:true, allowUnauthenticated:false` and the graph endpoint returned **401** in this headless shell (no `LLM_WIKI_API_TOKEN`), the documented headless case. Fell back to the local file/search tools throughout; correctness grounded in the parses and committed files.

### Meta-doc reconciliation

- **Stale reference count fixed.** `index.md` and `overview.md` both said the reference DB held **1567** unique refs; the scout-owned [[reference-database]] now reports **2981** (its `Generated: 2026-05-30` summary). Updated both meta-docs to 2981. The scout's `wiki/references/**` files were **not** modified.
- **Counts reconciled to exact verified numbers:** 82 sources / 176 concepts / **47 entities** (46 authors + [[pytorch]]) / **12 findings** / **10 synthesis** / 4 comparisons / 2 methodology / 4 queries / 1 thesis. `index.md` and `overview.md` agree; every page on disk is indexed and every index link has a backing page.
- **`log.md`** already consolidated in the prior pass (the 89 automated "external batch delete" events live under [Raw-source housekeeping](#raw-source-housekeeping)); this pass only prepended this entry. Verified mojibake-free at the byte level (em-dashes/curly quotes intact) — meta-docs were edited with the file tools, never PowerShell redirection.

### Coverage added (analytical layer)

- **Findings (+1 → 12):** [[acbft-throughput-increase]] — up to 96.2% consensus-throughput increase vs existing chaining protocols, grounded at [[wang-2025-acbft-uav-consensus]] parse L35 (the finding deferred in the prior pass, now mintable because the number is confirmed in-parse).
- **Synthesis (+1 → 10):** [[blockchain-on-edge-trust-layer]] — maps the 3 blockchain-on-edge sources ([[mao-2025-bcsa-frl]], [[qin-2025-bcuav-masac]], [[wang-2025-acbft-uav-consensus]]) by **which layer the chain defends** (consensus-protocol / aggregation / audit). Complements the existing pairwise [[bcsa-frl-vs-bc-uav-masac]] comparison by adding the consensus-layer source.

### Entity coverage (+8 → 47)

Computed author recurrence across all 82 source pages and verified affiliations against the parses (author-bio + correspondence lines). **Created 8 entity pages** where the identity is unambiguous and affiliation-consistent:

- [[shuang-liang]] — Northeast Normal Univ.; identical email `liangshuang@nenu.edu.cn` across all 3 sources ([[chen-2025-swipt-mec-sac]], [[sun-2024-mvtora-postdisaster-vfc]], [[wang-2025-lae-network-survey]]); [[geng-sun]] aerial-MEC/LAE cluster.
- [[weifeng-zhong]] & [[shengli-xie]] — Guangdong Univ. of Technology, School of Automation (`wfzhongs@gdut.edu.cn` / `shlxie@gdut.edu.cn`); CMOP-evolutionary lineage with [[xumin-huang]] / [[jiawen-kang]] / [[chaoda-peng]].
- [[qiqi-xie]] — South China Agricultural Univ., College of Mathematics & Informatics; both sources ([[wu-2026-terrain-aware-uav-mec]], [[xie-2026-uav-multisource-fusion]]); previously a lower-priority candidate, now confirmed.
- [[nei-kato]] (Tohoku Univ., identical email), [[jiadai-wang]], [[yijie-xun]], [[yangbo-liu]] (all Northwestern Polytechnical Univ., the integrated aero-space-ground-ocean lab) — the [[bomin-mao]] NTN cluster, stable across [[mao-2024-ntn-hierarchical-caching-cav]] + [[mao-2025-bcsa-frl]].

**Still deferred (not created):** "Nan Zhao" (genuine namesake — Hubei Univ. of Technology vs Dalian Univ. of Technology, different emails). Lower-priority cross-cutting seniors with topically-divergent 2-source pairs (Mohsen Guizani, Dong In Kim) and tight-cluster 2-source co-authors (Hongbin Chen / Fangqing Tan, Guangxu Zhu) left as candidates for a future pass — affiliation-plausible but not minted this pass to avoid over-linking.

### Raw-folder reconciliation

84 raw folders vs 82 source pages. The 2 unmatched folders are again confirmed **duplicate MinerU ingests** (space-named variants) of already-curated papers — `Optimizing Spectrum Sharing in UAV Swarms…` (= [[wang-2025-uav-swarm-stackelberg]]) and `UAV-Enabled Multi-Source Data Fusion…` (= [[xie-2026-uav-multisource-fusion]]); byte-identical titles/abstracts. No uncurated paper exists, so nothing was routed to `mec-wiki-curator`.

## 2026-05-30 — Audit, refinement & coverage-expansion pass

Full audit + refinement pass on the existing 82-source corpus (no new raw papers). Focus: tidy the meta-docs, broaden the analytical layer, resolve deferred author identities, and re-verify correctness end-to-end.

### Meta-doc cleanup

- **`log.md`** de-noised and reordered. The 89 automated "external batch delete" blocks (machine-generated raw-artifact prune events, ~386 files, **0 wiki pages** ever deleted) were consolidated into the single [Raw-source housekeeping](#raw-source-housekeeping) section at the foot of the file. Entries reordered strictly newest-first; date headers normalized to `## YYYY-MM-DD — <title>`. File shrank from 1184 lines to a readable curation/audit history.
- **`index.md`** de-duplicated. Removed the second copy of the "Joint trajectory / caching / migration" source section; gave each of the 4 cross-listed sources ([[zhu-2025-lycnn-drl-wpt-mec]], [[wu-2025-iopo-irs-uav-thz-mec]], [[chen-2024-ulse-game]], [[hao-2025-priority-aware-task-driven-co]]) a single primary home with a `>` cross-reference note where useful; de-duplicated the three twice-listed concepts ([[generative-ai-for-mec]], [[edge-user-allocation]], [[collaborative-dl-inference]]); folded the single-item "Generic offloading techniques" section into "Compute offloading & DRL"; added the previously-unindexed [[j-ppo-en-convntm]] concept. Verified all 82 source / 176 concept / 34 entity pages resolve and are indexed.
- **`overview.md`** reconciled to exact counts (82 / 176 / 34), refreshed the analytical-layer line, and noted the new derived pages.

### Coverage expansion (analytical layer)

- **Findings (+4 → 11):** [[maritime-three-tier-energy-saving]] (39.3% energy saving, [[zhang-2025-three-tier-maritime-offloading]] — grounded verbatim in the parse abstract); [[fedleo-delay-accuracy-tradeoff]] (up to 41% delay reduction / 9.39% accuracy gain, [[zhai-2023-fedleo-decentralized-fl]] — grounded in the parse abstract + per-dataset breakdown); [[asap-swarm-inference-speedup]] (up to 92.66% computing-latency reduction vs raw-data offloading, hardware-validated on 24 airborne computers + 5 UAVs, [[sun-2024-asap-uav-swarm]]); [[masac-beats-maddpg-sensing-queue]] (+15.41% sensing rate / −30.73% queue delay vs MADDPG, [[qin-2025-bcuav-masac]] — grounded at parse L709/L725).
- **Synthesis (+3 → 9):** [[sagin-satellite-offloading-landscape]] (8 SAGIN/satellite sources); [[isac-sensing-in-aerial-mec]] (7 ISAC/sensing sources); [[maritime-mec-architectures]] (7 maritime sources).
- **Comparisons (+1 → 4):** [[game-theoretic-offloading-formulations]] (potential vs Stackelberg vs bargaining vs matching, across the game-theoretic sources).
- **Queries (+2 → 4):** [[query-when-does-dro-beat-drl-for-csi-uncertainty]]; [[query-video-vs-cooperative-perception-offloading-shape]].
- **Methodology (+1 → 2):** [[ao-sdr-sca-convex-pipeline]] (the alternating-optimization + SDR + SCA convex pipeline recurring across the ISAC/secure-beamforming sources).

Every new page grounds its claims in specific parses; figure-derived or unlabeled magnitudes are flagged indicative. A planned ACBFT-throughput finding was **dropped**: the "96.2% throughput" figure is **not in the [[wang-2025-acbft-uav-consensus]] parse** (see Correctness audit below), so no finding was minted on an ungrounded number.

### Entity coverage (+5 → 39)

Re-examined the 5 deferred namesake-risk authors against parse affiliations (first ~40 lines of each source). **Created 5 entity pages** where the identity proved unambiguous and affiliation-consistent; **kept 1 deferred** as a genuine namesake.

- **Created:**
  - ying-chen — Beijing Information Sci. & Tech. Univ.; `chenying@bistu.edu.cn` identical across [[chen-2023-dotora-air-ground-online]] and [[chen-2024-ulse-game]] (shared co-authors [[yuan-wu]] + Jiwei Huang).
  - [[jie-xu]] — CUHK-Shenzhen (SSE); consistent ISAC affiliation across [[meng-2024-uav-isac-overview]] and [[yao-2025-secure-isac-dual-eavesdropping]].
  - [[fuhong-song]] — first author of [[song-2022-emorl-tcto-uav]] (SWJTU) and [[song-2024-mol-aoi-energy]] (Guizhou Univ. of Finance & Economics); a student→faculty move confirmed by the shared co-author Huanlai Xing (`hxx@home.swjtu.edu.cn` in both) and the shared evolutionary-MORL niche.
  - [[yong-wang]] — School of Automation, Central South Univ.; `ywang@csu.edu.cn` **identical** in both [[wang-2019-todetas-deployment-scheduling]] and [[wang-acve-constraint-violation-cmop]] (the shared email overrides the earlier "different topics" deferral).
  - [[wei-zhang]] — Shandong Computer Science Center (Nat'l Supercomputer Center in Jinan); identical lab + identical co-author roster ([[hao-hao]], Changqiao Xu, Shujie Yang, Gabriel-Miro Muntean) across [[hao-2024-clp-multiuav-priority-offloading]] and [[hao-2025-priority-aware-task-driven-co]].
- **Still deferred (genuine namesake — do NOT merge):** "Nan Zhao" — [[zhao-2022-matd3-multiuav-ec-offloading]] is **Hubei Univ. of Technology** (`nzhao@mail.hbut.edu.cn`, Member) while [[zhang-2025-gan-td3-isac-active-ris]] is **Dalian Univ. of Technology** (`zhaonan@dlut.edu.cn`, Senior Member). Different institutions and emails → two different people; no entity created.

### Correctness audit

- **Raw-folder reconciliation:** 84 raw folders vs 82 source pages. The 2 unmatched folders are confirmed **duplicate ingests** (space-named MinerU variants) of already-curated papers — `Optimizing Spectrum Sharing in UAV Swarms...` (= [[wang-2025-uav-swarm-stackelberg]], curated from the underscore-named folder) and `UAV-Enabled Multi-Source Data Fusion...` (= [[xie-2026-uav-multisource-fusion]]). Byte-identical titles/abstracts; no uncurated paper. No action beyond noting it here.
- **Ungrounded-number fixes (2 found):**
  1. [[wang-2025-acbft-uav-consensus]] asserted "increases throughput by up to **96.2%**" — that figure is **not in the parse** (only image references + a generic "higher throughput" statement at L37) and is not web-confirmable for this paper. Softened the source page to the parse-supported claim (chain propagation trades latency for higher throughput; Fig. 6 shows ACBFT leading other BFT protocols at `N=3f+1`) and explicitly flagged "96.2%" as not in parse.
  2. [[maddpg-vs-masac-in-mec]] and [[bcsa-frl-vs-bc-uav-masac]] quoted "+13.16% sensing / −29.47% queue delay" as the margin **vs MADDPG**. The parse (qin-2025-bcuav-masac L709/L725) shows those are the **PSO** comparison figures; the margins **vs MADDPG** are **+15.41% / −30.73%**. Corrected both pages.
- **Wikilink integrity:** Obsidian-faithful wiki-wide check (root `purpose.md` indexed, inline-code spans + table-escaped `\|` aliases handled) = **ZERO dangling links** after this pass (the new derived pages were forward-referenced from the log, then created).
- **DOI / venue spot-checks:** sampled source pages re-verified against parses; the only metadata issue found was the ACBFT throughput number above (a claim, not a venue/DOI error — DOI `10.1109/TVT.2025.3548281` and venue IEEE TVT are correct).
- **Frontmatter:** `type` / `title` / `tags` / dates / H1 validated via diagnostics on every page created or edited this pass.
- **LLM Wiki API:** not queried (headless shell); not required for correctness.

## 2026-05-29 — Follow-up cleanup pass (dangling links + author identities + references)

Scoped cleanup pass (no new sources curated). Three tasks:

### Task 1 — dangling wikilink resolution (now ZERO real dangling links)

- **`[[hp-mobility-models]]`** in [[liu-2026-jppo-en-convntm]] (System model table, IoT-mobility Reference cell) → replaced with **`[31]`**. Grounded in the parse (`raw/sources/Multi-UAV_Path_Planning_for_Mobile_Edge_Computing_With_High-Density_Mobile_Devices/full.md`, "Gauss-Markov (GM) mobility model … as [31]"), matching the bracketed-cite style of the other rows (`[5], [32]`, `[10]`, `[33]`). No `hp-mobility-models` page was invented.
- **`[[fairness-metrics-in-mec]]`** in [[peng-2025-drudm-cfg]] → **created** `wiki/concepts/fairness-metrics-in-mec.md` as a synthesis concept tying together the existing fairness vocabulary ([[jains-fairness-index]], [[theil-fairness-index]], [[spatial-equity-index]], [[service-experience-ratio]], [[energy-balancing-uav]]) and grounded in how the corpus uses them (liu-2026 Jain-style f_n in [[equilibrium-efficiency-metric]]; peng-2025 Theil regularizer; he-2023 fairness-among-UAVs; gao-2024 service-experience ratio). Dropped the "when that page exists" qualifier in the peng-2025 sentence.
- **`[[purpose]]`** in [[high-density-mobile-device-scenarios]] — **FALSE POSITIVE, left as-is.** Verified `purpose.md` exists at repo root and is indexed in `.llm-wiki/file-snapshot.json` (`purpose.md`, size 816). Obsidian resolves `[[purpose]]` by basename to the root file, so the link is valid. The earlier "dangling" report came from a `wiki/`-scoped integrity checker that does not index repo-root files.
- **Integrity re-check:** an Obsidian-faithful re-check (root indexed + inline-code spans stripped) reports **NO DANGLING LINKS**. The two real dangling links are fixed; the third was never real.

### Task 2 — deferred author identities confirmed (21 created, 5+ deferred)

Computed author recurrence across all 82 source pages and verified affiliations against each paper's parse (first ~40 lines). **Created 21 entity pages** for recurring authors whose identity is unambiguous and affiliation-consistent across their sources (schema mirrors [[geng-sun]]):

- Jilin-University / NTU aerial-MEC cluster: [[zemin-sun]], [[jiahui-li]] (Jilin Univ), [[jiacheng-wang]], [[dusit-niyato]] (NTU), [[qingqing-wu]] (Shanghai Jiao Tong Univ).
- NUAA aerial-computing cluster: [[ziye-jia]], [[chao-dong]], [[qihui-wu]] (NUAA), [[zhu-han]] (Univ of Houston / Kyung Hee).
- Dalian-Maritime-University maritime cluster: [[bin-lin]] (DMU), [[zhen-wang]] (DMU / Dalian Neusoft — same email `wangzhen_jsj@neusoft.edu.cn` across all 3 papers confirms one identity despite the common name), [[qiang-ye]] (Univ of Calgary).
- NWPU non-terrestrial-network cluster: [[bomin-mao]], [[hongzhi-guo]], [[jiajia-liu]] (Northwestern Polytechnical Univ, `@nwpu.edu.cn`).
- NCEPU aerial-edge cluster: [[peng-qin]], [[yang-fu]] (North China Electric Power Univ, `qinpeng@ncepu.edu.cn`); [[jingjing-wang]] (Beihang Univ, `drwangjj@buaa.edu.cn` — shared email confirms one identity).
- SCAU evolutionary UAV-MEC cluster: [[zexiong-wu]] (South China Agricultural Univ).
- Cross-cutting seniors: [[chunxiao-jiang]] (Tsinghua, `jchx@tsinghua.edu.cn`), [[tony-q-s-quek]] (SUTD, `tonyquek@sutd.edu.sg`).

Updated [[geng-sun]] to note its previously-deferred co-authors now have confirmed pages.

**Deferred — needs human confirmation** (not created at the time):

- **Yong Wang** (wang-2019-todetas, wang-acve) — common name; the ACVE paper is an evolutionary-computation work, wang-2019 is a different topic/affiliation; no shared affiliation in the parses.
- **Nan Zhao** (zhao-2022-matd3, zhang-2025-gan-td3-isac) — zhao-2022's Nan Zhao is at Hubei Univ of Technology; the zhang-2025 Nan Zhao affiliation is not confirmed identical → namesake risk.
- **Wei Zhang** (hao-2024, hao-2025) — extremely common name; affiliation not verified.
- **Ying Chen** (chen-2023-dotora, chen-2024-ulse-game) — common name; affiliation not verified this pass. *(Resolved 2026-05-30: shared `bistu.edu.cn` email → entity created.)*
- **Jie Xu** (meng-2024-uav-isac-overview, yao-2025-secure-isac) — common name; both point to CUHK-Shenzhen + ISAC. *(Resolved 2026-05-30: entity created.)*
- Lower-priority 2-source co-authors with consistent affiliation (candidates for a future pass, not ambiguous): Qiqi Xie (SCAU), Yijie Xun / Jiadai Wang / Yangbo Liu (NWPU), Nei Kato (Tohoku).

Cross-linking convention: entity→source links live in each entity page's `related` + roster (Obsidian auto-generates the backlinks); existing source pages do not embed author-entity links, so none were added, matching the established [[geng-sun]] pattern.

### Task 3 — references files committed

Staged and committed the prior reference-scout outputs: `wiki/references/recommendations.md`, `wiki/references/reference-database.json`, `wiki/references/reference-database.md`. Scanned for secrets/tokens — none present. Added a **References** section to `wiki/index.md` linking [[reference-database]] and [[recommendations]].

### Audit

- **Frontmatter:** validated `type`/`title`/`tags`/dates/H1 on all touched pages (1 concept + 21 entities + 2 sources + index + overview) via diagnostics — no issues.
- **Wikilink integrity:** Obsidian-faithful check = **NO DANGLING LINKS**. Pre-existing dangling links eliminated: `hp-mobility-models` (fixed) and `fairness-metrics-in-mec` (created); `purpose` confirmed as a valid root-file link.
- **Counts reconciled:** 82 sources, 176 concepts, 34 entity pages (33 authors + pytorch) — matched `overview.md` at the time.
- **LLM Wiki API:** not queried this pass (headless shell); graph stats unavailable — not required for correctness.

## 2026-05-29 — Curation pass (batch 4: 43 new sources + audit)

Curated all 43 newly-ingested raw papers (corpus 39 → 82 sources). Metadata extracted faithfully from each MinerU parse; DOIs/venues verified against the parse text. Year convention follows the existing wiki (DOI-embedded year).

- **New source pages (43):** [[he-2019-euagame-user-allocation]], [[mao-2017-mec-survey-communication]], [[wang-2025-acbft-uav-consensus]], [[wang-acve-constraint-violation-cmop]], [[sun-2023-bargain-match-vec]], [[faisal-2025-cgan-ris-isac-channel]], [[kang-2023-mappo-hierarchical-aerial]], [[du-2024-distributed-foundation-models-6g]], [[wang-2025-double-edge-samin]], [[chen-2023-dotora-air-ground-online]], [[zhang-2025-three-tier-maritime-offloading]], [[song-2022-emorl-tcto-uav]], [[he-2023-fairness-3d-multiuav-maddpg]], [[zhai-2023-fedleo-decentralized-fl]], [[zhang-2025-gan-td3-isac-active-ris]], [[khoramnejad-2025-gai-wireless-optimization-survey]], [[jia-2022-hierarchical-aerial-matching]], [[wang-2024-hybrid-oma-noma-sagin]], [[tang-2024-iscc-uav-feel]], [[you-2025-uncertain-maritime-hasac]], [[zhang-2019-uav-iot-comp-comm]], [[zhao-2024-caching-service-placement-uav]], [[wang-2019-todetas-deployment-scheduling]], [[chen-2025-swipt-mec-sac]], [[sun-2024-mvtora-postdisaster-vfc]], [[yu-2020-uav-ec-collaborative-offloading]], [[qin-2025-matd3-noma-queue-sagin]], [[du-2023-maddpg-service-placement-agin]], [[albakhrani-2025-moalf-uav-mec]], [[zhang-2024-dlrl-maritime-usv]], [[zhao-2022-matd3-multiuav-ec-offloading]], [[zhang-2024-gdmtd3-aerial-secure-cb]], [[guo-2023-mccco-multiuav-5g-offloading]], [[mao-2024-ntn-hierarchical-caching-cav]], [[yang-2022-stochastic-uav-mec-lyapunov]], [[fu-2025-otae-inference-lae-batching]], [[liu-2022-miso-uav-mec-trajectory]], [[chang-2022-marl-multiuav-trajectory]], [[li-2025-twohop-airground-drl-offloading]], [[wang-2024-twotier-satellite-marine]], [[zhang-2024-uav-task-offloading-ddpg]], [[meng-2024-uav-isac-overview]], [[yao-2025-secure-isac-dual-eavesdropping]].
- **New concept stubs (17):** [[edge-user-allocation]], [[byzantine-fault-tolerant-consensus]], [[particle-swarm-optimization]], [[constraint-violation-evaluation]], [[bargaining-game]], [[conditional-gan]], [[generative-adversarial-network]], [[mappo]], [[decentralized-federated-learning]], [[integrated-sensing-computation-communication]], [[heterogeneous-agent-rl]], [[differential-evolution]], [[vehicle-fog-computing]], [[non-terrestrial-network]], [[ant-colony-optimization]], [[over-the-air-computation]], [[distributed-foundation-models]]. All other referenced concepts reused existing slugs.
- **New entity (1):** [[geng-sun]] — Jilin University, confirmed consistent across 5 sources. Other recurring batch-4 authors (Zhen Wang / Bin Lin maritime cluster, Ziye Jia / Chao Dong / Zhu Han aerial cluster, Peng Qin / Yang Fu) deferred for human identity confirmation rather than minting/merging entities.
- **Navigation:** refreshed `wiki/index.md` (new groupings: Foundational surveys & overviews, Classical/convex optimization UAV-MEC, Game-theoretic offloading & allocation, Multi-UAV cooperative computing & deployment, Pure optimization methods, ISAC/sensing/PLS; plus GAI / maritime / hierarchical additions and the 17 new concepts) and `wiki/overview.md` (counts 39 → 82, expanded track table, corrected hardware-validated count).

### Audit (correctness-first)

- **DOI / venue / year:** verified against each parse's `Digital Object Identifier` line; year set to the DOI-embedded year per existing wiki convention.
- **`not in parse` handling:** [[wang-acve-constraint-violation-cmop]] — venue, year, and DOI genuinely absent from the parse and unconfirmable by web search (author homepage lists no matching publication); left blank / `not in parse` rather than guessed. [[du-2024-distributed-foundation-models-6g]] — DOI absent from parse; venue "IEEE Wireless Communications" web-confirmed; DOI left empty.
- **Claims:** headline numbers reproduced only where explicit in the parse (e.g. ACBFT "up to 96.2% throughput increase", FedLEO "up to 41% delay / 9.39% accuracy", three-tier maritime "39.3% energy saving"). Figure/abstract-derived numbers (e.g. MOALF percentages) flagged as indicative.
- **Wikilink integrity:** wiki-wide check shows **no NEW dangling links**. Pre-existing dangling links remained and were reported: `[[fairness-metrics-in-mec]]`, `[[hp-mobility-models]]`, `[[purpose]]` (all resolved in the 2026-05-29 follow-up pass).
- **Frontmatter:** `type` / `title` / `tags` / dates / H1 validated on touched pages via diagnostics (no issues).
- **LLM Wiki API:** not queried this pass (headless shell); graph stats unavailable — not required for correctness.

## 2026-05-29 — Audit pass (batch-3 verification)

Correctness-first audit of the 13 batch-3 source pages and refreshed navigation:

- **DOIs verified against parses.** All 13 new source DOIs cross-checked against `Digital Object Identifier` lines in their `full.md`. Two needed manual confirmation because a regex first-match picked up a precursor/reference DOI: [[li-2025-stochastic-game-uav-swarm]] (parse confirms `10.1109/TGCN.2024.3424449`; the WCNC 2024 `10570678` is a conference precursor) and [[shao-2024-drl-antijamming-mec]] (parse confirms `10.1109/TMC.2024.3432491`; the GLOBECOM 2023 hit was a reference). Both page DOIs are correct.
- **Frontmatter valid** on all 39 source pages (`type/title/authors/year/venue/tags/related/created/updated` + H1 present).
- **Wikilink integrity:** no NEW dangling links introduced by this batch. The only unresolved targets remained the three pre-existing ones (`fairness-metrics-in-mec`, `hp-mobility-models`, `purpose`).
- **Counts reconciled:** 39 sources, 158 concepts, 12 entities — matched `overview.md`.
- Created a reusable workspace agent `.kiro/agents/mec-wiki-curator.md` to standardize this curate-then-audit workflow for future raw-paper drops.

## 2026-05-29 — Curation pass (batch 3: 13 new sources)

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

### What this changed about the corpus

- **Corpus size:** 26 → 39 curated sources.
- **New tracks:** SAGIN/satellite offloading (4), UAV-swarm collaborative computing (2), game-theoretic offloading (now spans potential/stochastic/Stackelberg games), generative-AI MEC (2), anti-jamming security-DRL (1).
- **First hardware-validated sources** enter the corpus: [[sun-2024-asap-uav-swarm]] and [[shao-2024-drl-antijamming-mec]].
- **New formulation families:** potential/stochastic games + Nash-equilibrium analysis, multi-objective RL (vectorial reward), contract theory, IRS/THz channels, in-swarm collaborative DL inference, federated learning over SAGIN.
- **Diffusion-as-optimizer** now has two sources ([[ye-2025-aigc-diffusion-contract]], [[peng-2025-drudm-cfg]]).

### Issues flagged for follow-up

- **Synthesis refresh overdue.** The synthesis/findings/thesis pages still reflected the 26-source view at the time.
- **Figure-derived numbers:** several magnitudes in [[li-2025-stochastic-game-uav-swarm]] and [[han-2024-sagin-fl-handover]] were read from MinerU-parsed figure tables with unlabeled axes — treat as indicative trends; verify against the PDFs before citing exactly.

## 2026-05-29 — Deep synthesis audit (26-source era)

Read each new synthesis page paragraph by paragraph and cross-checked every factual claim against the underlying papers. Found seven concrete corrections plus several softening edits.

### `cmop-evolutionary-uav-mec-lineage`

- **Overclaim: "B-spline trajectory ... in every paper".** Verified against papers: only [[peng-2022-cmop-uav-path-planning]] and [[wu-2026-terrain-aware-uav-mec]] (the trajectory-design entries) actually use B-splines. [[huang-2023-mu-aec-task-energy]] (DAG scheduling), [[peng-2024-energy-time-uav-its]] (UAV-ITS), [[huang-2025-cmop-dispersed-computing]] (dispersed computing), [[xie-2026-uav-multisource-fusion]] (cooperative perception) don't have a UAV path to plan. Demoted B-spline to "trajectory-subset's shared tool, not a lineage-wide constant".
- **Overclaim: "CMOEA/D-CDP backbone in every paper".** Verified: peng-2022, huang-2023, peng-2024, huang-2025 use CMOEA/D-CDP; xie-2026 extends NSGA-II for the dynamic CMOO setting; wu-2026 uses a multi-tasking dual-population scheme with the constrained-domination principle but not strictly CMOEA/D-CDP. Softened to "CMOEA family backbone — even where the specific framework shifts" with the framework breakdown spelled out.
- **Overclaim: "Compare against the previous lineage entry plus 1-2 external baselines (typically ToP, PPS, NSGA-II, NSGA-III)".** Verified the actual baselines: peng-2022 used ToP, PPS; huang-2023 added NSGA-II; peng-2024 only PPS; huang-2025 used CCMO/BiCo/CMaO/CTAEA (none of those four); xie-2026 used NSGA-II/C-NSGA/C-MOEA; wu-2026 used CMOEMT/URCMO/ICMA/DPPPS. The lineage entries do *not* run head-to-head against each other on a common benchmark. Rewrote the template step to reflect "compare against external CMOEA baselines of the relevant generation" with explicit naming.
- **Overclaim: "All entries run 10^4-10^5 function evaluations".** Only [[peng-2022-cmop-uav-path-planning]] explicitly states 3x10^4 FE. The others report only generations x population. Softened.
- **Overclaim: "all reporting Pareto-front improvements over both DRL-style and prior-CMOEA baselines".** None of the lineage papers compares against a DRL controller. Removed the "DRL-style" half. Confidence on the working thesis reduced from "high" to "medium-high" with the caveat made explicit.
- **Inheritance graph: speculative.** Verified citations: peng-2024 cites peng-2022; huang-2025 cites peng-2022 but does **not** cite peng-2024 directly. Rewrote the graph caption to mark it as interpretive (technique reuse via shared authors), not direct citation.

### `hierarchical-aerial-mec-design-space`

- **Off-by-one: "Two of five (`bao-2025`, `nabi-2025`, `peng-2025`) use DRL".** That's three sources, not two. Fixed.
- **Wrong: "[[jia-2025-dro-uav-hap-mec]] optimizes trajectory jointly with offloading via WKD pre-stage".** WKD is a one-shot UAV deployment scheme; UAVs are quasi-stationary after deployment. So jia-2025 has placement, not trajectory. Reclassified as "in between" — placement, not full trajectory — with the distinction spelled out.
- **Stale "four-source roster" / "the four sources".** The roster has five sources. Updated to "five-source roster" everywhere.
- **Misleading objective table: jia-2025 latency = (chance-constraint), energy = checked.** The chance constraint *is* on latency, while energy is the actual sole objective. Clarified the cell to make this unambiguous.

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
- 3 dangling wikilinks remained (hp-mobility-models, fairness-metrics-in-mec, purpose) — all pre-existing, none introduced or worsened by the audit.

## 2026-05-29 — Audit pass (three corrections, 26-source era)

Reviewed all 14 new source pages against the parsed papers. Three issues found, all fixed:

### bao-2025-ddpg-video-offloading

- **Venue was wrong.** I had marked it as "Journal of Supercomputing / Cluster Computing (Springer; preprint, accepted Sep 2025)" because the MinerU parse didn't capture publication metadata. The actual venue is **Complex & Intelligent Systems** (Springer), DOI `10.1007/s40747-025-02106-1`. Confirmed via web search of the title; updated frontmatter and citation.
- **Findings claim was wrong.** I wrote "DDPG converges faster than PPO baselines on this problem". The actual paper compares DDPG against **AC** and **DQN** baselines (no PPO baseline in the paper). DQN explicitly fails to converge in continuous action space; AC trains but is unstable. Updated the Findings section and added a note that the wiki's broader [[ddpg-vs-jppo]] comparison should be read as cross-source rather than internal to this paper.

### huang-2025-cmop-dispersed-computing

- **Venue was wrong.** I had marked it as "IEEE / preprint (Huang/Peng group, 2025)". The actual venue is **IEEE Transactions on Evolutionary Computation**, DOI `10.1109/TEVC.2025.3569722`. Confirmed by grepping the parsed full.md for the DOI. Updated frontmatter and citation.

### Other checks that passed

- Cross-checked DOIs for the 12 other new source pages against their parsed papers — all match.
- Schema lint: 26 source pages, 103 concept pages, 11 entity pages, 6 synthesis pages all have valid frontmatter (`type`, `title`, `tags`, h1 heading, etc.).
- Method/findings claims spot-checked for: JCORA (wang-2026, two-stage matching+convex+PGD), EMOMVO-CGD/JCCPAPO (liu-2025), ESAC=SAC+PER (nabi-2025), three-tier+binary-offloading+P-DQN (ma-2025), DEM+B-spline+multi-tasking (wu-2026), repair-CHT (peng-2024), dual-population+repair (huang-2025), I>=J standby UAVs (peng-2024), ACCP/ARDCP/MBCM/SRCON (jiang-2025). All consistent with the papers.
- Three dangling wikilinks remained (`hp-mobility-models`, `fairness-metrics-in-mec`, `purpose`) — all pre-existing, not introduced by either the curation or audit pass.
- Graph: 161 nodes, 1073 edges (LLM Wiki API).

## 2026-05-29 — Synthesis + entity follow-up (26-source era)

Closed the follow-up items flagged at the end of the 14-source curation pass.

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
- [[drl-vs-evolutionary-vs-classical-solvers]] — corpus-wide solver-family synthesis. Operating guide for picking each, plus the gap analysis: no head-to-head between families, robustness only in classical so far.

**Refreshed:**

- [[drl-backbones-across-uav-mec-sources]] — extended the at-a-glance table to cover the 4 new DRL sources (P-DQN, DDPG video, ESAC, HAP-PPO) and added a "What the 2026-05-29 batch changes" section: a clean three-way hybrid-action taxonomy; DDPG's niche (single-agent + scalar + pure-continuous); PER + entropy-regularized policy as the default off-policy baseline; SAGIN-tier scheduling as its own optimization shape.

### Index updates

- Synthesis section then listed 6 pages.
- Entities section split into Authors / Tools subsections.

### Still not done (intentional, scope-bound at the time)

- **Findings / methodology / thesis pages** still anchored to the original 12-source corpus. Claims like [[hybrid-action-memory-augmented-drl-wins-uav-mec]] are framed as *theses about [[liu-2026-jppo-en-convntm]]'s framework*, not corpus-wide.
- **No `evolutionary-design-recipe`** companion to [[design-recipe-multi-uav-mec]] yet.
- **No fresh queries** raised in this pass; open questions flagged inside the new synthesis pages await promotion to formal `query-*` pages.

## 2026-05-29 — Curation pass (14 new sources)

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

(The lineage then had 6 entries including [[xie-2026-uav-multisource-fusion]].)

**HAP / SAGIN foundations — 1 new source:**

- [[hsu-2025-drl-hues-hap-noma]] — Hsu et al. 2025 (TCCN). HAP transmission + RF energy harvesting in NOMA SAGINs; PPO-based DRL-HUES.

**ISAC track — 2 new sources:**

- [[benaya-2025-aerial-isac-haps]] — Benaya et al. 2025 (TGCN). HAPS-mounted FD ISAC + friendly-jamming UAV + ground MEC; AO + SDR + SCA.
- [[jiang-2025-isac-lae-overview]] — Jiang et al. 2025 (ComMag). ISAC-for-LAE survey: IAGN architecture, MBCM channel model, stochastic-geometry analysis.

**Vehicular MEC — 1 new source:**

- [[ma-2025-pdqn-vehicular-mec]] — Ma et al. 2025 (TVT). P-DQN for hybrid-action three-tier vehicular MEC.

### Concept pages added (44)

- **Communication / sensing / security:** [[integrated-sensing-and-communication]], [[physical-layer-security]], [[friendly-jamming-uav]], [[space-air-ground-integrated-network]], [[rf-energy-harvesting]], [[unicast-multicast-cooperation]], [[wireless-backhaul]].
- **DRL:** [[ddpg]], [[parameterized-dqn]], [[prioritized-experience-replay]].
- **Optimization (classical / metaheuristic):** [[alternating-optimization-sdr-sca]], [[chance-constraint]], [[conditional-value-at-risk]], [[distributionally-robust-optimization]], [[binary-whale-optimization]], [[multi-verse-optimizer]], [[weighted-kmeans-uav-deployment]], [[two-stage-decomposition]], [[gale-shapley-matching]].
- **Evolutionary methods:** [[constrained-multi-objective-evolutionary-algorithm]], [[cmoea-d-cdp]], [[infeasible-individual-utilization]], [[dual-population-evolutionary-algorithm]], [[multi-tasking-evolutionary-algorithm]], [[local-search-evolutionary]], [[b-spline-trajectory]].
- **Channel modeling:** [[blockage-aware-channel-model]], [[terrain-aware-channel-model]], [[stochastic-geometry-network-analysis]], [[csi-estimation-error]].
- **Workload classes / scheduling:** [[video-analytics-offloading]], [[video-transcoding-tradeoff]], [[qoe-modeling-mec]], [[dispersed-computing]], [[task-redundancy-for-reliability]], [[parallel-vs-serial-processing]], [[interdependent-tasks-dag]], [[makespan-minimization]], [[completion-time-difference]], [[multi-source-data-fusion]].
- **Architecture / metrics:** [[three-tier-cloud-edge-end]], [[maritime-mec]], [[uav-enabled-its]], [[service-caching-mec]], [[load-balancing-uav-mec]], [[energy-balancing-uav]].

## 2026-05-29 — Synthesis pass (continued)

- Added [[maddpg-vs-masac-in-mec]] — synthesis on the recurring "MASAC beats MADDPG" pattern in the cooperative-MEC corpus. Working thesis at medium confidence based on direct evidence from [[qin-2025-bcuav-masac]] and [[zhang-2025-ssac-mgi-heterogeneous-uav]], indirect support from [[peng-2025-drudm-cfg]] and [[liu-2026-jppo-en-convntm]]. Documents the mechanism, when MADDPG is still preferable, and what would promote the thesis to high confidence.
- Updated `wiki/index.md` synthesis section.

## 2026-05-29 — Cross-source synthesis pass

- Added [[drl-backbones-across-uav-mec-sources]] — cross-corpus synthesis covering 9 of 12 sources, mapping action-space shape → backbone choice, single vs multi-agent, memory/prediction patterns, and DRL-vs-classical composition. Distills 6 practical recommendations.
- Added [[bcsa-frl-vs-bc-uav-masac]] — head-to-head comparison of the two blockchain-integrated MEC sources.
- Updated `wiki/index.md` so both pages are reachable from the type-grouped directory.

## 2026-05-28 — Initial corpus build (papers 1-12)

The wiki's first curation arc: 12 raw papers ingested and curated, with the analytical scaffolding (concepts, findings, methodology, thesis, queries, comparisons, synthesis, entities) built around the seed paper.

**Paper 1/12 — project creation + seed graph.**

- Project created. Repo initialized as a GitHub repo (private) under `EnosElinsa/mec-research-wiki`.
- Ingested first source: [[liu-2026-jppo-en-convntm]] — Liu et al., *Multi-UAV Path Planning for MEC with High-Density Mobile Devices*.
- Constructed the initial wiki graph: 16 concept pages (MEC, UAV decisions, Gauss-Markov mobility, PPO/GAE/POMDP, NTM/ConvLSTM/STN, the three evaluation metrics); 6 finding pages; 1 methodology page; 1 thesis page; 2 query pages; 2 comparison pages + 1 synthesis page (design recipe); 7 entity pages for authors plus PyTorch.
- Baseline `purpose.md` and `schema.md` left untouched — schema-compliant.

**Paper 2/12 — [[mao-2025-bcsa-frl]]** — Mao et al. 2025, *Blockchain-Enabled Cold Start Aggregation Scheme for FRL-Based Task Offloading in Zero Trust LEO Satellite Networks* (IEEE JSAC). Added concept pages [[leo-satellite-edge-computing]], [[zero-trust-architecture]], [[federated-reinforcement-learning]], [[blockchain-for-fl-aggregation]], [[ccvm-correction-voting]], [[csra-cold-start-reputation-aggregation]], [[fl-poisoning-attacks]], [[ddqn]]; finding [[bcsa-frl-tolerates-up-to-half-malicious-satellites]].

**Paper 3/12 — [[qin-2025-bcuav-masac]]** — Qin et al. 2025, *Cooperative UAV Trajectory Design and Resource Allocation in Blockchain-Enabled Secure Aerial Edge Computing Network* (IEEE TWC). Added [[lyapunov-optimization]], [[masac]], [[noma]], [[air-ground-integrated-network]]. Cross-linked with [[mao-2025-bcsa-frl]] (blockchain-on-edge) and [[liu-2026-jppo-en-convntm]] (multi-UAV-DRL).

**Paper 4/12 — [[peng-2025-drudm-cfg]]** — Peng et al. 2025, *DRUDM-CFG: A Fairness-Aware Multi-Agent DRL for AMEC-Assisted TO in Post-Disaster Scenarios*. Added [[high-altitude-platform-station]], [[post-disaster-mec]], [[theil-fairness-index]], [[hierarchical-aerial-mec]], [[adaptive-entropy-priority-replay]], [[ma-pomdp]].

**Paper 5/12 — [[zhu-2025-lycnn-drl-wpt-mec]]** — Zhu et al. 2025, *Enhancing Energy Efficiency in WPT-MEC Through Lyapunov-Guided DRL* (IEEE TWC). Added [[wireless-power-transfer]], [[binary-vs-partial-offloading]], [[fractional-programming-dinkelbach]].

**Paper 6/12 — [[zhang-2025-mcma-task-migration]]** — Zhang et al. 2025, *Multi-Agent DRL With Trajectory Prediction for Task Migration-Assisted Computation Offloading*. Added [[vehicular-mec]], [[task-migration]], [[informer-trajectory-prediction]], [[centralized-training-decentralized-execution]].

**Paper 7/12 — [[wang-2025-uav-swarm-stackelberg]]** — Wang et al. 2025, *Optimizing Spectrum Sharing in UAV Swarms: A Stackelberg Game-Based Incentive Mechanism* (IEEE TVT). Added [[stackelberg-game]], [[overlay-underlay-spectrum-access]], [[matching-theory-for-resource-allocation]], [[low-altitude-intelligent-network]]. First wireless-foundations track entry.

**Paper 8/12 — [[zhang-2025-ssac-mgi-heterogeneous-uav]]** — Zhang et al. 2025, *Safe and Energy-Efficient Trajectory Planning for Heterogeneous Multi-UAV Enabled MEC*. Added [[heterogeneous-uav-fleet]], [[safe-reinforcement-learning]], [[collision-avoidance-mgi]].

**Paper 9/12 — [[bi-2025-sg-mapg]]** — Bi et al. 2025, *SG-MAPG: A Three-Layer Hierarchical Model for Service Fairness and Cost Optimization in UAV-Assisted MEC*. No new concept pages — reuses [[stackelberg-game]], [[ma-pomdp]], [[hierarchical-aerial-mec]], [[matching-theory-for-resource-allocation]].

**Paper 10/12 — [[hao-2025-priority-aware-task-driven-co]]** — Hao et al. 2025, *Task-Driven Priority-Aware Computation Offloading Using DRL*. Added [[event-driven-vs-slot-driven-offloading]], [[task-priority-in-mec]].

**Paper 11/12 — [[wang-2025-lae-network-survey]]** — Wang et al. 2025, *Toward Realization of Low-Altitude Economy Networks* (IEEE TCCN). Added [[generative-ai-for-mec]] (placeholder for future GAI-MEC sources). Anchors the wiki's LAE thread.

**Paper 12/12 — [[xie-2026-uav-multisource-fusion]]** — Xie et al. 2026, *UAV-Enabled Multi-Source Data Fusion in Vehicular Networks* (IEEE TWC). Added [[cooperative-perception]], [[dynamic-constrained-multi-objective-optimization]]. All 12 initial raw sources curated.

## Raw-source housekeeping

The LLM-Wiki desktop app emits an automated "external batch delete" log entry every time it prunes raw MinerU artifacts (origin PDFs, `full.md`, and `origin_file.html` files) for papers that were ingested, parsed, and curated. These are bookkeeping events, not curation decisions — **every block recorded "0 wiki pages" deleted**. The 89 verbose per-file blocks that previously interleaved with the curation history have been consolidated here:

- **2026-05-28:** 15 automated prune events (~34 raw artifact files), across the first wave of curated papers (HAP-NOMA, Aerial-ISAC, vehicular P-DQN, aerial-marine SAR, CMOP path-planning, DRO aerial-MEC, HAP-UAV video offloading, maritime IoT, ISAC-for-LAE, dispersed-computing, hierarchical aerial computing, interdependent-task scheduling, spectrum-sharing, terrain-aware MEC, multi-source fusion).
- **2026-05-29:** 74 automated prune events (~352 raw artifact files, including one 108-file bulk event), across the batch-3 and batch-4 curated papers (UAV-swarm stochastic game, AoI/energy tradeoff, UAV-LEO game, SAGIN FL handover, traffic-aware SAGIN, IRS two-stage energy, perception-aided SAGIN, trajectory/caching/migration, multi-UAV priority offloading, AIGC diffusion contract, ASAP swarm, anti-jamming, service-experience caching, satellite-marine offloading, double-edge SAMIN, three-tier maritime, SWIPT-MEC, and the rest of batches 3-4).

Net effect across all events: **0 wiki pages deleted**; only redundant raw parse/PDF artifacts were pruned by the app. The authoritative raw parses for all 82 curated sources remain under `raw/sources/<Folder>/full.md`.
- **2026-05-31:** 1 automated prune event (5 raw artifact files) for the two duplicate MinerU re-ingests removed during cleanup (the space-named Stackelberg spectrum-sharing and UAV multi-source vehicular fusion folders); the underscore-named curated originals are unaffected.
## [2026-06-25] external batch delete | 527 source files

Deleted 527 source files and 0 wiki pages.

Sources:
- A DRL-Based High-Altitude Platform Transmission and Energy Harvesting Scheduling Scheme for 6G NOMA/bc50cd1f-cef0-4b2a-a746-92f0c4476f79_origin.pdf
- A DRL-Based High-Altitude Platform Transmission and Energy Harvesting Scheduling Scheme for 6G NOMA/full.md
- AAV-Assisted_Joint_Mobile_Edge_Computing_and_Data_Collection_via_Matching-Enabled_Deep_Reinforcement_Learning/2736a490-72e5-42fc-a86a-95deb3cb1918_origin.pdf
- AAV-Assisted_Joint_Mobile_Edge_Computing_and_Data_Collection_via_Matching-Enabled_Deep_Reinforcement_Learning/45c7922b-5ded-46b3-af22-4c3e93f5ab01_origin.pdf
- AAV-Assisted_Joint_Mobile_Edge_Computing_and_Data_Collection_via_Matching-Enabled_Deep_Reinforcement_Learning/full.md
- ACBFT_Adaptive_Chained_Byzantine_Fault-Tolerant_Consensus_Protocol_for_UAV_Ad_Hoc_Networks/51f1dd7a-88b5-4325-80ed-9c8336415dc9_origin.pdf
- ACBFT_Adaptive_Chained_Byzantine_Fault-Tolerant_Consensus_Protocol_for_UAV_Ad_Hoc_Networks/full.md
- A_Blockchain-Enabled_Cold_Start_Aggregation_Scheme_for_Federated_Reinforcement_Learning-Based_Task_Offloading_in_Zero_Trust_LEO_Satellite_Networks/1f4868d8-793c-4b04-9a68-4b04fd7a68eb_origin.pdf
- A_Blockchain-Enabled_Cold_Start_Aggregation_Scheme_for_Federated_Reinforcement_Learning-Based_Task_Offloading_in_Zero_Trust_LEO_Satellite_Networks/MinerU_markdown_202605072001035_dfcfcb28.md
- A_Blockchain-Enabled_Cold_Start_Aggregation_Scheme_for_Federated_Reinforcement_Learning-Based_Task_Offloading_in_Zero_Trust_LEO_Satellite_Networks/full.md
- A_Correlated_Data-Driven_Collaborative_Beamforming_Approach_for_Energy-Efficient_IoT_Data_Transmission/93114a44-ffd7-4880-a027-6fee2041613f_origin.pdf
- A_Correlated_Data-Driven_Collaborative_Beamforming_Approach_for_Energy-Efficient_IoT_Data_Transmission/full.md
- A_Game-Theoretical_Approach_for_User_Allocation_in_Edge_Computing_Environment.pdf-6a127707-a8c8-4eb3-95db-bd84451c63bb/5805eb5a-c860-435a-a363-c7e08e58d364_origin.pdf
- A_Game-Theoretical_Approach_for_User_Allocation_in_Edge_Computing_Environment.pdf-6a127707-a8c8-4eb3-95db-bd84451c63bb/full.md
- A_Reinforcement_Learning-Based_Stochastic_Game_for_Energy-Efficient_UAV_Swarm-Assisted_MEC_With_Dynamic_Clustering_and_Scheduling/fbb58c1a-07f7-4252-9763-a3a929187767_origin.pdf
- A_Reinforcement_Learning-Based_Stochastic_Game_for_Energy-Efficient_UAV_Swarm-Assisted_MEC_With_Dynamic_Clustering_and_Scheduling/full.md
- A_Survey_of_Graph-Based_Resource_Management_in_Wireless_NetworksPart_II_Learning_Approaches/e8665d88-3f6b-4b18-b801-2ef12d508743_origin.pdf
- A_Survey_of_Graph-Based_Resource_Management_in_Wireless_NetworksPart_II_Learning_Approaches/full.md
- A_Survey_of_Graph-Based_Resource_Management_in_Wireless_NetworksPart_I_Optimization_Approaches/08cb4879-c577-432f-8a9d-4c2bc815bbd8_origin.pdf
- A_Survey_of_Graph-Based_Resource_Management_in_Wireless_NetworksPart_I_Optimization_Approaches/full.md
- A_Survey_on_Mobile_Edge_Computing_The_Communication_Perspective/a4df4525-9548-41ce-848a-b64ff3be183c_origin.pdf
- A_Survey_on_Mobile_Edge_Computing_The_Communication_Perspective/full.md
- A_Three-Party_Hierarchical_Game_for_Physical_Layer_Security_Aware_Wireless_Communications_With_Dynamic_Trilateral_Coalitions/bb0f9a14-8da1-48a0-9b68-3575b7326232_origin.pdf
- A_Three-Party_Hierarchical_Game_for_Physical_Layer_Security_Aware_Wireless_Communications_With_Dynamic_Trilateral_Coalitions/full.md
- A_Tutorial_on_Extremely_Large-Scale_MIMO_for_6G_Fundamentals_Signal_Processing_and_Applications/b04ea9f9-0b10-4fd1-980b-bbad587f106c_origin.pdf
- A_Tutorial_on_Extremely_Large-Scale_MIMO_for_6G_Fundamentals_Signal_Processing_and_Applications/full.md
- A_Tutorial_on_UAVs_for_Wireless_Networks_Applications_Challenges_and_Open_Problems/902c0eb8-95e4-405a-9fc2-65a17e072331_origin.pdf
- A_Tutorial_on_UAVs_for_Wireless_Networks_Applications_Challenges_and_Open_Problems/full.md
- A_Unified_Framework_for_Guiding_Generative_AI_With_Wireless_Perception_in_Resource_Constrained_Mobile_Edge_Networks/5266099d-7f41-4574-b255-b221b46e6800_origin.pdf
- A_Unified_Framework_for_Guiding_Generative_AI_With_Wireless_Perception_in_Resource_Constrained_Mobile_Edge_Networks/full.md
- Accessing_From_the_Sky_A_Tutorial_on_UAV_Communications_for_5G_and_Beyond/79f4cb38-2287-4aee-bd6e-cf09af9369af_origin.pdf
- Accessing_From_the_Sky_A_Tutorial_on_UAV_Communications_for_5G_and_Beyond/full.md
- Active-Passive_Cascaded_RIS-Aided_Receiver_Design_for_Jamming_Nulling_and_Signal_Enhancing/0f38395b-057f-43c4-8509-284386fa542b_origin.pdf
- Active-Passive_Cascaded_RIS-Aided_Receiver_Design_for_Jamming_Nulling_and_Signal_Enhancing/full.md
- Adaptive_Bitrate_Video_Caching_in_UAV-Assisted_MEC_Networks_Based_on_Distributionally_Robust_Optimization/8107c9ad-a80c-4df7-9da5-82cf6ae85914_origin.pdf
- Adaptive_Bitrate_Video_Caching_in_UAV-Assisted_MEC_Networks_Based_on_Distributionally_Robust_Optimization/full.md
- Adaptive_Digital_Twin_Migration_in_Vehicular_Edge_Computing_and_Networks/72cf2610-67b7-4163-96d0-bba1843ff446_origin.pdf
- Adaptive_Digital_Twin_Migration_in_Vehicular_Edge_Computing_and_Networks/full.md
- Addressing Function Approximation Error in Actor-Critic Methods/3eb17782-ecfe-4c74-b3b6-929a6738ed73_origin.pdf
- Addressing Function Approximation Error in Actor-Critic Methods/full.md
- Aerial ISAC A HAPS-Assisted Integrated Sensing, Communications and Computing Framework for Enhanced/7b0dd176-7253-422b-ac0e-8100331fd0d8_origin.pdf
- Aerial ISAC A HAPS-Assisted Integrated Sensing, Communications and Computing Framework for Enhanced/full.md
- Aerial_Reliable_Collaborative_Communications_for_Terrestrial_Mobile_Users_via_Evolutionary_Multi-Objective_Deep_Reinforcement_Learning/5c6033ad-b6c2-4040-ba8a-fbc7ad824e49_origin.pdf
- Aerial_Reliable_Collaborative_Communications_for_Terrestrial_Mobile_Users_via_Evolutionary_Multi-Objective_Deep_Reinforcement_Learning/full.md
- AirGround_Coordinated_MEC_Joint_Task_Time_Allocation_and_Trajectory_Design/bb68f660-4524-4a34-927d-aab6cac62a85_origin.pdf
- AirGround_Coordinated_MEC_Joint_Task_Time_Allocation_and_Trajectory_Design/full.md
- All-Sky_Autonomous_Computing_in_UAV_Swarm/5bbeb0cb-515b-49cf-a0d5-cc2274e3e0b3_origin.pdf
- All-Sky_Autonomous_Computing_in_UAV_Swarm/full.md
- An_Adaptive_Constraint_Violation_Evaluation_Framework_for_Constrained_Multiobjective_Evolutionary_Optimization/1058f15e-3289-44ba-a46f-79175aa42220_origin.pdf
- An_Adaptive_Constraint_Violation_Evaluation_Framework_for_Constrained_Multiobjective_Evolutionary_Optimization/full.md
- AoI_and_Energy_Tradeoff_for_Aerial-Ground_Collaborative_MEC_A_Multi-Objective_Learning_Approach/59a5c499-4de5-4693-94d8-c8bb910236f5_origin.pdf
- AoI_and_Energy_Tradeoff_for_Aerial-Ground_Collaborative_MEC_A_Multi-Objective_Learning_Approach/full.md
- BARGAIN-MATCH_A_Game_Theoretical_Approach_for_Resource_Allocation_and_Task_Offloading_in_Vehicular_Edge_Computing_Networks/04bff10e-4497-45a2-a8ac-d649dc9ccda9_origin.pdf
- BARGAIN-MATCH_A_Game_Theoretical_Approach_for_Resource_Allocation_and_Task_Offloading_in_Vehicular_Edge_Computing_Networks/full.md
- Blockchain-Integrated_UAV-Assisted_Mobile_Edge_Computing_Trajectory_Planning_and_Resource_Allocation/055e520e-51a5-4fdc-bba4-f3b0bd7351e9_origin.pdf
- Blockchain-Integrated_UAV-Assisted_Mobile_Edge_Computing_Trajectory_Planning_and_Resource_Allocation/full.md
- Caching_UAV_Assisted_Secure_Transmission_in_Hyper-Dense_Networks_Based_on_Interference_Alignment/5ea8883d-cf74-4a56-9ca2-46a60411f341_origin.pdf
- Caching_UAV_Assisted_Secure_Transmission_in_Hyper-Dense_Networks_Based_on_Interference_Alignment/full.md
- Collaborative_Ground-Space_Communications_via_Evolutionary_Multi-Objective_Deep_Reinforcement_Learning/7990312e-55f1-40cd-9275-ebbdb7088122_origin.pdf
- Collaborative_Ground-Space_Communications_via_Evolutionary_Multi-Objective_Deep_Reinforcement_Learning/full.md
- Collaborative_Reinforcement_Learning_Based_Unmanned_Aerial_Vehicle_UAV_Trajectory_Design_for_3D_UAV_Tracking/e66ac6eb-6d88-4eb7-8b92-3093d496a202_origin.pdf
- Collaborative_Reinforcement_Learning_Based_Unmanned_Aerial_Vehicle_UAV_Trajectory_Design_for_3D_UAV_Tracking/full.md
- Collaborative_Task_Offloading_Optimization_for_Satellite_Mobile_Edge_Computing_Using_Multi-Agent_Deep_Reinforcement_Learning/0849ef00-bff4-4422-bd56-9bb12c3b810e_origin.pdf
- Collaborative_Task_Offloading_Optimization_for_Satellite_Mobile_Edge_Computing_Using_Multi-Agent_Deep_Reinforcement_Learning/full.md
- Communications_and_Control_for_Wireless_Drone-Based_Antenna_Array/9008ce99-8d1d-4fda-b24d-5d157becd943_origin.pdf
- Communications_and_Control_for_Wireless_Drone-Based_Antenna_Array/full.md
- Completion_Time_and_Energy_Optimization_in_the_UAV-Enabled_Mobile-Edge_Computing_System/c49c4d13-579e-4bd8-b7d3-1de74dcb1d03_origin.pdf
- Completion_Time_and_Energy_Optimization_in_the_UAV-Enabled_Mobile-Edge_Computing_System/full.md
- Computation Offloading and Resource Allocation in Vehicular MEC A Parameterized Deep Reinforcement/d2b86536-1061-4c7c-83e3-48ab00d620b7_origin.pdf
- Computation Offloading and Resource Allocation in Vehicular MEC A Parameterized Deep Reinforcement/full.md
- Computation-Efficient Aerial-Marine Integrated Networks for Search and Rescue via Cooperative HAPS/255b305e-ac42-4253-9f2f-66a881effee7_origin.pdf
- Computation-Efficient Aerial-Marine Integrated Networks for Search and Rescue via Cooperative HAPS/full.md
- Computation_Offloading_and_Resource_Allocation_in_LEO_Satellite-Terrestrial_Integrated_Networks_With_System_State_Delay/b2091f09-92a4-45bf-84c9-c40761291c80_origin.pdf
- Computation_Offloading_and_Resource_Allocation_in_LEO_Satellite-Terrestrial_Integrated_Networks_With_System_State_Delay/full.md
- Computation_Offloading_in_LEO_Satellite_Networks_With_Hybrid_Cloud_and_Edge_Computing/e05be22d-ce46-416b-8a40-8217f45f7995_origin.pdf
- Computation_Offloading_in_LEO_Satellite_Networks_With_Hybrid_Cloud_and_Edge_Computing/full.md
- Computation_Offloading_in_Resource-Constrained_Multi-Access_Edge_Computing/4cb00723-7605-4068-82a9-b4f936db0089_origin.pdf
- Computation_Offloading_in_Resource-Constrained_Multi-Access_Edge_Computing/full.md
- Computation_Rate_Maximization_in_UAV-Enabled_Wireless-Powered_Mobile-Edge_Computing_Systems/df798421-94bf-46dd-bd8e-881b362231e5_origin.pdf
- Computation_Rate_Maximization_in_UAV-Enabled_Wireless-Powered_Mobile-Edge_Computing_Systems/full.md
- Computing_Offloading_and_Resource_Allocation_of_NOMA-Based_UAV_Emergency_Communication_in_Marine_Internet_of_Things/2c43fbe3-f1e7-4956-8659-5ac538581e2f_origin.pdf
- Computing_Offloading_and_Resource_Allocation_of_NOMA-Based_UAV_Emergency_Communication_in_Marine_Internet_of_Things/full.md
- Conditional_Generative_Adversarial_Networks_for_Channel_Estimation_in_RIS-Assisted_ISAC_Systems/d17bf5a0-218d-4917-b746-6fc2a408824f_origin.pdf
- Conditional_Generative_Adversarial_Networks_for_Channel_Estimation_in_RIS-Assisted_ISAC_Systems/full.md
- Constrained_Multi-Objective_Optimization_for_UAV-Enabled_Mobile_Edge_Computing_Offloading_Optimization_and_Path_Planning/e2cbd4fd-01db-4ad4-a0b5-46084bd1f98c_origin.pdf
- Constrained_Multi-Objective_Optimization_for_UAV-Enabled_Mobile_Edge_Computing_Offloading_Optimization_and_Path_Planning/full.md
- Continuous control with deep reinforcement learning/70a198eb-de78-4b6f-8097-3b3287971492_origin.pdf
- Continuous control with deep reinforcement learning/full.md
- Continuous_Control_with_Deep_Reinforcement_Learning_for_Mobile_Robot_Navigation/74ba7c51-5414-4a43-84bb-eb76ef09e3b6_origin.pdf
- Continuous_Control_with_Deep_Reinforcement_Learning_for_Mobile_Robot_Navigation/full.md
- Convergence_of_MEC_and_DRL_in_Non-Terrestrial_Wireless_Networks_Key_Innovations_Challenges_and_Future_Pathways/fa7658de-0e7b-40ad-b509-17af655fda95_origin.pdf
- Convergence_of_MEC_and_DRL_in_Non-Terrestrial_Wireless_Networks_Key_Innovations_Challenges_and_Future_Pathways/full.md
- Cooperative_Federated_Learning_Over_Ground-to-Satellite_Integrated_Networks_Joint_Local_Computation_and_Data_Offloading/7fbd757a-263e-45ef-8f32-c6b6798bdca0_origin.pdf
- Cooperative_Federated_Learning_Over_Ground-to-Satellite_Integrated_Networks_Joint_Local_Computation_and_Data_Offloading/full.md
- Cooperative_Ground-Satellite_Scheduling_and_Power_Allocation_for_Urban_Air_Mobility_Networks/234d2f6f-8b9a-47e8-a15d-ca691bd8d46f_origin.pdf
- Cooperative_Ground-Satellite_Scheduling_and_Power_Allocation_for_Urban_Air_Mobility_Networks/full.md
- Cooperative_Offloading_and_Resource_Management_for_UAV-Enabled_Mobile_Edge_Computing_in_Power_IoT_System/a825b5cf-a844-4e7b-b65e-6c93373ed016_origin.pdf
- Cooperative_Offloading_and_Resource_Management_for_UAV-Enabled_Mobile_Edge_Computing_in_Power_IoT_System/full.md
- Cooperative_UAV-Mounted_RISs-Assisted_Energy-Efficient_Communications/8a131dd8-afe7-4f31-b1fa-e4560e6847ef_origin.pdf
- Cooperative_UAV-Mounted_RISs-Assisted_Energy-Efficient_Communications/full.md
- Cooperative_UAV_Resource_Allocation_and_Task_Offloading_in_Hierarchical_Aerial_Computing_Systems_A_MAPPO-Based_Approach/a6533d10-e97c-4756-a27b-ce396e62927d_origin.pdf
- Cooperative_UAV_Resource_Allocation_and_Task_Offloading_in_Hierarchical_Aerial_Computing_Systems_A_MAPPO-Based_Approach/full.md
- Cooperative_UAV_Trajectory_Design_and_Resource_Allocation_in_Blockchain-Enabled_Secure_Aerial_Edge_Computing_Network/34b5a662-8994-4f73-b5a1-a1e7c1537ea0_origin.pdf
- Cooperative_UAV_Trajectory_Design_and_Resource_Allocation_in_Blockchain-Enabled_Secure_Aerial_Edge_Computing_Network/full.md
- Cost-Efficient_Computation_Offloading_in_SAGIN_A_Deep_Reinforcement_Learning_and_Perception-Aided_Approach/ea57119f-657f-4e9c-a621-1d58cc99cfe3_origin.pdf
- Cost-Efficient_Computation_Offloading_in_SAGIN_A_Deep_Reinforcement_Learning_and_Perception-Aided_Approach/full.md
- Covert_mmWave_Communications_With_Finite_Blocklength_Against_Spatially_Random_Wardens/1e753f05-0bf1-4936-b674-792e98d1bde2_origin.pdf
- Covert_mmWave_Communications_With_Finite_Blocklength_Against_Spatially_Random_Wardens/full.md
- Cramr-Rao_Bound_Optimization_for_Active_RIS-Empowered_ISAC_Systems/d48ab3ec-381a-428a-ad73-8918f3f2befd_origin.pdf
- Cramr-Rao_Bound_Optimization_for_Active_RIS-Empowered_ISAC_Systems/full.md
- DNN_Partitioning_Task_Offloading_and_Resource_Allocation_in_Dynamic_Vehicular_Networks_A_Lyapunov-Guided_Diffusion-Based_Reinforcement_Learning_Approach/f88edc27-7d80-4bf5-8fb8-8657ec6da2ca_origin.pdf
- DNN_Partitioning_Task_Offloading_and_Resource_Allocation_in_Dynamic_Vehicular_Networks_A_Lyapunov-Guided_Diffusion-Based_Reinforcement_Learning_Approach/full.md
- DRUDM-CFG_a_Fairness-Aware_Multi-Agent_DRL_Algorithm_for_AMEC-Assisted_Task_Offloading_in_Post-Disaster_Scenarios/328a810b-17dd-4c5e-913a-2dbfe1e0ea85_origin.pdf
- DRUDM-CFG_a_Fairness-Aware_Multi-Agent_DRL_Algorithm_for_AMEC-Assisted_Task_Offloading_in_Post-Disaster_Scenarios/full.md
- Data_Offloading_in_UAV-Assisted_Multi-Access_Edge_Computing_Systems_Under_Resource_Uncertainty/a6b25c95-0fb6-48f2-8475-7425dbaf265d_origin.pdf
- Data_Offloading_in_UAV-Assisted_Multi-Access_Edge_Computing_Systems_Under_Resource_Uncertainty/full.md
- Decentralized_Computation_Offloading_Game_for_Mobile_Cloud_Computing/5d7c7d14-daa0-4fd7-b936-aeed3e43e0fc_origin.pdf
- Decentralized_Computation_Offloading_Game_for_Mobile_Cloud_Computing/full.md
- Decentralized_Navigation_With_Heterogeneous_Federated_Reinforcement_Learning_for_UAV-Enabled_Mobile_Edge_Computing/cdee9ff2-e35f-41ea-99cf-c62249fc2c16_origin.pdf
- Decentralized_Navigation_With_Heterogeneous_Federated_Reinforcement_Learning_for_UAV-Enabled_Mobile_Edge_Computing/full.md
- Deep_Reinforcement_Learning-Based_Resource_Management_for_UAV-Assisted_Mobile_Edge_Computing_Against_Jamming/61d1a406-15d3-42b7-9873-b406053311ee_origin.pdf
- Deep_Reinforcement_Learning-Based_Resource_Management_for_UAV-Assisted_Mobile_Edge_Computing_Against_Jamming/full.md
- Deep_Reinforcement_Learning_Based_Dynamic_Trajectory_Control_for_UAV-Assisted_Mobile_Edge_Computing/84e2e9e3-ad16-4cfd-992e-ff34ecae99f5_origin.pdf
- Deep_Reinforcement_Learning_Based_Dynamic_Trajectory_Control_for_UAV-Assisted_Mobile_Edge_Computing/full.md
- Deep_Reinforcement_Learning_Based_Latency_Minimization_for_Mobile_Edge_Computing_With_Virtualization_in_Maritime_UAV_Communication_Network/b8ab9143-b5a5-4717-a5d8-c0e8d7724606_origin.pdf
- Deep_Reinforcement_Learning_Based_Latency_Minimization_for_Mobile_Edge_Computing_With_Virtualization_in_Maritime_UAV_Communication_Network/full.md
- Deep_Reinforcement_Learning_with_Double_Q-learning/822580aa-aa9c-47c6-b712-d257e7c87e7c_origin.pdf
- Deep_Reinforcement_Learning_with_Double_Q-learning/full.md
- Delay-Aware_Cooperative_Task_Offloading_for_Multi-UAV_Enabled_Edge-Cloud_Computing/91f03895-a779-42f0-8e44-5ab02af4868e_origin.pdf
- Delay-Aware_Cooperative_Task_Offloading_for_Multi-UAV_Enabled_Edge-Cloud_Computing/full.md
- Delay-Aware_UAV_Computation_Offloading_and_Communication_Assistance_for_Post-Disaster_Rescue/981d6211-3e85-4f83-84b6-7bd1fb27b03f_origin.pdf
- Delay-Aware_UAV_Computation_Offloading_and_Communication_Assistance_for_Post-Disaster_Rescue/full.md
- Diffusion-Based_Reinforcement_Learning_for_Edge-Enabled_AI-Generated_Content_Services/a0e5dc98-b654-4f8f-a45d-962526a6e5ca_origin.pdf
- Diffusion-Based_Reinforcement_Learning_for_Edge-Enabled_AI-Generated_Content_Services/full.md
- Distributed_Foundation_Models_for_Multi-Modal_Learning_in_6G_Wireless_Networks/52184245-a588-46d7-8436-664582f236ae_origin.pdf
- Distributed_Foundation_Models_for_Multi-Modal_Learning_in_6G_Wireless_Networks/full.md
- Distributed_and_Collaborative_Beamforming_in_Wireless_Sensor_Networks_Classifications_Trends_and_Research_Directions/f3d66278-a519-4fb7-9168-65b58b3cc165_origin.pdf
- Distributed_and_Collaborative_Beamforming_in_Wireless_Sensor_Networks_Classifications_Trends_and_Research_Directions/full.md
- Distributionally Robust Optimization for Aerial Multi-Access Edge Computing via Cooperation of UAVs/ab4c9dcb-8a80-48b3-8fa8-219fd6933dcc_origin.pdf
- Distributionally Robust Optimization for Aerial Multi-Access Edge Computing via Cooperation of UAVs/full.md
- Double-Edge-Assisted_Computation_Offloading_and_Resource_Allocation_for_Space-Air-Marine_Integrated_Networks/3d74f158-5928-492f-a341-867a10312574_origin.pdf
- Double-Edge-Assisted_Computation_Offloading_and_Resource_Allocation_for_Space-Air-Marine_Integrated_Networks/51a15428-6640-4700-b016-4294726d6ad3_origin.pdf
- Double-Edge-Assisted_Computation_Offloading_and_Resource_Allocation_for_Space-Air-Marine_Integrated_Networks/full.md
- Drone_Small_Cells_in_the_Clouds_Design_Deployment_and_Performance_Analysis/b019ad77-4751-4aa5-af30-e76dc961c962_origin.pdf
- Drone_Small_Cells_in_the_Clouds_Design_Deployment_and_Performance_Analysis/full.md
- Drone_Swarm_Path_Planning_for_Mobile_Edge_Computing_in_Industrial_Internet_of_Things/8a81aa66-8aa0-446e-8642-8a52f76a8026_origin.pdf
- Drone_Swarm_Path_Planning_for_Mobile_Edge_Computing_in_Industrial_Internet_of_Things/full.md
- Dual_AAV_Cluster-Assisted_Maritime_Physical-Layer_Secure_Communications_via_Collaborative_Beamforming/a0a3f6f3-8df6-4c7b-ba76-cab656db7cc5_origin.pdf
- Dual_AAV_Cluster-Assisted_Maritime_Physical-Layer_Secure_Communications_via_Collaborative_Beamforming/full.md
- Dynamic_Computation_Offloading_for_Mobile-Edge_Computing_With_Energy_Harvesting_Devices/9330c407-dcdb-43a5-a2da-0836cdf65fe9_origin.pdf
- Dynamic_Computation_Offloading_for_Mobile-Edge_Computing_With_Energy_Harvesting_Devices/full.md
- Dynamic_Human_Digital_Twin_Deployment_at_the_Edge_for_Task_Execution_A_Two-Timescale_Accuracy-Aware_Online_Optimization/2cba3628-4325-4b17-8299-2800f817a892_origin.pdf
- Dynamic_Human_Digital_Twin_Deployment_at_the_Edge_for_Task_Execution_A_Two-Timescale_Accuracy-Aware_Online_Optimization/full.md
- Dynamic_Trajectory_Design_for_Multi-UAV-Assisted_Mobile_Edge_Computing/9ccf2fbd-fd55-4a5d-8f6b-247eee835fca_origin.pdf
- Dynamic_Trajectory_Design_for_Multi-UAV-Assisted_Mobile_Edge_Computing/full.md
- Efficient_3-D_placement_of_an_aerial_base_station_in_next_generation_cellular_networks/c94e6c2e-0400-4185-adba-7574e85c1e44_origin.pdf
- Efficient_3-D_placement_of_an_aerial_base_station_in_next_generation_cellular_networks/full.md
- Efficient_Deployment_of_Multiple_Unmanned_Aerial_Vehicles_for_Optimal_Wireless_Coverage/b3ffb44c-8fe3-4661-904e-1af48c1094af_origin.pdf
- Efficient_Deployment_of_Multiple_Unmanned_Aerial_Vehicles_for_Optimal_Wireless_Coverage/full.md
- Efficient_Multi-User_Computation_Offloading_for_Mobile-Edge_Cloud_Computing/8bc9edd3-253e-452e-891a-cdecfc849668_origin.pdf
- Efficient_Multi-User_Computation_Offloading_for_Mobile-Edge_Cloud_Computing/full.md
- Elastic_Collaborative_Edge_Intelligence_for_UAV_Swarm_Architecture_Challenges_and_Opportunities/c40d3f17-38d8-4dd3-8e96-1cca63360198_origin.pdf
- Elastic_Collaborative_Edge_Intelligence_for_UAV_Swarm_Architecture_Challenges_and_Opportunities/full.md
- Energy-Constrained_Satellite_Edge_Computing_for_Satellite-Terrestrial_Integrated_Networks/22571432-c100-42a5-b0a8-e7207975e1f0_origin.pdf
- Energy-Constrained_Satellite_Edge_Computing_for_Satellite-Terrestrial_Integrated_Networks/full.md
- Energy-Efficient_Computation_Peer_Offloading_in_Satellite_Edge_Computing_Networks/20f7aa2d-0c28-4925-a196-231937e5cb39_origin.pdf
- Energy-Efficient_Computation_Peer_Offloading_in_Satellite_Edge_Computing_Networks/full.md
- Energy-Efficient_Data_Collection_in_UAV_Enabled_Wireless_Sensor_Network/36546abf-5f44-4fa9-ab2f-da1fdc5e0a13_origin.pdf
- Energy-Efficient_Data_Collection_in_UAV_Enabled_Wireless_Sensor_Network/full.md
- Energy-Efficient_Design_of_Satellite-Terrestrial_Computing_in_6G_Wireless_Networks/1175b392-8817-40ca-8a3a-c85ea0d36500_origin.pdf
- Energy-Efficient_Design_of_Satellite-Terrestrial_Computing_in_6G_Wireless_Networks/full.md
- Energy-Efficient_Resource_Allocation_for_Mobile-Edge_Computation_Offloading/4d5109bd-44f7-4463-b1e0-7edf7ce78555_origin.pdf
- Energy-Efficient_Resource_Allocation_for_Mobile-Edge_Computation_Offloading/full.md
- Energy-Efficient_UAV-Assisted_Mobile_Edge_Computing_Resource_Allocation_and_Trajectory_Optimization/9072c131-3db4-4702-811d-8d248c3e68ee_origin.pdf
- Energy-Efficient_UAV-Assisted_Mobile_Edge_Computing_Resource_Allocation_and_Trajectory_Optimization/full.md
- Energy-Efficient_UAV_Communication_With_Trajectory_Optimization/7904aa79-bede-4336-b97e-10ba712dfa27_origin.pdf
- Energy-Efficient_UAV_Communication_With_Trajectory_Optimization/full.md
- Energy-Efficient_UAV_Swarm_Assisted_MEC_With_Dynamic_Clustering_and_Scheduling/a5acd178-4342-4fb9-b998-c93e0b3b71b1_origin.pdf
- Energy-Efficient_UAV_Swarm_Assisted_MEC_With_Dynamic_Clustering_and_Scheduling/full.md
- Energy-Optimal_Mobile_Cloud_Computing_under_Stochastic_Wireless_Channel/8e770bf5-44e9-46db-bcb4-1b5f8ed66d0e_origin.pdf
- Energy-Optimal_Mobile_Cloud_Computing_under_Stochastic_Wireless_Channel/full.md
- Energy_Consumption_Minimization_in_UAV-Assisted_Mobile-Edge_Computing_Systems_Joint_Resource_Allocation_and_Trajectory_Design/6ad0cc20-c36f-479b-8cae-d0aeeb96aa4c_origin.pdf
- Energy_Consumption_Minimization_in_UAV-Assisted_Mobile-Edge_Computing_Systems_Joint_Resource_Allocation_and_Trajectory_Design/full.md
- Energy_Efficiency_Maximization_of_Backscatter-Assisted_Wireless-Powered_MEC_With_User_Cooperation/8a8ab8ec-3d66-4ee2-b1cd-1dbced604602_origin.pdf
- Energy_Efficiency_Maximization_of_Backscatter-Assisted_Wireless-Powered_MEC_With_User_Cooperation/full.md
- Energy_Efficiency_Optimization_in_Intelligent_Reflecting_Surface-Aided_UAV_Wireless_Power_Transfer_Networks_Using_DRL/feca739c-1500-42f5-b7e1-f08dd3ad7979_origin.pdf
- Energy_Efficiency_Optimization_in_Intelligent_Reflecting_Surface-Aided_UAV_Wireless_Power_Transfer_Networks_Using_DRL/full.md
- Energy_Efficiency_of_Mobile_Clients_in_Cloud_Computing/897539aa-dea3-485f-bd8b-f783340f7639_origin.pdf
- Energy_Efficiency_of_Mobile_Clients_in_Cloud_Computing/full.md
- Energy_Efficient_Resource_Allocation_in_UAV-Enabled_Mobile_Edge_Computing_Networks/e8769b3e-96ac-4fc2-986f-c67cc4c27c6e_origin.pdf
- Energy_Efficient_Resource_Allocation_in_UAV-Enabled_Mobile_Edge_Computing_Networks/full.md
- Energy_Efficient_Task_Offloading_and_Resource_Allocation_in_Air-Ground_Integrated_MEC_Systems_A_Distributed_Online_Approach/69f11249-178f-489a-99dd-6013be4a2178_origin.pdf
- Energy_Efficient_Task_Offloading_and_Resource_Allocation_in_Air-Ground_Integrated_MEC_Systems_A_Distributed_Online_Approach/a7af4c61-064d-406a-8b3b-f4408286873c_origin.pdf
- Energy_Efficient_Task_Offloading_and_Resource_Allocation_in_Air-Ground_Integrated_MEC_Systems_A_Distributed_Online_Approach/full.md
- Energy_Minimization_for_Wireless_Communication_With_Rotary-Wing_UAV/ee0ea43c-110a-4655-ad55-33bdc434c5b9_origin.pdf
- Energy_Minimization_for_Wireless_Communication_With_Rotary-Wing_UAV/full.md
- Energy_Oriented_Three-Tier_Computation_Offloading_Scheme_in_Maritime_Edge_Computing_Network/05cc59c4-a99e-447a-9f94-9002dcc71c45_origin.pdf
- Energy_Oriented_Three-Tier_Computation_Offloading_Scheme_in_Maritime_Edge_Computing_Network/1d881528-e07b-4227-bdd8-2c2bfcaecc08_origin.pdf
- Energy_Oriented_Three-Tier_Computation_Offloading_Scheme_in_Maritime_Edge_Computing_Network/full.md
- Energy_and_Latency_Efficient_Joint_Communication_and_Computation_Optimization_in_a_Multi-UAV-Assisted_MEC_Network/feb0c599-91ed-4600-be1b-82bfc5e522f6_origin.pdf
- Energy_and_Latency_Efficient_Joint_Communication_and_Computation_Optimization_in_a_Multi-UAV-Assisted_MEC_Network/full.md
- Enhancing_AIoT_Device_Association_With_Task_Offloading_in_Aerial_MEC_Networks/d9002503-1183-4dad-a350-b11124bee8b4_origin.pdf
- Enhancing_AIoT_Device_Association_With_Task_Offloading_in_Aerial_MEC_Networks/full.md
- Enhancing_Deep_Reinforcement_Learning_A_Tutorial_on_Generative_Diffusion_Models_in_Network_Optimization/35cd8b3e-552a-425d-bab6-80e38e0b4b09_origin.pdf
- Enhancing_Deep_Reinforcement_Learning_A_Tutorial_on_Generative_Diffusion_Models_in_Network_Optimization/full.md
- Enhancing_Energy_Efficiency_in_Wireless-Powered_MEC_Systems_Through_Lyapunov-Guided_Deep_Reinforcement_Learning/3d5ceeab-9005-4303-aaab-247310b82ad4_origin.pdf
- Enhancing_Energy_Efficiency_in_Wireless-Powered_MEC_Systems_Through_Lyapunov-Guided_Deep_Reinforcement_Learning/full.md
- Evolutionary_Multi-Objective_Reinforcement_Learning_Based_Trajectory_Control_and_Task_Offloading_in_UAV-Assisted_Mobile_Edge_Computing/6d675f02-2610-41f9-8d08-e81e2f69eb79_origin.pdf
- Evolutionary_Multi-Objective_Reinforcement_Learning_Based_Trajectory_Control_and_Task_Offloading_in_UAV-Assisted_Mobile_Edge_Computing/full.md
- Exploiting_Multi-Layer_Refracting_RIS-Assisted_Receiver_for_HAP-SWIPT_Networks/7f8f7068-3367-48e8-80ef-3a0efe0b63bc_origin.pdf
- Exploiting_Multi-Layer_Refracting_RIS-Assisted_Receiver_for_HAP-SWIPT_Networks/full.md
- Fairness-Based_3-D_Multi-UAV_Trajectory_Optimization_in_Multi-UAV-Assisted_MEC_System/c0f2255d-e21b-42aa-8b98-d86bd3126819_origin.pdf
- Fairness-Based_3-D_Multi-UAV_Trajectory_Optimization_in_Multi-UAV-Assisted_MEC_System/full.md
- FedLEO_An_Offloading-Assisted_Decentralized_Federated_Learning_Framework_for_Low_Earth_Orbit_Satellite_Networks/c2b3ff92-9440-484e-82ac-7c26f755903f_origin.pdf
- FedLEO_An_Offloading-Assisted_Decentralized_Federated_Learning_Framework_for_Low_Earth_Orbit_Satellite_Networks/full.md
- GAI-Based_Resource_Management_in_RIS-Aided_Next-Generation_Network_and_Communication/ec31bf52-60eb-43c1-a664-b65bb3632fff_origin.pdf
- GAI-Based_Resource_Management_in_RIS-Aided_Next-Generation_Network_and_Communication/full.md
- Generative-Adversarial-Network-Enhanced_DRL_for_ISAC_With_Double_Active_RISs/54556004-5e12-446c-a020-2ca85e5d4fb8_origin.pdf
- Generative-Adversarial-Network-Enhanced_DRL_for_ISAC_With_Double_Active_RISs/full.md
- Generative_AI-Driven_Semantic_Communication_Networks_Architecture_Technologies_and_Applications/9b72d84b-10f1-4473-ada4-3ae09df62592_origin.pdf
- Generative_AI-Driven_Semantic_Communication_Networks_Architecture_Technologies_and_Applications/full.md
- Generative_AI_for_Integrated_Sensing_and_Communication_Insights_From_the_Physical_Layer_Perspective/ffff67cf-70f4-447d-8c0f-00ca4d58325c_origin.pdf
- Generative_AI_for_Integrated_Sensing_and_Communication_Insights_From_the_Physical_Layer_Perspective/full.md
- Generative_AI_for_Physical_Layer_Communications_A_Survey/d1617425-0384-4cea-84bd-da678212de96_origin.pdf
- Generative_AI_for_Physical_Layer_Communications_A_Survey/full.md
- Generative_AI_for_Secure_Physical_Layer_Communications_A_Survey/ea92e475-0f82-4ebc-86a8-0e468f43a8cc_origin.pdf
- Generative_AI_for_Secure_Physical_Layer_Communications_A_Survey/full.md
- Generative_AI_for_the_Optimization_of_Next-Generation_Wireless_Networks_Basics_State-of-the-Art_and_Open_Challenges/c848f928-34e9-426d-8306-3e39ef4ce670_origin.pdf
- Generative_AI_for_the_Optimization_of_Next-Generation_Wireless_Networks_Basics_State-of-the-Art_and_Open_Challenges/full.md
- HAP-UAV-Assisted Maritime IoT Communication Network/b802e38e-15e5-414e-b060-b4d4c009a479_origin.pdf
- HAP-UAV-Assisted Maritime IoT Communication Network/full.md
- HAP-UAV-assisted hierarchical aerial computing framework for video offloading a deep reinforcement/84fe2fa2-9cd4-458b-a3fd-c7c1a7fa57ec_origin.pdf
- HAP-UAV-assisted hierarchical aerial computing framework for video offloading a deep reinforcement/full.md
- HAP-UAV-assisted hierarchical aerial computing framework for video offloading a deep reinforcement/origin_file.html
- Handover_Protocol_Learning_for_LEO_Satellite_Networks_Access_Delay_and_Collision_Minimization/21665558-8d58-4194-abf8-b78c6eb2f36e_origin.pdf
- Handover_Protocol_Learning_for_LEO_Satellite_Networks_Access_Delay_and_Collision_Minimization/full.md
- Hierarchical_Aerial_Computing_for_Internet_of_Things_via_Cooperation_of_HAPs_and_UAVs/8011c826-f2ac-4903-afb0-d781ea9b50bb_origin.pdf
- Hierarchical_Aerial_Computing_for_Internet_of_Things_via_Cooperation_of_HAPs_and_UAVs/full.md
- Human-Level_Control_through_Deep_Reinforcement_Learning/f0ba15bc-6baf-4497-96c4-b54a7858b5f6_origin.pdf
- Human-Level_Control_through_Deep_Reinforcement_Learning/full.md
- Hybrid_Near-_and_Far-Field_THz_UM-MIMO_Channel_Estimation_A_Sparsifying_Matrix_Learning-Aided_Bayesian_Approach/99ef17c3-34b4-42fc-b3a9-337f2a8b84d5_origin.pdf
- Hybrid_Near-_and_Far-Field_THz_UM-MIMO_Channel_Estimation_A_Sparsifying_Matrix_Learning-Aided_Bayesian_Approach/full.md
- Hybrid_OMA_NOMA_Mode_Selection_and_Resource_Allocation_in_Space-Air-Ground_Integrated_Networks/44d6771e-2771-4368-ad1b-636d2251d8a8_origin.pdf
- Hybrid_OMA_NOMA_Mode_Selection_and_Resource_Allocation_in_Space-Air-Ground_Integrated_Networks/full.md
- Integrated Sensing and Communication for Low Altitude Economy Opportunities and Challenges/c3f1156a-22b5-4c6b-9d30-bb1ab8067bf8_origin.pdf
- Integrated Sensing and Communication for Low Altitude Economy Opportunities and Challenges/full.md
- Integrated Sensing and Communication for Low Altitude Economy Opportunities and Challenges/origin_file.html
- Integrated_Sensing_Computation_and_Communication_for_UAV-Assisted_Federated_Edge_Learning/bcf028aa-c5a5-4a9e-81e0-ab8face915e1_origin.pdf
- Integrated_Sensing_Computation_and_Communication_for_UAV-Assisted_Federated_Edge_Learning/full.md
- Intelligent_Reflecting_Surface_Assisted_Secure_Computation_of_Wireless_Powered_MEC_System/99856d28-6962-4628-b6b9-5d2f6392f850_origin.pdf
- Intelligent_Reflecting_Surface_Assisted_Secure_Computation_of_Wireless_Powered_MEC_System/full.md
- Intelligent_Reflecting_Surface_Enhanced_Wireless_Network_via_Joint_Active_and_Passive_Beamforming/e6a4fe69-f9e4-45a0-9202-30ac59c1df03_origin.pdf
- Intelligent_Reflecting_Surface_Enhanced_Wireless_Network_via_Joint_Active_and_Passive_Beamforming/full.md
- Intelligent_Spectrum_Sharing_Strategy_for_Integrated_Satellite-Maritime_Heterogeneous_Mobile_Networks/7ae57ae6-b71f-4d40-9db8-7e755fc78b6d_origin.pdf
- Intelligent_Spectrum_Sharing_Strategy_for_Integrated_Satellite-Maritime_Heterogeneous_Mobile_Networks/full.md
- JDACO_Joint_Data_Aggregation_and_Computation_Offloading_in_UAV-Enabled_Internet_of_Things_for_Post-Disaster_Scenarios/ef7fc8fb-b6e8-409f-bc0a-4f896837aa0a_origin.pdf
- JDACO_Joint_Data_Aggregation_and_Computation_Offloading_in_UAV-Enabled_Internet_of_Things_for_Post-Disaster_Scenarios/full.md
- Joint Latency and Charge Cost Minimization for Reliable Task Offloading in Dispersed Computing A Mu/39153acd-ed2c-4687-a492-c3198ec29647_origin.pdf
- Joint Latency and Charge Cost Minimization for Reliable Task Offloading in Dispersed Computing A Mu/full.md
- Joint Offloading Decision, User Association, and Resource Allocation in Hierarchical Aerial Computin/4ee311e2-a918-4848-859b-b50fb4cd16b0_origin.pdf
- Joint Offloading Decision, User Association, and Resource Allocation in Hierarchical Aerial Computin/full.md
- Joint Offloading Decision, User Association, and Resource Allocation in Hierarchical Aerial Computin/origin_file.html
- Joint_Altitude_and_Beamwidth_Optimization_for_UAV-Enabled_Multiuser_Communications/aee8a8b2-d582-4722-9cfe-079c22bc8f4d_origin.pdf
- Joint_Altitude_and_Beamwidth_Optimization_for_UAV-Enabled_Multiuser_Communications/full.md
- Joint_Beamforming_and_Reflection_Design_for_Secure_RIS-ISAC_Systems.pdf/0b899169-5cd3-4bfd-abb1-0974f6a35d90_origin.pdf
- Joint_Beamforming_and_Reflection_Design_for_Secure_RIS-ISAC_Systems.pdf/full.md
- Joint_Computation_Offloading_and_Multidimensional_Resource_Allocation_in_AirGround_Integrated_Vehicular_Edge_Computing_Network/247e2f83-465b-4484-b17c-e7bdcd0ba3f3_origin.pdf
- Joint_Computation_Offloading_and_Multidimensional_Resource_Allocation_in_AirGround_Integrated_Vehicular_Edge_Computing_Network/full.md
- Joint_Computation_Offloading_and_Resource_Allocation_for_Maritime_MEC_With_Energy_Harvesting/d2978212-57f7-4757-87c6-0b0c3f8ff592_origin.pdf
- Joint_Computation_Offloading_and_Resource_Allocation_for_Maritime_MEC_With_Energy_Harvesting/full.md
- Joint_Computation_Offloading_and_Resource_Allocation_for_Uncertain_Maritime_MEC_via_Cooperation_of_AAVs_and_Vessels/d4cfd60c-844d-4200-9959-58e733b9dd24_origin.pdf
- Joint_Computation_Offloading_and_Resource_Allocation_for_Uncertain_Maritime_MEC_via_Cooperation_of_AAVs_and_Vessels/fbddd1eb-b302-42d7-9ec3-3b79705ca118_origin.pdf
- Joint_Computation_Offloading_and_Resource_Allocation_for_Uncertain_Maritime_MEC_via_Cooperation_of_AAVs_and_Vessels/full.md
- Joint_Computation_and_Communication_Design_for_UAV-Assisted_Mobile_Edge_Computing_in_IoT/714dbdf1-14f0-4aa1-8086-94d182a61c42_origin.pdf
- Joint_Computation_and_Communication_Design_for_UAV-Assisted_Mobile_Edge_Computing_in_IoT/full.md
- Joint_Content_Caching_Service_Placement_and_Task_Offloading_in_UAV-Enabled_Mobile_Edge_Computing_Networks/2c7d63cc-6301-492b-b241-9d8cbb676fd1_origin.pdf
- Joint_Content_Caching_Service_Placement_and_Task_Offloading_in_UAV-Enabled_Mobile_Edge_Computing_Networks/full.md
- Joint_Data_Caching_and_Computation_Offloading_in_UAV-Assisted_Internet_of_Vehicles_via_Federated_Deep_Reinforcement_Learning/0458f7a2-0ea3-4f2c-9911-12f53de2f45d_origin.pdf
- Joint_Data_Caching_and_Computation_Offloading_in_UAV-Assisted_Internet_of_Vehicles_via_Federated_Deep_Reinforcement_Learning/full.md
- Joint_Deployment_and_Task_Scheduling_Optimization_for_Large-Scale_Mobile_Users_in_Multi-UAV-Enabled_Mobile_Edge_Computing/318c32ce-1de4-4b6e-933c-1dde4fe0af26_origin.pdf
- Joint_Deployment_and_Task_Scheduling_Optimization_for_Large-Scale_Mobile_Users_in_Multi-UAV-Enabled_Mobile_Edge_Computing/full.md
- Joint_Energy_and_Completion_Time_Difference_Minimization_for_UAV-Enabled_Intelligent_Transportation_Systems_A_Constrained_Multi-Objective_Optimization_Approach/9aeb297b-5e89-4774-8eb4-cf560799765b_origin.pdf
- Joint_Energy_and_Completion_Time_Difference_Minimization_for_UAV-Enabled_Intelligent_Transportation_Systems_A_Constrained_Multi-Objective_Optimization_Approach/full.md
- Joint_Interdependent_Task_Scheduling_and_Energy_Balancing_for_Multi-UAV-Enabled_Aerial_Edge_Computing_A_Multiobjective_Optimization_Approach/4e017c7c-629d-47fd-b843-7c070000881f_origin.pdf
- Joint_Interdependent_Task_Scheduling_and_Energy_Balancing_for_Multi-UAV-Enabled_Aerial_Edge_Computing_A_Multiobjective_Optimization_Approach/full.md
- Joint_Multi-Domain_Resource_Allocation_and_Trajectory_Optimization_in_UAV-Assisted_Maritime_IoT_Networks/12402d11-26d6-4b9f-bac9-8015f5b89f97_origin.pdf
- Joint_Multi-Domain_Resource_Allocation_and_Trajectory_Optimization_in_UAV-Assisted_Maritime_IoT_Networks/full.md
- Joint_Offloading_and_Computing_Optimization_in_Wireless_Powered_Mobile-Edge_Computing_Systems/b4e48c90-6a37-4656-97ea-4393e94abb1c_origin.pdf
- Joint_Offloading_and_Computing_Optimization_in_Wireless_Powered_Mobile-Edge_Computing_Systems/full.md
- Joint_Offloading_and_Trajectory_Design_for_UAV-Enabled_Mobile_Edge_Computing_Systems/6e3d3fa7-6144-4954-823b-ca11e5c83558_origin.pdf
- Joint_Offloading_and_Trajectory_Design_for_UAV-Enabled_Mobile_Edge_Computing_Systems/full.md
- Joint_Optimization_of_Trajectory_Offloading_Caching_and_Migration_for_UAV-Assisted_MEC/45f67a08-199f-481d-bf29-def86d9ae977_origin.pdf
- Joint_Optimization_of_Trajectory_Offloading_Caching_and_Migration_for_UAV-Assisted_MEC/full.md
- Joint_Optimization_of_Trajectory_and_Jamming_Power_for_Multiple_UAV-Aided_Proactive_Eavesdropping/ba79867e-6f99-4455-8f63-74eb780d7360_origin.pdf
- Joint_Optimization_of_Trajectory_and_Jamming_Power_for_Multiple_UAV-Aided_Proactive_Eavesdropping/full.md
- Joint_RAN_Slicing_and_Computation_Offloading_for_Autonomous_Vehicular_Networks_A_Learning-Assisted_Hierarchical_Approach/6a4901c5-82ae-44c4-92dc-79b7353d819f_origin.pdf
- Joint_RAN_Slicing_and_Computation_Offloading_for_Autonomous_Vehicular_Networks_A_Learning-Assisted_Hierarchical_Approach/full.md
- Joint_Resource_Management_for_Energy-Efficient_UAV-Assisted_SWIPT-MEC_A_Deep_Reinforcement_Learning_Approach/27aace2d-fd3d-44e6-ac23-4a2386878e16_origin.pdf
- Joint_Resource_Management_for_Energy-Efficient_UAV-Assisted_SWIPT-MEC_A_Deep_Reinforcement_Learning_Approach/89454a4b-6d60-4db8-bebf-117cc611ef74_origin.pdf
- Joint_Resource_Management_for_Energy-Efficient_UAV-Assisted_SWIPT-MEC_A_Deep_Reinforcement_Learning_Approach/full.md
- Joint_Resource_and_Trajectory_Optimization_for_Security_in_UAV-Assisted_MEC_Systems/4a0aaa0c-101c-4198-9c6f-efa42d18c909_origin.pdf
- Joint_Resource_and_Trajectory_Optimization_for_Security_in_UAV-Assisted_MEC_Systems/full.md
- Joint_Task_Offloading_DNN_Pruning_and_Computing_Resource_Allocation_for_Fault_Detection_With_Dynamic_Constraints_in_Industrial_IoT/f4368012-c1e7-481d-82ea-3238f4d5cceb_origin.pdf
- Joint_Task_Offloading_DNN_Pruning_and_Computing_Resource_Allocation_for_Fault_Detection_With_Dynamic_Constraints_in_Industrial_IoT/full.md
- Joint_Task_Offloading_Resource_Allocation_and_Trajectory_Design_for_Multi-UAV_Cooperative_Edge_Computing_With_Task_Priority/262c8c5f-9f79-487f-90c8-f7fe10c7a86e_origin.pdf
- Joint_Task_Offloading_Resource_Allocation_and_Trajectory_Design_for_Multi-UAV_Cooperative_Edge_Computing_With_Task_Priority/full.md
- Joint_Task_Offloading_and_Migration_Optimization_in_UAV-Enabled_Dynamic_MEC_Networks/48fff01b-84b5-45c8-b1cb-1065a9ac9683_origin.pdf
- Joint_Task_Offloading_and_Migration_Optimization_in_UAV-Enabled_Dynamic_MEC_Networks/full.md
- Joint_Task_Offloading_and_Resource_Allocation_in_Aerial-Terrestrial_UAV_Networks_With_Edge_and_Fog_Computing_for_Post-Disaster_Rescue/c83b18ed-ed3b-4ee8-98d0-5f04b355c25e_origin.pdf
- Joint_Task_Offloading_and_Resource_Allocation_in_Aerial-Terrestrial_UAV_Networks_With_Edge_and_Fog_Computing_for_Post-Disaster_Rescue/full.md
- Joint_Task_Offloading_and_Resource_Allocation_in_UAV-Enabled_Mobile_Edge_Computing/fd834c11-797d-4d59-af05-b36b8e770e1f_origin.pdf
- Joint_Task_Offloading_and_Resource_Allocation_in_UAV-Enabled_Mobile_Edge_Computing/full.md
- Joint_Trajectory_Design_and_Radio_Resource_Management_for_UAV-Aided_Vehicular_Networks/8b0db62d-3368-4cba-84e8-60b9224fbb27_origin.pdf
- Joint_Trajectory_Design_and_Radio_Resource_Management_for_UAV-Aided_Vehicular_Networks/full.md
- Joint_Trajectory_and_Communication_Design_for_Multi-UAV_Enabled_Wireless_Networks/628b90bc-21d9-46c2-820b-51b7d983d145_origin.pdf
- Joint_Trajectory_and_Communication_Design_for_Multi-UAV_Enabled_Wireless_Networks/full.md
- Joint_Trajectory_and_Communication_Optimization_for_Heterogeneous_Vehicles_in_Maritime_SAR_Multi-Agent_Reinforcement_Learning/4a8adcbe-3ad8-4c44-8016-750ad1aa1b3b_origin.pdf
- Joint_Trajectory_and_Communication_Optimization_for_Heterogeneous_Vehicles_in_Maritime_SAR_Multi-Agent_Reinforcement_Learning/full.md
- Latency_Minimization_Oriented_Hybrid_Offshore_and_Aerial-Based_Multi-Access_Computation_Offloading_for_Marine_Communication_Networks/03e8c28c-720b-4a50-aefc-49203523ab6a_origin.pdf
- Latency_Minimization_Oriented_Hybrid_Offshore_and_Aerial-Based_Multi-Access_Computation_Offloading_for_Marine_Communication_Networks/full.md
- Latency_Minimization_for_UAV-Enabled_URLLC-Based_Mobile_Edge_Computing_Systems/8c257105-871e-495d-a64c-ab887844aaac_origin.pdf
- Latency_Minimization_for_UAV-Enabled_URLLC-Based_Mobile_Edge_Computing_Systems/full.md
- Learning-Assisted_Dynamic_VNF_Selection_and_Chaining_for_6G_Satellite-Ground_Integrated_Networks/37509594-b990-4d21-a1de-ffe7a3823ac0_origin.pdf
- Learning-Assisted_Dynamic_VNF_Selection_and_Chaining_for_6G_Satellite-Ground_Integrated_Networks/full.md
- Learning-Based_NOMA-Enabled_Queue-Aware_Task_Offloading_and_AAV_3D_Trajectory_Planning_for_SAGIN/f675e19d-5e65-4eca-b496-6ddf8afa66dc_origin.pdf
- Learning-Based_NOMA-Enabled_Queue-Aware_Task_Offloading_and_AAV_3D_Trajectory_Planning_for_SAGIN/full.md
- MADDPG-Based_Joint_Service_Placement_and_Task_Offloading_in_MEC_Empowered_AirGround_Integrated_Networks/391ad469-1677-4a96-9d65-31fc8fd0b258_origin.pdf
- MADDPG-Based_Joint_Service_Placement_and_Task_Offloading_in_MEC_Empowered_AirGround_Integrated_Networks/full.md
- MEC_a_Key_Technology_Towards_5g/ffa34831-d2ed-4104-9c48-656c2e8a48e9_origin.pdf
- MEC_a_Key_Technology_Towards_5g/full.md
- MOALF-UAV-MEC_Adaptive_Multiobjective_Optimization_for_UAV-Assisted_Mobile_Edge_Computing_in_Dynamic_IoT_Environments/5563cba4-a83a-4c1c-bf33-64bf581d6168_origin.pdf
- MOALF-UAV-MEC_Adaptive_Multiobjective_Optimization_for_UAV-Assisted_Mobile_Edge_Computing_in_Dynamic_IoT_Environments/full.md
- MOTO_Mobility-Aware_Online_Task_Offloading_With_Adaptive_Load_Balancing_in_Small-Cell_MEC/657f07e6-4a0e-42c1-80a6-7a7ba943dbe4_origin.pdf
- MOTO_Mobility-Aware_Online_Task_Offloading_With_Adaptive_Load_Balancing_in_Small-Cell_MEC/full.md
- Maritime_Coverage_Enhancement_Using_UAVs_Coordinated_With_Hybrid_Satellite-Terrestrial_Networks/d53169d7-206a-47ba-8c25-568377f6560b_origin.pdf
- Maritime_Coverage_Enhancement_Using_UAVs_Coordinated_With_Hybrid_Satellite-Terrestrial_Networks/full.md
- Minimizing_Maximum_Latency_of_Task_Offloading_for_Multi-UAV-Assisted_Maritime_Search_and_Rescue/f97dc680-9b1d-4870-9526-c51a056a7c53_origin.pdf
- Minimizing_Maximum_Latency_of_Task_Offloading_for_Multi-UAV-Assisted_Maritime_Search_and_Rescue/full.md
- Mobile-Edge_Computing_Partial_Computation_Offloading_Using_Dynamic_Voltage_Scaling/b5308b34-ddb9-4e53-99ca-24cfb365458d_origin.pdf
- Mobile-Edge_Computing_Partial_Computation_Offloading_Using_Dynamic_Voltage_Scaling/full.md
- Mobile_Edge_Computing_A_Survey_on_Architecture_and_Computation_Offloading/16e17cfc-0e13-4e67-b4c9-cba4352b6c52_origin.pdf
- Mobile_Edge_Computing_A_Survey_on_Architecture_and_Computation_Offloading/full.md
- Mobile_Edge_Computing_via_a_UAV-Mounted_Cloudlet_Optimization_of_Bit_Allocation_and_Path_Planning/9cb733bb-0121-463c-99d9-147631d7e4d1_origin.pdf
- Mobile_Edge_Computing_via_a_UAV-Mounted_Cloudlet_Optimization_of_Bit_Allocation_and_Path_Planning/full.md
- Mobile_Edge_Deployment_and_Resource_Management_for_Maritime_Wireless_Networks/5a91bf50-456a-46ea-b877-ad1927709055_origin.pdf
- Mobile_Edge_Deployment_and_Resource_Management_for_Maritime_Wireless_Networks/full.md
- Mobile_Unmanned_Aerial_Vehicles_UAVs_for_Energy-Efficient_Internet_of_Things_Communications/b905eb51-494c-4f5b-95c4-b1f8f6ac328f_origin.pdf
- Mobile_Unmanned_Aerial_Vehicles_UAVs_for_Energy-Efficient_Internet_of_Things_Communications/full.md
- Mobility-Aware_Computation_Offloading_in_Satellite_Edge_Computing_Networks/4abbfef3-7758-4baa-b615-29f48b0ee97e_origin.pdf
- Mobility-Aware_Computation_Offloading_in_Satellite_Edge_Computing_Networks/full.md
- Multi-Agent_DRL_for_Task_Offloading_and_Resource_Allocation_in_Multi-UAV_Enabled_IoT_Edge_Network/589beaa0-1417-4773-b24d-ced75e7f14e8_origin.pdf
- Multi-Agent_DRL_for_Task_Offloading_and_Resource_Allocation_in_Multi-UAV_Enabled_IoT_Edge_Network/full.md
- Multi-Agent_Deep_Reinforcement_Learning-Based_Trajectory_Planning_for_Multi-UAV_Assisted_Mobile_Edge_Computing/524effe4-4706-429a-bd3e-4caca19ce2c6_origin.pdf
- Multi-Agent_Deep_Reinforcement_Learning-Based_Trajectory_Planning_for_Multi-UAV_Assisted_Mobile_Edge_Computing/e5d7b673-bd11-43f2-8872-4ceddac8e9b5_origin.pdf
- Multi-Agent_Deep_Reinforcement_Learning-Based_Trajectory_Planning_for_Multi-UAV_Assisted_Mobile_Edge_Computing/full.md
- Multi-Agent_Deep_Reinforcement_Learning_Based_UAV_Trajectory_Optimization_for_Differentiated_Services/386b97ad-2e06-4999-b320-d4c984a5a4d2_origin.pdf
- Multi-Agent_Deep_Reinforcement_Learning_Based_UAV_Trajectory_Optimization_for_Differentiated_Services/full.md
- Multi-Agent_Deep_Reinforcement_Learning_With_Trajectory_Prediction_for_Task_Migration-Assisted_Computation_Offloading/3bbea1fb-03eb-49d6-a0f0-a62cdd12f062_origin.pdf
- Multi-Agent_Deep_Reinforcement_Learning_With_Trajectory_Prediction_for_Task_Migration-Assisted_Computation_Offloading/full.md
- Multi-Agent_Deep_Reinforcement_Learning_for_Task_Offloading_in_UAV-Assisted_Mobile_Edge_Computing/53b68eba-b73b-4572-9649-7095ccf72806_origin.pdf
- Multi-Agent_Deep_Reinforcement_Learning_for_Task_Offloading_in_UAV-Assisted_Mobile_Edge_Computing/full.md
- Multi-Agent_Reinforcement_Learning_Based_Resource_Management_in_MEC-_and_UAV-Assisted_Vehicular_Networks/e792cab5-4bb8-4122-80c1-05a90eb3a865_origin.pdf
- Multi-Agent_Reinforcement_Learning_Based_Resource_Management_in_MEC-_and_UAV-Assisted_Vehicular_Networks/full.md
- Multi-Functional_RIS-Assisted_Semantic_Anti-Jamming_Communication_and_Computing_in_Integrated_Aerial-Ground_Networks/0a6fff1e-ad88-455d-b6a7-6b9286e0d7f9_origin.pdf
- Multi-Functional_RIS-Assisted_Semantic_Anti-Jamming_Communication_and_Computing_in_Integrated_Aerial-Ground_Networks/full.md
- Multi-Objective_Aerial_Collaborative_Secure_Communication_Optimization_via_Generative_Diffusion_Model-Enabled_Deep_Reinforcement_Learning/70a23b38-a360-4605-bd30-d5ae14ccd915_origin.pdf
- Multi-Objective_Aerial_Collaborative_Secure_Communication_Optimization_via_Generative_Diffusion_Model-Enabled_Deep_Reinforcement_Learning/full.md
- Multi-Objective_Optimization_for_UAV_Swarm-Assisted_IoT_With_Virtual_Antenna_Arrays/12c88c8c-3b81-48e0-803f-406912824221_origin.pdf
- Multi-Objective_Optimization_for_UAV_Swarm-Assisted_IoT_With_Virtual_Antenna_Arrays/full.md
- Multi-UAV-Enabled_Load-Balance_Mobile-Edge_Computing_for_IoT_Networks/433300e9-8bca-4615-a50c-95df17076d35_origin.pdf
- Multi-UAV-Enabled_Load-Balance_Mobile-Edge_Computing_for_IoT_Networks/full.md
- Multi-UAV_Aided_Multi-Access_Edge_Computing_in_Marine_Communication_Networks_A_Joint_System-Welfare_and_Energy-Efficient_Design/e4f5bdc2-b3d6-4fcc-abed-6d6335ab3004_origin.pdf
- Multi-UAV_Aided_Multi-Access_Edge_Computing_in_Marine_Communication_Networks_A_Joint_System-Welfare_and_Energy-Efficient_Design/full.md
- Multi-UAV_Cooperative_Task_Offloading_and_Resource_Allocation_in_5G_Advanced_and_Beyond/49030327-45e9-40f6-9943-aad25ec486d1_origin.pdf
- Multi-UAV_Cooperative_Task_Offloading_and_Resource_Allocation_in_5G_Advanced_and_Beyond/full.md
- Multi-UAV_Path_Planning_for_Mobile_Edge_Computing_With_High-Density_Mobile_Devices/9de84584-c0e5-4b27-b085-5256cd556869_origin.pdf
- Multi-UAV_Path_Planning_for_Mobile_Edge_Computing_With_High-Density_Mobile_Devices/full.md
- Multi-User_Task_Offloading_in_UAV-Assisted_LEO_Satellite_Edge_Computing_A_Game-Theoretic_Approach/f0eb5d57-dc3b-4515-85dc-cf2fd20577c0_origin.pdf
- Multi-User_Task_Offloading_in_UAV-Assisted_LEO_Satellite_Edge_Computing_A_Game-Theoretic_Approach/full.md
- Multiobjective_Optimization_Approach_for_Reducing_Hovering_and_Motion_Energy_Consumptions_in_UAV-Assisted_Collaborative_Beamforming/a8fd97f4-7c40-4394-bc5a-bf0986dde220_origin.pdf
- Multiobjective_Optimization_Approach_for_Reducing_Hovering_and_Motion_Energy_Consumptions_in_UAV-Assisted_Collaborative_Beamforming/full.md
- On_a_Hierarchical_Content_Caching_and_Asynchronous_Updating_Scheme_for_Non-Terrestrial_Network-Assisted_Connected_Automated_Vehicles/f75a75c7-9364-4126-8bd3-c62492c2f272_origin.pdf
- On_a_Hierarchical_Content_Caching_and_Asynchronous_Updating_Scheme_for_Non-Terrestrial_Network-Assisted_Connected_Automated_Vehicles/full.md
- On_an_Intelligent_Hierarchical_Routing_Strategy_for_Ultra-Dense_Free_Space_Optical_Low_Earth_Orbit_Satellite_Networks/d64c5633-bd55-4742-8d52-569b69234c67_origin.pdf
- On_an_Intelligent_Hierarchical_Routing_Strategy_for_Ultra-Dense_Free_Space_Optical_Low_Earth_Orbit_Satellite_Networks/full.md
- Online_Computation_Offloading_for_Collaborative_Space_Aerial-Aided_Edge_Computing_Toward_6G_System/068350a2-07a4-4e92-b6db-e5d3e28c52f6_origin.pdf
- Online_Computation_Offloading_for_Collaborative_Space_Aerial-Aided_Edge_Computing_Toward_6G_System/full.md
- Online_Trajectory_and_Resource_Optimization_for_Stochastic_UAV-Enabled_MEC_Systems/30cc749a-4be7-47fe-8892-b46a5f122267_origin.pdf
- Online_Trajectory_and_Resource_Optimization_for_Stochastic_UAV-Enabled_MEC_Systems/full.md
- Optimal_LAP_Altitude_for_Maximum_Coverage/44854c44-6da3-477f-968a-4621e883faa0_origin.pdf
- Optimal_LAP_Altitude_for_Maximum_Coverage/full.md
- Optimal_Task_Offloading_and_Trajectory_Planning_Algorithms_for_Collaborative_Video_Analytics_With_UAV-Assisted_Edge_in_Disaster_Rescue/51a417ff-e883-4afc-9179-ca7f3c146ed3_origin.pdf
- Optimal_Task_Offloading_and_Trajectory_Planning_Algorithms_for_Collaborative_Video_Analytics_With_UAV-Assisted_Edge_in_Disaster_Rescue/full.md
- Optimization_of_Secure_Computation_Efficiency_in_UAV-Enabled_RIS-Assisted_MEC-IoT_Networks_With_Aerial_and_Ground_Eavesdroppers/db6d74ad-4ef3-413b-b703-08049bf6bdd3_origin.pdf
- Optimization_of_Secure_Computation_Efficiency_in_UAV-Enabled_RIS-Assisted_MEC-IoT_Networks_With_Aerial_and_Ground_Eavesdroppers/full.md
- Optimization_of_UAV_Heading_for_the_Ground-to-Air_Uplink/bf1123c7-5ef2-464c-8432-3621f293b9b9_origin.pdf
- Optimization_of_UAV_Heading_for_the_Ground-to-Air_Uplink/full.md
- Optimizing_AIGC_Services_by_Prompt_Engineering_and_Edge_Computing_A_Generative_Diffusion_Model-Based_Contract_Theory_Approach/4f64765d-6919-4fa8-ac26-98022dfb6780_origin.pdf
- Optimizing_AIGC_Services_by_Prompt_Engineering_and_Edge_Computing_A_Generative_Diffusion_Model-Based_Contract_Theory_Approach/full.md
- Optimizing_Secrecy_Rate_for_Federated_Learning_Model_Aggregation_With_Intelligent_Reflecting_Surface_Toward_6G_Ubiquitous_Intelligence/d3ec5f34-da35-4d64-885b-704f6fbce97f_origin.pdf
- Optimizing_Secrecy_Rate_for_Federated_Learning_Model_Aggregation_With_Intelligent_Reflecting_Surface_Toward_6G_Ubiquitous_Intelligence/full.md
- Optimizing_Spectrum_Sharing_in_UAV_Swarms_A_Stackelberg_Game-Based_Incentive_Mechanism/87aa6c9a-017f-4584-9584-dcde07ce843b_origin.pdf
- Optimizing_Spectrum_Sharing_in_UAV_Swarms_A_Stackelberg_Game-Based_Incentive_Mechanism/full.md
- Orchestrating_Federated_Learning_in_Space-Air-_Ground_Integrated_Networks_Adaptive_Data_Offloading_and_Seamless_Handover/5f395380-8451-4fc0-8981-b70a16f3bab0_origin.pdf
- Orchestrating_Federated_Learning_in_Space-Air-_Ground_Integrated_Networks_Adaptive_Data_Offloading_and_Seamless_Handover/full.md
- Over-the-Air_Edge_Inference_for_Low-Altitude_Airspace_Generative_AI-Aided_Multi-Task_Batching_and_Beamforming_Design/6d668a50-906d-42d0-9e25-2095ab35fd4a_origin.pdf
- Over-the-Air_Edge_Inference_for_Low-Altitude_Airspace_Generative_AI-Aided_Multi-Task_Batching_and_Beamforming_Design/full.md
- Partial_Computation_Offloading_in_Satellite-Based_Three-Tier_Cloud-Edge_Integration_Networks/2f562306-355e-49b2-9964-9fd05ff66b39_origin.pdf
- Partial_Computation_Offloading_in_Satellite-Based_Three-Tier_Cloud-Edge_Integration_Networks/full.md
- Placement_Optimization_of_UAV-Mounted_Mobile_Base_Stations/8c3ca32b-93ea-4711-87cf-7f228f997e74_origin.pdf
- Placement_Optimization_of_UAV-Mounted_Mobile_Base_Stations/full.md
- Proximal Policy Optimization Algorithms/3317724e-5664-45cd-9efd-cc1594447c21_origin.pdf
- Proximal Policy Optimization Algorithms/full.md
- QoE-Aware_Decentralized_Task_Offloading_and_Resource_Allocation_for_End-Edge-Cloud_Systems_A_Game-Theoretical_Approach/7b2df536-f23c-4484-bf35-94b2befb4b1e_origin.pdf
- QoE-Aware_Decentralized_Task_Offloading_and_Resource_Allocation_for_End-Edge-Cloud_Systems_A_Game-Theoretical_Approach/full.md
- QoS_Aware_Virtual_Network_Embedding_in_Space-Air-Ground-Ocean_Integrated_Network/d1044579-538a-4faa-ab6c-bab8dbd63f5e_origin.pdf
- QoS_Aware_Virtual_Network_Embedding_in_Space-Air-Ground-Ocean_Integrated_Network/full.md
- Reliable_and_Energy-Efficient_Communications_via_Collaborative_Beamforming_for_UAV_Networks/99fb7d68-f08a-4b0e-a4b0-f1c1313ef24c_origin.pdf
- Reliable_and_Energy-Efficient_Communications_via_Collaborative_Beamforming_for_UAV_Networks/full.md
- Resource_Allocation_and_Trajectory_Design_for_MISO_UAV-Assisted_MEC_Networks/2baa483c-d5f2-4cc5-8924-3e5795ef84c3_origin.pdf
- Resource_Allocation_and_Trajectory_Design_for_MISO_UAV-Assisted_MEC_Networks/full.md
- Resource_and_Trajectory_Optimization_for_UAV-Relay-Assisted_Secure_Maritime_MEC/5199e515-1926-4114-a031-db1383b76209_origin.pdf
- Resource_and_Trajectory_Optimization_for_UAV-Relay-Assisted_Secure_Maritime_MEC/full.md
- Response_Delay_Optimization_in_Mobile_Edge_Computing_Enabled_UAV_Swarm/4dae0c96-f63e-479d-9376-14e31d19df53_origin.pdf
- Response_Delay_Optimization_in_Mobile_Edge_Computing_Enabled_UAV_Swarm/full.md
- Revolutionizing_Future_Connectivity_A_Contemporary_Survey_on_AI-Empowered_Satellite-Based_Non-Terrestrial_Networks_in_6G/b986cb44-7849-4954-ad1c-9a6331d70018_origin.pdf
- Revolutionizing_Future_Connectivity_A_Contemporary_Survey_on_AI-Empowered_Satellite-Based_Non-Terrestrial_Networks_in_6G/full.md
- Robust_Computation_Offloading_and_Trajectory_Optimization_for_Multi-UAV-Assisted_MEC_A_Multiagent_DRL_Approach/75f6c0b3-b5db-4db7-b353-da3ceb59acaa_origin.pdf
- Robust_Computation_Offloading_and_Trajectory_Optimization_for_Multi-UAV-Assisted_MEC_A_Multiagent_DRL_Approach/full.md
- SG-MAPG_A_Three-Layer_Hierarchical_Model_for_Service_Fairness_and_Cost_Optimization_in_UAV-Assisted_MEC_Systems/9cda5e1e-d93e-485a-a648-62e05ef017ee_origin.pdf
- SG-MAPG_A_Three-Layer_Hierarchical_Model_for_Service_Fairness_and_Cost_Optimization_in_UAV-Assisted_MEC_Systems/full.md
- Safe_and_Energy-Efficient_Trajectory_Planning_for_Heterogeneous_Multi-UAV_Enabled_Mobile_Edge_Computing/785caeb4-5dd9-485e-8759-13d68ecef021_origin.pdf
- Safe_and_Energy-Efficient_Trajectory_Planning_for_Heterogeneous_Multi-UAV_Enabled_Mobile_Edge_Computing/full.md
- Secrecy-Driven_Energy_Minimization_in_Federated-Learning-Assisted_Marine_Digital_Twin_Networks/5e0f8e15-6032-4671-91e2-01bb9c9f8537_origin.pdf
- Secrecy-Driven_Energy_Minimization_in_Federated-Learning-Assisted_Marine_Digital_Twin_Networks/full.md
- Secure_Computation_Offloading_for_Marine_IoT_An_Energy-Efficient_Design_via_Cooperative_Jamming/d233d075-7192-4565-84f6-c6a5ccccd3a0_origin.pdf
- Secure_Computation_Offloading_for_Marine_IoT_An_Energy-Efficient_Design_via_Cooperative_Jamming/full.md
- Semantic_Communication_in_Satellite-Borne_Edge_Cloud_Network_for_Computation_Offloading/9b7ac372-87f2-420b-9674-7e8b07b5ba6c_origin.pdf
- Semantic_Communication_in_Satellite-Borne_Edge_Cloud_Network_for_Computation_Offloading/full.md
- Semantic_Successive_Refinement_A_Generative_AI-Aided_Semantic_Communication_Framework/83b7b95c-8032-4d6a-bc2b-be3ce3d7d417_origin.pdf
- Semantic_Successive_Refinement_A_Generative_AI-Aided_Semantic_Communication_Framework/full.md
- Sensing-Assisted_Eavesdropper_Estimation_An_ISAC_Breakthrough_in_Physical_Layer_Security/aaf6f6ef-78ae-4e1a-800b-6da42bdc7573_origin.pdf
- Sensing-Assisted_Eavesdropper_Estimation_An_ISAC_Breakthrough_in_Physical_Layer_Security/full.md
- Sensing-Communication_Co-Design_for_UAV_Swarm-Assisted_Vehicular_Network_in_Perspective_of_Doppler/ffcab5e0-2cf3-40f3-bf90-0c348336bda7_origin.pdf
- Sensing-Communication_Co-Design_for_UAV_Swarm-Assisted_Vehicular_Network_in_Perspective_of_Doppler/full.md
- Service_Experience_Oriented_Cooperative_Computing_in_Cache-Enabled_UAVs_Assisted_MEC_Networks/22637016-68ae-4571-8474-b4efeba95c79_origin.pdf
- Service_Experience_Oriented_Cooperative_Computing_in_Cache-Enabled_UAVs_Assisted_MEC_Networks/full.md
- Service_Migration_or_Task_Rerouting_A_Two-Timescale_Online_Resource_Optimization_for_MEC/61b8a7bd-f66f-449b-85fe-e7bf1ede5c22_origin.pdf
- Service_Migration_or_Task_Rerouting_A_Two-Timescale_Online_Resource_Optimization_for_MEC/full.md
- Space-Air-Ground_Integrated_Networks_Spherical_Stochastic_Geometry-Based_Uplink_Connectivity_Analysis/c906bc17-555e-4351-9cb3-ea225f2ecc98_origin.pdf
- Space-Air-Ground_Integrated_Networks_Spherical_Stochastic_Geometry-Based_Uplink_Connectivity_Analysis/full.md
- Space_Aerial-Assisted_Computing_Offloading_for_IoT_Applications_A_Learning-Based_Approach/9555c1e6-ad9d-41df-892a-0e90db6b7b9a_origin.pdf
- Space_Aerial-Assisted_Computing_Offloading_for_IoT_Applications_A_Learning-Based_Approach/full.md
- Stochastic_Computation_Offloading_and_Trajectory_Scheduling_for_UAV-Assisted_Mobile_Edge_Computing/550b65f0-aa65-4137-baf9-47e6813dfd4c_origin.pdf
- Stochastic_Computation_Offloading_and_Trajectory_Scheduling_for_UAV-Assisted_Mobile_Edge_Computing/full.md
- TJCCT_A_Two-Timescale_Approach_for_UAV-Assisted_Mobile_Edge_Computing/62b7bcf3-5154-4512-b471-5e2054700086_origin.pdf
- TJCCT_A_Two-Timescale_Approach_for_UAV-Assisted_Mobile_Edge_Computing/full.md
- Task-Driven_Priority-Aware_Computation_Offloading_Using_Deep_Reinforcement_Learning/2b1402e9-c5b7-4f8a-9337-d3da5a04b105_origin.pdf
- Task-Driven_Priority-Aware_Computation_Offloading_Using_Deep_Reinforcement_Learning/full.md
- Task-Oriented_Sensing_Computation_and_Communication_Integration_for_Multi-Device_Edge_AI/3601f6e6-6f6a-4eda-9762-24c711523051_origin.pdf
- Task-Oriented_Sensing_Computation_and_Communication_Integration_for_Multi-Device_Edge_AI/full.md
- Terrain-Aware_UAV-Enabled_Mobile_Edge_Computing_in_Urban_Environments_A_Constrained_Multi-Objective_Approach_With_Task-Adaptive_Mechanism/20d2321e-85c6-423b-8fe7-5f0803a7637f_origin.pdf
- Terrain-Aware_UAV-Enabled_Mobile_Edge_Computing_in_Urban_Environments_A_Constrained_Multi-Objective_Approach_With_Task-Adaptive_Mechanism/full.md
- Through_the_Wall_Detection_and_Localization_of_Autonomous_Mobile_Device_in_Indoor_Scenario/a9952e0a-efdd-4168-93f1-28d96920cf64_origin.pdf
- Through_the_Wall_Detection_and_Localization_of_Autonomous_Mobile_Device_in_Indoor_Scenario/full.md
- Throughput_Maximization_for_UAV-Enabled_Mobile_Relaying_Systems/bd69614b-7555-41f0-aad4-3ae54b41e5f2_origin.pdf
- Throughput_Maximization_for_UAV-Enabled_Mobile_Relaying_Systems/full.md
- Time_and_Energy_Minimization_Communications_Based_on_Collaborative_Beamforming_for_UAV_Networks_A_Multi-Objective_Optimization_Method/52805bd9-edb4-4562-b064-8e6812a647af_origin.pdf
- Time_and_Energy_Minimization_Communications_Based_on_Collaborative_Beamforming_for_UAV_Networks_A_Multi-Objective_Optimization_Method/full.md
- Toward_Realization_of_Low-Altitude_Economy_Networks_Core_Architecture_Integrated_Technologies_and_Future_Directions/e609bbbb-d1d3-4e5b-84cc-22cbbc900778_origin.pdf
- Toward_Realization_of_Low-Altitude_Economy_Networks_Core_Architecture_Integrated_Technologies_and_Future_Directions/full.md
- Traffic-Aware_Lightweight_Hierarchical_Offloading_Toward_Adaptive_Slicing-Enabled_SAGIN/ca44e888-13c5-4031-abd4-7f82f289aab3_origin.pdf
- Traffic-Aware_Lightweight_Hierarchical_Offloading_Toward_Adaptive_Slicing-Enabled_SAGIN/full.md
- Trajectory_Design_and_Resource_Allocation_for_Multi-UAV_Networks_Deep_Reinforcement_Learning_Approaches/a578795f-48fe-44c7-8b8a-905efa289a02_origin.pdf
- Trajectory_Design_and_Resource_Allocation_for_Multi-UAV_Networks_Deep_Reinforcement_Learning_Approaches/full.md
- Two-Hop_Packet_Scheduling_Resource_Allocation_and_UAV_Trajectory_Design_for_Internet_of_Remote_Things_in_AirGround_Integrated_Network/856f284a-fd96-4ea7-be3c-a346965b1bb5_origin.pdf
- Two-Hop_Packet_Scheduling_Resource_Allocation_and_UAV_Trajectory_Design_for_Internet_of_Remote_Things_in_AirGround_Integrated_Network/full.md
- Two-Hop_Partial_Task_Offloading_and_Resource_Allocation_in_AirGround_Integrated_Mobile_Edge_Computing_Network_A_DRL-Based_Method/6228b26c-2629-40a4-824a-8ab71fafd31c_origin.pdf
- Two-Hop_Partial_Task_Offloading_and_Resource_Allocation_in_AirGround_Integrated_Mobile_Edge_Computing_Network_A_DRL-Based_Method/full.md
- Two-Stage_Deep_Energy_Optimization_in_IRS-Assisted_UAV-Based_Edge_Computing_Systems/6c4973d7-6eea-4a44-a471-8abc8b4bfeff_origin.pdf
- Two-Stage_Deep_Energy_Optimization_in_IRS-Assisted_UAV-Based_Edge_Computing_Systems/full.md
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach/16d5d3d1-67b2-4dd9-b065-9e963d14a649_origin.pdf
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach/870fe0f8-bcb9-4139-95ef-9aecd3daea78_origin.pdf
- Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach/full.md
- UAV-Aided_Offloading_for_Cellular_Hotspot/2f0c1474-9740-470d-8888-51b79d0d1a1e_origin.pdf
- UAV-Aided_Offloading_for_Cellular_Hotspot/full.md
- UAV-Assisted_Emergency_Networks_in_Disasters/a1edd2c9-73b0-4630-b6f9-3df0f62d486d_origin.pdf
- UAV-Assisted_Emergency_Networks_in_Disasters/full.md
- UAV-Assisted_MEC_System_With_Mobile_Ground_Terminals_DRL-Based_Joint_Terminal_Scheduling_and_UAV_3D_Trajectory_Design/4a3feac9-db40-4ecd-b608-16d91416d80f_origin.pdf
- UAV-Assisted_MEC_System_With_Mobile_Ground_Terminals_DRL-Based_Joint_Terminal_Scheduling_and_UAV_3D_Trajectory_Design/full.md
- UAV-Assisted_Multi-Access_Computation_Offloading_via_Hybrid_NOMA_and_FDMA_in_Marine_Networks/72487898-fd98-43fc-a18d-37adf2fb31be_origin.pdf
- UAV-Assisted_Multi-Access_Computation_Offloading_via_Hybrid_NOMA_and_FDMA_in_Marine_Networks/full.md
- UAV-Assisted_Relaying_and_Edge_Computing_Scheduling_and_Trajectory_Optimization/e6056c62-47d4-46ff-aeb8-b642b0db0488_origin.pdf
- UAV-Assisted_Relaying_and_Edge_Computing_Scheduling_and_Trajectory_Optimization/full.md
- UAV-Assisted_Task_Offloading_in_Edge_Computing/29225c6d-e56f-4b9d-8974-8a76c9df34b5_origin.pdf
- UAV-Assisted_Task_Offloading_in_Edge_Computing/full.md
- UAV-Assisted_Task_Offloading_in_Vehicular_Edge_Computing_Networks/a22d9cc1-13ea-401b-aa5b-c70531ba6991_origin.pdf
- UAV-Assisted_Task_Offloading_in_Vehicular_Edge_Computing_Networks/full.md
- UAV-Assisted_Wireless_Powered_Cooperative_Mobile_Edge_Computing_Joint_Offloading_CPU_Control_and_Trajectory_Optimization/2962fa3f-7ae0-4452-bd0f-48a9d634c25e_origin.pdf
- UAV-Assisted_Wireless_Powered_Cooperative_Mobile_Edge_Computing_Joint_Offloading_CPU_Control_and_Trajectory_Optimization/full.md
- UAV-Enabled_Collaborative_Beamforming_via_Multi-Agent_Deep_Reinforcement_Learning/b2e661db-ca7f-4a77-afb9-eb2a0bd0d798_origin.pdf
- UAV-Enabled_Collaborative_Beamforming_via_Multi-Agent_Deep_Reinforcement_Learning/full.md
- UAV-Enabled_Integrated_Sensing_and_Communication_Opportunities_and_Challenges/a8642c8e-2515-4841-8dc0-6d98cbff3be7_origin.pdf
- UAV-Enabled_Integrated_Sensing_and_Communication_Opportunities_and_Challenges/full.md
- UAV-Enabled_Multi-Source_Data_Fusion_in_Vehicular_Networks_A_Joint_Optimization_Approach_for_Reliability_and_Latency/3f0640e8-069b-47ea-8844-e0100315d78c_origin.pdf
- UAV-Enabled_Multi-Source_Data_Fusion_in_Vehicular_Networks_A_Joint_Optimization_Approach_for_Reliability_and_Latency/MinerU_markdown_202605131927481_3b25f7d3.md
- UAV-Enabled_Multi-Source_Data_Fusion_in_Vehicular_Networks_A_Joint_Optimization_Approach_for_Reliability_and_Latency/full.md
- UAV-Enabled_Secure_Communications_via_Collaborative_Beamforming_With_Imperfect_Eavesdropper_Information/b0b407e8-9ff7-4831-a73e-9d790e1b975a_origin.pdf
- UAV-Enabled_Secure_Communications_via_Collaborative_Beamforming_With_Imperfect_Eavesdropper_Information/full.md
- UAV-Enabled_Secure_ISAC_Against_Dual_Eavesdropping_Threats_Joint_Beamforming_and_Trajectory_Design/b189403a-de1d-405c-839d-7c4db1c48c4b_origin.pdf
- UAV-Enabled_Secure_ISAC_Against_Dual_Eavesdropping_Threats_Joint_Beamforming_and_Trajectory_Design/full.md
- UAV-Enabled_Wireless_Power_Transfer_Trajectory_Design_and_Energy_Optimization/7aaece4b-2696-4b7f-b602-3ee5873bc8b3_origin.pdf
- UAV-Enabled_Wireless_Power_Transfer_Trajectory_Design_and_Energy_Optimization/full.md
- URLLC-Aware_Trajectory_Plan_and_Beamforming_Design_for_NOMA-Aided_UAV_Integrated_Sensing_Communication_and_Computation_Networks/7a31a63e-9364-4a38-87d6-32b0d5dcf1fa_origin.pdf
- URLLC-Aware_Trajectory_Plan_and_Beamforming_Design_for_NOMA-Aided_UAV_Integrated_Sensing_Communication_and_Computation_Networks/full.md
- USV_Fleet-Assisted_Collaborative_Computation_Offloading_for_Smart_Maritime_Services_An_Energy-Efficient_Design/3dff6c8e-38ab-46fe-9bc5-a9865789b6f2_origin.pdf
- USV_Fleet-Assisted_Collaborative_Computation_Offloading_for_Smart_Maritime_Services_An_Energy-Efficient_Design/full.md
- Unleashing_the_Power_of_Edge-Cloud_Generative_AI_in_Mobile_Networks_A_Survey_of_AIGC_Services/2daf7688-fbfa-4594-bf8e-78567f6b4e65_origin.pdf
- Unleashing_the_Power_of_Edge-Cloud_Generative_AI_in_Mobile_Networks_A_Survey_of_AIGC_Services/full.md
- Unmanned_Aerial_Vehicle_With_Underlaid_Device-to-Device_Communications_Performance_and_Tradeoffs/8090181e-977c-4e03-95bb-bdc99eb016ee_origin.pdf
- Unmanned_Aerial_Vehicle_With_Underlaid_Device-to-Device_Communications_Performance_and_Tradeoffs/full.md
- Wireless_Relay_Communications_with_Unmanned_Aerial_Vehicles_Performance_and_Optimization/719259e0-762f-4830-9833-6e73bcef8d08_origin.pdf
- Wireless_Relay_Communications_with_Unmanned_Aerial_Vehicles_Performance_and_Optimization/full.md
- Wireless_communications_with_unmanned_aerial_vehicles_opportunities_and_challenges/cbb2ff13-ea2e-4e31-8060-2bdc8779c37b_origin.pdf
- Wireless_communications_with_unmanned_aerial_vehicles_opportunities_and_challenges/full.md
- YOLO-Based_Semantic_Communication_With_Generative_AI-Aided_Resource_Allocation_for_Digital_Twins_Construction/72143137-933e-46b2-b1e8-aaf9d3713ec3_origin.pdf
- YOLO-Based_Semantic_Communication_With_Generative_AI-Aided_Resource_Allocation_for_Digital_Twins_Construction/full.md
## [2026-07-07] curation pass: secure offloading, LAE privacy trajectory, and cooperative ISAC | 5 sources, 3 concepts

Curated five raw sources from the uncurated backlog:

- [[beishenalieva-2026-secrecy-aware-uav-path-planning]] — secrecy-aware UAV-ITS offloading with policy-gradient DRL, legitimate jamming, malicious aerial eavesdroppers/jammers, and PSO slot allocation.
- [[wu-2026-secure-split-offloading-ci]] — secure UAV-assisted collaborative DNN inference with multi-exit DNNs, dual-UAV trajectory design, cooperative jamming, SCA, and discrete WOA.
- [[wu-2025-security-aware-multiuav-service-placement]] — security-aware multi-UAV MEC deployment, offloading, service placement, and UAV-jammer power via OE-MATD3 plus closed-form device transmit power.
- [[wu-2026-service-oriented-segmented-trajectory]] — low-altitude high-rise UAV-MEC trajectory design with VSRL-LKH, TRA/SOS-TRA, service segmentation, and smart-window trajectory privacy.
- [[wang-2026-stbc-cooperative-isac]] — multi-BS cooperative ISAC with robust inter-BS nulling, space-time block codec echo separation, and SINR-weighted data fusion.

Added three concept pages: [[multi-exit-dnn]], [[trajectory-privacy]], and [[space-time-block-codec]]. Updated backlinks for PSO, collaborative inference, DNN partitioning, friendly-jamming UAVs, PLS, MATD3, service caching, networked ISAC, ISAC, CRB, LAIN, trajectory control, offloading, UAV-ITS, PPO, WOA, AO/SCA, and the [[zhiyong-feng]] entity page.

Process notes:

- DOI/venue/year for parse-silent metadata were verified through title-matched Crossref/IEEE DOI records; source claims remain grounded in the parsed Markdown.
- Local counts after the pass: 339 sources, 315 concepts, 73 entities, 345 raw folders.

## [2026-07-06] external batch delete | 22 source files

Deleted 22 source files and 0 wiki pages.

Sources:
- Energy-Efficient_UAV_Communication_With_Trajectory_Optimization/Energy-Efficient_UAV_Communication_With_Trajectory_Optimization.md
- Energy-Efficient_UAV_Communication_With_Trajectory_Optimization/Energy-Efficient_UAV_Communication_With_Trajectory_Optimization.pdf
- Energy_Minimization_for_Wireless_Communication_With_Rotary-Wing_UAV/Energy_Minimization_for_Wireless_Communication_With_Rotary-Wing_UAV.md
- Energy_Minimization_for_Wireless_Communication_With_Rotary-Wing_UAV/Energy_Minimization_for_Wireless_Communication_With_Rotary-Wing_UAV.pdf
- HAP-UAV-Assisted Maritime IoT Communication Network/HAP-UAV-Assisted Maritime IoT Communication Network.md
- HAP-UAV-Assisted Maritime IoT Communication Network/HAP-UAV-Assisted Maritime IoT Communication Network.pdf
- Integrated_Sensing_Computation_and_Communication_for_UAV-Assisted_Federated_Edge_Learning/Integrated_Sensing_Computation_and_Communication_for_UAV-Assisted_Federated_Edge_Learning.md
- Integrated_Sensing_Computation_and_Communication_for_UAV-Assisted_Federated_Edge_Learning/Integrated_Sensing_Computation_and_Communication_for_UAV-Assisted_Federated_Edge_Learning.pdf
- Joint_Trajectory_and_Communication_Design_for_Multi-UAV_Enabled_Wireless_Networks/Joint_Trajectory_and_Communication_Design_for_Multi-UAV_Enabled_Wireless_Networks.md
- Joint_Trajectory_and_Communication_Design_for_Multi-UAV_Enabled_Wireless_Networks/Joint_Trajectory_and_Communication_Design_for_Multi-UAV_Enabled_Wireless_Networks.pdf
- Mobile_Unmanned_Aerial_Vehicles_UAVs_for_Energy-Efficient_Internet_of_Things_Communications/Mobile_Unmanned_Aerial_Vehicles_UAVs_for_Energy-Efficient_Internet_of_Things_Communications.md
- Mobile_Unmanned_Aerial_Vehicles_UAVs_for_Energy-Efficient_Internet_of_Things_Communications/Mobile_Unmanned_Aerial_Vehicles_UAVs_for_Energy-Efficient_Internet_of_Things_Communications.pdf
- Multi-Objective_Aerial_Collaborative_Secure_Communication_Optimization_via_Generative_Diffusion_Model-Enabled_Deep_Reinforcement_Learning/Multi-Objective_Aerial_Collaborative_Secure_Communication_Optimization_via_Generative_Diffusion_Model-Enabled_Deep_Reinforcement_Learning.md
- Multi-Objective_Aerial_Collaborative_Secure_Communication_Optimization_via_Generative_Diffusion_Model-Enabled_Deep_Reinforcement_Learning/Multi-Objective_Aerial_Collaborative_Secure_Communication_Optimization_via_Generative_Diffusion_Model-Enabled_Deep_Reinforcement_Learning.pdf
- Multi-Objective_Optimization_for_UAV_Swarm-Assisted_IoT_With_Virtual_Antenna_Arrays/Multi-Objective_Optimization_for_UAV_Swarm-Assisted_IoT_With_Virtual_Antenna_Arrays.md
- Multi-Objective_Optimization_for_UAV_Swarm-Assisted_IoT_With_Virtual_Antenna_Arrays/Multi-Objective_Optimization_for_UAV_Swarm-Assisted_IoT_With_Virtual_Antenna_Arrays.pdf
- UAV-Enabled_Multi-Source_Data_Fusion_in_Vehicular_Networks_A_Joint_Optimization_Approach_for_Reliability_and_Latency/UAV-Enabled_Multi-Source_Data_Fusion_in_Vehicular_Networks_A_Joint_Optimization_Approach_for_Reliability_and_Latency.md
- UAV-Enabled_Multi-Source_Data_Fusion_in_Vehicular_Networks_A_Joint_Optimization_Approach_for_Reliability_and_Latency/UAV-Enabled_Multi-Source_Data_Fusion_in_Vehicular_Networks_A_Joint_Optimization_Approach_for_Reliability_and_Latency.pdf
- UAV-Enabled_Wireless_Power_Transfer_Trajectory_Design_and_Energy_Optimization/UAV-Enabled_Wireless_Power_Transfer_Trajectory_Design_and_Energy_Optimization.md
- UAV-Enabled_Wireless_Power_Transfer_Trajectory_Design_and_Energy_Optimization/UAV-Enabled_Wireless_Power_Transfer_Trajectory_Design_and_Energy_Optimization.pdf
- Unmanned_Aerial_Vehicle_With_Underlaid_Device-to-Device_Communications_Performance_and_Tradeoffs/Unmanned_Aerial_Vehicle_With_Underlaid_Device-to-Device_Communications_Performance_and_Tradeoffs.md
- Unmanned_Aerial_Vehicle_With_Underlaid_Device-to-Device_Communications_Performance_and_Tradeoffs/Unmanned_Aerial_Vehicle_With_Underlaid_Device-to-Device_Communications_Performance_and_Tradeoffs.pdf
