---
type: source
title: "Joint Optimization of UAV-Carried IRS for Urban Low Altitude mmWave Communications With Deep Reinforcement Learning"
authors: ["Wenwen Xie", "Geng Sun", "Bei Liu", "Jiahui Li", "Jiacheng Wang", "Hongyang Du", "Dusit Niyato", "Dong In Kim"]
year: 2026
url: "https://doi.org/10.1109/TMC.2025.3600682"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
modeling_card: required
tags: [source, uav-mounted-ris, mmwave, urban, trajectory-optimization, ppo, energy-efficiency, fairness]
related:
  - "[[neural-episodic-control-with-state-abstraction]]"
  - "[[mogrifier-lstm-policy]]"
  - "[[closed-form-irs-phase-alignment]]"
  - "[[uav-mounted-ris]]"
  - "[[uav-trajectory-control]]"
  - "[[rotary-wing-propulsion-energy-model]]"
  - "[[ppo]]"
  - "[[jains-fairness-index]]"
  - "[[blockage-aware-channel-model]]"
  - "[[geng-sun]]"
  - "[[jiahui-li]]"
  - "[[jiacheng-wang]]"
  - "[[dusit-niyato]]"
created: 2026-07-13
updated: 2026-07-16
---

# Joint Optimization of UAV-Carried IRS for Urban Low Altitude mmWave Communications With Deep Reinforcement Learning

## Citation

Xie, W., Sun, G., Liu, B., Li, J., Wang, J., Du, H., Niyato, D., & Kim, D. I. (2026). *Joint Optimization of UAV-Carried IRS for Urban Low Altitude mmWave Communications With Deep Reinforcement Learning*. **IEEE Transactions on Mobile Computing**, 25(1), 1381-1397. DOI: 10.1109/TMC.2025.3600682.

> **Metadata grounding note.** The parse records an August 2025 early-access date but omits the journal name and final issue. The DOI record places the article in the January 2026 TMC issue; the wiki uses that final issue year.

## TL;DR

Controls a rotary-wing UAV carrying a passive IRS through enhanced PPO while computing IRS phases analytically from LoS geometry. Neural episodic control with state abstraction and a mogrifier LSTM augment PPO; the objective multiplies Jain fairness by aggregate rate and divides by propulsion energy.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A source user communicates with mobile terrestrial users through a rotary-wing UAV carrying a planar IRS in an obstructed urban mmWave environment, with blocked direct links and TDMA service.

**Problem & objective**: The joint design maximizes long-term fairness-weighted rate per propulsion energy, $\max_{\boldsymbol\Theta,\mathbf A}\sum_{t=1}^{T}F_t$ with $F_t=\xi\sum_iR_{i,t}/E_t$, by controlling IRS phases and UAV displacement.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV displacement | $\mathbf a_t=[a_t^x,a_t^y,a_t^z]$ | Continuous 3-D vector | Move the UAV-carried IRS in slot $t$ |
| Trajectory controls | $\mathbf A$ | Continuous sequence | Collect all slot displacements |
| IRS phase matrix | $\boldsymbol\Theta_t$ | Continuous unit-modulus diagonal matrix | Align reflected LoS components |
| Element phase | $\omega_{i,t}$ | Continuous, $[-\pi,\pi)$ | Phase of IRS element $i$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Per-slot travel is bounded, $0\leq d_t^{IRS}\leq D^{\max}$ |
| C2 | Horizontal position satisfies $X^{\min}\leq x_t^{IRS}\leq X^{\max}$ |
| C3 | Horizontal position satisfies $Y^{\min}\leq y_t^{IRS}\leq Y^{\max}$ |
| C4 | Altitude satisfies $Z^{\min}\leq z_t^{IRS}\leq Z^{\max}$ |
| C5 | Each IRS phase satisfies $-\pi\leq\omega_{i,t}<\pi$ |

**Algorithm**: EPPO augments clipped PPO with neural episodic control over abstracted states and a mogrifier LSTM actor, while a geometry-based phase-alignment rule removes the high-dimensional IRS vector from the learned action so the policy outputs only three-dimensional UAV motion.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Xie et al. [x] optimized a UAV-carried IRS for obstructed urban low-altitude mmWave communication by balancing aggregate rate, Jain fairness, and propulsion energy. The formal problem jointly controls UAV displacement and IRS phases under per-slot movement, horizontal-area, altitude, and phase-range constraints. EPPO combines proximal policy optimization with neural episodic state abstraction and a mogrifier LSTM, while a geometry-derived phase rule reduces the learned action to three UAV movement components. Simulation results report higher rewards and data rates with lower energy consumption than the evaluated PPO, TD3, DDPG, and SAC baselines, although the study provides no global-optimality guarantee.

## System model and objective

- One source user reaches mobile terrestrial users through a UAV-carried planar IRS; blocked direct links are treated as unavailable and users are served by TDMA.
- Source-IRS and IRS-user links use geometry-derived Rician channels. The UAV takes one 3-D displacement action per slot within horizontal, altitude, and speed bounds.
- The formal objective sums `fairness * aggregate rate / propulsion energy` over time. IRS control energy, source transmission energy, onboard computation, positioning, and backhaul-control energy are excluded.
- The learned action contains only three movement components. [[closed-form-irs-phase-alignment]] removes the IRS phase vector from the policy action.

## Method

EPPO uses clipped [[ppo]] with an old-policy actor, actor-critic updates, and a replay buffer. [[neural-episodic-control-with-state-abstraction]] discretizes the continuous state into a score table and supplies intrinsic reward, while [[mogrifier-lstm-policy]] repeatedly gates the actor's input and recurrent state before ordinary LSTM updates.

The closed-form phase rule aligns geometric LoS terms, reducing the action dimension from `M_r M_c + 3` to 3. The paper gives no proof that this phase choice is globally optimal for the full Rician, fairness-weighted, trajectory-coupled problem. EPPO is heuristic: no convergence, approximation, robust-constraint, or optimality theorem is provided, and the state abstraction requires up to `N^K` cells.

## Key findings

- Fig. 5(c) reports roughly **250 J** of cumulative energy consumption, near the stated 248.09 J forward-flight minimum at 9.8 m/s; the paper describes a 0.77% deviation but does not clarify the aggregation interval in the accompanying prose.
- The text following Table IV reports reward gains of **20.33%** over PPO, **205.42%** over TD3, and **28.16%** over DDPG, derived from plotted rewards rather than a statistical test.
- Table IV reports EPPO training/decision time of **1.575 h / 1.7 ms**, versus PPO 0.751 h / 1.3 ms, DDPG 1.004 h / 1.2 ms, TD3 1.528 h / 1.3 ms, and SAC 2.049 h / 1.5 ms.
- The ablation figures attribute a small gain to the mogrifier LSTM and a larger gain to closed-form phase control; exact endpoint values are not stated.

The main simulation uses 620 m square bounds, 80-120 m altitude, 300 one-second slots, 30 m maximum slot displacement, 15 W source power, 2 MHz bandwidth, and 3,000 training episodes.

## Limitations / interpretation

Evidence is simulation-only with no airborne experiment, timing platform, seed count, confidence intervals, or statistical tests. The main model assumes known geometry and CSI, continuous IRS phases, a reliable source-to-UAV control link, and excludes wind, discrete phases, no-fly zones, multi-UAV coordination, and control/IRS energy.

Several parse/model inconsistencies limit literal interpretation: a stated 3-by-3 urban grid does not fit the 620 m bounds under the listed cell/road sizes; the parsed SNR lacks an absolute square; path loss appears in dB inside channel multiplication; the reward expression does not transparently reproduce the all-user objective; and instantaneous Jain fairness is unclear under one-user-per-slot TDMA. The cited 248.09 J minimum is for forward flight, despite prose calling it hovering.

## Relation to the corpus

This source combines [[uav-mounted-ris]], [[uav-trajectory-control]], and [[rotary-wing-propulsion-energy-model]] while structurally reducing the DRL action with [[closed-form-irs-phase-alignment]]. Its episodic score table is distinct from replay-memory concepts elsewhere in the corpus, and its mogrifier recurrence is not the same mechanism as SoftPPO-LSTM.

## Raw artifacts

- Parse: `raw/sources/Joint_Optimization_of_UAV-Carried_IRS_for_Urban_Low_Altitude_mmWave_Communications_With_Deep_Reinforcement_Learning/Joint_Optimization_of_UAV-Carried_IRS_for_Urban_Low_Altitude_mmWave_Communications_With_Deep_Reinforcement_Learning.md`
- Origin PDF and extracted figures (`images/`) in the same folder.
