# Wiki Index

## Sources (curated)

### Foundational surveys & overviews

- [[mao-2017-mec-survey-communication]] — Mao et al. 2017. Canonical **MEC survey** from the communication perspective (joint radio + compute resource management).
- [[mach-2017-mec-survey-architecture]] — Mach & Becvar 2017. **MEC survey** from the architecture + computation-offloading angle; MCC-vs-edge, integrated architectures (SCC/MMC/MobiScud/FMC/CONCERT) + ETSI, and the three offloading research areas (decision / resource allocation / mobility management) (IEEE COMST).
- [[liang-2025-gai-semcom-survey]] — Liang et al. 2025. Survey of **GAI-driven semantic communication (SemCom)** networks — novel three-plane architecture, transceiver design, information effectiveness metrics, knowledge management, use cases (IEEE TCCN).
- [[zhao-2025-gai-pls-survey]] — Zhao et al. 2025. Survey of **GAI for physical-layer security (PLS)** — GANs/AEs/VAEs/diffusion models across confidentiality, authentication, availability, resilience, integrity (IEEE TCCN).
- [[li-2025-thz-um-mimo-ce-hybrid-field]] — Li & Madhukumar 2025. **Hybrid near- and far-field THz UM-MIMO channel estimation** — dictionary-learning (BD-ODL) + Bayesian CSCE + BCRB; significant NMSE improvement over LS/MMSE/CS baselines (IEEE TWC). *(THz/near-field PHY anchor.)*
- [[wu-2019-irs-joint-beamforming]] — Wu & Zhang 2019. **Foundational IRS paper** — joint active (AP) + passive (IRS phase-shift) beamforming for SINR-constrained power minimization; asymptotic quadratic passive gain in the number of IRS elements; simulations show IRS-aided MIMO matching massive MIMO with far fewer RF chains (IEEE TWC). *(IRS anchor.)*
- [[he-2018-uav-altitude-beamwidth]] — He et al. 2018. Joint **UAV altitude and beamwidth optimization** for multiuser communications (MC/BC/MAC); fly-hover-and-communicate; optimal (H,Θ) differs by model (IEEE LCOMM). *(UAV-deployment anchor.)*
- [[lyu-2018-uav-hotspot-offloading]] — Lyu et al. 2018. **UAV-aided cellular hotspot offloading**: cyclical trajectory + bandwidth allocation + user partitioning; max-min throughput; spectrum reuse > orthogonal; beats small-cell (IEEE TWC). *(UAV-as-aerial-BS offloading anchor.)*
- [[khoramnejad-2025-gai-wireless-optimization-survey]] — Khoramnejad & Hossain 2025. Survey of **generative AI** for xG/6G wireless network optimization (GANs, GDMs, GFlowNets) + NTN case study.
- [[du-2024-gdm-network-optimization-tutorial]] — Du et al. 2024. **Tutorial** on **generative diffusion models** in network optimization (DRL enhancement, incentive/ISAC/SemCom/IoV case studies) (IEEE COMST).
- [[wang-gai-isac-physical-layer]] — Wang et al. Overview of **generative AI for ISAC** from the physical-layer perspective; five GAI models + a diffusion SSG near-field DoA case study (~1.03° MSE) (IEEE Wireless Communications; year not in parse).
- [[meng-2024-uav-isac-overview]] — Meng et al. 2024. Overview of **UAV-enabled ISAC** for 6G (motion control, resource allocation, S&C synergy).
- [[du-2024-distributed-foundation-models-6g]] — Du et al. 2024. Overview of **distributed foundation models** over 6G (pipeline/data parallelism + multi-modal learning).
- [[zeng-2019-uav-comm-tutorial-5g]] — Zeng et al. 2019. **Tutorial** on UAV communications for 5G and beyond; UAV-assisted comms vs **cellular-connected UAV** taxonomy (Proceedings of the IEEE).
- [[al-hourani-2014-optimal-lap-altitude]] — Al-Hourani et al. 2014. Foundational **air-to-ground channel** letter: closed-form sigmoid LoS-probability vs elevation angle + **optimal LAP altitude** for maximum ground coverage (IEEE WCL). *(Channel-model anchor, not MEC.)*
- [[xu-2024-mobile-aigc-survey]] — Xu et al. 2024. Survey of **edge-cloud generative AI / AIGC services** in mobile networks (**mobile AIGC networks**); generative-model fundamentals, AIGC lifecycle, cloud-edge-mobile infrastructure, and implementation challenges (resource allocation, offloading, caching, mobility, incentives) (IEEE COMST).
- [[mozaffari-2019-uav-wireless-tutorial]] — Mozaffari et al. 2019. **Tutorial** on UAVs for wireless networks; UAVs as aerial base stations vs cellular-connected UAVs, 3D deployment, channel modeling, energy efficiency, and the analytical toolbox (optimization, ML, stochastic geometry, game theory) (IEEE COMST). *(UAV-communications anchor, not MEC.)*
- [[mozaffari-2017-uav-iot-energy-efficient]] — Mozaffari et al. 2017. Energy-efficient **IoT data collection** via multiple mobile UAVs; joint 3D placement + device association + uplink power control + closed-form update-times/trajectory; −45% device tx power, +28% reliability vs stationary (IEEE TWC). *(UAV-deployment/data-collection anchor, not MEC.)*
- [[mozaffari-2015-drone-small-cells]] — Mozaffari et al. 2015. **Drone small-cell** optimal altitude (unique, analytically proven) + two-DSC optimal distance in interference-free and full-interference scenarios (IEEE GLOBECOM). *(UAV-deployment/coverage anchor, not MEC.)*
- [[mozaffari-2016-efficient-multi-uav-coverage]] — Mozaffari et al. 2016. Multi-UAV **coverage probability** + **circle-packing** 3D deployment for M UAVs; minimum-UAV-count formula (IEEE LCOMM). *(UAV-deployment/coverage anchor, not MEC.)*
- [[jayaprakasam-2017-dcbf-wsn-survey]] — Jayaprakasam et al. 2017. Survey of **distributed and collaborative beamforming (DCBF)** in WSNs: beampattern analysis, power/lifetime optimization, synchronization, prototypes; N²-fold array-gain anchor (IEEE COMST). *(DCBF/WSN survey anchor.)*
- [[mahboob-2024-ai-ntn-survey]] — Mahboob & Liu 2024. Survey of **AI-empowered satellite-based non-terrestrial networks** for 6G; AI-per-NTN-challenge taxonomy (channel/Doppler estimation, beam/resource management, handover, routing, slicing, offloading, security) + distributed-learning paradigms + O-RAN/RIC implementation (IEEE COMST).
- [[wang-2024-xl-mimo-tutorial]] — Wang et al. 2024. **Tutorial / survey on extremely large-scale MIMO (XL-MIMO)** for 6G; four hardware designs (ULA / UPA-patch / UPA-point / CAP), near-field channel modeling, and low-complexity + deep-learning signal processing (IEEE COMST). *(Physical-layer / near-field anchor, not MEC.)*
- [[huynh-2024-gai-physical-layer-survey]] — Van Huynh et al. 2024. Survey of **generative AI for physical-layer communications**; five GAI model families (GANs, **VAEs**, normalizing flows, diffusion, transformers) across modulation/signal classification, channel estimation/equalization, PLS, IRS, beamforming, JSCC, CSI feedback; GAI-vs-traditional-AI comparison + open issues (security, model-driven GAI, resource-efficient learning, real-time adaptation) (IEEE TCCN). *(Physical-layer GAI survey, not MEC.)*
- [[hu-2015-mec-5g-etsi-whitepaper]] — Hu et al. 2015. The **ETSI white paper** that introduces **Mobile Edge Computing** as a standardized concept (IT/cloud capabilities at the RAN edge), its market drivers, business value, service scenarios (AR, intelligent video acceleration, connected cars, IoT gateway), deployment locations, and the ETSI ISG MEC + Proof-of-Concept framework; positions MEC as complementary to NFV/SDN for 5G (ETSI White Paper No. 11; no DOI). *(Standardization anchor for MEC itself.)*
- [[dai-2024-graph-rm-survey-optimization]] — Dai et al. 2024. **Part I** of a two-part survey on **graph-based resource management** in wireless networks — the **graph-optimization** half (coloring / max-independent-set / max-flow / bipartite-stable matching) across cellular, D2D, multi-hop, multi-antenna, edge caching/computing, and NTN scenarios (IEEE TCCN).
- [[dai-2024-graph-rm-survey-learning]] — Dai et al. 2024. **Part II** of the same survey — the **graph-learning** half: GNN model families applied to power control, spectrum management, beamforming design, task scheduling, and aerial coverage planning, plus the two-part survey's consolidated challenges + future directions (IEEE TCCN).
- [[ullah-2026-mec-drl-ntn-survey]] — Ullah et al. 2026. Survey of **DRL for MEC-empowered non-terrestrial wireless networks (MeNT-WiNs)** — integrating MEC with AAVs, LEO/GEO satellites, and HAPs; reviews DRL fundamentals, the MeNT-WiN architecture + binary-vs-partial / task-call-graph offloading models, then DRL's role in satellite autonomy, AAV-swarm management, resource/spectrum/energy allocation, routing, and security, closing with complexity/real-time/scalability challenges (IEEE COMST).
- [[gong-2023-edge-intelligence-its-survey]] — Gong et al. 2023. Survey of **edge intelligence in intelligent transportation systems**; end-edge-cloud EI architecture, seven-level EI taxonomy, data gathering/processing, autonomous-driving/VEC/UAV/rail applications, platforms, datasets, and open challenges (IEEE T-ITS).
- [[du-2025-autonomous-intelligent-uav-swarms]] - Du et al. 2025. Survey of **autonomous and intelligent UAV swarms** across trajectory planning, task assignment, control, localization, perception, communication, and civil applications (IEEE T-ITS).
- [[javaid-2023-collaborative-uav-communication-control]] - Javaid et al. 2023. Survey of collaborative multi-UAV communication and control requirements, tasking, urban applications, use cases, and open problems in cellular integration, FL, offloading, and energy efficiency (IEEE T-ITS).

### Foundational DRL methods

- [[mnih-2015-dqn-atari]] — Mnih et al. 2015. Origin paper for **DQN** — deep convolutional Q-learning with experience replay + target network; human-level Atari across 49 games with same architecture/hyperparameters (Nature).
- [[fujimoto-2018-td3-actor-critic]] — Fujimoto et al. 2018. Origin paper for **TD3** — clipped double-Q + delayed policy updates + target smoothing to curb actor-critic overestimation (ICML).
- [[schulman-2017-ppo]] — Schulman et al. 2017. Origin paper for **PPO** — clipped surrogate objective enabling multi-epoch first-order policy updates with TRPO-like stability (OpenAI; arXiv, venue/DOI not in parse).
- [[lillicrap-2016-ddpg-continuous-control]] — Lillicrap et al. 2016. Origin paper for **DDPG** — off-policy actor-critic bringing DQN's replay + target networks to deterministic continuous control; soft target updates + OU exploration (ICLR; DOI/venue not in parse).
- [[van-hasselt-2016-double-dqn]] — van Hasselt et al. 2016. Origin paper for **Double DQN** — decouples action selection from evaluation (reusing the target network) to curb DQN's value over-estimation; SOTA Atari (AAAI; DOI/venue not in parse).
- [[xiang-sac-mapless-robot-navigation]] — Xiang et al. Mapless mobile-robot navigation via **Soft Actor-Critic** (LSTM value/Q nets); laser+target→velocity continuous control (venue/year not in parse).

### Joint trajectory / caching / migration

- [[hua-2026-ddrl-content-delivery]] - Hua et al. 2026. Multi-BS UAV content delivery with CNN-GRU clipped PPO for movement/transmission decisions and PSO-tuned cache replacement over popularity, size, and request frequency (IEEE TWC).
- [[zhao-2025-traj-offload-cache-migration]] — Zhao et al. 2025. Joint trajectory + offloading + migration + **computational-task caching**; Lyapunov + BCD + QCQP-SDR.
- [[gao-2024-service-experience-cache-uav]] — Gao & Zhai 2024. Fairness-aware cache-enabled UAV-MEC; **service-experience ratio** (Jain's index / delay); Dinkelbach + 4-stage AO.
- [[zhao-2024-caching-service-placement-uav]] — Zhao et al. 2024. Joint content caching + service placement + offloading; QoE max via Gibbs sampling + matching.
- [[ye-2026-flight-speed-battery-swapping]] - Ye et al. 2026. Flight-speed scheduling, battery swapping, and task offloading for UAV-enabled MEC inspection; virtual-node graph reformulation plus ATC large-scale heuristic (IEEE TMC).
- [[fan-2026-parallel-caching-uav-mec]] - Fan et al. 2026. Multi-task parallel UAV-MEC execution with content caching, computation offloading, and channel allocation; RLTL uses DQN for intra-UAV caching/offloading and regret-minimization learning for inter-UAV channel allocation (IEEE TMC).
- [[chen-2024-dro-video-caching]] — Chen et al. 2024. **Distributionally robust** adaptive-bitrate video caching + transcoding + backhaul in UAV-MEC; ζ-structure-metric confidence set + convex DRO latency minimizer under an energy budget; real YouTube traces (IEEE TMC).
- [[huang-2026-erasure-coded-uav-storage]] — Huang et al. 2026. **Erasure-coded UAV edge storage**; coded data/parity block placement + access routing in post-disaster UAV-enabled edge systems via CNN+ConvLSTM prediction and ME-HDRL (DDQN UAV agents + PPO edge agent) (IEEE TMC).
- [[tian-2026-coded-cache-repair]] - Tian et al. 2026. Erasure/regenerating-coded UAV caching with hierarchical two-timescale multi-agent P-DQN for placement, fragment repair, pairing, and motion (IEEE TWC).
- [[du-2023-maddpg-service-placement-agin]] — Du et al. 2023. **MADDPG** joint service placement + offloading in air-ground integrated MEC.

### Game-theoretic offloading & allocation

- [[jin-2026-skyndn-incentivizer]] - Jin et al. 2026. UAV named-data content sharing through a KKT-aligned iterative double auction and a separate diffusion-actor learned allocator (IEEE TMC).
- [[du-2026-hierarchical-coalition-deployment]] - Du et al. 2026. Nested ground-user coalition formation and potential-game UAV placement for shared-data acquisition over D2D links (IEEE TGCN).

- [[xu-2026-prizty-uav-mec-auction]] - Xu et al. 2026. **Prizty** privacy-preserving reverse auction for UAV-assisted MEC task offloading/resource allocation; UE location obfuscation + trajectory-aware feasible service sets + winner/payment selection (IEEE TMC).
- [[guo-2026-aoi-uav-mcs-contract]] - Guo et al. 2026. AoI-aware UAV-assisted mobile crowdsensing contracts; platform-UAV service-slot contract plus platform-user sensing/computation-cost contracts for freshness/cost control under incomplete information (IEEE TMC).
- [[wang-2023-differentiated-uav-services]] - Wang et al. 2023. Multi-agent imitation learning for a competitive UAV service market; full-information expert demonstrations, opponent modeling, and decentralized quantity/fleet control under substitutable demand (IEEE TMC).

- [[chen-2015-decentralized-offloading-game]] — Chen 2015. **Decentralized computation offloading game** for mobile cloud computing — potential game; Nash equilibrium existence + decentralized mechanism; ≤10% PoA over centralized optimum (IEEE TPDS).
- [[chen-2016-multiuser-offloading-game-mec]] — Chen et al. 2016. **Multi-user computation offloading game** for mobile-edge cloud computing — NP-hard centrally; potential game + distributed NE algorithm; multi-channel interference + contention environments (IEEE/ACM ToN).
- [[he-2019-euagame-user-allocation]] — He et al. 2019. **EUAGame** — edge user allocation as a potential game with a decentralized NE algorithm.
- [[ning-2023-uav-mec-offloading-deployment]] — Ning et al. 2023. Dynamic UAV-MEC computation offloading and server deployment as coupled stochastic games; UEPSSL/UAVPSSL learning plus chess-like asynchronous update toward NE (IEEE TMC).
- [[sun-2024-mvtora-postdisaster-vfc]] — Sun et al. 2024. Post-disaster aerial-terrestrial MEC + **vehicle fog computing**; game theory + convex + evolutionary (MVTORA).
- [[chen-2022-qoe-game-end-edge-cloud]] — Chen et al. 2022. **QoE-aware decentralized end-edge-cloud offloading** as a **potential game** (MUTO-Game); self-interested user devices compete for channels + edge compute, maximizing sum QoE; proven NE existence + the distributed GDTO algorithm + a convergence bound and a **Price-of-Anarchy** worst-case guarantee (IEEE TMC).
- [[ma-2026-mean-field-green-aec]] — Ma et al. 2026. Green aerial edge computing for metaverse users; [[mean-field-game]] task allocation + Lyapunov energy valuation across CE-UAVs and energy-harvesting EF-UAVs, with Raspberry Pi5/A100 hardware-in-the-loop validation (IEEE TMC).

> [[chen-2024-ulse-game]] (UAV-LEO offloading as a potential game) is also game-theoretic; it is filed under **SAGIN / satellite offloading** below as its primary architectural home.
> [[zhang-2026-uav-task-path-lu-its]] (multi-UAV low-altitude ITS task allocation as a potential game) is filed under **Architectural / spectrum / governance** as its primary low-altitude-economy home; [[jia-2026-ufsp-rail-inspection]] (imperfect-information stochastic potential game) is filed under **UAV-swarm collaborative computing**.

### Multi-UAV cooperative computing & deployment

- [[liu-2026-heterogeneous-sensor-satisfaction]] - Liu et al. 2026. Static multi-UAV data-collection deployment, sensor association, and transmit-power allocation for delay-, energy-, and dual-sensitive sensor utilities using ELGHEOA (IEEE TWC).

- [[chen-2026-hammurabi-cooperation]] - Chen et al. 2026. Hammurabi diagnoses self-interested pre-trained UAV policies, then fine-tunes parameter-shared policies with public-goods-style incentives and inequity aversion (IEEE TPDS).
- [[jia-2026-hierarchical-uav-swarms]] - Jia et al. 2026. Head/tail hierarchical UAV swarms for two-hop data collection; K-means/Voronoi predeployment and INS-WOA Pareto optimization of routes, user/UAV power, energy, and delay (IEEE TWC).
- [[zhou-2026-multiscale-dt-uav-delivery]] - Zhou et al. 2026. Terminal-edge multiscale digital twins for UAV parcel delivery; graph-matching macro twins assign parcel clusters, while cooperative-reinforcement-learning micro twins plan energy- and collision-aware paths (IEEE TMC).
- [[zhao-2026-dt-ddqn-bisd-deployment]] - Zhao et al. 2026. Digital-twin-driven multi-UAV IoT deployment with balanced mission division, 3-D transfer and fixed-altitude collection DDQNs, online obstacle synchronization, safety halts, and policy refresh (IEEE TWC).
- [[gao-2026-fmad3qn-uav-gd-association]] - Gao et al. 2026. Dynamic heterogeneous multi-UAV MEC with no-fly zones; closed-form UAV-GD association via optimal transport + federated multi-agent dueling DDQN for 3D deployment (IEEE TMC).

- [[wang-2025-maddpg-lc-dynamic-trajectory]] — Wang et al. 2025. **MADDPG-LC** — dynamic trajectory design for multi-UAV MEC with UAV **flight-dynamics** constraints; MADDPG + LQR tracking + CVXPY + blockchain security (IEEE TVT).
- [[guo-2023-mccco-multiuav-5g-offloading]] — Guo et al. 2023. SDN-enhanced cooperative multi-UAV partial offloading with task interdependency (MCCCO).
- [[wang-2019-todetas-deployment-scheduling]] — Wang et al. 2019. Two-layer UAV deployment (**differential evolution**) + task scheduling (greedy); ToDeTaS.
- [[miao-2022-gaglpp-drone-swarm-iiot]] — Miao et al. 2023. Drone-swarm path planning for Industrial-IoT MEC; ground-station global + onboard local planning (GAGLPP); priority/energy/distance scheduling (IEEE TII).

> [[peng-2026-demand-aware-multiuav-mec]] is a multi-UAV fleet-allocation source filed under **CMOP / evolutionary UAV-MEC** as its primary methodological home.

### Pure optimization methods

- [[wang-acve-constraint-violation-cmop]] — Wang et al. 2025. **ACVE** — adaptive constraint-violation-evaluation framework + DDCo dual-population coevolution (IEEE TEVC early access; DOI grounded by the source parse sidecar and by [[huang-2025-cmop-dispersed-computing]]).

### Compute offloading & DRL

- [[wang-2025-ppo-uav-positioning-offloading]] - Wang et al. 2025. PPO-based joint UAV positioning and partial task offloading in multi-UAV MEC; BS/UAV task splitting, access/backhaul links, latency minimization, and UAV-failure resilience (IEEE TMC).
- [[guo-2026-aot-uav-inspection-offloading]] - Guo et al. 2026. AGI-oriented Transformer for UAV-assisted railway inspection; shared encoder with trajectory and offloading heads for hive/UAV/sensor execution decisions (IEEE TMC).
- [[zhan-2026-gatd3qn-dependent-offloading]] - Zhan et al. 2026. Joint UAV placement, UAV-GU association, and dependent-task DAG offloading in multi-UAV MEC; JSPO plus GAT-enhanced D3QN (IEEE TMC).
- [[teng-2026-gstrl-sequential-offloading]] - Teng et al. 2026. Graph-based spatiotemporal RL for sequential task offloading in multi-UAV MEC; heterogeneous task/UAV graph encoding plus masked PPO for order-constrained offloading decisions (IEEE TMC).
- [[zhao-2026-heuristic-supervised-drl]] - Zhao et al. 2026. Heuristic-supervised DRL framework with TTSSA convergence analysis; PSO bridges upper-tier planning to MARL control in the UAV-MEC case study (IEEE TMC).
- [[chen-2026-qos-noma-multiuav]] - Chen et al. 2026. QoS-oriented NOMA multi-UAV MEC offloading with task priorities, Lagrange-dual constraint handling, and improved SAC for trajectories/association/offloading/resources (IEEE TWC).
- [[bui-2025-noma-near-far-offloading]] - Bui et al. 2025. UAV-aided NOMA MEC with near-field/far-field coexistence around large UAV arrays; alternating optimization over offloading decisions, transmit powers, and UAV computing allocation (IEEE TGCN).
- [[zhai-2026-collaborative-inference-uav-mec]] — Zhai et al. 2026. Multi-UAV DNN inference offloading; OPPS partition-point selection + fairness matching + TD3 trajectory/transmit-power control (IEEE T-ITS).
- [[wu-2026-secure-split-offloading-ci]] - Wu et al. 2026. Secure UAV-assisted collaborative DNN inference; multi-exit DNN, DNN partitioning, dual-UAV trajectories, cooperative jamming, SCA, and discrete WOA (IEEE TMC).
- [[shi-2026-aoi-active-ris-noma-agmec]] - Shi et al. 2026. **AoI-aware active-RIS + NOMA air-ground MEC**; joint UAV trajectory, active-RIS beamforming, and UE offloading via AADDPG with an action adjuster and battery-protection rule (IEEE TWC).
- [[liu-2026-lyapunov-diffusion-uav-vehicular]] - Liu et al. 2026. UAV-assisted vehicular V2X with **delayed CSI feedback**; Lyapunov energy queue + diffusion-actor DDPG (**D3PG**) over V2V channel reuse, power control, and UAV altitude (IEEE TWC).
- [[tong-2026-uneven-terrain-uav-mec]] — Tong et al. 2026. Uneven-terrain UAV-MEC with service coverage, partial UAV/BS task allocation, propulsion energy, and safe 3D flight; PH-DRL separates TD3 flight control from actor-critic task allocation (IEEE TMC).
- [[ma-not-in-parse-reinforced-traffic-prediction]] - Ma et al. Cell-level mobile traffic prediction with FFT feature characterization and value-based reinforced meta-learning that adapts the DNN structure, with transfer tests and a numerical UAV-offloading case study. *(Parsed metadata lacks DOI/venue/year.)*

- [[liu-2026-jppo-en-convntm]] — Liu et al. 2026. Multi-UAV path planning for MEC under high-density mobility. *j-PPO+EN-ConvNTM* (hybrid-action PPO + memory-augmented encoder).
- [[hao-2025-priority-aware-task-driven-co]] — Hao et al. 2025. Task-driven priority-aware computation offloading via DRL.
- [[hao-2024-clp-multiuav-priority-offloading]] — Hao et al. 2024. Multi-UAV cooperative MEC with task priority. *CLP* (TD3 + hybrid-action latent space).
- [[ma-2025-pdqn-vehicular-mec]] — Ma et al. 2025. Hybrid-action **P-DQN** for binary-offloading + power allocation in three-tier vehicular MEC.
- [[song-2024-mol-aoi-energy]] — Song et al. 2024. AoI-vs-energy aerial-ground MEC via **multi-objective RL** (MOL-AET: multi-objective PPO + evolutionary phase).
- [[song-2022-emorl-tcto-uav]] — Song et al. 2022. Trajectory control + offloading via **evolutionary multi-objective RL** (EMORL-TCTO); multi-policy Pareto set in one run.
- [[albakhrani-2025-moalf-uav-mec]] — AL-Bakhrani et al. 2025. **MOALF-UAV-MEC** — integrates MORL + MPC + APSO + Lyapunov optimization; burst-mode UAVs.
- [[zhao-2022-matd3-multiuav-ec-offloading]] — Zhao et al. 2022. Cooperative multi-UAV + multi-EC offloading; **MATD3** over trajectory + task allocation + resources.
- [[chang-2022-marl-multiuav-trajectory]] — Chang et al. 2022. Multi-UAV-as-base-station trajectory + user association + power; RL+DL and multi-agent DRL.
- [[he-2023-fairness-3d-multiuav-maddpg]] — He et al. 2023. Fairness-among-UAVs 3-D trajectory optimization; analytic offloading + **MADDPG**.
- [[zhang-2024-uav-task-offloading-ddpg]] — Zhang et al. 2024. **UTOM** — single-UAV offloading; convex (resource) + IPSO (offloading) + DDPG (trajectory).
- [[li-2025-twohop-airground-drl-offloading]] — Li et al. 2025. Two-hop partial offloading in air-ground MEC; MADDPG-IPER + NV-IPPO (JPTORAUTD).
- [[li-2024-twohop-iort-packet-scheduling]] — Li et al. 2024. Two-hop **packet scheduling** + resource allocation + UAV trajectory for IoRT in an air-ground integrated network; MADDPG + MADDQN + adaptive PER (MADDPG-APER) minimizing HAP→device packet-queue delay (IEEE IoT-J).
- [[wang-2025-sac-tma-mec-dc]] — Wang et al. 2025. Joint multi-AAV **MEC + data collection**; SAC + two-phase matching-based association (SAC-TMA).
- [[wang-2022-cat-rat-fmec-trajectory]] — Wang et al. 2022. Flying-MEC UAV trajectory + association + resource; **CAT** (BCD convex) and **RAT** (twin-DQN + PER + matching) (IEEE TMC).
- [[niazmand-2025-jopa-dnn-pruning-iiot]] — Niazmand & Ye 2025. **DNN-pruning-aware** IIoT fault-detection offloading; joint offloading + pruned-model selection + resource allocation; MRP + hybrid-action SAC (JOPA) (IEEE TCCN).
- [[duan-2023-moto-smallcell-offloading]] — Duan et al. 2023. **MOTO** — mobility-aware online task offloading + adaptive load balancing in terrestrial **small-cell MEC**; LSTM (offloading control) + Dueling Double DQN (server grouping); real WiFi-trace driven (IEEE TMC).
- [[yang-2020-loadbalance-multiuav-iot]] — Yang et al. 2020. **Load-balance** multi-UAV MEC for IoT; **differential-evolution** UAV deployment + **GAP** node assignment (LP-relax + rounding) + **DQN** task scheduling (IEEE IoT-J).
- [[li-2024-robust-bmappo-multiuav-mec]] — Li et al. 2024. **Robust** multi-UAV-MEC offloading under joint communication + computation uncertainty; weighted-energy min via **MAPPO with a Beta-distribution policy** (b-MAPPO) (IEEE IoT-J).
- [[liu-2020-cooperative-uav-mec-power-iot]] — Liu et al. 2020. **Cooperative** UAV-enabled MEC for **power IoT** (UAVs help neighboring small-cells compute); long-term utility max as a **semi-Markov** process; two-phase centralized + Q-value-transfer distributed DRL (IEEE TVT).
- [[wang-2024-hfrl-decentralized-navigation]] — Wang et al. 2024. Decentralized navigation for **heterogeneous** UAV-MEC; soft hierarchical DRL (SHDRLN, skill abstraction) + dual-end **federated RL** (DFRL) maximizing task-offloading energy efficiency (IEEE TMC).
- [[zhou-2024-jdl-abs-postdisaster-rescue]] — Zhou et al. 2024. **Post-disaster** ABS computation offloading + communication assistance; min task-queuing-delay over ABS-GU association + offloading ratio + trajectory; **JDL** = Lyapunov + actor-critic DRL with a **model-based SCA critic** (IEEE TWC).
- [[tang-2026-hg-maddpg-uav-rescue]] - Tang et al. 2026. Low-altitude UAV rescue with UAVs, ground embedded robots, and airships; HG-MADDPG combines Hungarian area assignment, Lyapunov queues, and generative-diffusion-enhanced MADDPG (IEEE TMC).
- [[guo-2026-spatiotemporal-information-quality-ugrnet]] - Guo et al. 2026. Martingale heterogeneous multi-hop delay bounds and Wasserstein spatial-completeness costs for UAV-assisted ground-robot information collection (IEEE TMC).
- [[raivi-2024-jdaco-postdisaster-iot]] — Raivi & Moh 2024. **JDACO** — joint data aggregation + computation offloading for multi-UAV **post-disaster** IoT; two-tier LT-UAV/HT-UAV; minimize aggregation+offload energy/delay + max IoT coverage; **VD3QN** (dueling double DQN + value-decomposition network); +20% training-time / +11.4% data / +5.6% energy-eff / +11.2% mission-duration, up to 98% devices served (IEEE IoT-J).
- [[sun-2024-ues-video-analytics-disaster]] — Sun et al. 2024. **Battery-aware** UAV-edge-server collaborative **video analytics** for **disaster rescue**; differential-evolution per-slot offloading + **DDQN** trajectory planning; doubles the smart-camera-network lifetime (IEEE TVT).
- [[gao-2024-d3qn-uav-mec-mobile-gt]] — Gao et al. 2024. **3D** UAV-MEC for **mobile** ground terminals in a **post-disaster** urban scenario; collect→compute→deliver total-time minimization over UAV 3D trajectory + GT scheduling, with **obstacle avoidance** among buildings + **probabilistic-LoS** channel; MDP + **multi-step dueling DDQN (D3QN)**; 3D beats 2D, robust to GT mobility / height limits (IEEE TVT).

### Classical / convex / optimization-based UAV-MEC

- [[shah-2026-cellfree-mimo-fap-control]] - Shah et al. 2026. APG trajectory/power control, GA association, and DBSCAN pilot-conflict repair for aerial user-centric cell-free massive MIMO (IEEE TWC).

- [[li-2026-noma-uav-relay-planning]] - Li et al. 2026. Max-min user-rate design for a two-hop NOMA amplify-forward UAV relay through AO, SDR/SCA, power control, beamforming, and 3-D trajectory planning (IEEE TGCN).

- [[zhan-2018-uav-wsn-data-collection]] — Zhan et al. 2018. UAV **data collection** in WSN; joint wake-up schedule + trajectory to minimize max SN energy; general fading + outage constraint; SCA (IEEE WCL).
- [[li-2020-energy-efficient-uav-mec-admm]] — Li et al. 2020. UAV-mounted cloudlet **energy efficiency** (compute-bits/energy ratio) maximization; Dinkelbach + SCA + **ADMM** distributed decomposition; Gaussian KDE for user-mobility prediction (IEEE TVT).
- [[ji-2021-uav-mec-noma-oma-energy-min]] — Ji et al. 2021. UAV-MEC **weighted-sum energy minimization** (UAV + UDs) under **partial offloading** with OMA and NOMA; block alternating descent + SCA; OMA beats NOMA in this energy-min setting (IEEE IoT-J).
- [[wang-2018-wpt-mec-joint-offloading]] — Wang et al. 2018. **Wireless-powered MEC**: joint energy beamforming + partial offloading + CPU freq + TDMA time allocation; minimizes AP energy; **local computing always beneficial** at optimum; semi-closed-form optimal solution (IEEE TWC).
- [[xu-2021-secure-uav-mec-dual-uav]] — Xu et al. 2021. **Dual-UAV** secure MEC (server UAV + jammer UAV); TDMA and NOMA; **secure computing capacity** maximization; BCD + P-BCD; NOMA > TDMA for security (IEEE TCOMM).
- [[wang-2026-secure-reliable-uav-mec]] — Wang et al. 2026. Energy-efficient UAV-assisted MEC with **secure and reliable data transmission**; user-side artificial noise, secrecy-outage chance constraint, fixed-wing trajectory/resource allocation, and augmented-Lagrangian secure-energy-efficiency optimization (IEEE TMC).
- [[zhang-2019-uav-iot-comp-comm]] — Zhang et al. 2019. Joint computation + communication design for single-UAV MEC; Lagrangian duality + SCA.
- [[yang-2019-sum-power-uav-mec]] — Yang et al. 2019. Multi-UAV-MEC **sum-power minimization** (UEs + UAV propulsion) over user association + power + compute-capacity + UAV location/altitude/beamwidth; compressive-sensing association + closed-form capacity + 1-D location search + fuzzy-c-means init (IEEE TWC).
- [[yu-2020-uav-ec-collaborative-offloading]] — Yu et al. 2020. Collaborative UAV+edge-cloud offloading; SCA; beats UAV-only / EC-only.
- [[liu-2022-miso-uav-mec-trajectory]] — Liu et al. 2022. **MISO** UAV-MEC; three-stage AO with closed-form CPU-freq / power; CSI-driven offloading.
- [[yang-2022-stochastic-uav-mec-lyapunov]] — Yang et al. 2022. Stochastic UAV-MEC; **Lyapunov** online algorithm; two-stage vs joint comparison.
- [[zhang-2019-stochastic-offloading-uav-mec]] — Zhang et al. 2019. **Stochastic** computation offloading + trajectory scheduling for single-UAV MEC; **Lyapunov** decomposition into three subproblems + ADMM/interior-point/CVX (IEEE IoT-J).
- [[liu-2020-wpt-cooperative-uav-mec]] — Liu et al. 2020. UAV-enabled **wireless-powered cooperative** MEC (UAV ET + MEC server; idle SDs as helpers); UAV-energy min via **SCA** + lower-complexity **DAI** over CPU / offloading / power / trajectory (IEEE IoT-J).
- [[hu-2026-latency-hybrid-uav-mec]] - Hu et al. 2026. Wireless-powered hybrid UAV-GBS MEC; latency minimization under TDMA/NOMA over slot count, time scheduling, CPU frequency, power, and 3D trajectory via double-loop AO/bisection (IEEE TMC).
- [[bai-2024-delay-aware-cooperative-edge-cloud]] — Bai et al. 2024. Multi-UAV edge-cloud **cooperative** offloading; convex approximation + **Lyapunov** online; cooperative-parallel-computing delay model; platform-verified (IEEE TMC).
- [[apostolopoulos-2021-prospect-theory-uav-offloading]] — Apostolopoulos et al. 2021. Risk-aware partial offloading to ground + UAV MEC servers via **prospect theory**; non-cooperative game with proven unique PNE (IEEE TMC).
- [[pervez-2024-acm-multiuav-mec]] — Pervez et al. 2024. Multi-UAV + BS MEC; weighted energy+latency cost via three-layer **ACM** (potential-game offloading + GWF power + SCA trajectory + gradient-descent CPU) (IEEE TWC).
- [[zeng-2019-rotary-wing-energy-min]] — Zeng et al. 2019. **Rotary-wing UAV propulsion energy model** + energy-minimizing trajectory; fly-hover-communicate (TSPN) and communicate-while-flying (path discretization + SCA) (IEEE TWC).
- [[hu-2019-pdd-uav-mec-offloading]] — Hu et al. 2019. Single-UAV MEC; min-max-delay offloading-ratio + trajectory + user scheduling via **penalty dual decomposition** (PDD + CCCP) + simplified l0-norm (IEEE IoT-J).
- [[wu-2024-urllc-uav-mec-latency]] — Wu et al. 2024. **URLLC / finite-blocklength** UAV-MEC; min-max latency via BCD + SCA over UAV 3D location + bandwidth + CPU frequency; Rician fading (IEEE TWC).
- [[wu-2018-multiuav-minrate-trajectory]] — Wu et al. 2018. Multi-UAV-as-base-station **max-min-rate** trajectory + scheduling + power; BCD + SCA + circle-packing init (communications framing, IEEE TWC).
- [[sun-2025-tjcct-twotimescale-uav-mec]] — Sun et al. 2025. **Two-timescale** UAV-MEC (TJCCT); MINLP system-utility max via short-timescale price-incentive resource allocation + matching offloading and long-timescale convex trajectory control; stability + complexity proved (IEEE TMC).
- [[jeong-2018-uav-cloudlet-bit-allocation]] — Jeong et al. 2018. Early **UAV-mounted cloudlet** MEC; joint **bit allocation** (uplink/compute/downlink) + trajectory to minimize mobile energy under latency + UAV-energy budget; orthogonal vs **NOMA** access; **SCA** (IEEE TVT).
- [[hu-2019-uav-relay-edge-computing]] — Hu et al. 2019. UAV as **MEC server + relay** simultaneously; minimize **weighted-sum energy** of UAV + UEs over computation scheduling + bandwidth allocation + trajectory; alternating optimization (closed-form Lagrange-dual + SCA) under **information-causality** constraints (IEEE TWC).
- [[song-2026-thz-multiuav-mec]] - Song et al. 2026. THz multi-UAV relay MEC with direct or IoT-UAV-MEC offloading paths; PDD optimizes relay selection, UAV power/deployment, user-resource association, and M/M/s MEC queueing delay (IEEE TMC).
- [[zhan-2020-completion-time-energy-uav-mec]] — Zhan et al. 2020. Single **fixed-wing** UAV-MEC server; joint offloading + resource allocation + trajectory + **completion time**, minimizing UAV **energy** and **completion time** separately and tracing their **Pareto** tradeoff; path discretization + AO + **SCA** (IEEE IoT-J).

### SAGIN / satellite offloading

- [[kim-2026-qmarl-sagin-access]] - Kim et al. 2026. Quantum-circuit multi-agent scheduling coordinates CubeSats and HALE-UAVs for differentiated ground-station access and residual-energy preservation (IEEE TMC).
- [[liao-2026-semantic-twinning-tracking]] - Liao et al. 2026. Goal-oriented semantic twinning for satellite-UAV collaborative target tracking; significance-triggered updates, causal graph learning, and EWC-regularized MADDPG control freshness and tracking quality under constrained links (IEEE TMC).
- [[tun-2025-thz-sag-mec-resource-allocation]] - Tun et al. 2025. THz-assisted MEC-enabled SAG networks; BCD over device offloading, THz sub-band/power control, UAV deployment, and UAV-to-UAV/LEO task forwarding (IEEE TMC).

- [[chen-2026-pddqn-sagin-mec]] - Chen et al. 2026. MEC-enabled SAGIN with local/UAV/LEO partial offloading; P-DDQN couples device/satellite association with transmit power, task ratios, and UAV 3D trajectory under LEO coverage-time constraints (IEEE TWC).

- [[diallo-2026-system-cost-uav-leo-offloading]] - Diallo et al. 2026. UAV-assisted LEO task offloading with task dropping cost, UAV trajectory, transmit power, and offloading/computing scheduling solved by a four-block classical decomposition (IEEE TGCN).

- [[zhao-2026-hcdrl-ga-sagin-sar]] - Zhao et al. 2026. Multi-UAV SAR in SAGIN; HCDRL/HCSAC trajectory/offloading with CNN+GCN state encoding plus GA deployment search under NOAA-derived wind fields (IEEE TMC).
- [[seid-2026-mafdrl-tn-ntn-incentive]] - Seid et al. 2026. TN-NTN offloading/resource allocation with a hierarchical double auction and hierarchical federated MADDPG/DDPG control across EDs, UAVs, HAPs, and LEO-backed coverage (IEEE TMC).

- [[cheng-2019-sagin-iot-offloading-rl]] — Cheng et al. 2019. **First SAGIN computing-offloading** paper for remote IoT; UAV edge + satellite cloud; MDP + **actor-critic RL** offloading + heuristic VM allocation (IEEE JSAC).
- [[zhou-2021-delay-sagin-task-scheduling]] — Zhou et al. 2021. Delay-oriented IoT task scheduling in SAGIN; UAV collects tasks and schedules local / BS / LEO execution via deep risk-sensitive RL with separate delay-cost and energy-risk Q-functions (IEEE TWC).
- [[liu-2024-sagin-spherical-sg-connectivity]] — Liu et al. 2024. **Spherical stochastic geometry** uplink path connectivity analysis for SAGIN; GUs + AVs on spherical surfaces; three connectivity metrics; first such model (IEEE JSAC).
- [[yang-2026-clustered-leo-adaptive-selection]] - Yang et al. 2026. Clustered LEO direct/cooperative communication with a UAV relay, spherical stochastic geometry, shadowed-Rician fading, and adaptive signal selection (IEEE TWC).
- [[huang-2026-amappo-satellite-edge]] — Huang et al. 2026. Cost-aware dependent-task offloading in UAV-assisted satellite edge computing; direct IoTD-to-LEO in spacious regions, UAV relay in obstructive regions, MATS DAG sequencing + asynchronous GNN-augmented MAPPO (IEEE TMC).
- [[he-2026-dt-sagimec-lae]] — He et al. 2026. DT-assisted SAGIMEC for low-altitude economy; ISD/UAV/LEO/cloud architecture, Lyapunov per-slot control, satellite-latency learning, and Stackelberg-game decentralized decisions (IEEE TMC).
- [[gao-2024-sagin-perception-offloading]] — Gao et al. 2024. **Perception-aided** SAGIN offloading (mmWave radar + YOLOv7 → DRL state); Lyapunov + DDPG + DQN + SGHS.
- [[chen-2024-thoas-traffic-aware-sagin]] — Chen et al. 2024. **THOAS** — traffic-aware slicing-enabled SAGIN; probsparse-attention prediction + lightweight distilled PPO.
- [[chen-2024-ulse-game]] — Chen et al. 2024. Multi-user UAV-LEO offloading as a **potential game** (LUTO-Game / JULTO distributed best-response).
- [[han-2024-sagin-fl-handover]] — Han et al. 2024. **Federated learning** across SAGIN with adaptive inter-layer data offloading + satellite seamless handover.
- [[qin-2025-matd3-noma-queue-sagin]] — Qin et al. 2025. NOMA-enabled queue-aware offloading + AAV 3D trajectory for SAGIN; Lyapunov + MATD3.
- [[wang-2024-hybrid-oma-noma-sagin]] — Wang et al. 2024. Hybrid **OMA/NOMA** mode selection + power allocation in SAGIN; SCA + Lagrange + DQN.
- [[zhai-2023-fedleo-decentralized-fl]] — Zhai et al. 2023. **FedLEO** — server-free decentralized FL over LEO constellations + offloading vs stragglers.
- [[mao-2024-ntn-hierarchical-caching-cav]] — Mao et al. 2024. Hierarchical content caching for CAVs over NTN (LEO+UAV); DM-ACO + MADRL-HCAU.
- [[cheng-2025-dos-satellite-edge-computing]] — Cheng et al. 2025. **Energy-constrained** LEO satellite edge computing for STINs; **DOS** — Lyapunov + convex decomposition under satellite energy-harvesting/eclipse dynamics (IEEE TVT).
- [[zhang-2025-vnf-sgin-dql]] — Zhang et al. 2025. **NFV/SDN service-function-chaining** for 6G satellite-ground integrated networks; dynamic VNF selection + chaining via deep Q-learning (DDVSC) to maximize long-term network profit (IEEE TVT).
- [[han-2024-ground-satellite-fl]] — Han et al. 2024. **Cooperative FL over ground-to-satellite networks**; LEO satellites as edge-compute units + aggregators + ISL relays; solar-battery-aware data offloading + convergence proof + latency minimizer (IEEE JSAC).
- [[lee-2024-dho-leo-handover]] — Lee et al. 2024. **DHO** — DRL-based LEO-satellite **handover protocol** that skips the Measurement Report by prediction; minimizes access delay + collision rate; trained with IMPALA; up to 6.86×/4.18× lower access delay vs conventional/heuristic HO (IEEE TWC). *(LEO connection-handover/networking, not offloading.)*
- [[mao-2024-fso-leo-hierarchical-routing]] — Mao et al. 2024. Hierarchical **routing** for ultra-dense **FSO LEO** constellations; dual-layer MEO/LEO + region division + multi-objective DRL utility routing + cooperative-mechanism conflict resolution; APT-terminal-adaptive (IEEE JSAC). *(LEO routing/networking, not offloading.)*
- [[zheng-2024-semcom-sec-offloading]] — Zheng et al. 2024. **Semantic communication** in a LEO **satellite-borne edge cloud** (SemCom-SEC) for computation offloading; **pruning-split federated learning** (PSFed) updates the semantic coders + a **Rubinstein-bargaining** task-scheduling mechanism (CTPS) for delay/energy under privacy + fairness; −40.50% comm cost, −51.43% privacy risk (IEEE JSAC).
- [[zhang-2024-coma-satellite-offloading]] — Zhang et al. 2024. **Collaborative task offloading for distributed satellite MEC**; autonomous LEO agents minimize energy under time-varying ISL visibility; POMDP solved with **COMA** (CTDE actor-critic) + an **attention-BiLSTM** actor; STK-built constellation (IEEE TVT).
- [[zhang-2024-mhspo-satellite-peer-offloading]] — Zhang et al. 2024. **Multi-hop computation peer offloading** (MHSPO) for MEC-enabled LEO satellite networks; an access satellite offloads tasks **horizontally** to peer satellites several ISL hops away for **load balancing**; weighted delay+energy min via **Lyapunov** + delayed online learning + gap-preserving per-satellite distributed decomposition (IEEE TMC).
- [[wang-2024-satellite-terrestrial-computing]] — Wang et al. 2024. **Satellite-terrestrial computing** for 6G; BSs + LEO satellites with MEC serve **GUEs + SUEs**; min weighted total energy under delay via joint **offloading selection** (relaxation mapping) + **receive beamforming** (SDR) + resource allocation; NP-hard → 3 subproblems solved by **AO**; NOMA-SIC uplinks + FSO inter-satellite links (IEEE TCOMM).
- [[zhou-2024-mco-satellite-edge-offloading]] — Zhou et al. 2024. **Mobility-aware** computation offloading in a three-layer SECN (GEO cloud / LEO edge / ground); first to model **LEO high-speed movement** (coverage-time model + four mobility scenarios); min weighted latency+energy; discrete non-convex → continuous convex relaxation → **MCO-A**, an **ADMM-based distributed** algorithm (convergence proved) scaling to large co-existing-user offloading (IEEE TMC).
- [[liu-2023-sagecn-online-offloading]] — Liu et al. 2023. Collaborative **space/aerial-aided** edge computing (SAGECN) for 6G where **LEO satellites are both servers and users**; a satellite offloads its own tasks one hop to a nearby aircraft or multi-hop to the cloud; min long-term completion delay via **Lyapunov** drift-plus-penalty + **delayed online learning** predicting task arrivals + queue lengths, per-slot bounded integer program (IEEE TVT).
- [[zhang-2023-three-tier-satellite-offloading]] — Zhang et al. 2023. **Satellite-based three-tier cloud-edge offloading**; remote ground UEs offload (data-partition **partial offloading**) to a LEO-edge server and further to a ground cloud; min system energy over **user association + power + task scheduling + fronthaul/backhaul bandwidth assignment**; NOMA fronthaul + quadratic-transform power + CVX bandwidth, in a joint iterative algorithm (IEEE TWC).
- [[zhang-2024-qos-vne-sagoin]] — Zhang et al. 2024. **QoS-aware multi-domain virtual network embedding** over a three-layer **space-air-ground-ocean** integrated network (SAGOI-Net); K-means classifies VNRs into compute/bandwidth/delay QoS categories to switch the **RL agent's reward**; convolutional policy network for node mapping + k-shortest-path link mapping (IEEE TSC). *(SDN/NFV resource orchestration.)*
- [[xie-2025-stin-delay-offloading]] — Xie et al. 2025. **LEO satellite-terrestrial** computation offloading + resource allocation that treats **system state delay** (stale observations / delayed actions) as a first-class modeling object: a **stochastic delay MDP** reduced to a standard MDP with an **augmented state**, solved by an augmented-experience **double DQN**, plus a multi-level feedback queue (RAMLFQ) for per-server CPU; MINLP energy minimization under latency (IEEE TMC).
- [[zhao-2025-probabilistic-semantic-sagin]] — Zhao et al. 2025. Energy-efficient [[probabilistic-semantic-communication]] over SAGIN; satellite-UAV-GT relay model with shared probabilistic graphs, semantic compression ratio, satellite/UAV computation allocation, bandwidth, power, and UAV placement optimized for total communication+computation energy (IEEE TWC).
- [[tang-2021-cecls-hybrid-cloud-edge]] — Tang et al. 2021. **Hybrid cloud-and-edge LEO satellite (CECLS)** network; **three-tier** (ground users / LEO-edge MEC / terrestrial cloud) sum-energy minimization with per-satellite **coverage-time** + **compute-capability** caps; binary nonconvex → **binary relaxation to an LP** → **distributed ADMM** + binary recovery (IEEE IoT-J).
- [[moon-2024-ground-satellite-uam-scheduling]] — Moon & Chae 2024. **Cooperative ground-satellite downlink scheduling + power allocation** for **urban air mobility (UAM)** in a 6G NTN; offload high-interference UAMs to the satellite band, recast GS link association as a **minimum-cost max-flow** graph problem, then **SCA** power allocation; prediction-based, CSI-light scheduling (MINLP, IEEE JSAC). *(Communication-layer scheduling, not computation offloading.)*
- [[wang-2026-spatiotemporal-leo-channel-prediction]] - Wang et al. 2026. Global/local spatiotemporal attention, masked partial-CSI reconstruction, and dominant-beam compression for UAV-RIS-assisted LEO MIMO channel forecasting (IEEE TWC).

### IRS / THz / anti-jamming

- [[liu-2026-passive-6dma]] - Liu et al. 2026. A rigid UAV-mounted passive IRS jointly controls 3-D position, three-axis orientation, and reflection phases for max-min multicast SNR (IEEE TWC).

- [[yin-2026-uav-antijamming-nfsp]] - Yin et al. 2026. Neural fictitious self-play, LSTM history, and dueling double Q-learning adapt a communicating UAV against an unobserved learning jammer (IEEE TMC).
- [[xie-2026-uav-irs-eppo]] - Xie et al. 2026. Urban UAV-carried IRS control with EPPO, neural episodic state abstraction, mogrifier LSTM, and closed-form LoS phase alignment (IEEE TMC).


- [[mahmoud-2021-uav-irs-iot-analysis]] - Mahmoud et al. 2021. Analytical UAV-mounted IRS link for one beyond-horizon IoT user; SNR bounds/distribution, SER, ergodic capacity, and outage expose ideal N-squared array scaling and elevation-dependent placement effects (IEEE TGCN).

- [[tang-2026-gat-antijamming]] - Tang et al. 2026. Hierarchical anti-jamming UAV control with GAT-based inner-loop beamforming and two-agent MADDPG outer-loop deployment/jammer-power adaptation (IEEE TWC).
- [[huroon-2026-bd-ris-rsma-uav]] - Huroon et al. 2026. Ground-mounted group-connected BD-RIS with cluster assignment and intra-group RSMA; augmented GBD plus BCD/SCA/RCG jointly optimize precoders, rates, trajectories, and non-diagonal scattering matrices (IEEE TWC).
- [[mihertie-2026-aerial-irs-rsma-ee]] - Mihertie et al. 2026. Communication-side energy-efficiency maximization for a UAV-mounted passive IRS MISO downlink with RSMA, aggregate hardware distortion, BCD/SCA, and sequential rank-one relaxation (IEEE TGCN).
- [[morshed-2026-active-ris-uav-noma-mappo]] - Morshed et al. 2026. Active-RIS-aided UAV-NOMA communication with MAPPO actors for BS power allocation, UAV motion, and RIS gain/phase under a shared rate/energy/fairness/outage reward (IEEE TGCN).
- [[huyen-2026-short-packet-aris-noma]] - Huyen et al. 2026. Finite-blocklength BLER and achievable-rate analysis for two-user NOMA through a UAV-mounted active RIS under imperfect SIC, plus one-dimensional power-split optimization (IEEE TMC).
- [[cui-2026-aris-v2x-icac]] - Cui et al. 2026. Active-RIS-aided multi-UAV V2X integrated communication/computation; ECCRA maximizes effective energy efficiency over ARIS association/beamforming, UAV/BS beamforming, vehicle scheduling, offloading ratios, and compute allocation (IEEE TMC).
- [[hu-2026-segmented-irs-cpn]] - Hu et al. 2026. Dynamically segmented IRS-assisted UAV computing-power network; MAPPO trajectory control plus phase alignment, association, compute allocation, and SCA-based IRS-row matching for delay/energy optimization (IEEE TMC).
- [[ahmed-2026-noma-irs-vehicular]] - Ahmed et al. 2026. Passive-IRS/NOMA UAV-to-vehicle sum-capacity optimization via projected fixed-point phase updates and alternating convex UAV power allocation (IEEE T-ITS).
- [[lin-2025-energy-effective-ris-multiuav-coverage]] - Lin et al. 2025. RIS-assisted multi-UAV coverage for fairness-aware ground terminals; K-DBSCAN deployment, throughput-variance filtering, and TDQN/DDQN/dueling-DQN trajectory control (IEEE TGCN).
- [[liu-2026-spherical-t-ris-bs]] - Liu et al. 2026. Angle-insensitive spherical transmissive-RIS base station with omnidirectional feed; BCD/SCA co-optimizes sensor scheduling, powers, phase shifts, and UAV trajectories for data collection under CU-rate and UAV-energy constraints (IEEE TWC).
- [[ning-2025-channel-aware-irs-uav]] - Ning et al. 2025. Channel-aware multi-IRS/multi-UAV NOMA communication with geometric blockage judgment, dynamic partitioned IRS-user association, MAPPO trajectory control, and SCA power allocation. *(DOI/venue not in parse.)*

- [[wu-2026-model-based-ppo-ris-uav-mec]] - Wu et al. 2026. RIS-assisted urban multi-UAV MEC with decentralized model-based PPO; local k-hop observations, RIS phase proposals, and branched rollouts for trajectory/offloading control (IEEE TMC).

- [[huang-2025-fedx-ris-uav-trajectory]] - Huang et al. 2025. RIS-assisted UAV communication trajectory planning with incomplete CSI, quadrotor propulsion, and FedX-accelerated SAC/PPO training (IEEE TMC).

- [[qin-2023-ris-uav-mec-ee]] - Qin et al. 2023. RIS-assisted UAV-MEC energy efficiency with NOMA; Dinkelbach + BCD/DC/SCA over task bits, power, RIS phase shifts, and UAV trajectory under imperfect CSI (IEEE TGCN).

- [[sheng-2025-ris-online-uav-mec]] - Sheng et al. 2025. RIS-empowered online UAV-MEC trajectory/resource allocation with mobile users and random arrivals; Lyapunov/Dinkelbach/BCD/SCA handle queue stability, outage constraints, UAV trajectory, and RIS phases (IEEE TGCN).
- [[chhea-2025-irs-uav-swipt-drl]] — Chhea et al. 2025. IRS-aided UAV **SWIPT** network; **DRL** with SINR-map reward maximizes average EE over trajectory + IRS phase shifts + transmit power + PS ratio (IEEE TVT).
- [[wu-2025-gai-ris-resource-management]] — Wu et al. 2025. **GAI + distributional RL (DBRL)** for RIS-aided 6G resource management; CDL cascade channel estimation + GAN-modeled distributional Q-function; maximizes joint EE + QoSSR (IEEE TCCN).
- [[wu-2025-iopo-irs-uav-thz-mec]] — Wu et al. 2025. **IRS-assisted** multi-UAV THz MEC; two-stage IOPO (order-preserving offloading + WOA phases).
- [[shao-2024-drl-antijamming-mec]] — Shao et al. 2024. **Anti-jamming** UAV-MEC resource management; PER-MATD3 (hardware-validated).
- [[beishenalieva-2026-secrecy-aware-uav-path-planning]] - Beishenalieva & Yoo 2026. Secrecy-aware UAV-ITS offloading against malicious aerial eavesdroppers/jammers; policy-gradient DRL path/power/mode control plus PSO slot allocation (IEEE T-ITS).
- [[chen-2026-maddpg-uav-swarm-antijamming]] - Chen et al. 2026. MADDPG-based multi-domain anti-jamming for UAV-swarm ITS monitoring; joint channel/power actions protect U2U payloads and U2G capacity under fixed, swept, and random jamming (IEEE T-ITS).
- [[yang-2026-embodied-antijamming-uav]] - Yang et al. 2026. Embodied anti-jamming resource allocation for U2U/U2I spectrum reuse; decentralized DDQN agents use prioritized and transferred experience for sub-band/power control under swept jamming, with Raspberry Pi/USRP channel validation (IEEE TWC).
- [[sun-2024-mfris-semantic-antijamming]] — Sun et al. 2024. **Multi-functional RIS** + **semantic** anti-jamming communication & computing for aerial-ground MEC; worst-case CSI; semantic-computation-rate max via monotonic optimization + DSOCP (+ GPI) (IEEE JSAC).
- [[sun-2024-active-passive-ris-receiver]] — Sun et al. 2024. **Active-passive cascaded RIS** receiver architecture for anti-jamming; worst-case rate max under imperfect angular jammer CSI via UM-ZF (passive) + AMM/C-M-CCD (active) semi-closed-form solutions (IEEE TWC). *(Physical-layer RIS-receiver anchor, not MEC.)*
- [[guo-2024-multiuav-proactive-eavesdropping]] — Guo et al. 2024. **Multi-UAV proactive eavesdropping** (legitimate surveillance): full-duplex UAVs jam multiple mobile suspicious links while planning trajectories; MDP decoupled into a closed-form **jamming-power solver** + per-UAV decentralized **RL moving policy** (IEEE TMC). *(Surveillance/PLS anchor, not MEC.)*

### UAV-swarm collaborative computing

- [[li-2026-jscfg-uav-grouping]] - Li, Xia, and Zhang 2026. Joint-switch coalition formation for dynamic heterogeneous-UAV mission grouping under ordered type requirements, overlapping coalitions, and predicted link persistence (IEEE TMC).
- [[zhang-2026-distance-attention-uav-navigation]] - Zhang et al. 2026. Distance-attention augmented CTDE reinforcement learning for cooperative 3-D UAV navigation in dense urban environments, with historical-feature-flow critics and explicit collision, timeout, and energy evaluation (IEEE TMC).
- [[zhang-2026-dt-aircomp-cluster-formation]] - Zhang et al. 2026. Digital-twin-empowered UAV-swarm cluster formation for AirComp, jointly optimizing UAV-group association, receiver scaling, device power, and collision-safe trajectories with BCD, SCA, and Dinkelbach iteration (IEEE TWC).
- [[sun-2024-asap-uav-swarm]] — Sun et al. 2024. **ASAP** — in-swarm collaborative DL inference (model + data partition, pipeline-parallel); hardware-validated.
- [[wang-2026-scalable-multiuav-analytics]] - Wang et al. 2026. Scalable collaborative multi-UAV video analytics; JDTSO centralized deployment/scheduling for small swarms and MAPDP distributed MAPPO+DAG partitioning for larger swarms (IEEE TGCN).
- [[zhu-2026-hab-mappo-target-search]] - Zhu et al. 2026. HAB-MAPPO cooperative UAV target search; 3D continuous trajectory, laser charging, heuristic image offloading/resource allocation, two-level attention, Beta policy, and curriculum learning (IEEE TMC).
- [[zhang-2026-ensemble-marl-uav-target-search]] - Zhang et al. 2026. Ensemble MARL for heterogeneous UAV target search in 3D; E-QMIX switches among graph, CNN, and DQN subnetworks using distance/camera/battery cues (IEEE TMC).
- [[wu-not-in-parse-aoi-sampling-buffering-routing]] - Wu et al. AoI-aware sampling, buffering, and routing for leader-follower UAV swarms; AASBR plus COMH-MAPPO jointly controls sensing, packet scheduling, and FANET next hops. *(Parsed metadata lacks DOI/venue/year.)*
- [[li-2026-la4h-uav-active-tracking]] - Li, Zhou, and Wu 2026. LA4H expert-assisted anomaly-aware UAV active target tracking; cross-modal anomaly cognition, assistance decisions, and teacher-student distillation for occlusion and distractor recovery (IEEE TMC).
- [[li-2026-tspf-forest-fire-uav-swarm]] - Li et al. 2026. Two-tier submodel partition for robust UAV-swarm forest-fire detection; graph-colored groups, intragroup backup, dynamic server selection, and two-tier federated aggregation (IEEE TMC).
- [[qu-ecoei-uav-swarm]] — Qu et al. **eCoEI** — elastic OODA-loop collaborative DL inference for UAV swarms, robust to node/A2A-link failure; proof-of-concept on Jetson devices (IEEE Communications Magazine; year not in parse).
- [[li-2025-stochastic-game-uav-swarm]] — Li et al. 2025. Energy-efficient UAV-swarm MEC as five **stochastic games** with dynamic clustering; RLDC multi-agent Q-learning.
- [[li-2025-dt-uav-swarm-resource-management]] — Li et al. 2025. Digital-twin-based task-driven UAV-swarm resource management for search and rescue; MADRL task crowdsourcing plus SNC traffic-flow delay bounds (IEEE T-ITS).
- [[jia-2026-ufsp-rail-inspection]] — Jia et al. 2026. Multi-UAV rail-line inspection under imperfect information; stochastic potential game + U-FSP belief-augmented Q-learning / policy averaging, with small-scale real-world deployment evidence (IEEE T-ITS).
- [[li-2024-rldc-uav-swarm-clustering]] — Li et al. 2024. **Conference precursor** of the above (IEEE WCNC 2024); six stochastic games + RLDC, no NE/convergence proof.
- [[zhang-2020-response-delay-uav-swarm]] — Zhang et al. 2020. **Response-delay** optimization for a MEC-enabled UAV swarm (T-UAV + B-UAVs); **stochastic geometry** + **queueing theory** closed-form delay; **hardware-validated** (2 DJI M100 + 5G NR mmWave) (IEEE TVT).

### Generative-AI MEC

- [[gong-2026-safe-economic-lae-trajectory]] - Gong et al. 2026. Hybrid SAC-LLM low-altitude UAV trajectory planning with obstacle avoidance, no-fly-zone/residential-zone compliance, landing, and energy constraints (IEEE TMC).
- [[wen-2026-hybridrag-low-carbon-lae]] - Wen et al. 2026. HybridRAG-formulated low-carbon LAE network optimization with R^2DSAC, a double-regularized diffusion-enhanced SAC solver (IEEE TMC).
- [[cai-2026-llm-drl-secure-lae-data]] - Cai et al. 2026. LLM-enhanced DRL for secure LAE data collection; LLM state/reward/simulator support for DDPG/TD3 with a data-collection UAV and a jamming UAV (IEEE TMC).
- [[wang-2026-llm-qos-multiuav-resource]] - Wang et al. 2026. LLM teacher-student QoS-aware resource allocation for multi-UAV cooperative edge computing; NKG/R-GAT/ToT teacher with MAPPO student distillation (IEEE TMC).
- [[wang-2026-lifelong-semantic-content-reuse]] — Wang et al. 2026. UAV-assisted Metaverse semantic content reuse; semantic subject/object caching plus DC-ELLA lifelong policy transfer for changing semantic environments (IEEE TMC).
- [[wang-2026-diffusion-semantic-uav-edge]] — Wang et al. 2026. UAV-assisted semantic edge computing; H-DDPG plus convex semantic-resource optimization, then diffusion-denoising DDPG for trajectory action generation (IEEE TWC).
- [[lin-2026-layered-semantic-uav-aggregation]] - Lin et al. 2026. Frozen image-semantic codec with learned or optimization-based signal/hover-position adaptation for OFDM-NOMA UAV aggregation (IEEE TWC).
- [[niu-2026-falcon-semantic]] - Niu et al. 2026. FALCON multimodal semantic communication; KANet/shared-prompt alignment, channel-aware Sparsemax token selection, and range-null diffusion signal recovery (IEEE TMC).
- [[zhang-2025-gsc-diffusion-semcom]] — Zhang et al. 2025. **Generative AI Semantic Communication (GSC)**: Swin Transformer encoder + **diffusion model** decoder for image transmission; +17.75% PSNR in AWGN vs DeepJSCC; MU-GSC multi-user extension (IEEE TCCN).
- [[ye-2025-aigc-diffusion-contract]] — Ye et al. 2025. Edge AIGC services via **contract theory** + prompt engineering; generative diffusion model as the contract-item optimizer.
- [[zhang-2024-gdmtd3-aerial-secure-cb]] — Zhang et al. 2024. UAV-swarm secure collaborative beamforming via **generative-diffusion-model-enhanced TD3** (GDMTD3).
- [[fu-2025-otae-inference-lae-batching]] — Fu et al. 2025. Over-the-air edge inference for low-altitude airspace; diffusion-based online batching + beamforming.
- [[du-2024-d2sac-aigc-asp-selection]] — Du et al. 2024. Edge AIGC-as-a-Service provider selection; diffusion decision generator (AGOD) inside SAC (**D2SAC**); beats 7 DRL baselines (IEEE TMC).
- [[wang-2024-wipe-gai]] — Wang et al. 2024. **WiPe-GAI** — wireless perception guides GAI for edge AIGC; sequential multi-scale perception predicts the user skeleton + a diffusion model generates the optimal **pricing** incentive strategy (IEEE TMC).
- [[du-2024-yolo-semcom-digital-twin]] — Du et al. 2024. **YOLO-based semantic communication** for **digital-twin** construction (apple orchard); a slimmed YOLOv7 (ELAN-H + SimAM) extracts semantic content from UAV images and transmission power is allocated by per-object importance — a confidence rule and a **diffusion-model-generated** scheme — cutting transmitted data ~91% on its case study (IEEE IoT-J).

### Generative-AI / GAN for ISAC & channels

- [[yang-2026-generative-radio-map-lae]] - Yang et al. 2026. CVCGAN-assisted generative radio map for LAE air-corridor channel estimation, with CNN integration over generated and estimated CSI (IEEE TMC).
- [[faisal-2025-cgan-ris-isac-channel]] — Faisal et al. 2025. **Conditional GAN** for channel estimation in RIS-assisted ISAC.
- [[zhang-2025-gan-td3-isac-active-ris]] — Zhang et al. 2025. **GAN-TD3** beamforming for ISAC with double active RISs.

### Multi-agent UAV-MEC

- [[peng-2025-drudm-cfg]] — Peng et al. 2025. Fairness-aware multi-agent DRL for HAS-UAV post-disaster MEC. *DRUDM-CFG*.
- [[zhang-2025-ssac-mgi-heterogeneous-uav]] — Zhang et al. 2025. Safe & energy-efficient trajectory planning for heterogeneous UAV-MEC. *SSAC-MGI* (shared SAC + Markov game of intervention).
- [[bi-2025-sg-mapg]] — Bi et al. 2025. Three-layer hierarchical Stackelberg game for UAV-MEC service fairness & cost. *SG-MAPG*.
- [[wang-2021-maddpg-multiuav-trajectory]] — Wang et al. 2021. **MADDPG** per-UAV trajectory planning for multi-UAV MEC; dual fairness (geographical + UE-load) + UE energy; low-complexity offloading step (IEEE TCCN).
- [[seid-2021-madrl-multiuav-iot-edge]] — Seid et al. 2021. Clustered multi-UAV IoT-edge offloading + resource allocation as a **stochastic game**; **MADDPG** (MADRL); energy+delay cost (IEEE TNSM).
- [[chen-2023-aiot-device-association]] — Chen et al. 2023. Distributed multi-UAV + GBS aerial MEC; QoE (avg response time + IoTD **cache-queue length**) max via joint **device association** (greedy recursive RSRT) + **task offloading** (0-1 knapsack-with-variable-value, backtracking BTO) + **MADDPG** UAV trajectory (IEEE IoT-J).
- [[ning-2023-madrl-uav-trajectory-differentiated-services]] — Ning et al. 2023. **Distributed multi-UAV trajectory** control in a **multi-SP differentiated-services** UAV-MEC with **non-binary, time-varying** user service preferences; minimizes short-term user + long-term UAV computational cost; proves a **unique Nash Equilibrium** (complete info) then a **Markov-game multi-agent DRL** controller using **local observations only** (IEEE TMC).

### Hierarchical aerial MEC (UAV + HAP)

- [[li-2026-uav-hap-ddqn-ppo-offloading]] - Li et al. 2026. Multi-UAV + HAP cooperative offloading; DDQN selects single-UAV/multi-UAV/HAP mode, PPO assigns cooperative ratios for energy-latency weighted consumption (IEEE TMC).


- [[nabi-2025-jour-hierarchical-aerial]] — Nabi & Moh 2025. *JOUR* — Gale-Shapley matching + ESAC for joint offloading, association, and resource allocation in UAV+HAP MEC.
- [[chen-2026-dart-hap-uav-mec]] — Chen et al. 2026. HAP-UAV-MEC with NOMA and WPT; DART combines Lyapunov decomposition, DDPG-attention trajectory/offloading, and convex resource allocation (IEEE TMC).
- [[bao-2025-ddpg-video-offloading]] — Bao et al. 2025. UAV+HAP video-analytics offloading with adaptive transcoding; DDPG over a QoE reward.
- [[jia-2026-dro-lawn-trajectory]] — Jia et al. 2026. Distributionally robust task-size offloading and UAV-trajectory optimization in a UAV/HAP low-altitude wireless network; L1/L-infinity/Fortet-Mourier ambiguity sets plus Benders/SCA (IEEE TMC).
- [[jia-2025-dro-uav-hap-mec]] — Jia et al. 2025. **Distributionally robust** UAV-HAP MEC under uncertain CSI; CVaR + primal decomposition + BWOA.
- [[jia-2022-hierarchical-aerial-matching]] — Jia et al. 2022. **Matching game** + heuristic for HAP+UAV aerial computing serving IoT (early anchor).
- [[kang-2023-mappo-hierarchical-aerial]] — Kang et al. 2023. **MAPPO** for UAV resource allocation + UAV→HAP offloading (CTDE).
- [[chen-2023-dotora-air-ground-online]] — Chen et al. 2023. HAP+UAV air-ground MEC; stochastic optimization + game theory (DGMS/TPA/DOTORA).

### Vehicular MEC

- [[ji-2026-llm-iov-uav-offloading]] - Ji et al. 2026. Multi-UAV-assisted IoV offloading; SOCP 3D trajectory, DRL+LLM resource scheduling, and LP task ratios for latency/energy/task-success tradeoffs (IEEE TMC).

- [[hu-2026-ertatd3-secure-caching]] - Hu et al. 2026. UAV-assisted vehicular MEC with secure task-result caching and ERTATD3 twin-actor reward shaping over trajectory/offloading/resource/caching decisions (IEEE TMC).
- [[ren-2026-security-aware-vec-td3]] - Ren et al. 2026. UAV-assisted security-aware VEC against a passive eavesdropper; TD3 controls UAV movement, offloading ratios, and VUE-UAV association under secure-rate degradation (IEEE TMC).
- [[feng-2026-prediction-service-migration]] - Feng et al. 2026. Prediction-assisted multi-UAV service migration and trajectory control for vehicular MEC; stacked LSTM + Lyapunov migration-cost control + MADDPG (IEEE TMC).
- [[chen-2026-hc-mappo-vehicle-twin-migration]] - Chen et al. 2026. Hierarchical-control MAPPO for vehicle-twin migration in UAV-assisted vehicular metaverses, using ACB-LSTM workload prediction and deterministic lower-layer migration mapping (IEEE TMC).
- [[wei-2026-airfogsim-uav-vfc]] - Wei et al. 2026. **AirFogSim** lightweight modular simulator for UAV-integrated vehicular fog computing; traffic/UAV mobility, communication, computation, energy, security/privacy, blockchain, and scheduling modules (IEEE TMC).
- [[zhou-2026-a2g-madrl-air-ground-vcs]] - Zhou et al. 2026. Air-ground vehicular crowdsensing with UAV-UGV pairs; A2G-MADRL combines HVGCN and dynamically ordered masked policy generation for sAoI, latency-weighted collection, and NOMA channel assignment (IEEE TMC).
- [[zhao-2026-uav-carrier-vcs]] - Zhao et al. 2026. Carrier-enabled UAV-UGV vehicular crowdsensing; HADRL-VCS combines attentive memory-integrated information exchange with mutual policy-divergence exploration (IEEE TMC).
- [[qi-2026-drone-vehicle-mec-inspection]] - Qi et al. 2026. Cooperative drone-vehicle MEC for low-altitude inspection; GV-carried accompanying/detached drones, battery swapping, route planning, and detached-drone speed optimization minimize mission completion time (IEEE TMC).

- [[liu-2025-multimodal-semantic-iov-jamming]] - Liu et al. 2025. Multi-UAV-assisted IoV MEC under jamming with multi-modal semantic communication; SC-MA-TD3 jointly controls UAV trajectories, user association, and channel selection to reduce delay and preserve semantic accuracy (IEEE TMC).
- [[liu-2025-mad2rl-dnn-vec]] — Liu et al. 2025. **MAD2RL** — DNN partitioning + task offloading in VEC; Lyapunov + diffusion-model-based MARL + convex resource allocation (IEEE TMC).
- [[huang-2024-fed-idcco-iov-caching]] — Huang et al. 2024. **Fed-IDCCO** — joint **data caching + computation offloading** in UAV-assisted IoV; DRL + **federated learning** (privacy + convergence); minimizes delay + maximizes cache hit ratio (IEEE TVT).
- [[li-2025-energy-latency-uav-vec]] — Li et al. 2025. UAV-assisted VEC **federated-learning participant selection** and bandwidth/compute allocation; weighted energy-latency cost as an MDP solved by AB-DDQN (AdamW + BOA hyperparameter tuning) (IEEE TGCN).
- [[li-2026-isac-vec-beamforming-deployment]] - Li et al. 2026. ISAC-enhanced UAV-assisted VEC; joint UAV deployment and beamforming via refraction-based sparrow search plus SCA/Taylor convexification, improving road-hotspot coverage and UAV energy (IEEE TWC).
- [[spampinato-2025-uabs-v2x-3dqn-ilp]] — Spampinato et al. 2025. UABS trajectory (**3DQN**) + **ILP** RRM for V2X extended-sensing in urban scenario; SUMO mobility; coverage-limited + capacity-limited scenarios (IEEE TVT).
- [[wang-2025-ctmig-task-migration-uav]] — Wang et al. 2025. **CTMiG / ILCTS** — joint task offloading + **migration** in multi-UAV MEC; PPO expert + **GAIL** online refinement; large-result delivery latency (IEEE TSC).
- [[zhang-2025-mcma-task-migration]] — Zhang et al. 2025. Task migration with Informer trajectory prediction across edge servers. *MCMA*.
- [[xie-2026-uav-multisource-fusion]] — Xie et al. 2026. UAV-enabled cooperative perception fusion via dynamic constrained multi-objective optimization.
- [[sun-2023-bargain-match-vec]] — Sun et al. 2023. **BARGAIN-MATCH** — bargaining (intra-server) + matching (inter-server) for VEC offloading.
- [[peng-2020-maddpg-uav-vehicular]] — Peng & Shen 2020. **MADDPG** multi-dimensional resource management (vehicle association + allocation) in MEC- and UAV-assisted vehicular networks; converges in ~200 episodes (IEEE JSAC).
- [[li-2024-airground-vec-offloading]] — Li et al. 2024. **Air-ground integrated VEC** (HAP + UAVs + RSU, each with MEC; UAVs/RSU also relay to the HAP); minimizes total task offloading delay (**JCESRA**) via BCD: many-to-one **matching** + **coalition game** (equipment selection) + CVX (bandwidth/compute) + **SCA** (UAV trajectory), then HAP as a **knapsack** solved by dynamic programming + compute reallocation (IEEE IoT-J).
- [[zhang-2026-dwell-time-aerial-vec]] — Zhang et al. 2026. Multi-layer aerial VEC with UAV/HAP service and a dwell-time feasibility constraint for high-speed vehicles; weighted latency+economic cost minimized via BCD/Lagrangian/ADMM-style allocation (IEEE T-ITS).
- [[ye-2021-ran-slicing-offloading]] — Ye et al. 2021. **Two-timescale joint RAN slicing + computation offloading** for autonomous vehicular networks (C-AVN); small-timescale task scheduling for load balancing with minimal offloading variation via cooperative **multi-agent deep Q-learning** (fingerprint), large-timescale **RAN slicing** as a convex program with statistical QoS, in a learning-assisted hierarchical loop (IEEE OJVT).
- [[dai-2024-uav-vehicular-offloading-lyapunov]] — Dai et al. 2024. UAV relieves **overloaded RSUs** in VEC; minimizes time-average vehicular task delay under long-term UAV energy via **Lyapunov** + **Markov-approximation** online offloading (IEEE TMC).
- [[mou-2025-adm-dt-migration]] — Mou et al. 2025. **Adaptive digital-twin migration** in vehicular edge networks (VECONs); minimizes communication + colocation + migration cost (NP-hard, three-way DT-communication latency) with an off-policy **actor-critic** agent **warm-started on expert (Greedy) demonstrations** then decayed; ~39% average migration-latency reduction on real Cologne traces (IEEE TVT).

### Maritime MEC

- [[yao-2026-secure-maritime-sutn]] - Yao et al. 2026. Robust coordinated beamforming and UAV trajectory design for secure maritime satellite-UAV-terrestrial coexistence under norm-bounded CSI errors (IEEE TWC).
- [[wang-2026-noma-marine-data-computation]] - Wang et al. 2026. NOMA marine sensing-data collection followed by UAV computation; min-max-normalized TD3 jointly controls trajectory, device power, and aerial compute allocation (IEEE TGCN).
- [[huang-2026-coded-caching-uav-marine]] - Huang et al. 2026. Coded caching-enabled D2D content delivery in UAV-assisted marine edge networks; UAV/buoy/AUV acoustic-RF architecture with OJC3D Lyapunov online trajectory/caching/request optimization (IEEE TMC).
- [[qian-2024-marine-fl-dt-secrecy]] — Qian et al. 2024. **FL-assisted marine digital twin** with secrecy; USV NOMA model-upload to HAP + chaotic spread-spectrum broadcast; energy minimization; layered decomposition (IEEE IoT-J).
- [[wang-2026-aerial-marine-msar]] — Wang et al. 2026. UAV+HAPS+MASS three-tier MEC for maritime search & rescue. *JCORA* (matching + convex + PGD).
- [[li-2026-cdto-inland-waterways]] — Li et al. 2026. UAV-assisted inland-waterway edge offloading; USV D2D computation-sharing clusters, UAV cluster-head positioning, exact-potential-game CDTO, and graph-based MARL (IEEE T-ITS).
- [[liao-2025-ris-uav-usv-resource-allocation]] — Liao et al. 2025. RIS-assisted UAV-USV cooperative MEC for inland waterways; bidirectional USV tasks with hard time windows, UAV routing, task-mode/arrival-time choice, hovering-coordinate, and RIS-phase optimization (IEEE TGCN).
- [[liao-2026-aoi-ris-uav-usv-mec]] - Liao et al. 2026. AoI-aware RIS-assisted UAV-USV MEC; TUAV-mounted RIS, RUAV trajectory/service-duration control, and Lyapunov plus enhanced WOA/AO optimization (IEEE TMC).
- [[lei-2024-hvmappo-maritime-sar]] — Lei et al. 2024. **Heterogeneous-vehicle maritime SAR** (observation UAVs + relay UAVs + ASV edge servers); joint trajectory + offloading + routing topology minimizing time/energy while maximizing relay **fault tolerance**; Dec-POMDP + **HVMAPPO** (MAPPO/CTDE + param-sharing + normalized GAE + Pop-Art) (IEEE TVT).
- [[liu-2025-haps-uav-maritime-iot]] — Liu et al. 2025. HAP-UAV maritime IoT comm: HAP-as-backhaul, UAV multicast, vessel unicast.
- [[wang-2025-double-edge-samin]] — Wang et al. 2025. Double-edge (UAV+LEO) offloading for space-air-marine networks; AO + layered decomposition.
- [[zhang-2025-three-tier-maritime-offloading]] — Zhang et al. 2025. Three-tier (MWD/OBS/LEO) maritime offloading; MINLP decomposition; 39.3% energy saving.
- [[wang-2024-maritime-eh-jcora]] — Wang et al. 2024. **Energy-harvesting** maritime MEC (solar + ocean-wave buoys); throughput max under queue + energy constraints; Lyapunov / JCORA (IEEE IoT-J).
- [[dai-2023-hybrid-marine-mmwl]] — Dai et al. 2023. **Hybrid** offshore (FDMA) + aerial-UAV (NOMA) multi-access offloading; min-max workloads latency (MMWL); layered 3-subproblem decomposition (IEEE TCOMM).
- [[dai-2023-hybrid-noma-fdma-marine]] — Dai et al. 2023. **Hybrid NOMA (underwater USN→USV) + FDMA (aerial USV→UAV)** multi-access offloading; **total-energy minimization + secrecy provisioning** against an eavesdropper; layered top/sub-problem line-search decomposition (IEEE TNSE).
- [[zhang-2024-dlrl-maritime-usv]] — Zhang et al. 2024. USV mobile-edge deployment + offloading; dual-layer RL (outer DDPG / inner Q-learning).
- [[you-2025-uncertain-maritime-hasac]] — You et al. 2025. Uncertain maritime MEC (AAVs+vessels); Lyapunov + Markov game + heterogeneous-agent SAC.
- [[wang-2024-twotier-satellite-marine]] — Wang et al. 2024. Two-tier satellite-marine offloading; hybrid **Stackelberg-Bargaining** game (NOMA/FDMA).
- [[qian-2022-uav-maritime-iot-noma]] — Qian et al. 2022. **NOMA-based UAV-assisted maritime IoT** MEC; USVs offload via uplink power-domain NOMA (SIC) to a UAV-MEC; **total-energy minimization** (USV tx/compute + UAV compute + UAV propulsion) over offload ratio + power + UAV compute allocation + trajectory; NP-hard → vertical two-layer decomposition: **DDPG** trajectory (top) + **Lagrangian** closed-form resource allocation (underlying) (IEEE IoT-J).
- [[lyu-2023-noma-marine-emergency-offloading]] — Lyu et al. 2023. **NOMA**-based UAV emergency communication for marine IoT; MINLP decomposed into quasi-convex/convex resource allocation + **coalition-game** offloading (CGTO) (IEEE IoT-J).
- [[qi-2024-msar-minmax-latency]] — Qi et al. 2024. Multi-UAV maritime **search & rescue**; **min-max latency** over offloading + R-UAV deployment + S-UAV–target association; iterative linearization + SCA + Branch-and-Bound (IEEE TVT).
- [[dai-2024-multiuav-marine-welfare]] — Dai et al. 2024. Multi-UAV multi-access marine MEC (UAVs + **ocean beacon stations**); maximizes **system revenue** (welfare − energy) via layered decomposition + **double-auction** OBS selection (IEEE TCOMM).
- [[li-2026-online-maritime-double-auction]] - Li et al. 2026. Online double auction for maritime network resource allocation; OMDAM prices ship connectivity bids against ISP antenna/UAV capacity with social-welfare, deadline, coverage, and budget-balance constraints (IEEE T-ITS).
- [[li-2023-secure-marine-iot-jamming]] — Li et al. 2023. **Secure** marine-IoT offloading: USVs upload to a **HAP** via NOMA then provide **cooperative jamming**; system-energy min via monotonic optimization (PAS) + cross-entropy (CASE) (IEEE TVT).
- [[lu-2023-uav-relay-secure-maritime-mec]] — Lu et al. 2023. **UAV-relay-assisted secure maritime MEC** with a **flying eavesdropper**; a relay UAV amplify-and-forwards maritime-device tasks to a coastal edge server while a **coastal jammer** disrupts an eavesdropping UAV; **max-min secure computing capacity** over transmit power + time-slot + local-computation + UAV trajectory; non-convex → **BCD + SCA** (IEEE TCOMM).
- [[zeng-2024-usv-fleet-collaborative-offloading]] — Zeng et al. 2024. UAVs offload tasks **to USV fleets**; first-price sealed **reverse auction** (reserve price) incentive + symmetric-equilibrium bidding, then BCD + improved **ADMM** energy minimization (IEEE TVT).
- [[liu-2022-maritime-uav-mec-virtualization]] — Liu et al. 2022. Two-layer maritime UAV-MEC (T-UAV MEC server over B-UAVs) with **VM-multiplexing** parallel computing under I/O interference; latency min via DQN + DDPG over T-UAV trajectory + VM count (IEEE TVT).
- [[li-2020-maritime-uav-satellite-coverage]] — Li et al. 2020. **Coverage enhancement** of a hybrid satellite-UAV-terrestrial maritime network; a **fixed-wing UAV** shares spectrum with satellites and uses TBS/satellite backhaul; jointly optimizes pre-planned **trajectory + in-flight transmit power** to **max-min ergodic rate** using only **location-dependent large-scale CSI** (AIS-derived ship positions); non-convex → decomposition + SCA + bisection (IEEE TCOMM). *(Maritime communication-layer coverage, not MEC offloading.)*

### Trust, security, and federated MEC

- [[zhong-2026-hierarchical-ota-fl]] - Zhong et al. 2026. A mobile UAV parameter server collects partial AirComp gradient aggregates along its path and combines them hierarchically under gradient-correlation-aware MSE optimization (IEEE TWC).
- [[ron-2026-federated-a3c-uav-energy]] - Ron and Lee 2026. Hierarchical federated A3C for UAV-relayed FR3 networks; ground users jointly select powers, UAV hover positions, bandwidth fractions, and associations for compute/transmit energy and round-trip service reliability (IEEE TGCN).

- [[fu-2026-uav-fl-user-grouping]] - Fu et al. 2026. DBSCAN client grouping and two-phase SCA jointly control FL participation, data volume, UE power, UAV hover time, and trajectory under an expected-global-loss bound (IEEE TGCN).
- [[li-2026-clp-uav-hpfl]] - Li et al. 2026. Critical-learning-period-aware hierarchical personalized FL with parameter-divergence and data-drift detectors plus SAC-controlled UAV visits and aggregation periods (IEEE TMC).
- [[chen-2026-sdhfl-completion-time]] - Chen et al. 2026. UAV-assisted semi-decentralized hybrid FL with D2D cluster consensus, asynchronous UAV aggregation, Lyapunov cluster selection, and joint mobility/resource optimization for completion time (IEEE TMC).
- [[zhou-2026-cpsfl-uav-foundation-models]] - Zhou et al. 2026. Communication-pipelined split federated learning for LoRA fine-tuning of foundation models in UAV networks; sequential downlink gradient transmission plus attention-based DRL split/resource decisions (IEEE TMC).
- [[lim-2021-uav-iov-contract-matching]] - Lim et al. 2021. Multidimensional contract screening plus stable UAV-subregion matching for federated IoV data collection under private sensing, travel, computation, and upload costs (IEEE T-ITS).
- [[zhao-2026-uav-fl-inspection-incentives]] - Zhao et al. 2026. Contract-theoretic incentive assignment for UAV-client federated intelligent inspection under communication-sensing-computing integration; models data quality, sensing/computation costs, and FL participation utilities (IEEE TMC).
- [[huang-2026-aircomp-uav-swarms-afl]] - Huang et al. 2026. AirComp-assisted asynchronous federated learning for UAV swarms; branch-and-bound/AO aggregation scheduling plus layer-wise staleness filtering for faster convergence (IEEE TWC).
- [[qian-2026-federated-bandit-aircomp]] - Qian et al. 2026. Event-triggered federated LinUCB over UAV-aided AirComp; BCD-ADMM controls power, receive normalization, and UAV trajectory under channel-noise-aware regret analysis (IEEE TMC).
- [[gong-2026-lp2-casku-uav-clusters]] - Gong et al. 2026. LP2-CASKU privacy-preserving authentication and session-key update for dynamic low-altitude UAV clusters; message aggregation, cross-cluster anonymity/unlinkability, and forward/backward secrecy (IEEE TMC).
- [[mao-2025-bcsa-frl]] — Mao et al. 2025. Blockchain-enabled cold-start FRL for ZT LEO satellite networks. *BCSA-FRL* (CCVM + CSRA).
- [[mao-2025-irs-noma-fl-secrecy]] — Mao et al. 2025. **IRS-assisted** secrecy-rate maximization for **NOMA-based federated-learning** model aggregation; max-min secrecy rate over device power + IRS phase shift via **DDPG** (IEEE TCCN).
- [[qin-2025-bcuav-masac]] — Qin et al. 2025. Blockchain-enabled secure UAV-MEC: Lyapunov + MASAC + DOA.
- [[benaya-2025-aerial-isac-haps]] — Benaya et al. 2025. HAPS-mounted FD ISAC + friendly-jamming UAV + ground MEC; AO + SDR + SCA.
- [[wu-2025-security-aware-multiuav-service-placement]] - Wu et al. 2025. Security-aware multi-UAV MEC service placement and task offloading with a cooperative UAV jammer; OE-MATD3 plus closed-form device transmit power (IEEE TMC).
- [[wang-2026-blockchain-lae-fl-mappo]] — Wang et al. 2026. Blockchain-assisted low-altitude edge-intelligence network; UEs/TUAVs/SUAVs/BS four-layer offloading+caching+FL stack, FL-MAPPO-BOCRAOA, PV-aware throttling, M/M/1 queueing, and blockchain-supported cache cooperation (IEEE TMC).
- [[wang-2025-acbft-uav-consensus]] — Wang et al. 2025. **ACBFT** — PSO-ordered chain-based Byzantine fault-tolerant consensus for UAV ad hoc networks.
- [[wang-2024-blockchain-uav-mec-dpos]] — Wang et al. 2024. **Blockchain-integrated** UAV-assisted MEC; improved **DPoS** consensus (UAV light nodes + reputation-voted ground full nodes) + two-stage **Stackelberg** game over trajectory and resource allocation, solved with SCA (IEEE TVT).

### ISAC, sensing & physical-layer security

- [[wang-2026-covert-cognitive-radio]] - Wang et al. 2026. Finite-blocklength covert secondary transmission uses a UAV-forwarded primary signal as masking interference while preserving primary QoS under multi-warden constraints (IEEE TWC).
- [[lin-2026-fc-ris-surveillance]] - Lin et al. 2026. UAV-borne fully connected RIS surveillance with reflecting-channel antenna selection, closed-form monitoring-success probabilities, and statistical placement (IEEE TWC).
- [[zhan-2026-star-ris-aerial-monitoring]] - Zhan et al. 2026. STAR-RIS-assisted aerial monitoring couples stochastic target motion, indoor/outdoor dissemination, beamforming, UAV trajectory, and a Lyapunov propulsion-energy queue (IEEE TWC).
- [[wang-2026-multiuav-transceiver-beamforming]] - Wang et al. 2026. Multi-UAV ISAC transmit and receive beamforming with exact fixed-block receive updates, Dinkelbach/SDR transmit optimization, and SCA trajectory refinement (IEEE TGCN).
- [[wang-2026-fd-covert-isac]] - Wang et al. 2026. Covert UAV-ISAC with full-duplex receiver jamming, sensing-assisted cover traffic, bounded warden-location uncertainty, and alternating SDR/SCA optimization (IEEE TWC).
- [[chen-2026-aris-location-privacy]] - Chen et al. 2026. A virtual-partitioned active RIS splits elements and power between legitimate-UAV sum rate and artificial-noise interference against malicious RSS localization (IEEE TWC).
- [[chen-2026-pointrl-uav-isac]] - Chen et al. 2026. Point-cloud DQN jointly selects UAV motion and communication power from vehicle radar returns, balancing communication, radar capacity, and minimum-user performance (IEEE TMC).
- [[bai-2026-passive-uav-detection]] - Bai et al. 2026. Ambient-DTMB channel estimation and a compact temporal network detect UAV presence and classify four motion states in physical outdoor experiments (IEEE TWC).
- [[zhang-2026-polarfix-uav-mmwave]] - Zhang et al. 2026. Passive polarization conversion and programmable transmissive beamforming improve orientation-sensitive COTS 802.11ad links in a ground-motion prototype (IEEE TMC).
- [[lyu-2023-isac-maneuver-beamforming]] - Lyu et al. 2023. Sensing-feasible placement/reachability plus alternating SCA/SDR UAV maneuver and transmit-beam design (IEEE TWC).

- [[guo-2026-dual-objective-multiuav-isac]] - Guo et al. 2026. Multi-UAV trajectories, powers, user associations, and target associations optimized as a communication-sum-rate versus sensing-CRB Pareto front by archive-guided MOEA/D with adaptive PSO/GA updates (IEEE TWC).
- [[lu-2026-multiuav-iscpt]] - Lu et al. 2026. Cascading residual graph attention generates static 3-D multi-UAV deployment and powers for worst-user communication, sensing, and RF-energy metrics (IEEE TMC).
- [[yao-2026-transformer-mean-field-isac-sagin]] - Yao et al. 2026. Transformer-encoded mean-field actor-critic control of cross-tier interference, UAV roles, beamforming, association, and trajectories in an ISAC-SAGIN Stackelberg formulation (IEEE TWC).
- [[deng-2025-covert-isac-trajectory]] - Deng et al. 2025. UAV-ISAC sensing waveforms mask covert information transmission while BCD alternates SDR beamforming and SCA trajectory updates (IEEE TWC).
- [[zhou-2026-jrc-multiuav-resource]] - Zhou et al. 2026. Worst-user-rate versus worst-target-SPEB JRC design with joint association, power, and spectral-clustering/Gibbs multi-UAV deployment (IEEE TWC).

- [[cheng-2026-cnn-mamba-cracks]] - Cheng et al. 2026. WTCMamba pavement-crack segmentation combines CNN features, Haar-wavelet guidance, and Mamba selective state-space blocks; an LMC-Belloch/Triton scan is benchmarked on Jetson, separately from the proposed air-ground acquisition platform (IEEE T-ITS).
- [[li-2026-directional-modulation-irs-uav]] - Li et al. 2026. IRS-assisted UAV directional modulation with discrete phase shifts; VT, CE-VT, and BCD-VT jointly design symbol-level digital weights, UAV position, and IRS phases to preserve the legitimate constellation while disrupting an eavesdropper (IEEE TGCN).
- [[qin-2023-symmetry-augmented-uav-isac]] - Qin et al. 2023. Multi-UAV ISAC association, trajectory, and sensing/communication power control via SAC with permutation-equivariant replay augmentation, plus a CTDE MASAC alternative (IEEE TWC).
- [[wu-2026-sensing-error-uav-scheduling]] - Wu et al. 2026. Sensing-error-aware multi-UAV ISAC scheduling with an error-averaged communication rate, diffusion-augmented MADQN replay, and adaptive sensing periods (IEEE TWC).
- [[lyu-2026-situation-aware-uav-isac]] - Lyu et al. 2026. Phase-dependent periodic/event-triggered sensing with angle-only or position-plus-angle UAV control for industrial relay energy efficiency (IEEE TWC).
- [[xu-2026-hecta-predictive-beamforming]] - Xu et al. 2026. HECTA-Net predicts BS transmit and UAV receive beams directly from historical matched-filtered ISAC echoes through CNN, dilated causal TCN, and temporal attention (IEEE TWC).
- [[meng-2026-uav-isac-corrections]] - Meng et al. 2026. One-page correction to periodic UAV-ISAC throughput optimization; removes a duplicated association factor and supplies the omitted auxiliary-variable/Taylor transformation that makes the corrected subproblems convex (IEEE TWC).
- [[meng-2023-uav-ipsac-throughput]] - Meng et al. 2023. Integrated periodic sensing and communication with joint UAV trajectory, user/target scheduling, and beamforming; read with the 2026 convexification correction (IEEE TWC).
- [[he-2026-lscr-uav-relay-tracking]] - He et al. 2026. LSCR target handover for collaborative UAV relay tracking; Delaunay target graphs, TGR features, and Twin-GRCN similarity matching reach 92.1% accuracy with 0.063 KB transfer and a 20 KB model (IEEE T-ITS).
- [[wang-2026-rmaddpg-dda-uav-isac-vehicular]] - Wang et al. 2026. UAV-enabled vehicular ISAC with RMADDPG-DDA adaptive control over UAV motion/yaw, communication power, and ISAC transmit power; RND novelty, parameter sharing, and dynamic data augmentation improve served users and effective MI (IEEE TMC).
- [[hazarika-2026-dynamo-uav-vehicle-tracking]] - Hazarika & Rahmati 2026. Predictive UAV tracking for fast-moving vehicles using DynaMo motion prediction, DTPM prioritization, CRLB/FIM optimization, and POMDP-MADDPG control (IEEE T-ITS).
- [[bai-2026-aoi-uav-isac]] - Bai et al. 2026. AoI-centric UAV-enabled ISAC with SAC trajectory/beam activation, Kalman target prediction, and RZF communication beam synthesis for freshness-aware target updates (IEEE TMC).
- [[yan-not-in-parse-multibs-isac-uav-trajectory]] - Yan et al. Asynchronous UAV trajectory monitoring in cellular ISAC; LDFT/TO-CFO preprocessing, compressed-sensing multi-BS feature fusion, and SUKF trajectory tracking. *(Parsed metadata lacks DOI/venue/year.)*
- [[bayessa-not-in-parse-uav-isac-secure-content-hdrl]] - Bayessa et al. UAV-enabled ISAC secure content delivery; CRLB/EKF eavesdropper localization plus action-masked hierarchical DDQN over caching, association, deployment, and beamforming. *(Parsed metadata lacks DOI/venue/year.)*
- [[li-2026-control-based-uav-isac]] - Li et al. 2026. Control-based UAV-ISAC beamforming and trajectory design; SCA/SDR beamforming plus 3-DoF/6-DoF control-parameterized trajectory optimization by SQP reduces actual-flight sensing violations and rate degradation (IEEE TWC).
- [[zhao-2026-mappo-jscc-aec]] - Zhao et al. 2026. HAP-assisted multi-UAV sensing-communication-computing; Lyapunov energy stability plus MAPPO-JSCC with embedded sensing, SCA, and Dinkelbach solvers (IEEE TWC).
- [[wen-2026-uav-edge-inference-iscc]] - Wen et al. 2026. UAV-assisted ISCC edge inference; Hamiltonian-cycle access ordering plus AO/SA trajectory/resource optimization under discriminant-gain accuracy constraints (IEEE TWC).
- [[zhou-2026-radar-energy-iscac]] - Zhou & Liu 2026. Multi-UAV ISCAC with HAP-side MEC processing; three-layer SCA/relaxation algorithm trades radar sensing data against total energy over scheduling, power, and UAV/HAP trajectories (IEEE TGCN).

- [[huang-2026-offgrid-lae-imager]] - Huang et al. 2026. Cooperative cellular-ISAC low-altitude imaging; CS/PSF analysis plus physics-embedded DNN/OHEM off-grid reconstruction from CSI, reporting up to 97.55% detection rate in the parsed ablation (IEEE TWC).
- [[hou-2025-pbia-air-iscc-uav-its]] - Hou et al. 2025. UAV-swarm Air-ISCC for ITS; PBIA/PPO jointly controls sensing time, power, service association, and compute allocation to balance success rate and UAV energy (IEEE TGCN).

- [[li-2023-adaptive-digital-twin-uav-iscc]] - Li et al. 2023. DT-enabled UAV-assisted ISCC; ATB-MAPPO with Beta-policy actors and attention critics for radar beampattern / energy tradeoff (IEEE TGCN).
- [[tang-2025-cooperative-isac-lae]] - Tang et al. 2025. Cooperative ISAC for low-altitude economy; tensor-decomposition monostatic estimation, false-removing MST association, Pareto position fusion, and residual-weighted velocity estimation (IEEE TWC).
- [[zhang-2025-cooperative-anti-uav-isac]] - Zhang et al. 2025. Multi-cell anti-UAV ISAC transceiver beamforming; centralized AO/SCA/Dinkelbach and primal-decomposition distributed solvers maximize sensing SCNR under user-SINR and BS-power constraints (IEEE TWC).
- [[zhang-2026-air-sea-isac-inspection]] - Zhang et al. 2026. Energy-aware UAV-USV inspection using target clustering, heterogeneous Bi-TSPN routing, SCA refinement, and alternating hover-point beamforming/current-aware marine motion (IEEE TWC).
- [[wang-2026-robust-anti-uav-isac]] - Wang et al. 2026. Multi-UAV anti-UAV ISAC with slot-wise transmitter/receiver roles, worst-case CRB, robust beamforming, and trajectory optimization under target-position uncertainty (IEEE TWC).
- [[wang-2025-cellular-uav-cooperative-detection]] - Wang et al. 2025. Ground-BS and cellular-UAV cooperative detection through delay/Doppler/DoA estimation, state association, EKF fusion, and trajectory/beamforming control (IEEE TWC).
- [[jing-2024-isac-trajectory-localization]] - Jing et al. 2024. Multi-stage estimate-design-sense UAV trajectory and bandwidth allocation for joint communication and target localization under a finite energy budget (IEEE TWC).
- [[lu-2026-icsn-beamforming]] - Lu et al. 2026. Low-altitude integrated communication, sensing, and navigation beamforming with CRB-guided angular confidence regions and fractional programming; navigation is represented by angle delivery rather than navigation error (IEEE TGCN).
- [[ye-2026-mode-lae-isac]] - Ye et al. 2026. Multi-objective LAE ISAC; MODE combines DDPG with mixture-of-experts multi-task learning to tune the communication/sensing tradeoff across objective-preference weights (IEEE TMC).
- [[zhao-2025-networked-isac-uav-handover]] - Zhao et al. 2025. Networked ISAC UAV tracking/handover for LAE; virtual sensing cells, MUSIC estimation, centralized EKF fusion, PBS handover, and VSC handover maintain multi-BS tracking (IEEE TWC).
- [[cao-2026-uav-self-tracking-ms-mm]] - Cao et al. 2026. GNSS-independent 3-D UAV self-tracking from non-cooperative anchors; EAIP minor-subspace updates, continuous MM position iteration, KF/MA smoothing, and per-dimension CRLB benchmarking (IEEE TWC).
- [[wang-2026-stbc-cooperative-isac]] - Wang et al. 2026. Space-time block codec cooperative ISAC; multi-BS shared-resource UAV sensing with robust inter-BS nulling, STBC echo separation, and SINR-weighted fusion (IEEE TMC).
- [[ye-2026-meta-deepesc-lae-isac]] - Ye et al. 2026. Meta-DeepESC for energy-efficient LAE ISAC; TD3-style constrained action selection, episodic replay, and meta-learning for GBS beamforming plus authorized-UAV trajectories (IEEE TMC).
- [[ye-2026-deeplsc-lae-isac]] - Ye et al. 2026. DeepLSC LAE ISAC; DDPG-based joint GBS beamforming and UAV-trajectory control with constrained noise exploration, hierarchical replay, and symmetric experience augmentation (IEEE TWC).
- [[zeng-2026-fmcw-isibc-lae]] — Zeng & Liang 2026. **FMCW-enabled integrated sensing, identification, and backscatter communication** for LAE; UAV-mounted BDs modulate identity symbols onto FMCW echoes, with SVD-based range/velocity/symbol estimation and CRLB analysis (IEEE TWC).

- [[qin-2025-urllc-noma-uav-iscc]] — Qin et al. 2025. **NOMA-aided UAV ISCC** with URLLC: sensing + communication + computation; Lyapunov tail-constraint + **SAC-TPBD** DRL; comparable to SCA/SDR baselines with higher efficiency (IEEE TVT).
- [[tang-2024-iscc-uav-feel]] — Tang et al. 2025. **ISCC** for UAV-assisted federated edge learning; deployment + sensing/compute/comm via AO (BBPO).
- [[wang-2024-ttw-amd-localization]] — Wang et al. 2024. **Through-the-wall (TTW)** passive AMD detection + localization via CSI; reference-channel SSI cancellation + 2D matrix pencil ToF/PLCR estimation; hardware-validated (glass/brick walls: 0.964/0.952 detection accuracy, 1.65/2.05 m median error) (IEEE JSAC).
- [[yao-2025-secure-isac-dual-eavesdropping]] — Yao et al. 2025. Secure UAV-ISAC against dual eavesdropping; AO + SCA + SDR for secrecy + sensing security.
- [[chen-2024-three-party-hierarchical-game-pls]] — Chen et al. 2024. **Three-party hierarchical game** for PLS with dynamic trilateral coalitions (LUs / EVs / JAs); HCSF + DRL (IEEE TWC).
- [[wang-2026-secure-lae-uav-scheduling]] — Wang et al. 2026. Secure low-altitude aerial communications; UAVs dynamically switch between communication and artificial-noise jamming roles while optimizing scheduling, power, 3D trajectory, and velocity for secrecy energy efficiency (IEEE TWC).
- [[li-2026-secrecy-ee-uav-ris-iov]] - Li et al. 2026. Untrusted-relay mobile-IoV security with vehicle jamming and UAV-mounted RIS; Dinkelbach/CCCP, MM, and firefly-warm-started DDPG maximize secrecy energy efficiency (IEEE TWC).
- [[hosseini-2026-aoi-covert-uav]] - Hosseini et al. 2026. UAV-assisted covert communication with AoI minimization, PD-NOMA public cover traffic, aerial Eve detection, and AO/SCA/SDR trajectory-beamforming design (IEEE TWC).
- [[zhang-2026-air-ground-covert-jamming]] - Zhang et al. 2026. Air-ground cooperative covert transmission with UAV-mounted RIS directional jamming, SDR/Dinkelbach static optimization, and DDQN trajectory/user scheduling (IEEE TMC).
- [[chen-2026-air-ground-covert]] - Chen et al. 2026. Air-to-ground covert communication under Willie-location uncertainty and PPP environmental interference; gamma interference approximation, covertness/reliability/covert-throughput analysis (IEEE TWC).
- [[li-not-in-parse-movable-antenna-pls]] - Li et al. Physical-layer-security comparison of movable-antenna micro-mobility and UAV macro-mobility; projected-gradient/AdaGrad position control is benchmarked against AO/SCA UAV trajectory optimization. *(Parsed metadata lacks DOI/venue/year.)*
- [[he-not-in-parse-cipc-covert-uav]] - He et al. Multi-user secret and covert UAV communication using Bob's confidential signal as NOMA cover and truncated channel-inversion power control; analytical rotary-wing and AO/SCA fixed-wing designs. *(Parsed metadata lacks DOI/venue/year.)*
- [[michailidis-2024-secure-ris-uav-mec-iot]] — Michailidis et al. 2024. Secure UAV-**RIS**-MEC-IoT offloading against **aerial + ground eavesdroppers**; SOP over Nakagami-m + max-min **secure computation efficiency** via Dinkelbach + BCD + bisection (IEEE TCOMM).
- [[su-2024-sensing-aided-isac-pls]] — Su et al. 2024. **Sensing-aided PLS** for ISAC: dual-functional BS estimates eavesdropper directions (CAML) then jointly minimizes CRB and maximizes AN-aided secrecy rate via AO + fractional programming (IEEE TWC).
- [[wen-2024-iscc-edge-ai]] — Wen et al. 2024. **Task-oriented ISCC** for multi-device **edge-AI inference**: ISAC devices radar-sense multi-view data, quantize + offload features to an edge server running split inference; maximize **discriminant gain** (KL-divergence accuracy surrogate) over sensing/transmit power + comm time + quantization bits; non-convex but solved **optimally** by the **sum-of-ratios** method (IEEE TWC).
- [[zhu-2024-sensing-comm-doppler-uav-swarm]] — Zhu et al. 2024. **Sensing-communication co-design** for UAV-swarm-assisted vehicular networks in perspective of **Doppler**; min-max GV **CRLB** under SNR-loss constraint via differential evolution (IEEE TVT).
- [[chu-2024-secure-ris-isac]] — Chu et al. 2024. **Secure RIS-ISAC** correspondence; maximize radar output SNR under per-user comm SINR + eavesdropping-SINR ceiling + power + RIS unit-modulus; AO + SDR + fractional programming + **majorization-minimization**; ~2 dB radar gain vs no-RIS (IEEE TVT). *(PHY secure-ISAC anchor, not MEC.)*
- [[zhu-2024-crb-active-ris-isac]] — Zhu et al. 2024. **Active-RIS-empowered ISAC** for an obstructed target; derives the **CRB** for target **DoA** estimation and minimizes it over BS precoding + active-RIS reflection beamforming under per-user SINR + BS/RIS power + RIS amplitude constraints; AO + SDR + **majorization-minimization**; >30 dB CRB reduction vs passive RIS (IEEE TWC). *(PHY active-RIS ISAC anchor, not MEC.)*
- [[zhao-2018-caching-uav-ia-secure]] — Zhao et al. 2018. **Caching-UAV secure transmission** in hyper-dense small cells; **interference alignment** (SBS precoding) for single-antenna UAVs + idle SBSs repurposed as zero-forced **friendly jammers** against a passive eavesdropper; feasibility + secrecy analysis (IEEE TCOMM). *(Caching + interference-alignment PLS anchor, not MEC offloading.)*
- [[zhu-2024-zdrl-uav-tracking]] — Zhu et al. 2024. **Collaborative-RL 3D UAV tracking**; one active + four passive UAVs localize a target via TDOA/TSWLS; joint power + trajectory design via **Z-function-decomposition RL** (distributional RL); up to 39.4% / 64.6% lower positioning error vs VD-RL / independent DRL (IEEE TMC). *(UAV localization + trajectory design, not MEC offloading.)*
- [[zhu-2026-uav-localization-jamming]] - Zhu et al. 2026. 3-D UAV localization under jamming; BS switches GAN/TDOA positioning methods and passive-measurement subsets while mixture-Gaussian collaborative RL controls active-UAV power and trajectories (IEEE TMC). *(UAV localization security, not MEC offloading.)*
- [[an-2024-multilayer-ris-hap-swipt]] — An et al. 2024. **Multi-layer refracting RIS-assisted receiver** enabling **SWIPT** over long-distance **HAP** links; worst-case sum-rate max under imperfect angular CSI + non-linear EH; scalable toolbox-free robust optimization (CSI discretization + **LogSumExp-dual** precoder + **M-CCD** RIS coefficients + closed-form PS/decoder) (IEEE TWC). *(PHY RIS-receiver / SWIPT anchor, not MEC offloading.)*
- [[ma-2024-covert-mmwave-finite-blocklength]] — Ma et al. 2024. **Covert mmWave communication with finite blocklength** against **spatially random wardens** (Willies as a PPP); derives covertness-constraint + **average effective covert throughput (AECT)** expressions for **phased-array (PA)** and **linear frequency diverse array (LFDA)** beamforming via **stochastic geometry**, then jointly optimizes transmit power + blocklength; the best scheme (PA vs LFDA) depends on the receiver's direction (IEEE IoT-J). *(Covert-communication / PHY-security anchor, not MEC.)*

### Collaborative beamforming & aerial communications

- [[chai-2026-random-position-relay-deployment]] - Chai et al. 2026. Statistical-user-position UAV relay deployment and power control with independent DQN agents plus greedy association/load repair (IEEE TGCN).
- [[wang-2026-6dara-cellfree]] - Wang et al. 2026. Two-timescale aerial cell-free control with six-dimensional rotatable arrays, team-MMSE combining, potential-game association, and AB-MAPPO geometry updates (IEEE TWC).
- [[fang-2026-cellfree-uav-predictive-beamforming]] - Fang et al. 2026. Ground-AP EKF tracking, covariance-intersection fusion, and PCRB-guided pilots support predictive cell-free UAV beams and resource allocation (IEEE TWC).
- [[ren-2026-distributed-uav-los]] - Ren et al. 2026. Finite Matérn hard-core base stations and the 3GPP urban UAV LoS model yield outage/capacity comparisons for best, nearest, and LoS-conditioned association (IEEE TGCN).
- [[krishna-m-2026-multiuav-nbiot]] - Krishna M. and Balasubramanya 2026. Stationary UAV relays combine NB-IoT, Zadoff-Chu code-domain NOMA, and dynamic longest-load-first grouping (IEEE TMC).
- [[sun-2021-temcmop-uav-cb]] — Sun et al. 2021. **Earliest CB entry** — UAVs form a virtual antenna array to communicate with remote BSs; multi-objective **TEMCMOP** (transmission time / VAA-performing time / motion+hovering energy) over positions + speeds + excitation weights + BS-serving order; NP-hard, energy-optimal-speed reformulation + **improved multi-objective ant lion optimizer (IMOALO)** with chaos-OBL init + hybrid update (IEEE JSAC).
- [[sun-2025-emoppo-vlh-aerial-cb]] — Sun et al. 2025. AAV-swarm **collaborative beamforming** (virtual antenna array) to a terrestrial mobile user; evolutionary multi-objective PPO with vectorized value + LSTM + hyper-sphere task selection (EMOPPO-VLH).
- [[li-2024-emodrl-ground-space-cb]] — Li et al. 2024. **Distributed collaborative beamforming** for ground-space (terminal-to-LEO) uplink; evolutionary multi-objective DRL (EMODRL); saves 30% handover frequency.
- [[li-2024-emssa-uav-swarm-vaa]] — Li et al. 2024. **Virtual antenna arrays** for UAV-swarm-assisted IoT data harvesting/dissemination; multi-objective (time / eavesdropper / energy) **salp swarm** optimizer (EMSSA); ground + aerial CB (IEEE TMC).
- [[sun-2024-imssa-uav-secure-cb]] — Sun et al. 2024. **Secure** UAV collaborative beamforming (UVAA) with **imperfect / unknown eavesdropper** information; multi-objective SCMOP (worst-case secrecy rate / max SLL / flight energy) solved by an **improved multi-objective salp swarm algorithm** (IMSSA); Raspberry Pi demo (IEEE TMC).
- [[huang-2025-dual-aav-maritime-secure-cb]] — Huang et al. 2025. **Dual AAV cluster** maritime secure communication via CB: an MUVAA **relay** forwards data to a vessel while an MUVAA **jammer** beams jamming at the eavesdropper; multi-objective SEMCMOP (Bob SINR / Willie SINR / flight energy) solved by an **improved multi-objective mayfly algorithm** (IMOMA) (IEEE IoT-J).
- [[liang-2024-hmecmop-uav-cb]] — Liang et al. 2024. UAV-swarm **collaborative beamforming** to remote BSs; multi-objective **hovering vs motion energy** minimization (HMECMOP) over positions + excitation weights + BS-communication order; **improved multiverse optimizer** (IMOMVO) (IEEE IoT-J).
- [[zheng-2024-recmop-uav-cb]] — Zheng et al. 2024. **Reliable + energy-efficient** UAV collaborative beamforming (UVAA relay → remote BSs) in emergency communications; multi-objective RECMOP (max-min BS SNR / min-max AU SNR / min propulsion energy) over UAV locations + excitation weights; **improved multi-objective gravitational search algorithm** (IMOGSA) (IEEE TWC).
- [[liu-2024-hatrpo-ucb-cb]] — Liu et al. 2024. UAV-enabled **collaborative beamforming** (UVAA → remote BSs); multi-objective UCBMOP (max transmission rate / min UAV energy) over positions + excitation weights; **heterogeneous-agent trust-region MADRL** (HATRPO-UCB) with observation enhancement + agent-specific global state + Beta-distribution policy (IEEE TMC).
- [[li-2025-omrp-cb-iot]] — Li et al. 2025. **Collaborative beamforming for static ground IoT** (the corpus's only ground-IoT CB entry): a sensing-area-**overlap**-driven hierarchical clustering routing protocol (**OMRP**) feeds **SoftPPO-LSTM** CB-node selection for the long uplink to a remote BS; +17% network lifetime over benchmark routing, +8.3% CB throughput over benchmark algorithms, Raspberry Pi 4B deployment (IEEE IoT-J).
- [[chakareski-2019-uav-mmwave-hetnet-ee]] - Chakareski 2019. Energy-efficient UAV-assisted millimeter-wave 5G heterogeneous cellular networking; optimizes UAV-BS placement/offloading and bandwidth/energy tradeoffs for mmWave small-cell support (IEEE TGCN).
- [[zeng-2026-movable-antenna-u2u-channel]] - Zeng et al. 2026. Movable-antenna-aided MIMO wideband UAV-to-UAV channel model for LAE; closed-form STF-CF/SD-PSD/PSDS plus gradient log-det antenna-position optimization (IEEE TWC). *(Channel-model anchor, not MEC offloading.)*
- [[lu-2026-uav-swarm-two-level-ma]] - Lu et al. 2026. UAV-swarm two-level movable-antenna system for LAE uplink communication; jointly optimizes swarm placement, local antenna positions, and receive beamforming (IEEE TWC). *(Physical-layer LAE anchor, not MEC offloading.)*
- [[jeon-2026-ampli-flection-aerial-backhaul]] - Jeon & Chae 2026. Aerial active-RIS backhaul for UAV-BSs with full 3-D coverage; optimizes platform placement, array partitioning, phase, and amplification for energy efficiency (IEEE TWC).
- [[bai-adaptive-near-field-xl-mimo-multi-uav]] - Bai et al. Adaptive near-field channel modeling for 6G XL-MIMO UPA-to-multi-UAV cooperative communications; selective near-field area pruning keeps spherical-wave accuracy while reducing channel-computation load. *(Parsed metadata lacks DOI/venue/year.)*

### Architectural / spectrum / governance

- [[fan-2026-directional-neighbor-discovery]] - Fan et al. 2026. Synchronous/asynchronous directional FANET neighbor discovery optimized by power-delay surrogates, GP, and CCP with chamber validation (IEEE TMC).

- [[guo-2026-event-triggered-sinr-navigation]] - Guo et al. 2026. UT-Grid refreshes local/global SINR maps when MC-dropout uncertainty crosses a threshold, while Top-1 MoE-D3QN plans a cellular-UAV path under outage, update-traffic, and inference-cost tradeoffs (IEEE TMC).

- [[chen-2026-cargo-uav-pickup-lae]] - Chen et al. 2026. Cellular-connected cargo-UAV pickup in the low-altitude economy; CACMO combines D3QN trajectory learning, simulated annealing sequence planning, and collision-aware refinement (IEEE TMC).
- [[cao-2026-radio-map-cargo-pickup]] - Cao et al. 2026. Radio-map-aided cargo pickup; expected-SNR-grid A* paths feed PSO trip allocation and payload-dependent speed selection for propulsion-energy minimization (IEEE T-ITS).
- [[lee-2026-uav-delivery-time-energy]] - Lee & Chae 2026. UAV-enabled parcel pickup/drop-off with payload-weight, no-fly-zone, 3-D trajectory, and variable-slot optimization; SCA+PCCP exposes a completion-time vs propulsion-energy tradeoff (IEEE T-ITS).
- [[jiang-2026-bi-level-uav-delivery-safety]] - Jiang et al. 2026. Bi-level urban low-altitude UAV delivery with TC-NSGA-III assignment and RG-FMT* trajectory planning under target-level-of-safety risk constraints. *(DOI 10.1109/TITS.2026.3660878; venue not in parse.)*
- [[gao-2026-air-ground-instant-delivery]] - Gao et al. 2026. Cooperative UAV-taxi instant delivery with delivery-gap station placement, demand-driven UAV repositioning, courier-preference transfer, and generalized parcel assignment on Shanghai traces (IEEE TMC).
- [[deng-2026-uav-cpn-energy]] - Deng et al. 2026. UAV-enabled Computing Power Network; stochastic-geometry task-completion probability and altitude/power optimization under fuel and battery constraints (IEEE TMC).
- [[pham-2026-vnf-control-loop]] - Pham & Nguyen 2026. UAV-aided emergency-network VNF orchestration; slot-level MADDPG multipath routing feeds event-triggered BSUM VNF replication and placement (IEEE TMC).
- [[zhang-2026-uav-task-path-lu-its]] — Zhang et al. 2026. Cooperative task allocation and collision-free path planning for multi-UAV low-altitude urban intelligent transportation systems; ILLA potential-game allocation + CBMBA A-Star path search (IEEE T-ITS).
- [[zang-2026-uav-ev-priority-cav-speed]] - Zang et al. 2026. UAV-assisted emergency-vehicle priority on expressways; rolling SROC uses dual-layer PSO to coordinate CAV speed under uncertain human lane changes (IEEE T-ITS).
- [[wang-2025-uav-swarm-stackelberg]] — Wang et al. 2025. Stackelberg-game spectrum sharing for U2U/U2B in UAV swarms.
- [[zhao-2026-temporal-spectrum-cartography]] - Zhao et al. 2026. Temporal spectrum cartography for LAE networks with sparse static/mobile sensing, RecMAE reconstruction, and multi-agent diffusion-policy UAV sensor placement (IEEE TMC).
- [[wang-2026-bayesian-uav-spectrum-mapping]] - Wang et al. 2026. Bayesian 3-D spectrum mapping with 3DIG-RRT* information-driven UAV sampling and SBDL-GP recovery over a measured 117 m x 97 m radio map. *(DOI 10.1109/TWC.2026.3694148; venue not in parse.)*
- [[prabhath-not-in-parse-3d-space-spectrum-utilization]] - Prabhath & Jayaweera. Three-dimensional UAV cellular spectrum-utilization analysis with truncated-octahedron frequency reuse, blocking probability, and channel-shadowing sensitivity. *(Parsed metadata lacks DOI/venue/year.)*
- [[wang-2025-lae-network-survey]] – Wang et al. 2025. Survey: low-altitude economy network architecture, integrated technologies, and future directions.
- [[belgiovine-not-in-parse-multidt-abs-deployment]] - Belgiovine et al. Multi-digital-twin airborne-BS deployment; Sionna optimizes ABS placement/orientation/power while AODT validates mobile-UE scenarios and coverage-drop recovery. *(Parsed metadata lacks DOI/venue/year.)*
- [[jiang-2025-isac-lae-overview]] – Jiang et al. 2025. ISAC for LAE – IAGN architecture, MBCM channel model, stochastic-geometry analysis.
- [[wu-2026-service-oriented-segmented-trajectory]] - Wu et al. 2026. Service-oriented segmented trajectories for high-rise low-altitude UAV-MEC; VSRL-LKH plus TRA/SOS-TRA for latency, energy, and smart-window trajectory privacy (IEEE TMC).
- [[hsu-2025-drl-hues-hap-noma]] — Hsu et al. 2025. **HAP** transmission + RF energy harvesting in NOMA SAGINs; PPO-based DRL-HUES.
- [[wu-2024-satellite-maritime-spectrum-sharing]] — Wu et al. 2024. **VDES satellite-maritime spectrum sharing** (VDE-SAT + VDE-TER co-frequency under ITU uplink/downlink interference constraints); satellite-centralized allocation maximizing combined throughput with task-priority weighting; partial observability → **POMDP** solved with **SCA-D3QN** (Double + Dueling DQN), offline-train/online-deploy (IEEE TVT). *(Satellite-maritime spectrum/comms, not MEC offloading.)*

### CMOP / evolutionary UAV-MEC (Peng/Huang lineage)

- [[peng-2022-cmop-uav-path-planning]] — Peng et al. 2022. **Lineage seed** — CMOP for UAV path planning + offloading; infeasibility-utilization CMOEA.
- [[peng-2024-energy-time-uav-its]] — Peng et al. 2024. UAV-ITS energy + completion-time-difference; CMOEA/D-CDP + repair + service caching.
- [[peng-2026-demand-aware-multiuav-mec]] — Demand-aware multi-area fleet allocation; joint deployment, association, bandwidth, and CPU allocation with constraint-guided solution reconstruction (IEEE TMC).
- [[huang-2023-mu-aec-task-energy]] — Huang et al. 2023. Multi-UAV interdependent (DAG) tasks; makespan + energy balancing; CMOEA + local search.
- [[huang-2025-cmop-dispersed-computing]] — Huang et al. 2025. Dispersed computing with task-redundancy reliability; dual-population CMOEA.
- [[wu-2026-terrain-aware-uav-mec]] — Wu et al. 2026. Urban UAV-MEC with terrain-aware channel + B-spline trajectory; multi-tasking CMOEA.

### Energy efficiency & WPT

- [[chen-2026-laser-powered-multiuav-qoe]] - Chen and Jiang 2026. Laser-powered UAV access points combine rematching, placement, and redundant power/backhaul reallocation to maximize QoE-qualified users (IEEE TMC).
- [[peng-2023-dual-domain-eh-ris]] - Peng & Wang 2023. UAV-mounted RIS combines time splitting with element-level reflection/harvesting; SD3 controls harvesting time, power, scheduling, and phases under QoS constraints (IEEE TWC).
- [[zhang-2022-solar-charging-uav-iot]] - Zhang et al. 2022. Action-confined Q-learning and SARSA route one solar-powered UAV among charging stations and serving points under battery, downlink-data, and Jain-fairness rewards (IEEE TMC).
- [[xie-2023-wireless-powered-short-packet-uav]] - Xie et al. 2023. Static UAV hybrid access point with downlink WPT and TDMA finite-blocklength uploads; alternating SCA/fractional updates solve a continuous relaxation before heuristic integer-symbol rounding (IEEE TGCN).
- [[lin-2026-uav-wpucn-time-allocation]] - Lin et al. 2026. Hybrid HAP/UAV energy delivery and convex phase-time allocation for soil-attenuated wireless-powered underground data collection (IEEE TGCN).
- [[xie-2021-uav-wpt-tutorial]] - Xie et al. 2021. Tutorial on UAV-enabled WPT, WPCNs, and wireless-powered MEC through multi-location hovering, hover-and-fly, and time-quantized trajectory design (IEEE TGCN).
- [[liu-2021-edivert-mobile-crowdsensing]] - Liu et al. 2021. e-Divert energy-efficient unmanned-vehicle crowdsensing with charging stations, CNN/LSTM CTDE control, Ape-X actors, and distributed prioritized replay (IEEE TMC).
- [[he-2026-memdrl-uav-navigation]] - He et al. 2026. MEMDRL multi-UAV navigation for cooperative sensing and upload; MATD3 combines BeBold exploration, ConvLSTM histories, and multi-agent prioritized replay on Shenzhen and Beijing map layouts (IEEE TMC).
- [[dong-2026-digital-tides-provisioning]] - Dong et al. 2026. Fluid-dynamic logistics-UAV workload modeling and information-flux-triggered activation of sleeping ground MEC infrastructure under setup latency (IEEE TMC).
- [[wang-2026-wutf-fair-communication]] - Wang et al. 2026. Wireless-powered multi-UAV fair communication; WUTF combines CNN-GRU actors, a centralized critic, and sequential PPO-style updates for trajectory, Jain fairness, and propulsion/communication efficiency (IEEE TMC).
- [[wang-2026-glint-aoi-wireless-powered-edge]] - Wang et al. 2026. Wireless-powered multi-UAV AoI control; GLINT sequentially resolves 3-D mobility/association and WPT-time/transmission scheduling through local critics plus monotonic value mixing (IEEE TMC).
- [[wu-2026-parallel-cooperative-charging]] - Wu et al. 2026. Shared-cost RF charging across provider stations and unequal-power parallel facilities; CSAU combines uniform-machine approximation with greedy set cover and derives a gamma(ln n + 1) bound (IEEE TMC).
- [[zhao-2026-adaptive-wdc-wet-lae]] - Zhao et al. 2026. Adaptive low-altitude WDC/WET service balancing; MA2HDRL learns reward preference for AoI/HoE tradeoff while coordinating UAV trajectories, WET slots, and WDC subslots (IEEE TMC).
- [[shi-2025-aoi-energy-replenishment-multiuav]] - Shi et al. 2025. AoI-aware multi-UAV IoT data collection and wireless energy replenishment; Dec-POMDP with VDN/QMIX CTDE policies over flight, SN/CS association, and charging decisions (IEEE TGCN).
- [[zhu-2025-lycnn-drl-wpt-mec]] — Zhu et al. 2025. Lyapunov-guided DRL for WPT-MEC.
- [[chen-2025-swipt-mec-sac]] — Chen et al. 2025. SWIPT-MEC with directional-antenna UAV; improved SAC (SAC-SK), bi-objective energy.
- [[panahi-2026-uav-green-iot-offloading]] — Panahi & Panahi 2026. Cost-aware UAV-enabled green-IoT computation offloading; Q-learning region trajectory plus laser / renewable energy procurement and COF/WPT service-compensation accounting (IEEE TGCN).
- [[mohammadi-2026-star-ris-uav-mec-noma]] — Mohammadi et al. 2026. STAR-RIS-assisted UAV-MEC with NOMA; weighted energy minimization over task-bit allocation, transmit power, STAR-RIS phases, and UAV trajectory via BCD/SCA/MRT-style updates (IEEE TGCN).
- [[xiao-2025-star-ris-bidirectional-uav-mec]] — Xiao et al. 2025. STAR-RIS-enhanced UAV-MEC with same-slot bidirectional offloading to BS-MEC and UAV-MEC servers; EE maximization over scheduling, resource allocation, STAR-RIS beamforming, and trajectory via Dinkelbach/SCA BCD (IEEE TWC).
- [[zhou-2018-uav-wireless-powered-mec]] — Zhou et al. 2018. **Computation-rate maximization** in UAV-enabled wireless-powered MEC; partial + binary offloading; two-/three-stage closed-form optimization (JSAC).
- [[he-2024-backscatter-wpmec-cooperation]] — He et al. 2024. **Backscatter-assisted wireless-powered MEC with user cooperation** (source node + helper-relay + HAP-with-MEC); integrated **BackCom + active comm**; **user energy-efficiency** maximization via Dinkelbach fractional programming + convex transform to semi-closed-form solutions (IEEE TMC).
- [[li-2024-irs-secure-wpmec]] — Li et al. 2024. **IRS-assisted secure wireless-powered MEC** with a passive eavesdropper; harvest-then-offload (TDMA) + partial offloading; **sum secure computation task bits** maximization over AP energy beamforming + IRS phase shifts (WPT + offload) + power + time + local frequency; non-convex → 3 subproblems via Taylor expansion + SDR + Lagrange-duality/KKT, iterative AO; >45% secure-bits gain at max AP power (IEEE TMC).
- [[xu-2018-uav-wpt-trajectory]] — Xu et al. 2018. Foundational **UAV-enabled WPT**: trajectory design + energy optimization; sum-energy optimum is **single-location hovering** (near-far fairness issue), max-min (min-energy) optimum is **multi-location hovering** → **successive hover-and-fly** + SCP under a max-speed constraint (IEEE TWC).
- [[wang-2025-airground-laser-mec]] — Wang et al. 2025. **Air-ground coordinated MEC** with a **laser-powered** rotary-wing UAV: a grid-powered ground AP both laser-charges the UAV and serves as a compute server, while the UAV is simultaneously MEC server + relay; minimizes long-term average **UAV energy** by decomposing into an **LP** task/EH-time allocation stage + a **DDPG** trajectory stage (**LP-DDPG**) (IEEE TVT).
- [[pan-2025-uav-ris-energy-efficient-comm]] — Pan et al. 2025. **Cooperative multiple UAV-mounted RISs** serving multiple ground users when direct BS→GU links are blocked; three-objective **EEComm-MOF** (max-min rate / max total rate / min total energy) jointly over BS beamforming + UAV-RIS 3D locations + **discrete** phase shifts, solved by **INSGA-II-CDC** (NSGA-II + continuous/discrete/complex mechanisms) returning a Pareto set in one run (IEEE TMC).

> [[liu-2020-wpt-cooperative-uav-mec]] (UAV-enabled wireless-powered cooperative MEC; SCA + DAI) also targets WPT energy minimization; it is filed under **Classical / convex / optimization-based UAV-MEC** above as its primary home.
> [[wu-2025-iopo-irs-uav-thz-mec]] (IRS-assisted THz energy optimization) also targets energy efficiency; it is filed under **IRS / THz / anti-jamming** above as its primary home.

### MEC / MCC fundamentals & edge offloading theory

- [[zhang-2013-energy-optimal-mcc-stochastic]] — Zhang et al. 2013. **Energy-optimal mobile cloud computing** under a stochastic (Gilbert-Elliott) channel; mobile vs cloud execution with DVS CPU-frequency / transmission-rate scheduling; closed-form policies + a **threshold policy** on data consumption rate $L/T$ (IEEE TWC).
- [[mao-2016-lodco-eh-mec-offloading]] — Mao et al. 2016. **Green MEC with energy-harvesting devices**; execution-cost (delay + task failure) minimization via the **LODCO** Lyapunov online algorithm deciding offloading + DVFS CPU frequency + transmit power from current state only; asymptotically optimal (IEEE JSAC).
- [[you-2017-meco-resource-allocation]] — You et al. 2017. **Multiuser MECO resource allocation** (TDMA + OFDMA); min weighted-sum mobile energy under a latency constraint; the optimal TDMA policy is **threshold-based** on a derived **offloading priority function** (complete vs minimum offloading), extended to a finite-capacity cloud + a low-complexity OFDMA scheme (IEEE TWC).
- [[miettinen-2010-mcc-energy-efficiency]] — Miettinen & Nurminen 2010. Foundational **mobile-cloud-computing energy** measurement/analysis: offloading saves energy only when $E_{cloud}<E_{local}$, governed by the **computing-to-communication ratio**; WLAN-vs-3G + traffic-pattern sensitivity (USENIX HotCloud '10). *(Corpus's earliest anchor; measurement study, no DOI.)*
- [[wang-2016-partial-offloading-dvs]] — Wang et al. 2016. **Partial computation offloading using dynamic voltage scaling (DVS)**; jointly optimizes SMD computational speed + transmit power + offloading ratio for **energy minimization (ECM)** and **latency minimization (LM)**; ECM recast convex via variable substitution → closed-form **EPCO**, LM via univariate search; multi-cloud extension in closed form; proves **total offloading is never optimal under DVS** (IEEE TCOM).
- [[yang-2024-taco-human-digital-twin-edge]] — Yang et al. 2024. **Human digital twin** deployment at the edge under an end-edge-cloud framework; two-timescale accuracy-aware online optimization (**TACO**) jointly placing/updating virtual twins + task offloading + access selection; improved Lyapunov + piecewise McCormick envelopes + BCD (IEEE TMC).
- [[shi-2023-two-timescale-migration-rerouting]] — Shi et al. 2023. **Service migration vs task rerouting** for MEC handovers; **two-timescale** online optimization — slow access-selection + migration/rerouting, fast computing/communication resource allocation — minimizing long-term average service delay; improved **Lyapunov** + randomized rounding (JASTO) + Lagrange-dual (OASTR), asymptotically optimal (IEEE TWC).
- [[li-2024-smdrl-resource-constrained-mec]] — Li et al. 2024. **Computation offloading in resource-constrained multi-access MEC** where the shared wireless medium is **bandwidth-limited**; **Scheduled Multi-agent DRL (SMDRL)** learns message encoding + action selection + self-scheduling with a **TopK** broadcast limit, and a **virtual energy-deficit queue** turns a long-term per-device energy cap into a per-slot **QoE-maximization** MDP; near-optimal QoE under communication + energy constraints (IEEE TMC).
- [[yang-2025-generalizable-pareto-offloading]] — Yang et al. 2025. **Generalizable Pareto-optimal MEC offloading**; context-conditioned Discrete-SAC learns one policy across delay/energy preference weights, edge-server counts, and CPU-frequency profiles (IEEE TSC).

### UAV communications & deployment foundations

- [[zhang-2021-safe-dqn-emergency]] - Zhang et al. 2021. Lyapunov-filtered Safe-DQN controls an emergency UAV trajectory under a conservative user-energy surrogate and next-grid-point obstacle checks (IEEE TGCN).
- [[challita-2019-cellular-uav-interference-drl]] - Challita et al. 2019. Distributed deep echo-state-network RL jointly controls cellular-UAV grid paths, serving cells, and powers in a dynamic noncooperative game; its SPNE result is conditional on training convergence (IEEE TWC).

- [[xie-2026-geoagg-hsac]] - Xie et al. 2026. Mountainous integrated localization and communication with terrain-occlusion-aware graph aggregation and hybrid SAC control of UAV trajectories, user association, and resource allocation (IEEE TWC).
- [[liu-2026-uav-hsr-jitter]] - Liu et al. 2026. Gaussian-random-walk UAV jitter analysis for CA/DA high-speed-rail mmWave links, with outage/rate expressions and codebook-aware adaptive beamwidth (IEEE T-ITS).
- [[zhang-2019-fast-uav-deployment]] - Zhang & Duan 2019. Fast heterogeneous-UAV coverage deployment under min-max and min-sum travel delay, with exact, FPTAS, bounded-greedy, and pseudo-polynomial algorithms (IEEE TMC).
- [[zhu-2026-fixed-wing-fd-af-wind]] - Zhu et al. 2026. Constant-wind fixed-wing full-duplex AF relaying; wind-triangle case analysis jointly selects air speed and flight time, then derives pitch/crab compensation (IEEE TGCN).
- [[wang-2026-robust-multiuav-jtcra]] - Wang et al. 2026. Energy-depletion-aware A2G service continuity; parameter-shared MAPPO/QMIX jointly control multi-UAV trajectories, power, and bandwidth under a Jain-fairness requirement (IEEE TWC).
- [[chen-2026-traffic-aware-asynchronous-control]] - Chen et al. 2026. Spatial/traffic graph-attention clustering plus GNN-GRU PPO for asynchronous multi-UAV collection, relaying, delivery, and trajectory control (IEEE TMC).
- [[yin-2026-m2llm-trajectory-beamforming]] - Yin et al. 2026. LoRA-tuned multimodal LLaVA predicts mobile-user trajectories and supplies a fixed-dimensional state to DDPG for joint UAV motion and beamforming (IEEE TWC).
- [[zeng-2018-uav-multicasting-completion-time]] - Zeng et al. 2018. RLNC multicast completion-time minimization through conservative connection-duration constraints, virtual-base-station waypoints, and fixed-path LP speed allocation (IEEE TWC).
- [[liu-2020-distributed-uav-coverage-navigation]] - Liu et al. 2020. Distributed actor-critic navigation for long-term multi-UAV communication coverage, Jain geographic fairness, movement-energy efficiency, and peer-connectivity constraints (IEEE TMC).
- [[fu-2026-dubins-uav-data-collection]] - Fu et al. 2026. Carrier/subordinate heterogeneous-UAV data collection with release, obstacle-aware Dubins tours, and synchronized airborne recovery (IEEE T-ITS).
- [[wang-2026-multimodal-uav-coverage-backhaul]] - Wang, Farooq, and Chen 2026. Distributed multi-modal UAV access control that switches among cluster exploration, local service, and minimum-spanning-tree bridge roles for coverage and resilient backhaul (IEEE TMC).
- [[zhang-2026-distributed-jscc-uav-video]] - Zhang et al. 2026. Distributed video DeepJSCC for UAV networks; lightweight onboard encoders, receiver-side decoding, and DQN-controlled direct or amplify-and-forward relay transmission trade video quality against network lifetime (IEEE TMC).
- [[vitale-2026-density-aware-4d-trajectory]] - Vitale et al. 2026. Density-aware urban UAV traffic planning with reverse-time cube/slot reservations and distributed robust MPC under probabilistic separation and arrival-time QoS constraints (IEEE T-ITS).
- [[zhang-2026-omnidirectional-monitoring-deployment]] - Zhang et al. 2026. Joint UAV and fixed-camera deployment for continuous omnidirectional monitoring, with strategy-space reduction, obstacle-aware path planning, approximation guarantees, simulation, and a ten-UAV field test (IEEE TMC).
- [[li-2023-energy-constrained-uav-data-collection]] - Li et al. 2023. Energy-constrained UAV collection as a depot-returning full/partial orienteering problem, with an ILP, no-overlap approximation algorithms, and overlap-aware marginal-gain heuristics (IEEE TMC).
- [[liu-2026-usp-nfrp-emergency-communication]] - Liu et al. 2026. Persistent emergency UAV swarm service with periodic replacement paths, dynamic tree backhaul repair, and max-min ant-system planning to minimize required fleet size (IEEE TGCN).
- [[li-2026-dff-slam]] - Li et al. 2026. DFF-SLAM combines YOLOv3, multiscale optical flow, and epipolar filtering for GPS-suppressed UAV positioning, with TUM RGB-D accuracy tests and 16-FPS Jetson Xavier NX platform execution (IEEE TMC).
- [[fan-2026-hap-uav-iort-oee]] - Fan et al. 2026. HAP-UAV IoRT collection with overall energy efficiency, joint aerial trajectories, HAP selection, UAV power, bandwidth allocation, meteorological fading, and Dinkelbach/BCD/SCA optimization (IEEE TMC).
- [[chen-not-in-parse-uav-human-medical-delivery]] - Chen et al. Cooperative emergency medical pickup-delivery scheduling with UAVs and human couriers; an attention-based cooperative DRL policy uses type-specific decoders, feasibility masks, and a vehicle coordinator. *(Parsed metadata lacks DOI/venue/year.)*
- [[yang-2025-hcdrl-pursuit-evasion]] - Yang et al. 2025. Hierarchical cooperative DRL for multi-UAV pursuit-evasion; a meta-policy selects five encirclement subtasks and CTDE lower policies control collision-aware maneuvers (IEEE GC Wkshps).
- [[zhang-2022-uav-relay-substitution]] - Zhang et al. 2022. HUS/SEUS UAV substitution relaying extends service beyond one relay's flight duration and co-optimizes relay trajectories and source/relay powers (IEEE TGCN).
- [[zhang-2019-secure-uav-trajectory-power]] - Zhang et al. 2019. Joint trajectory and temporal power control for average secrecy-rate maximization in UAV-to-ground and ground-to-UAV links (IEEE TWC).
- [[le-2026-asynchronous-uav-data-collection]] - Le et al. 2026. Asynchronous-QMIX remote data collection with Dec-POSMDP event timing, range-limited map exchange, recurrent value decomposition, and local imperfect-CSI bandwidth optimization (IEEE TWC).
- [[zhang-not-in-parse-cellular-uav-to-x]] - Zhang et al. Cellular UAV-to-X communication with cooperative UAV-to-network and UAV-to-UAV sense-and-send operation; ISASOA combines LP, branch-and-bound, and convex speed control. *(Parsed metadata lacks DOI/venue/year.)*
- [[bai-2026-multimodal-uav-vehicle-channel]] - Bai et al. 2026. LiDAR-aided multi-modal intelligent channel model for multi-UAV-to-multi-vehicle links; MUMV-CSCI dataset, TTD/ATD density parameters, and TSF-CF/TSI/DPSD statistics (IEEE TWC).
- [[hussain-2026-unet-uav-mmwave-pathloss]] - Hussain 2026. Multi-scale U-Net pathloss prediction for UAV-assisted mmWave networks using log-distance, LoS-mask, and building-mask inputs plus vectorized LoS preprocessing (IEEE TWC).
- [[zhang-2026-control-assisted-beam-tracking]] - Zhang et al. 2026. Control-assisted BS-UAV mmWave beam prediction using PID flight state, a Bayesian DNN, and a kinematic estimator, evaluated in Gazebo and with real F450 flight data (IEEE TWC).
- [[huang-2026-aim-uav-relay-aor]] - Huang et al. 2026. AIM angle-of-radiation-aware UAV relay-chain deployment; joint 3-D position and heading search minimizes relay count under per-link RSS thresholds and maintains 100% success in the parsed terrain/RSS tests (IEEE TMC).
- [[bujari-2018-stateless-fanet-routing]] - Bujari et al. 2018. Comparative study of stateless geographic FANET routing; progress, randomized, face/projection, hybrid, and restricted-flooding protocols are evaluated for delivery, path dilation, traffic, and scalability in 3-D UAV ad hoc networks (IEEE TMC).
- [[fatemidokht-2021-vru-vanet-routing]] - Fatemidokht et al. 2021. Trust-filtered vehicle/UAV routing for urban VANETs; road-network paths use UAV connectivity estimates, while an ant-colony aerial fallback handles sparse connectivity (IEEE T-ITS).
- [[song-2026-albpd-directional-fanet]] - Song et al. 2026. ALBP-D directional FANET link maintenance; breakage-probability prediction separates distance and angular failures, then adjusts beamwidth/range for longer UAV-to-UAV link lifetime (IEEE TWC).
- [[deng-2026-eret-fanet-routing]] - Deng et al. 2026. eRET adaptive FANET routing evolves route expiration time so UAV swarms shift between host-centric route reuse and content-centric discovery (IEEE TMC).
- [[zheng-2026-active-search-low-altitude-uav]] - Zheng & Chen 2026. Active low-altitude UAV sensing/communication search under unknown user locations and unknown blockage; equipotential-surface search plus online LoS channel estimation (IEEE TMC).
- [[ebrahimi-not-in-parse-autonomous-uav-localization-rl]] - Ebrahimi et al. Autonomous UAV trajectory for RSSI-based ground-object localization; Q-learning waypoint control reduces multilateration error under energy, path-length, waypoint, and time budgets. *(Parsed metadata lacks DOI/venue/year.)*
- [[heo-not-in-parse-blockage-aided-multiuav-interference]] - Heo et al. Building-blockage-aided multi-UAV interference coordination; SCA/PCCP/BCD trajectory-resource control keeps desired links LoS while pushing interfering links behind buildings. *(Parsed metadata lacks DOI/venue/year.)*
- [[zhang-2026-fuzzy-observer-harbor-approach]] - Zhang et al. 2026. Surface-air vehicle harbor-approach control with time-varying guidance and an adaptive event-triggered fuzzy state observer (IEEE T-ITS).
- [[li-2026-aerial-ris-trajectory-phase]] - Li et al. 2026. Aerial RIS-enhanced communications with tilt-aware UAV-mounted RIS control; SAC-PER jointly controls Euler angles, RIS phase shifts, and trajectory/energy while ZF/water-filling handles BS beamforming (IEEE TWC).
- [[li-2026-aeroguard-uav-fault-detection]] - Li et al. 2026. AeroGuard real-time UAV flight-data fault detection; residual-driven LSTM/ARX fusion plus Z-score/SPRT tests on attitude streams, with Raspberry Pi and real-flight evaluation (IEEE TMC).
- [[gao-2023-uav-mcs-uma]] - Gao et al. 2023. UMA UAV-assisted mobile crowd sensing; combines participant incentives, quality prediction, UAV coverage, sensor calibration, and MADDPG scheduling (IEEE TMC).
- [[gong-2026-uav-3d-visual-coverage]] - Gong et al. 2026. Path-aware 3-D object visual coverage with a single UAV; viewpoint generation plus energy-aware B-spline trajectory optimization (IEEE TMC).
- [[zhu-2026-fas-uav-fbl]] - Zhu et al. 2026. Fluid-antenna-assisted finite-blocklength UAV relaying with correlated-port diversity, rural/urban BLER analysis, and probing-aware energy-efficiency optimization (IEEE TWC).
- [[meng-2026-fullspace-star-ris-secure]] - Meng & Wu 2026. Full-space STAR-RIS UAV trajectory and role switching for robust secure NOMA uplink under colluding-eavesdropper CSI uncertainty (IEEE TGCN).
- [[zhou-2026-gl-ahg-coverage-planning]] - Zhou et al. 2026. Game-learning weighted waypoint selection and alternating hierarchical genetic route optimization for energy-aware terrain coverage (IEEE TMC).
- [[guang-2026-hiswta-mcs]] - Guang et al. 2026. Dynamic UAV clustering, inter-head information routing, fuzzy self-healing, and approximate Shapley task allocation for mobile crowdsensing (IEEE TMC).
- [[ma-2026-game-ibs-deployment]] - Ma et al. 2026. Claimed exact-potential-game anti-UAV interference-base-station placement evaluated through exhaustive deployment search and SAC UAV path responses (IEEE TWC).
- [[zeng-2017-energy-efficient-uav-trajectory]] — Zeng & Zhang 2017. **Energy-efficient UAV communication** via trajectory optimization; first **fixed-wing propulsion-energy model** (speed + acceleration) + bits/Joule energy-efficiency; circular + generally-constrained SCA trajectories (IEEE TWC). *(UAV-communications anchor, not MEC.)*
- [[zeng-2016-throughput-relaying]] — Zeng et al. 2016. **UAV mobile relaying** throughput maximization; joint relay trajectory + source/relay power; "staircase" water-filling power structure + SCA trajectory under **information-causality** (IEEE TCOMM). *(UAV mobile-relaying anchor, not MEC.)*
- [[li-2016-energy-balanced-uav-relaying]] - Li et al. 2016. Energy-balanced cooperative UAV relaying; exact min-max scheduling and EPLA assign packets and modulation levels, with forwarding power derived from the selected rate and channel, without modeling propulsion energy (IEEE TMC).
- [[zhao-2019-uav-emergency-disasters]] — Zhao et al. 2019. **UAV-assisted emergency networks** in disasters (magazine framework): joint trajectory+scheduling with surviving BSs, multihop D2D coverage extension, and multihop UAV relaying (AF/DF) — IEEE Wireless Communications. *(Post-disaster comms framework, not a single MEC formulation.)*
- [[tian-2026-joint-localization-communication]] - Tian et al. 2026. Air-ground emergency-network localization and communication; AOA/ESPRIT localization feeds CoMP beamforming and DDQN control of UAV movement, time, and power (IEEE TWC).
- [[bor-yaliniz-2016-3d-abs-placement]] – Bor-Yaliniz et al. 2016. First **3-D placement** of a drone-cell (aerial base station): jointly choose altitude + coverage location/size to maximize covered users; quadratically-constrained MINLP via bisection + interior-point solver (IEEE ICC). *(Aerial-base-station deployment anchor, not MEC.)*
- [[mozaffari-not-in-parse-3d-drone-cellular-network]] - Mozaffari et al. Foundational 3-D wireless cellular network with LAP drone-BSs, drone-UEs, HAP/FSO backhaul, truncated-octahedron frequency reuse, KDE demand modeling, and optimal-transport association. *(Parsed metadata lacks DOI/venue/year.)*
- [[li-2026-uav-bs-semantic-mfmaddpg-kde]] - Li et al. 2026. Semantic-communication UAV-BS 3-D deployment; MF-MADDPG-KDE models continuous neighboring actions and optimizes BLEU-derived semantic fidelity under SINR/interference constraints (IEEE TWC).
- [[you-2019-rician-uav-data-harvesting]] - You & Zhang 2019. UAV-enabled WSN data harvesting under angle-dependent Rician fading; outage-aware effective fading power regression plus BCD/SCA scheduling and 3-D trajectory optimization (IEEE TWC).
- [[jiang-2012-uav-heading-sdma]] — Jiang & Swindlehurst 2012. Multi-antenna fixed-wing UAV heading optimization for ground-to-air **SDMA** uplink; adaptive heading maximizes ergodic sum rate via prediction filter + line search; SDMA >> TDMA (IEEE JSAC). *(Multi-antenna UAV relay / heading-optimization anchor.)*
- [[lyu-2017-spiral-mbs-placement]] — Lyu et al. 2017. **Minimum-count UAV-MBS placement** as the NP-hard **Geometric Disk Cover** problem; a polynomial-time **spiral** algorithm places base stations along the convex-hull perimeter of uncovered ground terminals and nudges inward; near core-sets-optimal on small instances, beats strip-based/K-means/random (IEEE COMML). *(Aerial-base-station deployment anchor, not MEC.)*
- [[zeng-2016-uav-comm-opportunities-challenges]] — Zeng et al. 2016. **Magazine overview** of UAV-aided wireless communications: networking architecture, air-to-ground LoS channel characteristics, three use cases (ubiquitous coverage / relaying / data collection), and design challenges (CNPC links, dynamic topology, SWAP constraints, interference coordination) (IEEE Communications Magazine). *(Foundational UAV-comms overview, not MEC.)*
- [[zhan-2011-uav-relay-heading-optimization]] — Zhan et al. 2011. **Earliest UAV-comms source** — multi-UAV relays connect ground APs to a BTS on the uplink; defines the **ergodic normalized transmission rate (ENTR)**, approximates it as a **sinusoid** in UAV heading → closed-form optimal heading, plus an adaptive **handoff** algorithm + new-relay deployment for the mobile topology (IEEE TAES). *(UAV mobile-relaying / heading-control anchor, not MEC.)*
- [[mozaffari-2016-uav-underlaid-d2d]] — Mozaffari et al. 2016. UAV downlink base station **coexisting with an underlaid D2D network**; **stochastic-geometry** coverage / sum-rate analysis for static + mobile UAV; optimal altitude (decreasing in D2D density), **disk-covering** minimum stop-points for full coverage, and the **coverage-vs-delay / D2D-outage** tradeoff (IEEE TWC). *(Aerial-base-station + D2D coexistence anchor, not MEC.)*
- [[azari-2020-uav-to-uav-cellular]] - Azari et al. 2020. Stochastic-geometry analysis of direct U2U pairs sharing cellular uplink spectrum, comparing concurrent reuse with orthogonal bandwidth partition and fractional power control (IEEE TWC).
- [[mozaffari-2019-drone-antenna-array]] — Mozaffari et al. 2019. **Drone-based antenna array** that beam-steers by **physically repositioning** the drones; minimum-**service-time** design = transmission time (perturbation-theory drone-spacing directivity max) + control time (**bang-bang** closed-form minimum control time under wind/gravity); +32% spectral efficiency vs fixed uniform array (IEEE TCOMM). *(UAV-communications / aerial-beamforming anchor, not MEC.)*

- [[zhao-2026-uav-irs-data-collection]] - Zhao et al. 2026. Transmission-prioritized UAV-mounted IRS sensor collection with CJ-BS element-count search, SCA hover placement, and GA visit ordering (IEEE TGCN).
- [[guo-2026-uav-wsn-completion-time]] - Guo et al. 2026. Wireless-powered WSN completion-time minimization with energy-based clustering, GA/B-spline path design, and fly-while-communication velocity control (IEEE TGCN).
- [[lv-2026-isac-sar-tlsp]] - Lv et al. 2026. Bistatic UAV-ISAC SAR mission optimization using inner SQP and outer constrained Bayesian optimization for energy, resolution, and resolution fairness (IEEE TWC).
- [[liu-2025-aoi-iscc-five-stage]] - Liu et al. 2025. Energy-constrained UAV ISCC with radar-estimation-rate/AoI tradeoffs and five-stage alternating scheduling, sensing, power, CPU, and motion control (IEEE TWC).
- [[wang-2026-ikpp-vehicular-uav]] - Wang et al. 2026. IKPP control for multi-UAV vehicular uplinks, combining PPO motion/power/carrier scores with load-constrained nearest-UAV association and action reconstruction (IEEE TWC).

- [[lu-2026-aoi-trajectory-channel]] - Lu et al. 2026. SAC-style multi-agent trajectory and channel control for a transmission-duration freshness proxy under UAV/jammer interference (IEEE TWC).
- [[zhang-2026-irs-uav-covert-fbl]] - Zhang et al. 2026. Finite-blocklength covert UAV transmission with IRS-assisted active/passive beamforming, SCA trajectory design, and lower-complexity PDDGP updates (IEEE TGCN).
- [[ning-2026-uav-isac-secure-beamforming]] - Ning et al. 2026. Robust UAV-ISAC secrecy control combining CRB-derived eavesdropper uncertainty, sensing/jamming beams, scheduling, and 3-D trajectory optimization (IEEE TWC).
- [[wang-2023-drl-irs-uav-trajectory]] - Wang et al. 2023. DQN/DDPG UAV trajectory control with nearest-IRS selection and closed-form passive phase alignment for a moving UE (IEEE TMC).
- [[wen-2026-cooperative-jamming-uav]] - Wen et al. 2026. MADDPG relay/jammer trajectory and power control against a mobile aerial eavesdropper under perfect and imperfect CSI (IEEE TWC).

- [[samir-2021-uav-cell-free-coverage]] - Samir et al. 2021. DDPG dispatch and trajectory control for energy-aware UAV coverage along an infrastructure-unavailable highway (IEEE TMC).
- [[huang-2026-uav-friendly-jamming-transsac]] - Huang et al. 2026. Transformer-enhanced SAC with bandit-selected secrecy/energy weights for UAV jamming in satellite-maritime links (IEEE TMC).
- [[jiang-2026-sensing-assisted-uav-tracking]] - Jiang et al. 2026. EKF-based sensing-assisted predictive beamforming with outage approximation, sensing-time control, and SCA trajectory updates (IEEE TWC).
- [[zhang-2026-msialns-air-ground-inspection]] - Zhang et al. 2026. Adaptive large-neighborhood search for multi-vehicle/multi-UAV inspection with node conflicts and cross-vehicle recovery (IEEE T-ITS).
- [[ammar-2026-oran-maritime-slicing]] - Ammar et al. 2026. A2C/PPO control of O-RAN maritime slicing, VNF deployment, radio/compute resources, and UAV trajectories (IEEE TMC).

- [[betalo-2026-meta-uav-scheduling]] - Betalo et al. 2026. MW-MAD3PG combines MAML-style adaptation, multi-agent deterministic control, and Jain-fairness shaping for UAV-assisted ITS sensor assignment and resources (IEEE TMC).
- [[zhai-2026-uav-ma-secrecy]] - Zhai and Luo 2026. Joint scheduling, beamforming, UAV trajectory, and movable-element positioning for max-min secrecy under bounded eavesdropper-location uncertainty (IEEE TWC).
- [[su-2026-three-tier-uav-capacity]] - Su et al. 2026. NOMA access, multihop UAV relay allocation, and jitter-aware SDMA backhaul capacity for a three-tier emergency wireless network (IEEE TGCN).
- [[wan-2026-movable-antenna-multiuav-mimo]] - Wan et al. 2026. WMMSE and hierarchical group-sparse position selection for macro/micro movable-antenna multi-UAV uplink MIMO (IEEE TWC).
- [[ren-2026-movable-antenna-uav-trajectory]] - Ren et al. 2026. Selective uniform-cost search jointly plans a cellular UAV path, serving BS, MMSE receiver, and onboard movable-array positions (IEEE TWC).

- [[cui-2020-marl-uav-resource-allocation]] - Cui et al. 2020. Independent tabular Q-learning for UAV user, subchannel, and power selection in a non-cooperative stochastic game (IEEE TWC).
- [[wang-2026-mat-target-tracking]] - Wang et al. 2026. TDOA localization, Hungarian formation assignment, and an autoregressive Multi-Agent Transformer for obstacle-aware UAV-swarm target tracking (IEEE T-ITS).
- [[dong-2026-radio-map-d2d-relay]] - Dong et al. 2026. Terrain-derived multi-frequency radio maps guide D2D subnetworks, gateway selection, and rate-weighted UAV-relay deployment (IEEE TWC).
- [[jin-2026-jitter-aware-uav-comp]] - Jin et al. 2026. UAV-jitter channel analysis and J-LSTM next-symbol CSI prediction for distributed multi-UAV CoMP transmission (IEEE TWC).
- [[ye-2023-graph-uav-coverage]] - Ye et al. 2023. FANET graph attention, GRU memory, and maximum-entropy Q-learning coordinate partially observing UAVs for coverage, fairness, and movement energy (IEEE TMC).
- [[samir-2022-aoi-altitude-scheduling]] - Samir et al. 2022. Online PPO alternates two-hop status scheduling and UAV altitude movement to minimize weighted AoI (IEEE TMC).
- [[ding-2026-optimization-driven-spectrum-sharing]] - Ding et al. 2026. Robust SCA/CVX targets guide hybrid DQN-DDPG resource and trajectory control over licensed/unlicensed bands under uncertain jamming (IEEE TMC).
- [[xia-2026-ubt-emergency-response]] - Xia et al. 2026. Learned taxi availability and non-overlapping coverage-gain bus selection coordinate UAV-bus-taxi emergency response (IEEE T-ITS).
- [[dang-2026-uav-fl-energy]] - Dang et al. 2026. Alternating inner approximations jointly control simultaneous FL uploads, local resources, and rotary-wing 3-D placement under mixed A2G propagation and return energy (IEEE TGCN).
- [[kanani-2026-haps-uav-isac]] - Kanani et al. 2026. GA and NSGA-II optimize target-echo power and worst-user SINR in a HAPS-processed multi-UAV ISAC architecture (IEEE TWC).
- [[yu-2026-ris-uav-iab-outage]] - Yu et al. 2026. SCA/SDR alternates UAV heights and rooftop-RIS phases to match access and backhaul rates in urban IAB (IEEE TWC).
- [[tan-2025-sagin-outage-altitude]] - Tan et al. 2025. Energy- and SNR-outage analysis selects altitude for a solar-powered ground-UAV-satellite relay and compares relayed/direct capacity (IEEE TWC).
- [[v-2026-pb-papp-survivor-detection]] - V et al. 2026. Logistic PSL prediction, priority-aware routing, and hierarchical model averaging guide simulated multi-UAV survivor search (IEEE TMC).
- [[alsenwi-2026-ris-uav-energy-efficiency]] - Alsenwi et al. 2026. Cloud-trained, edge-executed actor-critic control jointly selects a UAV-mounted RIS position, quantized phases, and BS precoding for mmWave energy efficiency and rate reliability (IEEE TGCN).
- [[wei-2026-runs-uav-network-slicing]] - Wei et al. 2026. RUNs combines robust reformulation, closed-form altitude elimination, augmented Lagrangian, block-coordinate updates, and knapsack rounding for uncertain UAV network slicing (IEEE TWC).
- [[li-2026-radio-map-predictive-routing]] - Li and Chen 2026. Radio maps and moving-node trajectories parameterize interference-bottleneck routing, hop timing, and power over a dynamic space-time graph (IEEE TWC).
- [[jiang-2026-ray-antenna-array]] - Jiang and Zeng 2026. A switch-selected radial antenna array provides direction-independent angular resolution under stated assumptions for OFDM UAV-swarm ISAC (IEEE TWC).
- [[min-2026-sparse-bistatic-nearfield-isac]] - Min et al. 2026. Sparse XL-MIMO and fourth-order bistatic virtual arrays for near-field angle/range separation and 3-D UAV-swarm localization (IEEE TWC).
- [[theocharides-2026-uav-traffic-estimation]] - Theocharides et al. 2026. Gaussian-process virtual measurements and successive-convexification moving-horizon estimation recover regional road-traffic states from sparse UAV sensing (IEEE T-ITS).
- [[hsu-2022-collision-avoidance-trajectory]] - Hsu and Gau 2022. Convex-TSP routing through heterogeneous communication disks and distributed tabular Q-learning provide data collection and simulated collision avoidance (IEEE TMC).
- [[feng-2026-aerial-ris-secure]] - Feng et al. 2026. Phase-aware relativistic adaptive descent and environment-state interactive attention coordinate aerial-RIS secrecy under phase, CSI, and GPS errors (IEEE TWC).
- [[ge-2026-ra-spma-fanet-mac]] - Ge et al. 2026. Statistical priority, dynamic contention thresholds, and adaptive backoff provide differentiated FANET random access (IEEE TGCN).
- [[meng-2026-star-ris-uav-energy]] - Meng et al. 2026. A fixed STAR-RIS, UAV RF energy supply, and NOMA resource allocation jointly improve simulated system sum-rate (IEEE TWC).
- [[wang-2018-uav-powered-d2d]] - Wang et al. 2018. A single-switch harvest-transmit-store schedule supports D2D communication powered by UAV wireless energy transfer (IEEE TGCN).
- [[zhu-2025-green-isac-q-learning]] - Zhu et al. 2025. Inverse-CRLB anchor geometry initializes independent tabular Q-learners for UAV-swarm sensing and communication resource allocation (IEEE TGCN).
- [[li-2026-full-duplex-noma-uav-relay]] - Li et al. 2026. Bernstein-safe chance constraints guide full-duplex NOMA relay positioning and power control under Gaussian UAV location error (IEEE TWC).
- [[li-2021-robust-ris-uav-secrecy]] - Li et al. 2021. Alternating trajectory, power, and RIS-phase optimization maximizes bidirectional worst-case secrecy under bounded eavesdropper CSI error (IEEE TWC).
- [[qi-2026-ocma-ddqn-data-collection]] - Qi et al. 2026. Potential-game cooperation, distance-conditioned experience sharing, and LSTM outage compensation support simulated multi-UAV data collection under jamming (IEEE TGCN).
- [[huang-2026-slim-eiv-uav-fleet]] - Huang et al. 2026. SLIM+ jointly places edge intelligent vehicles and sizes deadline- and energy-constrained UAV fleets through nested dynamic programming and approximation (IEEE TMC).
- [[kamatchi-2025-slipt-uav-fso]] - Kamatchi et al. 2025. Analytical SLIPT ground-to-UAV FSO reception compares AC-DC separation, time-switching, power-splitting, and hybrid TSPS protocols under Malaga turbulence, pointing error, and field-of-view constraints (IEEE TGCN).
- [[huang-2026-star-ris-nearfield-isac]] - Huang et al. 2026. Semi-passive STAR-RIS sensing and near-field spherical-wave modeling support joint communication beamforming, radar-information optimization, and UAV hover-point design (IEEE TWC).
- [[chakraborty-2026-skyscale-rti-deployment]] - Chakraborty et al. 2026. SKYSCALE reduces radio-tomographic deployment measurements through rank-saturation updates, reusable attenuation maps, and segment-coverage trajectories, with a real WiFi UAV testbed (IEEE TMC).
- [[xu-2026-mrlmn-llm-multihop]] - Xu et al. 2026. MRLMN combines task-oriented UAV grouping, behavioral connectivity loss, and GPT-4o-guided policy distillation for simulated multi-hop emergency networking (IEEE TMC).
- [[kim-2026-scale-reconfigurable-marl]] - Kim et al. 2026. Masked variable-width actors and hidden-state sharing make one four-ground-station MARL policy reconfigurable across changing visible CubeSat and UAV sets (IEEE TMC early access).
- [[xiao-2020-secrecy-energy-efficiency-relaying]] - Xiao et al. 2020. Collect-store-forward scheduling, power allocation, and fixed-wing trajectory optimization maximize mobile-relay secrecy throughput per propulsion joule (IEEE TGCN).
- [[guo-2026-irs-uav-isac-secrecy]] - Guo et al. 2026. A UAV-mounted IRS, artificial noise, beamforming, and robust trajectory design maximize secrecy rate under radar-SNR and bounded-CSI constraints (IEEE TGCN).
- [[li-2026-credit-aware-uav-irs-secrecy]] - Li et al. 2026. Exact Shapley credit and primal-dual constraints extend MASAC for cooperative multi-UAV-IRS secrecy control (IEEE TWC).
- [[huang-2026-intelligent-jamming-maritime]] - Huang et al. 2026. Advantage-conditioned SAC-CVAE and LSTM eavesdropper prediction coordinate relay/jammer UAVs for secure energy-aware maritime communication (IEEE TMC accepted version).
- [[feng-2026-secure-short-packet-noma-relay]] - Feng et al. 2026. Dual-phase spatially suppressed artificial noise, finite-blocklength NOMA allocation, and hovering relay placement maximize weighted effective secrecy rate (IEEE TWC).
- [[yan-2026-uav-trajectory-monitoring]] - Yan et al. 2026. Single-BS ISAC trajectory monitoring with PRDFT motion estimation, position/velocity association, and IMMUKF prediction (IEEE TWC).
- [[zhu-2023-aoi-transformer-trajectory]] - Zhu et al. 2023. AoI-minimal clustered IoT collection using Transformer cluster ordering and weighted A-star hover-point selection (IEEE TWC).
- [[samir-2020-time-constrained-data-collection]] - Samir et al. 2020. Hard-deadline IoT admission with joint UAV trajectory and spectrum allocation through BRB and scalable SCA (IEEE TWC).
- [[chang-2026-data-offloading-energy-constraints]] - Chang et al. 2026. Many-to-one IoT pickup/delivery routing with battery-station insertion and iterative completion-time minimization (IEEE TGCN).
- [[hua-2026-unpredictable-uav-trajectory]] - Hua et al. 2026. Navigation/stochastic heading-control decomposition evaluated through one-step Kalman prediction error for anti-jamming UAV data collection (IEEE T-ITS).
- [[hong-2026-beam-delay-alignment]] - Hong et al. 2026. Wideband ground-AP cell-free downlink with beam-delay alignment, semi-synchronized path sets, GCN clique proposals, and reused true-time-delay hardware (IEEE TWC).
- [[shi-2026-vhetnet-comp-coverage]] - Shi et al. 2026. Same-tier three-site CoMP coverage analysis and deficit-weighted ABS placement in a vertical terrestrial-aerial heterogeneous network (IEEE TWC).

## Entities

- [[qunshu-wang]] - Dalian University of Technology researcher across full-duplex covert ISAC and primary-signal-assisted cooperative cognitive radio.
- [[cheng-zhan]] - Southwest University professor spanning UAV data collection, MEC optimization, dependent-task offloading, and STAR-RIS aerial monitoring.
- [[kaifeng-song]], [[rongfei-fan]], and [[han-hu]] - Beijing Institute of Technology researchers recurring across dependent-task UAV-MEC and stochastic aerial monitoring; Han Hu also contributes to classical UAV-MEC optimization.
- [[xiaojun-yuan]] - UESTC researcher connecting robust RIS-assisted UAV secrecy and hierarchical AirComp federated learning.
- [[ying-jun-angela-zhang]] - CUHK researcher connecting stochastic Lyapunov UAV-MEC control and hierarchical AirComp federated learning.
- [[tiankui-zhang]] - BUPT researcher spanning classical UAV-MEC optimization, secure dual-UAV MEC, safe emergency trajectory control, and radio-map-aided aerial logistics.
- [[rong-chai]] - CQUPT researcher across satellite-aerial offloading, UAV-ISAC content delivery, and statistical relay deployment.
- [[qianbin-chen]] - CQUPT researcher across satellite-aerial offloading, UAV-ISAC content delivery, LLM-guided multi-UAV edge control, and statistical relay deployment.
- [[kaitao-meng]] - University of Macau UAV-ISAC researcher across the 2023 periodic-sensing article, 2024 overview, and 2026 correction.
- [[wei-yang-bryan-lim]] - recurring UAV federated-learning author spanning contract-matching incentives and communication-pipelined split FL.

### Authors

- [[chunguo-li]] - Southeast University researcher across delay-aligned cell-free transmission, robust UAV collection, and covert ISAC.
- [[dongming-wang]] - Southeast University researcher across cell-free distributed MIMO and cooperative low-altitude ISAC.
- [[xiaohu-you]] - Southeast University IEEE Fellow across cell-free UAV service, cooperative ISAC, and control-assisted beam tracking.
- [[shaoqiang-yan]] - single- and multi-BS ISAC UAV trajectory monitoring.
- [[hongliang-luo]] - Tsinghua researcher across single-BS monitoring, multi-BS fusion, and sensing-cell handover.
- [[ping-yang]] - Rocket Force University researcher in ISAC UAV trajectory monitoring.
- [[feifei-gao]] - Tsinghua IEEE Fellow across UAV monitoring and networked-ISAC tracking.
- [[moataz-samir]] - UAV collection, vehicular coverage, and AoI scheduling.
- [[sanaa-sharafeddine]] - UAV communications, data collection, coverage, freshness, and localization.
- [[chadi-assi]] - Concordia researcher across UAV collection, coverage, AoI, and localization.
- [[ali-ghrayeb]] - UAV data collection, vehicular coverage, and freshness control.
- [[ling-lyu]] - Dalian Maritime University / Xidian University; graph resource management and situation-aware UAV-ISAC control.
- [[yanpeng-dai]] - Dalian Maritime University / Xidian University; graph resource management and UAV sensing/control.
- [[nan-cheng]] - Xidian University; non-terrestrial networking, graph resource management, and UAV-ISAC.
- [[weidang-lu]] - Zhejiang University of Technology; emergency networking, secure aerial edge computing, and robotic-network information quality.
- [[suzhi-bi]] - Shenzhen University; wireless optimization across UAV-MEC, localization, and sparse-array ISAC.
- [[carla-fabiana-chiasserini]] - Politecnico di Torino; TN-NTN incentives and satellite/UAV-RIS channel prediction.

- [[xiang-cheng]] (Peking University - aerial channel modeling, UAV/vehicle simulation, and multi-UAV ISAC; 4 sources), [[rongqing-zhang]] (HKUST Guangzhou - intelligent transportation and aerial networks; 2 sources), [[jung-ryun-lee]] (Chung-Ang University - learning-based UAV/IRS energy control; 2 sources), [[octavia-a-dobre]] (Memorial University - RIS/ISAC channel analysis and generation; 2 sources), and [[halim-yanikomeroglu]] (Carleton University - aerial placement, UAV-mounted IRS communications, and HAPS-UAV ISAC; 3 sources).
- [[yonghui-li]] (University of Sydney - intelligent surfaces, secure wireless-powered MEC, and aerial IAB backhaul; 2 sources).
- [[zhu-xiao]] (Hunan University - vehicular edge offloading and channel-based passive UAV detection; 2 sources).
- [[gang-feng]] and [[shuang-qin]] (UESTC - satellite-edge resource management and robust UAV network slicing; 2 sources each), [[junting-chen]] (CUHK-Shenzhen - radio-map search and predictive routing; 2 sources), and [[charalambos-menelaou]] and [[stelios-timotheou]] (KIOS/University of Cyprus - urban UAV traffic planning and UAV-sensed road-state estimation; 2 sources each).

- [[zheng-chang]] (UESTC / University of Jyväskylä - UAV communications, edge computing, ISAC, and green communications; 7 sources).
- [[dusit-niyato]] (NTU) appears across 66 sources spanning aerial networking, edge intelligence, security, incentives, and optimization; [[zhu-han]] (Univ. of Houston / Kyung Hee) appears across 22 sources; [[xuemin-shen]] (Waterloo) appears across 18 sources; [[ning-zhang]] (Windsor) appears across 4 sources after the adaptive digital-twin UAV-ISCC paper.
- [[shi-jin]] (Southeast University - low-altitude ISAC, movable arrays, anti-jamming, and cooperative data collection; 5 sources), [[yongming-huang]] (Southeast University / Purple Mountain Laboratories - predictive UAV beam tracking and aerial rotatable arrays; 3 sources), and [[jun-du]] (Tsinghua University - distributed 6G learning and location privacy; 2 sources).
- [[qi-qi]] (BUPT - satellite/aerial edge computing and multi-UAV cooperation; 2 sources), [[shaohua-wu]] (Harbin Institute of Technology, Shenzhen - satellite-UAV semantic communication and maritime/satellite networking; 3 sources), and [[qinyu-zhang]] (Harbin Institute of Technology, Shenzhen - satellite, maritime, and non-terrestrial communications; 4 sources).
- [[fuhong-song]], [[jie-xu]], [[wei-zhang]], [[ying-chen]], and [[yong-wang]] - indexed author pages with cross-source MEC, UAV-communications, and optimization rosters; see the individual pages for source-specific affiliations and namesake notes.
- [[zehui-xiong]] (Queen's University Belfast - generative AI, semantic communication, physical-layer security, and low-altitude resource allocation; 15 sources spanning surveys, diffusion/GDM methods, aerial/satellite control, UAV content incentives, and federated-learning mechanisms).
- [[weijie-yuan]] (Southern University of Science and Technology - ISAC, OTFS, covert jamming, and low-altitude wireless networks; 5 sources), [[george-k-karagiannidis]] (Aristotle University of Thessaloniki - wireless communication and signal processing; 3 sources), [[yuanming-shi]] (ShanghaiTech University - edge AI, wireless optimization, and federated learning; 3 sources), and [[xingwang-li]] (Henan Polytechnic University - UAV/IRS wireless communications; 4 sources).
- [[kai-kit-wong]] (University College London - wireless communications, fluid antennas, RIS, UAV-MEC, and spectrum sharing; 8 sources), [[chan-byoung-chae]] (Yonsei University - aerial communications and resource allocation; 3 sources), [[riheng-jia]] (Zhejiang Normal University - wireless/energy-harvesting networks and smart IoT; 2 sources), and [[minglu-li]] (Zhejiang Normal University / Shanghai Jiao Tong University - AIoT and network computing; 2 sources).
- [[qixun-zhang]] (BUPT - UAV-swarm MEC, physical-layer mobility, and cooperative ISAC detection; 3 sources), [[kun-yang]] (Nanjing University / University of Essex - UAV-MEC and cooperative sensing; 4 sources), [[fan-liu]] (SUSTech to Southeast University - ISAC sensing, localization, and tracking; 3 sources), and [[christos-masouros]] (University College London - ISAC and control-assisted beamforming; 3 sources).
- [[derrick-wing-kwan-ng]] (wireless communications, RIS, UAV edge systems, covert ISAC, predictive beam tracking, ISCPT, and wireless surveillance; 8 sources), [[arumugam-nallanathan]] (Queen Mary University of London - aerial edge and wireless security; 7 sources), [[yanping-liu]] (heterogeneous UAV data collection and AoI-energy optimization; 2 sources), [[xuming-fang]] (multi-UAV resource management; 3 sources), [[zhongxiang-wei]] (JRC and secure aerial-RIS systems; 2 sources), and [[qingjiang-shi]] (wireless optimization and aerial ISAC; 2 sources).
- [[guangxu-zhu]] (Shenzhen Research Institute of Big Data - ISAC and edge AI; 6 sources), [[zhe-song]] and [[xuanhe-yang]] (Beijing Institute of Technology - directional UAV discovery/link maintenance; 2 sources each), [[shuai-wang]] and [[gaofeng-pan]] (Beijing Institute of Technology - directional FANETs and jitter-aware CoMP; 3 sources each), and [[chee-yen-leow]] (Universiti Teknologi Malaysia - UAV protocols and collaborative beamforming; 2 sources).
- [[rongke-liu]] (Beihang University - satellite offloading, UAV-swarm sensing/communication, and bistatic UAV-ISAC SAR; 4 sources), [[xiaotian-zhou]] (Shandong University - aerial vehicular control and predictive beamforming; 2 sources), and [[haixia-zhang]] (Shandong University - UAV computing-power networks, predictive beamforming, and vehicular resource control; 3 sources).
- [[xiaojie-wang]] (CQUPT - UAV-MEC, differentiated aerial services, IRS mobility, and ISAC security; 8 sources), [[lei-guo]] (Northeastern University - secure UAV-MEC, aerial service control, and robust ISAC; 8 sources), [[cunhua-pan]] (Southeast University - UAV-MEC, RIS, and cooperative aerial ISAC; 6 sources), and [[nauman-aslam]] (Northumbria University - UAV-MEC trajectory learning and IRS-assisted aerial communication; 3 sources).

- [[lihan-liu]], [[hongrui-miao]], [[chunhui-qu]], [[zhuwei-wang]], [[haijun-zhang]], [[zhidu-li]] — co-authors of [[liu-2026-jppo-en-convntm]].
- [[chaoda-peng]], [[xumin-huang]], and [[yuan-wu]] are recurring co-authors across the [[cmop-evolutionary-uav-mec-lineage|CMOP-evolutionary UAV-MEC lineage]]; [[jiawen-kang]] appears across 24 sources spanning that lineage, generative AI, semantic communication, localization, federated-learning incentives, and aerial edge computing.
- [[hao-hao]] — first author of the two priority-aware offloading sources ([[hao-2024-clp-multiuav-priority-offloading]], [[hao-2025-priority-aware-task-driven-co]]).
- [[geng-sun]] — recurring (co-)author across 25 Jilin-University / NTU aerial-MEC and secure-maritime sources, including collaborative beamforming, low-altitude-economy surveying, and [[huang-2026-intelligent-jamming-maritime]].
- **Jilin-University / NTU aerial-MEC cluster:** [[zemin-sun]], [[jiahui-li]] (Jilin University), [[jiacheng-wang]], [[dusit-niyato]] (NTU), [[victor-c-m-leung]], and [[qingqing-wu]] (Shanghai Jiao Tong University).
- **NUAA aerial-computing cluster:** [[ziye-jia]], [[chao-dong]], [[qihui-wu]] (NUAA), [[zhu-han]] (Univ of Houston / Kyung Hee), spanning HAP/UAV MEC, maritime AAV cooperation, [[jia-2026-dro-lawn-trajectory]], and [[jia-2026-hierarchical-uav-swarms]].
- **Dalian-Maritime-University maritime cluster:** [[bin-lin]] (DMU), [[zhen-wang]] (DMU / Dalian Neusoft), [[qiang-ye]] (Univ of Calgary).
- **NWPU non-terrestrial-network cluster:** [[bomin-mao]], [[hongzhi-guo]], [[jiajia-liu]] (Northwestern Polytechnical University).
- **Virginia Tech (Wireless@VT) UAV-communications cluster:** [[mohammad-mozaffari]], [[walid-saad]] – foundational UAV-as-aerial-base-station, 3-D deployment, and 3-D cellular-network works (5 sources each).
- **NCEPU aerial-edge cluster:** [[peng-qin]], [[yang-fu]] (North China Electric Power University); [[jingjing-wang]] (Beihang University) links the blockchain-UAV thread.
- **South-China-Agricultural-University evolutionary UAV-MEC cluster:** [[zexiong-wu]] (with [[chaoda-peng]], [[xumin-huang]], [[yuan-wu]]).
- **Cross-cutting seniors:** [[chunxiao-jiang]] (Tsinghua), [[tony-q-s-quek]] (SUTD).
- [[chi-harold-liu]] (Beijing Institute of Technology - mobile crowdsensing and distributed multi-UAV DRL; 3 sources).
- [[zhaolong-ning]] (Chongqing University of Posts and Telecommunications - differentiated UAV services, multi-UAV MEC, IRS-assisted communication, computing-power networks, and secure/age-aware low-altitude control; 11 sources).
- [[shuang-liang]] (Northeast Normal Univ. — aerial-MEC / LAE, [[geng-sun]] cluster), [[weifeng-zhong]] & [[shengli-xie]] (Guangdong Univ. of Technology — CMOP-evolutionary lineage), [[qiqi-xie]] (South China Agricultural Univ. — evolutionary UAV-MEC), [[nei-kato]] (Tohoku Univ.), [[jiadai-wang]], [[yijie-xun]], [[yangbo-liu]] (Northwestern Polytechnical Univ. — NTN cluster, [[bomin-mao]] group).
- [[boxiong-wang]] & [[hui-kang]] (Jilin University — [[geng-sun]] aerial-MEC cluster; 2 sources each).
- [[yuben-qu]] & [[hao-sun]] (Nanjing Univ. of Aeronautics and Astronautics — UAV-swarm collaborative-inference cluster with [[chao-dong]]/[[qihui-wu]]; 2 sources each — [[qu-ecoei-uav-swarm]] + [[sun-2024-asap-uav-swarm]], identical `@nuaa.edu.cn` emails).
- [[kezhi-wang]] (Northumbria Univ. — UAV-MEC trajectory/offloading group; 5 sources), [[xuemin-shen]] (Univ. of Waterloo — MEC and non-terrestrial resource management; 18 sources), [[yuguang-fang]] (City Univ. of Hong Kong — maritime MEC and UAV-enabled Computing Power Networks; 3 sources), [[haixia-peng]] (Univ. of Waterloo → Xi'an Jiaotong Univ. — vehicular + maritime MEC; 2 sources, affiliation move documented in both parses).
- [[liping-qian]] (Zhejiang Univ. of Technology — NOMA / multi-access marine MEC; 7 sources), [[qian-wang]] (Zhejiang Univ. of Technology - marine-IoT energy/security resource allocation; 3 sources), [[minghui-dai]] (Univ. of Macau — marine multi-access offloading; 3 sources, `minghuidai@um.edu.mo`), [[zhiyong-feng]] (Beijing Univ. of Posts and Telecommunications — UAV-swarm MEC, UAV-ISAC, cooperative multi-BS ISAC, and movable-antenna PLS; 6 sources).
- [[fuhui-zhou]] (Nanjing Univ. of Aeronautics and Astronautics - wireless-powered MEC, UAV optimization, embodied tracking, physical-layer security, spectrum sharing, and cooperative data collection; 7 sources).
- [[xinlei-chen]] (Tsinghua SIGS - multi-UAV ISAC and LLM-guided emergency networking; 2 sources), plus [[gyu-seon-kim]] and [[joongheon-kim]] (Korea University), [[soyi-jung]] (Ajou University), and [[soohyun-park]] (Sookmyung Women's University) across dynamic SAGIN access and scale-reconfigurable MARL (2 sources each, with [[soohyun-park]] also contributing to LEO handover optimization).
- [[qian-zhu]] (Beihang University - UAV-swarm ISAC positioning and resource allocation; 2 sources), [[daosen-zhai]] and [[ruonan-zhang]] (Northwestern Polytechnical University - robust relaying and semantic aerial-edge optimization; 2 sources each), [[marco-di-renzo]] (Paris-Saclay/CNRS - robust and learned aerial-RIS communications; 2 sources), and [[meixia-tao]] (Shanghai Jiao Tong University - RIS secrecy and secure UAV-MEC; 2 sources).
- [[shichao-li]] & [[hongbin-chen]] (Guilin Univ. of Electronic Technology — air-ground IoRT MEC, VEC, SAGIN, and UAV-IRS data collection; 4 and 5 sources), [[mianxiong-dong]] (Muroran Inst. of Technology; 2 sources) & [[ning-zhang]] (Univ. of Windsor; 2 sources) — co-authors across the IoRT + robust-multi-UAV DRL offloading thread, [[victor-c-m-leung]] (Shenzhen MSU-BIT / Shenzhen Univ. / UBC, `vleung@ieee.org`; 12 sources across aerial-MEC, SAGIN, WDC/WET, and secure IoV).
- [[zhou-su]] (Xi'an Jiaotong Univ. — maritime/vehicular edge computing; 2 sources, corresponding author of [[zeng-2024-usv-fleet-collaborative-offloading]]), [[yanheng-liu]] (Jilin Univ. — [[geng-sun]] aerial/vehicular-MEC cluster; 2 sources).
- [[jiawei-huang]] and [[aimin-wang]] (Jilin University - maritime physical-layer security through collaborative beamforming and learning-based friendly jamming; 3 sources each), and [[basem-shihada]] (KAUST - energy-aware UAV communication and O-RAN maritime slicing; 2 sources).
- [[qiuming-zhu]] (NUAA - aerial channel reconstruction and movable-antenna multi-UAV MIMO; 2 sources), [[yuanwei-liu]] (wireless security, aerial collaborative beamforming, cooperative ISAC, movable antennas, and decentralized UAV resource allocation; 8 sources), and [[haichao-wang]] (Army Engineering University - wireless-powered D2D, NOMA-UAV relay planning, and hierarchical UAV deployment; 3 sources).
- [[li-wang]] and [[lianming-xu]] (BUPT - emergency UAV caching/repair and joint localization-communication control; 3 sources each, identity matched by affiliation and ORCID).
- [[ke-xiong]] (Beijing Jiaotong University - wireless-powered aerial computing and ISCPT; 2 sources), [[pingyi-fan]] (Tsinghua University - aerial/vehicular optimization; 3 sources), [[khaled-ben-letaief]] (HKUST - MEC, physical-layer AI, XL-MIMO, and aerial systems; 8 sources), and [[naofal-al-dhahir]] (UT Dallas - robust RIS and anti-jamming wireless systems; 3 sources).
- [[kaoru-ota]] (Muroran Inst. of Technology, `ota@csse.muroran-it.ac.jp` — with [[mianxiong-dong]]; 2 sources, blockchain-secured + air-ground IoRT UAV-MEC). [[mianxiong-dong]] is now at 3 sources (+[[wang-2024-blockchain-uav-mec-dpos]]).
- [[dong-jun-han]] & [[christopher-brinton]] (Purdue University — non-terrestrial **federated-learning** offloading cluster with Mung Chiang / David J. Love / Seyyedali Hosseinalipour; 2 sources each — [[han-2024-ground-satellite-fl]] + [[han-2024-sagin-fl-handover]]).
- [[yong-zeng]] (Southeast University / Purple Mountain Laboratories; earlier National University of Singapore — **UAV-communications / trajectory-optimization** foundations plus low-altitude [[movable-antenna]], ISAC-localization, secure relaying, multicast, and ray-array design; 17 sources, including [[zeng-2016-throughput-relaying]], [[zeng-2017-energy-efficient-uav-trajectory]], [[zeng-2018-uav-multicasting-completion-time]], [[xiao-2020-secrecy-energy-efficiency-relaying]], and [[jiang-2026-ray-antenna-array]]).
- [[lin-xiao]], [[yu-xu]], and [[dingcheng-yang]] (Nanchang University/BUPT progression - UAV relaying, secure MEC, and aerial resource optimization; 2, 3, and 5 sources), [[xulong-li]] and [[wei-huangfu]] (USTB - MARL for aerial ISAC and UAV-IRS secrecy; 2 sources each), [[jiahao-huo]] (USTB - satellite offloading and UAV secure communication; 2 sources), [[huabing-lu]] (Nanchang University - NOMA, URLLC, and air-ground MEC; 2 sources), [[chengwen-xing]] (Beijing Institute of Technology - RIS-ISAC and finite-blocklength security; 3 sources), and [[xianbin-wang]] (Western University - trusted maritime and robust aerial communications; 4 sources).
- [[shuguang-cui]] (The Chinese University of Hong Kong, Shenzhen — physical-layer / edge-AI / surveys; 7 sources spanning the graph-based-resource-management two-part survey, XL-MIMO, generative-AI/ISAC physical-layer, ISCC edge-AI, and generative-diffusion network optimization).

(One recurring author name remains deferred for human confirmation as genuine **namesakes**: "Nan Zhao" appears in [[zhao-2022-matd3-multiuav-ec-offloading]] (Hubei Univ. of Technology) and [[zhang-2025-gan-td3-isac-active-ris]] (Dalian Univ. of Technology) — different institutions and emails, so not merged. The Tsinghua-era "Jingjing Wang" in [[yang-2020-loadbalance-multiuav-iot]] is the same [[jingjing-wang]] now at Beihang: both biographies report the 2014 Dalian B.S., 2019 Tsinghua Ph.D., 2017-2018 Southampton visit, and collaboration with [[chunxiao-jiang]].)

> Deferred affiliation move: "Chau Yuen" recurs in [[jia-2022-hierarchical-aerial-matching]] (Singapore Univ. of Technology and Design, `yuenchau@sutd.edu.sg`) and [[sun-2025-tjcct-twotimescale-uav-mec]] (Nanyang Technological Univ., `chau.yuen@ntu.edu.sg`). Same name, different listed institution/email (a plausible affiliation move rather than a namesake), so no entity page was minted pending human confirmation.

### Tools

- [[airfogsim]] - modular simulator for UAV-integrated vehicle fog computing.

- [[pytorch]] — DL framework.

(More authors appear in source frontmatter; entity pages exist for the central recurring contributors.)

## Concepts

- [[beam-delay-alignment-transmission]] - path-aware beamforming plus transmission delays that align useful multipath arrivals.
- [[semi-synchronized-path-set]] - AP-local delay-compatible user-path clique under a cyclic-prefix tolerance.
- [[wideband-asynchronous-cell-free-massive-mimo]] - distributed AP service when propagation/multipath delay exceeds CP tolerance.
- [[dual-purpose-time-delay-network]] - analog delay hardware reused for beam-split calibration and symbol synchronization.
- [[coordinated-multipoint-transmission]] - multiple coordinated sites jointly serving a user.
- [[same-tier-three-site-comp]] - three aerial or three terrestrial sites cooperate while mixed serving triads are excluded.
- [[two-regime-aerial-user-association]] - parameter-dependent altitude regimes balancing terrestrial LoS and aerial-site proximity.
- [[poisson-delaunay-comp-clustering]] - Delaunay-triangle cooperation groups for point-process CoMP analysis.
- [[uav-trajectory-monitoring]] - discovery, association, state estimation, and prediction for maintaining target-UAV trajectory histories.
- [[phase-rotated-dft-motion-parameter-estimation]] - coarse spectral estimation refined by bounded phase rotation.
- [[position-gated-velocity-nearest-neighbor-association]] - covariance position gating followed by velocity-difference track selection.
- [[transformer-weighted-a-star-trajectory-planning]] - learned service-group ordering followed by layered hover-point search.
- [[generalized-traveling-salesman-problem]] - one-representative-per-group combinatorial routing.
- [[hovering-disk-data-collection]] - selecting service points within SNR-feasible cluster disks.
- [[deadline-constrained-uav-data-collection]] - complete-upload admission within device-specific generation/deadline windows.
- [[branch-reduce-and-bound]] - globally bounded partition/reduction search for small monotonic formulations.
- [[many-to-one-pickup-and-delivery]] - grouped pickups that must precede designated delivery nodes.
- [[dynamic-programming-battery-station-insertion]] - optimal replenishment-stop insertion for a fixed service order.
- [[mixed-integer-linear-programming]] - linear optimization with binary or integer decision variables.
- [[unpredictable-uav-trajectory-control]] - stochastic motion designed to raise observer prediction difficulty while preserving mission progress.
- [[navigation-stochastic-control-decomposition]] - bounded split between mission-directed and random motion inputs.
- [[wireless-powered-underground-communication-network]] - above-ground RF energy delivery and underground-to-air data return under soil attenuation.
- [[underground-air-soil-wireless-channel]] - air propagation, interface refraction, and lossy-soil attenuation governed by depth and soil composition.
- [[csi-free-multiantenna-wireless-energy-transfer]] - multi-antenna WET without instantaneous receiver-channel acquisition.
- [[wireless-powered-communication-network]] - harvest-then-transmit communication with coupled WPT and uplink resource allocation.
- [[multi-location-hovering]] - speed-relaxed UAV service represented by optimized hover points and dwell times.
- [[computation-causality-constraint]] - cumulative execution and result-return limits imposed by prior task arrivals and completed computation.
- [[norm-bounded-csi-robust-optimization]] - worst-case design over deterministic channel-error balls.
- [[s-procedure-for-csi-uncertainty]] - conversion of quadratic bounded-CSI implications into finite LMIs.
- [[uav-to-uav-communication]] - direct aerial links for coordination, payload exchange, or relaying.
- [[fractional-power-control]] - capped partial path-loss compensation for uplink interference control.
- [[attentive-memory-integrated-information-exchange]] - attention over link-qualified messages and actions combined with persistent multi-agent memory.
- [[mutual-policy-divergence-exploration]] - inter-agent and temporal policy-divergence objectives for heterogeneous MARL exploration.
- [[integrated-periodic-sensing-and-communication]] - communication-continuous ISAC with prescribed per-frame target sensing frequency and optimized sensing-slot placement.
- [[multidimensional-contract-matching]] - contract screening followed by preference matching under heterogeneous service-provider costs.
- [[spatial-temporal-graph-attention-traffic-clustering]] - device grouping from physical proximity and directional traffic distributions.
- [[traffic-aware-asynchronous-uav-control]] - per-UAV allocation among flight, collection, inter-UAV relay, and delivery modes.
- [[m2llm-state-representation-for-drl]] - projected multimodal-LLM hidden state used as numerical input to a continuous controller.
- [[prediction-driven-joint-trajectory-beamforming]] - future-motion prediction coupled to joint aerial path and beam decisions.
- [[random-linear-network-coding-multicast]] - common-file packet coding that supports recovery from any sufficiently large independent subset.
- [[virtual-base-station-waypoint-design]] - disk-cover waypoints, route ordering, and convex coverage-region entry/exit refinement.
- [[minimum-connection-time-trajectory]] - reliability constraints reduced to required dwell time inside receiver connection regions.

### MEC fundamentals

- [[mobile-edge-computing]]
- [[information-flux-triggered-infrastructure-activation]]
- [[edge-intelligence]]
- [[task-offloading]]
- [[sequential-task-offloading]]
- [[task-migration]]
- [[vehicle-twin-migration]]
- [[service-migration]]
- [[device-association]]
- [[computation-to-communication-ratio]]
- [[computation-peer-offloading]]
- [[computational-task-caching]]
- [[redundant-resource-reallocation]]
- [[uav-content-caching]]
- [[battery-swapping-uav-mec]]
- [[coded-caching]]
- [[erasure-coded-edge-storage]]
- [[regenerating-codes]]
- [[binary-vs-partial-offloading]]
- [[dynamic-voltage-scaling]]
- [[event-driven-vs-slot-driven-offloading]]
- [[task-priority-in-mec]]
- [[priority-based-delay-utility]]
- [[intra-swarm-task-delegation]]
- [[anti-jamming-mec]]
- [[embodied-anti-jamming-resource-allocation]]
- [[wireless-power-transfer]]
- [[laser-power-transfer]]
- [[adaptive-wdc-wet-service-balancing]]
- [[uav-assisted-edge-inference]]
- [[uav-enabled-computing-power-network]]
- [[rf-energy-harvesting]]
- [[energy-harvesting-mec]]
- [[energy-procurement-compensation]]
- [[backscatter-communication]]
- [[simultaneous-wireless-information-and-power-transfer]]
- [[dual-domain-ris-energy-harvesting]]
- [[noma]]
- [[code-domain-noma]]
- [[narrowband-iot]]
- [[cooperative-perception]]
- [[perception-aided-offloading]]
- [[multi-source-data-fusion]]
- [[video-analytics-offloading]]
- [[scalable-uav-video-analytics]]
- [[uav-forest-fire-detection]]
- [[video-transcoding-tradeoff]]
- [[qoe-modeling-mec]]
- [[service-caching-mec]]
- [[secure-caching-uav-mec]]
- [[semantic-content-reuse]]
- [[network-slicing]]
- [[traffic-aware-offloading]]
- [[cell-level-mobile-traffic-prediction]]
- [[parallel-vs-serial-processing]]
- [[virtual-machine-multiplexing]]
- [[task-redundancy-for-reliability]]
- [[dwell-time-constrained-offloading]]
- [[dispersed-computing]]
- [[generative-ai-for-mec]]
- [[hybridrag-network-optimization]]
- [[llm-assisted-resource-allocation]]
- [[aigc-service-provider]]
- [[mobile-aigc-network]]
- [[prompt-engineering]]
- [[distributed-foundation-models]]
- [[over-the-air-computation]]
- [[aircomp-assisted-asynchronous-fl]]
- [[vehicle-fog-computing]]
- [[edge-user-allocation]]
- [[uav-data-collection]]
- [[uav-assisted-mobile-crowd-sensing]]
- [[dynamic-qos-constraints]]
- [[finite-blocklength-urllc]]
- [[layered-semantic-communication]]
- [[semantic-reference-signal-matching]]
- [[network-function-virtualization]]
- [[virtual-network-embedding]]
- [[service-function-chaining]]
- [[small-cell-mec]]
- [[mobility-aware-offloading]]
- [[semantic-communication]]
- [[goal-oriented-semantic-twinning]]
- [[distributed-joint-source-channel-coding]]
- [[multi-modal-semantic-communication]]
- [[probabilistic-semantic-communication]]
- [[task-oriented-communication]]
- [[discriminant-gain]]
- [[device-to-device-communication]]
- [[digital-twin]]
- [[terminal-edge-multiscale-digital-twin]]
- [[multi-digital-twin-network-optimization]]
- [[stochastic-network-calculus]]
- [[graph-based-resource-management]]
- [[hot-spot-problem-iot]]
- [[omrp-overlap-routing]]

### Aerial / network architectures

- [[cooperative-cognitive-radio]]
- [[fully-connected-ris]]
- [[passive-six-dimensional-movable-antenna]]
- [[aerial-terrestrial-cell-free-massive-mimo]]
- [[directional-neighbor-discovery]]
- [[interference-aware-dbscan-pilot-assignment]]

- [[multi-uav-assisted-mec]]
- [[differentiated-uav-service-market]]
- [[high-density-mobile-device-scenarios]]
- [[heterogeneous-uav-fleet]]
- [[hierarchical-uav-swarm]]
- [[releasing-collecting-recycling-uav-framework]]
- [[high-altitude-platform-station]]
- [[hierarchical-aerial-mec]]
- [[air-ground-integrated-network]]
- [[low-altitude-intelligent-network]]
- [[ground-embedded-robot]]
- [[leo-satellite-edge-computing]]
- [[clustered-leo-adaptive-selection]]
- [[leo-satellite-coverage-time]]
- [[leo-handover-protocol]]
- [[walker-star-constellation]]
- [[free-space-optical-isl]]
- [[space-air-ground-integrated-network]]
- [[space-air-ground-ocean-integrated-network]]
- [[non-terrestrial-network]]
- [[urban-air-mobility]]
- [[uav-bus-taxi-emergency-response]]
- [[licensed-unlicensed-spectrum-sharing]]
- [[vehicular-mec]]
- [[uav-enabled-its]]
- [[autonomous-uav-swarms]]
- [[uav-named-data-networking]]
- [[cellular-connected-uav]]
- [[collaborative-uav-communication]]
- [[control-assisted-uav-beam-tracking]]
- [[uav-to-x-communication]]
- [[drone-cell-3d-placement]]
- [[geometric-disk-cover]]
- [[maritime-mec]]
- [[uav-usv-cooperative-mec]]
- [[post-disaster-mec]]
- [[persistent-emergency-uav-swarm-service]]
- [[routing-vnf-scaling-control-loop]]
- [[three-tier-cloud-edge-end]]
- [[wireless-backhaul]]
- [[aerial-active-ris-backhaul]]
- [[stateless-geographic-fanet-routing]]
- [[uav-assisted-vanet-routing]]
- [[directional-fanet-link-maintenance]]
- [[jitter-aware-uav-beamwidth-control]]
- [[evolvable-route-expiration-time]]
- [[fault-tolerant-relay-network]]
- [[intelligent-reflecting-surface]]
- [[beyond-diagonal-ris]]
- [[rate-splitting-multiple-access]]
- [[noma-af-uav-relaying]]
- [[imperfect-sic-residual-interference]]
- [[dynamic-irs-user-association]]
- [[spherical-transmissive-ris]]
- [[uav-mounted-ris]]
- [[tilt-aware-aerial-ris-control]]
- [[star-ris]]
- [[full-space-star-ris-uav-trajectory]]
- [[active-ris]]
- [[decentralized-active-ris-uav-noma-control]]
- [[multi-functional-ris]]
- [[terahertz-communication]]

### UAV control & decisions

- [[statistical-user-position-uav-deployment]]
- [[fly-while-communication]]

- [[uncertainty-triggered-radio-map-update]]

- [[uav-trajectory-control]]
- [[fast-heterogeneous-uav-deployment]]
- [[multi-modal-uav-coverage-backhaul-control]]
- [[distance-attention-uav-navigation]]
- [[memory-augmented-multi-uav-navigation]]
- [[reservation-based-density-aware-4d-uav-planning]]
- [[aircomp-aware-uav-device-cluster-formation]]
- [[control-parameterized-uav-trajectory]]
- [[equipotential-surface-uav-search]]
- [[event-triggered-fuzzy-state-observer]]
- [[compliance-aware-uav-trajectory]]
- [[target-level-of-safety]]
- [[trajectory-privacy]]
- [[bang-bang-control]]
- [[uav-charging-scheduling]]
- [[wireless-powered-uav-fair-service-control]]
- [[parallel-cooperative-uav-charging]]
- [[dynamic-uav-clustering]]
- [[gauss-markov-mobility-model]]
- [[hybrid-action-decision-making]]
- [[b-spline-trajectory]]
- [[rotary-wing-propulsion-energy-model]]
- [[path-aware-3d-visual-coverage]]
- [[fixed-wing-propulsion-energy-model]]
- [[uav-delivery-pickup-dropoff]]
- [[cooperative-uav-taxi-delivery]]
- [[cooperative-uav-human-courier-delivery]]
- [[cooperative-uav-pursuit-evasion]]
- [[speed-coordinated-robust-optimization-control]]
- [[uav-mobile-relaying]]
- [[energy-balanced-cooperative-uav-relaying]]
- [[uav-substitution-relaying]]
- [[angle-of-radiation-uav-relay]]
- [[successive-hover-and-fly-trajectory]]
- [[multi-stage-estimate-design-sense-trajectory]]
- [[energy-constrained-uav-data-collection-orienteering]]
- [[information-causality-constraint]]
- [[aoi-aware-uav-altitude-scheduling]]

### DRL backbones

- [[quantum-marl-sagin-access]]
- [[implicit-opponent-modeling]]
- [[ikpp-action-reconstruction]]

- [[deep-echo-state-network-reinforcement-learning]]
- [[hierarchical-federated-a3c]]

- [[ppo]] · [[j-ppo]]
- [[permutation-equivariant-replay-augmentation]]
- [[digital-twin-assisted-online-drl-policy-refresh]]
- [[ddqn]]
- [[dueling-dqn]]
- [[deep-q-network]]
- [[maximum-entropy-deep-q-learning]]
- [[optimization-driven-drl]]
- [[triple-deep-q-network]]
- [[ddpg]]
- [[td3]] · [[multi-agent-td3]] · [[softmax-deep-double-deterministic-policy-gradients]]
- [[maddpg]]
- [[rmaddpg-dda-uav-isac-control]]
- [[kernel-density-mean-field-marl]]
- [[multi-agent-diffusion-policy]]
- [[masac]]
- [[soft-actor-critic]]
- [[hierarchical-reinforcement-learning]]
- [[action-masked-hierarchical-drl]]
- [[mappo]]
- [[heterogeneous-agent-rl]]
- [[trust-region-policy-optimization]]
- [[parameterized-dqn]]
- [[multi-agent-q-learning]]
- [[value-decomposition-network]]
- [[qmix]]
- [[asynchronous-qmix]]
- [[ensemble-qmix]]
- [[counterfactual-multi-agent-policy-gradient]]
- [[distributional-reinforcement-learning]]
- [[impala]]
- [[gae]]
- [[pomdp]] · [[ma-pomdp]]
- [[markov-reward-process]]
- [[semi-markov-decision-process]]
- [[centralized-training-decentralized-execution]]
- [[multi-agent-imitation-learning]]
- [[communication-constrained-marl]]
- [[model-based-marl]]
- [[mixture-of-experts-drl]]
- [[end-to-end-vs-decomposition-in-drl-mec]]
- [[action-space-explosion-in-multi-uav-mec]]
- [[adaptive-entropy-priority-replay]]
- [[prioritized-experience-replay]]
- [[ape-x-actor-learner-replay]]
- [[episodic-experience-replay]]
- [[safe-reinforcement-learning]]
- [[hybrid-action-representation]]
- [[dynamic-confidence-interval-clipping]]
- [[knowledge-distillation-for-drl]]
- [[heuristic-supervised-drl]]
- [[meta-deep-reinforcement-learning]]
- [[multi-objective-reinforcement-learning]]
- [[multi-objective-mdp-vectorial-reward]]
- [[contextual-momdp]]
- [[evolutionary-reinforcement-learning]]
- [[generative-diffusion-model]]
- [[diffusion-augmented-madrl-replay]]
- [[diffusion-model-as-optimizer]]
- [[generative-adversarial-network]]
- [[variational-autoencoder]]
- [[conditional-gan]]
- [[beta-policy-drl]]
- [[softppo-lstm]]
- [[expert-guided-warm-start-rl]]
- [[pretrained-policy-cooperation-shaping]]
- [[parameter-sharing-marl]]
- [[graph-neural-network]]
- [[sequential-multi-agent-policy-generation]]
- [[multi-agent-transformer]]
- [[dual-network-sequential-aoi-control]]

### Memory / encoders

- [[ntm]] · [[en-convntm]]
- [[j-ppo-en-convntm]] — composite j-PPO + EN-ConvNTM framework page
- [[convlstm]]
- [[stn]]
- [[transformer-encoder]]
- [[spatiotemporal-attention-channel-prediction]]
- [[masked-csi-reconstruction-pretraining]]
- [[dft-beamspace-channel-compression]]
- [[partial-csi-outage-patterns]]
- [[transformer-encoded-mean-field-reinforcement-learning]]
- [[neural-episodic-control-with-state-abstraction]]
- [[mogrifier-lstm-policy]]
- [[wavelet-guided-mamba-crack-segmentation]]
- [[informer-trajectory-prediction]]
- [[probsparse-self-attention-prediction]]
- [[graph-attention-fanet]]
- [[cascading-residual-graph-attention-network]]

### Optimization techniques (classical & evolutionary)

- [[gale-shapley-rematching]]
- [[conditional-judgment-binary-search]]
- [[two-layer-successive-programming]]
- [[non-overlapping-coverage-gain-greedy]]

- [[lyapunov-optimization]]
- [[analytical-target-cascading]]
- [[markov-approximation]]
- [[two-timescale-optimization]]
- [[fractional-programming-dinkelbach]]
- [[stackelberg-game]]
- [[mean-field-game]]
- [[post-decision-state-stackelberg-actor-critic]]
- [[potential-game]]
- [[stochastic-game]]
- [[regret-minimization-learning]]
- [[fictitious-self-play]]
- [[bargaining-game]]
- [[coalition-formation-game]]
- [[joint-switch-coalition-formation-game]]
- [[nash-equilibrium]]
- [[price-of-anarchy]]
- [[prospect-theory]]
- [[contract-theory]]
- [[aoi-aware-contract-incentives]]
- [[contract-theoretic-fl-incentives]]
- [[matching-theory-for-resource-allocation]]
- [[optimal-transport-theory]]
- [[gale-shapley-matching]]
- [[overlay-underlay-spectrum-access]]
- [[unicast-multicast-cooperation]]
- [[mixed-integer-nonlinear-programming]]
- [[dynamic-constrained-multi-objective-optimization]]
- [[constrained-multi-objective-evolutionary-algorithm]]
- [[genetic-algorithm]]
- [[data-similarity-aware-coalition-formation]]
- [[partial-space-adaptive-play]]
- [[non-dominated-sorting-genetic-algorithm]]
- [[cmoea-d-cdp]]
- [[constraint-violation-evaluation]]
- [[infeasible-individual-utilization]]
- [[dual-population-evolutionary-algorithm]]
- [[multi-tasking-evolutionary-algorithm]]
- [[differential-evolution]]
- [[local-search-evolutionary]]
- [[enhanced-human-evolutionary-optimization]]
- [[two-stage-decomposition]]
- [[penalty-dual-decomposition]]
- [[second-order-cone-programming]]
- [[linear-programming]]
- [[alternating-optimization-sdr-sca]]
- [[accelerated-proximal-gradient-trajectory-power-control]]
- [[fixed-point-irs-passive-beamforming]]
- [[block-successive-upper-bound-minimization]]
- [[monotonic-optimization]]
- [[majorization-minimization]]
- [[qcqp-sdr-probabilistic-mapping]]
- [[order-preserving-quantization]]
- [[binary-whale-optimization]]
- [[whale-optimization-algorithm]]
- [[salp-swarm-algorithm]]
- [[sparrow-search-algorithm]]
- [[ant-lion-optimizer]]
- [[sum-of-ratios-optimization]]
- [[self-adaptive-global-best-harmony-search]]
- [[multi-verse-optimizer]]
- [[gravitational-search-algorithm]]
- [[particle-swarm-optimization]]
- [[ant-colony-optimization]]
- [[weighted-kmeans-uav-deployment]]
- [[k-dbscan-uav-deployment]]
- [[spectral-clustering-monotone-gibbs-deployment]]
- [[chance-constraint]]
- [[conditional-value-at-risk]]
- [[distributionally-robust-optimization]]
- [[robust-offloading]]
- [[cross-entropy-method]]
- [[generalized-assignment-problem]]
- [[double-auction]]
- [[iterative-double-auction-incentive]]
- [[online-maritime-double-auction]]
- [[reverse-auction-incentive]]
- [[alternating-direction-method-of-multipliers]]
- [[queueing-theory]]
- [[martingale-delay-violation-bound]]
- [[spatiotemporal-information-quality]]
- [[bi-traveling-salesman-problem-with-neighborhoods]]

### Channel modeling

- [[angle-dependent-irs-effective-aperture]]
- [[cell-free-uav-predictive-beamforming]]
- [[covariance-intersection-state-fusion]]
- [[pcrb-guided-pilot-length-optimization]]
- [[blockage-aware-channel-model]]
- [[air-to-ground-channel-model]]
- [[three-dimensional-frequency-reuse]]
- [[angle-dependent-rician-fading]]
- [[radio-map-assisted-channel-estimation]]
- [[radio-map-aided-uav-path-planning]]
- [[multi-modal-intelligent-channel-modeling]]
- [[multi-scale-unet-pathloss-prediction]]
- [[movable-antenna]]
- [[fluid-antenna-system]]
- [[two-level-movable-antenna]]
- [[selective-near-field-area]]
- [[terrain-aware-channel-model]]
- [[terrain-occlusion-aware-graph-state-aggregation]]
- [[first-order-radio-energy-model]]
- [[stochastic-geometry-network-analysis]]
- [[csi-estimation-error]]
- [[multi-frequency-radio-map-uav-relaying]]
- [[jitter-aware-lstm-channel-compensation]]
- [[3gpp-uav-los-probability-model]]
- [[matern-hard-core-bs-deployment]]
- [[polarization-matched-uav-mmwave-metasurface]]

### Sensing & security

- [[primary-signal-assisted-covertness]]
- [[wireless-information-surveillance]]
- [[monitoring-success-probability]]
- [[threshold-based-antenna-selection]]
- [[six-dimensional-aerial-rotatable-antenna-array]]
- [[team-mmse-receive-combining]]
- [[full-duplex-receiver-jamming]]
- [[virtual-partitioned-active-ris-location-privacy]]
- [[bistatic-sar-resolution-fairness]]
- [[radar-estimation-rate]]

- [[dual-objective-multi-uav-isac]]

- [[integrated-sensing-and-communication]]
- [[situation-aware-hybrid-isac-sensing]]
- [[sensing-error-aware-communication-rate]]
- [[adaptive-td-isac-sensing-period]]
- [[integrated-sensing-communication-power-transfer]]
- [[sensing-feasible-uav-reachability]]
- [[closed-form-irs-phase-alignment]]
- [[sensing-signal-assisted-covertness]]
- [[joint-localization-and-communication]]
- [[tdoa-based-uav-localization]]
- [[geometric-dilution-of-precision]]
- [[continuous-omnidirectional-monitoring]]
- [[networked-isac]]
- [[cooperative-isac-transceiver-beamforming]]
- [[space-time-block-codec]]
- [[cramer-rao-bound]]
- [[spatially-separated-uav-isac-role-scheduling]]
- [[ground-air-cooperative-isac-detection]]
- [[integrated-communication-sensing-navigation]]
- [[crb-guided-angular-confidence-beamforming]]
- [[multi-bs-feature-fusion-isac]]
- [[rss-based-uav-localization]]
- [[dynamic-feature-filtering-vslam]]
- [[minor-subspace-tracking]]
- [[uav-localization-under-jamming]]
- [[anti-uav-interference-base-station-deployment]]
- [[integrated-sensing-computation-communication]]
- [[target-graph-representation]]
- [[expert-assisted-anomaly-aware-tracking]]
- [[hybrid-uav-flight-data-fault-detection]]
- [[mmwave-radar-sensing]]
- [[radar-point-cloud-driven-uav-isac]]
- [[csi-based-passive-uav-detection]]
- [[historical-echo-predictive-beamforming]]
- [[radar-sensing-energy-tradeoff]]
- [[uav-backscatter-identification]]
- [[yolov7-object-detection]]
- [[spectrum-sensing-channel-selection]]
- [[multi-domain-uav-anti-jamming]]
- [[hierarchical-graph-anti-jamming-control]]
- [[temporal-spectrum-cartography]]
- [[information-driven-uav-spectrum-mapping]]
- [[physical-layer-security]]
- [[u2g-g2u-secrecy-asymmetry]]
- [[directional-modulation]]
- [[micro-macro-mobility-security]]
- [[covert-communication]]
- [[channel-inversion-power-control]]
- [[ris-assisted-directional-jamming]]
- [[ambient-interference-aided-covertness]]
- [[freshness-aware-covert-uav-communication]]
- [[aoi-centric-uav-isac-beam-control]]
- [[friendly-jamming-uav]]
- [[cooperative-jamming]]
- [[proactive-eavesdropping]]
- [[secure-computation-efficiency]]
- [[secrecy-outage-probability]]
- [[collaborative-beamforming]]
- [[interference-alignment]]
- [[building-blockage-aided-interference-coordination]]
- [[wireless-perception]]
- [[extremely-large-scale-mimo]]
- [[sparse-xl-mimo]]
- [[fourth-order-bistatic-virtual-array]]
- [[symmetric-double-nested-array]]
- [[near-field-communications]]

### Security / trust / federation

- [[hierarchical-over-the-air-federated-learning]]
- [[gradient-correlation-aware-aggregation-mse]]
- [[zero-trust-architecture]]
- [[federated-learning]]
- [[critical-learning-period]]
- [[federated-kl-divergence-norm]]
- [[federated-drift-norm]]
- [[federated-linear-bandit-learning]]
- [[semi-decentralized-hybrid-federated-learning]]
- [[split-federated-learning]]
- [[federated-reinforcement-learning]]
- [[fedx-training-acceleration]]
- [[hierarchical-federated-drl]]
- [[decentralized-federated-learning]]
- [[blockchain-for-fl-aggregation]]
- [[byzantine-fault-tolerant-consensus]]
- [[delegated-proof-of-stake]]
- [[ccvm-correction-voting]]
- [[csra-cold-start-reputation-aggregation]]
- [[fl-poisoning-attacks]]
- [[privacy-sensitive-data-partitioning]]
- [[uav-cluster-authentication]]
- [[two-tier-submodel-partition]]
- [[seamless-handover]]
- [[adaptive-inter-layer-data-offloading]]

### Metrics & fairness

- [[power-delay-product]]

- [[fairness-metrics-in-mec]] — hub tying together the corpus's fairness measures (Jain / spatial-equity / Theil / service-experience / energy-balancing).
- [[equilibrium-efficiency-metric]]
- [[spatial-equity-index]]
- [[energy-expenditure-coefficient]]
- [[theil-fairness-index]]
- [[jains-fairness-index]]
- [[service-experience-ratio]]
- [[completion-time-difference]]
- [[makespan-minimization]]
- [[energy-balancing-uav]]
- [[load-balancing-uav-mec]]
- [[energy-latency-tradeoff]]
- [[effective-energy-efficiency]]
- [[secrecy-energy-efficiency]]
- [[overall-energy-efficiency]]
- [[spectrum-utilization-efficiency]]
- [[age-of-information]]
- [[dynamic-target-prioritization-metric]]
- [[aoi-energy-tradeoff]]

### Distributed inference

- [[collaborative-dl-inference]]
- [[attention-based-uav-target-search]]
- [[multi-exit-dnn]]
- [[dnn-model-partition]]
- [[data-partition-parallel-inference]]
- [[pipeline-parallel-inference]]
- [[dl-inference-latency-prediction]]
- [[adaptive-intermediate-data-compression]]
- [[elastic-task-scheduling]]

### Scheduling

- [[interdependent-tasks-dag]]
- [[longest-transmission-time-first-uav-grouping]]

### Safety

- [[collision-avoidance-mgi]]

- [[adaptive-large-neighborhood-search]] - adaptive destroy-repair metaheuristic for constrained routing and scheduling.
- [[vehicle-uav-collaborative-inspection]] - coupled ground-carrier and aerial-task routing for infrastructure inspection.
- [[multi-armed-bandit-objective-weighting]] - online arm selection for scalarization weights in multi-objective learning.
- [[sensing-assisted-predictive-beamforming]] - echo-assisted prediction, state refinement, and reliability-aware beam control.
- [[open-radio-access-network]] - disaggregated, virtualized RAN architecture with open interfaces and intelligent controllers.
- [[advantage-actor-critic]] - synchronous on-policy actor-critic learning with advantage estimates.
- [[mw-mad3pg]] - MAML-enhanced fairness-aware multi-agent deterministic policy gradient for UAV-assisted sensor scheduling.
- [[weighted-minimum-mean-square-error]] - sum-rate/WMMSE equivalence used for alternating multi-user beamforming and geometry optimization.
- [[selective-uniform-cost-search]] - lower-bound-prioritized grid search with retained communication and movable-array state.
- [[simultaneous-interference-uav-federated-learning]] - UAV-FL resource control that keeps same-resource inter-user interference and rotary-wing return energy explicit.
- [[haps-uav-isac-resource-allocation]] - HAPS-processed multi-UAV sensing/communication trade-offs optimized with GA and NSGA-II.
- [[integrated-access-and-backhaul]] - shared wireless access/backhaul architecture whose end-to-end service is limited by the weaker segment.
- [[access-backhaul-rate-matching]] - anti-accumulation reliability condition coupling relay access rates to finite backhaul capacity.
- [[outage-aware-sagin-uav-altitude]] - ground-UAV-satellite altitude selection under energy- and SNR-outage conditions.
- [[prediction-based-priority-aware-path-planning]] - survivor-likelihood-guided Clarke-Wright routing for disaster-search UAVs.
- [[tree-structured-weight-synthesis]] - centralized averaging of hierarchical UAV logistic-regression models for PSL prediction.
- [[cloud-trained-edge-executed-drl]] - central policy training and refresh with latency-sensitive inference at an edge controller.
- [[robust-uav-network-slicing]] - aerial slice deployment and radio allocation under bounded demand/location uncertainty and Gaussian CSI error.
- [[radio-map-assisted-predictive-routing]] - data-route, hop-time, and power planning from future radio-map statistics along known trajectories.
- [[dynamic-space-time-graph-with-virtual-edges]] - fixed-depth forwarding graph whose same-node edges encode zero-cost caching or waiting.
- [[ray-antenna-array]] - radially oriented directly combined subarrays selected through a limited-RF-chain switch network.
- [[gaussian-process-moving-horizon-traffic-estimation]] - uncertainty-weighted virtual road-traffic measurements inside constrained moving-horizon estimation.
- [[convex-tsp-uav-data-collection]] - shortest-tour planning through heterogeneous communication disks via convex subproblems and TSP sequencing.
- [[distributed-tabular-q-learning-uav-collision-avoidance]] - independently learned local motion policies for simulated multi-UAV collision avoidance.
- [[phase-aware-relativistic-adaptive-descent]] - conformal-symplectic optimizer for unit-modulus aerial-RIS phase control.
- [[environment-state-interactive-attention]] - attention fusion of environment features with actor state for robust aerial-RIS position control.
- [[statistical-priority-based-multiple-access]] - priority-conditioned contention thresholds and backoff for differentiated FANET random access.
- [[uav-energy-supplied-star-ris-noma]] - fixed STAR-RIS/NOMA uplink whose users receive RF energy from a UAV.
- [[harvest-transmit-store-scheduling]] - frame scheduling that orders RF harvesting, D2D transmission, and residual-energy storage.
- [[energy-causality-constraint]] - cumulative-use constraint preventing a node from consuming energy before it is harvested.
- [[improved-fast-base-station-selection]] - rotating azimuth-group search for a low-CRLB subset of UAV localization anchors.
- [[crlb-initialized-q-table]] - inverse-positioning-CRLB prior injection into selected tabular resource-allocation actions.
- [[full-duplex-noma-uav-relay]] - pipelined decode-and-forward UAV relaying with NOMA, SIC, and direct/relay combining.
- [[bernstein-safe-approximation]] - conservative deterministic convex replacement for Gaussian quadratic chance constraints.
- [[robust-uav-position-power-optimization]] - joint expected 3-D relay placement and power allocation under stochastic position error.
- [[robust-ris-assisted-uav-secrecy]] - worst-case bidirectional UAV secrecy through joint trajectory, power, and passive RIS control.
- [[opportunistic-cooperative-multi-uav-ddqn]] - independent DDQN with distance-conditioned state and experience exchange.
- [[lstm-interruption-compensation]] - confidence-filtered short-horizon neighbor-action prediction during UAV link outages.
- [[experience-value-circles]] - distance-dependent utility model for cooperative UAV observation and replay sharing.
- [[edge-intelligent-vehicle]] - mobile UAV logistics hub combined with local edge data processing.
- [[joint-eiv-placement-uav-fleet-sizing]] - coupled ground-hub placement, UAV fleet sizing, speed selection, and deadline scheduling.
- [[simultaneous-lightwave-information-and-power-transfer]] - joint optical information decoding and photovoltaic energy harvesting from one received lightwave.
- [[ground-to-uav-fso-channel]] - ground-to-air optical channel combining atmospheric loss, turbulence, pointing error, and receiver field of view.
- [[fov-aware-optical-uav-reception]] - UAV optical reception whose outage, error, and harvested energy depend explicitly on field-of-view geometry.
- [[semi-passive-star-ris]] - STAR-RIS architecture pairing passive transmitting/reflecting elements with a separate active sensing array on the transmission side.
- [[near-field-star-ris-isac]] - near-field ISAC design using a STAR-RIS to shape communication and target-sensing paths across both half-spaces.
- [[radar-mutual-information-rate]] - information-theoretic sensing metric based on mutual information between a target response and received radar observations.
- [[radio-tomographic-attenuation-mapping]] - inference of spatial attenuation coefficients from links whose paths cross discretized environmental regions.
- [[rank-saturation-rem-updates]] - measurement-selection rule that stops radio-map updates when new path equations cease increasing system rank.
- [[segment-coverage-uav-trajectory]] - UAV trajectory visiting aerial voxels whose measurement rays intersect previously unseen terrain segments.
- [[llm-guided-marl-policy-distillation]] - offline LLM advice distilled into multi-agent policies so deployment no longer queries the language model.
- [[task-oriented-grouped-uav-marl]] - multi-agent control that partitions UAVs into mission groups with group-specific reward emphasis and network roles.
- [[connectivity-preserving-uav-behavioral-loss]] - auxiliary learning loss activated after a critical UAV loses all base-station links to steer it toward the highest-SNR base station.
- [[multi-hop-uav-emergency-networking]] - rapidly deployed UAV relay network maintaining multi-hop service after terrestrial infrastructure failure.
- [[scale-reconfigurable-marl]] - MARL architecture whose active network width adapts to varying numbers of observable devices while weights remain shared.
- [[hidden-state-sharing-marl]] - multi-agent policy that exchanges intermediate neural representations to coordinate decentralized decisions.
- [[collect-store-forward-relaying]] - delay-tolerant mobile relaying that separates reception and forwarding through onboard buffering and information causality.
- [[secure-irs-uav-isac]] - mobile-IRS architecture coupling secrecy, sensing quality, beamforming, artificial noise, and UAV motion.
- [[artificial-noise-aided-physical-layer-security]] - transmitter-generated structured interference steered away from legitimate receivers and toward eavesdroppers.
- [[shapley-value-marl-credit-assignment]] - coalition marginal-contribution rewards whose sum equals the full team value.
- [[primal-dual-constrained-marl]] - constrained policy learning with cost critics and adaptive Lagrange multipliers.
- [[advantage-conditioned-cvae-policy]] - multimodal action decoder conditioned on state and normalized learned advantage.
- [[lstm-eavesdropper-trajectory-prediction]] - partial-observation control using an LSTM estimate of an unobserved eavesdropper's current position.
- [[weighted-effective-secrecy-rate]] - weighted finite-blocklength secrecy throughput discounted by decoding-failure probability.
- [[dual-phase-artificial-noise-uav-relaying]] - source and UAV relay both inject spatially nulled artificial noise across a two-hop path.

## Methodology

- [[ctde-multi-agent-drl-protocol]] - centralized-training / decentralized-execution protocol for cooperative multi-agent MEC control
- [[drl-simulation-with-pomdp-formulation]] — POMDP simulation protocol used in [[liu-2026-jppo-en-convntm]]
- [[ao-sdr-sca-convex-pipeline]] — the AO + SDR + SCA convex pipeline recurring across the ISAC/secure-beamforming sources
- [[lyapunov-guided-drl]] — the Lyapunov drift-plus-penalty + per-slot DRL hybrid across 6 sources
- [[discrete-continuous-two-stage-decomposition]] — the discrete-then-continuous (matching/metaheuristic/discrete-policy + convex/continuous-policy) solver protocol
- [[llm-assisted-mec-optimization-control-plane]] — LLM formulation / teacher-policy / state-reward / long-tail repair roles around MEC optimizers

## Findings

- [[en-convntm-beats-baselines]]
- [[neuralmap-loses-spatial-info]]
- [[uav-count-inverted-u-energy]]
- [[charging-stations-improve-efficiency]]
- [[hybrid-action-beats-pure-drl]]
- [[finding-optimal-loss-entropy-weight-coefs]]
- [[bcsa-frl-tolerates-up-to-half-malicious-satellites]]
- [[maritime-three-tier-energy-saving]] — 39.3% system-energy saving ([[zhang-2025-three-tier-maritime-offloading]])
- [[fedleo-delay-accuracy-tradeoff]] — up to 41% delay / 9.39% accuracy ([[zhai-2023-fedleo-decentralized-fl]])
- [[asap-swarm-inference-speedup]] — up to 92.66% latency cut, hardware-validated ([[sun-2024-asap-uav-swarm]])
- [[masac-beats-maddpg-sensing-queue]] — +15.41% sensing / −30.73% queue delay vs MADDPG ([[qin-2025-bcuav-masac]])
- [[acbft-throughput-increase]] — up to 96.2% consensus-throughput increase vs existing chaining protocols ([[wang-2025-acbft-uav-consensus]])
- [[dcb-cuts-satellite-handover-frequency]] — ~30% fewer LEO handovers at similar uplink rate ([[li-2024-emodrl-ground-space-cb]])
- [[no-true-end-to-end-drl-in-corpus]] — corpus-wide: every DRL work exploits problem structure; no true end-to-end model
- [[llm-state-reward-secure-lae-data]] — LLM state/reward design cuts AoI and energy in secure LAE data collection ([[cai-2026-llm-drl-secure-lae-data]])

## Thesis

- [[hybrid-action-memory-augmented-drl-wins-uav-mec]] — hybrid-action, memory-augmented DRL is the right design for UAV-MEC under high-density mobility
- [[decomposition-beats-end-to-end-drl-in-mec]] — decomposition-based solvers beat truly end-to-end DRL for joint MEC optimization
- [[explicit-constraints-beat-reward-shaping-in-mec-drl]] — explicit constraint-handling mechanisms beat reward shaping for safety / long-term / robustness constraints

## Queries

- [[query-does-en-convntm-generalize-beyond-uav-mec]]
- [[query-real-world-validation-of-jppo-en-convntm]]
- [[query-when-does-dro-beat-drl-for-csi-uncertainty]] — DRO vs DRL vs structure for CSI uncertainty
- [[query-video-vs-cooperative-perception-offloading-shape]] — do rich-media offloading workloads share an optimization shape?
- [[end-to-end-drl-feasibility-large-scale-mec]] — is end-to-end DRL feasible in large-scale multi-UAV MEC?

## Comparisons

- [[ddpg-vs-jppo]]
- [[j-ppo-vs-pdqn]] — native hybrid-action head-to-head: on-policy j-PPO vs off-policy P-DQN
- [[j-ppo-baselines]]
- [[bcsa-frl-vs-bc-uav-masac]] — Blockchain-on-edge: BCSA-FRL vs BC-UAV-MASAC
- [[game-theoretic-offloading-formulations]] — potential vs Stackelberg vs bargaining vs matching
- [[ctde-actor-critic-backbones-in-mec]] — CTDE multi-agent backbones: MADDPG vs MATD3 vs MASAC vs MAPPO vs value-based

## Synthesis

- [[aerial-federated-aggregation-design-space]] — Synchronous, asynchronous, hierarchical, event-triggered, interference-limited, and split aggregation compared by learning and physical-layer assumptions.
- [[design-recipe-multi-uav-mec]] — 10-step recipe for DRL-controlled UAV-MEC.
- [[drl-backbones-across-uav-mec-sources]] — Cross-corpus DRL-backbone analysis.
- [[maddpg-vs-masac-in-mec]] — When entropy beats determinism in cooperative MEC.
- [[cmop-evolutionary-uav-mec-lineage]] — Peng/Huang group's 6-paper CMOP-evolutionary lineage (2022-2026).
- [[swarm-metaheuristics-in-uav-mec]] — Nine-plus swarm-intelligence metaheuristics (PSO/WOA/SSA/MVO/ALO/GSA/ACO/SGHS) mapped by role (standalone Pareto solver vs embedded sub-solver).
- [[hierarchical-aerial-mec-design-space]] — Cross-comparison of the 5 UAV+HAP hierarchical-MEC sources.
- [[drl-vs-evolutionary-vs-classical-solvers]] — Solver-family analysis (DRL / evolutionary / classical).
- [[sagin-satellite-offloading-landscape]] — The 8 SAGIN / satellite-offloading sources mapped by satellite role + solver shape.
- [[isac-sensing-in-aerial-mec]] — How sensing enters the 7 ISAC/sensing sources.
- [[gai-generator-vs-optimizer-in-isac]] — GAI as physical-layer generator vs decision-layer optimizer across the 4 ISAC GAI sources.
- [[maritime-mec-architectures]] — Tiering + solver families across the 7 maritime sources.
- [[blockchain-on-edge-trust-layer]] — Which layer the blockchain defends (consensus / aggregation / audit) across the 3 blockchain-on-edge sources.
- [[safety-and-robustness-mechanisms-in-mec]] — Safe-RL / DRO / bounded-robust / structural-side-step mechanisms compared by threat, guarantee, and cost.
- [[collaborative-beamforming-in-aerial-mec]] — Target / objectives / solver split across the 5 collaborative-beamforming sources.
- [[mobility-asynchrony-and-geometry-in-aerial-coverage]] — Mobility prediction, timing/path-delay asynchrony, cooperation scope, and geometry mapped without conflating coverage metrics.
- [[constraint-regimes-in-uav-data-collection]] — Energy, deadline, freshness, connectivity, kinematic, and information-quality constraints compared without ranking incompatible metrics.
- [[hardware-validation-and-sim-to-real-in-mec]] — What "hardware-validated" means across the few non-simulation sources, and the sim-to-real challenges they name.

## References

- [[reference-database]] — master citation-mining database (5054 unique references mined from the corpus parses; centrality ranking by in-corpus `cited_count`).
- [[recommendations]] — reference-scout recommendations: cited-but-not-yet-curated papers ranked by recency, venue, in-corpus citation frequency, and track coverage.
