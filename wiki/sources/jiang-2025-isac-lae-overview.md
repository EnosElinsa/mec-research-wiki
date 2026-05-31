---
type: source
title: "Integrated Sensing and Communication for Low Altitude Economy: Opportunities and Challenges"
authors: ["Yihang Jiang", "Xiaoyang Li", "Guangxu Zhu", "Hang Li", "Jing Deng", "Kaifeng Han", "Chao Shen", "Qingjiang Shi", "Rui Zhang"]
year: 2025
url: "https://doi.org/10.1109/MCOM.001.2400685"
venue: "IEEE Communications Magazine"
tags: [source, survey, isac, lae, low-altitude-economy, iagn, stochastic-geometry, channel-modeling]
related:
  - "[[integrated-sensing-and-communication]]"
  - "[[low-altitude-intelligent-network]]"
  - "[[wang-2025-lae-network-survey]]"
  - "[[benaya-2025-aerial-isac-haps]]"
  - "[[stochastic-geometry-network-analysis]]"
created: 2026-05-29
updated: 2026-06-01
---

# Integrated Sensing and Communication for Low Altitude Economy: Opportunities and Challenges

## Citation

Jiang, Y., Li, X., Zhu, G., Li, H., Deng, J., Han, K., Shen, C., Shi, Q., & Zhang, R. (2025). *Integrated Sensing and Communication for Low Altitude Economy: Opportunities and Challenges*. **IEEE Communications Magazine**. DOI: 10.1109/MCOM.001.2400685.

## TL;DR

A magazine-style overview of **ISAC for the low-altitude economy (LAE)**. The authors define the **integrated air-ground network (IAGN)** — the supporting infrastructure for cellular-connected aircraft — and walk through the technological prerequisites: cellular access for aircraft, spectrum sharing between aerial and ground users, 3D beamforming, interference cancellation, and active/passive sensing. They also cover aircraft-assisted functions: as aerial sensors, aerial base stations, relays, and traffic-offloading nodes.

Two technical anchors:

- **MBCM (Multi-Beam localized Channel Modeling)** under the SRCON framework — predicts SIR after BS antenna re-tilting using measured RSRP. Concrete tool, not just survey.
- **Stochastic geometry analysis** of an IAGN with PPP-distributed BSs, ground CUs, and aerial sensing targets. Performance metrics: ACCP (area communication coverage probability) under SIR + ARDCP (area radar detection coverage probability) under CFAR.

## Why this matters

This is the **survey-tier** companion to [[wang-2025-lae-network-survey]]. Where Wang et al. survey the *full LAE stack* (architecture, governance, applications), this paper zooms into the **physical-layer ISAC slice** of LAE.

Together they bracket the wiki's LAE thread:

| Question | Best survey reference |
|---|---|
| "What does the LAE stack look like end-to-end?" | [[wang-2025-lae-network-survey]] |
| "How do you do sensing + communication on the radio layer for LAE?" | This paper |
| "Concrete ISAC system + secrecy + computing offloading?" | [[benaya-2025-aerial-isac-haps]] |

## Key contributions

- **CNPC vs PC distinction.** Control & Non-Payload Communication (low-rate, high-reliability, low-latency for aircraft control) vs Payload Communication (high-rate, latency-tolerant, mission data). Useful vocabulary for LAE-MEC work across the corpus.
- **Localized channel modeling (MBCM).** Uses measured reference signals to model the channel angular power spectrum — better than purely statistical pathloss models, less expensive than full radio-map measurements.
- **Stochastic-geometry tradeoff analysis.** Formal coupling between communication coverage and sensing detection in a shared spectrum.

## Future directions flagged

- Aircraft collaboration (cooperative beamforming, cooperative sensing).
- Energy efficiency for ISAC at scale.
- AI-enabled LAE — explicit hand-off to the GAI thread that [[wang-2025-lae-network-survey]] develops.

## Cross-link with related sources

- **LAE thread anchor:** alongside [[wang-2025-lae-network-survey]] as the wiki's two LAE survey/overview entries. Treat them as the canonical references for vocabulary and scope.
- **Concrete ISAC instance:** [[benaya-2025-aerial-isac-haps]] picks up the full-duplex HAPS-mounted ISAC story.
- **Channel modeling:** the MBCM approach is a useful counterpoint to the **terrain-aware** model in [[wu-2026-terrain-aware-uav-mec]] (real-DEM-based) and the **statistical/Rician** models elsewhere in the corpus.

## Limitations

- Magazine paper — no full algorithms or experiments. Use it for terminology and architectural framing.
- Stochastic-geometry analysis is at the network level; says nothing about per-task offloading decisions.

## Raw artifacts

- `raw/sources/Integrated Sensing and Communication for Low Altitude Economy Opportunities and Challenges/full.md`
