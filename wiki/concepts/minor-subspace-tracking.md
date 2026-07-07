---
type: concept
title: "Minor Subspace Tracking"
tags: [signal-processing, localization, array-processing, subspace-tracking]
related:
  - "[[majorization-minimization]]"
  - "[[cramer-rao-bound]]"
  - "[[uav-trajectory-control]]"
  - "[[cao-2026-uav-self-tracking-ms-mm]]"
created: 2026-07-07
updated: 2026-07-07
---

# Minor Subspace Tracking

Minor subspace tracking estimates and updates the noise or low-eigenvalue subspace of an array-signal covariance structure over time. In localization, that subspace can carry direction/position information while suppressing dominant signal/noise components, making it useful for onboard sensing when a UAV cannot rely on GNSS.

In [[cao-2026-uav-self-tracking-ms-mm]], minor subspace tracking is the front end of a 3-D UAV self-tracking pipeline. The paper proposes an enhanced approximate inverse-power update, then feeds the updated minor subspace into a [[majorization-minimization]] position iteration and benchmarks the tracking error against [[cramer-rao-bound|CRLB]] expressions.
