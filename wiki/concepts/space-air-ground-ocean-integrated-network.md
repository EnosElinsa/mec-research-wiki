---
type: concept
title: "Space-Air-Ground-Ocean Integrated Network (SAGOI-Net)"
tags: [sagin, satellite, ocean, maritime, 6g, architecture, non-terrestrial-network]
related:
  - "[[space-air-ground-integrated-network]]"
  - "[[non-terrestrial-network]]"
  - "[[maritime-mec]]"
  - "[[virtual-network-embedding]]"
  - "[[network-function-virtualization]]"
  - "[[zhang-2024-qos-vne-sagoin]]"
created: 2026-06-02
updated: 2026-06-02
---

# Space-Air-Ground-Ocean Integrated Network (SAGOI-Net)

A hierarchical network architecture that extends the [[space-air-ground-integrated-network|SAGIN]] with an explicit **ocean / maritime** segment: it stacks **space** (satellites), **air** (HAPS/UAVs), **ground**, and **ocean** (ships, ocean platforms, maritime users) network tiers into one integrated system. The motivation is comprehensive, low-delay coverage for globally-roaming users — e.g. next-generation intelligent transportation and vehicle communications that travel across land *and* sea — where terrestrial networks alone cannot meet capacity/coverage/delay needs.

Because the tiers are heterogeneous and the topology is time-varying (satellite and platform movement, handovers), efficiently using SAGOI-Net resources and meeting differentiated QoS is hard. Network virtualization (SDN + [[network-function-virtualization|NFV]]) is the usual enabler: the substrate is abstracted into layers and rentable virtual resources are mapped onto it.

## In this wiki

[[zhang-2024-qos-vne-sagoin]] abstracts SAGOI-Net as a **three-layer** physical substrate (satellite / air / ground-ocean, with the ground and ocean segments grouped) and runs QoS-aware multi-domain [[virtual-network-embedding]] over it. SAGOI-Net is the ocean-augmented relative of [[space-air-ground-integrated-network|SAGIN]] within the broader [[non-terrestrial-network]] family, and overlaps the [[maritime-mec]] track wherever the ocean tier carries computation rather than only connectivity.
