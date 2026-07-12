---
type: concept
title: "Parallel Cooperative UAV Charging"
tags: [uav, wireless-charging, scheduling, approximation-algorithm, shared-cost]
related:
  - "[[wu-2026-parallel-cooperative-charging]]"
  - "[[uav-charging-scheduling]]"
  - "[[wireless-power-transfer]]"
  - "[[generalized-assignment-problem]]"
  - "[[trajectory-privacy]]"
created: 2026-07-12
updated: 2026-07-12
---

# Parallel Cooperative UAV Charging

Parallel cooperative charging assigns UAVs to provider-operated stations and then schedules each station's group across multiple unequal-power charging facilities. The cooperative part is economic: RF facilities can charge in parallel while the provider bills for group operating time, so UAVs assigned together share a station-level cost instead of paying independent per-UAV charges.

In [[wu-2026-parallel-cooperative-charging]], a UAV's station-dependent workload includes demanded energy plus the flight energy needed to detour through that station. The objective jointly chooses station groups and facility queues to minimize total payment. This creates a combination of set covering and uniform parallel-machine scheduling rather than a separable nearest-station assignment.

The CSAU method uses an approximation routine for each station's parallel arrangement and a greedy minimum-average-marginal-cost group extension. Its guarantee inherits both pieces as `gamma(ln n + 1)`. Release times, minimum-size privacy groups, and vehicle-assisted access change the problem enough that some of the original guarantees no longer hold.

This concept complements [[uav-charging-scheduling]], which usually treats recharge as a per-slot operational action competing with sensing or service. Here the core decision is batch formation and shared-cost parallel service across charging infrastructure. [[wireless-power-transfer]] supplies the physical energy-delivery mechanism; the contribution is the combinatorial charging-market schedule.
