---
type: comparison
title: "Game-theoretic offloading formulations: potential vs Stackelberg vs bargaining vs matching"
tags: [comparison, game-theory, offloading, mec]
related:
  - "[[chen-2024-ulse-game]]"
  - "[[he-2019-euagame-user-allocation]]"
  - "[[li-2025-stochastic-game-uav-swarm]]"
  - "[[wang-2025-uav-swarm-stackelberg]]"
  - "[[bi-2025-sg-mapg]]"
  - "[[sun-2023-bargain-match-vec]]"
  - "[[wang-2024-twotier-satellite-marine]]"
  - "[[sun-2024-mvtora-postdisaster-vfc]]"
  - "[[potential-game]]"
  - "[[stackelberg-game]]"
  - "[[bargaining-game]]"
  - "[[stochastic-game]]"
  - "[[matching-theory-for-resource-allocation]]"
  - "[[nash-equilibrium]]"
created: 2026-05-30
updated: 2026-06-07
---

# Game-theoretic offloading formulations: potential vs Stackelberg vs bargaining vs matching

A cluster of curated sources cast MEC offloading / resource allocation as a game. They span four distinct game families, each chosen for a structural reason. This page maps the formulation to the problem shape it fits — using the eight sources tabulated below as representatives — so the comparison distinguishes the equilibrium structure rather than defaulting to "a game". (Other curated sources also use a game formulation, e.g. [[zeng-2024-usv-fleet-collaborative-offloading]] (Stackelberg) and [[you-2025-uncertain-maritime-hasac]] (Markov game); the track is broader than this roster.)

## Roster

| Source | Venue / year | Game family | Players / roles | Solution concept |
|---|---|---|---|---|
| [[he-2019-euagame-user-allocation]] | TPDS 2019 | [[potential-game]] | Users competing for edge servers | Decentralized [[nash-equilibrium]] |
| [[chen-2024-ulse-game]] | TMC 2024 | [[potential-game]] | Users offloading to UAV/LEO | NE via distributed best-response (JULTO) |
| [[sun-2024-mvtora-postdisaster-vfc]] | TMC 2024 | [[potential-game]] (+ convex + evolutionary) | Vehicles + aerial-terrestrial nodes | NE + convex/evolutionary refinement (MVTORA) |
| [[li-2025-stochastic-game-uav-swarm]] | TGCN 2025 | [[stochastic-game]] | UAV swarm (dynamic clusters) | RL-based equilibrium (RLDC Q-learning) |
| [[wang-2025-uav-swarm-stackelberg]] | TVT 2025 | [[stackelberg-game]] + [[matching-theory-for-resource-allocation\|matching]] | U2B leaders, U2U followers | Stackelberg equilibrium + utility matching |
| [[bi-2025-sg-mapg]] | (venue not in parse) 2025 | [[stackelberg-game]] (3-layer) + auction | Operator / UAV / user layers | Stackelberg eq. approximated by MA policy gradient |
| [[wang-2024-twotier-satellite-marine]] | IoT-J 2024 | Hybrid [[stackelberg-game\|Stackelberg]]-[[bargaining-game\|Bargaining]] | Satellite leader, marine followers | Stackelberg price + Nash bargaining split |
| [[sun-2023-bargain-match-vec]] | TMC 2023 | [[bargaining-game]] + [[matching-theory-for-resource-allocation\|matching]] | Vehicles + edge servers | Intra-server bargaining + inter-server matching |

## When to pick which family

### Potential games — symmetric competition with a guaranteed NE

[[he-2019-euagame-user-allocation]], [[chen-2024-ulse-game]], and [[sun-2024-mvtora-postdisaster-vfc]] all use potential games because the problem is **symmetric self-interested competition** (users/vehicles each minimizing their own cost) and the existence of an exact potential function **guarantees a pure Nash equilibrium reachable by best-response**. The payoff: a fully decentralized algorithm with provable convergence and no central controller — exactly what you want when the players are independent edge clients. [[chen-2024-ulse-game]]'s JULTO and [[he-2019-euagame-user-allocation]]'s decentralized NE algorithm are the canonical examples.

### Stackelberg games — asymmetric leader/follower with pricing/incentives

[[wang-2025-uav-swarm-stackelberg]], [[bi-2025-sg-mapg]], and (in hybrid form) [[wang-2024-twotier-satellite-marine]] use Stackelberg because the problem has a **natural hierarchy**: a resource owner (U2B link / network operator / satellite) sets a price or policy, and followers (U2U links / UAVs / vessels) best-respond. The leader anticipates the followers' reaction. This is the right model whenever there's an **incentive-design** angle — getting selfish followers to participate by pricing the shared resource.

### Bargaining games — cooperative surplus splitting

[[sun-2023-bargain-match-vec]] and the bargaining half of [[wang-2024-twotier-satellite-marine]] use Nash bargaining because the parties are **cooperating to split a surplus** (e.g. how to divide the gains from an offloading deal) rather than purely competing. Bargaining gives a fairness-flavored split (Nash bargaining solution) that a pure auction wouldn't.

### Stochastic games — multi-stage with state dynamics

[[li-2025-stochastic-game-uav-swarm]] uses a stochastic (Markov) game because the UAV-swarm problem is **multi-stage with evolving state** (cluster membership, energy, queues change over time). A one-shot game can't capture the temporal coupling; the stochastic game is solved with multi-agent RL (RLDC Q-learning), which is where game theory meets the DRL track.

## Matching as the recurring companion

Three sources pair their game with **matching theory** ([[wang-2025-uav-swarm-stackelberg]], [[bi-2025-sg-mapg]], [[sun-2023-bargain-match-vec]]). The pattern: the game sets prices / surplus splits (the "how much"), and a matching algorithm decides the assignment (the "who pairs with whom"). Matching handles the combinatorial assignment that a pricing game leaves underdetermined. See [[matching-theory-for-resource-allocation]].

## Cross-cutting observations

1. **Decentralization is the shared motivation.** Every source here chose a game over a centralized optimizer because the players are independent and a central solver is impractical (no trusted coordinator, privacy, or scale). The price is optimality: NE/Stackelberg equilibria are generally not the social optimum.
2. **Hybrids dominate the newer sources.** The 2024–2025 sources combine a game with another solver — Stackelberg+matching, bargaining+matching, Stackelberg+bargaining, or potential-game+convex+evolutionary. Pure single-game formulations are the older/simpler ones ([[he-2019-euagame-user-allocation]]).
3. **Stochastic games bridge to DRL.** [[li-2025-stochastic-game-uav-swarm]] is the connective tissue between this comparison and [[drl-backbones-across-uav-mec-sources]] / [[maddpg-vs-masac-in-mec]] — the equilibrium is *learned*, not solved in closed form.

## Gaps

- **No source quantifies the price of anarchy** — i.e. how far the equilibrium sits from the centralized social optimum. This is the obvious missing measurement across the whole game-theoretic track.
- **No head-to-head** between a game-theoretic decentralized solver and a centralized DRL/convex solver on the same instance.
