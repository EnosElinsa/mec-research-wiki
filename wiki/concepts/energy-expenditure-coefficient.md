---
type: concept
title: Energy Expenditure Coefficient (κ)
tags: [metric, energy]
related:
  - "[[equilibrium-efficiency-metric]]"
  - "[[uav-charging-scheduling]]"
  - "[[liu-2026-jppo-en-convntm]]"
created: 2026-05-28
updated: 2026-05-28
---

# Energy Expenditure Coefficient (κ)

Defined in [[liu-2026-jppo-en-convntm]] as a weighted ratio of energy *spent* over energy *available*:

$$
\kappa_n = \frac{\eta_u \sum_u \sum_{i=1}^n E^{\text{Fly}}_{u,i} + \eta_d \sum_d \sum_{i=1}^n E_{d,i}}{\eta_u \sum_u \sum_{i=1}^n E^{\text{Charge}}_{u,i} + \eta_u \sum_u E^{\text{Origin}}_u + \eta_d \sum_d E^{\text{Origin}}_d}
$$

with $\eta_u, \eta_d$ as energy-balance weights between UAV side and device side. **Lower κ is better.**

The denominator includes the energy added by recharging, so a controller that uses charging stations effectively can sustain a longer mission without inflating κ. The trade-off is captured by [[charging-stations-improve-efficiency]] and [[uav-count-inverted-u-energy]].
