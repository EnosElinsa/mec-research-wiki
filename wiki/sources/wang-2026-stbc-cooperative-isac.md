---
type: source
title: "Space-Time Block Codec Based Cooperative Integrated Sensing and Communication System"
authors: ["Lin Wang", "Zhiyong Feng", "Zhiqing Wei", "Xinyi Wang", "Dingyou Ma", "Zesong Fei"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3655733"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, integrated-sensing-and-communication, networked-isac, cooperative-sensing, space-time-block-codec, low-altitude-economy]
related:
  - "[[integrated-sensing-and-communication]]"
  - "[[networked-isac]]"
  - "[[space-time-block-codec]]"
  - "[[cramer-rao-bound]]"
  - "[[low-altitude-intelligent-network]]"
  - "[[zhiyong-feng]]"
created: 2026-07-07
updated: 2026-07-16
modeling_card: not_applicable
---

# Space-Time Block Codec Based Cooperative Integrated Sensing and Communication System

## Citation

Wang, L., Feng, Z., Wei, Z., Wang, X., Ma, D., & Fei, Z. (2026). *Space-Time Block Codec Based Cooperative Integrated Sensing and Communication System*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2026.3655733. DOI appears in parse; venue/year are verified against a title-matched Crossref/IEEE DOI record.

## TL;DR

Proposes a multi-BS cooperative [[integrated-sensing-and-communication]] system for low-altitude UAVs at cell edges. Neighboring base stations share the same time-frequency resources, suppress line-of-sight inter-BS interference through robust angular nulling, separate reflected echoes through a [[space-time-block-codec]] OFDM design, and fuse range-profile estimates by SINR.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Wang et al. [x] proposed a cooperative multi-base-station ISAC architecture for sensing low-altitude UAVs near cell boundaries while reusing time-frequency resources. Robust angular-region nulling suppresses direct line-of-sight interference between neighboring base stations. An Alamouti-style space-time block codec separates their OFDM sensing echoes, after which range-profile estimates are fused according to SINR. The reported nulling pattern reached approximately -80 dB depth and remained more tolerant of direction error than exact-angle nulling. The shared-resource design improved detection and positioning relative to single-base-station sensing while using 66.67% fewer time-frequency resources than the fully orthogonal multi-base-station scheme. SINR-weighted data fusion also produced substantially lower positioning error than the compared single-base-station and soft-fusion methods under the examined synchronization errors.

## Problem

Single-BS ISAC has limited sensing capability for UAVs near cell boundaries. Multi-BS cooperation can improve sensing, but if neighboring BSs reuse the same time-frequency resources, line-of-sight interference can overrun ADC dynamic range and reflected inter-BS signals can corrupt range, angle, and velocity estimation. Orthogonal resource allocation avoids interference but wastes spectrum.

## System model

Multiple BSs are connected to the same BBU through fronthaul links in a centralized RAN-style architecture. The parsed model focuses on three cooperative BSs with known coordinates, separate transmit and receive arrays, and clock synchronization after a cooperative sensing request. A modified 5G NR frame inserts sensing symbols into downlink time. BSs transmit space-time block coded ISAC signals over shared time-frequency resources and decode the received echoes to separate signals originating from different BSs.

## Method

The method first designs an interference-nulling beam pattern that creates robust angular-region nulls around LoS directions between BSs. It then uses a space-time block codec, with Alamouti-style coding for two BSs and generalized STBC structures for more BSs, to generate separable OFDM sensing echoes while carrying communication payloads. Finally, target estimates from different echoes are fused at the data level using weights based on range-profile SINR.

## Key findings

- The proposed angular-region nulling reaches about -80 dB null depth while remaining more robust to LoS direction errors than exact-angle nulling.
- The proposed multi-BS scheme improves detection probability over a single-BS scheme and can achieve the same detection performance at lower transmit power in the parsed comparison.
- Neighboring-BS echoes improve AoA estimation rather than acting only as interference; the plotted CRLB trends support the observed RMSE behavior.
- Range and radial-velocity estimation are slightly worse than a fully orthogonal multi-BS scheme, but the proposed shared-resource method reduces occupied time-frequency resources by 66.67%.
- SINR-weighted data fusion improves positioning precision by an order of magnitude over single-BS and soft-fusion schemes in the parsed results.
- With clock synchronization errors modeled as truncated Gaussian timing errors with 10 ns standard deviation and [-20, 20] ns bounds, the proposed fusion still outperforms soft fusion with perfect synchronization and maintains meter-level accuracy.

## Limitations / future work

The paper identifies high-speed targets as future work because time-varying target response can disrupt the orthogonality of the space-time block coded sensing signals.

## Relation to the corpus

This source strengthens the [[networked-isac]] branch next to [[zhao-2025-networked-isac-uav-handover]] and [[tang-2025-cooperative-isac-lae]]. Its emphasis is physical-layer coexistence under shared resources: robust inter-BS nulling, STBC echo separation, and SINR-weighted data fusion for LAE UAV sensing.

## Raw artifacts

- `raw/sources/Space-Time Block Codec Based Cooperative Integrated Sensing and Communication System/Space-Time Block Codec Based Cooperative Integrated Sensing and Communication System.md`
- Original PDF and extracted figures (`images/`) in the same folder.
