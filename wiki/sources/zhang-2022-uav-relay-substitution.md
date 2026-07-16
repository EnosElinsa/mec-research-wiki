---
type: source
title: "Cooperative UAV Enabled Relaying Systems: Joint Trajectory and Transmit Power Optimization"
authors: ["Guangchi Zhang", "Xiaoqi Ou", "Miao Cui", "Qingqing Wu", "Shaodan Ma", "Wei Chen"]
year: 2022
url: "https://doi.org/10.1109/TGCN.2021.3108147"
venue: "IEEE Transactions on Green Communications and Networking (IEEE TGCN)"
tags: [source, uav, relaying, substitution, trajectory-optimization, power-control, sca]
related:
  - "[[qingqing-wu]]"
  - "[[uav-substitution-relaying]]"
  - "[[uav-mobile-relaying]]"
  - "[[information-causality-constraint]]"
  - "[[uav-trajectory-control]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[zeng-2016-throughput-relaying]]"
  - "[[angle-of-radiation-uav-relay]]"
created: 2026-07-12
updated: 2026-07-16
modeling_card: required
---

# Cooperative UAV Enabled Relaying Systems: Joint Trajectory and Transmit Power Optimization

## Citation

Zhang, G., Ou, X., Cui, M., Wu, Q., Ma, S., & Chen, W. (2022). *Cooperative UAV Enabled Relaying Systems: Joint Trajectory and Transmit Power Optimization*. **IEEE Transactions on Green Communications and Networking**, 6(1), 543-557. DOI: 10.1109/TGCN.2021.3108147.

## TL;DR

Extends a blocked ground source-destination relay connection beyond one UAV's flight duration by rotating multiple half-duplex decode-and-forward UAVs through service. HUS relays one UAV at a time; SEUS overlaps one UAV's forwarding phase with the next UAV's reception and jointly controls trajectories and powers to manage interference.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A blocked ground source-destination link is served by multiple half-duplex decode-and-forward UAV relays whose individual flight durations are shorter than the required communication period. HUS assigns nonoverlapping relay periods, while SEUS overlaps one relay's forwarding phase with the next relay's reception; air links use free-space LoS path loss with AWGN, and SEUS includes inter-relay interference.

**Problem & objective**: Nonconvex HUS problem (21) and SEUS problem (22) maximize average end-to-end throughput, for example $\max M^{-1}\sum_{m=1}^{M}\mu_m$ in SEUS, where each $\mu_m$ is bounded by both source-to-relay and relay-to-destination average rates.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV trajectories | $\mathbf q_m[n]$ | continuous, three-dimensional | Slotwise positions of relay UAV $m$ |
| Source power | $P_s[n]$ | continuous, bounded | Source transmit power in slot $n$ |
| Relay power | $P_m[n]$ | continuous, bounded | Transmit power of UAV relay $m$ |
| Hop-throughput slack | $\eta_m$ or $\mu_m$ | continuous, nonnegative | End-to-end rate limited by the weaker DF hop in HUS or SEUS |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| 1 | Relay altitude satisfies $H_{\min}\leq z_m[n]\leq H_{\max}$ |
| 2/15 | Every relay follows prescribed endpoints and per-slot speed bound $\|\mathbf q_m[n+1]-\mathbf q_m[n]\|\leq V$ |
| 4-5/13-14 | Source and relay powers obey average and peak limits in their active periods |
| 16 | Overlapping SEUS relays maintain $\|\mathbf q_m[n]-\mathbf q_{m-1}[n]\|\geq d_{\min}$ |
| 21b-c/22b-c | Each throughput slack is no larger than either DF hop's average rate |

**Algorithm**: Solve HUS as independent single-relay trajectory and power subproblems. For SEUS, use block coordinate ascent: optimize source and relay powers for fixed trajectories, update all trajectories for fixed powers through slack-variable reformulation and successive convex approximation, and repeat until the nondecreasing throughput objective converges.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zhang et al. [x] studied cooperative UAV relaying when the required source-destination communication duration exceeds one UAV's flight duration. They proposed heuristic UAV substitution, which activates one half-duplex decode-and-forward relay at a time, and spectral-efficient UAV substitution, which overlaps consecutive relays' reception and forwarding periods. For both schemes, they formulated joint three-dimensional trajectory and transmit-power designs that maximize average end-to-end throughput under mobility, altitude, power, and decode-and-forward hop constraints. The SEUS problem is solved by block coordinate ascent with successive convex approximation for the coupled power and trajectory blocks. Simulations report that SEUS with joint trajectory and power control attains the highest throughput among the evaluated schemes and becomes preferable to a single optimized UAV when the required duration exceeds 360 seconds in the reported setting.

## Problem

Single-UAV relaying and simultaneous multi-UAV operation constrain service duration to one vehicle's flight endurance. Long streams may need a longer connection. Temporal relay substitution extends the service horizon, but spectral efficiency and relay-to-relay interference depend on how successive UAVs move and allocate transmit power.

## System model

- A blocked ground source-destination link is served by `M` half-duplex decode-and-forward UAV relays.
- HUS assigns each relay a receive half-period followed by a forward half-period and yields total service duration `M T_f`.
- SEUS overlaps adjacent relay periods so one UAV forwards while the next receives; total service duration is `(M+1)T_f/2`.
- Three-dimensional trajectories obey endpoints, altitude, speed, and separation constraints. Source and relay powers obey average and peak limits.
- LoS inverse-square air-ground channels and AWGN are assumed; SEUS additionally models interference from the forwarding relay to the receiving relay.

## Method

Each HUS period reduces to the single-relay trajectory/power problem used by [[zeng-2016-throughput-relaying]]. For SEUS, block coordinate ascent alternates power control and UAV trajectories. SCA linearizes interference/rate terms, slack variables convexify distance constraints, and CVX solves each subproblem. The paper establishes a non-decreasing, upper-bounded objective sequence and presents the result as a convergent suboptimal design; it does not prove stationarity or global optimality.

## Key findings

- The main simulation uses three relays, 100-500 m altitude bounds, 20 m/s maximum speed, 10 m minimum separation, and average power 5 dBm in the central comparisons.
- With joint trajectory/power control, SEUS has the best reported throughput and static relays the worst; exact rate ordinates are only in figures.
- A single optimized UAV is favored for required durations below 360 s, while optimized SEUS is favored above 360 s in the Fig. 12 prose.
- Power control improves throughput over fixed power at average power up to 10 dBm; above 10 dBm the compared results are described as similar.
- At `T_f=60 s`, SEUS coordinates source and relay powers over overlapping 30 s receive/forward intervals; the source stops sending to UAV 2 at about 50 s in the figure discussion.

## Limitations / parse caveats

Evaluation is simulation-only with deterministic LoS channels, a blocked direct link, half-duplex DF relays, and flight duration supplied exogenously rather than derived from propulsion energy. The algorithms are local and parameter-fixed. Several equations and plot labels are OCR-damaged, and exact throughput gains are not transcribed. The parse records online publication on August 27, 2021 and a February 16, 2022 current version; the final 2022 issue metadata was verified through the DOI's Crossref record.

## Relation to the corpus

[[uav-substitution-relaying]] extends [[uav-mobile-relaying]] from one optimized mobile relay to a rotating service schedule. It retains the trajectory-power coupling of [[zeng-2016-throughput-relaying]] while adding endurance extension and, under SEUS, inter-relay interference control.

## Raw artifacts

- Parse: `raw/sources/Cooperative_UAV_Enabled_Relaying_Systems_Joint_Trajectory_and_Transmit_Power_Optimization/Cooperative_UAV_Enabled_Relaying_Systems_Joint_Trajectory_and_Transmit_Power_Optimization.md`
- Origin PDF: `raw/sources/Cooperative_UAV_Enabled_Relaying_Systems_Joint_Trajectory_and_Transmit_Power_Optimization/Cooperative_UAV_Enabled_Relaying_Systems_Joint_Trajectory_and_Transmit_Power_Optimization.pdf`
- Figures: `raw/sources/Cooperative_UAV_Enabled_Relaying_Systems_Joint_Trajectory_and_Transmit_Power_Optimization/images/`
