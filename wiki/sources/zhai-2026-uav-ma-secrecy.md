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
updated: 2026-07-16
---

# Minimum Secrecy Rate Maximization for UAV-Mounted Movable Antenna Empowered Wireless Networks

## Citation

Zhai, L., & Luo, X. (2026). *Minimum Secrecy Rate Maximization for UAV-Mounted Movable Antenna Empowered Wireless Networks*. **IEEE Transactions on Wireless Communications, 25**, 10405-10418. DOI: 10.1109/TWC.2026.3651300.

## TL;DR

Jointly optimizes user scheduling, UAV trajectory, transmit beamforming, and one-dimensional onboard [[movable-antenna]] positions to maximize the worst user's average secrecy rate under bounded eavesdropper-location uncertainty.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: One fixed-altitude UAV with multiple one-dimensional movable antenna elements serves single-antenna ground users, at most one per slot, while eavesdroppers lie in bounded circular uncertainty regions. LoS channels couple whole-UAV motion and wavelength-scale array movement.

**Problem & objective**: A robust non-smooth problem maximizes the worst user's average secrecy rate, $\max \min_k\bar R_k^{\mathrm{sec}}$, over scheduling, beamforming, UAV trajectory, and antenna positions.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| User schedule | $s_k[n]$ | binary | User served in slot $n$ |
| Transmit beamformer | $\mathbf w[n]$ | complex continuous vector | UAV downlink beam |
| UAV trajectory | $\mathbf q[n]$ | continuous horizontal position | Macro-scale flight path |
| Antenna positions | $r_m[n]$ | continuous 1-D coordinates | Micro-scale element locations |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | At most one user is scheduled in each slot |
| C2 | Transmit beam power stays within the UAV budget |
| C3 | UAV trajectory satisfies endpoints and per-slot speed |
| C4 | Each movable element stays inside its travel region |
| C5 | Element spacing exceeds the minimum and secrecy is robust to every eavesdropper region |

**Algorithm**: Bound worst-case path loss by triangle inequality and approximate the corresponding steering direction → relax scheduling and update it convexly → update beamforming by SCA → update UAV trajectory by SCA → lower-bound antenna-position terms to update element coordinates → alternate the four BCD blocks.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zhai and Luo [x] studied minimum secrecy-rate maximization in UAV-mounted movable-antenna wireless networks with uncertain eavesdropper locations. They jointly optimized user scheduling, transmit beamforming, the UAV trajectory, and onboard antenna positions under power, mobility, movement-region, spacing, and robust secrecy constraints. Triangle inequalities bound worst-case path loss and a representative steering direction approximates angular uncertainty. A four-block BCD method alternates relaxed scheduling, SCA beamforming, SCA trajectory control, and second-order antenna-position updates. Simulations report higher secrecy rate and supportable user count than the evaluated fixed-antenna and restricted-mobility baselines.

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
