---
type: concept
title: "UAV-Mounted RIS"
tags: [intelligent-reflecting-surface, uav, aerial, deployment, 6g]
related:
  - "[[xie-2026-uav-irs-eppo]]"
  - "[[morshed-2026-active-ris-uav-noma-mappo]]"
  - "[[decentralized-active-ris-uav-noma-control]]"
  - "[[intelligent-reflecting-surface]]"
  - "[[drone-cell-3d-placement]]"
  - "[[pan-2025-uav-ris-energy-efficient-comm]]"
  - "[[wu-2025-iopo-irs-uav-thz-mec]]"
  - "[[star-ris]]"
  - "[[mohammadi-2026-star-ris-uav-mec-noma]]"
  - "[[xiao-2025-star-ris-bidirectional-uav-mec]]"
  - "[[liao-2025-ris-uav-usv-resource-allocation]]"
  - "[[liao-2026-aoi-ris-uav-usv-mec]]"
  - "[[li-2026-aerial-ris-trajectory-phase]]"
  - "[[tilt-aware-aerial-ris-control]]"
  - "[[zhang-2026-air-ground-covert-jamming]]"
  - "[[ris-assisted-directional-jamming]]"
  - "[[mihertie-2026-aerial-irs-rsma-ee]]"
  - "[[rate-splitting-multiple-access]]"
  - "[[peng-2023-dual-domain-eh-ris]]"
  - "[[dual-domain-ris-energy-harvesting]]"
  - "[[li-2026-secrecy-ee-uav-ris-iov]]"
  - "[[mahmoud-2021-uav-irs-iot-analysis]]"
created: 2026-06-03
updated: 2026-07-13
---

# UAV-Mounted RIS

A deployment in which a [[intelligent-reflecting-surface|reconfigurable intelligent surface (RIS)]] is carried by an uncrewed aerial vehicle rather than fixed to a building facade. The RIS itself is a passive, low-cost array that reflects incident signals with element-wise phase shifts; mounting it on a UAV adds **3D mobility and opportunistic deployment**, letting the surface be repositioned to establish a favorable reflected path (e.g. when the direct BS-to-user link is blocked) faster and more controllably than a fixed surface or a tethered balloon.

Design considerations that recur:

- **3D placement.** The UAV-RIS location is a continuous decision variable that, like [[drone-cell-3d-placement]], trades off coverage, path loss, and inter-surface interference when multiple UAV-RISs operate together.
- **Discrete phase shifts.** Practical RIS hardware quantizes element phases, so the passive-beamforming sub-problem is discrete rather than continuous.
- **Flight vs communication energy.** A UAV-RIS spends propulsion energy to hold or move its position in addition to any communication-side energy, so energy-efficiency objectives must account for both.

In the wiki, [[pan-2025-uav-ris-energy-efficient-comm]] studies **cooperative multiple** UAV-RISs serving multiple ground users, jointly optimizing BS beamforming, UAV-RIS 3D locations, and discrete phase shifts under a multi-objective (rate/fairness/energy) formulation. It is related to but distinct from [[wu-2025-iopo-irs-uav-thz-mec]], which couples an IRS-UAV with THz MEC offloading rather than pure communication.

[[mahmoud-2021-uav-irs-iot-analysis]] is the analytical single-link anchor: it derives error, capacity, and outage behavior for an ideally phase-aligned static UAV-mounted IRS and exposes quadratic average-SNR scaling with element count under its assumptions.

The corpus also uses UAV-mounted RIS in MEC-specific roles. [[mohammadi-2026-star-ris-uav-mec-noma]] equips the UAV with a [[star-ris]] so transmitted and reflected paths can feed UAV-MEC and terrestrial MEC servers under NOMA. [[xiao-2025-star-ris-bidirectional-uav-mec]] mounts the STAR-RIS horizontally and uses its reflection/transmission paths for same-slot bidirectional offloading to BS-MEC and UAV-MEC servers. [[liao-2025-ris-uav-usv-resource-allocation]] mounts RIS elements on UAVs to assist blocked inland-waterway TBS-USV links in a [[maritime-mec]] setting, while [[liao-2026-aoi-ris-uav-usv-mec]] uses a RIS-carried tethered UAV with RUAV service decisions for AoI-aware UAV-USV MEC. [[li-2026-aerial-ris-trajectory-phase]] adds [[tilt-aware-aerial-ris-control]], where Euler-angle motion and orientation-dependent RIS gain become first-class communication variables.

[[zhang-2026-air-ground-covert-jamming]] adds a security-oriented use: the UAV-mounted RIS assists decode-forward covert relay transmission while redirecting terrestrial jammer energy toward the warden rather than only improving the legitimate link.

[[morshed-2026-active-ris-uav-noma-mappo]] mounts an active RIS on the UAV and splits joint control across BS, platform, and surface agents. This [[decentralized-active-ris-uav-noma-control]] case explicitly counts static RIS power and dynamic amplifier power rather than treating the surface as passive or energetically free.

[[mihertie-2026-aerial-irs-rsma-ee]] mounts a passive continuous-phase IRS on one UAV and couples its deployment point to [[rate-splitting-multiple-access]] precoders and common-rate allocation. Its communication-side metric excludes propulsion and battery energy.

Two energy/security variants use the surface differently. [[peng-2023-dual-domain-eh-ris]] lets unscheduled elements harvest during information transmission through [[dual-domain-ris-energy-harvesting]], while [[li-2026-secrecy-ee-uav-ris-iov]] uses separate two-hop phase matrices to protect mobile vehicular traffic from an untrusted forwarding relay.
