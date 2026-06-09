---
type: source
title: "UAV-Enabled Wireless Power Transfer: Trajectory Design and Energy Optimization"
authors: ["Jie Xu", "Yong Zeng", "Rui Zhang"]
year: 2018
url: "https://doi.org/10.1109/TWC.2018.2838134"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, wireless-power-transfer, uav-trajectory-control, energy-fairness, convex-optimization, foundational]
related:
  - "[[wireless-power-transfer]]"
  - "[[rf-energy-harvesting]]"
  - "[[uav-trajectory-control]]"
  - "[[successive-hover-and-fly-trajectory]]"
  - "[[air-to-ground-channel-model]]"
  - "[[fairness-metrics-in-mec]]"
  - "[[zeng-2017-energy-efficient-uav-trajectory]]"
  - "[[zeng-2016-throughput-relaying]]"
  - "[[zeng-2019-rotary-wing-energy-min]]"
  - "[[zhou-2018-uav-wireless-powered-mec]]"
  - "[[liu-2020-wpt-cooperative-uav-mec]]"
  - "[[yong-zeng]]"
created: 2026-06-01
updated: 2026-06-09
---

# UAV-Enabled Wireless Power Transfer: Trajectory Design and Energy Optimization

## Citation

Xu, J., Zeng, Y., & Zhang, R. (2018). *UAV-Enabled Wireless Power Transfer: Trajectory Design and Energy Optimization*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2018.2838134. (Manuscript received 22 Sep 2017; accepted 14 May 2018; date of publication 25 May 2018; date of current version 10 Aug 2018. Parts presented at IEEE GLOBECOM Workshop 2017 and APCC Workshop 2017.)

## TL;DR

A foundational study of **UAV-enabled wireless power transfer (WPT)**: a UAV-mounted mobile energy transmitter is dispatched to charge a set of ground energy receivers (ERs) at known locations, and its **trajectory** is optimized to maximize energy delivered over a finite charging period $T$ under a maximum-speed constraint. Two problems are solved. **Sum-energy maximization** has an optimal solution in which the UAV **hovers at one fixed location** for the whole period — but this creates a severe **"near-far" fairness** problem. **Min-energy maximization** (maximize the minimum received energy across ERs) fixes the fairness issue: ignoring the speed limit, the optimum is **multi-location hovering** with optimal time allocation, and with the speed limit a **successive hover-and-fly** trajectory plus an SCP-based refinement are proposed.

## Problem framing

Conventional WPT deploys fixed energy transmitters, which require ultra-dense deployment to cover a wide area because of severe RF propagation loss — costly and impractical. The paper takes a system-level approach instead: mount the ET on a UAV and exploit its **controllable mobility** to shorten ET-to-ER distances on demand. The core question is how to design the UAV trajectory to maximize energy transferred to all ERs *fairly*, which the authors state had not been studied before, and is non-trivial even for one UAV and two ERs.

## System model

- **Actors.** One UAV/ET at fixed altitude $H>0$; $K \ge 2$ ground ERs at known fixed locations; finite charging period $\mathcal{T}=[0,T]$ ([[wireless-power-transfer]]).
- **Channel.** UAV-to-ER links are assumed LoS-dominated, so a **free-space path-loss** model is used: channel power gain $\propto d_k^{-2}(t)$ with $\beta_0$ the gain at 1 m reference distance ([[air-to-ground-channel-model]]).
- **Received power/energy.** With constant transmit power $P$, the RF power at ER $k$ is $\beta_0 P / d_k^2(t)$; the received energy is the time integral over $\mathcal{T}$. The performance metric is **received RF power/energy prior to RF-to-DC conversion**, because no generic accurate non-linear RF-to-DC model exists ([[rf-energy-harvesting]]).
- **Constraint.** Maximum UAV speed $V$; initial/final locations are free to optimize.

## Method

- **Sum-energy maximization (P1).** Non-convex with infinitely many variables, but solved optimally: the optimal trajectory is **single-location hovering**, with the location found by a 2D exhaustive search (closed-form for $K=2$). For $K=2$, when the inter-ER distance $D \le 2H/\sqrt{3} = 5.77$ m the optimum hovers above the midpoint; beyond that threshold it shifts toward one ER.
- **Min-energy maximization, ideal case (P3).** Ignoring the speed constraint, the problem satisfies a time-sharing condition and is solved **optimally via the Lagrange dual method**; the optimum is **multi-location hovering** with optimal hovering-time allocation across a set of fixed locations.
- **Min-energy maximization, general case (P2).** With the speed constraint, a **successive hover-and-fly** trajectory is proposed ([[successive-hover-and-fly-trajectory]]) — hover at each optimal location for a duration, fly at maximum speed between them along the shortest visiting path. It is proved optimal for $K=2$ and asymptotically optimal for $K>2$ as $T\to\infty$. A **successive convex programming (SCP)** algorithm, initialized by the hover-and-fly trajectory, iteratively refines toward a locally optimal solution ([[uav-trajectory-control]]).

## Key findings

- **Single-location hovering is optimal for sum-energy** — and provably so — but induces a near-far fairness gap: in the $K=10$ example, the optimal hovering point sits near ERs 7–10, which receive far more power (figure-derived values around 0.19 mW) than distant ERs like ER 1 (~0.013 mW), an order-of-magnitude disparity (indicative, from the parse's extracted figure).
- **Mobility buys fairness when ERs are spread out.** For $K=2$, when $D \le 5.77$ m a static UAV matches a mobile one; when $D > 5.77$ m the mobile design delivers strictly higher max-min received power, and the gain grows with $D$ and with the maximum speed $V$.
- **SCP refines hover-and-fly.** For $K=10$ the ideal case yields $\Gamma=4$ optimal hovering clusters; the proposed successive hover-and-fly and SCP-based trajectories both visit them and outperform single-location hovering, with the SCP trajectory achieving the best performance and converging to the (speed-unconstrained) upper bound as $T$ grows.
- Simulation setup (verbatim): $\beta_0=-30$ dB, $H=5$ m, $P=40$ dBm; metric is average received power (energy normalized by $T$).

## Limitations / future work

- The paper focuses on **one UAV/ET**, leaving the multi-UAV/ET case for future work.
- The LoS **free-space path-loss** assumption may not hold with obstacles/scatterers (e.g. forests), where a path-loss exponent larger than 2 applies; the authors note their problem structures and algorithms extend to such cases but do not solve them here.
- The metric is received RF power **before** RF-to-DC conversion, sidestepping the (non-linear) rectifier model.

## Relation to the corpus

A **foundational UAV-WPT trajectory-optimization** anchor, and the WPT-only precursor to the corpus's WPT-MEC line — it predates and underpins [[zhou-2018-uav-wireless-powered-mec]] (computation-rate maximization) and [[liu-2020-wpt-cooperative-uav-mec]] (idle-SD cooperative WPT-MEC), which add a compute/offloading layer on top of the energy-delivery problem this paper isolates. By [[yong-zeng]] and Rui Zhang (with Jie Xu), it shares the convex-optimization / SCA(SCP) trajectory-design methodology and authorship of the UAV-communications foundations [[zeng-2017-energy-efficient-uav-trajectory]], [[zeng-2016-throughput-relaying]], and [[zeng-2019-rotary-wing-energy-min]]. Its **near-far / max-min energy fairness** framing connects to the corpus's [[fairness-metrics-in-mec]] hub, and the **successive hover-and-fly** structure ([[successive-hover-and-fly-trajectory]]) recurs as a UAV-trajectory primitive.

> Author note: the first author **Jie Xu** here is affiliated with the **School of Information Engineering, Guangdong University of Technology** (Guangzhou) — distinct from the [[jie-xu]] entity in this wiki (CUHK-Shenzhen, ISAC). They are treated as separate identities pending confirmation, so no entity link is embedded for this Jie Xu.

## Raw artifacts

- Parse: `raw/sources/UAV-Enabled_Wireless_Power_Transfer_Trajectory_Design_and_Energy_Optimization/full.md`
- Origin PDF: `raw/sources/UAV-Enabled_Wireless_Power_Transfer_Trajectory_Design_and_Energy_Optimization/7aaece4b-2696-4b7f-b602-3ee5873bc8b3_origin.pdf`
- Figures: `raw/sources/UAV-Enabled_Wireless_Power_Transfer_Trajectory_Design_and_Energy_Optimization/images/`
