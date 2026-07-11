---
type: concept
title: "RSS-Based UAV Localization"
tags: [localization, rssi, uav, air-to-ground-channel, trajectory-control]
related:
  - "[[ebrahimi-not-in-parse-autonomous-uav-localization-rl]]"
  - "[[air-to-ground-channel-model]]"
  - "[[uav-trajectory-control]]"
  - "[[uav-localization-under-jamming]]"
  - "[[zhu-2026-uav-localization-jamming]]"
  - "[[cao-2026-uav-self-tracking-ms-mm]]"
created: 2026-07-11
updated: 2026-07-11
---

# RSS-Based UAV Localization

RSS-based UAV localization uses a UAV as a mobile aerial anchor. Ground objects broadcast signals, the UAV records received-signal strength at multiple waypoints, converts RSSI to range estimates through an air-to-ground path-loss model, and then estimates object positions by multilateration or related range-based localization methods.

[[ebrahimi-not-in-parse-autonomous-uav-localization-rl]] adds the trajectory-control layer. The UAV first scans the region to discover objects, then uses Q-learning to choose waypoint cells that reduce average localization error under energy, path-length, time, or waypoint-count budgets. The localization error depends on the geometry of collected RSSI measurements, so motion planning and [[air-to-ground-channel-model|ATG channel modeling]] are inseparable.

This is distinct from [[uav-localization-under-jamming]], where the UAV itself is the target being localized under attack. RSS-based UAV localization is about using the UAV to localize ground objects.
