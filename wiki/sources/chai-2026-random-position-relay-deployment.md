---
type: source
title: "Transmission Time Minimization-Based UAV Deployment and Resource Allocation With Random User Position Information"
authors: ["Rong Chai", "Huiling Wang", "Hong Chen", "Lin He", "Ruijin Sun", "Qianbin Chen"]
year: 2026
url: "https://doi.org/10.1109/TGCN.2025.3602956"
venue: "IEEE Transactions on Green Communications and Networking (IEEE TGCN), vol. 10, pp. 921-932"
modeling_card: required
tags: [source, uav-relay, satellite, statistical-user-position, deep-q-network, device-association, physical-layer-security]
related:
  - "[[statistical-user-position-uav-deployment]]"
  - "[[deep-q-network]]"
  - "[[multi-agent-q-learning]]"
  - "[[device-association]]"
  - "[[uav-mobile-relaying]]"
  - "[[physical-layer-security]]"
  - "[[noma]]"
  - "[[space-air-ground-integrated-network]]"
  - "[[shi-2026-vhetnet-comp-coverage]]"
  - "[[mobility-asynchrony-and-geometry-in-aerial-coverage]]"
  - "[[rong-chai]]"
  - "[[qianbin-chen]]"
created: 2026-07-14
updated: 2026-07-16
---

# Transmission Time Minimization-Based UAV Deployment and Resource Allocation With Random User Position Information

## Citation

Chai, R., Wang, H., Chen, H., He, L., Sun, R., & Chen, Q. (2026). *Transmission Time Minimization-Based UAV Deployment and Resource Allocation With Random User Position Information*. **IEEE Transactions on Green Communications and Networking, 10**, 921-932. DOI: 10.1109/TGCN.2025.3602956.

## TL;DR

Models unknown ground-user positions with a truncated Gaussian density, trains independent DQN agents for relay-UAV grid placement and satellite-link power, and alternates that learned control with shortest-transmission-time association plus greedy load balancing.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Ground users with a two-dimensional truncated-Gaussian position density upload through fixed-altitude aerial relays to a satellite while an eavesdropper UAV overhears the access hop. OFDMA separates users associated with one relay, NOMA supports relay-to-satellite forwarding, relay sites lie on a rectangular grid, and the objective integrates two-hop transmission time over the user density.

**Problem & objective**: Problem (29) minimizes expected system transmission time, $\min_{\mathbf q_n,P_n,\alpha_n(x,y)}T$ with $T=\sum_{n=1}^{N}\tilde T_n$, by jointly choosing relay deployment, relay transmit power, and user association.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Relay deployment position | $\mathbf q_n=(x_n,y_n)$ | discrete grid point in $\tilde\Psi$ | Horizontal location of aerial relay $n$ |
| Relay transmit power | $P_n$ | continuous, $0\leq P_n\leq P_n^{\max}$; discretized into $W$ DQN levels | Power used by relay $n$ on the satellite hop |
| User association | $\alpha_n(x,y)$ | binary, $\{0,1\}$ | Whether a user at $(x,y)$ is served by relay $n$ |
| DQN relay action | $a_{n,t}=(\psi_{n,t},P_{n,t})$ | finite movement and power action | Stay or move to an adjacent grid and choose one power level |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | A user accesses at most one relay, $\sum_{n=1}^{N}\alpha_n(x,y)\leq1$ |
| C2-C3 | Relay load does not exceed $F$ subchannels and every deployed relay serves a positive user mass |
| C4 | Relay separation is safe, $\|\mathbf q_n-\mathbf q_{n'}\|_2\geq l_s$ for $n\neq n'$ |
| C5-C6 | Each relay remains inside the rectangular deployment region |
| C7 | At most one relay occupies a grid, $\mathbf q_n\neq\mathbf q_{n'}$ for $n\neq n'$ |
| C8 | Relay power is bounded, $P_n\leq P_n^{\max}$ |

**Algorithm**: Each relay is a DQN agent whose state is $\mathbf q_{n,t}$, whose action combines an adjacent-grid move with one discretized power level, and whose reward is $r_n(s_{n,t},a_{n,t})=-T(s_{n,t},a_{n,t},\Omega_t)$. For every deployment and power iterate, the embedded association routine assigns each user to its shortest-time relay, then greedily moves users from the heaviest-loaded relay to a second-choice relay until the load-difference threshold is met.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Chai et al. [x] studied joint aerial-relay deployment, satellite-link power allocation, and ground-user association in a UAV-assisted satellite system with statistically distributed user locations and an eavesdropper UAV. They minimized the expected two-hop system transmission time over relay positions, powers, and binary associations under subchannel capacity, nonempty relay load, inter-relay separation, deployment-region, distinct-grid, and maximum-power constraints. Their iterative scheme trains one DQN agent per relay using grid movement and discretized power actions with negative transmission time as reward, while an improved K-means association stage assigns each user to its shortest-time relay and shifts users to balance loads. Simulations report more balanced relay loads and transmission-time reductions of 20% and 18% against the two cited comparison algorithms at 0.01 W user power and $10^{-12}$ W noise.

## System and method

Ground users upload through fixed-altitude aerial relays to a satellite while a UAV eavesdropper threatens the first hop. OFDMA supports ground access and NOMA supports relay-satellite forwarding. The expected objective sums two-hop transmission time over the user-position density.

Each relay agent chooses a neighboring grid move or stay action and one discretized power level. All agents receive negative total transmission time. Given deployment and powers, users select the relay with shortest modeled time; a greedy repair shifts users from overloaded relays to their second choice.

## Findings and guarantee scope

The DQN/greedy embedded loop has no global/local optimality, monotonicity, feasibility, or convergence theorem for the joint problem. In simulation, the proposed association is more balanced than K-means and reports transmission-time gains over three baselines under selected bandwidth, power, and noise settings.

## Limitations

Simulation only; fixed-altitude grid deployment, static users, known density and demand, discretized power, direct satellite links, and simplified secrecy rates. The written association constraint permits unserved users, secrecy rate lacks a positive-part operator, and the online routine nevertheless assumes exact user coordinates. The greedy repair does not explicitly recheck every formal capacity constraint, and summing relay times is not justified as wall-clock completion time under parallel operation.

## Relation to the corpus

This source links [[statistical-user-position-uav-deployment]] to [[device-association]] in a satellite-aerial relay setting. Unlike deterministic deployment pages that optimize from known coordinates, it integrates the placement objective over a user density, yet its association and load-balancing routine still depends on realized positions; the page therefore keeps statistical planning and online assignment as distinct mechanisms.

## Raw artifacts

- Parse: `raw/sources/Transmission_Time_Minimization-Based_UAV_Deployment_and_Resource_Allocation_With_Random_User_Position_Information/Transmission_Time_Minimization-Based_UAV_Deployment_and_Resource_Allocation_With_Random_User_Position_Information.md`
- Original PDF and extracted figures are in the same folder.
