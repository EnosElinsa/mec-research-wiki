---
type: source
modeling_card: required
title: "A Three-Party Hierarchical Game for Physical Layer Security Aware Wireless Communications With Dynamic Trilateral Coalitions"
authors: ["Ruoyang Chen", "Changyan Yi", "Kun Zhu", "Bing Chen", "Jun Cai", "Mohsen Guizani"]
year: 2024
url: "https://doi.org/10.1109/TWC.2023.3322776"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, physical-layer-security, hierarchical-game, coalition-formation-game, friendly-jamming, drl, stackelberg-game]
related:
  - "[[physical-layer-security]]"
  - "[[coalition-formation-game]]"
  - "[[stackelberg-game]]"
  - "[[friendly-jamming-uav]]"
  - "[[nash-equilibrium]]"
  - "[[yao-2025-secure-isac-dual-eavesdropping]]"
  - "[[zhang-2024-gdmtd3-aerial-secure-cb]]"
  - "[[bi-2025-sg-mapg]]"
created: 2026-05-31
updated: 2026-07-16
---

# A Three-Party Hierarchical Game for Physical Layer Security Aware Wireless Communications With Dynamic Trilateral Coalitions

## Citation

Chen, R., Yi, C., Zhu, K., Chen, B., Cai, J., & Guizani, M. (2024). *A Three-Party Hierarchical Game for Physical Layer Security Aware Wireless Communications With Dynamic Trilateral Coalitions*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2023.3322776.

## TL;DR

A **hierarchical game** framework for **physical-layer-security (PLS)**-aware uplink communications with **dynamic trilateral coalitions** among three selfish parties: legitimate users (LUs) sending secret data to base stations, eavesdroppers (EVs), and jammers (JAs) who may ally with **either** LUs (to raise secrecy rate) or EVs (to raise eavesdropping rate) in exchange for rewards. Unlike prior PLS work with fixed ally-adversary relationships, the coalitions here can merge and split over time. The paper proposes a **hedonic coalition selection and formation (HCSF)** algorithm for a stable per-slot coalition partition, proves the hierarchical game converges to an equilibrium, and adds a **DRL-based solution** for long-term performance across time slots.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: In a slotted uplink network, legitimate users transmit confidential data to associated base stations, eavesdroppers activate at different locations, and jammers choose discrete power and may dynamically ally with either legitimate users or eavesdroppers under time-varying channels.

**Problem & objective**: The three parties solve coupled long-term utility problems of the form $\arg\max_{\pi_i}\lim_{T\to\infty}\frac{1}{T}\sum_{t\in[0,T]}U_i(t)$ for $i\in\{\mathcal K,\mathcal N,\mathcal J\}$, balancing security or eavesdropping gains, incentives, power costs, activation costs, and coalition reconfiguration costs.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Eavesdropper activation | $x_k^{sw}(t)$ | Binary, $\{0,1\}$ | Activates eavesdropper $k$ at its current location. |
| Eavesdropper incentive | $\mu_E(t)$ | Continuous, $[0,\mu_E^{\max}]$ | Unit reward offered to attract jammer cooperation. |
| User association and power | $x_{nm}^T(t),P_n^T(t)$ | Binary association and finite power levels | Selects one receiving base station and a transmit-power level for user $n$. |
| User incentive | $\mu_L(t)$ | Continuous, $[0,\mu_L^{\max}]$ | Unit reward offered by legitimate users to jammers. |
| Jammer coalition and power | $x_{\{EJ\}}(t),x_{\{LJ\}}(t),P_j^J(t)$ | Binary coalition choices and finite power levels | Chooses one ally at most and allocates jamming power. |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Every legitimate link satisfies $R_{nm}^T(t)\ge R_{\min}^T$. |
| C2 | Base-station association is binary and exclusive, $\sum_mx_{nm}^T(t)=1$. |
| C3 | Incentives lie in their bounded intervals and user and jammer powers come from their prescribed $l$-level sets. |
| C4 | Jammers can ally with at most one side, $x_{\{EJ\}}(t)+x_{\{LJ\}}(t)\le1$. |
| C5 | Coalition changes incur $c_{conf}\mathcal F(t)$, coupling consecutive time slots. |

**Algorithm**: HCSF performs hedonic coalition selection, merge, and split operations to reach a stable per-slot partition, after which a PPO-based multi-agent DRL construction learns the parties' mixed strategies over repeated time slots.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Chen et al. [x] studied physical-layer-secure uplink communication with strategic legitimate users, eavesdroppers, and jammers that can dynamically change allies. They formulated a repeated three-stage hierarchical game in which the parties maximize long-term utilities over activation, association, incentives, discrete transmission or jamming power, and unilateral jammer coalition choices under secrecy and QoS constraints. Their HCSF procedure finds a stable coalition partition in each slot, and a PPO-based DRL solution learns the mixed-strategy equilibrium across time-varying channels. Simulations show rapid convergence and higher cumulative utilities than fixed legitimate-friendly or eavesdropper-friendly jamming schemes implemented with DRL or particle swarm optimization.

## Problem framing

Most PLS work ignores that all three parties (LUs, EVs, JAs) may behave strategically and that their interests are sometimes mutually beneficial — JAs can be incentivized by LUs (cooperative jamming) or by EVs (jam LUs to force higher transmit power). Prior coalition studies fixed these alliances; in reality the coalition structure is not pre-defined and evolves under wireless uncertainties (e.g. time-varying channels), requiring a dynamic, hierarchical, multi-time-slot treatment.

## System model

- **Parties.** LUs (uplink secret transmission to associated BSs), EVs (eavesdroppers, may be active/inactive at different locations), JAs (allocate jamming power, choose an ally).
- **Decision sequence (hierarchy).** EVs first decide active/inactive status and the unit incentive to stimulate JAs; then LUs decide BS associations, transmit-power allocations, and their competing incentive for JA help; then JAs decide their ally (LUs or EVs) and jamming-power allocations.
- **Coalition layer.** An underlying **coalition formation game (CFG)** in which any two of the three parties may temporarily form coalitions and dynamically merge/split across time slots ([[coalition-formation-game]]).
- **Dynamics.** Time-varying channel conditions make the strategies (and the CFG) evolve, motivating long-term optimization.

## Method

- **HCSF algorithm.** A hedonic coalition selection and formation procedure that reaches a **stable coalition partition** each time slot; its feasibility (existence of a stable partition) is proven.
- **Hierarchical-game equilibrium.** The paper defines and theoretically analyzes the equilibrium, showing the overall hierarchical game converges to it under HCSF.
- **DRL-based solution.** A deep-reinforcement-learning solver derives the equilibrium with long-term performance guarantees across multiple time slots with dynamic coalition evolution.

## Key findings

- A stable coalition partition provably exists for the underlying CFG, and applying HCSF drives the hierarchical game to an equilibrium.
- The DRL-based solution produces the equilibrium strategic decisions over multiple time slots and, in simulations, shows superiority over its counterparts (qualitative; specific curves in the paper).

## Limitations / future work

The parse's contribution section does not enumerate explicit limitations; evaluation is simulation-based.

## Relation to the corpus

A **game-theoretic PLS** entry that extends the wiki's [[physical-layer-security]] and game-theory threads with a three-party, dynamically-coalitional twist. It complements the secure-beamforming / friendly-jamming sources [[zhang-2024-gdmtd3-aerial-secure-cb]] and [[yao-2025-secure-isac-dual-eavesdropping]] (which treat eavesdroppers and jamming) and the hierarchical-Stackelberg formulation [[bi-2025-sg-mapg]] (multi-layer games solved with DRL). Introduces [[coalition-formation-game]] as new vocabulary; reinforces [[stackelberg-game]] and [[friendly-jamming-uav]].

## Raw artifacts

- `raw/sources/A_Three-Party_Hierarchical_Game_for_Physical_Layer_Security_Aware_Wireless_Communications_With_Dynamic_Trilateral_Coalitions/full.md`
- Original PDF and extracted figures in the same folder.
