---
type: source
title: "A DRL-Based High-Altitude Platform Transmission and Energy Harvesting Scheduling Scheme for 6G NOMA SAGINs"
authors: ["Yi-Huai Hsu", "Jiun-Ian Lee", "Chao-Hung Lee"]
year: 2025
url: "https://doi.org/10.1109/TCCN.2025.3629973"
venue: "IEEE Transactions on Cognitive Communications and Networking"
tags: [source, hap, sagin, noma, energy-harvesting, ppo, drl, 6g]
related:
  - "[[high-altitude-platform-station]]"
  - "[[noma]]"
  - "[[space-air-ground-integrated-network]]"
  - "[[rf-energy-harvesting]]"
  - "[[ppo]]"
  - "[[wireless-power-transfer]]"
  - "[[zhu-2025-lycnn-drl-wpt-mec]]"
created: 2026-05-29
updated: 2026-06-01
---

# A DRL-Based High-Altitude Platform Transmission and Energy Harvesting Scheduling Scheme for 6G NOMA SAGINs

## Citation

Hsu, Y.-H., Lee, J.-I., & Lee, C.-H. (2025). *A DRL-Based High-Altitude Platform Transmission and Energy Harvesting Scheduling Scheme for 6G NOMA SAGINs*. **IEEE Transactions on Cognitive Communications and Networking**. DOI: 10.1109/TCCN.2025.3629973.

## TL;DR

A [[high-altitude-platform-station|HAP]] in a [[space-air-ground-integrated-network|SAGIN]] simultaneously relays uplink data to a satellite (sharing a ground station's TDMA slot via [[noma|NOMA]]) and harvests RF energy from that same ground station's signal. Per-slot decisions: time-sharing ratio α between transmission and harvesting, plus the HAP's transmit power ratio β. Goal: maximize **long-term average binary scale satisfaction (BSS)** — fraction of slots in which the HAP's per-slot data-rate requirement is met — subject to battery-energy and power constraints.

The authors prove the problem is NP-hard via reduction from knapsack and solve it with a **DRL-HUES** scheme based on [[ppo|PPO]] over an MDP formulation.

## Why this matters for MEC

Not strictly an MEC paper, but it's a **foundations** entry for the wiki's HAP track. Most HAP-MEC papers (e.g. [[peng-2025-drudm-cfg]], [[qin-2025-bcuav-masac]]) assume the HAP has reliable energy and uplink. This paper supplies the underlying scheduler that keeps an energy-constrained HAP viable.

The objective choice — **BSS** rather than average data rate — is worth noting: optimizing average rate concentrates energy in good slots and starves bad ones, which is exactly the wrong shape for a long-term service guarantee.

## Method (DRL-HUES)

- **State.** Remaining battery energy E(i), HAP data-rate requirement R_req(i), GS transmit power P_m^GS(i), channel gains.
- **Action.** Continuous (α(i), β(i)) ∈ [0, 1]².
- **Reward.** BSS(i) ∈ {0, 1} — 1 if achieved rate ≥ requirement.
- **Algorithm.** PPO with clipped surrogate objective.

## Findings

- DRL-HUES significantly outperforms No-Pain-No-Gain (the SoTA related-work baseline), random, and greedy schedulers on long-term average BSS.
- Greedy fails because it depletes the battery on early slots; random fails because it ignores demand. PPO learns to defer energy use to slots where the demand is feasible.

## Limitations

- Single HAP, single satellite, M ground stations — no swarm-level effects.
- Reward shape is binary, which is sample-inefficient. A shaped reward (e.g. softmin(SDR, 1)) would likely converge faster.
- Channel model is free-space + antenna gain only — no rain attenuation or atmospheric effects, which matter at HAP altitudes.

## Cross-link with related sources

- **Track:** energy-constrained aerial scheduling, alongside [[zhu-2025-lycnn-drl-wpt-mec]] (Lyapunov + WPT).
- **Architecture:** SAGIN puts this paper alongside [[mao-2025-bcsa-frl]] (LEO-tier) at the *upper* aerial layer, distinct from the UAV-only papers that dominate the corpus.
- **Solver:** vanilla PPO, in contrast with [[liu-2026-jppo-en-convntm]]'s hybrid-action j-PPO. PPO suffices here because the action space is purely continuous.

## Raw artifacts

- `raw/sources/A DRL-Based High-Altitude Platform Transmission and Energy Harvesting Scheduling Scheme for 6G NOMA/full.md`
