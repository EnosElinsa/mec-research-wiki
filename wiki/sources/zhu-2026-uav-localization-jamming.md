---
type: source
title: "3D UAV Localization Optimization Under Jamming Attacks: A Mixture Gaussian Distribution Based Collaborative Reinforcement Learning"
authors: ["Yujiao Zhu", "Mingzhe Chen", "Sihua Wang", "Yuchen Liu", "Changchuan Yin", "Tony Q. S. Quek"]
year: 2026
url: "https://doi.org/10.1109/TMC.2025.3628889"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, uav-localization, jamming-attacks, collaborative-reinforcement-learning, distributional-reinforcement-learning, mixture-gaussian-distribution, generative-adversarial-network, tdoa, trajectory-optimization, power-control]
related:
  - "[[uav-localization-under-jamming]]"
  - "[[distributional-reinforcement-learning]]"
  - "[[value-decomposition-network]]"
  - "[[generative-adversarial-network]]"
  - "[[anti-jamming-mec]]"
  - "[[uav-trajectory-control]]"
  - "[[tony-q-s-quek]]"
  - "[[zhu-2024-zdrl-uav-tracking]]"
created: 2026-07-07
updated: 2026-07-07
---

# 3D UAV Localization Optimization Under Jamming Attacks: A Mixture Gaussian Distribution Based Collaborative Reinforcement Learning

## Citation

Zhu, Y., Chen, M., Wang, S., Liu, Y., Yin, C., & Quek, T. Q. S. (2026). *3D UAV Localization Optimization Under Jamming Attacks: A Mixture Gaussian Distribution Based Collaborative Reinforcement Learning*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2025.3628889.

## TL;DR

Extends collaborative UAV localization to adversarial jamming. A BS, an active UAV, and passive UAVs localize a target UAV while a jamming UAV disrupts distance measurements. The BS can select between GAN-based positioning and TDOA-based positioning, and a mixture-Gaussian collaborative RL method jointly controls active-UAV transmit power, active/passive UAV trajectories, measurement subset selection, and localization-method choice.

## Problem

TDOA localization can be accurate but energy-consuming and vulnerable when jamming degrades the passive UAVs' distance measurements. GAN-based positioning can infer locations from learned samples but may fail under strong jamming or out-of-distribution target motion. The paper asks how to switch between these localization modes while controlling UAV motion and transmit power under unknown jamming patterns.

## System model

- A BS coordinates one active UAV and multiple passive UAVs to localize a target UAV.
- A jamming UAV transmits discontinuous interference toward passive UAVs.
- The BS chooses four passive-UAV distance measurements and selects either GAN-based or TDOA-based positioning.
- The objective minimizes positioning error while accounting for jamming, passive-UAV trajectories, and active-UAV transmit power.

## Method

- The collaborative RL method approximates each agent's value-function distribution with a mixture Gaussian model rather than only estimating an expectation.
- The active UAV optimizes transmit power and trajectory.
- The BS selects the measurement subset and positioning method according to UAV movement and the unknown jamming pattern.
- The method is compared with fixed-method baselines, VD-RL, QMIX, and QTRAN.

## Key findings

- The convergence plot reports up to 36.5%, 27.4%, and 12.7% reward gains over three baselines.
- At 5 W jamming power, the method reports positioning-error gains of 37.4%, 24.8%, and 14.0% over the same baseline groups.
- At target speed 6 m/s, the method reports positioning-error reductions of 45.4%, 30.8%, and 13.7%.
- At scattering coefficient 0.35, it reports reductions of 41.9%, 24.5%, and 18.8%.
- Against VD-RL, QMIX, and QTRAN, it reports future-reward gains of 12.7%, 10.6%, and 25.7%, and a lower convergence time of 1559.690 s in Table IV.

## Relation to the corpus

This source is a UAV sensing/security paper adjacent to MEC. It extends [[zhu-2024-zdrl-uav-tracking]] from non-jammed 3-D UAV tracking to [[uav-localization-under-jamming]], and links [[distributional-reinforcement-learning]] with [[generative-adversarial-network]] positioning and TDOA selection. It is adjacent to [[anti-jamming-mec]] because jamming is the threat model, but the controlled task here is localization rather than compute offloading.

## Raw artifacts

- `raw/sources/3D_UAV_Localization_Optimization_Under_Jamming_Attacks_A_Mixture_Gaussian_Distribution_Based_Collaborative_Reinforcement_Learning/3D_UAV_Localization_Optimization_Under_Jamming_Attacks_A_Mixture_Gaussian_Distribution_Based_Collaborative_Reinforcement_Learning.md`
- Original PDF and extracted figures (`images/`) in the same folder.
