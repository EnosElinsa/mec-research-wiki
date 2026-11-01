---
type: source
title: "On Energy Consumption of Airship-Based Flying Base Stations Serving Mobile Users"
authors: ["Zdenek Becvar", "Mohammadsaleh Nikooroo", "Pavel Mach"]
year: 2022
url: "https://doi.org/10.1109/TCOMM.2022.3196654"
venue: "IEEE Transactions on Communications, 70(10)"
modeling_card: required
tags: [source, flying-base-station, airship, energy-consumption, mobile-users, sum-capacity, positioning]
related:
  - "[[drone-cell-3d-placement]]"
  - "[[high-altitude-platform-station]]"
  - "[[nikooroo-2022-flybs-total-power]]"
  - "[[zdenek-becvar]]"
  - "[[mohammadsaleh-nikooroo]]"
created: 2026-11-02
updated: 2026-11-02
---

# On Energy Consumption of Airship-Based Flying Base Stations Serving Mobile Users

## Citation

Becvar, Z., Nikooroo, M., & Mach, P. (2022). *On Energy Consumption of Airship-Based Flying Base Stations Serving Mobile Users*. **IEEE Transactions on Communications, 70**(10). DOI: 10.1109/TCOMM.2022.3196654.

## TL;DR

Rotary-wing flying base stations (FlyBSs) waste energy hovering, so the paper studies airship-based FlyBSs serving moving users. It derives how sum capacity relates to flying energy, bounds the energy saving for a single FlyBS, and gives a multi-FlyBS repositioning algorithm that minimizes flying energy while keeping sum capacity within a factor $1-\epsilon$ of the capacity-maximizing positions.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: $M$ airship FlyBSs serve $N$ moving users over time steps. User $n$ associates with FlyBS $m$ through $a_{n,m}$ and obtains capacity $C_{n,m}$ over a mixed LoS/NLoS channel. Flying energy $E_{F,m}$ depends on how far each airship moves per step.

**Problem & objective**: Problem (4): $\hat{\mathbf V}(t)=\arg\min_{\mathbf V\in\mathbb R^{3M}}\sum_{m=1}^M E_{F,m}$, the total flying energy of all FlyBSs.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| FlyBS positions | $\mathbf V$ | $\mathbb R^{3M}$ | 3-D positions of all FlyBSs at the next step |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| (a) | Sum capacity guarantee, $\sum_n\sum_m a_{n,m}C_{n,m}\ge C_{opt}(1-\epsilon)$. |
| (b) | Movement per step, $d_m\le d_{max}$. |
| (c) | Altitude range, $h_{min}\le z_{f,m}\le h_{max}$. |

**Algorithm**: Derive the analytical relation between sum capacity and flying energy for one FlyBS, giving energy-saving bounds versus capacity degradation. Generalize to multiple FlyBSs with an algorithm that moves each airship only as far as needed to keep sum capacity above $(1-\epsilon)C_{opt}$.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Becvar et al. [x] studied the energy consumption of flying base stations that serve space-time varying traffic of moving users. Because rotary-wing flying base stations consume much energy while hovering, they considered airship-based flying base stations and derived an analytical relation between the users' sum capacity and the energy spent for flying. They showed theoretical bounds on energy saving relative to a guaranteed fraction of the maximum sum capacity for a single flying base station, and then proposed an algorithm that minimizes the flying energy of multiple flying base stations under a constraint on the minimum relative sum capacity. The algorithm reduces flying energy by dozens of percent at the cost of a marginal and controlled degradation in sum capacity. For example, with up to 1% sum-capacity degradation, it saves 55.4%, 67.5%, and 90.7% of the energy when five, three, and one flying base stations are deployed, respectively.

## Problem framing

Capacity-maximizing positions move with the users, and chasing them exactly costs flying energy. Allowing a small capacity loss lets the airships move much less.

## System model

- Mixed LoS/NLoS path loss with 10% NLoS probability in an open outdoor area.
- Airship propulsion energy grows with the distance moved per step.

## Method

The energy-capacity relation gives closed-form bounds for one FlyBS; the multi-FlyBS algorithm applies the same principle per airship.

## Key findings

- With 1% capacity degradation allowed, energy savings are 55.4%, 67.5%, and 90.7% for five, three, and one FlyBSs.
- Positioning errors of a few meters have only a marginal effect on sum capacity.

## Limitations / future work

The authors note that "perfect positioning" is unnecessary, opening a degree of freedom for future algorithm design.

## Relation to the corpus

An airship counterpart to rotary-wing [[drone-cell-3d-placement]]; total transmit-plus-propulsion power for a single FlyBS is treated in [[nikooroo-2022-flybs-total-power]].

## Raw artifacts

- Parse: `raw/sources/On_Energy_Consumption_of_Airship-Based_Flying_Base_Stations_Serving_Mobile_Users/On_Energy_Consumption_of_Airship-Based_Flying_Base_Stations_Serving_Mobile_Users.md`
- Origin PDF and extracted figures are in the same folder.
