---
type: source
title: "Toward Realization of Low-Altitude Economy Networks: Core Architecture, Integrated Technologies, and Future Directions"
authors: ["Yixian Wang", "Geng Sun", "Zemin Sun", "Jiacheng Wang", "Jiahui Li", "Changyuan Zhao", "Jing Wu", "Shuang Liang", "Minghao Yin", "Pengfei Wang", "Dusit Niyato", "Sumei Sun", "Dong In Kim"]
year: 2025
url: "https://doi.org/10.1109/TCCN.2025.3601015"
venue: "IEEE Transactions on Cognitive Communications and Networking"
tags: [source, survey, low-altitude-economy, lae, uav, evtol, gai, architecture, mec]
related:
  - "[[low-altitude-intelligent-network]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[hierarchical-aerial-mec]]"
  - "[[generative-ai-for-mec]]"
  - "[[wang-2025-uav-swarm-stackelberg]]"
created: 2026-05-28
updated: 2026-06-09
---

# Toward Realization of Low-Altitude Economy Networks: Core Architecture, Integrated Technologies, and Future Directions

## Citation

Wang, Y., Sun, G., Sun, Z., Wang, J., Li, J., Zhao, C., Wu, J., Liang, S., Yin, M., Wang, P., Niyato, D., Sun, S., & Kim, D. I. (2025). *Toward Realization of Low-Altitude Economy Networks: Core Architecture, Integrated Technologies, and Future Directions*. **IEEE Transactions on Cognitive Communications and Networking**. DOI: 10.1109/TCCN.2025.3601015.

## TL;DR

A **survey + architecture paper** on the low-altitude economy (LAE) — the rapidly emerging market combining UAVs, eVTOL aircraft, drone delivery, urban air mobility, and low-altitude IoT. Defines a six-layer LAE network architecture and surveys the integrated technologies (communication, sensing, computing, GAI, navigation, surveillance, flight control, airspace management) that support it.

This is the wiki's **panoramic foundation paper** — most other curated sources solve a narrow technical sub-problem within this larger LAE landscape.

## The 6-layer LAE network architecture

| Layer | Role |
|---|---|
| 1. Airborne Terminal & Physical Infrastructure | UAVs, eVTOLs, ground stations, vertiports |
| 2. Intelligent Collaboration & Digital Airspace | Multi-agent control, digital twin of airspace |
| 3. Multi-Collaboration & Service Assurance | Cross-operator service-level coordination |
| 4. Low-Altitude Supervision System | Regulatory authority — registration, traffic monitoring |
| 5. Low-Altitude Flight Service System | Flight planning, weather, NOTAMs |
| 6. Low-Altitude Flight Control System | Tactical control, deconfliction, ATC integration |

Layers 4–6 are governance / operations layers that the more technical MEC papers usually elide. The paper explicitly argues these *cannot* be ignored at scale.

## Integrated technology stack surveyed

- **Communications.** 5G-Advanced, LEO satellite augmentation, GAI-driven beamforming, semantic communication.
- **Sensing.** Active (radar, LiDAR) + passive (camera, RF), and collaborative cross-platform fusion.
- **Computing.** GAI-driven cloud–edge–end collaboration; **MEC** sits squarely here as the edge-tier compute.
- **Positioning / Navigation.** GNSS + INS + visual SLAM + 5G-positioning fusion.
- **Surveillance / Airspace management.** ADS-B, digital twins, AI-based deconfliction.
- **Flight control.** Advanced controllers + multi-agent coordination.

## Key applications discussed

- Low-altitude logistics (drone delivery — E-Hang, Zipline pilots cited)
- Low-altitude rescue
- Low-altitude transportation (urban air mobility)
- Low-altitude inspection (industrial, agricultural)

## Future directions highlighted

- Intelligent and adaptive **dynamic airspace** optimization (using GAI-enabled DRL, game theory, digital twins).
- **Quantum-driven** intelligence coordination — far horizon but explicitly flagged.
- Cross-tier integration: low-altitude with ground 5G/6G, with [[high-altitude-platform-station|HAPS]], with [[leo-satellite-edge-computing|LEO]].

## Why this paper anchors the wiki's LAE thread

- **Vocabulary.** The 6-layer architecture gives a stable taxonomy for placing future LAE-MEC papers.
- **Technology fusion.** Most narrow MEC papers assume an isolated communication stack; this paper reminds us that a real LAE system *must* fuse communication, sensing, computing, and control. Single-axis optimization is suboptimal.
- **Governance.** Reminds us that LAE networks operate inside a regulatory and surveillance frame that affects the optimization variables themselves (e.g. flight clearance is not a free trajectory variable).

## Cross-link with related sources

- Provides the umbrella for [[wang-2025-uav-swarm-stackelberg]] (LAE spectrum sharing).
- Provides the upper-tier integration story for [[peng-2025-drudm-cfg]] / [[hierarchical-aerial-mec]].
- The **GAI-driven MEC** thread (mentioned but not deeply elaborated here) deserves its own concept page when a more focused source enters the corpus.

## Limitations

- Survey, not original results — no quantitative benchmarks.
- Quantum-coordination section is speculative; readers should treat it as roadmap, not state-of-the-art.

## Raw artifacts

- Parse: `raw/sources/Toward_Realization_of_Low-Altitude_Economy_Networks_Core_Architecture_Integrated_Technologies_and_Future_Directions/full.md`
- Origin PDF: `raw/sources/Toward_Realization_of_Low-Altitude_Economy_Networks_Core_Architecture_Integrated_Technologies_and_Future_Directions/e609bbbb-d1d3-4e5b-84cc-22cbbc900778_origin.pdf`
- Figures: `raw/sources/Toward_Realization_of_Low-Altitude_Economy_Networks_Core_Architecture_Integrated_Technologies_and_Future_Directions/images/`
