---
type: source
title: "Evaluating the Impact of Jitter on Collaborative High-Speed Aerial and Railway Networks"
authors: ["Ziyue Liu", "Yue Xiao", "Enzhi Zhou", "Shuting Chen", "Xianfu Lei", "Xingwang Li", "Sotiris A. Tegos", "Panagiotis D. Diamantoulakis", "George K. Karagiannidis"]
year: 2026
url: "https://doi.org/10.1109/TITS.2026.3677161"
venue: "IEEE Transactions on Intelligent Transportation Systems (IEEE T-ITS)"
tags: [source, uav-hsr, uav-jitter, mmwave, adaptive-beamwidth, outage-probability, ergodic-rate]
related:
  - "[[jitter-aware-uav-beamwidth-control]]"
  - "[[directional-fanet-link-maintenance]]"
  - "[[control-assisted-uav-beam-tracking]]"
  - "[[air-to-ground-channel-model]]"
  - "[[uav-mobile-relaying]]"
  - "[[xingwang-li]]"
  - "[[george-k-karagiannidis]]"
created: 2026-07-13
updated: 2026-07-16
modeling_card: not_applicable
---

# Evaluating the Impact of Jitter on Collaborative High-Speed Aerial and Railway Networks

## Citation

Liu, Z., Xiao, Y., Zhou, E., Chen, S., Lei, X., Li, X., Tegos, S. A., Diamantoulakis, P. D., & Karagiannidis, G. K. (2026). *Evaluating the Impact of Jitter on Collaborative High-Speed Aerial and Railway Networks*. **IEEE Transactions on Intelligent Transportation Systems**, 27(7), 8057-8069. DOI: 10.1109/TITS.2026.3677161.

## TL;DR

Models UAV orientation jitter as a Gaussian random walk in a UAV-assisted high-speed-rail mmWave link. Closed-form and quadrature-based outage/rate analysis compares co-located and distributed train antennas, then a codebook-aware beamwidth rule balances directional gain, accumulated misalignment, and beam-training time.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Liu et al. [x] analyzed the effect of UAV orientation jitter on collaborative high-speed-rail mmWave communications. They modeled angular jitter as a Gaussian random walk and derived outage probability and ergodic-rate expressions for co-located and distributed train antenna layouts. They then mapped a continuous beamwidth choice to a discrete antenna codebook and evaluated candidate beamwidths under the accumulated misalignment and beam-training period. Numerical and Monte Carlo results compare the two layouts and report adaptive-beamwidth behavior across jitter intensity, update time, and signal-to-noise ratio. The work is a performance analysis and codebook design study rather than a central application-level resource-allocation model.

## Problem framing

UAVs can restore railway coverage when remote terrain or disasters disrupt trackside infrastructure, but turbulence, vibration, and speed changes disturb narrow mmWave beams. Existing UAV-HSR work rarely quantifies the resulting outage/rate loss or turns that analysis into a beamwidth decision robust to severe motion.

## System model

- A UAV aerial access point serves a multi-antenna mobile gateway on a high-speed train and is assumed to fly at the train's speed.
- The roof array uses either a co-located (CA) or uniformly distributed (DA) layout; the UAV-MG downlink is a `1 x M` SIMO link with maximum-ratio combining.
- Rural LoS propagation is approximated by free-space path loss; shadowing is ignored and small-scale fading is set to one.
- Angular jitter follows `Delta theta(t) ~ N(0, t sigma_u^2)` between beam realignments.
- A fixed 180-degree scan gives update period `T = tau / beta`, so narrower beams combine higher directivity with longer scans and greater accumulated jitter.

## Method

The paper inserts the random angular offset into the directional gain and derives CA outage using an upper incomplete gamma function. Period averages use 16-point Legendre-Gauss quadrature. High-SNR ergodic-rate expressions are exact only under the stated approximations; the DA rate also uses Jensen and path-loss bounds.

For [[jitter-aware-uav-beamwidth-control]], a continuous stationary beamwidth is mapped to the two nearest ULA-codebook choices. Evaluating both yields the CA optimum over the discrete beamset and a suboptimal DA setting. Monte Carlo tests use `10^5` jitter samples.

## Key findings

- CA rate decreases with elapsed time and jitter intensity under the high-SNR expression; DA geometry can provide spatial-diversity robustness for narrow beams or late in an update period.
- The CA/DA ordering can reverse for narrow beams: CA begins better after alignment but may fall below DA as jitter accumulates.
- The calculated codebook beamwidth is reported to match the simulated CA optimum and closely track the DA optimum.
- Adaptive beamwidth gives higher average ergodic rate than fixed `pi/2` and `pi/3` baselines, but the parse states no numerical gain.
- The parse conflicts on whether average outage increases or decreases with jitter intensity and alternates between concave and convex curvature language; those claims are not normalized here.

## Limitations / future work

Evidence is numerical and Monte Carlo only. The Gaussian jitter process is not validated against flight traces; multipath, shadowing, blockage, and imperfect speed synchronization are outside the model. DA outage suppresses layout geometry through CA-like approximations, and DA rate/beamwidth are bounded or suboptimal. Baselines exclude the compressed-sensing and learning methods discussed in related work.

## Relation to the corpus

This source adds a platform-motion counterpart to [[directional-fanet-link-maintenance]] and [[control-assisted-uav-beam-tracking]]. Those pages predict link breaks or use controller state to track a BS-UAV beam; this paper analytically links accumulated jitter to CA/DA outage and selects beamwidth from a physical codebook for a UAV-train link.

## Raw artifacts

- Parse: `raw/sources/Evaluating_the_Impact_of_Jitter_on_Collaborative_High-Speed_Aerial_and_Railway_Networks/Evaluating_the_Impact_of_Jitter_on_Collaborative_High-Speed_Aerial_and_Railway_Networks.md`
- Origin PDF: `raw/sources/Evaluating_the_Impact_of_Jitter_on_Collaborative_High-Speed_Aerial_and_Railway_Networks/Evaluating_the_Impact_of_Jitter_on_Collaborative_High-Speed_Aerial_and_Railway_Networks.pdf`
- Figures: `raw/sources/Evaluating_the_Impact_of_Jitter_on_Collaborative_High-Speed_Aerial_and_Railway_Networks/images/`
