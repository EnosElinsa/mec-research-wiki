---
type: concept
title: "Integrated Sensing and Communication (ISAC)"
tags: [isac, dual-function, beamforming, 6g]
related:
  - "[[ning-2026-uav-isac-secure-beamforming]]"
  - "[[kanani-2026-haps-uav-isac]]"
  - "[[chen-2026-pointrl-uav-isac]]"
  - "[[lv-2026-isac-sar-tlsp]]"
  - "[[lyu-2023-isac-maneuver-beamforming]]"
  - "[[yao-2026-transformer-mean-field-isac-sagin]]"
  - "[[deng-2025-covert-isac-trajectory]]"
  - "[[zhou-2026-jrc-multiuav-resource]]"
  - "[[low-altitude-intelligent-network]]"
  - "[[high-altitude-platform-station]]"
  - "[[benaya-2025-aerial-isac-haps]]"
  - "[[jiang-2025-isac-lae-overview]]"
  - "[[huang-2026-offgrid-lae-imager]]"
  - "[[hou-2025-pbia-air-iscc-uav-its]]"
  - "[[ye-2026-deeplsc-lae-isac]]"
  - "[[ye-2026-meta-deepesc-lae-isac]]"
  - "[[ye-2026-mode-lae-isac]]"
  - "[[networked-isac]]"
  - "[[zhao-2025-networked-isac-uav-handover]]"
  - "[[li-2026-isac-vec-beamforming-deployment]]"
  - "[[wang-2026-stbc-cooperative-isac]]"
  - "[[li-2026-control-based-uav-isac]]"
  - "[[control-parameterized-uav-trajectory]]"
  - "[[wang-2026-rmaddpg-dda-uav-isac-vehicular]]"
  - "[[rmaddpg-dda-uav-isac-control]]"
  - "[[hazarika-2026-dynamo-uav-vehicle-tracking]]"
  - "[[dynamic-target-prioritization-metric]]"
  - "[[bai-2026-aoi-uav-isac]]"
  - "[[aoi-centric-uav-isac-beam-control]]"
  - "[[yan-not-in-parse-multibs-isac-uav-trajectory]]"
  - "[[multi-bs-feature-fusion-isac]]"
  - "[[bayessa-not-in-parse-uav-isac-secure-content-hdrl]]"
  - "[[action-masked-hierarchical-drl]]"
  - "[[zhang-2025-cooperative-anti-uav-isac]]"
  - "[[cooperative-isac-transceiver-beamforming]]"
  - "[[meng-2026-uav-isac-corrections]]"
  - "[[xu-2026-hecta-predictive-beamforming]]"
  - "[[historical-echo-predictive-beamforming]]"
  - "[[qin-2023-symmetry-augmented-uav-isac]]"
  - "[[tian-2026-joint-localization-communication]]"
  - "[[joint-localization-and-communication]]"
  - "[[zhang-2026-air-sea-isac-inspection]]"
  - "[[wang-2026-robust-anti-uav-isac]]"
  - "[[wang-2025-cellular-uav-cooperative-detection]]"
  - "[[jing-2024-isac-trajectory-localization]]"
  - "[[lu-2026-icsn-beamforming]]"
  - "[[integrated-communication-sensing-navigation]]"
  - "[[bi-traveling-salesman-problem-with-neighborhoods]]"
  - "[[ground-air-cooperative-isac-detection]]"
  - "[[guo-2026-dual-objective-multiuav-isac]]"
  - "[[dual-objective-multi-uav-isac]]"
  - "[[jiang-2026-sensing-assisted-uav-tracking]]"
  - "[[lu-2026-multiuav-iscpt]]"
  - "[[jiang-2026-ray-antenna-array]]"
  - "[[ray-antenna-array]]"
created: 2026-05-29
updated: 2026-07-14
---

# Integrated Sensing and Communication (ISAC)

A 6G design pattern in which the **same RF hardware and waveform** simultaneously serves communication users and senses targets via radar-style echo processing. The motivation is dual: cut hardware cost in half by sharing front ends, and extract sensing information (target position, velocity, RCS) from signals that are already in the air for communication.

Two competing design philosophies appear in the wiki:

- **Dual-function waveform** — beamforming matrix splits energy across communication and sensing streams. See [[benaya-2025-aerial-isac-haps]] for a HAPS-mounted full-duplex example.
- **Time-division multiplexing (TDM-ISAC)** — alternate slots between sensing and communication, simpler to implement.

ISAC complicates [[physical-layer-security]] because the sensing operation can leak information to an eavesdropper that's also being tracked. [[benaya-2025-aerial-isac-haps]] uses an aerial friendly jammer to neutralize this leak.

For a high-level survey of ISAC in the LAE context, see [[jiang-2025-isac-lae-overview]] and [[wang-2025-lae-network-survey]]. The corpus now also has LAE control instances: [[ye-2026-deeplsc-lae-isac]] uses DDPG to jointly control GBS beamforming and UAV trajectories for sum-rate under sensing constraints, while [[ye-2026-meta-deepesc-lae-isac]] shifts the objective to energy efficiency and adds meta-learning for flight-period adaptation. [[ye-2026-mode-lae-isac]] turns that LAE line into a multi-objective communication/sensing controller using [[mixture-of-experts-drl]], and [[zhao-2025-networked-isac-uav-handover]] moves from single-cell ISAC links to multi-BS [[networked-isac]] tracking and sensing-cell handover. In VEC, [[li-2026-isac-vec-beamforming-deployment]] uses ISAC metrics to jointly shape UAV deployment and beamforming for temporary road hot spots.

The aerial and maritime cases expose several other forms of coupling. [[zhang-2026-air-sea-isac-inspection]] jointly routes a UAV and USV under sensing, communication, and propulsion constraints; [[wang-2026-robust-anti-uav-isac]] schedules spatially separated transmit/receive roles under target-position uncertainty; [[wang-2025-cellular-uav-cooperative-detection]] fuses ground and airborne estimates; and [[jing-2024-isac-trajectory-localization]] repeatedly updates the UAV path as accumulated range estimates improve. [[lu-2026-icsn-beamforming]] extends the label to [[integrated-communication-sensing-navigation]], although its navigation output is angular information rather than an end-to-end navigation-error model.

[[guo-2026-dual-objective-multiuav-isac]] adds explicit [[dual-objective-multi-uav-isac]] optimization: communication sum rate and target-location CRB remain separate objectives while trajectories, powers, and user/target associations are evolved into a Pareto archive.

[[huang-2026-offgrid-lae-imager]] adds a cooperative cellular-ISAC imaging view: multiple BSs use raw CSI to reconstruct sparse low-altitude aerial images and mitigate off-grid errors with physics-embedded learning. [[hou-2025-pbia-air-iscc-uav-its]] extends the same sensing/communication substrate into Air-ISCC, where UAV swarms also compute IoTD tasks in ITS scenarios.

[[wang-2026-stbc-cooperative-isac]] adds the shared-resource physical-layer version: multi-BS cooperative ISAC uses robust inter-BS nulling, a [[space-time-block-codec]], and SINR-weighted data fusion to sense low-altitude UAVs near cell edges without allocating fully orthogonal resources.

[[li-2026-control-based-uav-isac]] adds a control-theoretic UAV-ISAC design: communication/sensing beamforming is optimized with SCA/SDR, while the UAV trajectory is represented through 3-DoF or 6-DoF dynamics and [[control-parameterized-uav-trajectory|control parameterization]] so planned sensing constraints remain meaningful for actual flight.

Vehicular UAV-ISAC sources extend the same idea into moving-road targets. [[wang-2026-rmaddpg-dda-uav-isac-vehicular]] uses [[rmaddpg-dda-uav-isac-control]] to adapt UAV motion, yaw, communication power, and ISAC transmit power for moving vehicles, while [[hazarika-2026-dynamo-uav-vehicle-tracking]] uses prediction, CRLB/FIM optimization, and [[dynamic-target-prioritization-metric|DTPM]] to decide which fast-moving vehicle should receive the next sensing update. [[bai-2026-aoi-uav-isac]] makes update freshness the primary UAV-ISAC objective through [[aoi-centric-uav-isac-beam-control]], coupling SAC motion decisions, Kalman target prediction, and RZF communication beams.

Newer secure and networked entries widen the ISAC role. [[yan-not-in-parse-multibs-isac-uav-trajectory]] uses [[multi-bs-feature-fusion-isac]] to track UAV trajectories from asynchronous cellular-ISAC observations, while [[bayessa-not-in-parse-uav-isac-secure-content-hdrl]] uses ISAC sensing to localize UAV eavesdroppers before [[action-masked-hierarchical-drl]] controls caching, association, deployment, and beamforming for secure content delivery.

[[zhang-2025-cooperative-anti-uav-isac]] uses [[cooperative-isac-transceiver-beamforming]] for multi-cell anti-UAV surveillance, optimizing sensing SCNR together with communication SINR and BS power while comparing centralized coordination with multiplier-exchanging distributed control.

[[meng-2026-uav-isac-corrections]] documents a formulation-level correction for periodic UAV-ISAC: it removes a duplicated association factor, replaces an unsupported Hessian claim with an auxiliary-variable/Taylor transformation, and confirms that the resulting rate subproblems are convex.

[[xu-2026-hecta-predictive-beamforming]] adds a communication-centric ISAC use: historical matched-filtered echoes are fed directly to [[historical-echo-predictive-beamforming|HECTA-Net]] to predict the next BS transmit and UAV receive beams, without first estimating a kinematic state or explicit CSI.

[[kanani-2026-haps-uav-isac]] adds [[haps-uav-isac-resource-allocation]]: HAPS processes a two-slot multi-UAV architecture while NSGA-II preserves separate target-echo and minimum-user-SINR objectives on a Pareto front.

[[chen-2026-pointrl-uav-isac]] adds [[radar-point-cloud-driven-uav-isac]]: 3-D vehicle-shape returns feed a branched DQN controller for horizontal trajectory, power, radar capacity, and U2V fairness.

[[jiang-2026-ray-antenna-array]] adds the receiver-hardware view through a [[ray-antenna-array]]: radially oriented subarrays and switch-based ray selection provide direction-independent angular resolution under stated assumptions, followed by MUSIC, zero forcing, and delay-Doppler processing for OFDM UAV-swarm ISAC.
