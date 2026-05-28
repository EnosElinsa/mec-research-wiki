# Wiki Index

## Sources (curated)

### Compute offloading & DRL

- [[liu-2026-jppo-en-convntm]] — Liu et al. 2026. Multi-UAV path planning for MEC under high-density mobility. *j-PPO+EN-ConvNTM* (hybrid-action PPO + memory-augmented encoder).
- [[hao-2025-priority-aware-task-driven-co]] — Hao et al. 2025. Task-driven priority-aware computation offloading via DRL.
- [[zhu-2025-lycnn-drl-wpt-mec]] — Zhu et al. 2025. Long-term EE in WPT-MEC via Lyapunov-guided CNN actor + KKT sub-problem.

### Multi-agent UAV-MEC

- [[peng-2025-drudm-cfg]] — Peng et al. 2025. Fairness-aware multi-agent DRL for HAS-UAV post-disaster MEC. *DRUDM-CFG*.
- [[zhang-2025-ssac-mgi-heterogeneous-uav]] — Zhang et al. 2025. Safe & energy-efficient trajectory planning for heterogeneous UAV-MEC. *SSAC-MGI* (shared SAC + Markov game of intervention).
- [[bi-2025-sg-mapg]] — Bi et al. 2025. Three-layer hierarchical Stackelberg game for UAV-MEC service fairness & cost. *SG-MAPG*.

### Vehicular MEC

- [[zhang-2025-mcma-task-migration]] — Zhang et al. 2025. Task migration with Informer trajectory prediction across edge servers. *MCMA*.
- [[xie-2026-uav-multisource-fusion]] — Xie et al. 2026. UAV-enabled cooperative perception fusion via dynamic constrained multi-objective optimization.

### Trust, security, and federated MEC

- [[mao-2025-bcsa-frl]] — Mao et al. 2025. Blockchain-enabled cold-start FRL for ZT LEO satellite networks. *BCSA-FRL* (CCVM + CSRA).
- [[qin-2025-bcuav-masac]] — Qin et al. 2025. Blockchain-enabled secure UAV-MEC: Lyapunov + MASAC + DOA.

### Architectural / spectrum / governance

- [[wang-2025-uav-swarm-stackelberg]] — Wang et al. 2025. Stackelberg-game spectrum sharing for U2U/U2B in UAV swarms.
- [[wang-2025-lae-network-survey]] — Wang et al. 2025. Survey: low-altitude economy network architecture, integrated technologies, and future directions.

## Entities

- [[lihan-liu]], [[hongrui-miao]], [[chunhui-qu]], [[zhuwei-wang]], [[haijun-zhang]], [[zhidu-li]] — co-authors of [[liu-2026-jppo-en-convntm]]
- [[pytorch]] — DL framework

(More authors appear in source frontmatter but only the first source's authors have entity pages so far. Future entity pages should land here as the authors recur.)

## Concepts

### MEC fundamentals

- [[mobile-edge-computing]]
- [[task-offloading]]
- [[task-migration]]
- [[binary-vs-partial-offloading]]
- [[event-driven-vs-slot-driven-offloading]]
- [[task-priority-in-mec]]
- [[wireless-power-transfer]]
- [[noma]]
- [[cooperative-perception]]

### Aerial / network architectures

- [[multi-uav-assisted-mec]]
- [[high-density-mobile-device-scenarios]]
- [[heterogeneous-uav-fleet]]
- [[high-altitude-platform-station]]
- [[hierarchical-aerial-mec]]
- [[air-ground-integrated-network]]
- [[low-altitude-intelligent-network]]
- [[leo-satellite-edge-computing]]
- [[vehicular-mec]]
- [[post-disaster-mec]]

### UAV control & decisions

- [[uav-trajectory-control]]
- [[uav-charging-scheduling]]
- [[gauss-markov-mobility-model]]
- [[hybrid-action-decision-making]]

### DRL backbones

- [[ppo]] · [[j-ppo]]
- [[ddqn]]
- [[masac]]
- [[gae]]
- [[pomdp]] · [[ma-pomdp]]
- [[centralized-training-decentralized-execution]]
- [[adaptive-entropy-priority-replay]]
- [[safe-reinforcement-learning]]

### Memory / encoders

- [[ntm]] · [[en-convntm]]
- [[convlstm]]
- [[stn]]
- [[informer-trajectory-prediction]]

### Optimization techniques

- [[lyapunov-optimization]]
- [[fractional-programming-dinkelbach]]
- [[stackelberg-game]]
- [[matching-theory-for-resource-allocation]]
- [[overlay-underlay-spectrum-access]]
- [[dynamic-constrained-multi-objective-optimization]]

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

- [[query-real-world-validation-of-jppo-en-convntm]]
- [[query-does-en-convntm-generalize-beyond-uav-mec]]

## Comparisons

- [[ddpg-vs-jppo]]
- [[j-ppo-baselines]]
- [[bcsa-frl-vs-bc-uav-masac]] — Blockchain-on-edge: BCSA-FRL vs BC-UAV-MASAC

## Synthesis

- [[design-recipe-multi-uav-mec]] — 10-step recipe for DRL-controlled UAV-MEC
- [[drl-backbones-across-uav-mec-sources]] — Cross-corpus look at DRL backbone choices
- [[maddpg-vs-masac-in-mec]] — When entropy beats determinism in cooperative MEC
