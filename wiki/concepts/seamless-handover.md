---
type: concept
title: "Seamless Handover (LEO data/model handover)"
tags: [leo-satellite, handover, federated-learning, mobility]
related:
  - "[[leo-satellite-edge-computing]]"
  - "[[federated-learning]]"
  - "[[walker-star-constellation]]"
  - "[[han-2024-sagin-fl-handover]]"
created: 2026-05-29
updated: 2026-05-29
---

# Seamless Handover (LEO data/model handover)

In LEO-satellite computing, each satellite covers a target region only for a bounded window before orbiting away. A **seamless handover** transfers the in-progress computation state — here, the partially-trained model plus the dataset being processed — from the departing satellite to the next incoming one over an inter-satellite link (ISL), so the task continues uninterrupted despite limited per-satellite coverage time.

In the wiki, [[han-2024-sagin-fl-handover]] introduces this as a core mechanism for [[federated-learning]] across a SAGIN: the recursive per-coverage-window latency model triggers a handover whenever a satellite cannot finish its share within its window. It depends on knowing/estimating coverage times (modeled via a [[walker-star-constellation]]) and on the ISL handover delay being small relative to compute. Distinct from terrestrial cellular handover — here it's *compute state*, not a user connection, being handed over.
