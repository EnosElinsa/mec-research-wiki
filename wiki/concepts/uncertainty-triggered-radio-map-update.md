---
type: concept
title: "Uncertainty-Triggered Radio-Map Update"
tags: [radio-map, event-triggered-update, uncertainty-quantification, mc-dropout, uav-navigation]
related:
  - "[[guo-2026-event-triggered-sinr-navigation]]"
  - "[[radio-map-aided-uav-path-planning]]"
  - "[[information-driven-uav-spectrum-mapping]]"
created: 2026-07-13
updated: 2026-07-13
---

# Uncertainty-Triggered Radio-Map Update

An uncertainty-triggered radio-map update refreshes a UAV's map only when the map estimator becomes insufficiently certain at the current operating region. The trigger converts map freshness into an explicit communication-budget decision: a low threshold favors frequent accurate updates, while a high threshold suppresses traffic but tolerates staleness.

In [[guo-2026-event-triggered-sinr-navigation]], UT-Grid runs MC-dropout on a ground-side U-Net, uses predictive SINR variance as the trigger statistic, and sends coarse global plus fine local map patches to the UAV when the threshold is exceeded. This complements [[radio-map-aided-uav-path-planning]], which describes how maps guide motion, and [[information-driven-uav-spectrum-mapping]], where uncertainty drives where the UAV should measure rather than when a server should refresh its onboard map.
