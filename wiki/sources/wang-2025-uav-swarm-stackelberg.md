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
updated: 2026-07-16
---

# Optimizing Spectrum Sharing in UAV Swarms: A Stackelberg Game-Based Incentive Mechanism

## Citation

Wang, Q., Shen, Y., Xu, L., Zhang, H., Zhao, H., & Zhu, H. (2025). *Optimizing Spectrum Sharing in UAV Swarms: A Stackelberg Game-Based Incentive Mechanism*. **IEEE Transactions on Vehicular Technology**. DOI: 10.1109/TVT.2025.3595972.

## TL;DR

Game-theoretic incentive mechanism for UAV-to-UAV (U2U) spectrum sharing within a swarm where one UAV-to-base-station (U2B) link is the primary user. Multiple U2U links want to use the U2B's spectrum without unduly interfering with it. Two-level approach:

1. **Hybrid [[overlay-underlay-spectrum-access|overlay-underlay]]** access mode — U2U uses the U2B's idle slots overlay-style and falls back to underlay (low-power coexistence) when U2B is active. Reduces inter-user interference vs pure overlay or pure underlay.
2. **[[stackelberg-game|Stackelberg game]]** with U2B as leader (sets a price for spectrum access) and U2U links as followers (decide power and access duration to maximize utility minus payment). Equilibrium found via backward induction.
3. **[[matching-theory-for-resource-allocation|Matching algorithm]]** assigns specific U2U links to specific U2B sub-bands when there are multiple U2U-U2B candidate pairings.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A UAV swarm contains primary UAV-to-BS links and secondary UAV-to-UAV links. A secondary link can use idle primary slots in overlay mode or transmit at controlled power during active primary slots in underlay mode, with multiple candidate primary sub-bands assigned by matching.

**Problem & objective**: A hierarchical Stackelberg spectrum-trading game lets each primary leader maximize its access revenue and link utility while each secondary follower maximizes net transmission utility, $\max_{\pi}U_{\mathrm{U2B}}(\pi)$ and $\max_{p_i,\tau_i}\bigl(U_i-\mathrm{payment}_i\bigr)$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Spectrum price | $\pi_j$ | continuous, nonnegative | Price announced by primary U2B link $j$ |
| U2U transmit power | $p_i$ | continuous, bounded | Underlay power selected by secondary U2U link $i$ |
| Access duration | $\tau_i$ | continuous, slot-bounded | Overlay or underlay access time purchased by U2U link $i$ |
| Spectrum matching | $x_{i,j}$ | binary | Whether U2U link $i$ uses U2B sub-band $j$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | U2U powers and access durations satisfy their box and slot limits |
| C2 | Underlay interference preserves the primary U2B quality-of-service requirement |
| C3 | Overlay access uses only primary idle time and underlay access uses active time |
| C4 | Each U2U-U2B assignment satisfies the matching quotas and preference rules |
| C5 | Leader and follower choices satisfy their Stackelberg best-response conditions |

**Algorithm**: Separate overlay and underlay access opportunities → derive follower power and duration best responses → optimize the primary leader's price by backward induction → compute the Stackelberg equilibrium → assign multiple U2U links to U2B sub-bands with deferred-acceptance matching.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Wang et al. [x] studied spectrum sharing between primary UAV-to-base-station links and secondary UAV-to-UAV links in a UAV swarm. They proposed a hybrid overlay and underlay access mode that uses primary idle periods and controlled concurrent transmission. A Stackelberg game lets each primary link set a spectrum price while secondary links select transmit power and access duration to maximize their net utilities. Backward induction derives the leader and follower equilibrium, and a deferred-acceptance matching procedure assigns secondary links to candidate primary sub-bands. Simulations show higher spectrum utilization and utility than the evaluated pure-overlay, pure-underlay, and allocation baselines.

## Why this matters for MEC

The paper is not strictly MEC, but it sits in the **wireless infrastructure layer** that any UAV-MEC system depends on. If the UAV swarm can't share spectrum efficiently, computation offloading at the upper layer is bandwidth-starved. Future MEC papers that assume "abundant U2U bandwidth" effectively assume a working scheme like this.

The Stackelberg + matching pattern also recurs in the corpus — [[liu-2026-jppo-en-convntm]] mentions Stackelberg-based UAV resource pricing in adjacent work, and the low-altitude-economy survey [[wang-2025-lae-network-survey]] revisits it.

## Findings

- Hybrid overlay-underlay outperforms pure overlay (under-utilizes idle slots) and pure underlay (worst PU interference).
- The Stackelberg equilibrium gives the U2B an incentive-compatible pricing scheme — U2U honestly reports demand because misreporting hurts their own utility.
- Matching at scale (many U2U-to-U2B candidate pairings) is solved with a deferred-acceptance variant.

## Limitations / future work

- Assumes the U2B is willing to share — no analysis of operator-side trust or settlement.
- Does not jointly model the *compute* layer of the swarm — pure communication paper.
- The Stackelberg interaction is modeled around U2B/U2U trading roles rather than operator-level multi-market competition.

## Cross-link with related sources

- This is the **wireless-foundations** track in the wiki — adjacent to but distinct from the **compute-offloading** track that [[mao-2025-bcsa-frl]], [[qin-2025-bcuav-masac]], etc. live in.
- Connects to [[low-altitude-intelligent-network]], which the low-altitude-economy survey [[wang-2025-lae-network-survey]] defines more fully.

## Raw artifacts

- `raw/sources/Optimizing_Spectrum_Sharing_in_UAV_Swarms_A_Stackelberg_Game-Based_Incentive_Mechanism/full.md`
- Original PDF and extracted figures in the same folder.
