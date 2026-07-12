---
type: concept
title: "Fluid Antenna System"
tags: [antenna, spatial-diversity, port-selection, correlation, fluid-antenna]
related:
  - "[[zhu-2026-fas-uav-fbl]]"
  - "[[finite-blocklength-urllc]]"
  - "[[movable-antenna]]"
  - "[[air-to-ground-channel-model]]"
created: 2026-07-13
updated: 2026-07-13
---

# Fluid Antenna System

A fluid antenna system (FAS) exposes multiple candidate antenna positions, or ports, over a compact aperture and selects a favorable port using one or a small number of RF chains. It seeks spatial-diversity gain without the hardware footprint of a conventional simultaneous multi-antenna array.

Port gains are spatially correlated, so the physical port count is not automatically the number of independent diversity branches. In [[zhu-2026-fas-uav-fbl]], a Jakes correlation matrix is eigendecomposed and its rank defines an effective branch count. The selected gain is then approximated by the maximum of eigenvalue-weighted independent Nakagami branches, yielding a tractable diversity order proportional to that effective count.

FAS selection also has operational cost. The same source charges probing time and switching energy for every candidate port, so adding ports can improve [[finite-blocklength-urllc|finite-blocklength]] reliability while eventually reducing energy efficiency or exhausting the short-packet time budget.

FAS is related to [[movable-antenna]], but the control scales differ. A movable-antenna or UAV-positioning design changes a physical antenna or platform location; an FAS selects among closely spaced ports within one terminal aperture. Analytical gains based on independent-branch surrogates should be distinguished from validation on the original correlated physical channel or FAS hardware.
