---
type: concept
title: UAV Charging Scheduling
tags: [uav, energy, decision]
related:
  - "[[uav-trajectory-control]]"
  - "[[energy-expenditure-coefficient]]"
  - "[[charging-stations-improve-efficiency]]"
  - "[[liu-2026-jppo-en-convntm]]"
  - "[[shi-2025-aoi-energy-replenishment-multiuav]]"
  - "[[zhu-2026-hab-mappo-target-search]]"
  - "[[wu-2026-parallel-cooperative-charging]]"
  - "[[parallel-cooperative-uav-charging]]"
created: 2026-05-28
updated: 2026-07-12
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

[[shi-2025-aoi-energy-replenishment-multiuav]] applies the same scheduling tension to AoI-aware IoT data collection: a UAV either keeps serving sensor nodes or switches into a charging-station mode, and value-decomposition MARL learns when the AoI benefit of continued service no longer outweighs battery risk.

[[zhu-2026-hab-mappo-target-search]] uses the same scheduling idea in a laser-charged target-search setting: during the offloading subslot, each UAV either searches or charges, and the learned charging policy extends search time relative to a fixed-threshold charging baseline in the reported simulations.

[[wu-2026-parallel-cooperative-charging]] shifts the scheduling layer from per-slot mission control to charging infrastructure. Its [[parallel-cooperative-uav-charging]] model forms shared-cost station groups and assigns each group across unequal-power parallel facilities.
