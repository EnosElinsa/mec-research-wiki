---
type: source
modeling_card: not_applicable
title: "PolarFix: Fixing Polarization Mismatch for UAV mmWave Communication Enhancement"
authors: ["Hongqiang Zhang", "Chengcheng Zhao", "Yuanchao Shu", "Jie Xiong", "Peng Cheng"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3668716"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), vol. 25, no. 8, pp. 11804-11820"
tags: [source, mmwave, uav-communication, polarization, metasurface, beamforming, hardware-prototype]
related:
  - "[[polarization-matched-uav-mmwave-metasurface]]"
  - "[[air-to-ground-channel-model]]"
  - "[[blockage-aware-channel-model]]"
created: 2026-07-14
updated: 2026-07-16
---

# PolarFix: Fixing Polarization Mismatch for UAV mmWave Communication Enhancement

## Citation

Zhang, H., Zhao, C., Shu, Y., Xiong, J., & Cheng, P. (2026). *PolarFix: Fixing Polarization Mismatch for UAV mmWave Communication Enhancement*. **IEEE Transactions on Mobile Computing, 25**(8), 11804-11820. DOI: 10.1109/TMC.2026.3668716.

## TL;DR

Places a passive linear-to-circular polarization converter and a programmable 1-bit transmissive metasurface in front of COTS 60 GHz hardware, stabilizing orientation-sensitive UAV links while UWB-guided beam steering restores gain and supports multiple directional beams.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zhang et al. [x] presented PolarFix for polarization mismatch caused by orientation changes in COTS 60 GHz UAV links. The system places a passive linear-to-circular polarization metasurface and a programmable 1-bit transmissive metasurface in front of the access-point radio without modifying its baseband, MAC, antennas, or synchronization. UWB position updates guide analytical phase control for beam steering, while a 3D clustering procedure shares the aperture among multiple UAV directions. The separation between the two metasurfaces is selected from Fabry-Perot cavity analysis to support constructive transmission. Ground-based measurements report a 63% average static-rate increase over all tested distances and yaw angles relative to the no-metasurface configuration, and the tuned separation gives a 23% higher mean mobile rate than the tested alternative separation on the 1 m/s circular path.

## Problem and system model

COTS 802.11ad devices use linearly polarized arrays. Even with correct beam direction, UAV roll/yaw can rotate the receiving antenna toward orthogonality and sharply reduce power. The paper measures up to 36% throughput loss from yaw at 10 m and separates this polarization failure from blockage and beam misalignment.

PolarFix is physically symmetric for uplink and downlink. A passive L2C layer converts linear waves to circular polarization so any rotated linear receiver captures one component. A programmable 1-bit layer steers and focuses the incident linear wave before conversion, offsetting conversion/insertion loss. Fabry-Perot cavity analysis selects the inter-layer distance for constructive transmission.

## Method

The [[polarization-matched-uav-mmwave-metasurface]] prototype combines PCB-manufacturable 56-64 GHz L2C elements, binary phase cells, an STM32 driver, analytical position-to-phase control, UWB localization, and 3-D clustering for multi-UAV beam sharing. It does not modify the transceiver baseband, MAC, antennas, or synchronization.

## Key findings

- Across static vertical distances and yaw angles, both metasurfaces raise average physical rate by 63% over the no-metasurface COTS baseline.
- At 1 m/s on the emulated circular path, the optimized inter-metasurface spacing raises mean rate by 23% over a nearby arbitrary spacing.
- Position-guided beam updates maintain robust rates through tested motion up to 2 m/s; the paper estimates, rather than demonstrates, support near 26.3 m/s from beamwidth and roughly 100 ms loop latency.
- Multiple beams maintain links to three endpoints; clustering the larger multi-endpoint case reduces beam splitting and improves rate consistency.

## Limitations

The hardware is mounted on a DJI Matrice 100, but the 4.2+ kg platform is evaluated through equivalent ground motion because outdoor flight would require special licensing. Tests are LoS-only, the UWB setup covers roughly 100 x 100 m and cannot accurately track all seven UAV endpoints simultaneously, the moving tests stop at 2 m/s, and the prototype/LED driver is large relative to COTS radios. The paper is therefore a ground-based radio prototype, not a real-flight validation.

## Relation to the corpus

PolarFix adds polarization as a third mmWave mobility failure mode alongside beam misalignment and [[blockage-aware-channel-model|blockage]]. Unlike reflective RIS links, both layers are transmissive and close to the radio path, and the main contribution is a measured COTS physical-layer system rather than an optimized channel model.

## Raw artifacts

- Parse: `raw/sources/PolarFix_Fixing_Polarization_Mismatch_for_UAV_mmWave_Communication_Enhancement/PolarFix_Fixing_Polarization_Mismatch_for_UAV_mmWave_Communication_Enhancement.md`
- Origin PDF and extracted figures (`images/`) are in the same folder.
