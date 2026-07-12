---
type: source
title: "Fluid Antenna System-Enabled UAV Communications in the Finite Blocklength Regime"
authors: ["Xusheng Zhu", "Kai-Kit Wong", "Hanjiang Hong", "Han Xiao", "Hao Xu", "Tuo Wu", "Chan-Byoung Chae"]
year: 2026
url: "https://doi.org/10.1109/TWC.2026.3688660"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, fluid-antenna-system, finite-blocklength, urllc, uav-relay, block-error-rate, energy-efficiency]
related:
  - "[[fluid-antenna-system]]"
  - "[[finite-blocklength-urllc]]"
  - "[[uav-mobile-relaying]]"
  - "[[energy-latency-tradeoff]]"
  - "[[movable-antenna]]"
  - "[[kai-kit-wong]]"
  - "[[chan-byoung-chae]]"
created: 2026-07-13
updated: 2026-07-13
---

# Fluid Antenna System-Enabled UAV Communications in the Finite Blocklength Regime

## Citation

Zhu, X., Wong, K.-K., Hong, H., Xiao, H., Xu, H., Wu, T., & Chae, C.-B. (2026). *Fluid Antenna System-Enabled UAV Communications in the Finite Blocklength Regime*. **IEEE Transactions on Wireless Communications**, 25, 16714-16729. DOI: 10.1109/TWC.2026.3688660.

## TL;DR

Analyzes short-packet decode-and-forward UAV relaying to a user equipped with a fluid antenna system. An eigenvalue-weighted diversity surrogate yields rural/urban BLER expressions and diversity orders; a hierarchical search jointly chooses blocklength, UAV altitude and power, and port count while charging port-probing overhead.

## Problem framing

Finite-blocklength URLLC cannot use Shannon capacity as a reliability proxy, while size- and power-constrained ground terminals may not support conventional antenna arrays. Fluid ports can provide spatial diversity over a compact aperture, but correlation, port selection time, and switching energy make the number of candidate ports a reliability-efficiency tradeoff rather than a free gain.

## System model

- A BS communicates with one UE through a half-duplex decode-and-forward UAV relay; the FAS is installed at the UE.
- The UAV follows a fixed-radius, constant-altitude circular trajectory. Rural links use free-space loss; urban links use probabilistic LoS/NLoS loss.
- `N` ports lie on a one-dimensional aperture. Jakes correlation is eigendecomposed, and the selected physical-port gain is approximated by the maximum of `N_eff` eigenvalue-weighted independent Nakagami branches.
- A payload of `B` bits uses blocklength `L`; BLER follows the finite-blocklength normal approximation and a piecewise-linear Q-function approximation.
- Port probing takes `N tau_p`, leaving `L/W_band - N tau_p` for data. The energy model includes UAV transmit, propulsion, circuit, and FAS switching terms, although the FAS is physically at the UE.

## Method

The paper derives rural and urban hop CDFs and BLER expressions, using inclusion-exclusion for the FAS hop and Gauss-Chebyshev quadrature for circular-trajectory averaging. High-SNR analysis gives second-hop diversity `m_2 N_eff` (or condition-specific `m_2^k N_eff`) and an end-to-end first-hop error floor when UAV power grows while BS power stays fixed.

Energy efficiency is successful bits per joule. For each blocklength, altitude, and integer port count, a bisection routine finds the minimum UAV power meeting the BLER threshold; an outer grid/exhaustive search keeps the best tuple. The stated complexity is `O(I_L I_Z I_N log2(1/delta))`.

## Key findings

- Closed-form and Monte Carlo results agree for the analytical surrogate; this does not validate the surrogate against a physical correlated-port channel.
- Diversity grows with `N_eff`, while fixed first-hop power creates an end-to-end BLER floor.
- In the urban case at target BLER `10^-3` and `L=200`, `N=4` or `8` saves over `15 dB` of UAV transmit power versus a fixed-position antenna.
- EE is quasi-concave in port count because selection overhead eventually outweighs diversity. In one rural setting, `N*` is about 8 for `L >= 500`; at `L=200`, EE becomes zero for `N >= 10` because probing consumes the block.
- Rural deployment favors the lowest tested altitude; urban minimum power has an intermediate optimum near `450 m` because distance and LoS probability compete.

## Limitations / parse caveats

The system is single-user, one-dimensional-FAS, perfect-CSI, fixed-circle, and simulation-only. Closed forms require integer Nakagami parameters or retain incomplete-gamma forms. Q-function, quadrature, and nested grid searches are approximate. The parse does not prove that the minimum reliability-feasible power always maximizes EE, reconcile UE-side switching energy with a UAV-energy label, or explain two-hop block-time partitioning. Several urban equations and table symbols are damaged.

## Relation to the corpus

This source adds [[fluid-antenna-system]] to the finite-blocklength aerial-communications branch. Unlike whole-platform [[movable-antenna]] positioning, the compact aperture samples spatial ports at one terminal; unlike ordinary [[finite-blocklength-urllc]] optimization, port correlation and probing overhead determine the useful diversity order and energy optimum.

## Raw artifacts

- Parse: `raw/sources/Fluid_Antenna_System-Enabled_UAV_Communications_in_the_Finite_Blocklength_Regime/Fluid_Antenna_System-Enabled_UAV_Communications_in_the_Finite_Blocklength_Regime.md`
- Origin PDF: `raw/sources/Fluid_Antenna_System-Enabled_UAV_Communications_in_the_Finite_Blocklength_Regime/Fluid_Antenna_System-Enabled_UAV_Communications_in_the_Finite_Blocklength_Regime.pdf`
- Figures: `raw/sources/Fluid_Antenna_System-Enabled_UAV_Communications_in_the_Finite_Blocklength_Regime/images/`
