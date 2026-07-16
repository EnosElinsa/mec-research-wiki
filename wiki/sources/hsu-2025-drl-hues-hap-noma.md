---
type: source
title: "A DRL-Based High-Altitude Platform Transmission and Energy Harvesting Scheduling Scheme for 6G NOMA SAGINs"
authors: ["Yi-Huai Hsu", "Jiun-Ian Lee", "Chao-Hung Lee"]
year: 2025
url: "https://doi.org/10.1109/TCCN.2025.3629973"
venue: "IEEE Transactions on Cognitive Communications and Networking"
modeling_card: required
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
updated: 2026-07-16
---

# A DRL-Based High-Altitude Platform Transmission and Energy Harvesting Scheduling Scheme for 6G NOMA SAGINs

## Citation

Hsu, Y.-H., Lee, J.-I., & Lee, C.-H. (2025). *A DRL-Based High-Altitude Platform Transmission and Energy Harvesting Scheduling Scheme for 6G NOMA SAGINs*. **IEEE Transactions on Cognitive Communications and Networking**. DOI: 10.1109/TCCN.2025.3629973.

## TL;DR

A [[high-altitude-platform-station|HAP]] in a [[space-air-ground-integrated-network|SAGIN]] simultaneously relays uplink data to a satellite (sharing a ground station's TDMA slot via [[noma|NOMA]]) and harvests RF energy from that same ground station's signal. Per-slot decisions: time-sharing ratio α between transmission and harvesting, plus the HAP's transmit power ratio β. Goal: maximize **long-term average binary scale satisfaction (BSS)** — fraction of slots in which the HAP's per-slot data-rate requirement is met — subject to battery-energy and power constraints.

The authors prove the problem is NP-hard via reduction from knapsack and solve it with a **DRL-HUES** scheme based on [[ppo|PPO]] over an MDP formulation.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A HAP relays uplink traffic to a satellite while sharing ground-station TDMA slots through NOMA and successive interference cancellation. In every slot it divides time between uplink transmission and RF energy harvesting from the ground-station signal under stochastic channel gains, demand, and finite battery capacity.

**Problem & objective**: Problem Q is an NP-hard nonlinear scheduling problem that maximizes long-term average binary scale satisfaction, $\max_{\boldsymbol\alpha,\boldsymbol\beta}\frac{1}{\lvert\mathcal I\rvert}\sum_{i\in\mathcal I}BSS(i)$, where a slot is satisfied when the achieved HAP data rate meets its requirement.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Transmission time share | $\alpha(i)$ | continuous, $[0,1]$ | Fraction of slot $i$ used for HAP uplink transmission rather than harvesting |
| HAP power ratio | $\beta(i)$ | continuous, $[0,1]$ | Fraction of maximum HAP transmit power used in slot $i$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| 13 | Battery recursion accounts for harvested and transmitted energy and caps storage at $E_{max}$ |
| 14 | Transmission energy satisfies $\alpha(i)TP^{HAP}(i)\leq E(i)$ |
| 15 | Time sharing satisfies $0\leq\alpha(i)\leq1$ |
| 16 | Power allocation satisfies $0\leq\beta(i)\leq1$ |
| 17 | HAP power satisfies $0\leq P^{HAP}(i)\leq P_{max}^{HAP}$ |

**Algorithm**: Transform Q into an MDP whose state contains channel gains, remaining battery energy, and current data-rate demand; choose continuous $(\alpha(i),\beta(i))$ actions; shape reward from scale-demand ratio so meeting the rate earns positive reward and excess allocation or failure is penalized; train the clipped-surrogate PPO actor and critic and execute the learned DRL-HUES policy slot by slot.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Hsu et al. [x] studied joint HAP uplink transmission and RF energy-harvesting scheduling in a NOMA space-air-ground integrated network. They formulated an NP-hard nonlinear program that maximizes long-term average binary scale satisfaction over the transmission-time share and HAP power ratio under battery recursion, available-energy, time-share, and transmit-power constraints. Their DRL-HUES scheme models stochastic channel, demand, and battery state as an MDP and trains a PPO policy for continuous scheduling actions. Simulations show higher long-term average binary scale satisfaction than the evaluated No-Pain-No-Gain, random, and greedy schedulers.

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
