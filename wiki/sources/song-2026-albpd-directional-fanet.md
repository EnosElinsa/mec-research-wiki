---
type: source
modeling_card: required
title: "A Robust Link Maintenance Algorithm for Directional UAV Networks Based on Breakage Probability Prediction"
authors: ["Yifei Song", "Shuai Wang", "Zhe Song", "Xuanhe Yang", "Gaofeng Pan", "Dusit Niyato", "George K. Karagiannidis"]
year: 2026
url: "https://doi.org/10.1109/TWC.2025.3627301"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, fanet, uav-communications, directional-antenna, mmwave, link-maintenance, breakage-prediction]
related:
  - "[[zhe-song]]"
  - "[[xuanhe-yang]]"
  - "[[shuai-wang]]"
  - "[[gaofeng-pan]]"
  - "[[directional-fanet-link-maintenance]]"
  - "[[stateless-geographic-fanet-routing]]"
  - "[[uav-mobile-relaying]]"
  - "[[wireless-backhaul]]"
  - "[[air-to-ground-channel-model]]"
  - "[[bujari-2018-stateless-fanet-routing]]"
  - "[[george-k-karagiannidis]]"
created: 2026-07-10
updated: 2026-07-16
---

# A Robust Link Maintenance Algorithm for Directional UAV Networks Based on Breakage Probability Prediction

## Citation

Song, Y., Wang, S., Song, Z., Yang, X., Pan, G., Niyato, D., & Karagiannidis, G. K. (2026). *A Robust Link Maintenance Algorithm for Directional UAV Networks Based on Breakage Probability Prediction*. **IEEE Transactions on Wireless Communications (IEEE TWC)**, 25, 6852-6868. DOI: 10.1109/TWC.2025.3627301.

## TL;DR

Proposes ALBP-D, an adaptive link-breakage-prediction algorithm for directional UAV networks. The method predicts distance-driven and angle-driven link breaks under UAV mobility, then adjusts communication range and beamwidth to extend mmWave-style directional FANET links without flooding the network with maintenance overhead.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A distributed directional FANET contains homogeneous half-duplex UAVs with directional transmitters and omnidirectional receivers. Gaussian mobility changes both distance and angular alignment, so a link is valid only inside a beam-dependent range and angular offset; neighbor positions are obtained from acknowledgements.

**Problem & objective**: ALBP-D is a robust link-maintenance control problem that maximizes predicted link lifetime, equivalently selecting communication distance and beamwidth so $\max\min(T_{\mathrm{distance}},T_{\mathrm{angle}})$ while limiting maintenance updates.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Communication distance | $r$ | continuous, bounded | Neighbor separation selected for the maintained link |
| Beamwidth | $\omega$ | continuous, antenna-bounded | Directional beamwidth used for the link |
| Maintenance count | $\ell$ | integer, $0\le\ell\le L$ | Number of distance/beamwidth adjustments |
| Neighbor state | $\hat{\mathbf s}$ | estimated continuous state | Position and motion used to predict breakage |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Link distance remains below the beam-dependent communication range |
| C2 | Angular offset remains within half the selected beamwidth |
| C3 | Adjustments stop when distance-break time exceeds angle-break time or $\ell=L$ |
| C4 | Beamwidth and distance remain within antenna and FANET geometry limits |

**Algorithm**: Estimate distance- and angle-breakage-time distributions → predict both break times from ACK position histories → adjust distance and beamwidth until the larger failure risk is balanced → choose the widest beam that avoids imminent distance breakage → stop at the adjustment limit and maintain the link.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Song et al. [x] studied robust link maintenance for directional UAV networks under mobility-driven distance and beam-angle breakage. ALBP-D predicts both breakage times from neighbor-table positions and adaptively adjusts communication distance and beamwidth with a bounded number of updates. The method stops when distance and angular risks are balanced or the adjustment limit is reached and selects the widest beam that avoids imminent distance failure. Simulations report roughly tenfold longer link lifetime and network-connectivity duration than the PLM and RPL baselines, together with five- to sevenfold maintenance-overhead efficiency improvements. A small prototype compares predicted and measured break times for a directional and an omnidirectional UAV node.

## Problem

Directional antennas and mmWave links can give UAV ad hoc networks high throughput and low latency, but UAV mobility changes both link distance and beam alignment. Narrow beams increase range but make angular misalignment more likely, so a link-maintenance method has to manage distance and angle fragility together.

## System model

- The paper studies a single-layer distributed flying ad hoc network with homogeneous, half-duplex, position-aware UAV nodes.
- The model uses a 2-D abstraction with directional transmit and omnidirectional receive behavior.
- Directional antenna gain is inversely related to beamwidth.
- A link is valid only when the receiver is within the beam-dependent range and the angular offset stays within half the beamwidth.
- Mobility is modeled through a Gaussian mobility model, and the analysis separates distance breakage from angular breakage.

## Method

ALBP-D derives probability distributions for distance and angular link-breakage times. Each node uses neighbor-table positions from ACKs to predict the two breakage times, then adaptively adjusts communication distance and beamwidth up to a maximum adjustment count `L`.

The algorithm stops when the distance-break time exceeds the angular-break time or when the adjustment limit is reached. The selected beamwidth is the widest beam that avoids imminent distance breakage while preserving angular robustness. The parsed complexity is `O(L*K)` per link and `O(m*L*K)` per node, with small constants such as `L <= 9` and `K <= 100`.

## Key findings

- The abstract reports roughly 10-fold improvement in link lifetime and network-connectivity duration over PLM/RPL baselines, plus 5-7-fold maintenance-overhead efficiency improvement.
- The simulation uses a 500 m by 500 m area, 30 UAVs, node speeds uniformly from -2 to 22 m/s, beamwidths of 30, 36, and 45 degrees, maintenance periods of 1-5 s, and about 20 minutes of operation under the parsed power settings.
- With large `L`, ALBP-D maintains network connectivity for 90% of nodes until energy depletion.
- Increasing initial beamwidth has limited effect; at `L = 9`, small beamwidth can reduce link duration by about 5%, but still outperforms PLM.
- Increasing node count from 30 to 50 increases maintained links under larger `L`.
- The method remains robust across tested Gauss-Markov memory factors.
- A small prototype uses a directional node, an omnidirectional UAV node, TrajAir trajectory data, one request frame per second, and an anechoic chamber. The predicted and measured break times are not identical because of Gaussian-motion mismatch, but their averages are close in the parsed evaluation.

## Limitations / future work

The local parse is silent on DOI, venue, and year; the bibliographic metadata above is title-matched DOI metadata. The paper's own future-work directions include heterogeneous networks, 3-D scenarios, blockage effects in urban or cluttered environments, and energy-aware duty cycling. The prototype is a small controlled demonstration rather than a full outdoor multi-UAV network.

## Relation to the corpus

This is a communications-foundation source rather than an MEC offloading formulation. It complements [[bujari-2018-stateless-fanet-routing]]: routing can avoid end-to-end state, but directional links still need beamwidth/range maintenance underneath. The concept [[directional-fanet-link-maintenance]] captures that lower-layer role for UAV mobile relaying, wireless backhaul, and mmWave-style aerial networks.

## Raw artifacts

- Parse: `raw/sources/A_Robust_Link_Maintenance_Algorithm_for_Directional_UAV_Networks_Based_on_Breakage_Probability_Prediction/A_Robust_Link_Maintenance_Algorithm_for_Directional_UAV_Networks_Based_on_Breakage_Probability_Prediction.md`
- Origin PDF: `raw/sources/A_Robust_Link_Maintenance_Algorithm_for_Directional_UAV_Networks_Based_on_Breakage_Probability_Prediction/A_Robust_Link_Maintenance_Algorithm_for_Directional_UAV_Networks_Based_on_Breakage_Probability_Prediction.pdf`
- Figures: `raw/sources/A_Robust_Link_Maintenance_Algorithm_for_Directional_UAV_Networks_Based_on_Breakage_Probability_Prediction/images/`
