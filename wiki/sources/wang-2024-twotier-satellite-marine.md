---
type: source
modeling_card: required
title: "Two-Tier Task Offloading for Satellite-Assisted Marine Networks: A Hybrid Stackelberg-Bargaining Game Approach"
authors: ["Zhen Wang", "Bin Lin", "Qiang Ye", "Haixia Peng"]
year: 2024
url: "https://doi.org/10.1109/JIOT.2024.3523527"
venue: "IEEE Internet of Things Journal (IEEE IoT-J)"
tags: [source, maritime-mec, satellite, stackelberg-game, bargaining-game, noma, task-offloading, two-tier]
related:
  - "[[maritime-mec]]"
  - "[[leo-satellite-edge-computing]]"
  - "[[stackelberg-game]]"
  - "[[bargaining-game]]"
  - "[[noma]]"
  - "[[task-offloading]]"
  - "[[wang-2025-double-edge-samin]]"
  - "[[you-2025-uncertain-maritime-hasac]]"
  - "[[sun-2023-bargain-match-vec]]"
created: 2026-05-29
updated: 2026-07-16
---

# Two-Tier Task Offloading for Satellite-Assisted Marine Networks: A Hybrid Stackelberg-Bargaining Game Approach

## Citation

Wang, Z., Lin, B., Ye, Q., & Peng, H. (2024). *Two-Tier Task Offloading for Satellite-Assisted Marine Networks: A Hybrid Stackelberg-Bargaining Game Approach*. **IEEE Internet of Things Journal**. DOI: 10.1109/JIOT.2024.3523527.

## TL;DR

A two-tier task-offloading scheme for **satellite-assisted marine MEC** using a hybrid **Stackelberg + Bargaining game**. Underwater, autonomous underwater vehicles (AUVs) upload data to maritime autonomous surface ships (MASSs) over acoustic links using **NOMA**; above the sea surface, a LEO satellite (LEOS) acts as a space edge server reached by MASSs via FDMA. AUV↔MASS offloading is a **Stackelberg game** (AUV strategy + MASS pricing); MASS↔LEOS offloading is a **Bargaining game** (bidding strategies). The aim is to maximize the utility of marine devices.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Underwater AUVs upload computation workloads to MASSs through acoustic NOMA, while MASSs may offload workloads to a LEO satellite through FDMA; AUVs, MASSs, and the satellite have separate utilities and energy costs.

**Problem & objective**: The two-tier game solves utility maximization for the three parties, represented by $\max\{Z_i(a_{i,m},k_i),Z_m(k_i,b_{i,n}),Z_n(b_{i,n})\}$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| AUV offloading ratio | $a_{i,m}$ | continuous, $0\leq a_{i,m}\leq1$ | Fraction sent from AUV $i$ to MASS $m$ |
| MASS price | $k_i$ | continuous, $0\leq k_i\leq k_i^{max}$ | Price per processed data unit |
| MASS to LEOS ratio | $b_{i,n}$ | continuous, $0\leq b_{i,n}\leq1$ | Fraction sent from MASS $m$ to LEOS $n$ |
| Bargaining share | $\eta_i$ | continuous, $[0,1]$ | Distribution weight in the transaction |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | AUV offloading ratio is bounded: $0\leq a_{i,m}\leq1$. |
| C2 | AUV computation and transmission energy stays below $E_i^{max}$. |
| C3 | AUV task completion time meets the coverage bound: $T_i^{tot}\leq T^{max}$. |
| C4 | AUV, MASS, and LEOS utilities are nonnegative. |
| C5 | MASS price is bounded: $0\leq k_i\leq k_i^{max}$. |
| C6 | MASS to LEOS offloading ratio is bounded: $0\leq b_{i,n}\leq1$. |
| C7 | MASS and LEOS energy budgets are respected. |

**Algorithm**: Solve the AUV and MASS Stackelberg subgames with binary search and linear search, solve the MASS-LEOS bargaining equilibrium, and combine the equilibria in the two-tier task-offloading algorithm.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Wang et al. [x] model satellite-assisted marine offloading as a two-tier incentive system linking AUVs, MASSs, and a LEO edge server. The Stackelberg tier jointly selects AUV offloading ratios and MASS prices under energy, delay, price, and nonnegative-utility constraints, while the bargaining tier selects MASS to satellite ratios and a surplus share. Binary search, linear search, and a bargaining equilibrium are combined into the two-tier task-offloading algorithm. The reported experiments show convergence to stable utility or offloading values and higher utility than the benchmark bargaining and pricing settings.

## Problem framing

Marine devices are rational, selfish, and compute-limited, so incentives are needed to make them participate in task processing. The architecture spans underwater (acoustic, interference-prone → NOMA) and above-surface (FDMA to avoid co-channel interference) tiers, each calling for a different game.

## System model

- **Tier 1 (underwater).** Multiple AUVs (managed by MASSs) upload via underwater acoustic NOMA ([[noma]]).
- **Tier 2 (above surface).** MASS offloads to a LEOS (space edge server) via FDMA.
- **Utilities** defined for AUVs, MASSs, and LEOSs.

## Method

- **AUV↔MASS:** [[stackelberg-game|Stackelberg game]] — optimize AUV offloading strategy and MASS pricing.
- **MASS↔LEOS:** [[bargaining-game|Bargaining game]] — optimize bidding strategies for both.
- Efficient algorithms refine offloading, pricing, and bidding.

## Key findings

- Simulations show the algorithms significantly outperform benchmark schemes in achieving optimal solutions (qualitative; specific curves in the paper).

## Limitations / future work

Future work: efficient resource management for satellite-marine integrated networks, and DRL-based intelligent algorithms to improve adaptability of offloading decisions in dynamic marine environments.

## Relation to the corpus

A **game-theoretic maritime offloading** entry whose Stackelberg+bargaining hybrid mirrors the bargaining+matching structure of [[sun-2023-bargain-match-vec]] and contrasts with the optimization-based [[wang-2025-double-edge-samin]] and DRL-based [[you-2025-uncertain-maritime-hasac]] treatments of maritime offloading (all three Wang/Lin/Ye papers share co-authors). Connects to [[stackelberg-game]], [[bargaining-game]], [[noma]], and [[leo-satellite-edge-computing]].

## Raw artifacts

- `raw/sources/Two-Tier_Task_Offloading_for_Satellite-Assisted_Marine_Networks_A_Hybrid_StackelbergBargaining_Game_Approach/full.md`
- Original PDF and extracted figures in the same folder.
