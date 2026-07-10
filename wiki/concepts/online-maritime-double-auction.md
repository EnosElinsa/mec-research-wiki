---
type: concept
title: "Online Maritime Double Auction"
tags: [auction, maritime, online-algorithm, resource-allocation, mechanism-design]
related: ["[[maritime-mec]]", "[[li-2026-online-maritime-double-auction]]", "[[dai-2024-multiuav-marine-welfare]]", "[[zeng-2024-usv-fleet-collaborative-offloading]]"]
created: 2026-07-11
updated: 2026-07-11
---

# Online Maritime Double Auction

An online double-auction pattern for maritime connectivity: ships arrive over time as buyers of bandwidth, ISPs act as sellers through antennas or UAVs, and the auctioneer must accept/reject bids before seeing all future demand.

[[li-2026-online-maritime-double-auction]] implements this pattern as OMDAM. Its auction is maritime-specific because feasibility depends on ship mobility, bid deadlines, antenna/UAV coverage radius, ISP capacity, UAV availability, and weather-linked link state. It differs from the [[dai-2024-multiuav-marine-welfare]] marine-MEC double auction, where UAVs buy computation from ocean beacon stations, and from [[zeng-2024-usv-fleet-collaborative-offloading]], where UAVs use a reverse auction to offload computation to USV fleets.

The concept is useful whenever maritime resource allocation must preserve real-time responsiveness and economic participation constraints while the network topology is moving.
