---
type: source
title: "Optimization of Total Power Consumed by Flying Base Station Serving Mobile Users"
authors: ["Mohammadsaleh Nikooroo", "Zdenek Becvar"]
year: 2022
url: "https://doi.org/10.1109/TNSE.2022.3169846"
venue: "IEEE Transactions on Network Science and Engineering, 9(4)"
modeling_card: required
tags: [source, flying-base-station, propulsion-power, transmission-power, mobile-users, positioning, closed-form-solution]
related:
  - "[[drone-cell-3d-placement]]"
  - "[[rotary-wing-propulsion-energy-model]]"
  - "[[becvar-2022-airship-flybs-energy]]"
  - "[[zdenek-becvar]]"
  - "[[mohammadsaleh-nikooroo]]"
created: 2026-11-02
updated: 2026-11-02
---

# Optimization of Total Power Consumed by Flying Base Station Serving Mobile Users

## Citation

Nikooroo, M., & Becvar, Z. (2022). *Optimization of Total Power Consumed by Flying Base Station Serving Mobile Users*. **IEEE Transactions on Network Science and Engineering, 9**(4). DOI: 10.1109/TNSE.2022.3169846.

## TL;DR

A UAV flying base station (FlyBS) must keep guaranteeing each moving user's capacity while its limited power supply covers both propulsion and transmission. The paper derives a closed-form position and transmission power that minimize total power at a single time step and a numerical solution over a long movement period, reducing total power by up to 91% compared with existing solutions.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: One FlyBS at position $\mathbf r(t_k)=(X,Y,H)$ serves $n$ moving users over $T$ time steps. Each user receives bandwidth $B_i$ and capacity $C_i(t_k)$. Total power combines a realistic non-linear propulsion model and transmission power.

**Problem & objective**: Problem (11): $\min_{\mathbf r(t_k),\mathbf B(t_k)}P^{avg}_{tot}$, the average total power over $1\le k\le T$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| FlyBS position | $\mathbf r(t_k)$ | continuous 3-D | Position at each time step |
| Bandwidth allocation | $\mathbf B(t_k)$ | $\sum_iB_i\le B_{tot}$ | Bandwidth assigned to each user |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| (a) | Capacity guarantee, $C_i(t_k)\ge C^{min}_i$ for all users and steps. |
| (b) | Location-dependent altitude range, $H_{min}(X,Y)\le H(t_k)\le H_{max}(X,Y)$. |
| (c) | Speed limit, $\lVert\mathbf r(t_{k+1})-\mathbf r(t_k)\rVert\le V_{max}(t_{k+1}-t_k)$. |
| (d) | Bandwidth budget, $\sum_iB_i\le B_{tot}$. |

**Algorithm**: For single-point optimization, derive the closed-form FlyBS position and transmission power. For multi-point optimization over a period, solve numerically, with schemes EMPS, MPS, and SPS, for both unconstrained and constrained transmission power.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Nikooroo and Becvar [x] studied unmanned aerial vehicles acting as flying base stations that are dynamically positioned according to users' communication demands while their power supply is limited. They reduced the total power consumption of the flying base station while guaranteeing the required communication capacity to mobile users at every time instant of their movement. A closed-form solution was derived for optimizing total power in a single time step under a realistic non-linear power consumption model, and a numerical solution was provided for the total power optimization over a long period of user movement. Simulations show that the proposed scheme reduces the overall power consumed by the flying base station by up to 91% compared with existing solutions.

## Problem framing

Prior work optimized either transmission power or propulsion power. Joint optimization accounts for the fact that moving closer to users lowers transmit power but can raise propulsion power.

## System model

- Altitude bounds vary with position to reflect obstacles and regulation.
- Users move continuously, so capacity must hold at every step.

## Method

The single-point closed form is applied within the multi-point numerical procedure; EMPS, MPS, and SPS are variants compared with a baseline MTX.

## Key findings

- At 25 m/s, EMPS, MPS, and SPS reduce propulsion power by about 91%, 90%, and 90% relative to MTX.
- With unconstrained transmission power and $C^{min}=5$ Mbps, total power drops by 91%, 90%, and 89%; at $C^{min}=10$ Mbps, propulsion gains fall to about 36%, 34%, and 33%.
- With constrained transmission power, total power drops by about 90%, 89%, and 88% at 5 Mbps.

## Limitations / future work

The study considers one FlyBS.

## Relation to the corpus

Joins transmission and [[rotary-wing-propulsion-energy-model]] terms in [[drone-cell-3d-placement]] for mobile users; the airship multi-FlyBS case is [[becvar-2022-airship-flybs-energy]].

## Raw artifacts

- Parse: `raw/sources/Optimization_of_Total_Power_Consumed_by_Flying_Base_Station_Serving_Mobile_Users/Optimization_of_Total_Power_Consumed_by_Flying_Base_Station_Serving_Mobile_Users.md`
- Origin PDF and extracted figures are in the same folder.
