---
type: concept
title: "Angle-of-Radiation UAV Relay Deployment"
tags: [uav-communications, relay-deployment, antenna-radiation, connectivity]
related:
  - "[[huang-2026-aim-uav-relay-aor]]"
  - "[[uav-mobile-relaying]]"
  - "[[air-to-ground-channel-model]]"
  - "[[wireless-backhaul]]"
created: 2026-07-10
updated: 2026-07-10
---

# Angle-of-Radiation UAV Relay Deployment

Angle-of-radiation UAV relay deployment treats each relay's antenna heading as part of the connectivity decision. Instead of assuming isotropic antennas, it computes received signal strength from the transmitter and receiver positions plus their horizontal/vertical radiation angles, so a UAV operational state includes both 3-D position and heading.

In [[huang-2026-aim-uav-relay-aor]], this turns relay placement into an NP-hard graph search over feasible operational states. The AIM algorithm uses an AoR-aware reachability table to minimize the number of intermediate UAVs while keeping every relay-chain link above the application RSS threshold. The concept extends [[uav-mobile-relaying]] from trajectory/power control toward antenna-pattern-aware deployment.
