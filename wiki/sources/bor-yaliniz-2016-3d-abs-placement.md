---
type: source
title: "Efficient 3-D Placement of an Aerial Base Station in Next Generation Cellular Networks"
authors: ["R. Irem Bor-Yaliniz", "Amr El-Keyi", "Halim Yanikomeroglu"]
year: 2016
url: "https://doi.org/10.1109/ICC.2016.7510820"
venue: "IEEE International Conference on Communications (IEEE ICC)"
modeling_card: required
tags: [source, aerial-base-station, drone-cell, 3d-placement, air-to-ground-channel-model, mixed-integer-nonlinear-programming, cellular-coverage]
related:
  - "[[drone-cell-3d-placement]]"
  - "[[air-to-ground-channel-model]]"
  - "[[al-hourani-2014-optimal-lap-altitude]]"
  - "[[cellular-connected-uav]]"
  - "[[mixed-integer-nonlinear-programming]]"
  - "[[high-altitude-platform-station]]"
  - "[[mozaffari-2019-uav-wireless-tutorial]]"
  - "[[weighted-kmeans-uav-deployment]]"
created: 2026-06-01
updated: 2026-07-16
---

# Efficient 3-D Placement of an Aerial Base Station in Next Generation Cellular Networks

## Citation

Bor-Yaliniz, R. I., El-Keyi, A., & Yanikomeroglu, H. (2016). *Efficient 3-D Placement of an Aerial Base Station in Next Generation Cellular Networks*. **IEEE International Conference on Communications (ICC)**. DOI: 10.1109/ICC.2016.7510820.

> **Metadata grounding note.** The MinerU parse of this paper contains **no** publication-date, venue, or DOI line (its reference list runs to 2015). The venue (IEEE ICC 2016) and DOI above are **not in the parse** and were confirmed externally via IEEE Xplore (document 7510820) and the arXiv preprint 1603.00300; treat them as web-confirmed rather than parse-grounded.

## TL;DR

A foundational **drone-cell** (low-altitude UAV-mounted aerial base station, ABS) placement paper. It is stated to be the first to pose **3-D placement** — jointly choosing the drone-cell's **altitude** and the **location + size of its coverage area** — with the objective of **maximizing the number of served users (network revenue)**. Using the urban air-to-ground LoS-probability channel model, the problem becomes a quadratically-constrained **mixed-integer nonlinear program (MINLP)**; introducing a variable that ties altitude to coverage radius lets a **1-D bisection search** plus the MOSEK interior-point solver crack it efficiently.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A congested or failed macrocell has known uncovered-user coordinates $(x_i,y_i)$ and is assisted by one quasi-stationary, fixed-power low-altitude drone-cell. A user is served when the environment-dependent air-to-ground path loss $L(h,r_i)$ is below the QoS threshold $\gamma$.

**Problem & objective**: The original 3D-placement MINLP maximizes network revenue measured by covered users, $\max_{x_D,y_D,h,\{u_i\}}\sum_{i\in\mathbb{U}}u_i$, while jointly selecting the drone-cell's horizontal location, altitude, and coverage set.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Horizontal location | $x_D,y_D$ | Continuous, $[x_l,x_u]\times[y_l,y_u]$ | Drone-cell ground-plane coordinates |
| Altitude | $h$ | Continuous, $[h_l,h_u]$ | Drone-cell altitude |
| User coverage | $u_i$ | Binary, $\{0,1\}$ | Whether user $i$ is served |
| Coverage radius | $R$ | Continuous, $R\geq0$ | Radius in the equivalent reformulation |
| Altitude-radius ratio | $\alpha=h/R$ | Continuous, $\alpha\geq0$ | Environment-dependent ratio used to recover altitude |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| QoS | $h^2+r_i^2\leq10^{[\gamma-(AP(h,r_i)+B)]/10}+M_1(1-u_i)$ |
| Placement bounds | $x_l\leq x_D\leq x_u$, $y_l\leq y_D\leq y_u$, and $h_l\leq h\leq h_u$ |
| Coverage indicator | $u_i\in\{0,1\}$ for every $i\in\mathbb{U}$ |
| Radius linkage | $R\geq r_i-M_2(1-u_i)$ and $\alpha=h/R$ |
| Equivalent radius limit | $R^2\leq\Gamma(\alpha)+M_1(1-u_i)$, where $\Gamma(\alpha)=10^{[\gamma-(AP(\alpha)+B)]/10}/(1+\alpha^2)$ |

**Algorithm**: A one-dimensional bisection search finds the unique numerical maximizer $\alpha^*$ of $\Gamma(\alpha)$ by locating the root of $d\Gamma(\alpha)/d\alpha$. With $\alpha^*$ fixed, the remaining quadratically constrained MINLP over $x_D$, $y_D$, $R$, and $u_i$ is solved by the MOSEK interior-point optimizer, and the altitude is recovered as $h=\alpha^*R$.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Bor-Yaliniz et al. [x] studied three-dimensional placement of a single low-altitude drone-cell that assists a congested or failed macrocell with known user locations. They modeled urban air-to-ground path loss through an elevation-dependent line-of-sight probability and treated a user as covered when its path loss satisfies a fixed QoS threshold. The resulting mixed-integer nonlinear program maximizes the number of covered users by jointly selecting horizontal position, altitude, coverage radius, and binary user-coverage indicators within placement and QoS bounds. The authors introduced the altitude-to-radius ratio $\alpha=h/R$, found its environment-dependent optimum by one-dimensional bisection, and solved the remaining quadratically constrained mixed-integer problem with MOSEK. Numerical experiments with 40 uniformly distributed users showed consistent covered-user counts across 100 Monte Carlo trials and strong dependence of achievable revenue on the suburban, urban, dense-urban, or high-rise environment.

## Problem framing

Next-generation cellular networks face unexpected or temporary events — natural disasters, extreme user densities, rural coverage gaps — where permanent infrastructure is not cost-justified. Low-altitude UAVs serving as ABSs (drone-cells) offer quick, on-demand deployment. The key difficulty: unlike terrestrial BSs, a drone-cell's placement spans the **vertical** dimension too, and the **air-to-ground channel** differs from terrestrial channels (higher LoS chance, environment-dependent blockage). Prior work fixed altitude (1-D) or considered only horizontal placement (2-D); in a congested cell, neither the size nor the location of the area to cover is known a priori — both must be set against target revenue and QoS. Altitude is intertwined because the UAV-user channel depends on it.

## System model

- **Actors.** A macrocell with known user locations $(x_i,y_i)$; when the terrestrial BS (eNB) cannot serve all users (congestion/malfunction), a single low-altitude **quasi-stationary** drone-cell with fixed transmit power assists.
- **Channel.** Adopts the urban **air-to-ground** model ([[air-to-ground-channel-model]]): LoS probability is a sigmoid in the elevation angle $\arctan(h/r_i)$ with environment constants $a,b$; path loss combines free-space term with LoS/NLoS excess losses $\eta_{LoS},\eta_{NLoS}$ — the same family of model from [[al-hourani-2014-optimal-lap-altitude]].
- **Objective.** Maximize **revenue** $\propto$ number of covered users (each user covered if received SNR exceeds a QoS threshold), by choosing altitude $h$ and coverage-region location/size.

## Method

- Formulate the **3-D placement** as maximizing covered users; show it reduces (after manipulation) to a quadratically-constrained **MINLP** ([[mixed-integer-nonlinear-programming]]).
- Introduce a new variable **relating altitude to coverage radius**; its optimal value has no closed form but is obtained by **1-D bisection search**.
- With that variable fixed, the residual MINLP is solved by the **interior-point optimizer of the MOSEK solver**.

## Key findings

- The reformulation makes the 3-D placement **efficiently solvable**, returning the drone-cell's altitude and the coverage region's location and size (the paper's stated contribution).
- Numerical results show the **number of covered users depends strongly on environment**: with 40 users uniformly distributed in a macrocell, the mean covered-user count and the optimal coverage geometry differ markedly across **suburban / urban / dense-urban / high-rise-urban** environments (Fig. 4, parse; values reported with 95% confidence intervals are environment-specific and indicative).
- The optimal placement is **not** simply "directly above the user cluster" — environment-dependent blockage shifts the best altitude and coverage region.

## Limitations / future work

The authors flag (stated) modeling **inter-cell/inter-drone interference** and deploying **multiple drone-cells** as future directions. The model is single drone-cell, quasi-stationary, and assumes known user locations and fixed QoS.

## Relation to the corpus

A canonical **aerial-base-station 3-D placement** anchor — it defines the [[drone-cell-3d-placement]] problem the wiki refers back to, and uses the urban [[air-to-ground-channel-model]] introduced in [[al-hourani-2014-optimal-lap-altitude]]. It is a *placement/deployment* (coverage-maximization) framing rather than compute offloading, complementing the deployment-oriented [[weighted-kmeans-uav-deployment]] and the UAV-as-base-station taxonomy surveyed in [[mozaffari-2019-uav-wireless-tutorial]]. Distinct from [[high-altitude-platform-station|HAPS]] (much higher, long-endurance) and from [[cellular-connected-uav]] (UAV as a user, not a BS).

## Raw artifacts

- `raw/sources/Efficient_3-D_placement_of_an_aerial_base_station_in_next_generation_cellular_networks/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
