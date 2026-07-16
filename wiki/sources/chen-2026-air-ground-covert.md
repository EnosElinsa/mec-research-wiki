---
type: source
title: "Air-to-Ground Covert Communication With Location and Interference Uncertainty"
authors: ["Hongchi Chen", "Junsheng Mu", "Na Deng", "Haichao Wei", "Nan Zhao"]
year: 2026
url: "https://doi.org/10.1109/TWC.2026.3687670"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
modeling_card: required
tags: [source, covert-communication, physical-layer-security, stochastic-geometry, ppp, air-to-ground-channel-model, interference-modeling, location-uncertainty]
related:
  - "[[ambient-interference-aided-covertness]]"
  - "[[covert-communication]]"
  - "[[stochastic-geometry-network-analysis]]"
  - "[[air-to-ground-channel-model]]"
  - "[[physical-layer-security]]"
  - "[[cooperative-jamming]]"
  - "[[hosseini-2026-aoi-covert-uav]]"
  - "[[ma-2024-covert-mmwave-finite-blocklength]]"
  - "[[al-hourani-2014-optimal-lap-altitude]]"
created: 2026-07-11
updated: 2026-07-16
---

# Air-to-Ground Covert Communication With Location and Interference Uncertainty

## Citation

Chen, H., Mu, J., Deng, N., Wei, H., & Zhao, N. (2026). *Air-to-Ground Covert Communication With Location and Interference Uncertainty*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2026.3687670.

## TL;DR

Analyzes a UAV Alice sending covertly to ground Bob while a location-uncertain ground Willie performs radiometer detection amid co-channel ground interferers modeled as a homogeneous PPP. The paper approximates aggregate interference with a gamma distribution, then derives covertness, connection probability, and covert throughput under two Willie-knowledge cases.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A single-antenna UAV transmitter Alice sends to ground receiver Bob while a location-uncertain ground warden Willie performs radiometer detection. Ground interferers follow a homogeneous Poisson point process, and Willie either knows Alice's instantaneous received power or only its distribution.

**Problem & objective**: Covert throughput is the maximum target rate over Alice's transmit power and rate, $\xi=\max R(P_a^*)$, subject to average covertness $\bar p_{cv}\ge\beta$ and connection reliability $p_{cn}\ge\gamma$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Alice transmit power | $P_a$ | continuous, nonnegative | Power chosen to maximize feasible covert rate |
| Target transmission rate | $R$ | continuous, nonnegative | Alice-to-Bob rate and covert-throughput objective |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Average covert probability meets its target: $\bar p_{cv}(P_a,\epsilon^*)\ge\beta$. |
| C2 | Alice-to-Bob connection probability meets its target: $p_{cn}(P_a,R)\ge\gamma$. |
| C3 | Covertness and reliability targets satisfy $\beta,\gamma\in(0,1)$. |
| C4 | Willie uses the detection-error-minimizing threshold $\epsilon^*$ for the applicable knowledge case. |

**Algorithm**: Derive aggregate-interference moments with Campbell's theorem and PPP second-order product density, fit the interference by a gamma distribution with parameters $\rho$ and $\theta$, and derive Willie's optimal threshold and average covert probability for the instantaneous-power and distribution-knowledge cases. Evaluate Bob's connection probability with the fitted distribution, use the monotonic decrease of covertness in $P_a$ to find the largest $P_a^*$ satisfying $\bar p_{cv}(P_a^*,\epsilon^*)=\beta$, and then search for the largest $R^*$ satisfying $p_{cn}(P_a^*,R^*)=\gamma$.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Chen et al. [x] analyzed air-to-ground covert communication from a UAV transmitter to a ground receiver under a location-uncertain warden and Poisson-field environmental interference. They approximated aggregate interference with a gamma distribution, derived average covert probabilities for two warden-knowledge cases, and obtained connection-probability and covert-throughput expressions under covertness and reliability constraints. Their reusable decision model chooses Alice's transmit power and target rate by first saturating the covertness constraint and then searching for the largest rate that meets connection reliability. Results reported higher covert probability and covert throughput for the distribution-knowledge case, especially with sparse interferers.

## Problem framing

UAV line-of-sight propagation makes transmission behavior easier to detect. Existing UAV covert-communication studies often use finite deterministic node layouts and omit both large-scale environmental interference and warden-location uncertainty. This paper asks how ambient interference can both shield Alice from Willie and degrade Bob's reliability.

## System model

- Single-antenna UAV Alice transmits to ground Bob.
- Ground Willie is uniformly distributed inside a known uncertainty disk.
- Single-antenna ground interferers follow a homogeneous two-dimensional PPP and remain static within a slot.
- Air-to-ground links use probabilistic LoS/NLoS propagation with Nakagami/Rayleigh fading; ground links use NLoS bounded path loss.
- Thermal noise is neglected relative to aggregate interference, and Willie is modeled with asymptotically many radiometer samples.
- Case 1 assumes Willie knows Alice's instantaneous received power; case 2 assumes Willie knows only its probability distribution.

## Method

The paper derives aggregate-interference moments using Campbell's theorem and PPP second-order product density, then compares two-moment matched gamma, inverse-gamma, inverse-Gaussian, and lognormal approximations. It adopts the gamma approximation, derives Willie's optimal threshold and average covert probability for both knowledge cases, derives Bob's connection probability, and defines covert throughput as the maximum rate satisfying covertness and reliability constraints.

## Key findings

- For the tested ground path-loss exponent `alpha_N = 4`, the gamma distribution fits aggregate interference best among the four candidates; inverse gamma performs worst.
- Increasing interferer power or density improves covertness but harms Bob's connection reliability.
- Case 2 generally yields higher average covert probability and covert throughput than case 1, especially when interferers are sparse.
- Covertness first decreases and then increases with UAV altitude, while connection probability first increases and then decreases.
- Connection probability is maximized when Alice hovers directly above Bob.
- Scaling Alice's power and interferer power by the same factor leaves the derived covert throughput unchanged.
- The prose does not give exact improvement percentages or optimum coordinates.

## Limitations / future work

The conclusion names multi-UAV interferers with power control as future work. Model-scope caveats include homogeneous PPP interferers, static positions per slot, single antennas, neglected thermal noise, asymptotically many radiometer samples, gamma-approximated interference, and numerical rather than field validation. One numerical-results sentence appears to invert the case-1/case-2 comparison; the abstract, contributions, conclusion, and plotted curves support case 2 as the higher-covertness case, so the page follows the consistent interpretation and flags the inconsistency here.

## Relation to the corpus

This is the corpus's [[ambient-interference-aided-covertness]] anchor: unlike [[zhang-2026-air-ground-covert-jamming]], which introduces deliberate RIS-directed jamming, this source relies on uncontrolled environmental interferers as stochastic cover. It also complements [[ma-2024-covert-mmwave-finite-blocklength]] by moving covert-communication randomness from spatially random wardens to PPP environmental interferers plus a location-uncertain Willie.

## Raw artifacts

- `raw/sources/Air-to-Ground_Covert_Communication_With_Location_and_Interference_Uncertainty/Air-to-Ground_Covert_Communication_With_Location_and_Interference_Uncertainty.md`
- Original PDF and extracted figures (`images/`) in the same folder.

## Metadata notes

The parsed Markdown is silent on final DOI/year/venue metadata. DOI, venue, and year were verified through the local PDF and exact-title DOI lookup; all technical claims above are grounded in the local parse.
