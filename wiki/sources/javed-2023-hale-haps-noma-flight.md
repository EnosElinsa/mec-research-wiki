---
type: source
title: "An Interdisciplinary Approach to Optimal Communication and Flight Operation of High-Altitude Long-Endurance Platforms"
authors: ["Sidrah Javed", "Mohamed-Slim Alouini", "Zhiguo Ding"]
year: 2023
url: "https://doi.org/10.1109/TAES.2023.3304615"
venue: "IEEE Transactions on Aerospace and Electronic Systems, 59(6)"
modeling_card: required
tags: [source, high-altitude-platform-station, solar-energy-harvesting, noma, station-keeping, power-allocation, propulsion-power]
related:
  - "[[high-altitude-platform-station]]"
  - "[[hap-solar-propulsion-energy-balance]]"
  - "[[noma]]"
  - "[[fixed-wing-propulsion-energy-model]]"
  - "[[mohamed-slim-alouini]]"
created: 2026-11-02
updated: 2026-11-02
---

# An Interdisciplinary Approach to Optimal Communication and Flight Operation of High-Altitude Long-Endurance Platforms

## Citation

Javed, S., Alouini, M.-S., & Ding, Z. (2023). *An Interdisciplinary Approach to Optimal Communication and Flight Operation of High-Altitude Long-Endurance Platforms*. **IEEE Transactions on Aerospace and Electronic Systems, 59**(6). DOI: 10.1109/TAES.2023.3304615.

## TL;DR

A solar-powered HAPS cruising in a station-keeping circle must cover propulsion and multicell communication from harvested and stored energy. The paper budgets solar, battery, propulsion, and transmission power, then jointly chooses downlink NOMA power coefficients, altitude, and airspeed: by day to maximize sum rate under QoS and power limits, by night to minimize propulsion power.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A fixed-wing HAPS flies a station-keeping circular flight in the stratosphere, harvesting solar power with photovoltaic cells and storing the surplus for night. Array panels under the aircraft form directional beams to $M$ cells, each with $K_m$ users served by downlink NOMA. Propagation includes small- and large-scale fading, and feed-line loss $\Upsilon$ reduces radiated power.

**Problem & objective**: P1 (daytime): $\max_{\alpha[n],H[n],V[n]}\sum_{m=1}^M\sum_{l=1}^{K_m}R^m_l(\alpha[n],H[n])$. P2 (nighttime): $\min_{H[n],V[n]}P_{\mathrm{pro}}(V[n],H[n])$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| NOMA power coefficients | $\alpha^m_k[n]$ | $0\le\alpha^m_k[n]\le1$ | Power share of user $k$ in cell $m$ during interval $n$ |
| Altitude | $H[n]$ | $[H_{\min},H_{\max}]$ | Flight altitude in interval $n$ |
| Airspeed | $V[n]$ | $[V_s,V_{\max}]$ | Cruise airspeed in interval $n$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| (32b) | QoS, $R^m_l\ge\Omega_m$ for every user. |
| (32c)-(32d) | Power coefficients per cell sum to one and lie in $[0,1]$, with NOMA ordering. |
| (32f) | Communication power budget after feed-line losses $\Upsilon$. |
| (32g) | Stored battery power $P_{\mathrm{st}}$ suffices for nighttime operation. |
| (32h)-(32i) | Altitude bounds and airspeed above the stall speed $V_s=\sqrt{2W/(\rho_h(H)SC_{L\min})}$. |

**Algorithm**: Decompose each problem into subproblems with closed-form solutions. Algorithm 1 alternates power allocation, altitude, and airspeed for P1; for P2, convexity in $H$ and $V$ separately gives P2(a) and P2(b), solved in Algorithm 2.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Javed et al. [x] studied self-sustaining high-altitude long-endurance platform stations whose photovoltaic cells harvest solar energy by day for communication and station keeping and store the excess in batteries for night operation. They carried out power budgeting to determine whether the available solar power can sustain both propulsion and communication, and proposed an energy-optimal trajectory for station-keeping flight together with nonorthogonal multiple access for multicell users served by directional beams. Optimization problems were formulated to maximize the sum rate by day and to minimize the power requirement at night, jointly over power allocation, altitude, and airspeed, and were solved by algorithms built on closed-form subproblem solutions. Numerical results show that the joint design reduces propulsion power by roughly 58% to 89% across aircraft models relative to unoptimized flight parameters. The optimized system also improves the average sum rate by about 70% to 119% for different QoS thresholds, and NOMA improves spectral efficiency over OMA.

## Problem framing

HAPS endurance depends on whether daytime harvesting can pay for propulsion, communication, and battery charging. Flight parameters change both propulsion power and link geometry, so they must be designed with the transmission strategy.

## System model

- Gallium arsenide multijunction solar cells with 39.1% efficiency.
- Several aircraft models are evaluated with their own aerodynamic parameters.
- Link budgets include beam gains, fading, and losses for multicell coverage.

## Method

Each subproblem yields a closed-form optimum, and the alternating procedure iterates among them. Night operation fixes the transmission budget and minimizes propulsion.

## Key findings

- Joint optimization cuts propulsion power by 88.68%, 84.84%, 84.82%, 79.88%, 81.61%, 57.78%, and 58.53% across seven aircraft models.
- Average sum rate rises by 69.83%, 84.38%, 99.04%, and 119.08% for QoS thresholds of 2, 2.5, 3, and 3.5 Mb/s.
- NOMA improves two spectral-efficiency measures by up to 50% and 26.7% over OMA.

## Limitations / future work

The model uses one HAPS with a fixed circular station-keeping pattern.

## Relation to the corpus

A detailed instance of [[hap-solar-propulsion-energy-balance]] for [[high-altitude-platform-station]] communication, combining [[noma]] with flight design.

## Raw artifacts

- Parse: `raw/sources/An_Interdisciplinary_Approach_to_Optimal_Communication_and_Flight_Operation_of_High-Altitude_Long-Endurance_Platforms/An_Interdisciplinary_Approach_to_Optimal_Communication_and_Flight_Operation_of_High-Altitude_Long-Endurance_Platforms.md`
- Origin PDF and extracted figures are in the same folder.
