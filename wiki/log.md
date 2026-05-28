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
