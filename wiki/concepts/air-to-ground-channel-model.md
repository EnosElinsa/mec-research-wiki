---
type: concept
title: "Air-to-Ground Channel Model"
tags: [channel-model, los-nlos, propagation, uav, coverage]
related:
  - "[[blockage-aware-channel-model]]"
  - "[[terrain-aware-channel-model]]"
  - "[[low-altitude-intelligent-network]]"
  - "[[al-hourani-2014-optimal-lap-altitude]]"
created: 2026-05-31
updated: 2026-05-31
---

# Air-to-Ground Channel Model

The **air-to-ground (ATG) channel model** describes propagation between an aerial platform (UAV / LAP / HAP) and ground receivers. The dominant formulation treats received signals as a probabilistic mixture of **LoS** and **NLoS** groups: the mean pathloss is the free-space pathloss plus a group-dependent **excessive pathloss**, weighted by the probability of each group. The **LoS probability** is commonly approximated as a sigmoid (S-curve) of the **elevation angle**, parameterized by the urban environment (built-up ratio, building density, building-height distribution).

## In this wiki

- [[al-hourani-2014-optimal-lap-altitude]] is the foundational origin of this sigmoid-LoS-vs-elevation-angle model: it derives the closed-form LoS probability from ITU P.1410 statistical parameters and uses it to compute the LAP altitude maximizing ground coverage. This statistical sub-family is the most common ATG model across the corpus's aerial sources (cf. [[blockage-aware-channel-model]]'s three sub-families — statistical, radio-map, and geometric — where the [[terrain-aware-channel-model]] is the geometric variant).
