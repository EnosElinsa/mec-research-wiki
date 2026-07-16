---
type: source
title: "Secrecy-Aware UAV Path Planning and Offloading Strategy Optimization Using Deep Reinforcement Learning and Particle Swarm Optimization"
authors: ["Aliia Beishenalieva", "Sang-Jo Yoo"]
year: 2026
url: "https://doi.org/10.1109/TITS.2025.3631889"
venue: "IEEE Transactions on Intelligent Transportation Systems (IEEE T-ITS)"
modeling_card: required
tags: [source, uav-enabled-its, physical-layer-security, ppo, particle-swarm-optimization, friendly-jamming, task-offloading]
related:
  - "[[uav-enabled-its]]"
  - "[[physical-layer-security]]"
  - "[[friendly-jamming-uav]]"
  - "[[particle-swarm-optimization]]"
  - "[[ppo]]"
  - "[[task-offloading]]"
  - "[[task-priority-in-mec]]"
created: 2026-07-07
updated: 2026-07-16
---

# Secrecy-Aware UAV Path Planning and Offloading Strategy Optimization Using Deep Reinforcement Learning and Particle Swarm Optimization

## Citation

Beishenalieva, A., & Yoo, S.-J. (2026). *Secrecy-Aware UAV Path Planning and Offloading Strategy Optimization Using Deep Reinforcement Learning and Particle Swarm Optimization*. **IEEE Transactions on Intelligent Transportation Systems**. DOI: 10.1109/TITS.2025.3631889. DOI/venue/year are parse-silent at the top level and verified against a title-matched Crossref/IEEE DOI record.

## TL;DR

Builds a secure UAV-assisted ITS offloading framework where legitimate serving UAVs collect data from ground edge units, a legitimate jamming UAV emits artificial noise, and malicious eavesdropping/jamming UAVs threaten secrecy. A policy-gradient DRL controller, instantiated with PPO/A2C comparisons, chooses UAV mobility, mode, and power; [[particle-swarm-optimization]] then allocates time slots inside each coverage frame.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Ground edge units buffer ITS sensing data for legitimate serving UAVs, while legitimate jamming UAVs emit artificial noise against mobile eavesdropping UAVs and malicious jamming UAVs interfere with collection. Directional serving-UAV links and omnidirectional ground/jamming links use free-space distance-based gains, and serving UAVs coordinate through a FANET while operating asynchronously in bounded frames.

**Problem & objective**: The MDP controller maximizes cumulative $R_{\mathrm{total}}(t+1)=R(t+1)(1-p_s^{\mathrm{ISO}})$, where $R(t+1)=w_1^rR_{\mathrm{data}}(t+1)+w_2^rR_{\mathrm{delay}}(t+1)+w_3^rR_{\mathrm{energy}}(t+1)$ and $w_1^r+w_2^r+w_3^r=1$; the second-stage PSO maximizes the analogous slot-allocation fitness $F(t+1)$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Serving-UAV position | $W_s(t)$ | Continuous, $\mathbb{R}^3$ | Next 3D position of legitimate serving UAV $s$ |
| Serving-UAV power | $P_s(t)$ | Continuous, $[P_s^{\min},P_s^{\max}]$ | Serving-UAV transmit power |
| Jamming-UAV modes | $MM_{lj}(t),AM_{lj}(t)$ | Discrete | Move or stay, and broadcast artificial noise or remain idle |
| Jamming-UAV control | $W_{lj}(t),P_{lj}(t)$ | Continuous | Next position and transmit power when the selected modes activate them |
| Ground-unit power | $P_{gu_g^s}(t)$ | Continuous, $[P_g^{\min},P_g^{\max}]$ | Transmit power of a covered ground edge unit |
| Slot assignment | $\mathfrak{s}_g(n)$ | Binary, $\{0,1\}$ | Whether slot $n$ is allocated to ground edge unit $g$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| 11 | FANET connectivity and separation, $d_{ss}^{\min}\leq d_{ss}\leq d_{ss}^{\max}$ |
| 13 | Legitimate-UAV residual energy, $E_i(t)\geq E_{\min}$ for $i\in\{s,lj\}$ |
| 14-16 | Serving-UAV, jamming-UAV, and ground-unit transmit powers remain within their respective minimum and maximum values |
| 17-18 | Frame duration satisfies $FL(t)\leq FL_{\max}$ and $FL(t)=\sum_{g\in\mathcal{GU}_s}N_g^{ts}$ |
| 19 | Single-user slot access, $\sum_{g\in\mathcal{GU}_s}\mathfrak{s}_g(n)\leq1$ with $\mathfrak{s}_g(n)\in\{0,1\}$ |

**Algorithm**: Policy-gradient DRL, evaluated with PPO and A2C losses, observes demand, locations, priorities, delay, service frequency, power, and energy, then selects mixed discrete and continuous UAV controls. For each selected serving-UAV position, PSO initializes feasible slot vectors, rejects vectors with $FL>FL_{\max}$, and updates particle velocities and positions against the data, delay, and hovering-energy fitness until returning the global-best allocation.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Beishenalieva and Yoo [x] studied secure UAV-assisted collection of ITS sensing data when legitimate serving and jamming UAVs face mobile aerial eavesdroppers and jammers. Their policy-gradient controller jointly selects serving-UAV trajectories and powers, jamming-UAV movement and activity modes, and covered ground-unit transmit powers. The reward combines securely served data, service satisfaction and frequency, secrecy rate, delay, and energy, while enforcing flight, connectivity, power, energy, frame-length, and single-user scheduling limits. After each serving UAV selects a position, particle swarm optimization assigns slots to covered ground units within the maximum frame length. Simulations identified a PPO clipping value of 0.2 as the most stable evaluated setting and reported higher average data reward for PPO than for A2C, hierarchical-reward PPO, optimum hovering, and random-action baselines. A 30-particle PSO configuration reached the best tested allocation within 10 iterations and used 600 evaluations in an example that required 3,200,000 evaluations under full search.

## Problem

RSU-based ITS data collection can fail under coverage gaps, congestion, outages, or attacks. UAVs can fill the gap, but their line-of-sight air-ground links expose traffic-sensing data to eavesdropping and jamming. The paper targets secure, low-delay, energy-aware offloading when the attackers are airborne and mobile rather than fixed ground eavesdroppers.

## System model

The system has ground edge units (GEUs) representing vehicle sensors, roadside sensors, and local traffic aggregators; legitimate serving UAVs (LSUs) collecting data; legitimate jamming UAVs (LJUs) transmitting artificial noise; malicious eavesdropping UAVs (MEUs); and malicious jamming UAVs (MJUs). GEUs have ON/OFF data-generation states, priority levels, and buffered offloading demand. LSUs move asynchronously across 3D positions, can hover only for a bounded frame length, and must return for recharge when energy constraints require it. The simulation uses a real Incheon map, 100 GEUs, 10 hotspots, a 500 m by 500 m by 100 m region, two LSUs, one LJU, three MEUs, and one MJU.

## Method

The high-level controller is a policy-gradient DRL loop that observes GEU demand, UAV positions, adversary positions, secrecy risk, and energy state, then chooses serving-UAV movement, transmission power, and jamming-UAV activity. Its reward combines served secure data, delay, energy, priority, service frequency, and secrecy rate. After the serving UAV selects a position, a PSO scheduler assigns slots to covered GEUs within the maximum frame length, optimizing data, delay, fairness, hovering energy, and frame-length feasibility.

## Key findings

- PPO clip 0.2 is selected because it gives more stable and higher served offloading demand than the tested alternatives.
- Reward curves converge under multiple reward-weight settings; the paper uses the data/energy/delay weight setting reported for subsequent evaluations.
- Increasing the number of LSUs can reduce total reward when there are too few GEUs because UAV energy is spent without enough data to collect.
- The dynamic-altitude malicious-UAV environment reports better secrecy-rate and delay-reward behavior than the fixed-height square-trajectory environment.
- PSO with 30 particles converges to the best slot-allocation solution within 10 iterations; in the example table, PSO uses 600 evaluations versus 3,200,000 for full search.
- PPO obtains higher average data reward than A2C, HRF-PPO, optimum-hovering, and random-action baselines; the optimum-hovering baseline requires nearly twice the operational-cycle time reported for the other methods.
- A reimplemented baseline converges faster, but the proposed method achieves a higher secrecy rate per time slot in the parsed comparison.

## Limitations / future work

The paper reports no real-world deployment, citing cost, complexity, regulatory barriers, missing public datasets, and difficulty building large aerial-ground testbeds. Future directions include prototype field validation, hardware-in-the-loop simulation, and meta-RL or game-theoretic adversarial learning for attackers that learn and adapt rather than following predefined or probabilistic mobility patterns.

## Relation to the corpus

This source connects [[uav-enabled-its]], [[physical-layer-security]], [[friendly-jamming-uav]], [[ppo]], and [[particle-swarm-optimization]]. It differs from vehicular-MEC offloading papers such as [[ji-2026-llm-iov-uav-offloading]] because the tasks are ITS sensing/offloading streams collected by UAVs, not computation jobs generated by vehicles. It also extends the anti-jamming/security-DRL track by combining legitimate jamming, airborne eavesdroppers, airborne jammers, and PSO slot scheduling in one control loop.

## Raw artifacts

- `raw/sources/Secrecy-Aware_UAV_Path_Planning_and_Offloading_Strategy_Optimization_Using_Deep_Reinforcement_Learning_and_Particle_Swarm_Optimization/Secrecy-Aware_UAV_Path_Planning_and_Offloading_Strategy_Optimization_Using_Deep_Reinforcement_Learning_and_Particle_Swarm_Optimization.md`
- Original PDF and extracted figures (`images/`) in the same folder.
