---
type: source
modeling_card: required
title: "Minimum Secrecy Rate Maximization for UAV-Mounted Movable Antenna Empowered Wireless Networks"
authors: ["Liangsen Zhai", "Xiapu Luo"]
year: 2026
url: "https://doi.org/10.1109/TWC.2026.3651300"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), vol. 25, pp. 10405-10418"
tags: [source, movable-antenna, physical-layer-security, trajectory-optimization, robust-optimization, beamforming]
related:
  - "[[movable-antenna]]"
  - "[[physical-layer-security]]"
  - "[[micro-macro-mobility-security]]"
  - "[[uav-trajectory-control]]"
  - "[[air-to-ground-channel-model]]"
  - "[[alternating-optimization-sdr-sca]]"
created: 2026-07-13
updated: 2026-11-03
---

# Minimum Secrecy Rate Maximization for UAV-Mounted Movable Antenna Empowered Wireless Networks

## Citation

Zhai, L., & Luo, X. (2026). *Minimum Secrecy Rate Maximization for UAV-Mounted Movable Antenna Empowered Wireless Networks*. **IEEE Transactions on Wireless Communications, 25**, 10405-10418. DOI: 10.1109/TWC.2026.3651300.

## TL;DR

Jointly optimizes user scheduling, UAV trajectory, transmit beamforming, and one-dimensional onboard [[movable-antenna]] positions to maximize the worst user's average secrecy rate under bounded eavesdropper-location uncertainty.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A UAV at fixed height $H$ carries $M$ movable antennas (MAs) on a one-dimensional linear region of length $D$ and serves $K$ single-antenna ground users, at most one per slot, over LoS channels. $L$ eavesdroppers are known only to lie inside circular uncertainty regions, so their angles carry errors.

**Problem & objective**: Problem (10) maximizes the minimum average secrecy rate $\max_{\mathbf A,\mathbf X,\mathbf W,\mathbf Q}\min_{k}\frac1N\sum_nR_{u_k}^{\mathrm{sec}}[n]$, where $R_{u_k}^{\mathrm{sec}}[n]$ in (9) subtracts the largest eavesdropping rate over all eavesdroppers and all positions in their regions.

**Decision variables**:
| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| User scheduling | $\mathbf A=\{\alpha_k[n]\}$ | binary | User $k$ served in slot $n$ |
| MA positions | $\mathbf X=\{x_m[n]\}$ | continuous, $[0,D]$ | Position of antenna $m$ on the linear region |
| Transmit beamforming | $\mathbf W=\{\mathbf w_k[n]\}$ | complex vectors | UAV beam for the scheduled user |
| UAV trajectory | $\mathbf Q=\{\mathbf q[n]\}$ | continuous, fixed height | Horizontal UAV position per slot |

**Constraints**:
| ID | Meaning and key expression |
|---|---|
| (10b) | $\sum_k\lVert\mathbf w_k[n]\rVert^2\le P_{\max}$ |
| (1), (2) | $x_m[n]\in[0,D]$ and spacing $x_m[n]-x_{\bar m}[n]\ge D_{\min}$ for $m>\bar m$ |
| (3), (4) | $\mathbf q[1]=\mathbf q_I$, $\mathbf q[N]=\mathbf q_F$, and $\lVert\mathbf q[n+1]-\mathbf q[n]\rVert\le v_{\max}\tau$ |
| (6), (7) | $\sum_k\alpha_k[n]\le1$ and $\alpha_k[n]\in\{0,1\}$ |
| Model rule | Secrecy is evaluated for the worst eavesdropper position within each uncertainty region |

**Algorithm**: Triangle-inequality bounds give the worst-case eavesdropper path loss, and a representative steering direction approximates the angular uncertainty. BCD then alternates four blocks: relaxed scheduling $0\le\alpha_k[n]\le1$ solved as a convex problem, SCA for the beamforming, SCA for the trajectory, and lower bounds on the antenna-position terms for the MA positions. The algorithm converged in about 15 iterations in simulation.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zhai and Luo [x] studied minimum secrecy-rate maximization in UAV-mounted movable-antenna wireless networks with uncertain eavesdropper locations. They jointly optimized user scheduling, transmit beamforming, the UAV trajectory, and onboard antenna positions under power, mobility, movement-region, spacing, and robust secrecy constraints. Triangle inequalities bound worst-case path loss and a representative steering direction approximates angular uncertainty. A four-block BCD method alternates relaxed scheduling, SCA beamforming, SCA trajectory control, and second-order antenna-position updates. Simulations report a higher minimum secrecy rate than fixed user scheduling, fixed beamforming, a fixed circular trajectory, and fixed-position antennas, across user numbers, power, flight time, antenna number, and movable range; the secrecy rate saturated as the movable range grew.

## Problem and system model

A fixed-altitude UAV with multiple movable elements serves single-antenna ground users while ground eavesdroppers occupy known circular uncertainty regions. At most one user is scheduled per slot. The LoS/free-space model imposes UAV speed/endpoints, transmit power, antenna travel, and minimum element-spacing constraints.

The secrecy objective subtracts the maximum feasible eavesdropping rate from the scheduled user rate. This couples macro-scale flight with wavelength-scale array motion and creates a non-smooth, non-concave problem with infinitely many candidate eavesdropper positions.

## Method

Triangle inequality bounds the worst-case path loss, while the steering vector is approximated at the corresponding point. A four-block BCD loop then alternates relaxed scheduling, SCA beamforming, SCA trajectory updates, and second-order antenna-position bounds, solving the convexified subproblems with CVX. The objective sequence is non-decreasing and bounded, which supports convergence of values to a local/suboptimal solution rather than global optimality.

## Key findings

- The abstract reports that at 3.5 bit/s/Hz the proposed scheme supports approximately 20% more users than fixed-position antennas and reduces transmit power and antenna count by more than 40%.
- The displayed algorithm converges in about 15 iterations in the tested settings; increasing location uncertainty or eavesdropper count reduces secrecy rate.
- Movable elements outperform equal-count fixed elements, while larger movement regions improve performance and then saturate in the plotted scenario.

## Limitations

Results are numerical simulations. The model assumes fixed altitude, static ground nodes, LoS free-space channels, and bounded location regions. Robustness is approximate because angular variation inside each region is replaced by one steering direction. Scheduling is relaxed and may require sub-slot rounding. A printed angular-error interval is degenerate, and several parsed equation labels are damaged.

## Relation to the corpus

Where [[li-not-in-parse-movable-antenna-pls]] compares local antenna movement against whole-UAV movement, this source jointly uses both through [[micro-macro-mobility-security]]. It adds scheduling and bounded eavesdropper-location uncertainty to the same [[physical-layer-security]] design space.

## Raw artifacts

- `raw/sources/Minimum_Secrecy_Rate_Maximization_for_UAV-Mounted_Movable_Antenna_Empowered_Wireless_Networks/Minimum_Secrecy_Rate_Maximization_for_UAV-Mounted_Movable_Antenna_Empowered_Wireless_Networks.md`
- Original PDF and extracted figures (`images/`) are in the same folder.
