---
type: concept
title: "Cooperative UAV-Human Courier Delivery"
tags: [uav, delivery, medical-logistics, routing, deep-reinforcement-learning, heterogeneous-vehicles]
related:
  - "[[chen-not-in-parse-uav-human-medical-delivery]]"
  - "[[uav-delivery-pickup-dropoff]]"
  - "[[cooperative-uav-taxi-delivery]]"
  - "[[heterogeneous-agent-rl]]"
created: 2026-07-12
updated: 2026-07-12
---

# Cooperative UAV-Human Courier Delivery

Cooperative UAV-human courier delivery jointly assigns pickup-delivery orders and routes two fleets with different operating rules. Couriers can consolidate several orders; UAVs provide faster direct travel in the modeled setting but have lower capacity and serve one order at a time. The general model uses abstract route distances, while the Shenzhen case gives couriers Amap-derived road routes.

[[chen-not-in-parse-uav-human-medical-delivery]] applies this model to emergency medical logistics with soft deadlines, type-specific policy decoders, feasibility masks, and a vehicle coordinator. It extends [[uav-delivery-pickup-dropoff]] from UAV-only route control and differs from [[cooperative-uav-taxi-delivery]], where taxis contribute opportunistic capacity rather than a dedicated courier fleet.
