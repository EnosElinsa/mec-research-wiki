---
type: source
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
updated: 2026-07-13
---

# Movable Antenna Empowered Multi-UAV MIMO Communications: Joint Macro-Micro Positioning and Beamforming

## Citation

Wan, B., Zhang, Y., Chen, Y., Yang, S., Zhu, Q., Wei, N., Jiang, C., & Liu, Y. (2026). *Movable Antenna Empowered Multi-UAV MIMO Communications: Joint Macro-Micro Positioning and Beamforming*. **IEEE Transactions on Wireless Communications, 25**, 13776-13787. DOI: 10.1109/TWC.2026.3672791.

## TL;DR

Maximizes uplink multi-UAV MIMO sum rate by jointly selecting whole-UAV positions, local movable-element positions, per-UAV precoders, and BS receive combiners. A WMMSE transformation and hierarchical group-sparse pursuit turn continuous macro/micro geometry into dictionary-based position selection.

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
