---
type: source
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
updated: 2026-06-09
---

# Optimizing Spectrum Sharing in UAV Swarms: A Stackelberg Game-Based Incentive Mechanism

## Citation

Wang, Q., Shen, Y., Xu, L., Zhang, H., Zhao, H., & Zhu, H. (2025). *Optimizing Spectrum Sharing in UAV Swarms: A Stackelberg Game-Based Incentive Mechanism*. **IEEE Transactions on Vehicular Technology**. DOI: 10.1109/TVT.2025.3595972.

## TL;DR

Game-theoretic incentive mechanism for UAV-to-UAV (U2U) spectrum sharing within a swarm where one UAV-to-base-station (U2B) link is the primary user. Multiple U2U links want to use the U2B's spectrum without unduly interfering with it. Two-level approach:

1. **Hybrid [[overlay-underlay-spectrum-access|overlay-underlay]]** access mode — U2U uses the U2B's idle slots overlay-style and falls back to underlay (low-power coexistence) when U2B is active. Reduces inter-user interference vs pure overlay or pure underlay.
2. **[[stackelberg-game|Stackelberg game]]** with U2B as leader (sets a price for spectrum access) and U2U links as followers (decide power and access duration to maximize utility minus payment). Equilibrium found via backward induction.
3. **[[matching-theory-for-resource-allocation|Matching algorithm]]** assigns specific U2U links to specific U2B sub-bands when there are multiple U2U-U2B candidate pairings.

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
