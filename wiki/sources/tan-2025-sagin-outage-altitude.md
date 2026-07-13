---
type: source
title: "Outage Probability, Performance, and Fairness Analysis of Space-Air-Ground Integrated Network (SAGIN): UAV Altitude and Position Angle"
authors: ["Jingjing Tan", "Fengxiao Tang", "Ming Zhao", "Nei Kato"]
year: 2025
url: "https://doi.org/10.1109/TWC.2024.3503060"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), vol. 24, no. 2, pp. 940-954"
tags: [source, sagin, uav-relay, outage-probability, solar-energy, altitude-optimization]
related:
  - "[[outage-aware-sagin-uav-altitude]]"
  - "[[space-air-ground-integrated-network]]"
  - "[[uav-mobile-relaying]]"
  - "[[air-to-ground-channel-model]]"
  - "[[nei-kato]]"
created: 2026-07-14
updated: 2026-07-14
---

# Outage Probability, Performance, and Fairness Analysis of Space-Air-Ground Integrated Network (SAGIN): UAV Altitude and Position Angle

## Citation

Tan, J., Tang, F., Zhao, M., & Kato, N. (2025). *Outage Probability, Performance, and Fairness Analysis of Space-Air-Ground Integrated Network (SAGIN): UAV Altitude and Position Angle*. **IEEE Transactions on Wireless Communications, 24**(2), 940-954. DOI: 10.1109/TWC.2024.3503060.

## TL;DR

Derives energy- and SNR-outage expressions plus a feasible UAV altitude for a solar-powered ground-UAV-satellite uplink, then compares the transmission capacities of relayed GAS and direct ground-to-satellite links as a paper-specific notion of fairness.

## Problem and system model

Ground nodes send data through UAV relays to a satellite. The model combines ground-to-air and air-to-satellite fading, UAV altitude and satellite-relative position angle, fixed- and rotary-wing energy consumption, solar harvesting, and a backup battery. A replacement UAV can take over when an active relay cannot sustain service.

The analysis asks when harvested-plus-battery energy can cover propulsion and communication, when received SNR meets a threshold, and which altitude balances the two-hop transmission rates without violating either outage condition.

## Method

The [[outage-aware-sagin-uav-altitude]] analysis derives closed-form or integral expressions for UAV energy-outage and link SNR-outage probabilities, then constructs altitude conditions for the bottleneck rate of the ground-air-satellite path. It also derives transmission-time thresholds under which relayed GAS transmission capacity exceeds direct ground-to-satellite capacity.

## Key findings

- Monte Carlo experiments validate the theoretical altitude expressions under the paper's channel and energy assumptions.
- Increasing A2S bandwidth lowers the selected altitude while increasing GAS rate; increasing G2A bandwidth raises altitude until both altitude and rate saturate.
- Channel frequency, unfaded SNR, and the UAV-satellite position angle materially shift the optimal altitude through their effects on the two hops.
- The GAS/direct comparison yields different time thresholds depending on geometry. This is a two-mode capacity-gap analysis, not Jain-style fairness among users.

## Limitations

The evidence is analytical and simulation-based. Solar supply, fading distributions, geometry, and propulsion models are idealized; attitude and altitude-control error is omitted and named as future work. The derived altitude is tied to the modeled uplink and does not establish end-to-end network fairness or deployment robustness.

## Relation to the corpus

This source adds outage-aware relay placement to [[space-air-ground-integrated-network|SAGIN]]. Unlike MEC sources that select a satellite or UAV compute tier, it studies the physical viability of [[uav-mobile-relaying]] under solar-energy interruption, two-hop fading, and direct-link competition.

## Raw artifacts

- Parse: `raw/sources/Outage_Probability_Performance_and_Fairness_Analysis_of_Space-Air-Ground_Integrated_Network_SAGIN_UAV_Altitude_and_Position_Angle/Outage_Probability_Performance_and_Fairness_Analysis_of_Space-Air-Ground_Integrated_Network_SAGIN_UAV_Altitude_and_Position_Angle.md`
- Origin PDF and extracted figures (`images/`) are in the same folder.
