---
type: concept
title: "CSI Estimation Error"
tags: [channel-state-information, robust, uncertainty, communication]
related:
  - "[[shah-2026-cellfree-mimo-fap-control]]"
  - "[[distributionally-robust-optimization]]"
  - "[[chance-constraint]]"
  - "[[terrain-aware-channel-model]]"
  - "[[jia-2025-dro-uav-hap-mec]]"
  - "[[he-not-in-parse-cipc-covert-uav]]"
  - "[[channel-inversion-power-control]]"
  - "[[xu-2026-hecta-predictive-beamforming]]"
  - "[[historical-echo-predictive-beamforming]]"
  - "[[jin-2026-jitter-aware-uav-comp]]"
  - "[[ding-2026-optimization-driven-spectrum-sharing]]"
created: 2026-05-29
updated: 2026-07-13
---

# CSI Estimation Error

The discrepancy between the channel state information (CSI) used in resource-allocation decisions and the **actual** channel realized at transmission time. Sources include pilot noise, channel aging between estimation and use, mobility-induced Doppler, and environmental fluctuation (foliage, rain, sea waves).

Most MEC papers in the wiki **assume perfect CSI** to keep the optimization tractable. The wiki has three explicit responses to imperfect CSI:

- **Distributionally robust** — model errors as drawn from a worst-case distribution within a moment-based ambiguity set. [[jia-2025-dro-uav-hap-mec]].
- **Side-step via prior knowledge** — use historical / pre-measured CSI from known routes. [[wang-2026-aerial-marine-msar]] (maritime shipping routes), [[liu-2025-haps-uav-maritime-iot]].
- **Geometric model from terrain** — replace statistical CSI with a deterministic blockage prediction from DEM data. [[wu-2026-terrain-aware-uav-mec]] / [[terrain-aware-channel-model]].

DRL implicitly handles CSI noise by training on noisy environments, but provides no formal guarantees and risks distribution shift at deployment.

[[he-not-in-parse-cipc-covert-uav]] gives an analytical power-control example: Alice-Bob estimation error can make [[channel-inversion-power-control]] overcompensate, improving some legitimate connection metrics while strengthening the adversary and worsening secrecy/covertness.

[[xu-2026-hecta-predictive-beamforming]] sidesteps an explicit intermediate CSI estimate: [[historical-echo-predictive-beamforming]] maps echo history directly to the next bidirectional beam pair. This removes one estimation interface but does not by itself establish robustness to deployment channels outside the synthetic training distribution.

[[jin-2026-jitter-aware-uav-comp]] models attitude jitter as symbol-to-symbol channel aging and trains J-LSTM to predict next-symbol CSI for CoMP precoding from synthetic attitude/channel sequences.
