---
type: source
title: "Blockchain-Integrated UAV-Assisted Mobile Edge Computing: Trajectory Planning and Resource Allocation"
authors: ["Die Wang", "Yunjian Jia", "Mianxiong Dong", "Kaoru Ota", "Liang Liang"]
year: 2024
url: "https://doi.org/10.1109/TVT.2023.3306740"
venue: "IEEE Transactions on Vehicular Technology (IEEE TVT)"
modeling_card: required
tags: [source, uav-mec, blockchain, delegated-proof-of-stake, stackelberg-game, trajectory-control, resource-allocation, task-offloading]
related:
  - "[[mobile-edge-computing]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[delegated-proof-of-stake]]"
  - "[[blockchain-on-edge-trust-layer]]"
  - "[[stackelberg-game]]"
  - "[[uav-trajectory-control]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[qin-2025-bcuav-masac]]"
  - "[[wang-2025-acbft-uav-consensus]]"
  - "[[mao-2025-bcsa-frl]]"
created: 2026-05-31
updated: 2026-07-16
---

# Blockchain-Integrated UAV-Assisted Mobile Edge Computing: Trajectory Planning and Resource Allocation

## Citation

Wang, D., Jia, Y., Dong, M., Ota, K., & Liang, L. (2024). *Blockchain-Integrated UAV-Assisted Mobile Edge Computing: Trajectory Planning and Resource Allocation*. **IEEE Transactions on Vehicular Technology**. DOI: 10.1109/TVT.2023.3306740.

## TL;DR

Integrates a **consortium blockchain** into a UAV-assisted MEC network to secure task offloading. An improved **Delegated Proof of Stake (DPoS)** consensus scheme lets UAVs act as light nodes that collect tasks and verify signatures from ground users to form an initial block, then offload it to ground blockchain nodes (selected from base stations via a reputation-based voting mechanism) for final block generation. A **two-stage [[stackelberg-game|Stackelberg game]]** jointly optimizes the UAV's trajectory and communication-resource allocation against the ground nodes' computing-resource allocation; equilibrium is found by backward induction and the non-convex sub-problems are handled with successive convex approximation (SCA).

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A UAV light node collects user transactions, forms an initial block, and transmits it to a primary ground blockchain node plus validation nodes selected from base stations. The UAV moves at fixed altitude while ground nodes execute consensus under an improved reputation-based DPoS protocol.

**Problem & objective**: The leader solves $P_1:\max_{X_n(t),P_t(t)}U_n(t)$, trading validation delay satisfaction against consensus reward and propulsion or transmission cost; follower $s$ solves $P_2:\max_{f_s(t)}U_s(t)$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV location | $X_n(t)$ | continuous, 2D trajectory | Horizontal position of UAV $n$ |
| UAV transmit power | $P_t(t)$ | continuous, $0.1\le P_t(t)\le1$ | Uplink power during transaction offloading |
| Ground CPU allocation | $f_s(t)$ | continuous, $0\le f_s(t)\le f_{\max}$ | Consensus CPU cycles assigned to node $s$ |
| Consensus activity | $\omega_s(t)$ | binary | Whether node $s$ is executing consensus |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Block QoS: cumulative transmitted data $\sum_t\Delta R_{n,p}(X_n(t))\ge N_B\bar w$ |
| C2 | Rate supports node compute: $R_{n,p}(X_n(t))\ge f_s(t)/D_s$ |
| C3 | UAV speed: $\|v_n(X_n(t))\|_2\le v_{\max}$ |
| C4 | UAV power: $0.1\le P_t(t)\le1$ |
| C5 | Follower CPU bound: $0\le f_s(t)\le f_{\max}$ |
| C6 | Consensus workload: $\sum_t\Delta f_s(t)$ covers verification, execution, and hashing cycles |

**Algorithm**: Solve the two-stage game backward. Obtain follower CPU strategies from KKT conditions and the consensus Nash equilibrium, then solve the non-convex leader trajectory and power problem with SCA; iterate the resulting policies to the Stackelberg equilibrium.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Wang et al. [x] integrated an improved delegated-proof-of-stake consensus layer with UAV-assisted MEC task offloading. The UAV leader chooses its trajectory and transmit power to balance validation delay satisfaction, rewards paid to ground nodes, and propulsion or radio energy, while each ground follower allocates consensus CPU under workload and capacity constraints. Backward induction combines follower KKT or Nash solutions with an SCA leader update to obtain a dynamic Stackelberg policy. Simulations reported shorter transaction offloading delay than traditional DPoS and showed that reputation and transaction volume directly shape the learned UAV trajectory.

## Problem framing

Task offloading in UAV-assisted MEC has security/privacy exposure (single point of failure, DDoS on a central node, leakage during task migration) that conventional mechanisms cannot fully address. Three coupled challenges: (1) keep edge nodes reliable long-term while running block consensus; (2) deliver QoS to ground users under limited UAV/edge resources via proper trajectory and resource allocation; (3) split and quantify profits between UAVs and ground blockchain nodes so all parties participate. The paper states no prior work tackles all three simultaneously.

## System model

- **Actors.** Ground users; a UAV acting as a blockchain light node (collects tasks, forms the initial block); ground blockchain nodes (full nodes) selected from base stations — a primary node plus validation nodes.
- **Consensus.** Improved DPoS: BSs are voted in through a **reputation incentive mechanism** (reputation + computing capacity as key factors) and collaborate with the UAV to generate blocks, mitigating stakeholder voting collusion of traditional DPoS.
- **Objective.** A joint optimization trading off energy consumption, offload latency, and consensus reward; the reward to ground nodes depends on allocated compute and the number of nodes per slot, constrained by computational power and UAV mechanics.

## Method

- Formulated as a **two-stage Stackelberg game** maximizing the utilities of the UAV (leader) and the ground blockchain nodes (followers); existence of a Nash equilibrium is proven via backward induction.
- Because the per-stage utility functions differ in convexity, the **KKT conditions** are applied first for the convex part, then the **approximate convex algorithm (SCA)** approximates the non-convex problem solving (with auxiliary-variable lower bounds and a difference-of-convex reformulation derived in the appendix).

## Key findings

- Simulation results demonstrate the scheme's effectiveness for trusted management and **superior delay** (stated qualitatively; specific curves are figure-derived).
- The reputation-driven node selection plus reward mechanism keeps ground blockchain nodes trustworthy and incentivizes long-term collaboration with the UAV.

## Limitations / future work

Simulation-only; the parse does not enumerate explicit future work. The consensus design is consortium/DPoS-specific and the UAV is a single light node. DOI date of publication 21 Aug 2023 / date of current version 17 Jan 2024 → year 2024.

## Relation to the corpus

Extends the **blockchain-on-edge trust layer** to UAV-assisted MEC offloading, joining [[qin-2025-bcuav-masac]] (Lyapunov + MASAC secure UAV-MEC), [[wang-2025-acbft-uav-consensus]] (chain-based BFT consensus for UAV ad hoc networks), and [[mao-2025-bcsa-frl]] (blockchain-enabled cold-start FRL) in the [[blockchain-on-edge-trust-layer]] synthesis. Its **Stackelberg + SCA** solver pairs the game-theoretic offloading thread (e.g. [[wang-2025-uav-swarm-stackelberg]], [[bi-2025-sg-mapg]]) with the [[alternating-optimization-sdr-sca]] convex family. First author **Die Wang** (Chongqing University / Muroran Institute of Technology); co-authors [[mianxiong-dong]] and Kaoru Ota recur across the air-ground MEC thread.

## Raw artifacts

- `raw/sources/Blockchain-Integrated_UAV-Assisted_Mobile_Edge_Computing_Trajectory_Planning_and_Resource_Allocation/full.md`
- Original PDF and extracted figures in the same folder.
