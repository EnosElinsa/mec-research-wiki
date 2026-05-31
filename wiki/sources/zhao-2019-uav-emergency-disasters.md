---
type: source
title: "UAV-Assisted Emergency Networks in Disasters"
authors: ["Nan Zhao", "Weidang Lu", "Min Sheng", "Yunfei Chen", "Jie Tang", "F. Richard Yu", "Kai-Kit Wong"]
year: 2019
url: "https://doi.org/10.1109/MWC.2018.1800160"
venue: "IEEE Wireless Communications"
tags: [source, post-disaster-mec, uav-communications, uav-mobile-relaying, emergency-network, device-to-device, trajectory-design]
related:
  - "[[post-disaster-mec]]"
  - "[[uav-mobile-relaying]]"
  - "[[uav-trajectory-control]]"
  - "[[air-to-ground-channel-model]]"
  - "[[noma]]"
  - "[[zeng-2016-throughput-relaying]]"
  - "[[wu-2018-multiuav-minrate-trajectory]]"
  - "[[zhou-2024-jdl-abs-postdisaster-rescue]]"
  - "[[raivi-2024-jdaco-postdisaster-iot]]"
  - "[[lyu-2023-noma-marine-emergency-offloading]]"
created: 2026-06-01
updated: 2026-06-01
---

# UAV-Assisted Emergency Networks in Disasters

## Citation

Zhao, N., Lu, W., Sheng, M., Chen, Y., Tang, J., Yu, F. R., & Wong, K.-K. (2019). *UAV-Assisted Emergency Networks in Disasters*. **IEEE Wireless Communications**, 26(1), 45–51. DOI: 10.1109/MWC.2018.1800160. (The parse carries the DOI but no explicit publication date/volume → year, venue, volume/issue, and pages **web-confirmed** via dblp: IEEE Wireless Communications, vol. 26, no. 1, pp. 45–51, 2019, and flagged as such.)

## TL;DR

A **magazine-style unified framework** for UAV-assisted emergency networks when terrestrial base stations (BSs) are damaged by a disaster. It assembles three complementary schemes: (1) **joint trajectory + communication scheduling** of UAVs to serve ground devices alongside surviving BSs; (2) **UAV transceiver design + multihop device-to-device (D2D)** establishment to extend wireless coverage in areas with no surviving BS; and (3) **multihop UAV relaying** (optimizing UAV hovering positions) to exchange information between the disaster area and the outside. Simulations illustrate each scheme, and open research issues are discussed.

## Problem framing

When communications infrastructure is destroyed, emergency rescue needs a flexible network. UAVs acting as flying BSs offer mobility and rapid deployment. The article notes that prior UAV-communications work rarely addressed the specific disaster setting, and proposes a single framework spanning the three regimes — surviving-BS coexistence, no-BS coverage extension, and disaster-to-outside relaying.

## System model

- **Scenario 1 (surviving BSs).** UAVs jointly optimize flight **trajectory + communication scheduling** to serve mobile devices, while managing **interference** between BS-served and UAV-served devices.
- **Scenario 2 (no surviving BS).** A large-scale UAV with $M$ antennas at the disaster-area center (radius $R_1$, altitude $H$) provides coverage to $K$ single-antenna ground devices; uplink decoding vectors and downlink precoding designed via SOCP-based iterative optimization. **Multihop D2D** with a **shortest-path-routing (SPR)** algorithm extends coverage; outage probability analyzed via a Poisson-point-process model. A **NOMA** discussion covers the single-antenna-UAV case.
- **Multihop UAV relaying.** $N-1$ relay UAVs on a horizontal line at altitude $h$ link source and destination; received SNR analyzed for **amplify-and-forward (AF)** and **decode-and-forward (DF)** protocols under a Nakagami-m channel; air-to-air / air-to-ground path-loss parameters drawn from prior measurements.

## Method

- A descriptive **framework + scheme** article rather than a single optimization formulation: each of the three regimes carries its own design (joint trajectory/scheduling; SOCP transceiver + SPR D2D; AF/DF multihop relay hovering-position optimization), each illustrated by simulation.

## Key findings

- Simulation results demonstrate the effectiveness of all three schemes (the article reports qualitative effectiveness; specific curves are figure-derived and indicative).
- Joint trajectory + scheduling improves service when surviving BSs coexist, provided UAV-BS interference is properly avoided.
- Multihop D2D (via SPR) and multihop UAV relaying extend coverage / connect the disaster area to the outside, with AF/DF SNR characterized over the Nakagami-m channel.

## Limitations / future work

A magazine framework article; not a single rigorous optimization with convergence guarantees. It explicitly closes by pointing out **open research issues and challenges** for UAV-assisted emergency networks (stated, not enumerated as a formal list).

## Relation to the corpus

A **post-disaster / emergency-network** anchor ([[post-disaster-mec]]) that frames UAVs as flying BSs, D2D extenders, and multihop relays — predating and contextualizing the corpus's optimization-heavy post-disaster offloading sources [[zhou-2024-jdl-abs-postdisaster-rescue]] and [[raivi-2024-jdaco-postdisaster-iot]], and the NOMA marine-emergency offloading of [[lyu-2023-noma-marine-emergency-offloading]]. Its multihop-relaying component builds on the UAV mobile-relaying line ([[uav-mobile-relaying]]) — it cites [[zeng-2016-throughput-relaying]] (reference [2]) and the multi-UAV max-min-rate design [[wu-2018-multiuav-minrate-trajectory]] (reference [5]). A communications/coverage framing rather than compute offloading.

## Raw artifacts

- `raw/sources/UAV-Assisted_Emergency_Networks_in_Disasters/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
