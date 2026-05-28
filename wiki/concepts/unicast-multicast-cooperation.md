---
type: concept
title: "Unicast-Multicast Cooperation"
tags: [communication, unicast, multicast, noma, sic]
related:
  - "[[noma]]"
  - "[[wireless-backhaul]]"
  - "[[liu-2025-haps-uav-maritime-iot]]"
created: 2026-05-29
updated: 2026-05-29
---

# Unicast-Multicast Cooperation

A hybrid transmission scheme in which one infrastructure node delivers **unicast** content (per-recipient, e.g. private vessel data) while another delivers **multicast** content (shared, e.g. weather, traffic) to the same set of users. Receivers decode the multicast stream first via SIC ([[noma]]-style "stronger user" detection), then decode their unicast stream using the residual signal.

The defining bottleneck of multicast is the **worst channel in the multicast group** — the multicast achievable rate is capped by the laggard receiver. UAV placement therefore tends to favor the worst-channel user, which is a different optimization shape than unicast-only deployment.

In the wiki, [[liu-2025-haps-uav-maritime-iot]] uses HAPS as a unicast provider for vessels and UAVs as multicast providers for grouped vessels, with the HAPS also providing a wireless backhaul link to the UAVs.
