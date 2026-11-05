---
type: source
modeling_card: required
title: "Optimizing Spectrum Sharing in UAV Swarms: A Stackelberg Game-Based Incentive Mechanism"
authors: ["Qin Wang", "Yi Shen", "Longting Xu", "Hui Zhang", "Haitao Zhao", "Hongbo Zhu"]
year: 2025
url: "https://doi.org/10.1109/TVT.2025.3595972"
venue: "IEEE Transactions on Vehicular Technology"
tags: [source, uav, swarm, spectrum-sharing, stackelberg, game-theory, low-altitude, cognitive-radio, matching]
related:
  - "[[stackelberg-game]]"
  - "[[overlay-underlay-spectrum-access]]"
  - "[[matching-theory-for-resource-allocation]]"
  - "[[low-altitude-intelligent-network]]"
  - "[[multi-uav-assisted-mec]]"
created: 2026-05-28
updated: 2026-11-03
---

# Optimizing Spectrum Sharing in UAV Swarms: A Stackelberg Game-Based Incentive Mechanism

## Citation

Wang, Q., Shen, Y., Xu, L., Zhang, H., Zhao, H., & Zhu, H. (2025). *Optimizing Spectrum Sharing in UAV Swarms: A Stackelberg Game-Based Incentive Mechanism*. **IEEE Transactions on Vehicular Technology**. DOI: 10.1109/TVT.2025.3595972.

## TL;DR

Game-theoretic incentive mechanism for UAV-to-UAV (U2U) spectrum sharing in a swarm whose UAV-to-base-station (U2B) links are the primary users. Multiple U2U links buy resource blocks (RBs) of a U2B link's reusable sub-band. Three parts:

1. **Hybrid [[overlay-underlay-spectrum-access|overlay-underlay]]** access mode — every U2U link reuses the U2B spectrum as underlay, with transmit power below an interference threshold, while U2U links sharing one U2B link occupy mutually orthogonal RBs (overlay among themselves), so they need no spectrum sensing or mutual negotiation.
2. **[[stackelberg-game|Stackelberg game]]** with each U2B link as leader (sets the unit RB price, P0) and U2U links as followers (choose how many RBs to buy, P1, weighting urgency-scaled capacity and a QoS-based satisfaction term against the payment). The unique equilibrium is found by backward induction.
3. **[[matching-theory-for-resource-allocation|Utility-based matching]]** assigns U2U links to U2B sub-bands: U2U links propose to their highest-utility U2B link, and a U2B link without enough RBs keeps its highest-ranked requesters and rejects the rest.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A BS and a UAV swarm form a cellular network with $I$ primary UAV-to-BS (U2B) links and $J$ secondary UAV-to-UAV (U2U) links over Rician channels. Each U2B link divides its reusable sub-band into orthogonal resource blocks (RBs); U2U links buy RBs and access them in the hybrid mode, underlay with respect to the U2B link (transmit power below an interference threshold) and overlay among U2U links (orthogonal RBs, no mutual interference).
**Problem & objective**: A two-stage Stackelberg game: each U2B leader solves P0 (11), $\max_{p_j^i}U_i=A\,n_j^ib_{RB}/b_j^{QoS}+p_j^in_j^i-C_T$ s.t. $p_j^i\ge0$, and each U2U follower solves P1 (15), $\max_{n_j^i}U_j=\omega_j\gamma C_j^i+S_j^i-p_j^in_j^i$, where $S_j^i$ (12) penalizes deviation from the QoS bandwidth and $\omega_j$ is task urgency; the equilibrium is (16)–(17).
**Decision variables**:
| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| RB unit price | $p_j^i$ | continuous, $\ge0$ | Price set by U2B link $i$ for U2U link $j$ |
| Traded RBs | $n_j^i$ | nonnegative | RBs bought by U2U link $j$ from U2B link $i$ |
| Matching | $\rho_{i,j}$ | binary | U2U link $j$ shares the sub-band of U2B link $i$ |
**Constraints**:
| ID | Meaning and key expression |
|---|---|
| (11) | Leader price is nonnegative: $p_j^i\ge0$ |
| (15), 1st–2nd lines | Follower demand: $n_{i,j}\ge0$ and the matched U2U links fit the sub-band, $\sum_j\rho_{i,j}n_j^ib_{RB}\le B_i$ |
| (15), 3rd line | Urgency bounds: $\omega_{\min}\le\omega_j\le\omega_{\max}$ |
| Model rule | Underlay U2U transmit power stays below the U2B interference threshold |
**Algorithm**: Derive the follower best response $n_j^{i*}$ and the leader price $p_j^{i*}$ by backward induction (16)–(17) → form preference lists from the equilibrium utilities → run the utility-based matching (Algorithm 1), in which U2U links propose to their top U2B link and U2B links with insufficient RBs keep their highest-ranked requesters and reject the rest, until no requests remain.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Wang et al. [x] studied spectrum sharing between primary UAV-to-base-station links and secondary UAV-to-UAV links in a UAV swarm. They proposed a hybrid access mode in which secondary links access primary resource blocks in underlay mode, below an interference threshold, and share orthogonal blocks with one another in overlay mode. A Stackelberg game lets each primary link set a spectrum price while secondary links choose how many resource blocks to buy, weighting capacity by task urgency against a QoS-based satisfaction term. Backward induction derives the leader and follower equilibrium, and a utility-based propose-and-reject matching procedure assigns secondary links to candidate primary sub-bands. With 30 U2U links, simulations report system utility 90.53%, 26.99%, and 276.55% higher than fixed pricing (FP), reverse-auction RAIM, and fairness-oriented DOAF, respectively.

## Why this matters for MEC

The paper is not strictly MEC, but it sits in the **wireless infrastructure layer** that any UAV-MEC system depends on. If the UAV swarm can't share spectrum efficiently, computation offloading at the upper layer is bandwidth-starved. Future MEC papers that assume "abundant U2U bandwidth" effectively assume a working scheme like this.

The Stackelberg + matching pattern also recurs in the corpus; see [[game-theoretic-offloading-formulations]].

## Findings

- With 30 U2U links, system utility is 90.53%, 26.99%, and 276.55% higher than fixed pricing (FP), reverse-auction RAIM, and fairness-oriented Stackelberg DOAF, respectively.
- The follower problem has a unique optimal RB amount under the stated conditions, so backward induction yields a unique Stackelberg equilibrium.
- The paper does not compare the hybrid mode against pure overlay or pure underlay; its baselines differ in pricing and allocation, not in access mode.

## Limitations / future work

- Assumes the U2B is willing to share — no analysis of operator-side trust or settlement.
- Does not jointly model the *compute* layer of the swarm — pure communication paper.
- The Stackelberg interaction is modeled around U2B/U2U trading roles rather than operator-level multi-market competition.

## Cross-link with related sources

- This is the **wireless-foundations** track in the wiki — adjacent to but distinct from the **compute-offloading** track that [[mao-2025-bcsa-frl]], [[qin-2025-bcuav-masac]], etc. live in.
- Connects to [[low-altitude-intelligent-network]], which the low-altitude-economy survey [[wang-2025-lae-network-survey]] defines more fully.

## Raw artifacts

- `raw/sources/Optimizing_Spectrum_Sharing_in_UAV_Swarms_A_Stackelberg_Game-Based_Incentive_Mechanism/Optimizing_Spectrum_Sharing_in_UAV_Swarms_A_Stackelberg_Game-Based_Incentive_Mechanism.md`
- Original PDF and extracted figures in the same folder.
