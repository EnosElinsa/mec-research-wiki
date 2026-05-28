---
type: concept
title: UAV Charging Scheduling
tags: [uav, energy, decision]
related:
  - "[[uav-trajectory-control]]"
  - "[[energy-expenditure-coefficient]]"
  - "[[charging-stations-improve-efficiency]]"
  - "[[liu-2026-jppo-en-convntm]]"
created: 2026-05-28
updated: 2026-05-28
---

# UAV Charging Scheduling

A discrete decision per UAV per time slot: $\xi_{u,n} \in \{0,1\}$, where 1 means "fly toward an effective area near a charging station, hover, and recharge". The model in [[liu-2026-jppo-en-convntm]] adds a fixed fraction $q E^{\max}_u$ of capacity per charging slot:

$$
E^{\text{Left}}_{u,n} = E^{\text{Old-Left}}_{u,n} + q\, \xi_{u,n}\, E^{\max}_{u,n}
$$

with $E^{\text{Old-Left}}_{u,n} = E^{\text{Left}}_{u,n-1} - E^{\text{Fly}}_{u,n}$ — the cost of flying to the station is paid first.

## Why scheduling matters

Charging is *not free* — the UAV must abandon its data-collection role for the duration. Choosing the wrong moment to recharge costs both $\psi$ (data collection) and $f$ (fairness). Choosing the wrong station inflates $\kappa$. Increasing the *number* of stations gives the controller more locally-cheap options — see [[charging-stations-improve-efficiency]].

In [[liu-2026-jppo-en-convntm]] this is the discrete-action component handled by [[j-ppo]]'s discrete head.
