---
type: source
modeling_card: required
title: "AoI and Energy Tradeoff for Aerial-Ground Collaborative MEC: A Multi-Objective Learning Approach"
tags: [source, age-of-information, aoi-energy-tradeoff, multi-objective-reinforcement-learning, uav-mec, high-altitude-platform, hap-uav, ppo, evolutionary-rl, task-offloading, trajectory-control]
related:
  - "[[age-of-information]]"
  - "[[aoi-energy-tradeoff]]"
  - "[[multi-objective-reinforcement-learning]]"
  - "[[multi-objective-mdp-vectorial-reward]]"
  - "[[evolutionary-reinforcement-learning]]"
  - "[[mobile-edge-computing]]"
  - "[[task-offloading]]"
  - "[[uav-trajectory-control]]"
  - "[[high-altitude-platform-station]]"
  - "[[air-ground-integrated-network]]"
  - "[[hierarchical-aerial-mec]]"
  - "[[ppo]]"
  - "[[gae]]"
  - "[[binary-vs-partial-offloading]]"
  - "[[jia-2025-dro-uav-hap-mec]]"
  - "[[nabi-2025-jour-hierarchical-aerial]]"
  - "[[liu-2025-haps-uav-maritime-iot]]"
  - "[[peng-2024-energy-time-uav-its]]"
  - "[[peng-2022-cmop-uav-path-planning]]"
  - "[[huang-2023-mu-aec-task-energy]]"
created: 2026-05-29
updated: 2026-07-16
authors: [Fuhong Song, Qixun Yang, Mingsen Deng, Huanlai Xing, Yanping Liu, Xi Yu, Kaiju Li, Lexi Xu]
year: 2024
url: "https://doi.org/10.1109/TMC.2024.3394568"
venue: "IEEE Transactions on Mobile Computing (TMC)"
---

# AoI and Energy Tradeoff for Aerial-Ground Collaborative MEC: A Multi-Objective Learning Approach

## Citation

Song, F., Yang, Q., Deng, M., Xing, H., Liu, Y., Yu, X., Li, K., & Xu, L. (2024). *AoI and Energy Tradeoff for Aerial-Ground Collaborative MEC: A Multi-Objective Learning Approach*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2024.3394568.

## TL;DR
This paper studies the [[aoi-energy-tradeoff]] (the "AET problem") in an aerial-ground collaborative [[mobile-edge-computing]] system where a [[high-altitude-platform-station]] and a single rotary-wing UAV cooperate to serve ground devices (GDs): the UAV flies a planned path to collect tasks and either processes them locally or partially offloads them to the HAP. Total GD [[age-of-information]] and total UAV energy are conflicting objectives, so rather than the usual fixed-weight scalarization, the authors model the problem as a [[multi-objective-mdp-vectorial-reward]] and solve it with **MOL-AET**, a [[multi-objective-reinforcement-learning]] algorithm that combines multi-objective [[ppo]] (training) with policy-network genetic operators ([[evolutionary-reinforcement-learning]], the evolutionary phase) to output a set of nondominated policies. MOL-AET improves average AoI, energy, and cost by at least 39.8%, 2.1%, and 15.3% over two MOEAs and three MORL variants.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: One rotary-wing UAV collects tasks from static ground devices without cellular coverage and either computes them locally or partially offloads them to a high-altitude platform. TDMA separates collection, the UAV flies at fixed height, and the AoI of each device resets after successful collection while propulsion and computing energy accumulate.

**Problem & objective**: The AET multi-objective MDP minimizes total ground-device AoI and total UAV energy, $\min(A_{\mathrm{total}},E_{\mathrm{total}})$, subject to region, coverage, movement, queue, and per-device AoI limits.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Flight direction | $b_t$ | continuous/discretized angle | UAV direction in slot $t$ |
| Flight distance | $d_t$ | continuous/discretized, $[0,d_{\max}]$ | UAV displacement in slot $t$ |
| Partial offloading ratio | $o_t$ | continuous, $[0,1]$ | Fraction of unfinished tasks sent to the HAP |
| Preference vector | $\mathbf w$ | continuous simplex | AoI-energy tradeoff used by one policy individual |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | UAV position remains in the rectangular flight region and speed is bounded |
| C2 | A ground device is collected only within the UAV coverage radius |
| C3 | The UAV task queue and per-slot local/HAP computing capacities remain feasible |
| C4 | Each device's AoI remains below $A_{\max}$ |
| C5 | Partial offloading ratios and HAP transmission resources stay in their domains |

**Algorithm**: Encode the two objectives as vector rewards → initialize individuals over preference vectors → train multi-objective PPO with GAE → maintain a nondominated policy set → evolve policy-network parameters by uniform crossover and Gaussian mutation → output the Pareto AoI-energy policies.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Song et al. [x] studied the age-of-information and energy tradeoff in an aerial-ground collaborative MEC system with one UAV and one high-altitude platform. They formulated a multi-objective problem that minimizes total ground-device AoI and UAV energy by optimizing UAV movement and partial task offloading under coverage, queue, region, and AoI constraints. MOL-AET models the problem as a vector-reward MDP, trains multiple preference-conditioned PPO policies, and applies crossover and Gaussian mutation to their policy networks. It returns a nondominated policy set for changing AoI-energy preferences. Simulations report average improvements of at least 39.8% in AoI, 2.1% in energy, and 15.3% in cost over the evaluated MOEA and MORL baselines.

## Problem
IoT ground devices (intelligent transport, forest-fire/environmental monitoring, autonomous driving) are computing-intensive and delay-sensitive but resource-limited, and terrestrial base stations may be unavailable in remote or disaster scenarios. UAVs bring compute and coverage close to GDs, but their energy and onboard compute are limited, so a HAP is introduced as a powerful collaborative tier the UAV can offload to ([[hierarchical-aerial-mec]], [[air-ground-integrated-network]]). Beyond latency, the **freshness** of collected data — measured by [[age-of-information]] — drives QoE in these applications. The paper formulates the AET problem as a multi-objective optimization: simultaneously minimize total GD AoI and total UAV energy by optimizing the UAV's per-slot flight (direction + distance) and [[task-offloading]] ratios. The objectives genuinely conflict (collecting more tasks lowers AoI but raises energy), and the authors argue prior work wrongly collapses this into a single objective with fixed preference weights — ignoring the conflict and failing when user preferences drift.

## System model
- **Tiers/actors**: one HAP (quasi-static stratospheric, fixed height H = 20 km, abundant compute) + one rotary-wing UAV (fixed height U, constant speed) + J static GDs scattered in a rectangle with no cellular coverage; TDMA for collection.
- **Time**: discrete slots of duration δ; the mission spans T slots.
- **UAV movement** ([[uav-trajectory-control]]): per-slot direction b_t ∈ [0,2π), distance d_t ∈ [0,d_max], confined to an X_max × Y_max region, speed ≤ v_max.
- **Energy**: standard rotary-wing propulsion power P(v) (blade-profile + induced + parasite) integrated over the mission, plus local-compute energy (effective capacitance κ) and HAP-offload transmission energy.
- **AoI** ([[age-of-information]]): A_t^j = δ(t − L_t^j); reset to δ when a GD's task is collected, otherwise grows by δ up to a tolerable A_max (beyond which the task is invalid).
- **Coverage**: only GDs within horizontal radius R_max = U·tan(ϑ_max) can be collected — so flying higher covers more GDs.
- **Compute/queue**: UAV holds a queue of capacity N_max = 10; each slot a fraction o_t ∈ [0,1] of unfinished tasks is offloaded to the HAP ([[binary-vs-partial-offloading]] — here partial), the rest run locally up to a per-slot cap φ.
- **Channel**: UAV→HAP free-space path loss + Shannon-Hartley rate; HAP processing and result-return delays/energy neglected (HAP assumed ample).
- **Assumptions**: static GDs, negligible collection delay/energy, single UAV, simulation-only.

## Method
- **Formulation**: the AET MOP (minimize (A_total, E_total) subject to movement/region/coverage and per-GD AoI ≤ A_max) is modeled as a [[multi-objective-mdp-vectorial-reward]] with two reward components, one per objective.
  - *State*: per-GD distances and AoIs + UAV status (slot, out-of-region indicator/count, coordinate, #unfinished and #collected tasks); normalized.
  - *Action*: a_t = (b_t, d_t, o_t) discretized to 8×7×11 = 616 combinations; the policy network uses three parallel sub-networks over a shared feature layer to avoid output blow-up.
  - *Vectorial reward*: r_t^A = negative AoI increment; r_t^E = −(E_t + ε_b) (scaled to match magnitudes); both penalized by ε_p on region exit.
- **MOL-AET** ([[multi-objective-reinforcement-learning]]), three phases:
  1. *Initialization*: n uniformly distributed preference weight vectors (systematic approach; e.g. m=2, β=29 → 30 weights), each defining a learning individual ⟨w, policy net, value net⟩.
  2. *Training*: multi-objective [[ppo]] (clipped surrogate objective + [[gae]]) trains each individual on the scalarized reward w·r_t; a nondominated/Pareto policy set Q* is maintained across individuals.
  3. *Evolutionary* ([[evolutionary-reinforcement-learning]]): gradient-free uniform crossover + Gaussian mutation applied directly to policy-network parameters of each individual and its matched nondominated peer, refining Q* and escaping premature convergence.
- **Rationale**: blend PPO's local exploitation with EA's global exploration since gradient descent alone falls into local optima while EAs alone are sample-inefficient in high dimensions. Output is a *set* of nondominated policies (one per preference), robust to shifting user preferences.

## Key findings
- MOL-AET improves average AoI / energy / cost by at least **39.8% / 2.1% / 15.3%** over the five baselines.
- **AAoI** cut on average by 50.6%, 46.3%, 52.2%, 45.9%, 39.9% vs NSGA-II, MOEA/D, MODQN, MOPG, MOPPO; best in all 9 instances.
- **AEC** cut on average by 19.1%, 18.9%, 13.3%, 6.9%, 2.1% vs the same five; best in 6/9 instances (MOPPO wins AEC in 3 instances but loses AAoI there).
- **AC** cut on average by 32.2%, 32.2%, 24.0%, 19.1%, 15.3%; best on cost in all instances — the strongest overall AoI-energy tradeoff.
- Algorithm metrics: far lower **IGD** and **GED** than all baselines, and **rank #1** in the Friedman test across IGD, GED, AAoI, AEC, AC.
- All MORL methods beat the MOEAs NSGA-II/MOEA/D (which choke on the length-900, high-dimensional dynamic MOP); MOPPO > MODQN/MOPG; the evolutionary phase further improves MOPPO (visible IGD improvement after generation 100).
- Preference behavior: energy-focused weight (0.2,0.8) → short cautious paths; AoI-focused weight (0.8,0.2) → long sweeping paths covering more GDs; AAoI falls as flight height U grows.
- Setup: 9 instances over J ∈ {60,100,140}, U ∈ {30,40,50}; A_max=300, N_max=10, d_max=30 m, v_max=30 m/s, f_UAV=1 GHz, H=20 km, γ=0.99, Φ_tra=Φ_evo=100.

## Limitations
Simulation-only on synthetic instances (no benchmark dataset, no hardware). Single UAV — multi-UAV collaboration, collision avoidance, and a planned multi-agent multi-objective + game-theory extension are deferred to future work. HAP compute and result-return delays/energy are neglected; GDs are static with neglected collection cost; action variables are discretized; and three of the MORL baselines (MODQN, MOPG, MOPPO) are self-implemented ablations of MOL-AET rather than independent prior systems.

## Relation to the corpus
This is an aerial-ground / [[hierarchical-aerial-mec]] work that, unlike most of the corpus, makes [[age-of-information]] a first-class objective and treats the [[aoi-energy-tradeoff]] as a true [[multi-objective-reinforcement-learning]] problem via a [[multi-objective-mdp-vectorial-reward]] rather than fixed-weight scalarization. Its HAP+UAV collaborative compute structure pairs naturally with [[jia-2025-dro-uav-hap-mec]], [[nabi-2025-jour-hierarchical-aerial]], and [[liu-2025-haps-uav-maritime-iot]]. Its multi-objective UAV trajectory/energy framing relates to [[peng-2024-energy-time-uav-its]] and [[peng-2022-cmop-uav-path-planning]] (which solve their MOPs with evolutionary algorithms rather than MORL — a clean DRL-vs-evolutionary contrast), and its delay/freshness-vs-energy tradeoff connects to [[huang-2023-mu-aec-task-energy]]. Methodologically it builds on [[ppo]] + [[gae]] and adds [[evolutionary-reinforcement-learning]] (genetic operators on policy-network parameters), a distinctive hybrid worth tracking.

## Raw artifacts
- `raw/sources/AoI_and_Energy_Tradeoff_for_Aerial-Ground_Collaborative_MEC_A_Multi-Objective_Learning_Approach/full.md`
- Original PDF (`59a5c499-4de5-4693-94d8-c8bb910236f5_origin.pdf`) and extracted figures (`images/`) in the same folder.
