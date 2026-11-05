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
updated: 2026-11-03
---

# A Robust Link Maintenance Algorithm for Directional UAV Networks Based on Breakage Probability Prediction

## Citation

Song, Y., Wang, S., Song, Z., Yang, X., Pan, G., Niyato, D., & Karagiannidis, G. K. (2026). *A Robust Link Maintenance Algorithm for Directional UAV Networks Based on Breakage Probability Prediction*. **IEEE Transactions on Wireless Communications (IEEE TWC)**, 25, 6852-6868. DOI: 10.1109/TWC.2025.3627301.

## TL;DR

Proposes ALBP-D, an adaptive link-breakage-prediction algorithm for directional UAV networks. The method predicts distance-driven and angle-driven link breaks under UAV mobility, then adjusts communication range and beamwidth to extend mmWave-style directional FANET links without flooding the network with maintenance overhead.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A distributed FANET of homogeneous half-duplex UAVs uses directional antennas after neighbor discovery. Relative motion follows a Gaussian velocity model, so a link breaks when the neighbor leaves the range $R$ (29) or its angular offset exceeds $BW/2$ (30)–(31); range scales inversely with beamwidth, $R\propto1/BW$ (2), and neighbor positions come from ACK frames.
**Problem & objective**: No formal optimization problem is stated. ALBP-D predicts the link break step $n_{\mathrm{break}}=\min\{n\mid P_{\mathrm{break}}(n)>0\}$ (5) from distance- and angle-breakage distributions, and adjusts communication range and beamwidth to lengthen the predicted link lifetime with at most $L$ range adjustments.
**Decision variables**:
| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Communication range | $R=R_{\mathrm{init}}+i\Delta R$ | continuous, $\le R_{\max}$ | Range used to maintain the link |
| Beamwidth | $BW=BW_{\mathrm{init}}R_{\mathrm{init}}/R$ | continuous, set by $R$ | Beamwidth implied by the chosen range |
| Adjustment index | $i$ | integer, $0\le i<L$ | Number of range increments applied |
**Constraints**:
| ID | Meaning and key expression |
|---|---|
| (29) | Distance breakage: $X_n^2+Y_n^2+Z_n^2>R^2$ |
| (30)–(31), (33) | Angular breakage: azimuth or elevation offset exceeds $BW/2$ |
| (40) | Adjustment limit: $L=\lceil(R_{\max}-R_{\mathrm{init}})/\Delta R\rceil$ |
| Algorithm rule | Stop when $n_{\mathrm{disBreak}}>n_{\mathrm{angBreak}}$ or $i\ge L$; report $n_{\mathrm{break}}=\min(n_{\mathrm{disBreak}},n_{\mathrm{angBreak}})$ |
**Algorithm**: Send maintenance frames and update neighbor positions from ACKs → for $i=0,\dots,L-1$, set $R=R_{\mathrm{init}}+i\Delta R$ and $BW=BW_{\mathrm{init}}/(R/R_{\mathrm{init}})$ → compute $n_{\mathrm{disBreak}}$ from the distance distribution (16) and $n_{\mathrm{angBreak}}$ from the angular distribution (23) → stop once distance breakage comes later than angular breakage → schedule the next maintenance at $n_{\mathrm{break}}$.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Song et al. [x] studied robust link maintenance for directional UAV networks under mobility-driven distance and beam-angle breakage. ALBP-D predicts both breakage times from neighbor-table positions and adaptively adjusts communication distance and beamwidth with a bounded number of updates. Each adjustment extends the range and narrows the beam, and the search stops once predicted distance breakage comes later than angular breakage or the adjustment limit is reached. Simulations report roughly tenfold longer link lifetime and network-connectivity duration than the PLM and RPL baselines, together with five- to sevenfold maintenance-overhead efficiency improvements. A two-node anechoic-chamber prototype driven by real UAV trajectories shows predicted break times close to, but not exactly matching, measured ones because the trajectories are not fully Gaussian.

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

The algorithm stops when the distance-break time exceeds the angular-break time or when the adjustment limit is reached. Each adjustment extends the range by $\Delta R$ and narrows the beam in proportion, and the reported break step is the smaller of the two predicted break times. The parsed complexity is `O(L*K)` per link and `O(m*L*K)` per node, with small constants such as `L <= 9` and `K <= 100`.

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
