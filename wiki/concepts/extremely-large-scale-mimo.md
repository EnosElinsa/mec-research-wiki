---
type: concept
title: "Extremely Large-Scale MIMO (XL-MIMO)"
tags: [xl-mimo, mimo, 6g, physical-layer, near-field]
related:
  - "[[min-2026-sparse-bistatic-nearfield-isac]]"
  - "[[sparse-xl-mimo]]"
  - "[[near-field-communications]]"
  - "[[intelligent-reflecting-surface]]"
  - "[[terahertz-communication]]"
  - "[[wang-2024-xl-mimo-tutorial]]"
  - "[[selective-near-field-area]]"
  - "[[bai-adaptive-near-field-xl-mimo-multi-uav]]"
created: 2026-06-02
updated: 2026-07-14
---

# Extremely Large-Scale MIMO (XL-MIMO)

[[min-2026-sparse-bistatic-nearfield-isac]] adds [[sparse-xl-mimo]]: deliberately enlarged element spacing increases aperture and coarray degrees of freedom with fewer physical elements, but introduces grating lobes and calibration/model-sensitivity risks.

A 6G physical-layer evolution of massive MIMO (mMIMO) that deploys a much larger number of antennas and a substantially larger array aperture in a compact space, to gain spectral efficiency and spatial degrees of freedom. Two mainstream realizations: a **discrete** aperture packing thousands of antennas at sub-half-wavelength spacing, and a **continuous aperture (CAP)** that approximates an infinite number of infinitesimal antennas via metamaterials.

[[wang-2024-xl-mimo-tutorial]] organizes XL-MIMO into four hardware designs — ULA-based, UPA-based with patch antennas, UPA-based with point antennas, and CAP-based — and surveys their near-field channel models and signal processing.

## Why it differs from mMIMO

- Far higher antenna count → higher signal-processing complexity and new electromagnetic effects (spatial non-stationarity, severe mutual coupling, polarization).
- Much smaller antenna spacing → more antennas but more hardware complexity/coupling.
- Larger aperture pushes users into the **near field**, so [[near-field-communications|spherical-wave]] models and near-field signal processing replace conventional far-field assumptions.

It is studied alongside other 6G PHY enablers such as [[intelligent-reflecting-surface|RIS]] and [[terahertz-communication|THz]] communication, with applications in physical-layer security, [[integrated-sensing-and-communication|ISAC]], and IoT.

[[bai-adaptive-near-field-xl-mimo-multi-uav]] adds a concrete UAV-channel-modeling instance: an XL-MIMO UPA at a ground station serves multiple UAVs, and [[selective-near-field-area]] limits where spherical-wave computation is required.
