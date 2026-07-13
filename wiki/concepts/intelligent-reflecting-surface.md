---
type: concept
title: "Intelligent Reflecting Surface (IRS)"
tags: [communication, channel, beamforming, metasurface]
related:
  - "[[liu-2026-passive-6dma]]"
  - "[[passive-six-dimensional-movable-antenna]]"
  - "[[angle-dependent-irs-effective-aperture]]"
  - "[[guo-2026-irs-uav-isac-secrecy]]"
  - "[[li-2021-robust-ris-uav-secrecy]]"
  - "[[zhang-2026-irs-uav-covert-fbl]]"
  - "[[wang-2023-drl-irs-uav-trajectory]]"
  - "[[mahmoud-2021-uav-irs-iot-analysis]]"
  - "[[terahertz-communication]]"
  - "[[blockage-aware-channel-model]]"
  - "[[csi-estimation-error]]"
  - "[[wu-2025-iopo-irs-uav-thz-mec]]"
  - "[[star-ris]]"
  - "[[spherical-transmissive-ris]]"
  - "[[qin-2023-ris-uav-mec-ee]]"
  - "[[mohammadi-2026-star-ris-uav-mec-noma]]"
  - "[[liao-2025-ris-uav-usv-resource-allocation]]"
  - "[[wu-2026-model-based-ppo-ris-uav-mec]]"
  - "[[liao-2026-aoi-ris-uav-usv-mec]]"
  - "[[sheng-2025-ris-online-uav-mec]]"
  - "[[lin-2025-energy-effective-ris-multiuav-coverage]]"
  - "[[liu-2026-spherical-t-ris-bs]]"
  - "[[ning-2025-channel-aware-irs-uav]]"
  - "[[dynamic-irs-user-association]]"
  - "[[li-2026-directional-modulation-irs-uav]]"
  - "[[ahmed-2026-noma-irs-vehicular]]"
  - "[[fixed-point-irs-passive-beamforming]]"
  - "[[hu-2026-segmented-irs-cpn]]"
  - "[[beyond-diagonal-ris]]"
  - "[[huroon-2026-bd-ris-rsma-uav]]"
  - "[[mihertie-2026-aerial-irs-rsma-ee]]"
  - "[[yu-2026-ris-uav-iab-outage]]"
created: 2026-05-29
updated: 2026-07-14
---

# Intelligent Reflecting Surface (IRS)

A planar surface of many passive reflecting elements, each able to impose a tunable **phase shift** on the incident signal. By jointly configuring the per-element phases (the diagonal phase-shift matrix $\Phi = \mathrm{diag}(e^{j\phi_k})$), an IRS reshapes the wireless propagation environment — creating a controllable cascaded path that can restore coverage around blockages and boost the effective channel gain, without active RF chains or extra transmit power. Also called a reconfigurable intelligent surface (RIS).

In the wiki, [[wu-2025-iopo-irs-uav-thz-mec]] mounts an IRS in a multi-UAV [[terahertz-communication]] MEC system to counter THz blockage/path-loss, optimizing the IRS phases (stage 2) with the [[whale-optimization-algorithm]] given a fixed offloading decision. Removing the IRS or using random phases measurably lowers transmission speed and raises energy. Other corpus sources apply IRS/RIS to anti-jamming and secure beamforming — see [[sun-2024-active-passive-ris-receiver]] (cascaded active-passive RIS), [[sun-2024-mfris-semantic-antijamming]] ([[multi-functional-ris]]), [[michailidis-2024-secure-ris-uav-mec-iot]], [[mao-2025-irs-noma-fl-secrecy]], and [[zhang-2025-gan-td3-isac-active-ris]] (double-active-RIS ISAC).

Recent corpus uses broaden the RIS family beyond reflecting-only surfaces. [[qin-2023-ris-uav-mec-ee]] is the fixed-building RIS UAV-MEC anchor: the RIS assists NOMA offloading to a UAV-mounted MEC server and must be jointly optimized with transmit power, task-bit allocation, and UAV trajectory. [[sheng-2025-ris-online-uav-mec]] adds the online-control variant, where a building-mounted RIS relays UAV-to-AP traffic while Lyapunov/Dinkelbach/BCD decisions handle random arrivals, mobile users, and outage constraints. [[mohammadi-2026-star-ris-uav-mec-noma]] uses [[star-ris]] for simultaneous transmission/reflection in UAV-MEC, while [[liao-2025-ris-uav-usv-resource-allocation]] and [[liao-2026-aoi-ris-uav-usv-mec]] use UAV-mounted RIS elements to restore blocked inland-waterway MEC links and support AoI-aware UAV-USV service.

[[lin-2025-energy-effective-ris-multiuav-coverage]] adds a non-MEC coverage-control case: facade RIS panels assist multiple UAV mobile BSs, while [[triple-deep-q-network]] controls UAV trajectories and service scheduling under throughput-fairness screening.

[[liu-2026-spherical-t-ris-bs]] adds [[spherical-transmissive-ris]] as a BS-architecture branch: one omnidirectional feed plus a spherical transmissive RIS replaces a conventional antenna array and reduces angle-sensitive gain loss for dynamic low-altitude communications.

[[ning-2025-channel-aware-irs-uav]] adds [[dynamic-irs-user-association]] for multi-UAV communication: facade IRS elements can be partitioned among users, and MAPPO changes association as UAV positions and blockage states evolve.

[[huroon-2026-bd-ris-rsma-uav]] extends the surface model to [[beyond-diagonal-ris|group-connected BD-RIS]], where coupled cells form non-diagonal scattering blocks assigned to UAV groups. [[mihertie-2026-aerial-irs-rsma-ee]] instead keeps a conventional passive diagonal surface on the UAV and jointly optimizes it with [[rate-splitting-multiple-access]].
