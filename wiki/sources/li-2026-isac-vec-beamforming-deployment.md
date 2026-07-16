---
type: source
title: "Joint Beamforming and UAV Deployment Optimization for ISAC-Enhanced UAV-Assisted VEC"
authors: ["Chunlin Li", "Wenhao Wu", "Zhihao Zhang", "Tianbing Ma", "Shaohua Wan"]
year: 2026
url: "https://doi.org/10.1109/TWC.2026.3694912"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
modeling_card: required
tags: [source, vehicular-mec, isac, uav-assisted-vec, beamforming, uav-deployment, sparrow-search-algorithm]
related:
  - "[[vehicular-mec]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[sparrow-search-algorithm]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[cramer-rao-bound]]"
  - "[[weighted-kmeans-uav-deployment]]"
  - "[[li-2025-energy-latency-uav-vec]]"
created: 2026-07-07
updated: 2026-07-16
---

# Joint Beamforming and UAV Deployment Optimization for ISAC-Enhanced UAV-Assisted VEC

## Citation

Li, C., Wu, W., Zhang, Z., Ma, T., & Wan, S. (2026). *Joint Beamforming and UAV Deployment Optimization for ISAC-Enhanced UAV-Assisted VEC*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2026.3694912.

## TL;DR

Uses UAVs as flexible ISAC support for urban vehicular edge computing when fixed RSUs cannot cover temporary congestion or hot spots. The paper jointly optimizes UAV deployment positions and beamforming to maximize communication capacity under energy and sensing constraints. It decomposes the problem into UAV deployment and beamforming blocks, using a refraction-based-learning sparrow search algorithm for deployment and an SCA / first-order-Taylor convexification loop for beamforming.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Multiple UAVs augment an urban vehicular edge-computing network with joint communication and sensing service for moving vehicles. Each UAV selects a 3-D deployment and ISAC beamforming over slotted TDD operation, while communication capacity, sensing accuracy, flight energy, coverage, and mobility are modeled jointly.

**Problem & objective**: Problem $P_1$ maximizes aggregate communication capacity through $\max_{x,y,h,G_{\mathrm{ISAC}}}C_{\mathrm{sum}}$ by jointly optimizing UAV deployment coordinates and the ISAC beamforming design.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Horizontal deployment | $(x_u(t),y_u(t))$ | continuous coordinates | Horizontal location of UAV $u$ in slot $t$ |
| Flight altitude | $h_u(t)$ | continuous, $H_{\min}\leq h_u(t)\leq H_{\max}$ | Altitude of UAV $u$ |
| ISAC beamformer | $G_{\mathrm{ISAC}}$ or $\boldsymbol w$ | complex continuous design | Joint communication and sensing beamforming variables |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| 26b-26e | Downlink, flexible, and uplink time, rate, spectrum, and one-UAV association limits are satisfied |
| 26f-26g | Communication capacity is at least $C_{\min}$ and distance and angle CRBs meet their sensing thresholds |
| 26h | Total ISAC and flight energy obeys $\sum_t(E_{\mathrm{ISAC}}^u(t)+E_{\mathrm{Fly}}^u(t))\leq E_{\max}$ |
| 26i | A served vehicle remains in coverage: $d_{u,n}(t)\leq R_{\mathrm{cov}}$ |
| 26j-26m | Horizontal and vertical motion, altitude, and vehicle-speed bounds hold in every slot |

**Algorithm**: Use block coordinate descent between deployment and beamforming. For fixed beamforming, solve the NP-hard 3-D deployment block with a sparrow search enhanced by refracted opposition-based initialization and SCA local search; for fixed deployment, linearize the non-convex beamforming expressions by first-order Taylor expansion, solve the convex surrogate, and alternate the two blocks.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Li et al. [x] studied joint UAV deployment and beamforming for ISAC-enhanced UAV-assisted vehicular edge computing in spatially uneven urban traffic. They formulated communication-capacity maximization over 3-D UAV positions and ISAC beamforming subject to time, rate, spectrum, association, sensing-accuracy, energy, coverage, and mobility constraints. Their block-coordinate method combines a refracted opposition-based sparrow search and SCA for deployment with first-order convexification for beamforming. Simulations reported an average coverage-rate gain of 10.51% and an average UAV-energy reduction of 19.83% relative to the evaluated baselines, with the joint solver converging within 300 to 400 iterations.

## Problem framing

Urban VEC hotspots are spatially uneven and time-varying. Fixed RSUs can be overloaded or poorly placed, while UAVs can reposition to improve coverage and sensing. The difficulty is the communication-sensing-energy tradeoff: stronger coverage and radar information may require unfavorable UAV locations, beam powers, or flight energy.

## System model

- A two-layer in-vehicle terminal / edge architecture lets vehicles upload complex tasks to edge computing stations, with UAVs supporting coverage and sensing.
- The TDD frame separates downlink, flexible, and uplink parts; sensing and communication are both active in downlink, while uplink carries communication.
- Communication capacity and Cramer-Rao-bound-style sensing metrics enter an ISAC sensing-communication effectiveness function.
- The main case considers spatially separated crossing roads and neglects inter-UAV co-channel interference; the parse also reports a denser multi-UAV interference scenario.

## Method

- Formulate a joint optimization problem over UAV deployment and beamforming with communication capacity, sensing performance, and UAV energy constraints.
- Apply block-coordinate decomposition: optimize deployment and beamforming as separate subproblems.
- Use an improved [[sparrow-search-algorithm]] with refraction-based learning for UAV deployment.
- Use SCA and first-order Taylor expansion to convexify the beamforming subproblem, aligning it with the broader [[alternating-optimization-sdr-sca]] family.

## Key findings

- The proposed algorithm converges faster and more smoothly than the tested benchmark functions in the parse.
- In the 30-vehicle case, reported coverage is 9.6%, 20.1%, and 4.4% higher than DDPG, PSO, and TPaPBA baselines, respectively.
- Across UAV-scale settings from 3 to 5 UAVs, the paper reports an average 10.51% coverage improvement over baselines and a 19.83% reduction in UAV energy consumption.
- Ablations show that fixed-sequence optimization reduces communication capability and radar mutual information; omitting sensing can slightly improve communication but loses the ISAC balance; fixing the sensing/communication split degrades communication and cost.

## Limitations / future work

The evaluation is simulation-based, including Veins-style traffic modeling. The main scenario simplifies interference by placing UAVs over spatially separated roads; the denser interference case is reported separately. Future work named in the parse is collaborative optimization among UAVs and vehicles.

## Relation to the corpus

This VEC entry makes [[integrated-sensing-and-communication]] central to UAV-assisted vehicular edge deployment. It complements [[li-2025-energy-latency-uav-vec]], which used UAV-assisted VEC for FL participant selection and resource allocation, by focusing instead on deployment plus beamforming for coverage/sensing. Methodologically it adds [[sparrow-search-algorithm]] to the swarm-metaheuristic family and pairs it with classical SCA beamforming.

## Raw artifacts

- `raw/sources/Joint Beamforming and UAV Deployment Optimization for ISAC-Enhanced UAV-Assisted VEC/Joint Beamforming and UAV Deployment Optimization for ISAC-Enhanced UAV-Assisted VEC.md`
- Original PDF and extracted figures (`images/`) in the same folder.
