---
type: source
title: "Secrecy Sum Rate Maximization in UAV-IRS Assisted Networks With Credit-Aware Cooperative Multi-Agent Reinforcement Learning"
authors: ["Xulong Li", "Jiahao Huo", "Wei Huangfu", "Keping Long", "Haijun Zhang"]
year: 2026
url: "https://doi.org/10.1109/TWC.2025.3602188"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), vol. 25, pp. 3186-3197"
tags: [source, uav-mounted-ris, physical-layer-security, multi-agent-reinforcement-learning, shapley-value, primal-dual-optimization, trajectory-optimization, phase-shift-design]
related:
  - "[[shapley-value-marl-credit-assignment]]"
  - "[[primal-dual-constrained-marl]]"
  - "[[uav-mounted-ris]]"
  - "[[physical-layer-security]]"
  - "[[masac]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[uav-trajectory-control]]"
  - "[[xulong-li]]"
  - "[[wei-huangfu]]"
  - "[[jiahao-huo]]"
  - "[[haijun-zhang]]"
  - "[[qin-2023-symmetry-augmented-uav-isac]]"
  - "[[xie-2026-uav-irs-eppo]]"
created: 2026-07-14
updated: 2026-07-14
---

# Secrecy Sum Rate Maximization in UAV-IRS Assisted Networks With Credit-Aware Cooperative Multi-Agent Reinforcement Learning

## Citation

Li, X., Huo, J., Huangfu, W., Long, K., & Zhang, H. (2026). *Secrecy Sum Rate Maximization in UAV-IRS Assisted Networks With Credit-Aware Cooperative Multi-Agent Reinforcement Learning*. **IEEE Transactions on Wireless Communications, 25**, 3186-3197. DOI: 10.1109/TWC.2025.3602188.

## TL;DR

Controls multiple UAV-mounted IRSs under decentralized execution to maximize downlink secrecy sum rate. Exact Shapley values turn coalition contributions into agent-specific rewards, while a primal-dual constraint discourages the competition introduced by individual credit; the resulting PD-CMASAC jointly learns 3-D UAV motion and continuous IRS phases but retains factorial credit-computation cost during training.

## Problem

A multi-UAV-IRS system must strengthen blocked BS-user links while suppressing mobile eavesdroppers. Because every reflected signal contributes to the shared secrecy outcome, a common team reward gives weak agent-level learning signals. Assigning each UAV an individual contribution reward improves exploration but can also make agents compete, so the paper treats credit assignment and cooperation control as coupled learning problems.

## System model

- A `K`-antenna BS serves `M` single-antenna users in the presence of `E` single-antenna eavesdroppers. Each of `N` UAVs carries an `L`-element IRS, and decisions span `T` equal slots.
- The direct BS-user link is blocked. Signals reflected by all UAV-IRSs superpose at every user and eavesdropper; all modeled aerial reflection links use distance-dependent Rician fading.
- Users and eavesdroppers move in the target area under the simulated mobility process. The main observation model uses perfect BS/UAV-IRS and user/UAV-IRS CSI but bounded-error, outdated eavesdropper-link estimates.
- The BS uses fixed zero-forcing precoding and equal user power `P_max/M`. IRS amplitudes are fixed to one, leaving continuous phase shifts and UAV motion as decisions.
- Per-user secrecy is the legitimate rate minus the maximum rate available to any eavesdropper, clipped at zero. The objective maximizes cumulative secrecy sum rate over trajectories and phase-shift matrices.
- Constraints bound horizontal position, altitude, per-slot displacement, and phase, and impose a minimum per-slot secrecy rate for every user. The formulation does not include collision avoidance, propulsion energy, battery limits, terminal positions, or return-to-base requirements.

## Method

The paper maps one UAV-IRS to each agent in a Markov game and uses [[centralized-training-decentralized-execution]]. A local observation contains the UAV's own position and incident channel information; its action contains a 3-D displacement and all IRS phases. The shared reward is secrecy sum rate minus minimum-rate violation penalties.

[[shapley-value-marl-credit-assignment]] evaluates every UAV coalition and assigns each agent its exact marginal contribution. The resulting individual rewards satisfy the Shapley efficiency property: they sum to the grand-coalition value. To counter the competition induced by individual rewards, a binary cost identifies non-cooperative behavior, and a decreasing allowance progressively tightens a cooperation constraint.

The resulting PD-CMASAC extends MASAC with twin reward critics, twin constraint critics, stochastic policies, target networks, adaptive entropy temperatures, and per-agent Lagrange multipliers. [[primal-dual-constrained-marl]] updates policies against both the Shapley reward and learned cost constraint. Coalition evaluation and network updates occur at a training data center, which the paper places at the BS or a UAV-IRS; distributed execution uses only local observations and trained policies.

Exact coalition credit is the main scalability cost. The paper states `O((M+N)N!)` for credit calculation and a total training complexity containing the same factorial term. The learned policies avoid that term at execution time.

## Key findings

- The default simulation uses a `1 km x 1 km` area, 20 users, two eavesdroppers, three UAV-IRSs, 15 IRS elements per UAV, and a BS antenna count equal to the number of users. UAV altitude is constrained to `50-120 m`, BS power is `40 dBm`, and training runs for 8,000 episodes.
- **Figure-read approximate:** the cumulative sum secure rate converges near `395-400 bit/s/Hz` for PD-CMASAC, versus about `310` for MASAC-IR, `295-300` for MASAC-RS, and `235-240` for MASAC-TR. These are visual readings, not prose-stated values and should not be conflated with the penalized learning reward.
- **Figure-read approximate:** as the number of UAVs increases from 1 to 9, PD-CMASAC secrecy rate rises from about `9` to `28.9 bit/s/Hz`; all MASAC variants coincide near `9 bit/s/Hz` for one UAV, where multi-agent credit and cooperation distinctions disappear.
- **Figure-read approximate:** increasing IRS elements from 5 to 45 raises PD-CMASAC secrecy rate from about `15.4` to `25.6 bit/s/Hz`, while increasing users from 5 to 25 lowers it from about `30.2` to `19.6 bit/s/Hz`.
- A fairness-objective experiment adds weighted Jain fairness. **Figure-read approximate:** PD-CMASAC ends near `13.5 bit/s/Hz` and fairness `0.74`. These rates are not directly comparable with the main cumulative-reward curve because the objective changes.
- **Figure-read approximate:** under the paper's imperfect-CSI experiment, PD-CMASAC falls from about `400` to `340 bit/s/Hz` but remains highest among the plotted methods. The tested bounded-error radii are not exposed in the parsed parameter table.

## Limitations

The study is simulation-only and optimizes UAV and IRS decisions while holding BS beamforming and power allocation fixed. Exact Shapley enumeration scales factorially, yet the largest reported UAV-count experiment uses nine agents and provides no wall-clock training cost. The model assumes ideal continuous unit-amplitude IRS coefficients, omits flight energy and collision safety, and obtains local learned policies rather than a global optimum.

The main experiments assume perfect legitimate-link CSI; an imperfect-CSI sensitivity plot does not report its estimation-error radii in the parse and is not a worst-case robust-optimization guarantee. Several formulas are damaged or internally inconsistent: the displayed constraint labels are shifted, Eq. (32) appears to update a multiplier from the policy symbol rather than its previous multiplier, and the constraint-critic prose asks for a smaller target while Eq. (40) uses `max`. These points should not be silently repaired from context.

## Relation to the corpus

This source extends [[uav-mounted-ris]] and [[physical-layer-security]] with explicit multi-agent credit assignment. [[qin-2023-symmetry-augmented-uav-isac]] shares the Xulong Li, Wei Huangfu, and [[haijun-zhang]] research cluster and a MASAC/CTDE control pattern, but targets UAV-ISAC rather than secrecy through aerial IRSs. [[xie-2026-uav-irs-eppo]] and [[pan-2025-uav-ris-energy-efficient-comm]] are closer on UAV-carried IRS trajectory control, while this paper's distinct contribution is the combination of exact Shapley rewards and a primal-dual cooperation constraint.

## Raw artifacts

- Parse: `raw/sources/Secrecy_Sum_Rate_Maximization_in_UAV-IRS_Assisted_Networks_With_Credit-Aware_Cooperative_Multi-Agent_Reinforcement_Learning/Secrecy_Sum_Rate_Maximization_in_UAV-IRS_Assisted_Networks_With_Credit-Aware_Cooperative_Multi-Agent_Reinforcement_Learning.md`
- Origin PDF: `raw/sources/Secrecy_Sum_Rate_Maximization_in_UAV-IRS_Assisted_Networks_With_Credit-Aware_Cooperative_Multi-Agent_Reinforcement_Learning/Secrecy_Sum_Rate_Maximization_in_UAV-IRS_Assisted_Networks_With_Credit-Aware_Cooperative_Multi-Agent_Reinforcement_Learning.pdf`
- Figures: `raw/sources/Secrecy_Sum_Rate_Maximization_in_UAV-IRS_Assisted_Networks_With_Credit-Aware_Cooperative_Multi-Agent_Reinforcement_Learning/images/`

## Metadata notes

The paper was published online on 2 September 2025 and lists a current-version date of 22 December 2025, but the journal header assigns it to volume 25 (2026), pages 3186-3197; the citation therefore uses 2026.
