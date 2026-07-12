---
type: concept
title: UAV Trajectory Control
tags: [uav, control, path-planning]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[uav-charging-scheduling]]"
  - "[[liu-2026-jppo-en-convntm]]"
  - "[[mohammadi-2026-star-ris-uav-mec-noma]]"
  - "[[xiao-2025-star-ris-bidirectional-uav-mec]]"
  - "[[wang-2026-secure-lae-uav-scheduling]]"
  - "[[tong-2026-uneven-terrain-uav-mec]]"
  - "[[ye-2026-deeplsc-lae-isac]]"
  - "[[ye-2026-meta-deepesc-lae-isac]]"
  - "[[ye-2026-mode-lae-isac]]"
  - "[[zhao-2026-hcdrl-ga-sagin-sar]]"
  - "[[qin-2023-ris-uav-mec-ee]]"
  - "[[huang-2025-fedx-ris-uav-trajectory]]"
  - "[[ji-2026-llm-iov-uav-offloading]]"
  - "[[wang-2025-ppo-uav-positioning-offloading]]"
  - "[[guo-2026-aot-uav-inspection-offloading]]"
  - "[[wu-2026-model-based-ppo-ris-uav-mec]]"
  - "[[liao-2026-aoi-ris-uav-usv-mec]]"
  - "[[cai-2026-llm-drl-secure-lae-data]]"
  - "[[liu-2025-multimodal-semantic-iov-jamming]]"
  - "[[sheng-2025-ris-online-uav-mec]]"
  - "[[ye-2026-flight-speed-battery-swapping]]"
  - "[[hu-2026-ertatd3-secure-caching]]"
  - "[[feng-2026-prediction-service-migration]]"
  - "[[chen-2026-qos-noma-multiuav]]"
  - "[[diallo-2026-system-cost-uav-leo-offloading]]"
  - "[[tang-2026-hg-maddpg-uav-rescue]]"
  - "[[zhao-2026-temporal-spectrum-cartography]]"
  - "[[gong-2026-safe-economic-lae-trajectory]]"
  - "[[beishenalieva-2026-secrecy-aware-uav-path-planning]]"
  - "[[wu-2026-secure-split-offloading-ci]]"
  - "[[wu-2026-service-oriented-segmented-trajectory]]"
  - "[[zhao-2026-adaptive-wdc-wet-lae]]"
  - "[[zhou-2026-radar-energy-iscac]]"
  - "[[zhu-2026-hab-mappo-target-search]]"
  - "[[cao-2026-uav-self-tracking-ms-mm]]"
  - "[[you-2019-rician-uav-data-harvesting]]"
  - "[[lee-2026-uav-delivery-time-energy]]"
  - "[[zhu-2026-uav-localization-jamming]]"
  - "[[li-2026-control-based-uav-isac]]"
  - "[[control-parameterized-uav-trajectory]]"
  - "[[du-2025-autonomous-intelligent-uav-swarms]]"
  - "[[gong-2026-uav-3d-visual-coverage]]"
  - "[[path-aware-3d-visual-coverage]]"
  - "[[li-2026-aerial-ris-trajectory-phase]]"
  - "[[hosseini-2026-aoi-covert-uav]]"
  - "[[bai-2026-aoi-uav-isac]]"
  - "[[tilt-aware-aerial-ris-control]]"
  - "[[liu-2026-spherical-t-ris-bs]]"
  - "[[ebrahimi-not-in-parse-autonomous-uav-localization-rl]]"
  - "[[rss-based-uav-localization]]"
  - "[[wang-2026-bayesian-uav-spectrum-mapping]]"
  - "[[information-driven-uav-spectrum-mapping]]"
  - "[[belgiovine-not-in-parse-multidt-abs-deployment]]"
  - "[[jiang-2026-bi-level-uav-delivery-safety]]"
  - "[[target-level-of-safety]]"
  - "[[heo-not-in-parse-blockage-aided-multiuav-interference]]"
  - "[[building-blockage-aided-interference-coordination]]"
  - "[[hua-2026-ddrl-content-delivery]]"
  - "[[uav-content-caching]]"
  - "[[meng-2026-uav-isac-corrections]]"
  - "[[liu-2026-usp-nfrp-emergency-communication]]"
  - "[[persistent-emergency-uav-swarm-service]]"
  - "[[wang-2026-wutf-fair-communication]]"
  - "[[wireless-powered-uav-fair-service-control]]"
  - "[[li-2023-energy-constrained-uav-data-collection]]"
  - "[[energy-constrained-uav-data-collection-orienteering]]"
  - "[[morshed-2026-active-ris-uav-noma-mappo]]"
  - "[[decentralized-active-ris-uav-noma-control]]"
  - "[[wang-2026-glint-aoi-wireless-powered-edge]]"
  - "[[dual-network-sequential-aoi-control]]"
  - "[[qin-2023-symmetry-augmented-uav-isac]]"
  - "[[vitale-2026-density-aware-4d-trajectory]]"
  - "[[zhang-2026-omnidirectional-monitoring-deployment]]"
  - "[[zhao-2026-dt-ddqn-bisd-deployment]]"
  - "[[zhang-2026-dt-aircomp-cluster-formation]]"
  - "[[zhang-2026-distance-attention-uav-navigation]]"
  - "[[liu-2020-distributed-uav-coverage-navigation]]"
  - "[[liu-2021-edivert-mobile-crowdsensing]]"
  - "[[fu-2026-dubins-uav-data-collection]]"
  - "[[releasing-collecting-recycling-uav-framework]]"
  - "[[wang-2026-multimodal-uav-coverage-backhaul]]"
  - "[[multi-modal-uav-coverage-backhaul-control]]"
created: 2026-05-28
updated: 2026-07-13
---

# UAV Trajectory Control

The continuous-action portion of the [[multi-uav-assisted-mec]] decision vector: choosing the per-step displacement of each UAV. In [[liu-2026-jppo-en-convntm]] the controller assumes:

- constant cruise speed $v_u = 10$ m/s during data-collection mode
- hover during charging
- fixed flight altitude $h_u = 35$ m
- per-step displacement bounded by $D_{\max}$

The objective is shaped by the [[equilibrium-efficiency-metric]] — coverage and fairness pull the UAV outward toward sparsely-visited regions, while the energy term and obstacle/inter-UAV penalties pull it back. Trajectories are sampled from a Gaussian policy head; see [[j-ppo]] for how this couples with the discrete decisions.

The trajectory-control role changes with architecture. [[mohammadi-2026-star-ris-uav-mec-noma]] optimizes the UAV path jointly with STAR-RIS phase shifts, transmit powers, and task-bit allocation inside a BCD/SCA energy-minimization loop, while [[xiao-2025-star-ris-bidirectional-uav-mec]] optimizes the path for energy-efficient bidirectional STAR-RIS offloading. [[qin-2023-ris-uav-mec-ee]] shows the fixed-RIS version: the UAV trajectory shifts toward the building-mounted RIS when the reflected channel is optimized, [[huang-2025-fedx-ris-uav-trajectory]] accelerates SAC/PPO trajectory training for RIS-assisted UAV communication through [[fedx-training-acceleration]], and [[sheng-2025-ris-online-uav-mec]] turns RIS-assisted trajectory/resource allocation into an online Lyapunov problem under mobile users and random task arrivals. [[wang-2026-secure-lae-uav-scheduling]] treats trajectory and velocity as secrecy-energy-efficiency variables because UAVs must decide when to communicate, jam, approach users, or suppress eavesdroppers. [[tong-2026-uneven-terrain-uav-mec]] treats 3D safe flight over uneven terrain as the first level of a hierarchical DRL controller, with task allocation triggered by the set of UEs currently covered. In the LAE ISAC line [[ye-2026-deeplsc-lae-isac]], [[ye-2026-meta-deepesc-lae-isac]], and [[ye-2026-mode-lae-isac]], authorized UAV trajectories are continuous DRL actions coupled to GBS beamforming and constrained by mission completion, collision avoidance, sensing, and GBS transmit power. [[liu-2025-multimodal-semantic-iov-jamming]] uses trajectory control to maintain multi-modal semantic links under jamming. [[zhao-2026-hcdrl-ga-sagin-sar]] couples trajectory with SAGIN offloading and GA deployment for SAR under wind fields, while [[ji-2026-llm-iov-uav-offloading]] solves 3D vehicular-coverage trajectory planning through SOCP before resource scheduling and LP offloading.

The same control surface also appears in placement-, inspection-, maritime-, and secure-data-collection forms: [[wang-2025-ppo-uav-positioning-offloading]] learns UAV placement with task splitting, [[guo-2026-aot-uav-inspection-offloading]] treats the inspection route as a Transformer-encoded TSP-like decision, [[wu-2026-model-based-ppo-ris-uav-mec]] couples decentralized trajectories to RIS phase recommendations and offloading, [[liao-2026-aoi-ris-uav-usv-mec]] optimizes RUAV trajectories for AoI-energy tradeoffs in RIS-assisted UAV-USV MEC, and [[cai-2026-llm-drl-secure-lae-data]] coordinates a data-collection UAV with a jamming UAV for secure LAE updates. [[zhao-2026-adaptive-wdc-wet-lae]] uses trajectories to balance WDC freshness against WET energy urgency, [[zhou-2026-radar-energy-iscac]] jointly optimizes UAV/HAP trajectories for radar sensing data versus energy, and [[zhu-2026-hab-mappo-target-search]] controls continuous 3D target-search trajectories under altitude-dependent sensing fidelity and image-offloading constraints. [[ebrahimi-not-in-parse-autonomous-uav-localization-rl]] adds an adjacent [[rss-based-uav-localization]] case where waypoint choices are trained to reduce ground-object localization error rather than communication/offloading cost. [[wang-2026-bayesian-uav-spectrum-mapping]] adds [[information-driven-uav-spectrum-mapping]], where trajectory control selects high-information spectrum-sensing waypoints; [[belgiovine-not-in-parse-multidt-abs-deployment]] uses differentiable ray tracing to recover mission-critical coverage; [[jiang-2026-bi-level-uav-delivery-safety]] enforces [[target-level-of-safety]] in delivery paths; and [[heo-not-in-parse-blockage-aided-multiuav-interference]] uses [[building-blockage-aided-interference-coordination]] to place UAVs so buildings attenuate interference.

Newer trajectory-control variants add infrastructure, QoS, security, privacy, sensing, logistics, and compliance coupling: [[ye-2026-flight-speed-battery-swapping]] schedules flight speeds jointly with battery swaps and offloading, [[hu-2026-ertatd3-secure-caching]] learns UAV motion with secure vehicular caching, [[feng-2026-prediction-service-migration]] combines trajectory control with prediction-assisted service migration, [[chen-2026-qos-noma-multiuav]] jointly controls 3D trajectories and priority-aware NOMA offloading, [[diallo-2026-system-cost-uav-leo-offloading]] optimizes UAV paths with LEO task scheduling and task dropping, [[tang-2026-hg-maddpg-uav-rescue]] uses UAV exploration trajectories inside low-altitude rescue, [[zhao-2026-temporal-spectrum-cartography]] moves UAV sensors to reduce temporal spectrum-map reconstruction error, [[gong-2026-safe-economic-lae-trajectory]] treats urban safety and airspace compliance as first-class trajectory constraints, [[beishenalieva-2026-secrecy-aware-uav-path-planning]] uses policy-gradient control for secrecy-aware ITS offloading, [[wu-2026-secure-split-offloading-ci]] couples dual-UAV trajectories to secure collaborative inference, and [[wu-2026-service-oriented-segmented-trajectory]] turns smart-window privacy into a trajectory-refinement constraint. [[li-2026-control-based-uav-isac]] adds a dynamics-first ISAC variant where [[control-parameterized-uav-trajectory]] planning accounts for 3-DoF and 6-DoF UAV motion before judging communication-rate and sensing-threshold feasibility. [[li-2026-aerial-ris-trajectory-phase]] ties motion to [[tilt-aware-aerial-ris-control]], [[hosseini-2026-aoi-covert-uav]] couples trajectory to covert AoI and public-cover PD-NOMA, [[bai-2026-aoi-uav-isac]] couples trajectory to freshness-aware ISAC beams, and [[liu-2026-spherical-t-ris-bs]] co-optimizes UAV 3-D trajectories with spherical T-RIS phases, scheduling, and transmit power. Adjacent non-MEC trajectory papers include [[you-2019-rician-uav-data-harvesting]] for outage-aware 3-D data-harvesting paths, [[lee-2026-uav-delivery-time-energy]] for payload-aware pickup/drop-off delivery routes, [[zhu-2026-uav-localization-jamming]] for sensing-UAV trajectories under jamming, [[cao-2026-uav-self-tracking-ms-mm]] for self-tracking from onboard array observations, [[du-2025-autonomous-intelligent-uav-swarms]] for the broader swarm-autonomy planning taxonomy, and [[gong-2026-uav-3d-visual-coverage]] for [[path-aware-3d-visual-coverage]] where viewpoint selection and propulsion-energy trajectory planning are coupled.

[[hua-2026-ddrl-content-delivery]] adds [[uav-content-caching]] to the mobility coupling: a route changes user access delay, energy use, and the BS backhaul cost of a cache miss, while a CNN-GRU PPO policy controls movement alongside transmission behavior.

[[meng-2026-uav-isac-corrections]] repairs the convexified trajectory/rate block in periodic UAV-ISAC, while [[liu-2026-usp-nfrp-emergency-communication]] turns trajectories into closed replacement loops for [[persistent-emergency-uav-swarm-service]] under fixed-wing return-energy constraints.

Wireless powering and collection add four trajectory couplings: [[wang-2026-wutf-fair-communication]] trades fair coverage against tower access and propulsion energy; [[li-2023-energy-constrained-uav-data-collection]] chooses depot-returning hover tours under one battery budget; [[morshed-2026-active-ris-uav-noma-mappo]] couples motion to active-RIS gain/phase and NOMA power; and [[wang-2026-glint-aoi-wireless-powered-edge]] resolves UAV position/association before charging-time and update scheduling.
