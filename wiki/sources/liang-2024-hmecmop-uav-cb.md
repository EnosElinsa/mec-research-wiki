---
type: source
title: "Multiobjective Optimization Approach for Reducing Hovering and Motion Energy Consumptions in UAV-Assisted Collaborative Beamforming"
authors: ["Shuang Liang", "Minghao Yin", "Geng Sun", "Jiahui Li"]
year: 2024
url: "https://doi.org/10.1109/JIOT.2023.3315708"
venue: "IEEE Internet of Things Journal (IEEE IoT-J)"
tags: [source, collaborative-beamforming, multi-objective-optimization, energy-efficiency, multi-verse-optimizer, virtual-antenna-array, rotary-wing-propulsion-energy-model, uav-data-collection]
related:
  - "[[collaborative-beamforming]]"
  - "[[multi-verse-optimizer]]"
  - "[[rotary-wing-propulsion-energy-model]]"
  - "[[uav-data-collection]]"
  - "[[mixed-integer-nonlinear-programming]]"
  - "[[salp-swarm-algorithm]]"
  - "[[li-2024-emssa-uav-swarm-vaa]]"
  - "[[sun-2025-emoppo-vlh-aerial-cb]]"
  - "[[collaborative-beamforming-in-aerial-mec]]"
  - "[[geng-sun]]"
created: 2026-06-01
updated: 2026-06-01
---

# Multiobjective Optimization Approach for Reducing Hovering and Motion Energy Consumptions in UAV-Assisted Collaborative Beamforming

## Citation

Liang, S., Yin, M., Sun, G., & Li, J. (2024). *Multiobjective Optimization Approach for Reducing Hovering and Motion Energy Consumptions in UAV-Assisted Collaborative Beamforming*. **IEEE Internet of Things Journal**. DOI: 10.1109/JIOT.2023.3315708. (Manuscript received 14 July 2023; accepted 11 September 2023; date of publication 15 September 2023; date of current version 6 February 2024 → year 2024 per the date-of-current-version convention.)

## TL;DR

For UAV-assisted **collaborative beamforming (CB)** — where a swarm of UAVs forms a **virtual antenna array (VAA)** to reach several faraway base stations (BSs) — the paper formulates a **hovering and motion energy consumption multiobjective optimization problem (HMECMOP)** that simultaneously **minimizes total hovering energy and total motion energy** of the UAVs by jointly choosing UAV positions, excitation-current weights (ECWs), and the **order** of communicating with the different BSs. The problem is proven **NP-hard** and a **hybrid MOP** (mixed continuous + discrete variables), and is solved by an **improved multiobjective multiverse optimizer (IMOMVO)** that uses a vertical-and-horizontal renewal strategy and a nearest-neighbor procedure (NNP) to handle the mixed solution space.

## Problem framing

UAVs have limited onboard energy and transmit power, which makes communicating with **remote BSs** hard. CB boosts transmission range/directivity by coherently combining UAV signals into a VAA, avoiding the energy cost of approaching BSs or building multihop flying ad-hoc links and avoiding the weight cost of directional antennas. But CB performance depends on the UAV **positions** and **ECWs**, and constructing a good VAA requires extra flights — so **hovering energy** (faster transmission ⇒ less hovering) and **motion energy** (forming the array ⇒ more flight) are in tension, motivating a multiobjective formulation.

## System model

- **Setup.** A set of rotary-wing UAVs (flying at ~100 m, omnidirectional ISM-band antennas) form a VAA and use CB to communicate with $N_\text{BS}$ randomly-distributed remote BSs, in disaster-relief or agricultural data-collection scenarios where terrestrial infrastructure is unavailable; data are cached then backhauled.
- **Array factor / beam gain.** The VAA array factor sums per-UAV excitation-weighted phase terms over 3D positions; the beam gain toward a BS follows the standard far-field expression. CB can ideally achieve a gain scaling with the **square** of the UAV count.
- **Energy model.** Rotary-wing **propulsion energy** (blade-profile + induced + parasite terms) dominates communication energy (the latter is ignored); a heuristic closed-form approximation adds kinetic and potential terms for arbitrary 3D (climb/descent) trajectories. A lemma establishes that vertical flight costs more energy per unit distance than horizontal flight.
- **Decision variables.** Per-UAV 3D positions, ECWs, and the BS communication sequence.
- **Objectives.** (1) Total hovering energy and (2) total motion energy, both minimized (Pareto front of trade-off solutions).

## Method

- **IMOMVO** — an improved multiobjective **multiverse optimizer** ([[multi-verse-optimizer]]) tailored to the hybrid (continuous positions/ECWs + discrete BS order) HMECMOP.
- **Vertical-and-horizontal renewal strategy** plus a **nearest-neighbor procedure (NNP)** to update solutions across the mixed continuous/discrete solution space.
- Maintains a Pareto-optimal set/front; policymakers pick a trade-off solution per application.

## Key findings

- IMOMVO **effectively reduces the UAVs' hovering and motion energy** when communicating with multiple remote BSs, improving communication performance, versus conventional methods such as multihop communications (the paper's stated result; comparative magnitudes live in the simulation figures and are indicative).
- A VAA achieves a markedly higher transmission rate than a single UAV over multi-km distances (Fig. 2, parse; figure-derived, indicative), motivating CB for remote-BS data backhaul.

## Limitations / future work

The model ignores UAV communication energy (propulsion dominates), assumes LoS A2G channels at altitude, and uses a fixed UAV count. The parse does not enumerate an explicit future-work list → `not in parse`.

## Relation to the corpus

A **collaborative-beamforming / virtual-antenna-array** entry from the Jilin-University group around [[geng-sun]] and [[jiahui-li]], and a methodological sibling of [[li-2024-emssa-uav-swarm-vaa]] (which uses an enhanced [[salp-swarm-algorithm]] for a time/eavesdropper/energy MOP) and [[sun-2025-emoppo-vlh-aerial-cb]] (evolutionary multi-objective PPO). Unlike those, this one targets the **hovering-vs-motion energy** trade specifically and solves it with the [[multi-verse-optimizer]] (grounding that concept's CB use), placing it in the [[collaborative-beamforming-in-aerial-mec]] synthesis. Reinforces [[collaborative-beamforming]], [[uav-data-collection]], and the [[rotary-wing-propulsion-energy-model]].

## Raw artifacts

- `raw/sources/Multiobjective_Optimization_Approach_for_Reducing_Hovering_and_Motion_Energy_Consumptions_in_UAV-Assisted_Collaborative_Beamforming/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
