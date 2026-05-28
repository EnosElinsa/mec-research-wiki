# Wiki Index

## Sources (curated)

### Compute offloading & DRL

- [[liu-2026-jppo-en-convntm]] — Liu et al. 2026. Multi-UAV path planning for MEC under high-density mobility. *j-PPO+EN-ConvNTM* (hybrid-action PPO + memory-augmented encoder).
- [[hao-2025-priority-aware-task-driven-co]] — Hao et al. 2025. Task-driven priority-aware computation offloading via DRL.
- [[zhu-2025-lycnn-drl-wpt-mec]] — Zhu et al. 2025. Long-term EE in WPT-MEC via Lyapunov-guided CNN actor + KKT sub-problem.
- [[ma-2025-pdqn-vehicular-mec]] — Ma et al. 2025. Hybrid-action **P-DQN** for binary-offloading + power allocation in three-tier vehicular MEC.

### Multi-agent UAV-MEC

- [[peng-2025-drudm-cfg]] — Peng et al. 2025. Fairness-aware multi-agent DRL for HAS-UAV post-disaster MEC. *DRUDM-CFG*.
- [[zhang-2025-ssac-mgi-heterogeneous-uav]] — Zhang et al. 2025. Safe & energy-efficient trajectory planning for heterogeneous UAV-MEC. *SSAC-MGI* (shared SAC + Markov game of intervention).
- [[bi-2025-sg-mapg]] — Bi et al. 2025. Three-layer hierarchical Stackelberg game for UAV-MEC service fairness & cost. *SG-MAPG*.

### Hierarchical aerial MEC (UAV + HAP)

- [[nabi-2025-jour-hierarchical-aerial]] — Nabi & Moh 2025. *JOUR* — Gale-Shapley matching + ESAC for joint offloading, association, and resource allocation in UAV+HAP MEC.
- [[bao-2025-ddpg-video-offloading]] — Bao et al. 2025. UAV+HAP video-analytics offloading with adaptive transcoding; DDPG over a QoE reward.
- [[jia-2025-dro-uav-hap-mec]] — Jia et al. 2025. **Distributionally robust** UAV-HAP MEC under uncertain CSI; CVaR + primal decomposition + BWOA.

### Vehicular MEC

- [[zhang-2025-mcma-task-migration]] — Zhang et al. 2025. Task migration with Informer trajectory prediction across edge servers. *MCMA*.
- [[xie-2026-uav-multisource-fusion]] — Xie et al. 2026. UAV-enabled cooperative perception fusion via dynamic constrained multi-objective optimization.

### Maritime MEC

- [[wang-2026-aerial-marine-msar]] — Wang et al. 2026. UAV+HAPS+MASS three-tier MEC for maritime search & rescue. *JCORA* (matching + convex + PGD).
- [[liu-2025-haps-uav-maritime-iot]] — Liu et al. 2025. HAP-UAV maritime IoT comm: HAP-as-backhaul, UAV multicast, vessel unicast.

### Trust, security, and federated MEC

- [[mao-2025-bcsa-frl]] — Mao et al. 2025. Blockchain-enabled cold-start FRL for ZT LEO satellite networks. *BCSA-FRL* (CCVM + CSRA).
- [[qin-2025-bcuav-masac]] — Qin et al. 2025. Blockchain-enabled secure UAV-MEC: Lyapunov + MASAC + DOA.
- [[benaya-2025-aerial-isac-haps]] — Benaya et al. 2025. HAPS-mounted FD ISAC + friendly-jamming UAV + ground MEC; AO + SDR + SCA.

### Architectural / spectrum / governance

- [[wang-2025-uav-swarm-stackelberg]] — Wang et al. 2025. Stackelberg-game spectrum sharing for U2U/U2B in UAV swarms.
- [[wang-2025-lae-network-survey]] — Wang et al. 2025. Survey: low-altitude economy network architecture, integrated technologies, and future directions.
- [[jiang-2025-isac-lae-overview]] — Jiang et al. 2025. ISAC for LAE — IAGN architecture, MBCM channel model, stochastic-geometry analysis.
- [[hsu-2025-drl-hues-hap-noma]] — Hsu et al. 2025. **HAP** transmission + RF energy harvesting in NOMA SAGINs; PPO-based DRL-HUES.

### CMOP / evolutionary UAV-MEC (Peng/Huang lineage)

- [[peng-2022-cmop-uav-path-planning]] — Peng et al. 2022. **Lineage seed** — CMOP for UAV path planning + offloading; infeasibility-utilization CMOEA.
- [[peng-2024-energy-time-uav-its]] — Peng et al. 2024. UAV-ITS energy + completion-time-difference; CMOEA/D-CDP + repair + service caching.
- [[huang-2023-mu-aec-task-energy]] — Huang et al. 2023. Multi-UAV interdependent (DAG) tasks; makespan + energy balancing; CMOEA + local search.
- [[huang-2025-cmop-dispersed-computing]] — Huang et al. 2025. Dispersed computing with task-redundancy reliability; dual-population CMOEA.
- [[wu-2026-terrain-aware-uav-mec]] — Wu et al. 2026. Urban UAV-MEC with terrain-aware channel + B-spline trajectory; multi-tasking CMOEA.

### Energy efficiency & WPT

- [[zhu-2025-lycnn-drl-wpt-mec]] — Zhu et al. 2025. Single-source so far.

### Generic offloading techniques

- [[hao-2025-priority-aware-task-driven-co]] — Hao et al. 2025. Single-source so far.

## Entities

### Authors

- [[lihan-liu]], [[hongrui-miao]], [[chunhui-qu]], [[zhuwei-wang]], [[haijun-zhang]], [[zhidu-li]] — co-authors of [[liu-2026-jppo-en-convntm]].
- [[chaoda-peng]], [[xumin-huang]], [[yuan-wu]], [[jiawen-kang]] — recurring co-authors across the [[cmop-evolutionary-uav-mec-lineage|CMOP-evolutionary UAV-MEC lineage]] (4–6 sources each).

### Tools

- [[pytorch]] — DL framework.

(More authors appear in source frontmatter; entity pages currently exist for the central recurring contributors. Future entity pages should land here as more authors recur.)

## Concepts

### MEC fundamentals

- [[mobile-edge-computing]]
- [[task-offloading]]
- [[task-migration]]
- [[binary-vs-partial-offloading]]
- [[event-driven-vs-slot-driven-offloading]]
- [[task-priority-in-mec]]
- [[wireless-power-transfer]]
- [[rf-energy-harvesting]]
- [[noma]]
- [[cooperative-perception]]
- [[multi-source-data-fusion]]
- [[video-analytics-offloading]]
- [[video-transcoding-tradeoff]]
- [[qoe-modeling-mec]]
- [[service-caching-mec]]
- [[parallel-vs-serial-processing]]
- [[task-redundancy-for-reliability]]
- [[dispersed-computing]]

### Aerial / network architectures

- [[multi-uav-assisted-mec]]
- [[high-density-mobile-device-scenarios]]
- [[heterogeneous-uav-fleet]]
- [[high-altitude-platform-station]]
- [[hierarchical-aerial-mec]]
- [[air-ground-integrated-network]]
- [[low-altitude-intelligent-network]]
- [[leo-satellite-edge-computing]]
- [[space-air-ground-integrated-network]]
- [[vehicular-mec]]
- [[uav-enabled-its]]
- [[maritime-mec]]
- [[post-disaster-mec]]
- [[three-tier-cloud-edge-end]]
- [[wireless-backhaul]]

### UAV control & decisions

- [[uav-trajectory-control]]
- [[uav-charging-scheduling]]
- [[gauss-markov-mobility-model]]
- [[hybrid-action-decision-making]]
- [[b-spline-trajectory]]

### DRL backbones

- [[ppo]] · [[j-ppo]]
- [[ddqn]]
- [[ddpg]]
- [[masac]]
- [[parameterized-dqn]]
- [[gae]]
- [[pomdp]] · [[ma-pomdp]]
- [[centralized-training-decentralized-execution]]
- [[adaptive-entropy-priority-replay]]
- [[prioritized-experience-replay]]
- [[safe-reinforcement-learning]]

### Memory / encoders

- [[ntm]] · [[en-convntm]]
- [[convlstm]]
- [[stn]]
- [[informer-trajectory-prediction]]

### Optimization techniques (classical & evolutionary)

- [[lyapunov-optimization]]
- [[fractional-programming-dinkelbach]]
- [[stackelberg-game]]
- [[matching-theory-for-resource-allocation]]
- [[gale-shapley-matching]]
- [[overlay-underlay-spectrum-access]]
- [[unicast-multicast-cooperation]]
- [[dynamic-constrained-multi-objective-optimization]]
- [[constrained-multi-objective-evolutionary-algorithm]]
- [[cmoea-d-cdp]]
- [[infeasible-individual-utilization]]
- [[dual-population-evolutionary-algorithm]]
- [[multi-tasking-evolutionary-algorithm]]
- [[local-search-evolutionary]]
- [[two-stage-decomposition]]
- [[alternating-optimization-sdr-sca]]
- [[binary-whale-optimization]]
- [[multi-verse-optimizer]]
- [[weighted-kmeans-uav-deployment]]
- [[chance-constraint]]
- [[conditional-value-at-risk]]
- [[distributionally-robust-optimization]]

### Channel modeling

- [[blockage-aware-channel-model]]
- [[terrain-aware-channel-model]]
- [[stochastic-geometry-network-analysis]]
- [[csi-estimation-error]]

### Sensing & security

- [[integrated-sensing-and-communication]]
- [[physical-layer-security]]
- [[friendly-jamming-uav]]

### Security / trust / federation

- [[zero-trust-architecture]]
- [[federated-reinforcement-learning]]
- [[blockchain-for-fl-aggregation]]
- [[ccvm-correction-voting]]
- [[csra-cold-start-reputation-aggregation]]
- [[fl-poisoning-attacks]]

### Metrics & fairness

- [[equilibrium-efficiency-metric]]
- [[spatial-equity-index]]
- [[energy-expenditure-coefficient]]
- [[theil-fairness-index]]
- [[completion-time-difference]]
- [[makespan-minimization]]
- [[energy-balancing-uav]]
- [[load-balancing-uav-mec]]

### Scheduling

- [[interdependent-tasks-dag]]

### Safety

- [[collision-avoidance-mgi]]

### Adjacent / forward-looking

- [[generative-ai-for-mec]] (placeholder — no deep-dive source curated yet)

## Methodology

- [[drl-simulation-with-pomdp-formulation]] — POMDP simulation protocol used in [[liu-2026-jppo-en-convntm]]

## Findings

- [[en-convntm-beats-baselines]]
- [[neuralmap-loses-spatial-info]]
- [[uav-count-inverted-u-energy]]
- [[charging-stations-improve-efficiency]]
- [[hybrid-action-beats-pure-drl]]
- [[finding-optimal-loss-entropy-weight-coefs]]
- [[bcsa-frl-tolerates-up-to-half-malicious-satellites]]

## Thesis

- [[hybrid-action-memory-augmented-drl-wins-uav-mec]]

## Queries

- [[query-does-en-convntm-generalize-beyond-uav-mec]]
- [[query-real-world-validation-of-jppo-en-convntm]]

## Comparisons

- [[ddpg-vs-jppo]]
- [[j-ppo-baselines]]
- [[bcsa-frl-vs-bc-uav-masac]] — Blockchain-on-edge: BCSA-FRL vs BC-UAV-MASAC

## Synthesis

- [[design-recipe-multi-uav-mec]] — 10-step recipe for DRL-controlled UAV-MEC.
- [[drl-backbones-across-uav-mec-sources]] — Cross-corpus DRL-backbone analysis (12 sources).
- [[maddpg-vs-masac-in-mec]] — When entropy beats determinism in cooperative MEC.
- [[cmop-evolutionary-uav-mec-lineage]] — Peng/Huang group's 6-paper CMOP-evolutionary lineage (2022-2026).
- [[hierarchical-aerial-mec-design-space]] — Cross-comparison of the 5 UAV+HAP hierarchical-MEC sources.
- [[drl-vs-evolutionary-vs-classical-solvers]] — Solver-family analysis across all 26 sources.
