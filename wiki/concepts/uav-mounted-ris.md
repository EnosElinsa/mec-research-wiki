---
type: concept
title: "UAV-Mounted RIS"
tags: [intelligent-reflecting-surface, uav, aerial, deployment, 6g]
related:
  - "[[intelligent-reflecting-surface]]"
  - "[[drone-cell-3d-placement]]"
  - "[[pan-2025-uav-ris-energy-efficient-comm]]"
  - "[[wu-2025-iopo-irs-uav-thz-mec]]"
  - "[[star-ris]]"
  - "[[mohammadi-2026-star-ris-uav-mec-noma]]"
  - "[[liao-2025-ris-uav-usv-resource-allocation]]"
created: 2026-06-03
updated: 2026-07-07
---

# UAV-Mounted RIS

A deployment in which a [[intelligent-reflecting-surface|reconfigurable intelligent surface (RIS)]] is carried by an uncrewed aerial vehicle rather than fixed to a building facade. The RIS itself is a passive, low-cost array that reflects incident signals with element-wise phase shifts; mounting it on a UAV adds **3D mobility and opportunistic deployment**, letting the surface be repositioned to establish a favorable reflected path (e.g. when the direct BS-to-user link is blocked) faster and more controllably than a fixed surface or a tethered balloon.

Design considerations that recur:

- **3D placement.** The UAV-RIS location is a continuous decision variable that, like [[drone-cell-3d-placement]], trades off coverage, path loss, and inter-surface interference when multiple UAV-RISs operate together.
- **Discrete phase shifts.** Practical RIS hardware quantizes element phases, so the passive-beamforming sub-problem is discrete rather than continuous.
- **Flight vs communication energy.** A UAV-RIS spends propulsion energy to hold or move its position in addition to any communication-side energy, so energy-efficiency objectives must account for both.

In the wiki, [[pan-2025-uav-ris-energy-efficient-comm]] studies **cooperative multiple** UAV-RISs serving multiple ground users, jointly optimizing BS beamforming, UAV-RIS 3D locations, and discrete phase shifts under a multi-objective (rate/fairness/energy) formulation. It is related to but distinct from [[wu-2025-iopo-irs-uav-thz-mec]], which couples an IRS-UAV with THz MEC offloading rather than pure communication.

The corpus also uses UAV-mounted RIS in MEC-specific roles. [[mohammadi-2026-star-ris-uav-mec-noma]] equips the UAV with a [[star-ris]] so transmitted and reflected paths can feed UAV-MEC and terrestrial MEC servers under NOMA. [[liao-2025-ris-uav-usv-resource-allocation]] mounts RIS elements on UAVs to assist blocked inland-waterway TBS-USV links in a [[maritime-mec]] setting.
