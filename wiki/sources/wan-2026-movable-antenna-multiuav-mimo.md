---
type: source
modeling_card: required
title: "Movable Antenna Empowered Multi-UAV MIMO Communications: Joint Macro-Micro Positioning and Beamforming"
authors: ["Boyu Wan", "Yu Zhang", "Yong Chen", "Songjie Yang", "Qiuming Zhu", "Ning Wei", "Chunxiao Jiang", "Yuanwei Liu"]
year: 2026
url: "https://doi.org/10.1109/TWC.2026.3672791"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), vol. 25, pp. 13776-13787"
tags: [source, movable-antenna, multi-uav, mimo, beamforming, wmmse, sparse-recovery]
related:
  - "[[movable-antenna]]"
  - "[[two-level-movable-antenna]]"
  - "[[air-to-ground-channel-model]]"
  - "[[weighted-minimum-mean-square-error]]"
  - "[[qiuming-zhu]]"
  - "[[chunxiao-jiang]]"
  - "[[yuanwei-liu]]"
created: 2026-07-13
updated: 2026-11-03
---

# Movable Antenna Empowered Multi-UAV MIMO Communications: Joint Macro-Micro Positioning and Beamforming

## Citation

Wan, B., Zhang, Y., Chen, Y., Yang, S., Zhu, Q., Wei, N., Jiang, C., & Liu, Y. (2026). *Movable Antenna Empowered Multi-UAV MIMO Communications: Joint Macro-Micro Positioning and Beamforming*. **IEEE Transactions on Wireless Communications, 25**, 13776-13787. DOI: 10.1109/TWC.2026.3672791.

## TL;DR

Maximizes uplink multi-UAV MIMO sum rate by jointly selecting whole-UAV positions, local movable-element positions, per-UAV precoders, and BS receive combiners. A WMMSE transformation and hierarchical group-sparse pursuit turn continuous macro/micro geometry into dictionary-based position selection.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: $K$ UAVs, each carrying an $N_u$-element movable-antenna (MA) array, send $D$ data streams each in the uplink to an $N_b$-antenna BS. Channels are LoS with free-space path loss, and inter-UAV interference couples the UAV positions $\mathbf p_k$, MA positions $\mathbf q_k$, precoders $\mathbf F_k$, and BS receive matrices $\mathbf W_k$.

**Problem & objective**: Problem (13), a non-convex sum-rate maximization, $\max\sum_kR_k$ with $R_k=\log_2\det(\mathbf I_D+\mathbf F_k^H\mathbf H_k^H\mathbf N^{-1}\mathbf H_k\mathbf F_k)$ in (12), over precoders, UAV positions, and MA positions.

**Decision variables**:
| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV position (macro) | $\mathbf p_k=(x_k,y_k,z_k)$ | continuous; horizontal box | Location of UAV $k$ |
| MA positions (micro) | $\mathbf q_k=\{(x_{n_u,k},y_{n_u,k})\}$ | continuous; local box | Antenna-element positions on UAV $k$ |
| UAV precoder | $\mathbf F_k$ | complex matrix | Uplink precoder for the $D$ streams of UAV $k$ |
| BS receive matrix | $\mathbf W_k\in\mathbb C^{N_b\times D}$ | complex matrix (WMMSE block) | Linear receiver for UAV $k$; MMSE-optimal in (19) |

**Constraints**:
| ID | Meaning and key expression |
|---|---|
| (C1) | UAV power: $\mathrm{Tr}(\mathbf F_k\mathbf F_k^H)\le P_{k,\max}$ |
| (C2)–(C3) | UAV horizontal ranges: $x^u_{\min}\le x^u_k\le x^u_{\max}$, $y^u_{\min}\le y^u_k\le y^u_{\max}$ |
| (C4)–(C5) | MA ranges on each UAV, $(x^a_{\min},x^a_{\max})$ and $(y^a_{\min},y^a_{\max})$ per the text (the parse prints $u$ superscripts) |
| (C6) | UAV collision avoidance: $\lVert\mathbf p_k-\mathbf p_i\rVert\ge d^u_{\min}$ |
| (C7) | Antenna spacing: inter-antenna distance at least $d^a_{\min}$ |

**Algorithm**: GGO-WMMSE: rewrite (13) in WMMSE form with weights $\mathbf B_k$; update $\mathbf W_k$ by the MMSE solution (19) and $\mathbf B_k$ by matrix inversion (21); handle (C1) with a Lagrange multiplier found by binary search for $\mathbf F_k$; select UAV- and MA-position atoms from candidate dictionaries that satisfy (C6)–(C7) with the hierarchical grouped sparse pursuit RLS-G-GSOMP (Algorithm 1); repeat until convergence.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Wan et al. [x] studied movable-antenna-enhanced multi-UAV MIMO uplink communication. They formulated a sum-rate maximization problem that jointly optimizes whole-UAV positions, local antenna-element positions, UAV precoders, and base-station receive combiners under power, deployment, collision, and antenna-spacing constraints. A WMMSE transformation alternates combiner, weight, and precoder updates, while hierarchical grouped sparse pursuit selects macro and micro position atoms from dictionaries. The transformed objective is monotone and bounded, yielding value convergence without a global-optimality claim for the continuous problem. Simulations compare GGO-WMMSE with FPA-OPU (UAV positions only), FPU-MA (MA positions only), WMMSE, and MMSE baselines; the gap is small at low SNR and widens as SNR grows.

## Problem and system model

Multiple UAVs each send one uplink stream to a multi-antenna BS. Every UAV carries a two-dimensional movable array. LoS/free-space links and mutual multi-UAV interference couple UAV locations, local element offsets, transmit precoders, and receive combiners under power, position-box, collision-distance, and element-spacing constraints.

## Method

The sum-rate problem is transformed through [[weighted-minimum-mean-square-error|WMMSE]] and regularized least squares. GGO-WMMSE alternates closed-form MMSE combiner/weight updates with RLS-G-GSOMP: a hierarchical greedy sparse-recovery step first selects a UAV-position atom, then grouped antenna-position atoms. The transformed objective is monotone and bounded, proving value convergence but not global optimality of the original continuous problem.

## Key findings

Across the plotted SNR, UAV-count, antenna-count, and movement-region sweeps, the proposed method has the highest displayed sum rate among the tested fixed-position, partially movable, conventional WMMSE, and MMSE baselines. The advantage grows with denser UAV loading and larger arrays. The paper gives no prose-level exact gain, so these comparisons remain qualitative and figure-derived.

## Limitations

Evaluation is simulation-only. Continuous positions are quantized onto finite dictionaries, so grid resolution trades complexity for quality. The model assumes LoS/free-space propagation, one stream per UAV, fixed altitude, and perfect modeled channel/state information. One simulation-table antenna bound appears sign-reversed. Measured channels, hover jitter, vibration, and physical movable-array tests remain future work.

## Relation to the corpus

This source extends [[two-level-movable-antenna]] from max-min swarm reception to uplink sum-rate design with independent UAV transmitters and a cellular BS. Its macro/micro variables are optimized through sparse position dictionaries rather than SCA geometry updates.

## Raw artifacts

- `raw/sources/Movable_Antenna_Empowered_Multi-UAV_MIMO_Communications_Joint_Macro-Micro_Positioning_and_Beamforming/Movable_Antenna_Empowered_Multi-UAV_MIMO_Communications_Joint_Macro-Micro_Positioning_and_Beamforming.md`
- Original PDF and extracted figures (`images/`) are in the same folder.
