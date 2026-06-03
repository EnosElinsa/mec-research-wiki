---
type: concept
title: "Overlap-Based Multihop Routing Protocol (OMRP)"
tags: [iot, routing, clustering, wireless-sensor-network, energy-efficiency, spatial-correlation]
related:
  - "[[collaborative-beamforming]]"
  - "[[hot-spot-problem-iot]]"
  - "[[first-order-radio-energy-model]]"
  - "[[softppo-lstm]]"
  - "[[load-balancing-uav-mec]]"
  - "[[li-2025-omrp-cb-iot]]"
created: 2026-06-03
updated: 2026-06-03
---

# Overlap-Based Multihop Routing Protocol (OMRP)

OMRP is a hierarchical clustering routing protocol for IoT / wireless-sensor networks that uses the **sensing-area overlap degree** ρ as the primary signal for its topology decisions: cluster-head (CH) election, intra-cluster TDMA scheduling, and inter-cluster relay-vs-direct routing. It is proposed in [[li-2025-omrp-cb-iot]] as the routing half of a joint routing + collaborative-beamforming framework.

## Overlap degree
For node i with sensing area Aᵢ and neighbor list Fᵢ (nodes j with dᵢⱼ < 2r):

> ρᵢ = (1/Aᵢ) Σⱼ∈Fᵢ |Aᵢ ∩ Aⱼ|, with 0 ≤ ρᵢ ≤ 1.

A high-ρ node has its sensing area largely covered by neighbors — its data is more redundant, and it tends to be geographically central (more neighbors → near a cluster center).

## Cluster-head election
OMRP extends the LEACH threshold function:

> T(i) = [P / (1 − P·(r mod 1/P))] · Kρᵢ, for eligible nodes,

where P is the lower-bound CH fraction and K ≥ 1 is an amplification factor. The Kρᵢ multiplier biases election toward high-overlap (central) nodes, reducing cluster-member transmission distances and thus energy.

## TDMA scheduling by overlap order
A CH sorts member JOIN_IN messages by ρ **descending** before broadcasting the TDMA slot schedule, so nodes with more redundant data transmit and are fused first. After each fusion the accumulated packet shrinks, lowering energy for subsequent hops.

## Relay vs. direct
For a CH communicating to the sink, OMRP uses the distance factor

> βᵢⱼ = dᵢₛ² − dᵢⱼ² − dⱼₛ²,

and prefers relay via node j when βmax > 2Eelec/εfs (the energy saved by shorter hops exceeds the extra receive overhead).

## Reported benchmark comparisons
On a 400-node, 200 m × 200 m simulation against PEGASIS, LEACH, D2CRP, and IGHND, [[li-2025-omrp-cb-iot]] reports OMRP reaching FND/HND/AND of 271/624/870 rounds (vs. LEACH 187/473/733), a ~17% network-lifetime improvement over benchmark routing protocols, an FND–HND energy-consumption rate ~6%/12%/20%/92% below IGHND/D2CRP/LEACH/PEGASIS, and stronger data-perception maintenance (608/674/723 rounds to retain 75%/50%/25% perception).

## Relationship to other concepts
- OMRP feeds its output (data fused at the sink node) into [[softppo-lstm]] for CB node selection.
- Its overlap-driven CH election uses geometry rather than residual energy as the election signal.
- It mitigates the [[hot-spot-problem-iot]] by routing relay load through geometrically central CHs instead of nodes nearest the BS.
- All of its energy calculations rest on the [[first-order-radio-energy-model]].
