---
type: concept
title: "Traffic-Aware Offloading"
tags: [offloading, traffic-prediction, resource-provisioning]
related:
  - "[[network-slicing]]"
  - "[[probsparse-self-attention-prediction]]"
  - "[[task-offloading]]"
  - "[[chen-2024-thoas-traffic-aware-sagin]]"
created: 2026-05-29
updated: 2026-05-29
---

# Traffic-Aware Offloading

Coupling time-series **traffic prediction** with offloading and resource-provisioning decisions, so capacity adapts to spatio-temporal load fluctuations rather than being statically provisioned. The idea: forecast where and when demand will spike, then pre-size slices/resources and route offloaded tasks accordingly, avoiding both under-supply (deadline violations) and over-supply (wasted rent).

In the wiki, [[chen-2024-thoas-traffic-aware-sagin]] is the anchor: a [[probsparse-self-attention-prediction|probsparse self-attention predictor]] forecasts cellular traffic (validated on the Milan dataset), and the forecast drives both adaptive [[network-slicing]] and the DRL [[task-offloading]] policy. Distinct from offloading approaches that assume static traffic or known future demand.
