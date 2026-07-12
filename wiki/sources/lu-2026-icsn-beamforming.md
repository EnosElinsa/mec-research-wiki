---
type: source
title: "Integrated Communication, Sensing and Navigation Beamforming Design for Low-altitude Scenarios"
authors: ["Ruoyu Lu", "Yuexia Zhang", "Chuanjun Li", "Xiao Liang", "Baojin Liu"]
year: 2026
url: "https://doi.org/10.1109/TGCN.2026.3709306"
venue: "IEEE Transactions on Green Communications and Networking (IEEE TGCN)"
tags: [source, integrated-communication-sensing-navigation, low-altitude, beamforming, cramer-rao-bound, fractional-programming]
related:
  - "[[integrated-communication-sensing-navigation]]"
  - "[[crb-guided-angular-confidence-beamforming]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[cramer-rao-bound]]"
  - "[[fractional-programming-dinkelbach]]"
  - "[[low-altitude-intelligent-network]]"
  - "[[joint-localization-and-communication]]"
  - "[[su-2024-sensing-aided-isac-pls]]"
created: 2026-07-13
updated: 2026-07-13
---

# Integrated Communication, Sensing and Navigation Beamforming Design for Low-altitude Scenarios

## Citation

Lu, R., Zhang, Y., Li, C., Liang, X., & Liu, B. (2026). *Integrated Communication, Sensing and Navigation Beamforming Design for Low-altitude Scenarios*. **IEEE Transactions on Green Communications and Networking**, early access, 1-1. DOI: 10.1109/TGCN.2026.3709306.

*Metadata note:* The parse carries an unresolved August 2025 draft header (`VOL. XX, NO. XX`) and no DOI. The exact-title Crossref record identifies the final 2026 TGCN early-access article above.

## TL;DR

Uses a two-stage base-station beam design for airborne-user communication, angular target sensing, and navigation assistance. An ISMR-constrained acquisition beam estimates directions; a CRB-guided AO/FP loop then reshapes communication and sensing covariances around angular-confidence regions.

## Problem framing

Low-altitude aerial users need communication, environment sensing, and navigation support from limited spectrum and compact arrays. User-directed communication power competes with sensing/navigation mainlobes, while direct tri-functional optimization is unstable before target directions are known.

## System model

- One ULA-equipped BS serves `K` single-antenna airborne users and senses `L` single-antenna targets.
- Stage 1 probes coarse angular ranges, estimates directions with a Capon spectrum, and derives CRBs.
- Stage 2 sends angular information to users as navigation assistance while superposing user communication beams and continued radar sensing.
- Communication uses sum rate and minimum SINR; sensing uses FIM/CRB determinants and mainlobe/sidelobe constraints.
- Airborne-user CSI is perfect, target CSI is partially uncertain, and target angles are modeled as Gaussian around their estimates.

## Method

[[integrated-communication-sensing-navigation|ICSN]] first maximizes a sensing FIM determinant under an integrated sidelobe-to-mainlobe ratio constraint. [[crb-guided-angular-confidence-beamforming]] converts each angle CRB into the next mainlobe region, then updates communication and radar covariance matrices.

The second stage uses a quadratic-transform fractional-programming update for communication rate and a log-determinant sensing objective. An outer alternating loop recomputes CRBs, target angles, and angular regions until convergence. The implementation reports CVXPY 1.6.4/Python 3.12 for optimization and MATLAB R2018b for figures.

## Key findings

- Directional initialization converges within `2-3` iterations for both 95% and 99% confidence settings; the 99% omnidirectional start remains broader after four iterations.
- Tightening the Stage-1 ISMR from `-10 dB` to `-20 dB` suppresses sidelobes and broadens the mainlobe, trading DoA precision for acquisition robustness.
- AO-FP is reported above omnidirectional transmission across the plotted powers, approaching the communication-only Max-SR benchmark as user count grows.
- Its sensing FIM remains close to the sensing-only Min-CRB benchmark and above the omnidirectional baseline, but the prose gives no exact rate, CRB, or percentage gaps.

## Limitations / parse caveats

Navigation error is explicitly not modeled: navigation is an angle-information service, not a demonstrated navigation-state estimator or 3-D positioning controller. Evaluation is simulation-only, assumes a known coarse angular range, perfect user CSI, ULAs, and one angular dimension, and reports no runtime or convergence proof.

The parse has a missing Stage-2 constraint, damaged covariance/FIM terms, conflicting CRB/FIM normalization labels, mismatched confidence rules, and a 2025 header/2026 degree-timeline conflict. Claims of green operation are conceptual because no energy metric is evaluated.

## Relation to the corpus

This source generalizes the two-stage sensing-aided beam pipeline in [[su-2024-sensing-aided-isac-pls]] from secrecy/eavesdropper estimation to low-altitude user communication and angular navigation assistance. It is adjacent to [[joint-localization-and-communication]], but does not establish navigation accuracy.

## Raw artifacts

- Parse: `raw/sources/Integrated_Communication_Sensing_and_Navigation_Beamforming_Design_for_Low-altitude_Scenarios/Integrated_Communication_Sensing_and_Navigation_Beamforming_Design_for_Low-altitude_Scenarios.md`
- Origin PDF: `raw/sources/Integrated_Communication_Sensing_and_Navigation_Beamforming_Design_for_Low-altitude_Scenarios/Integrated_Communication_Sensing_and_Navigation_Beamforming_Design_for_Low-altitude_Scenarios.pdf`
- Figures: `raw/sources/Integrated_Communication_Sensing_and_Navigation_Beamforming_Design_for_Low-altitude_Scenarios/images/`
