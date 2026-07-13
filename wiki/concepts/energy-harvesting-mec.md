---
type: concept
title: "Energy Harvesting MEC"
tags: [energy-harvesting, sustainability, maritime, green-energy, lyapunov]
related:
  - "[[kamatchi-2025-slipt-uav-fso]]"
  - "[[rf-energy-harvesting]]"
  - "[[wireless-power-transfer]]"
  - "[[lyapunov-optimization]]"
  - "[[maritime-mec]]"
  - "[[wang-2024-maritime-eh-jcora]]"
  - "[[wang-2026-blockchain-lae-fl-mappo]]"
  - "[[ma-2026-mean-field-green-aec]]"
  - "[[zhang-2022-solar-charging-uav-iot]]"
created: 2026-05-31
updated: 2026-07-13
---

# Energy Harvesting MEC

MEC where the edge node (or device) is powered, fully or partly, by **harvested ambient energy** rather than the grid or a fixed battery. Unlike [[rf-energy-harvesting]] (scavenging from radio signals) or [[wireless-power-transfer]] (a dedicated charger pushes energy), the broader **EH-MEC** framing covers renewable sources — solar, wind, and ocean-wave energy — used to keep off-grid edge servers running.

The harvested energy is **uncertain and time-varying**, so EH-MEC designs typically pair an **energy budget / battery-level constraint** with a long-term performance objective and solve the temporal coupling with [[lyapunov-optimization]] (drift-plus-penalty), avoiding the need to predict future harvest.

In the wiki, [[wang-2024-maritime-eh-jcora]] powers maritime information stations (intelligent buoys) with combined **solar + ocean-wave** harvesting and maximizes long-term throughput under queue-stability + energy constraints via Lyapunov optimization — a renewable EH instance for [[maritime-mec]] where grid access is infeasible at sea. [[wang-2026-blockchain-lae-fl-mappo]] adds PV-aware throttling for service UAVs in a low-altitude FL/MAPPO offloading-and-caching system. [[ma-2026-mean-field-green-aec]] treats energy harvesting as a population-level sustainability mechanism, with energy-focused UAVs replenishing a green aerial edge computing fleet. Complements the RF/WPT energy track ([[hsu-2025-drl-hues-hap-noma]], [[zhu-2025-lycnn-drl-wpt-mec]], [[chen-2025-swipt-mec-sac]]).

[[zhang-2022-solar-charging-uav-iot]] adds a non-MEC communications case in which a UAV harvests modeled solar energy during flight/service and visits charging stations when the learned battery-aware route requires additional energy.
