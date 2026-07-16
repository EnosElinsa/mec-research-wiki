---
type: source
title: "3-D Self-Tracking of UAV Based on Minor Subspace Majorization-Minimization Iteration"
authors: ["Zhongkang Cao", "Jianfeng Li", "Pan Li", "Jianghao Xiao", "Qihui Wu"]
year: 2026
url: "https://doi.org/10.1109/TWC.2026.3686429"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
modeling_card: not_applicable
tags: [source, uav-localization, uav-self-tracking, array-signal-processing, minor-subspace, majorization-minimization, kalman-filter, cramer-rao-bound]
related:
  - "[[minor-subspace-tracking]]"
  - "[[majorization-minimization]]"
  - "[[cramer-rao-bound]]"
  - "[[uav-trajectory-control]]"
  - "[[qihui-wu]]"
  - "[[zhao-2025-networked-isac-uav-handover]]"
  - "[[zhu-2024-zdrl-uav-tracking]]"
created: 2026-07-07
updated: 2026-07-16
---

# 3-D Self-Tracking of UAV Based on Minor Subspace Majorization-Minimization Iteration

## Citation

Cao, Z., Li, J., Li, P., Xiao, J., & Wu, Q. (2026). *3-D Self-Tracking of UAV Based on Minor Subspace Majorization-Minimization Iteration*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2026.3686429.

## TL;DR

Builds a GNSS-independent 3-D UAV self-tracking pipeline from non-cooperative anchors. The method updates a noise-suppressed minor subspace with an enhanced approximate inverse-power (EAIP) algorithm, extracts position through continuous majorization-minimization (MM) iteration instead of grid search, then smooths tracking intervals with a Kalman filter and moving average. The paper also derives per-dimension CRLBs as tracking-accuracy benchmarks.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Cao et al. [x] studied GNSS-independent three-dimensional UAV self-tracking from same-frequency signals emitted by non-cooperative anchors. They proposed an enhanced approximate inverse-power update for noise-suppressed minor-subspace tracking, followed by continuous majorization-minimization position iteration, Kalman filtering, and moving-average acceleration control. They also derived per-axis Cramer-Rao lower bounds as accuracy benchmarks. Simulations report an average minor-subspace error of -15.9637 dB and an average tracking error of 4.089 m, with lower errors than the evaluated AIP-based MUSIC and SSF pipelines.

## Problem

GNSS interruption and radio interference make ordinary UAV navigation unreliable. Cellular-connected localization can be expensive because it consumes cellular-network resources, while RSS/TDOA/FDOA localization often depends on attenuation models or synchronization. The paper asks whether an onboard array can use angle-of-arrival structure from non-cooperative anchors to track the UAV's own 3-D position with lower complexity and better accuracy.

## System model

- A UAV receives non-cooperative anchor signals and estimates self-position from array observations.
- The signal-processing chain focuses on minor-subspace extraction from the array covariance structure.
- The tracking model uses position estimates over time, with Kalman filtering and moving-average acceleration control used for temporal smoothing.
- The paper derives CRLB expressions for the three spatial dimensions to benchmark estimator performance.

## Method

- **EAIP minor-subspace update.** The enhanced approximate inverse-power method adds a residual term, a new orthonormal matrix, and eigenvalue updating to improve minor-subspace precision and suppress noise.
- **MM position iteration.** Continuous MM iteration extracts position from the minor subspace and avoids the initial-value sensitivity and complexity of grid search.
- **Tracking smoother.** A Kalman filter handles interval tracking, while a moving average controls the UAV dynamics acceleration parameter without explicitly constructing a full state-transition equation.

## Key findings

- The proposed EAIP minor-subspace tracker reports an average MS error of -15.9637 dB, lower than ODPM, FDPM, YAST, and AIP by 24.0267 dB, 16.7102 dB, 11.7559 dB, and 2.9436 dB, respectively.
- The full tracking pipeline reports 4.089 m average tracking error, which is 9.841 m lower than AIP+MUSIC+KF and 5.188 m lower than AIP+SSF+KF, while remaining 2.278 m above the CRLB benchmark.
- Per-axis average errors are reported as 2.052 m in x, 1.5 m in y, and 2.495 m in z.
- The evaluation is simulation-based and emphasizes accuracy/complexity, not task offloading.

## Relation to the corpus

This is a sensing/localization source adjacent to MEC rather than an MEC offloading paper. It expands the corpus's UAV-localization thread from [[zhao-2025-networked-isac-uav-handover]] and [[zhu-2024-zdrl-uav-tracking]] toward local self-tracking with array signal processing. Its solver connects [[minor-subspace-tracking]], [[majorization-minimization]], and [[cramer-rao-bound]], and it adds another parse-confirmed source to the [[qihui-wu]] NUAA aerial-computing / sensing cluster.

## Raw artifacts

- `raw/sources/3-D_Self-Tracking_of_UAV_Based_on_Minor_Subspace_Majorization-Minimization_Iteration/3-D_Self-Tracking_of_UAV_Based_on_Minor_Subspace_Majorization-Minimization_Iteration.md`
- Original PDF and extracted figures (`images/`) in the same folder.
