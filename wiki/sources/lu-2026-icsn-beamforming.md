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
modeling_card: required
created: 2026-07-13
updated: 2026-07-16
---

# Integrated Communication, Sensing and Navigation Beamforming Design for Low-altitude Scenarios

## Citation

Lu, R., Zhang, Y., Li, C., Liang, X., & Liu, B. (2026). *Integrated Communication, Sensing and Navigation Beamforming Design for Low-altitude Scenarios*. **IEEE Transactions on Green Communications and Networking**, early access, 1-1. DOI: 10.1109/TGCN.2026.3709306.

*Metadata note:* The parse carries an unresolved August 2025 draft header (`VOL. XX, NO. XX`) and no DOI. The exact-title Crossref record identifies the final 2026 TGCN early-access article above.

## TL;DR

Uses a two-stage base-station beam design for airborne-user communication, angular target sensing, and navigation assistance. An ISMR-constrained acquisition beam estimates directions; a CRB-guided AO/FP loop then reshapes communication and sensing covariances around angular-confidence regions.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A ULA-equipped base station serves $K$ single-antenna airborne users and senses $L$ angular targets; Stage 1 probes coarse directions, and Stage 2 sends communication and navigation assistance while reserving radar power, with uncertain target CSI.

**Problem & objective**: For Stage 2, maximize the normalized communication and sensing tradeoff, $\max_{\mathbf W_k,\mathbf R_r}\frac{\rho}{\mathcal R_{\mathrm{sum}}}\sum_kR_k^{\mathrm{Com}}+\frac{1-\rho}{\log_2\mathcal D_{\max}}\log_2\det(\mathbf{FIM}_2)$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| User covariance | $\mathbf W_k$ | positive semidefinite matrix | Covariance of user $k$ communication beam |
| Radar covariance | $\mathbf R_r$ | positive semidefinite matrix | Dedicated sensing covariance in Stage 2 |
| FP auxiliary | $y_k$ | continuous scalar | Quadratic-transform variable for user $k$ rate |
| Stage-1 radar covariance | $\mathbf R_{\mathrm{rad}}$ | positive semidefinite matrix | Wide acquisition beam covariance |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Communication reliability requires $\mathrm{SINR}_k^{\mathrm{Com}}\geq\gamma_{\mathrm{com}}$. |
| C2 | Mainlobe and sidelobe powers obey $P(\theta_t)-P(\theta_s)\geq\gamma_s$ for sidelobe angles. |
| C3 | Mainlobe stability bounds use $(1-\alpha)P(\theta_t)\leq P(\theta_m)\leq(1+\alpha)P(\theta_t)$. |
| C4 | Covariances are positive semidefinite and satisfy $\mathrm{tr}(\sum_k\mathbf W_k+\mathbf R_r)=P_0$. |
| C5 | Stage 1 focuses the acquisition beam with $\mathrm{ISMR}\leq\mathrm{ISMR}_{\max}$ and $\mathrm{tr}(\mathbf R_{\mathrm{rad}})\leq P_0$. |

**Algorithm**: Solve the Stage-1 max-det FIM problem under ISMR and power constraints, estimate directions with Capon spectra and CRB confidence intervals, then alternate Stage-2 covariance updates using quadratic fractional programming and log-det FIM optimization until the angular estimates and beamformers converge.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Lu et al. [x] studied integrated communication, sensing, and navigation beamforming for a ULA base station serving airborne users and angular targets. They formulated a weighted sum-rate and FIM-determinant problem with SINR, mainlobe-sidelobe, positive-semidefinite, and total-power constraints. A wide ISMR-constrained acquisition beam and Capon angle estimation initialize CRB confidence regions, after which fractional programming and alternating optimization refine the communication and radar covariances. Simulations show faster convergence from directional initialization and report communication and sensing performance close to the corresponding single-objective benchmarks while outperforming omnidirectional transmission.

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
