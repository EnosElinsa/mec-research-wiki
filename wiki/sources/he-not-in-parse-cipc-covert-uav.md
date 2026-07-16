---
type: source
title: "Channel Inversion Power Control-Aided Multi-User Secret and Covert UAV Communications"
authors: ["Yingqi He", "Jinpeng Xu", "Lin Zhou", "Jingjing Wang", "Chunxiao Jiang"]
year: ""
url: ""
venue: ""
modeling_card: required
tags: [source, covert-communication, physical-layer-security, noma, channel-inversion-power-control, uav-trajectory-control]
related:
  - "[[channel-inversion-power-control]]"
  - "[[covert-communication]]"
  - "[[physical-layer-security]]"
  - "[[noma]]"
  - "[[secrecy-outage-probability]]"
  - "[[csi-estimation-error]]"
  - "[[stochastic-geometry-network-analysis]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[uav-trajectory-control]]"
  - "[[jingjing-wang]]"
  - "[[chunxiao-jiang]]"
created: 2026-07-12
updated: 2026-07-16
---

# Channel Inversion Power Control-Aided Multi-User Secret and Covert UAV Communications

## Citation

He, Y., Xu, J., Zhou, L., Wang, J., & Jiang, C. *Channel Inversion Power Control-Aided Multi-User Secret and Covert UAV Communications*. Venue / year / DOI: **not in parse**.

## TL;DR

Combines confidential and covert uplink traffic in one UAV receiver. Bob's strong secret signal provides cover for weaker TDMA-scheduled covert users through power-domain NOMA, while truncated channel-inversion power control targets a stable received power at the UAV; the paper derives reliability, secrecy, covertness, and detection metrics and optimizes both rotary-wing and fixed-wing operation.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A secret ground user and multiple covert users transmit uplink to a UAV receiver while an adversary both eavesdrops and detects covert activity. The secret user's truncated channel-inversion signal acts as cover for a TDMA-selected covert user under power-domain NOMA and SIC.

**Problem & objective**: For rotary-wing operation, maximize average effective sum covert rate, $\max_{Q_c,I,H}\mathbb E\{\sum_kP_{cc}^kR_c^k\}$; for fixed-wing operation, maximize the minimum user-average effective covert rate over scheduling, powers, channel-inversion target, and flight variables.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Covert-user power | $Q_c$ or $Q_c^k[n]$ | continuous, bounded | Common rotary-wing power or slotwise fixed-wing power |
| CIPC target | $I$ | continuous, positive | Target received secret-signal power at the UAV |
| Hover altitude | $H$ | continuous, $[H_{\min},H_{\max}]$ | Rotary-wing deployment height |
| User scheduling | $\alpha_k[n]$ | binary | Covert user served in fixed-wing slot $n$ |
| Flight state | $\mathbf L_a[n],\mathbf v[n],\mathbf a[n]$ | continuous | Fixed-wing position, velocity, and acceleration |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Willie's minimum detection error probability satisfies the covertness target. |
| C2 | Bob's secret connection probability and secrecy outage probability meet reliability and secrecy targets. |
| C3 | Covert-user powers remain within their peak limits. |
| C4 | Rotary-wing altitude remains inside its prescribed interval. |
| C5 | Fixed-wing TDMA serves one user per slot and enforces a minimum average effective rate for every user. |
| C6 | Fixed-wing initial and final positions, speed range, acceleration limit, and motion recursion are satisfied. |

**Algorithm**: Derive closed-form connection, secrecy-outage, and detection-error expressions under CIPC. For hovering operation, combine theorem-based one-dimensional search with a lower-complexity coordinate-descent update for $Q_c$, $I$, and $H$; for fixed-wing operation, alternate relaxed scheduling, user power, trajectory-velocity-acceleration, and CIPC updates using SCA and convex interior-point subproblems.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

He et al. [x] combined multi-user covert uplink traffic with a secret user's channel-inversion-controlled signal as natural cover at a UAV receiver. They optimized rotary-wing covert power, CIPC target, and altitude for average effective sum covert rate, then extended the model to max-min fixed-wing scheduling, user powers, trajectory, velocity, and acceleration under covertness, connection, secrecy, power, fairness, and flight constraints. Closed-form performance measures support theorem-based and coordinate-descent hovering solutions, while alternating optimization and SCA handle the fixed-wing mixed decisions. Numerical results showed the coordinate-descent solution close to exhaustive optimization and the fixed-wing method above fixed-power and fixed-schedule baselines while preserving fair service.

## Problem

UAV physical-layer security often protects either message confidentiality or the existence of a transmission, serves only one or two security-sensitive users, or relies on artificial noise. This paper asks whether a useful secret signal can serve as natural cover for multiple covert users while satisfying reliability, secrecy, and covertness constraints.

## System model

- Bob is the secret user, `K` Carlos are covert users, Alice is the UAV receiver, and Willie is an adversary that both eavesdrops Bob and detects Carlo transmissions.
- TDMA selects one covert user, while power-domain NOMA superimposes that user's signal on Bob's secret signal for SIC decoding at Alice.
- Bob applies truncated channel-inversion power control to target received power `I` at Alice and remains silent when the required transmit power exceeds his budget.
- Rotary-wing operation maximizes average effective sum covert rate over common covert power, `I`, and hovering altitude. Fixed-wing operation maximizes the minimum average effective covert rate over scheduling, user powers, trajectory, velocity, acceleration, and `I`.

## Method

The paper derives closed-form secret connection probability, secrecy outage probability, covert connection probability, and detection error probability under Willie's noise uncertainty, then studies Alice-Bob channel-estimation uncertainty. A theorem-based optimal solution and coordinate-descent approximation handle the rotary-wing model. The fixed-wing solver alternates relaxed slot allocation, covert-user power allocation, trajectory/velocity/acceleration optimization, and CIPC-parameter optimization using SCA and interior-point convex subproblems.

## Key findings

- Main settings include Bob maximum power 40 dBm, covert-user maximum power 0 dBm, Bob target and secret rates 12 and 10 bps, covert target rate 4 bps, Alice/Willie average noise powers -90 dBm, and Willie noise-uncertainty parameter 2. The page preserves the parse's `bps` units.
- Higher covert-user density or covert power lowers Bob's secret connection probability through interference. More secret-rate redundancy lowers secrecy outage probability, while stronger secret power or weaker covert power improves Willie's SNR and raises secrecy outage.
- Detection error probability is U-shaped in Willie's threshold, and lower covert transmit power improves covertness. Higher Alice-Bob channel uncertainty can raise connection probabilities through CIPC overcompensation but also strengthens Willie's received signal and worsens secrecy/covertness.
- The coordinate-descent rotary-wing result stays close to the optimal result in the reported comparisons, especially at low covert-user density.
- In the fixed-wing case, the proposed AO solver converges rapidly; a 90 s flight period outperforms 75 s and AO exceeds fixed-power and fixed-trajectory baselines. The greedy closest-user baseline is described as marginally higher-throughput but unfair, whereas AO balances throughput across users.
- The fixed-wing setup uses speeds 1-20 m/s, maximum acceleration 2 m/s squared, three covert users, one Bob, and one Willie over the stated 75 s and 90 s periods.

## Limitations / parse caveats

The evidence is closed-form analysis and numerical simulation, not hardware validation. The main model assumes single antennas, legitimate-user perfect CSI, and Alice's knowledge of Willie's position; Willie's detector also assumes a sufficiently long observation sequence. The uncertainty analysis is not carried through all later optimization expressions. Several equations are corrupted and the parse contains Xplore watermark text, so formulas are not transcribed verbatim. No exact fixed-wing percentage improvement is stated in stable prose.

## Relation to the corpus

This source links [[physical-layer-security]] and [[covert-communication]] through [[channel-inversion-power-control]]. Unlike public-cover traffic in [[hosseini-2026-aoi-covert-uav]], Bob's confidential signal is itself the cover signal for multiple covert users; the stochastic-geometry rotary-wing model and AO/SCA fixed-wing model provide complementary analytical and trajectory-control views.

## Raw artifacts

- Parse: `raw/sources/Channel_Inversion_Power_Control-Aided_Multi-User_Secret_and_Covert_UAV_Communications/Channel_Inversion_Power_Control-Aided_Multi-User_Secret_and_Covert_UAV_Communications.md`
- Origin PDF: `raw/sources/Channel_Inversion_Power_Control-Aided_Multi-User_Secret_and_Covert_UAV_Communications/Channel_Inversion_Power_Control-Aided_Multi-User_Secret_and_Covert_UAV_Communications.pdf`
- Figures: `raw/sources/Channel_Inversion_Power_Control-Aided_Multi-User_Secret_and_Covert_UAV_Communications/images/`
