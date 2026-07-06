---
type: concept
title: "Intelligent Reflecting Surface (IRS)"
tags: [communication, channel, beamforming, metasurface]
related:
  - "[[terahertz-communication]]"
  - "[[blockage-aware-channel-model]]"
  - "[[csi-estimation-error]]"
  - "[[wu-2025-iopo-irs-uav-thz-mec]]"
  - "[[star-ris]]"
  - "[[qin-2023-ris-uav-mec-ee]]"
  - "[[mohammadi-2026-star-ris-uav-mec-noma]]"
  - "[[liao-2025-ris-uav-usv-resource-allocation]]"
created: 2026-05-29
updated: 2026-07-07
---

# Intelligent Reflecting Surface (IRS)

A planar surface of many passive reflecting elements, each able to impose a tunable **phase shift** on the incident signal. By jointly configuring the per-element phases (the diagonal phase-shift matrix $\Phi = \mathrm{diag}(e^{j\phi_k})$), an IRS reshapes the wireless propagation environment — creating a controllable cascaded path that can restore coverage around blockages and boost the effective channel gain, without active RF chains or extra transmit power. Also called a reconfigurable intelligent surface (RIS).

In the wiki, [[wu-2025-iopo-irs-uav-thz-mec]] mounts an IRS in a multi-UAV [[terahertz-communication]] MEC system to counter THz blockage/path-loss, optimizing the IRS phases (stage 2) with the [[whale-optimization-algorithm]] given a fixed offloading decision. Removing the IRS or using random phases measurably lowers transmission speed and raises energy. Other corpus sources apply IRS/RIS to anti-jamming and secure beamforming — see [[sun-2024-active-passive-ris-receiver]] (cascaded active-passive RIS), [[sun-2024-mfris-semantic-antijamming]] ([[multi-functional-ris]]), [[michailidis-2024-secure-ris-uav-mec-iot]], [[mao-2025-irs-noma-fl-secrecy]], and [[zhang-2025-gan-td3-isac-active-ris]] (double-active-RIS ISAC).

Recent corpus uses broaden the RIS family beyond reflecting-only surfaces. [[qin-2023-ris-uav-mec-ee]] is the fixed-building RIS UAV-MEC anchor: the RIS assists NOMA offloading to a UAV-mounted MEC server and must be jointly optimized with transmit power, task-bit allocation, and UAV trajectory. [[mohammadi-2026-star-ris-uav-mec-noma]] uses [[star-ris]] for simultaneous transmission/reflection in UAV-MEC, while [[liao-2025-ris-uav-usv-resource-allocation]] uses UAV-mounted RIS elements to restore blocked TBS-USV links for inland-waterway MEC.
