---
type: concept
title: "Energy Harvesting MEC"
tags: [energy-harvesting, sustainability, maritime, green-energy, lyapunov]
related:
  - "[[rf-energy-harvesting]]"
  - "[[wireless-power-transfer]]"
  - "[[lyapunov-optimization]]"
  - "[[maritime-mec]]"
  - "[[wang-2024-maritime-eh-jcora]]"
created: 2026-05-31
updated: 2026-05-31
---

# Energy Harvesting MEC

MEC where the edge node (or device) is powered, fully or partly, by **harvested ambient energy** rather than the grid or a fixed battery. Unlike [[rf-energy-harvesting]] (scavenging from radio signals) or [[wireless-power-transfer]] (a dedicated charger pushes energy), the broader **EH-MEC** framing covers renewable sources — solar, wind, and ocean-wave energy — used to keep off-grid edge servers running.

The harvested energy is **uncertain and time-varying**, so EH-MEC designs typically pair an **energy budget / battery-level constraint** with a long-term performance objective and solve the temporal coupling with [[lyapunov-optimization]] (drift-plus-penalty), avoiding the need to predict future harvest.

In the wiki, [[wang-2024-maritime-eh-jcora]] powers maritime information stations (intelligent buoys) with combined **solar + ocean-wave** harvesting and maximizes long-term throughput under queue-stability + energy constraints via Lyapunov optimization — a renewable EH instance for [[maritime-mec]] where grid access is infeasible at sea. Complements the RF/WPT energy track ([[hsu-2025-drl-hues-hap-noma]], [[zhu-2025-lycnn-drl-wpt-mec]], [[chen-2025-swipt-mec-sac]]).
