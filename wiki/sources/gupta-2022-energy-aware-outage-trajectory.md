---
type: source
title: "Energy-Aware Trajectory Design for Outage Minimization in UAV-Assisted Communication Systems"
authors: ["Nishant Gupta", "Deepak Mishra", "Satyam Agarwal"]
year: 2022
url: "https://doi.org/10.1109/TGCN.2022.3146627"
venue: "IEEE Transactions on Green Communications and Networking, 6(3)"
modeling_card: required
tags: [source, uav-trajectory, outage-probability, on-board-energy, probabilistic-los, greedy-algorithm]
related:
  - "[[uav-trajectory-control]]"
  - "[[3gpp-uav-los-probability-model]]"
  - "[[air-to-ground-channel-model]]"
  - "[[rotary-wing-propulsion-energy-model]]"
  - "[[gupta-not-in-parse-uav-replacement]]"
  - "[[nishant-gupta]]"
  - "[[deepak-mishra]]"
  - "[[satyam-agarwal]]"
created: 2026-11-02
updated: 2026-11-02
---

# Energy-Aware Trajectory Design for Outage Minimization in UAV-Assisted Communication Systems

## Citation

Gupta, N., Mishra, D., & Agarwal, S. (2022). *Energy-Aware Trajectory Design for Outage Minimization in UAV-Assisted Communication Systems*. **IEEE Transactions on Green Communications and Networking, 6**(3). DOI: 10.1109/TGCN.2022.3146627.

## TL;DR

A single UAV flies from a fixed start to a fixed end while providing 5G service to users in a circular field. The paper minimizes average outage probability over users and time by optimizing the 3-D trajectory under velocity and on-board energy limits, using a low-complexity vertex approach and a higher-performance sequential approach that improve on benchmarks by 31% and 52% on average.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: One UAV serves $N$ ground users over $M$ slots, launching from $(x_0,y_0,z_0)$ and ending at $(\mathrm x_F,\mathrm y_F,\mathrm z_F)$. Channels follow a probabilistic LoS model with separate LoS and NLoS probabilities, and propulsion energy $\mathcal E(v[m])$ depends on per-slot speed.

**Problem & objective**: (P1): $\min_{\{x[m],y[m],z[m]\}}\frac{1}{MN}\sum_{m=1}^M\sum_{i=1}^N P^i_{out}[m]$, the average outage probability.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV position | $(x[m],y[m],z[m])$ | continuous 3-D, $z[m]\ge H$ | Trajectory waypoint in slot $m$ |
| Slot speed | $v[m]$ | $\le V_{max}$, derived from consecutive positions | Flight speed between waypoints |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | On-board energy, $\sum_m\mathcal E(v[m])\le\mathcal E_{tot}$. |
| C2 | Final location reached, $(x[M],y[M],z[M])=(\mathrm x_F,\mathrm y_F,\mathrm z_F)$. |
| C3 | Minimum altitude for collision avoidance, $z[m]\ge H$. |
| C4 | Maximum speed, $v[m]\le V_{max}$. |

**Algorithm**: Replace $P^i_{out}$ with an equivalent approximation $\hat P^i_{out}$. The vertex approach finds the globally optimal single 3-D location without velocity and energy limits, then builds a feasible trajectory greedily. The sequential approach searches the best feasible location slot by slot from the start.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Gupta et al. [x] studied the flight trajectory of a UAV that provides fifth-generation cellular service in a given area while flying from a fixed initial location to a final location. Considering the UAV's limited on-board energy, they minimized the average outage probability of the system by optimizing the three-dimensional trajectory subject to velocity and on-board energy constraints under a probabilistic LoS channel model. They proposed a low-complexity vertex approach, which first obtains the optimal location with the velocity and energy constraints relaxed and then constructs a greedy solution, and a high-performance sequential approach that finds the optimal location in each time slot sequentially. Simulation results show that the proposed strategies provide on average 41% improvement in average outage probability over the benchmark schemes, with the sequential approach outperforming the vertex approach at higher computational complexity.

## Problem framing

Ground infrastructure cannot always be deployed quickly for emergency or search services. A UAV can fill the gap, but its energy budget limits how long it can loiter near users, which links trajectory to outage.

## System model

- Users are distributed in a circular field.
- The approximation uses $e^{-a}\approx1-a$ for small $a$, giving an outage expression that depends on 3-D distance and LoS probability.
- If the start altitude is below $H$, the UAV first climbs vertically.

## Method

The vertex optimal location also serves as a reference for the asymptotic outage when energy is ample.

## Key findings

- Vertex and sequential approaches improve average outage probability by about 31% and 52% over benchmarks.
- The sequential approach outperforms the vertex approach at higher computational cost.
- A tradeoff exists between UAV velocity and available energy.

## Limitations / future work

The analysis uses one UAV with a fixed endpoint.

## Relation to the corpus

The same authors study replacement of depleted UAVs in [[gupta-not-in-parse-uav-replacement]]. The outage objective under a probabilistic LoS model connects to [[3gpp-uav-los-probability-model]] and [[uav-trajectory-control]].

## Raw artifacts

- Parse: `raw/sources/Energy-Aware_Trajectory_Design_for_Outage_Minimization_in_UAV-Assisted_Communication_Systems/Energy-Aware_Trajectory_Design_for_Outage_Minimization_in_UAV-Assisted_Communication_Systems.md`
- Origin PDF and extracted figures are in the same folder.
