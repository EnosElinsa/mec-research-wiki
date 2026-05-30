# Wiki Index

## Sources (curated)

### Foundational surveys & overviews

- [[mao-2017-mec-survey-communication]] — Mao et al. 2017. Canonical **MEC survey** from the communication perspective (joint radio + compute resource management).
- [[khoramnejad-2025-gai-wireless-optimization-survey]] — Khoramnejad & Hossain 2025. Survey of **generative AI** for xG/6G wireless network optimization (GANs, GDMs, GFlowNets) + NTN case study.
- [[du-2024-gdm-network-optimization-tutorial]] — Du et al. 2024. **Tutorial** on **generative diffusion models** in network optimization (DRL enhancement, incentive/ISAC/SemCom/IoV case studies) (IEEE COMST).
- [[wang-gai-isac-physical-layer]] — Wang et al. Overview of **generative AI for ISAC** from the physical-layer perspective; five GAI models + a diffusion SSG near-field DoA case study (~1.03° MSE) (IEEE Wireless Communications; year not in parse).
- [[meng-2024-uav-isac-overview]] — Meng et al. 2024. Overview of **UAV-enabled ISAC** for 6G (motion control, resource allocation, S&C synergy).
- [[du-2024-distributed-foundation-models-6g]] — Du et al. 2024. Overview of **distributed foundation models** over 6G (pipeline/data parallelism + multi-modal learning).
- [[zeng-2019-uav-comm-tutorial-5g]] — Zeng et al. 2019. **Tutorial** on UAV communications for 5G and beyond; UAV-assisted comms vs **cellular-connected UAV** taxonomy (Proceedings of the IEEE).
- [[al-hourani-2014-optimal-lap-altitude]] — Al-Hourani et al. 2014. Foundational **air-to-ground channel** letter: closed-form sigmoid LoS-probability vs elevation angle + **optimal LAP altitude** for maximum ground coverage (IEEE WCL). *(Channel-model anchor, not MEC.)*

### Foundational DRL methods

- [[fujimoto-2018-td3-actor-critic]] — Fujimoto et al. 2018. Origin paper for **TD3** — clipped double-Q + delayed policy updates + target smoothing to curb actor-critic overestimation (ICML).
- [[xiang-sac-mapless-robot-navigation]] — Xiang et al. Mapless mobile-robot navigation via **Soft Actor-Critic** (LSTM value/Q nets); laser+target→velocity continuous control (venue/year not in parse).

### Joint trajectory / caching / migration

- [[zhao-2025-traj-offload-cache-migration]] — Zhao et al. 2025. Joint trajectory + offloading + migration + **computational-task caching**; Lyapunov + BCD + QCQP-SDR.
- [[gao-2024-service-experience-cache-uav]] — Gao & Zhai 2024. Fairness-aware cache-enabled UAV-MEC; **service-experience ratio** (Jain's index / delay); Dinkelbach + 4-stage AO.
- [[zhao-2024-caching-service-placement-uav]] — Zhao et al. 2024. Joint content caching + service placement + offloading; QoE max via Gibbs sampling + matching.
- [[du-2023-maddpg-service-placement-agin]] — Du et al. 2023. **MADDPG** joint service placement + offloading in air-ground integrated MEC.

### Game-theoretic offloading & allocation

- [[he-2019-euagame-user-allocation]] — He et al. 2019. **EUAGame** — edge user allocation as a potential game with a decentralized NE algorithm.
- [[sun-2024-mvtora-postdisaster-vfc]] — Sun et al. 2024. Post-disaster aerial-terrestrial MEC + **vehicle fog computing**; game theory + convex + evolutionary (MVTORA).

> [[chen-2024-ulse-game]] (UAV-LEO offloading as a potential game) is also game-theoretic; it is filed under **SAGIN / satellite offloading** below as its primary architectural home.

### Multi-UAV cooperative computing & deployment

- [[guo-2023-mccco-multiuav-5g-offloading]] — Guo et al. 2023. SDN-enhanced cooperative multi-UAV partial offloading with task interdependency (MCCCO).
- [[wang-2019-todetas-deployment-scheduling]] — Wang et al. 2019. Two-layer UAV deployment (**differential evolution**) + task scheduling (greedy); ToDeTaS.
- [[miao-2022-gaglpp-drone-swarm-iiot]] — Miao et al. 2023. Drone-swarm path planning for Industrial-IoT MEC; ground-station global + onboard local planning (GAGLPP); priority/energy/distance scheduling (IEEE TII).

### Pure optimization methods

- [[wang-acve-constraint-violation-cmop]] — Wang et al. **ACVE** — adaptive constraint-violation-evaluation framework + DDCo dual-population coevolution (venue/year `not in parse`).

### Compute offloading & DRL

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
- [[wang-2025-sac-tma-mec-dc]] — Wang et al. 2025. Joint multi-AAV **MEC + data collection**; SAC + two-phase matching-based association (SAC-TMA).
- [[wang-2022-cat-rat-fmec-trajectory]] — Wang et al. 2022. Flying-MEC UAV trajectory + association + resource; **CAT** (BCD convex) and **RAT** (twin-DQN + PER + matching) (IEEE TMC).
- [[niazmand-2025-jopa-dnn-pruning-iiot]] — Niazmand & Ye 2025. **DNN-pruning-aware** IIoT fault-detection offloading; joint offloading + pruned-model selection + resource allocation; MRP + hybrid-action SAC (JOPA) (IEEE TCCN).
- [[duan-2023-moto-smallcell-offloading]] — Duan et al. 2023. **MOTO** — mobility-aware online task offloading + adaptive load balancing in terrestrial **small-cell MEC**; LSTM (offloading control) + Dueling Double DQN (server grouping); real WiFi-trace driven (IEEE TMC).
- [[yang-2020-loadbalance-multiuav-iot]] — Yang et al. 2020. **Load-balance** multi-UAV MEC for IoT; **differential-evolution** UAV deployment + **GAP** node assignment (LP-relax + rounding) + **DQN** task scheduling (IEEE IoT-J).
- [[li-2024-robust-bmappo-multiuav-mec]] — Li et al. 2024. **Robust** multi-UAV-MEC offloading under joint communication + computation uncertainty; weighted-energy min via **MAPPO with a Beta-distribution policy** (b-MAPPO) (IEEE IoT-J).

### Classical / convex / optimization-based UAV-MEC

- [[zhang-2019-uav-iot-comp-comm]] — Zhang et al. 2019. Joint computation + communication design for single-UAV MEC; Lagrangian duality + SCA.
- [[yu-2020-uav-ec-collaborative-offloading]] — Yu et al. 2020. Collaborative UAV+edge-cloud offloading; SCA; beats UAV-only / EC-only.
- [[liu-2022-miso-uav-mec-trajectory]] — Liu et al. 2022. **MISO** UAV-MEC; three-stage AO with closed-form CPU-freq / power; CSI-driven offloading.
- [[yang-2022-stochastic-uav-mec-lyapunov]] — Yang et al. 2022. Stochastic UAV-MEC; **Lyapunov** online algorithm; two-stage vs joint comparison.
- [[bai-2024-delay-aware-cooperative-edge-cloud]] — Bai et al. 2024. Multi-UAV edge-cloud **cooperative** offloading; convex approximation + **Lyapunov** online; cooperative-parallel-computing delay model; platform-verified (IEEE TMC).
- [[apostolopoulos-2021-prospect-theory-uav-offloading]] — Apostolopoulos et al. 2021. Risk-aware partial offloading to ground + UAV MEC servers via **prospect theory**; non-cooperative game with proven unique PNE (IEEE TMC).
- [[pervez-2024-acm-multiuav-mec]] — Pervez et al. 2024. Multi-UAV + BS MEC; weighted energy+latency cost via three-layer **ACM** (potential-game offloading + GWF power + SCA trajectory + gradient-descent CPU) (IEEE TWC).
- [[zeng-2019-rotary-wing-energy-min]] — Zeng et al. 2019. **Rotary-wing UAV propulsion energy model** + energy-minimizing trajectory; fly-hover-communicate (TSPN) and communicate-while-flying (path discretization + SCA) (IEEE TWC).
- [[hu-2019-pdd-uav-mec-offloading]] — Hu et al. 2019. Single-UAV MEC; min-max-delay offloading-ratio + trajectory + user scheduling via **penalty dual decomposition** (PDD + CCCP) + simplified l0-norm (IEEE IoT-J).
- [[wu-2024-urllc-uav-mec-latency]] — Wu et al. 2024. **URLLC / finite-blocklength** UAV-MEC; min-max latency via BCD + SCA over UAV 3D location + bandwidth + CPU frequency; Rician fading (IEEE TWC).
- [[wu-2018-multiuav-minrate-trajectory]] — Wu et al. 2018. Multi-UAV-as-base-station **max-min-rate** trajectory + scheduling + power; BCD + SCA + circle-packing init (communications framing, IEEE TWC).

### SAGIN / satellite offloading

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

### IRS / THz / anti-jamming

- [[wu-2025-iopo-irs-uav-thz-mec]] — Wu et al. 2025. **IRS-assisted** multi-UAV THz MEC; two-stage IOPO (order-preserving offloading + WOA phases).
- [[shao-2024-drl-antijamming-mec]] — Shao et al. 2024. **Anti-jamming** UAV-MEC resource management; PER-MATD3 (hardware-validated).
- [[sun-2024-mfris-semantic-antijamming]] — Sun et al. 2024. **Multi-functional RIS** + **semantic** anti-jamming communication & computing for aerial-ground MEC; worst-case CSI; semantic-computation-rate max via monotonic optimization + DSOCP (+ GPI) (IEEE JSAC).

### UAV-swarm collaborative computing

- [[sun-2024-asap-uav-swarm]] — Sun et al. 2024. **ASAP** — in-swarm collaborative DL inference (model + data partition, pipeline-parallel); hardware-validated.
- [[qu-ecoei-uav-swarm]] — Qu et al. **eCoEI** — elastic OODA-loop collaborative DL inference for UAV swarms, robust to node/A2A-link failure; proof-of-concept on Jetson devices (IEEE Communications Magazine; year not in parse).
- [[li-2025-stochastic-game-uav-swarm]] — Li et al. 2025. Energy-efficient UAV-swarm MEC as five **stochastic games** with dynamic clustering; RLDC multi-agent Q-learning.
- [[li-2024-rldc-uav-swarm-clustering]] — Li et al. 2024. **Conference precursor** of the above (IEEE WCNC 2024); six stochastic games + RLDC, no NE/convergence proof.
- [[zhang-2020-response-delay-uav-swarm]] — Zhang et al. 2020. **Response-delay** optimization for a MEC-enabled UAV swarm (T-UAV + B-UAVs); **stochastic geometry** + **queueing theory** closed-form delay; **hardware-validated** (2 DJI M100 + 5G NR mmWave) (IEEE TVT).

### Generative-AI MEC

- [[ye-2025-aigc-diffusion-contract]] — Ye et al. 2025. Edge AIGC services via **contract theory** + prompt engineering; generative diffusion model as the contract-item optimizer.
- [[zhang-2024-gdmtd3-aerial-secure-cb]] — Zhang et al. 2024. UAV-swarm secure collaborative beamforming via **generative-diffusion-model-enhanced TD3** (GDMTD3).
- [[fu-2025-otae-inference-lae-batching]] — Fu et al. 2025. Over-the-air edge inference for low-altitude airspace; diffusion-based online batching + beamforming.
- [[du-2024-d2sac-aigc-asp-selection]] — Du et al. 2024. Edge AIGC-as-a-Service provider selection; diffusion decision generator (AGOD) inside SAC (**D2SAC**); beats 7 DRL baselines (IEEE TMC).

### Generative-AI / GAN for ISAC & channels

- [[faisal-2025-cgan-ris-isac-channel]] — Faisal et al. 2025. **Conditional GAN** for channel estimation in RIS-assisted ISAC.
- [[zhang-2025-gan-td3-isac-active-ris]] — Zhang et al. 2025. **GAN-TD3** beamforming for ISAC with double active RISs.

### Multi-agent UAV-MEC

- [[peng-2025-drudm-cfg]] — Peng et al. 2025. Fairness-aware multi-agent DRL for HAS-UAV post-disaster MEC. *DRUDM-CFG*.
- [[zhang-2025-ssac-mgi-heterogeneous-uav]] — Zhang et al. 2025. Safe & energy-efficient trajectory planning for heterogeneous UAV-MEC. *SSAC-MGI* (shared SAC + Markov game of intervention).
- [[bi-2025-sg-mapg]] — Bi et al. 2025. Three-layer hierarchical Stackelberg game for UAV-MEC service fairness & cost. *SG-MAPG*.
- [[wang-2021-maddpg-multiuav-trajectory]] — Wang et al. 2021. **MADDPG** per-UAV trajectory planning for multi-UAV MEC; dual fairness (geographical + UE-load) + UE energy; low-complexity offloading step (IEEE TCCN).
- [[seid-2021-madrl-multiuav-iot-edge]] — Seid et al. 2021. Clustered multi-UAV IoT-edge offloading + resource allocation as a **stochastic game**; **MADDPG** (MADRL); energy+delay cost (IEEE TNSM).

### Hierarchical aerial MEC (UAV + HAP)

- [[nabi-2025-jour-hierarchical-aerial]] — Nabi & Moh 2025. *JOUR* — Gale-Shapley matching + ESAC for joint offloading, association, and resource allocation in UAV+HAP MEC.
- [[bao-2025-ddpg-video-offloading]] — Bao et al. 2025. UAV+HAP video-analytics offloading with adaptive transcoding; DDPG over a QoE reward.
- [[jia-2025-dro-uav-hap-mec]] — Jia et al. 2025. **Distributionally robust** UAV-HAP MEC under uncertain CSI; CVaR + primal decomposition + BWOA.
- [[jia-2022-hierarchical-aerial-matching]] — Jia et al. 2022. **Matching game** + heuristic for HAP+UAV aerial computing serving IoT (early anchor).
- [[kang-2023-mappo-hierarchical-aerial]] — Kang et al. 2023. **MAPPO** for UAV resource allocation + UAV→HAP offloading (CTDE).
- [[chen-2023-dotora-air-ground-online]] — Chen et al. 2023. HAP+UAV air-ground MEC; stochastic optimization + game theory (DGMS/TPA/DOTORA).

### Vehicular MEC

- [[zhang-2025-mcma-task-migration]] — Zhang et al. 2025. Task migration with Informer trajectory prediction across edge servers. *MCMA*.
- [[xie-2026-uav-multisource-fusion]] — Xie et al. 2026. UAV-enabled cooperative perception fusion via dynamic constrained multi-objective optimization.
- [[sun-2023-bargain-match-vec]] — Sun et al. 2023. **BARGAIN-MATCH** — bargaining (intra-server) + matching (inter-server) for VEC offloading.
- [[peng-2020-maddpg-uav-vehicular]] — Peng & Shen 2020. **MADDPG** multi-dimensional resource management (vehicle association + allocation) in MEC- and UAV-assisted vehicular networks; converges in ~200 episodes (IEEE JSAC).

### Maritime MEC

- [[wang-2026-aerial-marine-msar]] — Wang et al. 2026. UAV+HAPS+MASS three-tier MEC for maritime search & rescue. *JCORA* (matching + convex + PGD).
- [[liu-2025-haps-uav-maritime-iot]] — Liu et al. 2025. HAP-UAV maritime IoT comm: HAP-as-backhaul, UAV multicast, vessel unicast.
- [[wang-2025-double-edge-samin]] — Wang et al. 2025. Double-edge (UAV+LEO) offloading for space-air-marine networks; AO + layered decomposition.
- [[zhang-2025-three-tier-maritime-offloading]] — Zhang et al. 2025. Three-tier (MWD/OBS/LEO) maritime offloading; MINLP decomposition; 39.3% energy saving.
- [[wang-2024-maritime-eh-jcora]] — Wang et al. 2024. **Energy-harvesting** maritime MEC (solar + ocean-wave buoys); throughput max under queue + energy constraints; Lyapunov / JCORA (IEEE IoT-J).
- [[dai-2023-hybrid-marine-mmwl]] — Dai et al. 2023. **Hybrid** offshore (FDMA) + aerial-UAV (NOMA) multi-access offloading; min-max workloads latency (MMWL); layered 3-subproblem decomposition (IEEE TCOMM).
- [[zhang-2024-dlrl-maritime-usv]] — Zhang et al. 2024. USV mobile-edge deployment + offloading; dual-layer RL (outer DDPG / inner Q-learning).
- [[you-2025-uncertain-maritime-hasac]] — You et al. 2025. Uncertain maritime MEC (AAVs+vessels); Lyapunov + Markov game + heterogeneous-agent SAC.
- [[wang-2024-twotier-satellite-marine]] — Wang et al. 2024. Two-tier satellite-marine offloading; hybrid **Stackelberg-Bargaining** game (NOMA/FDMA).
- [[lyu-2023-noma-marine-emergency-offloading]] — Lyu et al. 2023. **NOMA**-based UAV emergency communication for marine IoT; MINLP decomposed into quasi-convex/convex resource allocation + **coalition-game** offloading (CGTO) (IEEE IoT-J).
- [[qi-2024-msar-minmax-latency]] — Qi et al. 2024. Multi-UAV maritime **search & rescue**; **min-max latency** over offloading + R-UAV deployment + S-UAV–target association; iterative linearization + SCA + Branch-and-Bound (IEEE TVT).
- [[dai-2024-multiuav-marine-welfare]] — Dai et al. 2024. Multi-UAV multi-access marine MEC (UAVs + **ocean beacon stations**); maximizes **system revenue** (welfare − energy) via layered decomposition + **double-auction** OBS selection (IEEE TCOMM).
- [[li-2023-secure-marine-iot-jamming]] — Li et al. 2023. **Secure** marine-IoT offloading: USVs upload to a **HAP** via NOMA then provide **cooperative jamming**; system-energy min via monotonic optimization (PAS) + cross-entropy (CASE) (IEEE TVT).

### Trust, security, and federated MEC

- [[mao-2025-bcsa-frl]] — Mao et al. 2025. Blockchain-enabled cold-start FRL for ZT LEO satellite networks. *BCSA-FRL* (CCVM + CSRA).
- [[qin-2025-bcuav-masac]] — Qin et al. 2025. Blockchain-enabled secure UAV-MEC: Lyapunov + MASAC + DOA.
- [[benaya-2025-aerial-isac-haps]] — Benaya et al. 2025. HAPS-mounted FD ISAC + friendly-jamming UAV + ground MEC; AO + SDR + SCA.
- [[wang-2025-acbft-uav-consensus]] — Wang et al. 2025. **ACBFT** — PSO-ordered chain-based Byzantine fault-tolerant consensus for UAV ad hoc networks.

### ISAC, sensing & physical-layer security

- [[tang-2024-iscc-uav-feel]] — Tang et al. 2024. **ISCC** for UAV-assisted federated edge learning; deployment + sensing/compute/comm via AO (BBPO).
- [[yao-2025-secure-isac-dual-eavesdropping]] — Yao et al. 2025. Secure UAV-ISAC against dual eavesdropping; AO + SCA + SDR for secrecy + sensing security.
- [[chen-2024-three-party-hierarchical-game-pls]] — Chen et al. 2024. **Three-party hierarchical game** for PLS with dynamic trilateral coalitions (LUs / EVs / JAs); HCSF + DRL (IEEE TWC).
- [[michailidis-2024-secure-ris-uav-mec-iot]] — Michailidis et al. 2024. Secure UAV-**RIS**-MEC-IoT offloading against **aerial + ground eavesdroppers**; SOP over Nakagami-m + max-min **secure computation efficiency** via Dinkelbach + BCD + bisection (IEEE TCOMM).

### Collaborative beamforming & aerial communications

- [[sun-2025-emoppo-vlh-aerial-cb]] — Sun et al. 2025. AAV-swarm **collaborative beamforming** (virtual antenna array) to a terrestrial mobile user; evolutionary multi-objective PPO with vectorized value + LSTM + hyper-sphere task selection (EMOPPO-VLH).
- [[li-2024-emodrl-ground-space-cb]] — Li et al. 2024. **Distributed collaborative beamforming** for ground-space (terminal-to-LEO) uplink; evolutionary multi-objective DRL (EMODRL); saves 30% handover frequency.
- [[li-2024-emssa-uav-swarm-vaa]] — Li et al. 2024. **Virtual antenna arrays** for UAV-swarm-assisted IoT data harvesting/dissemination; multi-objective (time / eavesdropper / energy) **salp swarm** optimizer (EMSSA); ground + aerial CB (IEEE TMC).

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

- [[zhu-2025-lycnn-drl-wpt-mec]] — Zhu et al. 2025. Lyapunov-guided DRL for WPT-MEC.
- [[chen-2025-swipt-mec-sac]] — Chen et al. 2025. SWIPT-MEC with directional-antenna UAV; improved SAC (SAC-SK), bi-objective energy.
- [[zhou-2018-uav-wireless-powered-mec]] — Zhou et al. 2018. **Computation-rate maximization** in UAV-enabled wireless-powered MEC; partial + binary offloading; two-/three-stage closed-form optimization (JSAC).

> [[wu-2025-iopo-irs-uav-thz-mec]] (IRS-assisted THz energy optimization) also targets energy efficiency; it is filed under **IRS / THz / anti-jamming** above as its primary home.

## Entities

### Authors

- [[lihan-liu]], [[hongrui-miao]], [[chunhui-qu]], [[zhuwei-wang]], [[haijun-zhang]], [[zhidu-li]] — co-authors of [[liu-2026-jppo-en-convntm]].
- [[chaoda-peng]], [[xumin-huang]], [[yuan-wu]], [[jiawen-kang]] — recurring co-authors across the [[cmop-evolutionary-uav-mec-lineage|CMOP-evolutionary UAV-MEC lineage]] (4–6 sources each).
- [[hao-hao]] — first author of the two priority-aware offloading sources ([[hao-2024-clp-multiuav-priority-offloading]], [[hao-2025-priority-aware-task-driven-co]]).
- [[geng-sun]] — recurring (co-)author across the Jilin-University aerial/maritime cluster (5 sources): [[sun-2023-bargain-match-vec]], [[sun-2024-mvtora-postdisaster-vfc]], [[chen-2025-swipt-mec-sac]], [[zhang-2024-gdmtd3-aerial-secure-cb]], [[wang-2025-lae-network-survey]].
- **Jilin-University / NTU aerial-MEC cluster:** [[zemin-sun]], [[jiahui-li]] (Jilin University), [[jiacheng-wang]], [[dusit-niyato]] (NTU), [[qingqing-wu]] (Shanghai Jiao Tong University) — confirmed in the 2026-05-29 follow-up pass.
- **NUAA aerial-computing cluster:** [[ziye-jia]], [[chao-dong]], [[qihui-wu]] (NUAA), [[zhu-han]] (Univ of Houston / Kyung Hee).
- **Dalian-Maritime-University maritime cluster:** [[bin-lin]] (DMU), [[zhen-wang]] (DMU / Dalian Neusoft), [[qiang-ye]] (Univ of Calgary).
- **NWPU non-terrestrial-network cluster:** [[bomin-mao]], [[hongzhi-guo]], [[jiajia-liu]] (Northwestern Polytechnical University).
- **NCEPU aerial-edge cluster:** [[peng-qin]], [[yang-fu]] (North China Electric Power University); [[jingjing-wang]] (Beihang University) links the blockchain-UAV thread.
- **South-China-Agricultural-University evolutionary UAV-MEC cluster:** [[zexiong-wu]] (with [[chaoda-peng]], [[xumin-huang]], [[yuan-wu]]).
- **Cross-cutting seniors:** [[chunxiao-jiang]] (Tsinghua), [[tony-q-s-quek]] (SUTD).
- **Newly confirmed (2026-05-30):** [[ying-chen]] (Beijing Information Sci. & Tech. Univ. — online + game-theoretic offloading), [[jie-xu]] (CUHK-Shenzhen — ISAC), [[fuhong-song]] (SWJTU → Guizhou Univ. of Finance & Economics — evolutionary MORL), [[yong-wang]] (Central South Univ. — constrained/evolutionary optimization), [[wei-zhang]] (Shandong Computer Science Center — task-priority offloading, [[hao-hao]] group).
- **Newly confirmed (2026-05-31):** [[shuang-liang]] (Northeast Normal Univ. — aerial-MEC / LAE, [[geng-sun]] cluster), [[weifeng-zhong]] & [[shengli-xie]] (Guangdong Univ. of Technology — CMOP-evolutionary lineage), [[qiqi-xie]] (South China Agricultural Univ. — evolutionary UAV-MEC), [[nei-kato]] (Tohoku Univ.), [[jiadai-wang]], [[yijie-xun]], [[yangbo-liu]] (Northwestern Polytechnical Univ. — NTN cluster, [[bomin-mao]] group).
- **Newly confirmed (batch 1/8):** [[boxiong-wang]] & [[hui-kang]] (Jilin University — [[geng-sun]] aerial-MEC cluster; 2 sources each, email-confirmed).
- **Newly confirmed (batch 3/8):** [[yuben-qu]] & [[hao-sun]] (Nanjing Univ. of Aeronautics and Astronautics — UAV-swarm collaborative-inference cluster with [[chao-dong]]/[[qihui-wu]]; 2 sources each — [[qu-ecoei-uav-swarm]] + [[sun-2024-asap-uav-swarm]] — identical `@nuaa.edu.cn` emails).
- **Newly confirmed (batch 5/8):** [[kezhi-wang]] (Northumbria Univ. — UAV-MEC trajectory/offloading group; 3 sources, `kezhi.wang@northumbria.ac.uk`-matched), [[xuemin-shen]] (Univ. of Waterloo — MEC resource management; 2 sources), [[yuguang-fang]] (City Univ. of Hong Kong — maritime MEC, [[bin-lin]] cluster; 2 sources), [[haixia-peng]] (Univ. of Waterloo → Xi'an Jiaotong Univ. — vehicular + maritime MEC; 2 sources, affiliation move documented in both parses).
- **Newly confirmed (batch 6/8):** [[liping-qian]] (Zhejiang Univ. of Technology — NOMA / multi-access marine MEC; 3 sources, `lpqian@zjut.edu.cn`-matched), [[minghui-dai]] (Univ. of Macau — marine multi-access offloading; first author of 2 sources, `minghuidai@um.edu.mo`), [[zhiyong-feng]] (Beijing Univ. of Posts and Telecommunications — UAV-swarm MEC + UAV-ISAC; 2 sources, `fengzy@bupt.edu.cn`-matched).

(One recurring author remains deferred for human confirmation as a genuine **namesake**: "Nan Zhao" appears in [[zhao-2022-matd3-multiuav-ec-offloading]] (Hubei Univ. of Technology) and [[zhang-2025-gan-td3-isac-active-ris]] (Dalian Univ. of Technology) — different institutions and emails, so they are not merged. See the 2026-05-30 log entry. A second **namesake** was confirmed in batch 6/8: the "Jingjing Wang" in [[yang-2020-loadbalance-multiuav-iot]] is at **Tsinghua University** (`chinaeephd@gmail.com`, Shuimu Tsinghua Scholar), distinct from the existing **Beihang** [[jingjing-wang]] entity (`drwangjj@buaa.edu.cn`) — not merged.)

### Tools

- [[pytorch]] — DL framework.

(More authors appear in source frontmatter; entity pages currently exist for the central recurring contributors. Future entity pages should land here as more authors recur.)

## Concepts

### MEC fundamentals

- [[mobile-edge-computing]]
- [[task-offloading]]
- [[task-migration]]
- [[computational-task-caching]]
- [[binary-vs-partial-offloading]]
- [[event-driven-vs-slot-driven-offloading]]
- [[task-priority-in-mec]]
- [[priority-based-delay-utility]]
- [[intra-swarm-task-delegation]]
- [[anti-jamming-mec]]
- [[wireless-power-transfer]]
- [[rf-energy-harvesting]]
- [[energy-harvesting-mec]]
- [[noma]]
- [[cooperative-perception]]
- [[perception-aided-offloading]]
- [[multi-source-data-fusion]]
- [[video-analytics-offloading]]
- [[video-transcoding-tradeoff]]
- [[qoe-modeling-mec]]
- [[service-caching-mec]]
- [[network-slicing]]
- [[traffic-aware-offloading]]
- [[parallel-vs-serial-processing]]
- [[task-redundancy-for-reliability]]
- [[dispersed-computing]]
- [[generative-ai-for-mec]]
- [[aigc-service-provider]]
- [[prompt-engineering]]
- [[distributed-foundation-models]]
- [[over-the-air-computation]]
- [[vehicle-fog-computing]]
- [[edge-user-allocation]]
- [[uav-data-collection]]
- [[dynamic-qos-constraints]]
- [[finite-blocklength-urllc]]
- [[network-function-virtualization]]
- [[service-function-chaining]]
- [[small-cell-mec]]
- [[mobility-aware-offloading]]
- [[semantic-communication]]

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
- [[walker-star-constellation]]
- [[space-air-ground-integrated-network]]
- [[non-terrestrial-network]]
- [[vehicular-mec]]
- [[uav-enabled-its]]
- [[cellular-connected-uav]]
- [[maritime-mec]]
- [[post-disaster-mec]]
- [[three-tier-cloud-edge-end]]
- [[wireless-backhaul]]
- [[intelligent-reflecting-surface]]
- [[multi-functional-ris]]
- [[terahertz-communication]]

### UAV control & decisions

- [[uav-trajectory-control]]
- [[uav-charging-scheduling]]
- [[dynamic-uav-clustering]]
- [[gauss-markov-mobility-model]]
- [[hybrid-action-decision-making]]
- [[b-spline-trajectory]]
- [[rotary-wing-propulsion-energy-model]]

### DRL backbones

- [[ppo]] · [[j-ppo]]
- [[ddqn]]
- [[deep-q-network]]
- [[ddpg]]
- [[td3]] · [[multi-agent-td3]]
- [[maddpg]]
- [[masac]]
- [[soft-actor-critic]]
- [[mappo]]
- [[heterogeneous-agent-rl]]
- [[parameterized-dqn]]
- [[multi-agent-q-learning]]
- [[gae]]
- [[pomdp]] · [[ma-pomdp]]
- [[markov-reward-process]]
- [[centralized-training-decentralized-execution]]
- [[adaptive-entropy-priority-replay]]
- [[prioritized-experience-replay]]
- [[safe-reinforcement-learning]]
- [[hybrid-action-representation]]
- [[dynamic-confidence-interval-clipping]]
- [[knowledge-distillation-for-drl]]
- [[multi-objective-reinforcement-learning]]
- [[multi-objective-mdp-vectorial-reward]]
- [[evolutionary-reinforcement-learning]]
- [[generative-diffusion-model]]
- [[diffusion-model-as-optimizer]]
- [[generative-adversarial-network]]
- [[conditional-gan]]
- [[beta-policy-drl]]

### Memory / encoders

- [[ntm]] · [[en-convntm]]
- [[j-ppo-en-convntm]] — composite j-PPO + EN-ConvNTM framework page
- [[convlstm]]
- [[stn]]
- [[informer-trajectory-prediction]]
- [[probsparse-self-attention-prediction]]

### Optimization techniques (classical & evolutionary)

- [[lyapunov-optimization]]
- [[fractional-programming-dinkelbach]]
- [[stackelberg-game]]
- [[potential-game]]
- [[stochastic-game]]
- [[bargaining-game]]
- [[coalition-formation-game]]
- [[nash-equilibrium]]
- [[prospect-theory]]
- [[contract-theory]]
- [[matching-theory-for-resource-allocation]]
- [[gale-shapley-matching]]
- [[overlay-underlay-spectrum-access]]
- [[unicast-multicast-cooperation]]
- [[mixed-integer-nonlinear-programming]]
- [[dynamic-constrained-multi-objective-optimization]]
- [[constrained-multi-objective-evolutionary-algorithm]]
- [[cmoea-d-cdp]]
- [[constraint-violation-evaluation]]
- [[infeasible-individual-utilization]]
- [[dual-population-evolutionary-algorithm]]
- [[multi-tasking-evolutionary-algorithm]]
- [[differential-evolution]]
- [[local-search-evolutionary]]
- [[two-stage-decomposition]]
- [[penalty-dual-decomposition]]
- [[alternating-optimization-sdr-sca]]
- [[monotonic-optimization]]
- [[qcqp-sdr-probabilistic-mapping]]
- [[order-preserving-quantization]]
- [[binary-whale-optimization]]
- [[whale-optimization-algorithm]]
- [[salp-swarm-algorithm]]
- [[self-adaptive-global-best-harmony-search]]
- [[multi-verse-optimizer]]
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
- [[queueing-theory]]

### Channel modeling

- [[blockage-aware-channel-model]]
- [[air-to-ground-channel-model]]
- [[terrain-aware-channel-model]]
- [[stochastic-geometry-network-analysis]]
- [[csi-estimation-error]]

### Sensing & security

- [[integrated-sensing-and-communication]]
- [[integrated-sensing-computation-communication]]
- [[mmwave-radar-sensing]]
- [[yolov7-object-detection]]
- [[spectrum-sensing-channel-selection]]
- [[physical-layer-security]]
- [[friendly-jamming-uav]]
- [[cooperative-jamming]]
- [[secure-computation-efficiency]]
- [[secrecy-outage-probability]]
- [[collaborative-beamforming]]

### Security / trust / federation

- [[zero-trust-architecture]]
- [[federated-learning]]
- [[federated-reinforcement-learning]]
- [[decentralized-federated-learning]]
- [[blockchain-for-fl-aggregation]]
- [[byzantine-fault-tolerant-consensus]]
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

- [[drl-simulation-with-pomdp-formulation]] — POMDP simulation protocol used in [[liu-2026-jppo-en-convntm]]
- [[ao-sdr-sca-convex-pipeline]] — the AO + SDR + SCA convex pipeline recurring across the ISAC/secure-beamforming sources

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

## Thesis

- [[hybrid-action-memory-augmented-drl-wins-uav-mec]]

## Queries

- [[query-does-en-convntm-generalize-beyond-uav-mec]]
- [[query-real-world-validation-of-jppo-en-convntm]]
- [[query-when-does-dro-beat-drl-for-csi-uncertainty]] — DRO vs DRL vs structure for CSI uncertainty
- [[query-video-vs-cooperative-perception-offloading-shape]] — do rich-media offloading workloads share an optimization shape?

## Comparisons

- [[ddpg-vs-jppo]]
- [[j-ppo-baselines]]
- [[bcsa-frl-vs-bc-uav-masac]] — Blockchain-on-edge: BCSA-FRL vs BC-UAV-MASAC
- [[game-theoretic-offloading-formulations]] — potential vs Stackelberg vs bargaining vs matching

## Synthesis

- [[design-recipe-multi-uav-mec]] — 10-step recipe for DRL-controlled UAV-MEC.
- [[drl-backbones-across-uav-mec-sources]] — Cross-corpus DRL-backbone analysis.
- [[maddpg-vs-masac-in-mec]] — When entropy beats determinism in cooperative MEC.
- [[cmop-evolutionary-uav-mec-lineage]] — Peng/Huang group's 6-paper CMOP-evolutionary lineage (2022-2026).
- [[hierarchical-aerial-mec-design-space]] — Cross-comparison of the 5 UAV+HAP hierarchical-MEC sources.
- [[drl-vs-evolutionary-vs-classical-solvers]] — Solver-family analysis (DRL / evolutionary / classical).
- [[sagin-satellite-offloading-landscape]] — The 8 SAGIN / satellite-offloading sources mapped by satellite role + solver shape.
- [[isac-sensing-in-aerial-mec]] — How sensing enters the 7 ISAC/sensing sources.
- [[maritime-mec-architectures]] — Tiering + solver families across the 7 maritime sources.
- [[blockchain-on-edge-trust-layer]] — Which layer the blockchain defends (consensus / aggregation / audit) across the 3 blockchain-on-edge sources.

## References

- [[reference-database]] — master citation-mining database (2981 unique references mined from the corpus parses; centrality ranking by in-corpus `cited_count`).
- [[recommendations]] — reference-scout recommendations: cited-but-not-yet-curated papers ranked by recency, venue, in-corpus citation frequency, and track coverage.
