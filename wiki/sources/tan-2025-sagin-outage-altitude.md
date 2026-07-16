---
type: source
title: "Outage Probability, Performance, and Fairness Analysis of Space-Air-Ground Integrated Network (SAGIN): UAV Altitude and Position Angle"
authors: ["Jingjing Tan", "Fengxiao Tang", "Ming Zhao", "Nei Kato"]
year: 2025
url: "https://doi.org/10.1109/TWC.2024.3503060"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), vol. 24, no. 2, pp. 940-954"
modeling_card: required
tags: [source, sagin, uav-relay, outage-probability, solar-energy, altitude-optimization]
related:
  - "[[outage-aware-sagin-uav-altitude]]"
  - "[[space-air-ground-integrated-network]]"
  - "[[uav-mobile-relaying]]"
  - "[[air-to-ground-channel-model]]"
  - "[[nei-kato]]"
created: 2026-07-14
updated: 2026-07-16
---

# Outage Probability, Performance, and Fairness Analysis of Space-Air-Ground Integrated Network (SAGIN): UAV Altitude and Position Angle

## Citation

Tan, J., Tang, F., Zhao, M., & Kato, N. (2025). *Outage Probability, Performance, and Fairness Analysis of Space-Air-Ground Integrated Network (SAGIN): UAV Altitude and Position Angle*. **IEEE Transactions on Wireless Communications, 24**(2), 940-954. DOI: 10.1109/TWC.2024.3503060.

## TL;DR

Derives energy- and SNR-outage expressions plus a feasible UAV altitude for a solar-powered ground-UAV-satellite uplink, then compares the transmission capacities of relayed GAS and direct ground-to-satellite links as a paper-specific notion of fairness.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Ground traffic reaches a satellite through a solar-powered hybrid fixed/rotary-wing UAV relay. The end-to-end ground-air-space rate is the bottleneck of a ground-to-air hop with path, misalignment, and multipath fading and an air-to-space hop with propagation, atmospheric, and rain attenuation.

**Problem & objective**: Problem (29) maximizes the bottleneck rate $\min\{R_{GA},R_{AS}\}$ over UAV altitude and the ground-air and air-space position angles while excluding energy and SNR outages.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV altitude | $h_U$ | continuous, positive | Relay altitude that changes both hop rates and return-flight energy |
| Ground-air position angle | $\theta_{GA}$ | continuous angle | Geometry between the base station and UAV |
| Air-space position angle | $\theta_{AS}$ | continuous angle | Geometry between the UAV and satellite |
| Transmission duration | $T_t$ | continuous, $0<T_t\leq T_t^*$ | Service time adjusted to preserve energy feasibility |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 / 29b | Harvested energy plus backup energy must cover transmission, hovering, activation, and return flight |
| C2 / 29c | Ground-to-air SNR meets its threshold, $\mathrm{SNR}_{GA}\geq\mathrm{SNR}_{GA}^{th}$ |
| C3 / 29d | Air-to-space SNR meets its threshold, $\mathrm{SNR}_{AS}\geq\mathrm{SNR}_{AS}^{th}$ |
| 30 | The maximum feasible service duration $T_t^*$ couples altitude, return distance, battery energy, and harvested power |

**Algorithm**: The paper derives outage distributions, splits the bottleneck analysis into $R_{GA}\leq R_{AS}$ and $R_{GA}\geq R_{AS}$ cases, and obtains closed-form altitude and angle expressions. If the energy-limited altitude condition is active, it uses the boundary altitude and shortens $T_t$ or replaces the relay UAV.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Tan et al. [x] studied a solar-powered ground-air-space uplink in which a hybrid fixed/rotary-wing UAV relays traffic from ground users to a satellite. They derived energy-outage and SNR-outage probabilities under stochastic solar harvesting, backup-battery energy, ground-to-air fading, and air-to-space attenuation. The placement problem maximizes the minimum rate of the two hops over UAV altitude and position angles subject to energy and link-SNR requirements. Their case analysis yields altitude and angle expressions for both possible bottleneck hops and a service-time bound that can trigger UAV replacement. Simulations validate the altitude expressions and show that bandwidth, carrier frequency, unfaded SNR, and satellite-relative angle materially change the selected altitude.

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
