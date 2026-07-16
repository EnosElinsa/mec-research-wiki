---
type: source
title: "Optimization-Driven DRL for Resource Allocation Under Licensed and Unlicensed UAV Spectrum Sharing Networks Against Uncertain Jamming"
authors: ["Rui Ding", "Fuhui Zhou", "Qihui Wu", "Kai-Kit Wong", "Naofal Al-Dhahir"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3673261"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), vol. 25, no. 8, pp. 13382-13398"
modeling_card: required
tags: [source, spectrum-sharing, anti-jamming, optimization-driven-drl, robust-optimization, hybrid-action, uav-trajectory]
related:
  - "[[optimization-driven-drl]]"
  - "[[licensed-unlicensed-spectrum-sharing]]"
  - "[[csi-estimation-error]]"
  - "[[hybrid-action-decision-making]]"
  - "[[deep-q-network]]"
  - "[[ddpg]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[uav-trajectory-control]]"
  - "[[multi-domain-uav-anti-jamming]]"
  - "[[fuhui-zhou]]"
  - "[[qihui-wu]]"
  - "[[kai-kit-wong]]"
  - "[[naofal-al-dhahir]]"
created: 2026-07-13
updated: 2026-07-16
---

# Optimization-Driven DRL for Resource Allocation Under Licensed and Unlicensed UAV Spectrum Sharing Networks Against Uncertain Jamming

## Citation

Ding, R., Zhou, F., Wu, Q., Wong, K.-K., & Al-Dhahir, N. (2026). *Optimization-Driven DRL for Resource Allocation Under Licensed and Unlicensed UAV Spectrum Sharing Networks Against Uncertain Jamming*. **IEEE Transactions on Mobile Computing, 25**(8), 13382-13398. DOI: 10.1109/TMC.2026.3673261.

## TL;DR

Combines robust SCA/CVX solutions with DQN-DDPG targets to learn licensed/unlicensed subchannel allocation, powers, and UAV trajectory under norm-bounded jammer-CSI uncertainty.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A cognitive UAV serves secondary users over licensed cellular and unlicensed Wi-Fi subchannels while protecting primary and Wi-Fi users from interference. A multi-antenna jammer attacks the secondary links, and jammer-to-user CSI lies in a norm-bounded uncertainty set.

**Problem & objective**: The robust joint design maximizes time-average secondary sum rate, $\max_{\mathcal A,\mathcal B,\mathcal P,\mathcal U,\mathcal Q}\frac{1}{N}\sum_{n=1}^{N}\sum_{k=1}^{K}R_k[n]$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Licensed allocation | $\rho_{k,j}^{\mathrm{lic}}[n]$ | binary, $\{0,1\}$ | Whether secondary user $k$ uses licensed subchannel $j$ in slot $n$ |
| Unlicensed allocation | $\rho_{k,m}^{\mathrm{unlic}}[n]$ | binary, $\{0,1\}$ | Whether secondary user $k$ uses unlicensed subchannel $m$ in slot $n$ |
| Licensed power | $p_{k,j}^{\mathrm{lic}}[n]$ | continuous, nonnegative | UAV power assigned on licensed subchannel $j$ |
| Unlicensed power | $p_{k,m}^{\mathrm{unlic}}[n]$ | continuous, nonnegative | UAV power assigned on unlicensed subchannel $m$ |
| UAV position | $\mathbf q[n]$ | continuous, $\mathbb R^2$ | Horizontal UAV waypoint in slot $n$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Every secondary user meets its robust average-rate target for all jammer channels in the uncertainty set |
| C2-C3 | Average leakage to each primary and Wi-Fi user stays below the licensed or unlicensed tolerance |
| C4-C8 | Licensed and unlicensed assignments are binary and satisfy one-user and one-subchannel exclusivity rules |
| C9-C10 | Total licensed and unlicensed transmit powers stay below their respective peak budgets |
| C11 | Consecutive UAV positions obey the flight-speed limit, $\lVert\mathbf q[n]-\mathbf q[n-1]\rVert\leq V_{\max}\delta_t$ |

**Algorithm**: The model-based module alternates robust resource and trajectory blocks, using the S-procedure and successive convex approximation to generate offline lower-bound actions and returns. During learning, DQN selects discrete subchannels and DDPG selects continuous powers and motion; a gate substitutes the optimization-informed target when it exceeds the ordinary DRL target, while deployment uses only neural inference.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Ding et al. [x] considered a cognitive UAV that shares licensed cellular and unlicensed Wi-Fi spectrum with incumbent users while facing norm-bounded jammer-channel uncertainty. They maximized robust secondary sum rate over binary subchannel assignments, transmit powers, and UAV trajectory under rate, interference-leakage, assignment, power, and mobility constraints. Their optimization-driven DRL framework uses S-procedure and SCA solutions as gated offline targets for a DQN discrete policy and DDPG continuous policy. The reported learning curve converges about 200 episodes earlier than conventional DQN-DDPG, and joint licensed and unlicensed access achieves approximately twice the sum rate of the licensed-only baseline.

## Problem and system model

A cognitive UAV serves secondary users while sharing licensed cellular subchannels with primary users and unlicensed Wi-Fi subchannels with Wi-Fi users. A multi-antenna jammer attacks the secondary links. The objective maximizes average secondary sum rate under minimum-rate, interference-leakage, assignment, power, and UAV-speed constraints.

Jam-to-user CSI follows a norm-bounded error model. [[licensed-unlicensed-spectrum-sharing]] expands capacity but exposes open unlicensed channels and must protect both incumbent systems.

## Method

The model-based module alternates resource allocation and trajectory blocks. S-procedure transformations handle semi-infinite jammer uncertainty, while relaxations and successive convex approximations produce a robust lower-bound solution.

The learning module uses DQN for discrete licensed/unlicensed assignment and DDPG for continuous power and trajectory. [[optimization-driven-drl]] computes offline robust actions and return targets; a gate replaces the ordinary DRL target/action when the optimization target is larger. Runtime-critical inference remains neural, while the SCA/CVX targets are generated offline.

## Key findings

- The reported reward curve converges about 200 episodes earlier than conventional DQN-DDPG in one setting.
- Additional unlicensed spectrum yields approximately twice the sum rate of the licensed-only LTE-A baseline in the reported simulations.
- The proposed method remains strongest as Wi-Fi-user count, UAV power, jammer power, interference tolerance, and flight duration vary.
- Average DQN-DDPG training time is 1.84 s per episode versus 304.8 s for one optimization-module episode; offline target generation is excluded from online inference.
- Learning rates above roughly `7e-4` destabilize smaller replay configurations in the displayed sweep.

## Limitations

Evaluation is simulation-only, with distance-dependent LoS channels and no field or hardware validation. The robust optimizer supplies a local lower-bound solution rather than a global optimum. Optimization targets are expensive and precomputed offline; the paper does not quantify target-dataset generation cost at scale. Hybrid DQN/DDPG actions use reward penalties rather than guaranteeing all constraints during learning, and several equations are parse-damaged.

## Relation to the corpus

This source links [[multi-domain-uav-anti-jamming]] with hybrid action control. Unlike pure model-free anti-jamming policies, it injects a robust optimization target into replay-based learning; unlike online SCA, deployment executes only the learned networks.

## Raw artifacts

- Parse: `raw/sources/Optimization-Driven_DRL_for_Resource_Allocation_Under_Licensed_and_Unlicensed_UAV_Spectrum_Sharing_Networks_Against_Uncertain_Jamming/Optimization-Driven_DRL_for_Resource_Allocation_Under_Licensed_and_Unlicensed_UAV_Spectrum_Sharing_Networks_Against_Uncertain_Jamming.md`
- Origin PDF and extracted figures (`images/`) are in the same folder.
