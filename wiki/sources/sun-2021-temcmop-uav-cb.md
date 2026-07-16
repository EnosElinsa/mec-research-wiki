---
type: source
modeling_card: required
title: "Time and Energy Minimization Communications Based on Collaborative Beamforming for UAV Networks: A Multi-Objective Optimization Method"
authors: ["Geng Sun", "Jiahui Li", "Yanheng Liu", "Shuang Liang", "Hui Kang"]
year: 2021
url: "https://doi.org/10.1109/JSAC.2021.3088720"
venue: "IEEE Journal on Selected Areas in Communications (IEEE JSAC)"
tags: [source, collaborative-beamforming, multi-objective-optimization, ant-lion-optimizer, swarm-intelligence, uav-communications, energy-efficiency]
related:
  - "[[collaborative-beamforming]]"
  - "[[ant-lion-optimizer]]"
  - "[[fixed-wing-propulsion-energy-model]]"
  - "[[multi-verse-optimizer]]"
  - "[[salp-swarm-algorithm]]"
  - "[[collaborative-beamforming-in-aerial-mec]]"
  - "[[liang-2024-hmecmop-uav-cb]]"
  - "[[zheng-2024-recmop-uav-cb]]"
  - "[[liu-2024-hatrpo-ucb-cb]]"
  - "[[li-2024-emssa-uav-swarm-vaa]]"
  - "[[geng-sun]]"
  - "[[jiahui-li]]"
  - "[[shuang-liang]]"
  - "[[hui-kang]]"
created: 2026-06-02
updated: 2026-07-16
---

# Time and Energy Minimization Communications Based on Collaborative Beamforming for UAV Networks: A Multi-Objective Optimization Method

## Citation

Sun, G., Li, J., Liu, Y., Liang, S., & Kang, H. (2021). *Time and Energy Minimization Communications Based on Collaborative Beamforming for UAV Networks: A Multi-Objective Optimization Method*. **IEEE Journal on Selected Areas in Communications**, 39(11), 3555–3572. DOI: 10.1109/JSAC.2021.3088720. (Manuscript received 14 October 2020; accepted 12 April 2021; date of publication 14 June 2021; date of current version 18 October 2021.)

## TL;DR

Studies a UAV network where a set of UAVs form a **virtual antenna array (VAA)** and use **collaborative beamforming (CB)** to communicate, in turn, with several remote base stations (BSs). Because the UAVs start at random/discrete positions, performing a good VAA requires them to fly to optimal positions (at optimal speeds) and adjust optimal **excitation current weights** — which costs time and energy and trades off against transmission performance. The paper formulates a **time and energy minimization communication multi-objective optimization problem (TEMCMOP)** that simultaneously minimizes (i) total transmission time, (ii) total VAA-performing time, and (iii) total motion + hovering energy of the UAVs, by jointly optimizing UAV positions, flight speeds, excitation current weights, and the **order** of communicating with the different BSs. The problem is proven **NP-hard**; the authors derive an **energy-optimal flight-speed strategy** to reformulate it (R-TEMCMOP), then solve it with an **improved multi-objective ant lion optimizer (IMOALO)**.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Several UAVs form a virtual antenna array and sequentially use collaborative beamforming to communicate with remote base stations. UAVs fly from random initial positions to VAA configurations, choose excitation currents and flight speeds, and pay motion, hovering, VAA-formation, and transmission energy.

**Problem & objective**: TEMCMOP, an NP-hard mixed discrete-continuous multi-objective problem, minimizes $\big(T_{\mathrm{trans}},T_{\mathrm{VAA}},E_{\mathrm{motion+hover}}\big)$ over UAV positions, speeds, excitation weights, and BS service order.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV positions | $\mathbf q_i$ | continuous 3-D positions | VAA formation points for UAV $i$ |
| Flight speeds | $v_i$ | continuous, speed-bounded | Speed used to reach each formation |
| Excitation currents | $w_i$ | complex/continuous bounded weights | Per-UAV CB amplitude and phase weights |
| BS service order | $\pi$ | discrete permutation | Order in which remote BSs are served |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | UAV positions and inter-UAV distances satisfy formation and collision limits |
| C2 | Flight speeds obey aircraft speed bounds and energy-optimal speed relations |
| C3 | Excitation currents satisfy amplitude, phase, and collaborative-beamforming limits |
| C4 | Each remote BS is served once in the selected order |
| C5 | Transmission, VAA-formation, and motion times/energies are computed consistently |

**Algorithm**: Derive the energy-optimal flight-speed strategy and reformulate TEMCMOP as R-TEMCMOP → initialize a mixed continuous/discrete population with chaos and opposition learning → update solutions with the hybrid IMOALO operator → retain the nondominated Pareto set.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Sun et al. [x] studied time and energy minimization for UAV networks that form virtual antenna arrays through collaborative beamforming. They formulated an NP-hard multi-objective problem that minimizes transmission time, VAA-formation time, and UAV motion and hovering energy by jointly optimizing UAV positions, flight speeds, excitation currents, and the order of remote base-station service. An energy-optimal speed strategy removes the speed dimension and yields the reformulated R-TEMCMOP. The improved multi-objective ant lion optimizer uses chaos and opposition-based initialization and a mixed continuous/discrete update operator to obtain a Pareto set. Simulations report the best overall three-objective performance among the evaluated collaborative-beamforming and evolutionary baselines.

## Problem framing

UAV communications face limited on-board energy and restricted transmit power, making it hard for a single UAV to reach a remote BS efficiently. Flying a UAV close to each receiver shortens link distance but costs motion energy and task-completion time. Collaborative beamforming lets distributed UAVs act as one VAA, producing a high-gain mainlobe toward the remote BS to raise transmission rate and extend range — but forming the VAA is itself time- and energy-consuming because the UAVs must fly to suitable positions, the per-element excitation weight critically shapes the beam pattern, and flight speed affects both completion time and energy. Prior CB-by-UAV works optimize beam directivity/sidelobe, transmission/control time, or rate, but not the joint trade-off of positions, excitation weights, speeds, and BS-serving order under simultaneous time and energy objectives. The paper targets exactly this multi-objective trade-off.

## System model

- **Scenario.** Several UAVs perform a UAV-enabled VAA to communicate with `N` remote BSs sequentially via CB (a typical data-collection scenario); each round the swarm flies to a configuration, forms the VAA, and beams to a BS.
- **Decision variables.** UAV positions, flight speeds, per-UAV excitation current weights, and the order in which BSs are served — a **hybrid** solution space with continuous (positions, speeds, weights, time) and discrete (BS order) dimensions.
- **Objectives (all minimized).** Total transmission time, total performing time of the UAV-enabled VAAs, and total motion + hovering energy consumption of the UAVs. The objectives trade off against each other (e.g. flying to a better beamforming geometry cuts transmission time but raises motion energy).
- **Energy model.** Based on the UAV energy-consumption model of Zeng et al. ([14] in the parse); the paper investigates the relationship between VAA-performing time, UAV flight speeds, and motion energy, and **derives the energy-optimal flight-speed strategy**, which reformulates TEMCMOP into the more tractable R-TEMCMOP.
- **Hardness.** The formulated TEMCMOP and its trade-offs are analyzed and proven **NP-hard**.

## Method

- **Reformulation.** The energy-optimal flight-speed strategy collapses the speed dimension, yielding R-TEMCMOP with mixed continuous + discrete solution dimensions.
- **IMOALO.** An improved multi-objective ant lion optimizer solves R-TEMCMOP. Two improvements: (i) **chaos + opposition-based learning (chaos-OBL)** initialization to improve initial-solution quality, and (ii) a **hybrid solution-update operator** to handle the mixed continuous/discrete solution space that conventional swarm-intelligence algorithms (e.g. standard MOALO) struggle with.
- **Solution concept.** A multi-objective problem returns a **Pareto-optimal (non-dominated) set**; a decision-maker selects a preferred trade-off afterward.

## Key findings

- IMOALO **effectively solves** the formulated TEMCMOP and achieves the **overall best performance** across the three objectives when communicating with different BSs, compared with CB-based baselines (LAA, RAA, MPOECW, MODA, MOPSO, NSGA-II, and conventional MOALO).
- The proposed CB-based communication strategy is shown **more suitable** for the considered scenario than alternative UAV communication strategies. A discussion section analyzes the effect of UAV flight strategies, collision-avoidance methods, channel models, and carrier frequency (noting most UAV systems operate at 2.4 GHz). Specific numeric margins are figure-derived; treat exact values as indicative.

## Limitations / future work

Evaluation is **simulation-only**. The CB model assumes phase synchronization (the paper analyzes the effect of phase errors from imperfect synchronization / phase jitter separately) and a chosen channel model / carrier frequency; collision avoidance and flight strategy are addressed in discussion rather than as hard constraints in the core formulation. Explicit future-work statements are `not in parse`.

## Relation to the corpus

The **earliest** collaborative-beamforming entry in the corpus and the methodological seed of the [[geng-sun]]-group CB thread mapped in [[collaborative-beamforming-in-aerial-mec]]. It introduces the recurring CB design tension — improving the beam (here, transmission time) requires flying, which costs energy — that every later CB source inherits. Where this paper uses a pure swarm-intelligence solver ([[ant-lion-optimizer|IMOALO]]) on a time/VAA-time/energy objective set, the later [[liang-2024-hmecmop-uav-cb]] uses the [[multi-verse-optimizer]] on a hovering-vs-motion-energy split, [[zheng-2024-recmop-uav-cb]] the gravitational-search algorithm on a reliability + propulsion-energy set, [[li-2024-emssa-uav-swarm-vaa]] the [[salp-swarm-algorithm]], and [[liu-2024-hatrpo-ucb-cb]] a heterogeneous-agent MADRL — all sharing the BS-serving / positions / excitation-weights structure first formulated here. It complements the UAV-mobile-relaying and energy-model foundations of the corpus's UAV-communications track.

## Raw artifacts

- `raw/sources/Time_and_Energy_Minimization_Communications_Based_on_Collaborative_Beamforming_for_UAV_Networks_A_Multi-Objective_Optimization_Method/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
