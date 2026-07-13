---
type: concept
title: "Cooperative UAV-Taxi Delivery"
tags: [uav, taxi, delivery, logistics, scheduling, transfer-learning]
related:
  - "[[gao-2026-air-ground-instant-delivery]]"
  - "[[uav-delivery-pickup-dropoff]]"
  - "[[weighted-kmeans-uav-deployment]]"
  - "[[generalized-assignment-problem]]"
  - "[[cooperative-uav-human-courier-delivery]]"
  - "[[chen-not-in-parse-uav-human-medical-delivery]]"
  - "[[xia-2026-ubt-emergency-response]]"
created: 2026-07-12
updated: 2026-07-13
---

# Cooperative UAV-Taxi Delivery

Cooperative UAV-taxi delivery allocates parcels across aerial and crowdsourced ground capacity. Taxis exploit trips they already make but face passenger, route-detour, timing, and participation limits; UAVs provide flexible coverage but face battery, payload, range, and no-fly-zone limits.

[[gao-2026-air-ground-instant-delivery]] estimates taxi delivery capacity, places UAV stations from the residual delivery gap, repositions UAVs toward predicted unmet demand, transfers human-courier preferences into mode-specific assignment models, and sends remaining parcels to a generalized assignment solver. It extends [[uav-delivery-pickup-dropoff]] from UAV-only route design to a city-scale complementary-capacity system.

[[cooperative-uav-human-courier-delivery]] is the dedicated-fleet counterpart: it routes couriers and UAVs directly under medical-order soft deadlines rather than treating existing taxi trips as time-varying residual capacity.
