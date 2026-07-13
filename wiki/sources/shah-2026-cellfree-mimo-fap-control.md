---
type: source
title: "Joint Optimization of UAV Trajectory, Transmit Power, and User Association in Aerial-Terrestrial Cell-Free Massive MIMO Network"
authors: ["Syed Ammad Ali Shah", "Xavier N. Fernando", "Rasha Kashef"]
year: 2026
url: "https://doi.org/10.1109/TWC.2026.3685988"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, cell-free-massive-mimo, flying-access-point, trajectory-optimization, power-control, user-association, pilot-assignment]
related:
  - "[[aerial-terrestrial-cell-free-massive-mimo]]"
  - "[[accelerated-proximal-gradient-trajectory-power-control]]"
  - "[[interference-aware-dbscan-pilot-assignment]]"
  - "[[genetic-algorithm]]"
  - "[[device-association]]"
  - "[[uav-trajectory-control]]"
  - "[[csi-estimation-error]]"
created: 2026-07-13
updated: 2026-07-13
---

# Joint Optimization of UAV Trajectory, Transmit Power, and User Association in Aerial-Terrestrial Cell-Free Massive MIMO Network

## Citation

Shah, S. A. A., Fernando, X. N., & Kashef, R. (2026). *Joint Optimization of UAV Trajectory, Transmit Power, and User Association in Aerial-Terrestrial Cell-Free Massive MIMO Network*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2026.3685988.

> **Metadata grounding note.** The parse prints the DOI but omits final venue and year. Those fields were verified through the DOI's Crossref record; technical claims below remain parse-grounded.

## TL;DR

Combines three sequential modules for user-centric aerial cell-free massive MIMO: accelerated proximal-gradient updates for flying-access-point (FAP) trajectories and powers, a genetic algorithm for many-to-many user association and FAP deactivation, and interference-aware DBSCAN clustering for pilot reuse. The pipeline improves lower-tail simulated throughput, but it is a heuristic decomposition rather than a globally optimal joint solution.

## Problem

Cell-free cooperation removes fixed cell boundaries and frequent UAV handovers, but dense flying access points share pilots and create estimation error, interference, association overhead, and deployment cost. The paper maximizes sum user throughput subject to minimum-throughput, association, FAP capacity/power, flight-region, and speed constraints while also seeking fewer active FAPs and less pilot contamination. Table II lists 2 m safe FAP spacing, but the displayed formulation does not enforce pairwise separation.

## System model

- A central processing unit coordinates single-antenna UAV FAPs that jointly serve mobile users over the same resources using a 3GPP Option 8 functional split.
- Users may connect to multiple FAPs and each FAP may serve multiple users. Uplink training uses fewer orthogonal pilots than users, so co-pilot interference enters the MMSE channel estimates.
- FAP-user links use altitude/distance-dependent gain and fading; users follow low-speed random-waypoint mobility while FAPs reposition in 3-D over a 10 s local epoch.
- Throughput explicitly subtracts pilot overhead from the coherence interval.

## Method

1. [[accelerated-proximal-gradient-trajectory-power-control]] fixes association and minimizes negative sum throughput plus growing penalties for rate, power, capacity, and mobility violations. Momentum, projected gradient candidates, a fallback update, and relaxed objective thresholds control the iteration.
2. A [[genetic-algorithm]] evolves binary FAP-user association matrices using tournament selection, two-point crossover, guided mutation, elitism, and penalties for QoS, load, power, and excessive assignments.
3. [[interference-aware-dbscan-pilot-assignment]] first forms Euclidean-distance clusters and assigns pilots, then detects cross-cluster users sharing both a pilot and FAP and re-associates one user to a nearest conflict-free FAP. This is narrower than the abstract's claim that clustering itself uses spatial and interference metrics.

The APG discussion gives sufficient Lipschitz/step-size conditions and a numerical stopping rule, but the objective remains non-convex and the paper does not prove global optimality. The GA and DBSCAN stages are heuristic and are optimized sequentially rather than as one jointly convergent procedure.

## Key findings

- With 100 FAPs, 80 users, and 30 pilots, Fig. 2 reports an approximately **18 dB 95%-likely SINR**, versus about 9 dB for GB-GS and negative values for two other baselines.
- With 200 FAPs and 150 users, the proposed APG setting reports more than **40 Mbps** 95%-likely throughput and a median near 43 Mbps; a pilot length of 50 raises the lower-tail value to **47 Mbps** in Fig. 5.
- Table III reports **44.3 Mbps** for the full pipeline versus 37 Mbps for GA association alone: APG power alone, APG trajectory alone, and IB-DBSCAN alone are listed at 37.5, 39.7, and 38.3 Mbps. Its stated 16.4% full-pipeline gain conflicts with `(44.3-37)/37 = 19.73%`.
- Fig. 8 reports **42.7 Mbps** for IB-DBSCAN, compared with 19.64 Mbps for interference-based K-means, 19.38 Mbps for geography-based K-means, and 18.42 Mbps for random pilot assignment. The proposed setting also uses fewer FAPs than the baselines, so this is not a same-configuration comparison.

## Limitations / interpretation

Evidence is Python/Google-Colab simulation on two CPU cores; seeds and repeated-run uncertainty are not reported. The 500 m square uses periodic boundaries, short local repositioning, simplified single-antenna FAPs, and centralized Option 8 processing. Propulsion energy, fronthaul/backhaul capacity and power, and end-to-end latency are omitted.

Several comparisons require caution. Fig. 6 juxtaposes methods at different user loads, so it does not independently establish the abstract's “over 40%” UAV reduction at equal demand. Figs. 7-8 change FAP configurations, and Fig. 7 also changes antenna counts. Table III uses GA association as its baseline, making the prose claim that most gain “originates from GA” unsupported by that ablation. The formulation alternates between sum-throughput and per-user/fairness language; minimum-rate constraints protect users, but the objective is not max-min fairness.

## Relation to the corpus

The source adds [[aerial-terrestrial-cell-free-massive-mimo]] as a no-cell-boundary alternative to conventional UAV base-station association. It reuses [[device-association]] and [[uav-trajectory-control]], but separates continuous APG updates, combinatorial GA association, and pilot clustering instead of learning all decisions end to end.

## Raw artifacts

- Parse: `raw/sources/Joint_Optimization_of_UAV_Trajectory_Transmit_Power_and_User_Association_in_Aerial-Terrestrial_Cell-Free_Massive_MIMO_Network/Joint_Optimization_of_UAV_Trajectory_Transmit_Power_and_User_Association_in_Aerial-Terrestrial_Cell-Free_Massive_MIMO_Network.md`
- Origin PDF and extracted figures (`images/`) in the same folder.
