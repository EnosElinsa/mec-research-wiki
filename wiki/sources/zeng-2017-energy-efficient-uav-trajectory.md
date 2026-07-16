---
type: source
modeling_card: required
title: "Energy-Efficient UAV Communication With Trajectory Optimization"
authors: ["Yong Zeng", "Rui Zhang"]
year: 2017
url: "https://doi.org/10.1109/TWC.2017.2688328"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, uav-communications, energy-efficiency, trajectory-optimization, fixed-wing-uav, energy-model, alternating-optimization-sdr-sca]
related:
  - "[[uav-trajectory-control]]"
  - "[[fixed-wing-propulsion-energy-model]]"
  - "[[rotary-wing-propulsion-energy-model]]"
  - "[[energy-latency-tradeoff]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[zeng-2019-rotary-wing-energy-min]]"
  - "[[wu-2018-multiuav-minrate-trajectory]]"
  - "[[zeng-2019-uav-comm-tutorial-5g]]"
  - "[[yong-zeng]]"
created: 2026-06-01
updated: 2026-07-16
---

# Energy-Efficient UAV Communication With Trajectory Optimization

## Citation

Zeng, Y., & Zhang, R. (2017). *Energy-Efficient UAV Communication With Trajectory Optimization*. **IEEE Transactions on Wireless Communications**, 16(6), 3747–3760. DOI: 10.1109/TWC.2017.2688328. (Received 5 Aug 2016; revised 15 Nov 2016 and 1 Feb 2017; accepted 15 Mar 2017; date of publication 28 Mar 2017; date of current version 8 Jun 2017.)

## TL;DR

A foundational **energy-efficient UAV communication** paper. For a UAV flying horizontally at fixed altitude communicating with a ground terminal (GT), it introduces a design paradigm that jointly weighs **communication throughput** against **UAV propulsion energy**. It first derives the **first theoretical propulsion-energy model for fixed-wing UAVs** as a function of flying speed, direction, and acceleration, then defines **energy efficiency (bits/Joule)** = total bits communicated ÷ propulsion energy over a finite horizon. It shows unconstrained rate-maximization and energy-minimization both give **vanishing** energy efficiency, then optimizes a practical **circular trajectory** (radius + speed) and finally a **generally constrained** trajectory via linear state-space approximation + **sequential convex optimization (SCA)**.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: One fixed-wing UAV flies horizontally at fixed altitude and communicates with one ground terminal over a finite horizon. LoS rate depends on distance, while propulsion energy depends on velocity and acceleration and diverges as speed approaches zero.

**Problem & objective**: A fractional trajectory-control problem maximizes communication energy efficiency, $\max \eta=\frac{\int_0^T R(\mathbf q(t))dt}{E_{\mathrm{prop}}(\mathbf q,\mathbf v,\mathbf a)}$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV position | $\mathbf q(t)$ | continuous 2-D trajectory | Horizontal flight path |
| UAV velocity | $\mathbf v(t)$ | continuous vector | Flight speed and direction |
| UAV acceleration | $\mathbf a(t)$ | continuous vector | Maneuvering input |
| Circular radius and speed | $r,V$ | continuous, positive | Practical circular-orbit design |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Position, velocity, and acceleration satisfy the state dynamics |
| C2 | Speed remains between fixed-wing minimum and maximum bounds |
| C3 | Acceleration magnitude remains within its limit |
| C4 | Prescribed initial and final positions and velocities are met |
| C5 | Propulsion energy follows the derived speed-and-acceleration model |

**Algorithm**: Derive the fixed-wing propulsion model → show unconstrained rate-only and energy-only extrema have vanishing bits per joule → jointly optimize circular radius and speed for the practical orbit → linearize the state dynamics and non-convex rate-energy terms → solve sequential convex approximations for the generally constrained trajectory.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zeng and Zhang [x] studied energy-efficient UAV communication through trajectory optimization for one fixed-wing UAV and one ground terminal. They derived a propulsion-energy model that depends on flight velocity and acceleration and defined energy efficiency as communicated bits per propulsion joule. The circular design jointly optimizes orbit radius and speed, while the general formulation controls position, velocity, and acceleration under state, speed, acceleration, and endpoint constraints. A linear state-space approximation and sequential convex optimization produce a locally optimized constrained trajectory. Numerical results report higher energy efficiency than the evaluated rate-maximizing and propulsion-energy-minimizing trajectories.

## Problem framing

UAV endurance and performance are fundamentally limited by finite onboard energy (aircraft size/weight constraints), so maximizing information bits per unit energy is paramount. UAV energy efficiency differs from terrestrial: (1) the motivation is critical endurance, not just cost; and (2) UAVs incur **propulsion power** to stay aloft and move, usually far exceeding communication power, and this propulsion energy depends on flight velocity and acceleration — so it must enter the design. Existing UAV energy-efficiency studies ignored propulsion energy, and trajectory-optimization studies ignored energy efficiency; this work joins them with a generic UAV energy model.

## System model

- **Actor.** A single **fixed-wing** UAV at fixed altitude communicating with one ground terminal over a finite horizon $T$; the channel is LoS-dominated and distance-dependent.
- **Propulsion-energy model.** A derived closed form relating fixed-wing propulsion power to **speed and acceleration** (drag decomposed into parasitic $c_1 V^2$ and lift-induced $c_2\kappa^2/V^2$ terms; minimum drag $D_{\min}=2\sqrt{c_1 c_2}$ at the drag-minimum speed $V_{dm}=(c_2/c_1)^{1/4}$). Fixed-wing power **diverges as $V\to 0$** (cannot hover) — contrast with the [[rotary-wing-propulsion-energy-model]].
- **Metric.** Energy efficiency in **bits/Joule** = communicated bits normalized by propulsion energy (radiation/signal-processing energy ignored).

## Method

- **Unconstrained analysis.** Show rate-maximization (hover nearest GT) and energy-minimization both drive energy efficiency to **zero**, so neither is energy-efficient.
- **Circular trajectory.** Introduce a practical circular path centered at the GT and **jointly optimize flight radius and speed** to maximize energy efficiency — a closed practical design for how a fixed-wing UAV should orbit a GT.
- **Generally constrained trajectory.** With constraints on initial/final location and velocity, and min/max speed and acceleration, propose an efficient algorithm using **linear state-space approximation + [[alternating-optimization-sdr-sca|sequential convex optimization]]** to find an approximately optimal trajectory.

## Key findings

- Both the rate-maximization and energy-minimization designs are **energy-inefficient** (vanishing bits/Joule) for unconstrained trajectories — the paper's central insight motivating the energy-efficiency objective.
- The proposed circular and generally-constrained trajectory designs achieve **significantly higher energy efficiency** than rate-maximization or energy-minimization benchmarks (numerical results, parse; specific bits/Joule curves figure-derived and indicative).
- The derived fixed-wing propulsion-energy model is the first to relate UAV energy to **both velocity (speed + direction) and acceleration**, where prior models used speed only.

## Limitations / future work

The derived model assumes **straight-and-level (constant-altitude) flight**; the more general model with **ascending/descending** is left as future work, as is extension to **rotary-wing** UAVs (model modified accordingly). Single GT, fixed altitude.

## Relation to the corpus

A canonical **UAV-communications energy-efficiency** anchor from the Zeng/Zhang group. Its fixed-wing propulsion-energy model (grounding the new [[fixed-wing-propulsion-energy-model]] concept) is the counterpart to the [[rotary-wing-propulsion-energy-model]] later derived in [[zeng-2019-rotary-wing-energy-min]] — together they are the two propulsion-energy references the corpus's energy-aware [[uav-trajectory-control]] work builds on. Its SCA trajectory machinery recurs in the multi-UAV max-min-rate design [[wu-2018-multiuav-minrate-trajectory]], and the broader UAV-comms context is surveyed in [[zeng-2019-uav-comm-tutorial-5g]]. A communications (bits/Joule) framing rather than compute offloading.

## Raw artifacts

- `raw/sources/Energy-Efficient_UAV_Communication_With_Trajectory_Optimization/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
