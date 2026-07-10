---
type: concept
title: "Double Auction"
tags: [game-theory, auction, market-mechanism, resource-allocation]
related:
  - "[[bargaining-game]]"
  - "[[matching-theory-for-resource-allocation]]"
  - "[[stackelberg-game]]"
  - "[[reverse-auction-incentive]]"
  - "[[online-maritime-double-auction]]"
  - "[[li-2026-online-maritime-double-auction]]"
  - "[[dai-2024-multiuav-marine-welfare]]"
  - "[[seid-2026-mafdrl-tn-ntn-incentive]]"
created: 2026-05-31
updated: 2026-07-11
---

# Double Auction

A **double auction** is a market mechanism with multiple buyers **and** multiple sellers who submit bids and asks; a controller matches them and sets transaction prices. Unlike a single-sided auction (one seller, many buyers), both sides are strategic, and the design must respect **individual rationality** (buyers never pay above their valuation; sellers never accept below their cost) while clearing many-to-many supply-demand.

## In this wiki

- [[dai-2024-multiuav-marine-welfare]] uses a double-auction game for **OBS selection** in marine multi-access MEC: UAVs are buyers of computing service, ocean beacon stations (OBSs) are sellers, and a leader OBS is the auction controller. It defines valuation, bidding, and K-payment rules plus a dynamic bidding-adjustment strategy to raise the transaction success ratio. It sits alongside the wiki's other market/negotiation mechanisms: [[bargaining-game]], [[stackelberg-game]], [[matching-theory-for-resource-allocation]], and the single-buyer [[reverse-auction-incentive]] used by [[zeng-2024-usv-fleet-collaborative-offloading]].
- [[seid-2026-mafdrl-tn-ntn-incentive]] uses a hierarchical double auction in TN-NTN resource trading: EDs buy computation, communication, and power resources while aerial providers and EDs can trade FL service participation, with a DDPG auctioneer selecting prices and matches.
- [[li-2026-online-maritime-double-auction]] adapts the double-auction family to online maritime connectivity. Ships buy bandwidth, antenna/UAV ISPs sell capacity, and [[online-maritime-double-auction]] adds bid deadlines, coverage radii, UAV mobility, weather-linked capacity, and weak-budget-balance constraints.
