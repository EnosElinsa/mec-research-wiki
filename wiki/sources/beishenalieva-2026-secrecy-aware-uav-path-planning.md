---
type: source
title: "Secrecy-Aware UAV Path Planning and Offloading Strategy Optimization Using Deep Reinforcement Learning and Particle Swarm Optimization"
authors: ["Aliia Beishenalieva", "Sang-Jo Yoo"]
year: 2026
url: "https://doi.org/10.1109/TITS.2025.3631889"
venue: "IEEE Transactions on Intelligent Transportation Systems (IEEE T-ITS)"
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
updated: 2026-07-07
---

# Secrecy-Aware UAV Path Planning and Offloading Strategy Optimization Using Deep Reinforcement Learning and Particle Swarm Optimization

## Citation

Beishenalieva, A., & Yoo, S.-J. (2026). *Secrecy-Aware UAV Path Planning and Offloading Strategy Optimization Using Deep Reinforcement Learning and Particle Swarm Optimization*. **IEEE Transactions on Intelligent Transportation Systems**. DOI: 10.1109/TITS.2025.3631889. DOI/venue/year are parse-silent at the top level and verified against a title-matched Crossref/IEEE DOI record.

## TL;DR

Builds a secure UAV-assisted ITS offloading framework where legitimate serving UAVs collect data from ground edge units, a legitimate jamming UAV emits artificial noise, and malicious eavesdropping/jamming UAVs threaten secrecy. A policy-gradient DRL controller, instantiated with PPO/A2C comparisons, chooses UAV mobility, mode, and power; [[particle-swarm-optimization]] then allocates time slots inside each coverage frame.

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

- `raw/sources/Secrecy-Aware UAV Path Planning and Offloading Strategy Optimization Using Deep Reinforcement Learning and Particle Swarm Optimization/Secrecy-Aware UAV Path Planning and Offloading Strategy Optimization Using Deep Reinforcement Learning and Particle Swarm Optimization.md`
- Original PDF and extracted figures (`images/`) in the same folder.
