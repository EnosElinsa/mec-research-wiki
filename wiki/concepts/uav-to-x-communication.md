---
type: concept
title: "UAV-to-X Communication"
tags: [uav-communications, cellular-network, uav-to-network, uav-to-uav, spectrum-sharing]
related:
  - "[[zhang-not-in-parse-cellular-uav-to-x]]"
  - "[[cellular-connected-uav]]"
  - "[[device-to-device-communication]]"
  - "[[overlay-underlay-spectrum-access]]"
  - "[[uav-mobile-relaying]]"
  - "[[uav-to-uav-communication]]"
created: 2026-07-12
updated: 2026-07-14
---

# UAV-to-X Communication

UAV-to-X communication coordinates multiple link roles around an aerial node rather than treating every UAV as a direct cellular user. In [[zhang-not-in-parse-cellular-uav-to-x]], high-SNR UAVs use UAV-to-network links to a base station, while low-SNR UAVs use underlaid UAV-to-UAV links to a nearby relay UAV that caches and later uploads their sensed data.

The pattern combines [[cellular-connected-uav]], [[device-to-device-communication]], and [[uav-mobile-relaying]]. Its resource-control problem must account for different air-to-ground, air-to-air, and ground channels, cross-mode interference under [[overlay-underlay-spectrum-access]], relay selection, subchannel reuse, and mobility deadlines.
