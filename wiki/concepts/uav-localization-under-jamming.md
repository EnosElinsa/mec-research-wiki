---
type: concept
title: "UAV Localization Under Jamming"
tags: [uav, localization, jamming, physical-layer-security, reinforcement-learning]
related:
  - "[[anti-jamming-mec]]"
  - "[[distributional-reinforcement-learning]]"
  - "[[generative-adversarial-network]]"
  - "[[uav-trajectory-control]]"
  - "[[zhu-2026-uav-localization-jamming]]"
  - "[[zhu-2024-zdrl-uav-tracking]]"
created: 2026-07-07
updated: 2026-07-07
---

# UAV Localization Under Jamming

UAV localization under jamming studies how a UAV/BS sensing system estimates a target UAV's position when an adversarial transmitter corrupts distance or signal measurements. The control problem is not only "where should the sensing UAVs move?" but also "which measurements and localization method remain reliable under the current interference pattern?"

In [[zhu-2026-uav-localization-jamming]], the BS dynamically selects between GAN-based and TDOA-based positioning while collaborative RL controls active-UAV power, active/passive UAV trajectories, and passive measurement subsets. The method approximates value-function distributions with mixture Gaussians, connecting the page to [[distributional-reinforcement-learning]].

This concept is adjacent to [[anti-jamming-mec]] because jamming is the threat, but the task is sensing/localization rather than MEC task offloading. It also extends the non-jammed UAV tracking setup in [[zhu-2024-zdrl-uav-tracking]].
