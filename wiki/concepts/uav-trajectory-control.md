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
  - "[[gong-2026-safe-economic-lae-trajectory]]"
created: 2026-05-28
updated: 2026-07-07
---

# UAV Trajectory Control

The continuous-action portion of the [[multi-uav-assisted-mec]] decision vector: choosing the per-step displacement of each UAV. In [[liu-2026-jppo-en-convntm]] the controller assumes:

- constant cruise speed $v_u = 10$ m/s during data-collection mode
- hover during charging
- fixed flight altitude $h_u = 35$ m
- per-step displacement bounded by $D_{\max}$

The objective is shaped by the [[equilibrium-efficiency-metric]] — coverage and fairness pull the UAV outward toward sparsely-visited regions, while the energy term and obstacle/inter-UAV penalties pull it back. Trajectories are sampled from a Gaussian policy head; see [[j-ppo]] for how this couples with the discrete decisions.

The trajectory-control role changes with architecture. [[mohammadi-2026-star-ris-uav-mec-noma]] optimizes the UAV path jointly with STAR-RIS phase shifts, transmit powers, and task-bit allocation inside a BCD/SCA energy-minimization loop, while [[xiao-2025-star-ris-bidirectional-uav-mec]] optimizes the path for energy-efficient bidirectional STAR-RIS offloading. [[qin-2023-ris-uav-mec-ee]] shows the fixed-RIS version: the UAV trajectory shifts toward the building-mounted RIS when the reflected channel is optimized, and [[sheng-2025-ris-online-uav-mec]] turns RIS-assisted trajectory/resource allocation into an online Lyapunov problem under mobile users and random task arrivals. [[wang-2026-secure-lae-uav-scheduling]] treats trajectory and velocity as secrecy-energy-efficiency variables because UAVs must decide when to communicate, jam, approach users, or suppress eavesdroppers. [[tong-2026-uneven-terrain-uav-mec]] treats 3D safe flight over uneven terrain as the first level of a hierarchical DRL controller, with task allocation triggered by the set of UEs currently covered. In the LAE ISAC line [[ye-2026-deeplsc-lae-isac]], [[ye-2026-meta-deepesc-lae-isac]], and [[ye-2026-mode-lae-isac]], authorized UAV trajectories are continuous DRL actions coupled to GBS beamforming and constrained by mission completion, collision avoidance, sensing, and GBS transmit power. [[liu-2025-multimodal-semantic-iov-jamming]] uses trajectory control to maintain multi-modal semantic links under jamming. [[zhao-2026-hcdrl-ga-sagin-sar]] couples trajectory with SAGIN offloading and GA deployment for SAR under wind fields, while [[ji-2026-llm-iov-uav-offloading]] solves 3D vehicular-coverage trajectory planning through SOCP before resource scheduling and LP offloading.

The same control surface also appears in placement-, inspection-, maritime-, and secure-data-collection forms: [[wang-2025-ppo-uav-positioning-offloading]] learns UAV placement with task splitting, [[guo-2026-aot-uav-inspection-offloading]] treats the inspection route as a Transformer-encoded TSP-like decision, [[wu-2026-model-based-ppo-ris-uav-mec]] couples decentralized trajectories to RIS phase recommendations and offloading, [[liao-2026-aoi-ris-uav-usv-mec]] optimizes RUAV trajectories for AoI-energy tradeoffs in RIS-assisted UAV-USV MEC, and [[cai-2026-llm-drl-secure-lae-data]] coordinates a data-collection UAV with a jamming UAV for secure LAE updates.

Newer trajectory-control variants add infrastructure, QoS, and compliance coupling: [[ye-2026-flight-speed-battery-swapping]] schedules flight speeds jointly with battery swaps and offloading, [[hu-2026-ertatd3-secure-caching]] learns UAV motion with secure vehicular caching, [[feng-2026-prediction-service-migration]] combines trajectory control with prediction-assisted service migration, [[chen-2026-qos-noma-multiuav]] jointly controls 3D trajectories and priority-aware NOMA offloading, and [[gong-2026-safe-economic-lae-trajectory]] treats urban safety and airspace compliance as first-class trajectory constraints.
