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

### Foundational DRL methods

- [[mnih-2015-dqn-atari]] — Mnih et al. 2015. Origin paper for **DQN** — deep convolutional Q-learning with experience replay + target network; human-level Atari across 49 games with same architecture/hyperparameters (Nature).
- [[fujimoto-2018-td3-actor-critic]] — Fujimoto et al. 2018. Origin paper for **TD3** — clipped double-Q + delayed policy updates + target smoothing to curb actor-critic overestimation (ICML).
- [[schulman-2017-ppo]] — Schulman et al. 2017. Origin paper for **PPO** — clipped surrogate objective enabling multi-epoch first-order policy updates with TRPO-like stability (OpenAI; arXiv, venue/DOI not in parse).
- [[lillicrap-2016-ddpg-continuous-control]] — Lillicrap et al. 2016. Origin paper for **DDPG** — off-policy actor-critic bringing DQN's replay + target networks to deterministic continuous control; soft target updates + OU exploration (ICLR; DOI/venue not in parse).
- [[van-hasselt-2016-double-dqn]] — van Hasselt et al. 2016. Origin paper for **Double DQN** — decouples action selection from evaluation (reusing the target network) to curb DQN's value over-estimation; SOTA Atari (AAAI; DOI/venue not in parse).
- [[xiang-sac-mapless-robot-navigation]] — Xiang et al. Mapless mobile-robot navigation via **Soft Actor-Critic** (LSTM value/Q nets); laser+target→velocity continuous control (venue/year not in parse).

### Joint trajectory / caching / migration

- [[zhao-2025-traj-offload-cache-migration]] — Zhao et al. 2025. Joint trajectory + offloading + migration + **computational-task caching**; Lyapunov + BCD + QCQP-SDR.
- [[gao-2024-service-experience-cache-uav]] — Gao & Zhai 2024. Fairness-aware cache-enabled UAV-MEC; **service-experience ratio** (Jain's index / delay); Dinkelbach + 4-stage AO.
- [[zhao-2024-caching-service-placement-uav]] — Zhao et al. 2024. Joint content caching + service placement + offloading; QoE max via Gibbs sampling + matching.
- [[chen-2024-dro-video-caching]] — Chen et al. 2024. **Distributionally robust** adaptive-bitrate video caching + transcoding + backhaul in UAV-MEC; ζ-structure-metric confidence set + convex DRO latency minimizer under an energy budget; real YouTube traces (IEEE TMC).
- [[huang-2026-erasure-coded-uav-storage]] — Huang et al. 2026. **Erasure-coded UAV edge storage**; coded data/parity block placement + access routing in post-disaster UAV-enabled edge systems via CNN+ConvLSTM prediction and ME-HDRL (DDQN UAV agents + PPO edge agent) (IEEE TMC).
- [[du-2023-maddpg-service-placement-agin]] — Du et al. 2023. **MADDPG** joint service placement + offloading in air-ground integrated MEC.

### Game-theoretic offloading & allocation

- [[xu-2026-prizty-uav-mec-auction]] - Xu et al. 2026. **Prizty** privacy-preserving reverse auction for UAV-assisted MEC task offloading/resource allocation; UE location obfuscation + trajectory-aware feasible service sets + winner/payment selection (IEEE TMC).

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
- [[zhai-2026-collaborative-inference-uav-mec]] — Zhai et al. 2026. Multi-UAV DNN inference offloading; OPPS partition-point selection + fairness matching + TD3 trajectory/transmit-power control (IEEE T-ITS).
- [[shi-2026-aoi-active-ris-noma-agmec]] - Shi et al. 2026. **AoI-aware active-RIS + NOMA air-ground MEC**; joint UAV trajectory, active-RIS beamforming, and UE offloading via AADDPG with an action adjuster and battery-protection rule (IEEE TWC).
- [[liu-2026-lyapunov-diffusion-uav-vehicular]] - Liu et al. 2026. UAV-assisted vehicular V2X with **delayed CSI feedback**; Lyapunov energy queue + diffusion-actor DDPG (**D3PG**) over V2V channel reuse, power control, and UAV altitude (IEEE TWC).
- [[tong-2026-uneven-terrain-uav-mec]] — Tong et al. 2026. Uneven-terrain UAV-MEC with service coverage, partial UAV/BS task allocation, propulsion energy, and safe 3D flight; PH-DRL separates TD3 flight control from actor-critic task allocation (IEEE TMC).

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
- [[raivi-2024-jdaco-postdisaster-iot]] — Raivi & Moh 2024. **JDACO** — joint data aggregation + computation offloading for multi-UAV **post-disaster** IoT; two-tier LT-UAV/HT-UAV; minimize aggregation+offload energy/delay + max IoT coverage; **VD3QN** (dueling double DQN + value-decomposition network); +20% training-time / +11.4% data / +5.6% energy-eff / +11.2% mission-duration, up to 98% devices served (IEEE IoT-J).
- [[sun-2024-ues-video-analytics-disaster]] — Sun et al. 2024. **Battery-aware** UAV-edge-server collaborative **video analytics** for **disaster rescue**; differential-evolution per-slot offloading + **DDQN** trajectory planning; doubles the smart-camera-network lifetime (IEEE TVT).
- [[gao-2024-d3qn-uav-mec-mobile-gt]] — Gao et al. 2024. **3D** UAV-MEC for **mobile** ground terminals in a **post-disaster** urban scenario; collect→compute→deliver total-time minimization over UAV 3D trajectory + GT scheduling, with **obstacle avoidance** among buildings + **probabilistic-LoS** channel; MDP + **multi-step dueling DDQN (D3QN)**; 3D beats 2D, robust to GT mobility / height limits (IEEE TVT).

### Classical / convex / optimization-based UAV-MEC

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
- [[zhan-2020-completion-time-energy-uav-mec]] — Zhan et al. 2020. Single **fixed-wing** UAV-MEC server; joint offloading + resource allocation + trajectory + **completion time**, minimizing UAV **energy** and **completion time** separately and tracing their **Pareto** tradeoff; path discretization + AO + **SCA** (IEEE IoT-J).

### SAGIN / satellite offloading

- [[tun-2025-thz-sag-mec-resource-allocation]] - Tun et al. 2025. THz-assisted MEC-enabled SAG networks; BCD over device offloading, THz sub-band/power control, UAV deployment, and UAV-to-UAV/LEO task forwarding (IEEE TMC).

- [[chen-2026-pddqn-sagin-mec]] - Chen et al. 2026. MEC-enabled SAGIN with local/UAV/LEO partial offloading; P-DDQN couples device/satellite association with transmit power, task ratios, and UAV 3D trajectory under LEO coverage-time constraints (IEEE TWC).

- [[zhao-2026-hcdrl-ga-sagin-sar]] - Zhao et al. 2026. Multi-UAV SAR in SAGIN; HCDRL/HCSAC trajectory/offloading with CNN+GCN state encoding plus GA deployment search under NOAA-derived wind fields (IEEE TMC).

- [[cheng-2019-sagin-iot-offloading-rl]] — Cheng et al. 2019. **First SAGIN computing-offloading** paper for remote IoT; UAV edge + satellite cloud; MDP + **actor-critic RL** offloading + heuristic VM allocation (IEEE JSAC).
- [[zhou-2021-delay-sagin-task-scheduling]] — Zhou et al. 2021. Delay-oriented IoT task scheduling in SAGIN; UAV collects tasks and schedules local / BS / LEO execution via deep risk-sensitive RL with separate delay-cost and energy-risk Q-functions (IEEE TWC).
- [[liu-2024-sagin-spherical-sg-connectivity]] — Liu et al. 2024. **Spherical stochastic geometry** uplink path connectivity analysis for SAGIN; GUs + AVs on spherical surfaces; three connectivity metrics; first such model (IEEE JSAC).
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

### IRS / THz / anti-jamming

- [[wu-2026-model-based-ppo-ris-uav-mec]] - Wu et al. 2026. RIS-assisted urban multi-UAV MEC with decentralized model-based PPO; local k-hop observations, RIS phase proposals, and branched rollouts for trajectory/offloading control (IEEE TMC).

- [[qin-2023-ris-uav-mec-ee]] - Qin et al. 2023. RIS-assisted UAV-MEC energy efficiency with NOMA; Dinkelbach + BCD/DC/SCA over task bits, power, RIS phase shifts, and UAV trajectory under imperfect CSI (IEEE TGCN).

- [[chhea-2025-irs-uav-swipt-drl]] — Chhea et al. 2025. IRS-aided UAV **SWIPT** network; **DRL** with SINR-map reward maximizes average EE over trajectory + IRS phase shifts + transmit power + PS ratio (IEEE TVT).
- [[wu-2025-gai-ris-resource-management]] — Wu et al. 2025. **GAI + distributional RL (DBRL)** for RIS-aided 6G resource management; CDL cascade channel estimation + GAN-modeled distributional Q-function; maximizes joint EE + QoSSR (IEEE TCCN).
- [[wu-2025-iopo-irs-uav-thz-mec]] — Wu et al. 2025. **IRS-assisted** multi-UAV THz MEC; two-stage IOPO (order-preserving offloading + WOA phases).
- [[shao-2024-drl-antijamming-mec]] — Shao et al. 2024. **Anti-jamming** UAV-MEC resource management; PER-MATD3 (hardware-validated).
- [[sun-2024-mfris-semantic-antijamming]] — Sun et al. 2024. **Multi-functional RIS** + **semantic** anti-jamming communication & computing for aerial-ground MEC; worst-case CSI; semantic-computation-rate max via monotonic optimization + DSOCP (+ GPI) (IEEE JSAC).
- [[sun-2024-active-passive-ris-receiver]] — Sun et al. 2024. **Active-passive cascaded RIS** receiver architecture for anti-jamming; worst-case rate max under imperfect angular jammer CSI via UM-ZF (passive) + AMM/C-M-CCD (active) semi-closed-form solutions (IEEE TWC). *(Physical-layer RIS-receiver anchor, not MEC.)*
- [[guo-2024-multiuav-proactive-eavesdropping]] — Guo et al. 2024. **Multi-UAV proactive eavesdropping** (legitimate surveillance): full-duplex UAVs jam multiple mobile suspicious links while planning trajectories; MDP decoupled into a closed-form **jamming-power solver** + per-UAV decentralized **RL moving policy** (IEEE TMC). *(Surveillance/PLS anchor, not MEC.)*

### UAV-swarm collaborative computing

- [[sun-2024-asap-uav-swarm]] — Sun et al. 2024. **ASAP** — in-swarm collaborative DL inference (model + data partition, pipeline-parallel); hardware-validated.
- [[qu-ecoei-uav-swarm]] — Qu et al. **eCoEI** — elastic OODA-loop collaborative DL inference for UAV swarms, robust to node/A2A-link failure; proof-of-concept on Jetson devices (IEEE Communications Magazine; year not in parse).
- [[li-2025-stochastic-game-uav-swarm]] — Li et al. 2025. Energy-efficient UAV-swarm MEC as five **stochastic games** with dynamic clustering; RLDC multi-agent Q-learning.
- [[li-2025-dt-uav-swarm-resource-management]] — Li et al. 2025. Digital-twin-based task-driven UAV-swarm resource management for search and rescue; MADRL task crowdsourcing plus SNC traffic-flow delay bounds (IEEE T-ITS).
- [[jia-2026-ufsp-rail-inspection]] — Jia et al. 2026. Multi-UAV rail-line inspection under imperfect information; stochastic potential game + U-FSP belief-augmented Q-learning / policy averaging, with small-scale real-world deployment evidence (IEEE T-ITS).
- [[li-2024-rldc-uav-swarm-clustering]] — Li et al. 2024. **Conference precursor** of the above (IEEE WCNC 2024); six stochastic games + RLDC, no NE/convergence proof.
- [[zhang-2020-response-delay-uav-swarm]] — Zhang et al. 2020. **Response-delay** optimization for a MEC-enabled UAV swarm (T-UAV + B-UAVs); **stochastic geometry** + **queueing theory** closed-form delay; **hardware-validated** (2 DJI M100 + 5G NR mmWave) (IEEE TVT).

### Generative-AI MEC

- [[wen-2026-hybridrag-low-carbon-lae]] - Wen et al. 2026. HybridRAG-formulated low-carbon LAE network optimization with R^2DSAC, a double-regularized diffusion-enhanced SAC solver (IEEE TMC).
- [[cai-2026-llm-drl-secure-lae-data]] - Cai et al. 2026. LLM-enhanced DRL for secure LAE data collection; LLM state/reward/simulator support for DDPG/TD3 with a data-collection UAV and a jamming UAV (IEEE TMC).
- [[wang-2026-llm-qos-multiuav-resource]] - Wang et al. 2026. LLM teacher-student QoS-aware resource allocation for multi-UAV cooperative edge computing; NKG/R-GAT/ToT teacher with MAPPO student distillation (IEEE TMC).
- [[wang-2026-lifelong-semantic-content-reuse]] — Wang et al. 2026. UAV-assisted Metaverse semantic content reuse; semantic subject/object caching plus DC-ELLA lifelong policy transfer for changing semantic environments (IEEE TMC).
- [[wang-2026-diffusion-semantic-uav-edge]] — Wang et al. 2026. UAV-assisted semantic edge computing; H-DDPG plus convex semantic-resource optimization, then diffusion-denoising DDPG for trajectory action generation (IEEE TWC).
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

- [[chen-2026-hc-mappo-vehicle-twin-migration]] - Chen et al. 2026. Hierarchical-control MAPPO for vehicle-twin migration in UAV-assisted vehicular metaverses, using ACB-LSTM workload prediction and deterministic lower-layer migration mapping (IEEE TMC).
- [[wei-2026-airfogsim-uav-vfc]] - Wei et al. 2026. **AirFogSim** lightweight modular simulator for UAV-integrated vehicular fog computing; traffic/UAV mobility, communication, computation, energy, security/privacy, blockchain, and scheduling modules (IEEE TMC).
- [[qi-2026-drone-vehicle-mec-inspection]] - Qi et al. 2026. Cooperative drone-vehicle MEC for low-altitude inspection; GV-carried accompanying/detached drones, battery swapping, route planning, and detached-drone speed optimization minimize mission completion time (IEEE TMC).

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
- [[li-2023-secure-marine-iot-jamming]] — Li et al. 2023. **Secure** marine-IoT offloading: USVs upload to a **HAP** via NOMA then provide **cooperative jamming**; system-energy min via monotonic optimization (PAS) + cross-entropy (CASE) (IEEE TVT).
- [[lu-2023-uav-relay-secure-maritime-mec]] — Lu et al. 2023. **UAV-relay-assisted secure maritime MEC** with a **flying eavesdropper**; a relay UAV amplify-and-forwards maritime-device tasks to a coastal edge server while a **coastal jammer** disrupts an eavesdropping UAV; **max-min secure computing capacity** over transmit power + time-slot + local-computation + UAV trajectory; non-convex → **BCD + SCA** (IEEE TCOMM).
- [[zeng-2024-usv-fleet-collaborative-offloading]] — Zeng et al. 2024. UAVs offload tasks **to USV fleets**; first-price sealed **reverse auction** (reserve price) incentive + symmetric-equilibrium bidding, then BCD + improved **ADMM** energy minimization (IEEE TVT).
- [[liu-2022-maritime-uav-mec-virtualization]] — Liu et al. 2022. Two-layer maritime UAV-MEC (T-UAV MEC server over B-UAVs) with **VM-multiplexing** parallel computing under I/O interference; latency min via DQN + DDPG over T-UAV trajectory + VM count (IEEE TVT).
- [[li-2020-maritime-uav-satellite-coverage]] — Li et al. 2020. **Coverage enhancement** of a hybrid satellite-UAV-terrestrial maritime network; a **fixed-wing UAV** shares spectrum with satellites and uses TBS/satellite backhaul; jointly optimizes pre-planned **trajectory + in-flight transmit power** to **max-min ergodic rate** using only **location-dependent large-scale CSI** (AIS-derived ship positions); non-convex → decomposition + SCA + bisection (IEEE TCOMM). *(Maritime communication-layer coverage, not MEC offloading.)*

### Trust, security, and federated MEC

- [[zhou-2026-cpsfl-uav-foundation-models]] - Zhou et al. 2026. Communication-pipelined split federated learning for LoRA fine-tuning of foundation models in UAV networks; sequential downlink gradient transmission plus attention-based DRL split/resource decisions (IEEE TMC).
- [[mao-2025-bcsa-frl]] — Mao et al. 2025. Blockchain-enabled cold-start FRL for ZT LEO satellite networks. *BCSA-FRL* (CCVM + CSRA).
- [[mao-2025-irs-noma-fl-secrecy]] — Mao et al. 2025. **IRS-assisted** secrecy-rate maximization for **NOMA-based federated-learning** model aggregation; max-min secrecy rate over device power + IRS phase shift via **DDPG** (IEEE TCCN).
- [[qin-2025-bcuav-masac]] — Qin et al. 2025. Blockchain-enabled secure UAV-MEC: Lyapunov + MASAC + DOA.
- [[benaya-2025-aerial-isac-haps]] — Benaya et al. 2025. HAPS-mounted FD ISAC + friendly-jamming UAV + ground MEC; AO + SDR + SCA.
- [[wang-2026-blockchain-lae-fl-mappo]] — Wang et al. 2026. Blockchain-assisted low-altitude edge-intelligence network; UEs/TUAVs/SUAVs/BS four-layer offloading+caching+FL stack, FL-MAPPO-BOCRAOA, PV-aware throttling, M/M/1 queueing, and blockchain-supported cache cooperation (IEEE TMC).
- [[wang-2025-acbft-uav-consensus]] — Wang et al. 2025. **ACBFT** — PSO-ordered chain-based Byzantine fault-tolerant consensus for UAV ad hoc networks.
- [[wang-2024-blockchain-uav-mec-dpos]] — Wang et al. 2024. **Blockchain-integrated** UAV-assisted MEC; improved **DPoS** consensus (UAV light nodes + reputation-voted ground full nodes) + two-stage **Stackelberg** game over trajectory and resource allocation, solved with SCA (IEEE TVT).

### ISAC, sensing & physical-layer security

- [[zhao-2026-mappo-jscc-aec]] - Zhao et al. 2026. HAP-assisted multi-UAV sensing-communication-computing; Lyapunov energy stability plus MAPPO-JSCC with embedded sensing, SCA, and Dinkelbach solvers (IEEE TWC).

- [[huang-2026-offgrid-lae-imager]] - Huang et al. 2026. Cooperative cellular-ISAC low-altitude imaging; CS/PSF analysis plus physics-embedded DNN/OHEM off-grid reconstruction from CSI, reporting up to 97.55% detection rate in the parsed ablation (IEEE TWC).
- [[hou-2025-pbia-air-iscc-uav-its]] - Hou et al. 2025. UAV-swarm Air-ISCC for ITS; PBIA/PPO jointly controls sensing time, power, service association, and compute allocation to balance success rate and UAV energy (IEEE TGCN).

- [[li-2023-adaptive-digital-twin-uav-iscc]] - Li et al. 2023. DT-enabled UAV-assisted ISCC; ATB-MAPPO with Beta-policy actors and attention critics for radar beampattern / energy tradeoff (IEEE TGCN).
- [[tang-2025-cooperative-isac-lae]] - Tang et al. 2025. Cooperative ISAC for low-altitude economy; tensor-decomposition monostatic estimation, false-removing MST association, Pareto position fusion, and residual-weighted velocity estimation (IEEE TWC).
- [[ye-2026-meta-deepesc-lae-isac]] - Ye et al. 2026. Meta-DeepESC for energy-efficient LAE ISAC; TD3-style constrained action selection, episodic replay, and meta-learning for GBS beamforming plus authorized-UAV trajectories (IEEE TMC).
- [[ye-2026-deeplsc-lae-isac]] - Ye et al. 2026. DeepLSC LAE ISAC; DDPG-based joint GBS beamforming and UAV-trajectory control with constrained noise exploration, hierarchical replay, and symmetric experience augmentation (IEEE TWC).
- [[zeng-2026-fmcw-isibc-lae]] — Zeng & Liang 2026. **FMCW-enabled integrated sensing, identification, and backscatter communication** for LAE; UAV-mounted BDs modulate identity symbols onto FMCW echoes, with SVD-based range/velocity/symbol estimation and CRLB analysis (IEEE TWC).

- [[qin-2025-urllc-noma-uav-iscc]] — Qin et al. 2025. **NOMA-aided UAV ISCC** with URLLC: sensing + communication + computation; Lyapunov tail-constraint + **SAC-TPBD** DRL; comparable to SCA/SDR baselines with higher efficiency (IEEE TVT).
- [[tang-2024-iscc-uav-feel]] — Tang et al. 2025. **ISCC** for UAV-assisted federated edge learning; deployment + sensing/compute/comm via AO (BBPO).
- [[wang-2024-ttw-amd-localization]] — Wang et al. 2024. **Through-the-wall (TTW)** passive AMD detection + localization via CSI; reference-channel SSI cancellation + 2D matrix pencil ToF/PLCR estimation; hardware-validated (glass/brick walls: 0.964/0.952 detection accuracy, 1.65/2.05 m median error) (IEEE JSAC).
- [[yao-2025-secure-isac-dual-eavesdropping]] — Yao et al. 2025. Secure UAV-ISAC against dual eavesdropping; AO + SCA + SDR for secrecy + sensing security.
- [[chen-2024-three-party-hierarchical-game-pls]] — Chen et al. 2024. **Three-party hierarchical game** for PLS with dynamic trilateral coalitions (LUs / EVs / JAs); HCSF + DRL (IEEE TWC).
- [[wang-2026-secure-lae-uav-scheduling]] — Wang et al. 2026. Secure low-altitude aerial communications; UAVs dynamically switch between communication and artificial-noise jamming roles while optimizing scheduling, power, 3D trajectory, and velocity for secrecy energy efficiency (IEEE TWC).
- [[michailidis-2024-secure-ris-uav-mec-iot]] — Michailidis et al. 2024. Secure UAV-**RIS**-MEC-IoT offloading against **aerial + ground eavesdroppers**; SOP over Nakagami-m + max-min **secure computation efficiency** via Dinkelbach + BCD + bisection (IEEE TCOMM).
- [[su-2024-sensing-aided-isac-pls]] — Su et al. 2024. **Sensing-aided PLS** for ISAC: dual-functional BS estimates eavesdropper directions (CAML) then jointly minimizes CRB and maximizes AN-aided secrecy rate via AO + fractional programming (IEEE TWC).
- [[wen-2024-iscc-edge-ai]] — Wen et al. 2024. **Task-oriented ISCC** for multi-device **edge-AI inference**: ISAC devices radar-sense multi-view data, quantize + offload features to an edge server running split inference; maximize **discriminant gain** (KL-divergence accuracy surrogate) over sensing/transmit power + comm time + quantization bits; non-convex but solved **optimally** by the **sum-of-ratios** method (IEEE TWC).
- [[zhu-2024-sensing-comm-doppler-uav-swarm]] — Zhu et al. 2024. **Sensing-communication co-design** for UAV-swarm-assisted vehicular networks in perspective of **Doppler**; min-max GV **CRLB** under SNR-loss constraint via differential evolution (IEEE TVT).
- [[chu-2024-secure-ris-isac]] — Chu et al. 2024. **Secure RIS-ISAC** correspondence; maximize radar output SNR under per-user comm SINR + eavesdropping-SINR ceiling + power + RIS unit-modulus; AO + SDR + fractional programming + **majorization-minimization**; ~2 dB radar gain vs no-RIS (IEEE TVT). *(PHY secure-ISAC anchor, not MEC.)*
- [[zhu-2024-crb-active-ris-isac]] — Zhu et al. 2024. **Active-RIS-empowered ISAC** for an obstructed target; derives the **CRB** for target **DoA** estimation and minimizes it over BS precoding + active-RIS reflection beamforming under per-user SINR + BS/RIS power + RIS amplitude constraints; AO + SDR + **majorization-minimization**; >30 dB CRB reduction vs passive RIS (IEEE TWC). *(PHY active-RIS ISAC anchor, not MEC.)*
- [[zhao-2018-caching-uav-ia-secure]] — Zhao et al. 2018. **Caching-UAV secure transmission** in hyper-dense small cells; **interference alignment** (SBS precoding) for single-antenna UAVs + idle SBSs repurposed as zero-forced **friendly jammers** against a passive eavesdropper; feasibility + secrecy analysis (IEEE TCOMM). *(Caching + interference-alignment PLS anchor, not MEC offloading.)*
- [[zhu-2024-zdrl-uav-tracking]] — Zhu et al. 2024. **Collaborative-RL 3D UAV tracking**; one active + four passive UAVs localize a target via TDOA/TSWLS; joint power + trajectory design via **Z-function-decomposition RL** (distributional RL); up to 39.4% / 64.6% lower positioning error vs VD-RL / independent DRL (IEEE TMC). *(UAV localization + trajectory design, not MEC offloading.)*
- [[an-2024-multilayer-ris-hap-swipt]] — An et al. 2024. **Multi-layer refracting RIS-assisted receiver** enabling **SWIPT** over long-distance **HAP** links; worst-case sum-rate max under imperfect angular CSI + non-linear EH; scalable toolbox-free robust optimization (CSI discretization + **LogSumExp-dual** precoder + **M-CCD** RIS coefficients + closed-form PS/decoder) (IEEE TWC). *(PHY RIS-receiver / SWIPT anchor, not MEC offloading.)*
- [[ma-2024-covert-mmwave-finite-blocklength]] — Ma et al. 2024. **Covert mmWave communication with finite blocklength** against **spatially random wardens** (Willies as a PPP); derives covertness-constraint + **average effective covert throughput (AECT)** expressions for **phased-array (PA)** and **linear frequency diverse array (LFDA)** beamforming via **stochastic geometry**, then jointly optimizes transmit power + blocklength; the best scheme (PA vs LFDA) depends on the receiver's direction (IEEE IoT-J). *(Covert-communication / PHY-security anchor, not MEC.)*

### Collaborative beamforming & aerial communications

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
- [[zeng-2026-movable-antenna-u2u-channel]] - Zeng et al. 2026. Movable-antenna-aided MIMO wideband UAV-to-UAV channel model for LAE; closed-form STF-CF/SD-PSD/PSDS plus gradient log-det antenna-position optimization (IEEE TWC). *(Channel-model anchor, not MEC offloading.)*

### Architectural / spectrum / governance

- [[chen-2026-cargo-uav-pickup-lae]] - Chen et al. 2026. Cellular-connected cargo-UAV pickup in the low-altitude economy; CACMO combines D3QN trajectory learning, simulated annealing sequence planning, and collision-aware refinement (IEEE TMC).
- [[zhang-2026-uav-task-path-lu-its]] — Zhang et al. 2026. Cooperative task allocation and collision-free path planning for multi-UAV low-altitude urban intelligent transportation systems; ILLA potential-game allocation + CBMBA A-Star path search (IEEE T-ITS).
- [[wang-2025-uav-swarm-stackelberg]] — Wang et al. 2025. Stackelberg-game spectrum sharing for U2U/U2B in UAV swarms.
- [[wang-2025-lae-network-survey]] — Wang et al. 2025. Survey: low-altitude economy network architecture, integrated technologies, and future directions.
- [[jiang-2025-isac-lae-overview]] — Jiang et al. 2025. ISAC for LAE — IAGN architecture, MBCM channel model, stochastic-geometry analysis.
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

- [[zeng-2017-energy-efficient-uav-trajectory]] — Zeng & Zhang 2017. **Energy-efficient UAV communication** via trajectory optimization; first **fixed-wing propulsion-energy model** (speed + acceleration) + bits/Joule energy-efficiency; circular + generally-constrained SCA trajectories (IEEE TWC). *(UAV-communications anchor, not MEC.)*
- [[zeng-2016-throughput-relaying]] — Zeng et al. 2016. **UAV mobile relaying** throughput maximization; joint relay trajectory + source/relay power; "staircase" water-filling power structure + SCA trajectory under **information-causality** (IEEE TCOMM). *(UAV mobile-relaying anchor, not MEC.)*
- [[zhao-2019-uav-emergency-disasters]] — Zhao et al. 2019. **UAV-assisted emergency networks** in disasters (magazine framework): joint trajectory+scheduling with surviving BSs, multihop D2D coverage extension, and multihop UAV relaying (AF/DF) — IEEE Wireless Communications. *(Post-disaster comms framework, not a single MEC formulation.)*
- [[bor-yaliniz-2016-3d-abs-placement]] — Bor-Yaliniz et al. 2016. First **3-D placement** of a drone-cell (aerial base station): jointly choose altitude + coverage location/size to maximize covered users; quadratically-constrained MINLP via bisection + interior-point solver (IEEE ICC). *(Aerial-base-station deployment anchor, not MEC.)*
- [[jiang-2012-uav-heading-sdma]] — Jiang & Swindlehurst 2012. Multi-antenna fixed-wing UAV heading optimization for ground-to-air **SDMA** uplink; adaptive heading maximizes ergodic sum rate via prediction filter + line search; SDMA >> TDMA (IEEE JSAC). *(Multi-antenna UAV relay / heading-optimization anchor.)*
- [[lyu-2017-spiral-mbs-placement]] — Lyu et al. 2017. **Minimum-count UAV-MBS placement** as the NP-hard **Geometric Disk Cover** problem; a polynomial-time **spiral** algorithm places base stations along the convex-hull perimeter of uncovered ground terminals and nudges inward; near core-sets-optimal on small instances, beats strip-based/K-means/random (IEEE COMML). *(Aerial-base-station deployment anchor, not MEC.)*
- [[zeng-2016-uav-comm-opportunities-challenges]] — Zeng et al. 2016. **Magazine overview** of UAV-aided wireless communications: networking architecture, air-to-ground LoS channel characteristics, three use cases (ubiquitous coverage / relaying / data collection), and design challenges (CNPC links, dynamic topology, SWAP constraints, interference coordination) (IEEE Communications Magazine). *(Foundational UAV-comms overview, not MEC.)*
- [[zhan-2011-uav-relay-heading-optimization]] — Zhan et al. 2011. **Earliest UAV-comms source** — multi-UAV relays connect ground APs to a BTS on the uplink; defines the **ergodic normalized transmission rate (ENTR)**, approximates it as a **sinusoid** in UAV heading → closed-form optimal heading, plus an adaptive **handoff** algorithm + new-relay deployment for the mobile topology (IEEE TAES). *(UAV mobile-relaying / heading-control anchor, not MEC.)*
- [[mozaffari-2016-uav-underlaid-d2d]] — Mozaffari et al. 2016. UAV downlink base station **coexisting with an underlaid D2D network**; **stochastic-geometry** coverage / sum-rate analysis for static + mobile UAV; optimal altitude (decreasing in D2D density), **disk-covering** minimum stop-points for full coverage, and the **coverage-vs-delay / D2D-outage** tradeoff (IEEE TWC). *(Aerial-base-station + D2D coexistence anchor, not MEC.)*
- [[mozaffari-2019-drone-antenna-array]] — Mozaffari et al. 2019. **Drone-based antenna array** that beam-steers by **physically repositioning** the drones; minimum-**service-time** design = transmission time (perturbation-theory drone-spacing directivity max) + control time (**bang-bang** closed-form minimum control time under wind/gravity); +32% spectral efficiency vs fixed uniform array (IEEE TCOMM). *(UAV-communications / aerial-beamforming anchor, not MEC.)*

## Entities

### Authors

- [[dusit-niyato]] (NTU) appears across 37 sources after the movable-antenna U2U-channel paper; [[xuemin-shen]] (Waterloo) appears across 14 sources after the AoT UAV-inspection paper; [[ning-zhang]] (Windsor) appears across 4 sources after the adaptive digital-twin UAV-ISCC paper.

- [[lihan-liu]], [[hongrui-miao]], [[chunhui-qu]], [[zhuwei-wang]], [[haijun-zhang]], [[zhidu-li]] — co-authors of [[liu-2026-jppo-en-convntm]].
- [[chaoda-peng]], [[xumin-huang]], [[yuan-wu]], [[jiawen-kang]] — recurring co-authors across the [[cmop-evolutionary-uav-mec-lineage|CMOP-evolutionary UAV-MEC lineage]] (4–6 sources each).
- [[hao-hao]] — first author of the two priority-aware offloading sources ([[hao-2024-clp-multiuav-priority-offloading]], [[hao-2025-priority-aware-task-driven-co]]).
- [[geng-sun]] — recurring (co-)author across 20 Jilin-University / NTU aerial-MEC sources, including collaborative beamforming, low-altitude-economy surveying, and [[he-2026-dt-sagimec-lae]].
- **Jilin-University / NTU aerial-MEC cluster:** [[zemin-sun]], [[jiahui-li]] (Jilin University), [[jiacheng-wang]], [[dusit-niyato]] (NTU), [[victor-c-m-leung]], and [[qingqing-wu]] (Shanghai Jiao Tong University).
- **NUAA aerial-computing cluster:** [[ziye-jia]], [[chao-dong]], [[qihui-wu]] (NUAA), [[zhu-han]] (Univ of Houston / Kyung Hee), spanning HAP/UAV MEC, maritime AAV cooperation, and [[jia-2026-dro-lawn-trajectory]].
- **Dalian-Maritime-University maritime cluster:** [[bin-lin]] (DMU), [[zhen-wang]] (DMU / Dalian Neusoft), [[qiang-ye]] (Univ of Calgary).
- **NWPU non-terrestrial-network cluster:** [[bomin-mao]], [[hongzhi-guo]], [[jiajia-liu]] (Northwestern Polytechnical University).
- **Virginia Tech (Wireless@VT) UAV-communications cluster:** [[mohammad-mozaffari]], [[walid-saad]] — foundational UAV-as-aerial-base-station + 3D-deployment works (2 sources each).
- **NCEPU aerial-edge cluster:** [[peng-qin]], [[yang-fu]] (North China Electric Power University); [[jingjing-wang]] (Beihang University) links the blockchain-UAV thread.
- **South-China-Agricultural-University evolutionary UAV-MEC cluster:** [[zexiong-wu]] (with [[chaoda-peng]], [[xumin-huang]], [[yuan-wu]]).
- **Cross-cutting seniors:** [[chunxiao-jiang]] (Tsinghua), [[tony-q-s-quek]] (SUTD).
- [[ying-chen]] (Beijing Information Sci. & Tech. Univ. — online + game-theoretic offloading), [[jie-xu]] (CUHK-Shenzhen — ISAC), [[fuhong-song]] (SWJTU → Guizhou Univ. of Finance & Economics — evolutionary MORL), [[yong-wang]] (Central South Univ. — constrained/evolutionary optimization), [[wei-zhang]] (Shandong Computer Science Center — task-priority offloading, [[hao-hao]] group).
- [[shuang-liang]] (Northeast Normal Univ. — aerial-MEC / LAE, [[geng-sun]] cluster), [[weifeng-zhong]] & [[shengli-xie]] (Guangdong Univ. of Technology — CMOP-evolutionary lineage), [[qiqi-xie]] (South China Agricultural Univ. — evolutionary UAV-MEC), [[nei-kato]] (Tohoku Univ.), [[jiadai-wang]], [[yijie-xun]], [[yangbo-liu]] (Northwestern Polytechnical Univ. — NTN cluster, [[bomin-mao]] group).
- [[boxiong-wang]] & [[hui-kang]] (Jilin University — [[geng-sun]] aerial-MEC cluster; 2 sources each).
- [[yuben-qu]] & [[hao-sun]] (Nanjing Univ. of Aeronautics and Astronautics — UAV-swarm collaborative-inference cluster with [[chao-dong]]/[[qihui-wu]]; 2 sources each — [[qu-ecoei-uav-swarm]] + [[sun-2024-asap-uav-swarm]], identical `@nuaa.edu.cn` emails).
- [[kezhi-wang]] (Northumbria Univ. — UAV-MEC trajectory/offloading group; 3 sources), [[xuemin-shen]] (Univ. of Waterloo — MEC resource management; 3 sources), [[yuguang-fang]] (City Univ. of Hong Kong — maritime MEC, [[bin-lin]] cluster; 2 sources), [[haixia-peng]] (Univ. of Waterloo → Xi'an Jiaotong Univ. — vehicular + maritime MEC; 2 sources, affiliation move documented in both parses).
- [[liping-qian]] (Zhejiang Univ. of Technology — NOMA / multi-access marine MEC; 3 sources), [[minghui-dai]] (Univ. of Macau — marine multi-access offloading; 3 sources, `minghuidai@um.edu.mo`), [[zhiyong-feng]] (Beijing Univ. of Posts and Telecommunications — UAV-swarm MEC + UAV-ISAC; 2 sources).
- [[shichao-li]] & [[hongbin-chen]] (Guilin Univ. of Electronic Technology — two-hop air-ground IoRT MEC, `@guet.edu.cn`-matched; 2 and 3 sources), [[mianxiong-dong]] (Muroran Inst. of Technology; 2 sources) & [[ning-zhang]] (Univ. of Windsor; 2 sources) — co-authors across the IoRT + robust-multi-UAV DRL offloading thread, [[victor-c-m-leung]] (Shenzhen MSU-BIT / Shenzhen Univ. / UBC, `vleung@ieee.org`; 9 sources in the [[geng-sun]]/[[dusit-niyato]] aerial-MEC cluster).
- [[zhou-su]] (Xi'an Jiaotong Univ. — maritime/vehicular edge computing; 2 sources, corresponding author of [[zeng-2024-usv-fleet-collaborative-offloading]]), [[yanheng-liu]] (Jilin Univ. — [[geng-sun]] aerial/vehicular-MEC cluster; 2 sources).
- [[kaoru-ota]] (Muroran Inst. of Technology, `ota@csse.muroran-it.ac.jp` — with [[mianxiong-dong]]; 2 sources, blockchain-secured + air-ground IoRT UAV-MEC). [[mianxiong-dong]] is now at 3 sources (+[[wang-2024-blockchain-uav-mec-dpos]]).
- [[dong-jun-han]] & [[christopher-brinton]] (Purdue University — non-terrestrial **federated-learning** offloading cluster with Mung Chiang / David J. Love / Seyyedali Hosseinalipour; 2 sources each — [[han-2024-ground-satellite-fl]] + [[han-2024-sagin-fl-handover]]).
- [[yong-zeng]] (National University of Singapore — **UAV-communications / trajectory-optimization** foundations; 5 sources: [[zeng-2016-throughput-relaying]], [[zeng-2017-energy-efficient-uav-trajectory]], [[zeng-2019-rotary-wing-energy-min]], [[zeng-2019-uav-comm-tutorial-5g]], [[wu-2018-multiuav-minrate-trajectory]]).
- [[shuguang-cui]] (The Chinese University of Hong Kong, Shenzhen — physical-layer / edge-AI / surveys; 7 sources spanning the graph-based-resource-management two-part survey, XL-MIMO, generative-AI/ISAC physical-layer, ISCC edge-AI, and generative-diffusion network optimization).

(Two recurring author names are deferred for human confirmation as genuine **namesakes**: "Nan Zhao" appears in [[zhao-2022-matd3-multiuav-ec-offloading]] (Hubei Univ. of Technology) and [[zhang-2025-gan-td3-isac-active-ris]] (Dalian Univ. of Technology) — different institutions and emails, so not merged; and the "Jingjing Wang" in [[yang-2020-loadbalance-multiuav-iot]] is at **Tsinghua University** (`chinaeephd@gmail.com`), distinct from the existing **Beihang** [[jingjing-wang]] entity (`drwangjj@buaa.edu.cn`) — not merged.)

> Deferred affiliation move: "Chau Yuen" recurs in [[jia-2022-hierarchical-aerial-matching]] (Singapore Univ. of Technology and Design, `yuenchau@sutd.edu.sg`) and [[sun-2025-tjcct-twotimescale-uav-mec]] (Nanyang Technological Univ., `chau.yuen@ntu.edu.sg`). Same name, different listed institution/email (a plausible affiliation move rather than a namesake), so no entity page was minted pending human confirmation.

### Tools

- [[airfogsim]] - modular simulator for UAV-integrated vehicle fog computing.

- [[pytorch]] — DL framework.

(More authors appear in source frontmatter; entity pages exist for the central recurring contributors.)

## Concepts

### MEC fundamentals

- [[mobile-edge-computing]]
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
- [[coded-caching]]
- [[erasure-coded-edge-storage]]
- [[binary-vs-partial-offloading]]
- [[dynamic-voltage-scaling]]
- [[event-driven-vs-slot-driven-offloading]]
- [[task-priority-in-mec]]
- [[priority-based-delay-utility]]
- [[intra-swarm-task-delegation]]
- [[anti-jamming-mec]]
- [[wireless-power-transfer]]
- [[rf-energy-harvesting]]
- [[energy-harvesting-mec]]
- [[energy-procurement-compensation]]
- [[backscatter-communication]]
- [[simultaneous-wireless-information-and-power-transfer]]
- [[noma]]
- [[cooperative-perception]]
- [[perception-aided-offloading]]
- [[multi-source-data-fusion]]
- [[video-analytics-offloading]]
- [[video-transcoding-tradeoff]]
- [[qoe-modeling-mec]]
- [[service-caching-mec]]
- [[semantic-content-reuse]]
- [[network-slicing]]
- [[traffic-aware-offloading]]
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
- [[vehicle-fog-computing]]
- [[edge-user-allocation]]
- [[uav-data-collection]]
- [[dynamic-qos-constraints]]
- [[finite-blocklength-urllc]]
- [[network-function-virtualization]]
- [[virtual-network-embedding]]
- [[service-function-chaining]]
- [[small-cell-mec]]
- [[mobility-aware-offloading]]
- [[semantic-communication]]
- [[probabilistic-semantic-communication]]
- [[task-oriented-communication]]
- [[discriminant-gain]]
- [[device-to-device-communication]]
- [[digital-twin]]
- [[stochastic-network-calculus]]
- [[graph-based-resource-management]]
- [[hot-spot-problem-iot]]
- [[omrp-overlap-routing]]

### Aerial / network architectures

- [[multi-uav-assisted-mec]]
- [[high-density-mobile-device-scenarios]]
- [[heterogeneous-uav-fleet]]
- [[high-altitude-platform-station]]
- [[hierarchical-aerial-mec]]
- [[air-ground-integrated-network]]
- [[low-altitude-intelligent-network]]
- [[leo-satellite-edge-computing]]
- [[leo-satellite-coverage-time]]
- [[leo-handover-protocol]]
- [[walker-star-constellation]]
- [[free-space-optical-isl]]
- [[space-air-ground-integrated-network]]
- [[space-air-ground-ocean-integrated-network]]
- [[non-terrestrial-network]]
- [[urban-air-mobility]]
- [[vehicular-mec]]
- [[uav-enabled-its]]
- [[cellular-connected-uav]]
- [[drone-cell-3d-placement]]
- [[geometric-disk-cover]]
- [[maritime-mec]]
- [[uav-usv-cooperative-mec]]
- [[post-disaster-mec]]
- [[three-tier-cloud-edge-end]]
- [[wireless-backhaul]]
- [[fault-tolerant-relay-network]]
- [[intelligent-reflecting-surface]]
- [[uav-mounted-ris]]
- [[star-ris]]
- [[active-ris]]
- [[multi-functional-ris]]
- [[terahertz-communication]]

### UAV control & decisions

- [[uav-trajectory-control]]
- [[bang-bang-control]]
- [[uav-charging-scheduling]]
- [[dynamic-uav-clustering]]
- [[gauss-markov-mobility-model]]
- [[hybrid-action-decision-making]]
- [[b-spline-trajectory]]
- [[rotary-wing-propulsion-energy-model]]
- [[fixed-wing-propulsion-energy-model]]
- [[uav-mobile-relaying]]
- [[successive-hover-and-fly-trajectory]]
- [[information-causality-constraint]]

### DRL backbones

- [[ppo]] · [[j-ppo]]
- [[ddqn]]
- [[dueling-dqn]]
- [[deep-q-network]]
- [[ddpg]]
- [[td3]] · [[multi-agent-td3]]
- [[maddpg]]
- [[masac]]
- [[soft-actor-critic]]
- [[hierarchical-reinforcement-learning]]
- [[mappo]]
- [[heterogeneous-agent-rl]]
- [[trust-region-policy-optimization]]
- [[parameterized-dqn]]
- [[multi-agent-q-learning]]
- [[value-decomposition-network]]
- [[counterfactual-multi-agent-policy-gradient]]
- [[distributional-reinforcement-learning]]
- [[impala]]
- [[gae]]
- [[pomdp]] · [[ma-pomdp]]
- [[markov-reward-process]]
- [[semi-markov-decision-process]]
- [[centralized-training-decentralized-execution]]
- [[communication-constrained-marl]]
- [[model-based-marl]]
- [[end-to-end-vs-decomposition-in-drl-mec]]
- [[action-space-explosion-in-multi-uav-mec]]
- [[adaptive-entropy-priority-replay]]
- [[prioritized-experience-replay]]
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
- [[diffusion-model-as-optimizer]]
- [[generative-adversarial-network]]
- [[variational-autoencoder]]
- [[conditional-gan]]
- [[beta-policy-drl]]
- [[softppo-lstm]]
- [[expert-guided-warm-start-rl]]
- [[graph-neural-network]]

### Memory / encoders

- [[ntm]] · [[en-convntm]]
- [[j-ppo-en-convntm]] — composite j-PPO + EN-ConvNTM framework page
- [[convlstm]]
- [[stn]]
- [[transformer-encoder]]
- [[informer-trajectory-prediction]]
- [[probsparse-self-attention-prediction]]

### Optimization techniques (classical & evolutionary)

- [[lyapunov-optimization]]
- [[markov-approximation]]
- [[two-timescale-optimization]]
- [[fractional-programming-dinkelbach]]
- [[stackelberg-game]]
- [[mean-field-game]]
- [[potential-game]]
- [[stochastic-game]]
- [[fictitious-self-play]]
- [[bargaining-game]]
- [[coalition-formation-game]]
- [[nash-equilibrium]]
- [[price-of-anarchy]]
- [[prospect-theory]]
- [[contract-theory]]
- [[matching-theory-for-resource-allocation]]
- [[optimal-transport-theory]]
- [[gale-shapley-matching]]
- [[overlay-underlay-spectrum-access]]
- [[unicast-multicast-cooperation]]
- [[mixed-integer-nonlinear-programming]]
- [[dynamic-constrained-multi-objective-optimization]]
- [[constrained-multi-objective-evolutionary-algorithm]]
- [[genetic-algorithm]]
- [[non-dominated-sorting-genetic-algorithm]]
- [[cmoea-d-cdp]]
- [[constraint-violation-evaluation]]
- [[infeasible-individual-utilization]]
- [[dual-population-evolutionary-algorithm]]
- [[multi-tasking-evolutionary-algorithm]]
- [[differential-evolution]]
- [[local-search-evolutionary]]
- [[two-stage-decomposition]]
- [[penalty-dual-decomposition]]
- [[second-order-cone-programming]]
- [[linear-programming]]
- [[alternating-optimization-sdr-sca]]
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
- [[chance-constraint]]
- [[conditional-value-at-risk]]
- [[distributionally-robust-optimization]]
- [[robust-offloading]]
- [[cross-entropy-method]]
- [[generalized-assignment-problem]]
- [[double-auction]]
- [[reverse-auction-incentive]]
- [[alternating-direction-method-of-multipliers]]
- [[queueing-theory]]

### Channel modeling

- [[blockage-aware-channel-model]]
- [[air-to-ground-channel-model]]
- [[radio-map-assisted-channel-estimation]]
- [[movable-antenna]]
- [[terrain-aware-channel-model]]
- [[first-order-radio-energy-model]]
- [[stochastic-geometry-network-analysis]]
- [[csi-estimation-error]]

### Sensing & security

- [[integrated-sensing-and-communication]]
- [[cramer-rao-bound]]
- [[integrated-sensing-computation-communication]]
- [[mmwave-radar-sensing]]
- [[uav-backscatter-identification]]
- [[yolov7-object-detection]]
- [[spectrum-sensing-channel-selection]]
- [[physical-layer-security]]
- [[covert-communication]]
- [[friendly-jamming-uav]]
- [[cooperative-jamming]]
- [[proactive-eavesdropping]]
- [[secure-computation-efficiency]]
- [[secrecy-outage-probability]]
- [[collaborative-beamforming]]
- [[interference-alignment]]
- [[wireless-perception]]
- [[extremely-large-scale-mimo]]
- [[near-field-communications]]

### Security / trust / federation

- [[zero-trust-architecture]]
- [[federated-learning]]
- [[split-federated-learning]]
- [[federated-reinforcement-learning]]
- [[decentralized-federated-learning]]
- [[blockchain-for-fl-aggregation]]
- [[byzantine-fault-tolerant-consensus]]
- [[delegated-proof-of-stake]]
- [[ccvm-correction-voting]]
- [[csra-cold-start-reputation-aggregation]]
- [[fl-poisoning-attacks]]
- [[privacy-sensitive-data-partitioning]]
- [[seamless-handover]]
- [[adaptive-inter-layer-data-offloading]]

### Metrics & fairness

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
- [[age-of-information]]
- [[aoi-energy-tradeoff]]

### Distributed inference

- [[collaborative-dl-inference]]
- [[dnn-model-partition]]
- [[data-partition-parallel-inference]]
- [[pipeline-parallel-inference]]
- [[dl-inference-latency-prediction]]
- [[adaptive-intermediate-data-compression]]
- [[elastic-task-scheduling]]

### Scheduling

- [[interdependent-tasks-dag]]

### Safety

- [[collision-avoidance-mgi]]

## Methodology

- [[ctde-multi-agent-drl-protocol]] - centralized-training / decentralized-execution protocol for cooperative multi-agent MEC control
- [[drl-simulation-with-pomdp-formulation]] — POMDP simulation protocol used in [[liu-2026-jppo-en-convntm]]
- [[ao-sdr-sca-convex-pipeline]] — the AO + SDR + SCA convex pipeline recurring across the ISAC/secure-beamforming sources
- [[lyapunov-guided-drl]] — the Lyapunov drift-plus-penalty + per-slot DRL hybrid across 6 sources
- [[discrete-continuous-two-stage-decomposition]] — the discrete-then-continuous (matching/metaheuristic/discrete-policy + convex/continuous-policy) solver protocol

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
- [[hardware-validation-and-sim-to-real-in-mec]] — What "hardware-validated" means across the few non-simulation sources, and the sim-to-real challenges they name.

## References

- [[reference-database]] — master citation-mining database (5054 unique references mined from the corpus parses; centrality ranking by in-corpus `cited_count`).
- [[recommendations]] — reference-scout recommendations: cited-but-not-yet-curated papers ranked by recency, venue, in-corpus citation frequency, and track coverage.
