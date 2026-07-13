---
type: source
title: "SkyNDN Incentivizer: Enhancing Content Sharing in UAV Named Data Networking"
authors: ["Chenlang Jin", "Haipeng Yao", "Ruze Cai", "Tianle Mai", "Jiaqi Xu", "Zehui Xiong", "Dusit Niyato"]
year: 2026
url: "https://doi.org/10.1109/TMC.2025.3622224"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), vol. 25, no. 3, pp. 4013-4030"
tags: [source, named-data-networking, uav-swarm, content-sharing, double-auction, incentive-mechanism, social-welfare, diffusion-reinforcement-learning]
related:
  - "[[uav-named-data-networking]]"
  - "[[iterative-double-auction-incentive]]"
  - "[[double-auction]]"
  - "[[diffusion-model-as-optimizer]]"
  - "[[generative-diffusion-model]]"
  - "[[gauss-markov-mobility-model]]"
  - "[[autonomous-uav-swarms]]"
  - "[[li-2026-online-maritime-double-auction]]"
  - "[[seid-2026-mafdrl-tn-ntn-incentive]]"
  - "[[dai-2024-multiuav-marine-welfare]]"
  - "[[ye-2025-aigc-diffusion-contract]]"
  - "[[du-2024-gdm-network-optimization-tutorial]]"
  - "[[zehui-xiong]]"
  - "[[dusit-niyato]]"
created: 2026-07-14
updated: 2026-07-14
---

# SkyNDN Incentivizer: Enhancing Content Sharing in UAV Named Data Networking

## Citation

Jin, C., Yao, H., Cai, R., Mai, T., Xu, J., Xiong, Z., & Niyato, D. (2026). *SkyNDN Incentivizer: Enhancing Content Sharing in UAV Named Data Networking*. **IEEE Transactions on Mobile Computing, 25**(3), 4013-4030. DOI: 10.1109/TMC.2025.3622224.

## TL;DR

Builds a broker-mediated content market for [[uav-named-data-networking|UAV Named Data Networking]], where consumers buy cached data from mobile producers. An iterative double auction aligns bid/ask updates with a social-welfare allocation under assumed concave utilities and convex costs; a separate twin-critic diffusion actor learns continuous many-to-many allocations when those analytical forms are not used by the solver.

## Problem

Named Data Networking lets a UAV retrieve content from any reachable producer or cache by issuing an Interest for its name. Resource-limited UAVs may nevertheless refuse to share cached data because forwarding consumes radio and energy resources. The paper introduces a virtual central broker that prices content exchanges, seeks high consumer utility minus producer cost, and incentivizes producers to participate despite private utility and cost information.

## System model

- For one content item, `M` consumers request amounts from `N` producers. Pairwise demand `theta_ij` and supply `omega_ji` must clear exactly, while each consumer has minimum/maximum demand and each producer has a capacity limit.
- UAV mobility follows a three-dimensional [[gauss-markov-mobility-model]]. Transmission energy switches between free-space distance-squared and multipath distance-fourth regimes, and delay sums transmission and propagation delay over a multihop path.
- Interest packets use content names. Because mobility may break the reverse Interest path, Data packets do not retrace it; every forwarder is assumed to choose the nearest available next hop.
- Producers use orthogonal subchannels, UAVs are homogeneous, and rates use an average-gain Shannon model. Consumer utility is increasing and concave in delivered content per delay, while producer cost is increasing and convex in transmission energy.

## Method

The welfare problem `P1` maximizes total consumer utility minus total producer cost under demand, capacity, and pairwise-clearing constraints. Under the adopted utility and cost functions, `P1` is strictly concave over compact convex constraints and can be characterized by KKT conditions.

[[iterative-double-auction-incentive|IDAA]] handles information asymmetry through consumer bid vectors, producer ask vectors, and broker settlement/payment rules. The broker repeatedly solves a surrogate allocation problem `P2`, announces allocations and prices, and receives updated bids and asks until all changes are below `epsilon`. Comparing the KKT systems of `P1` and `P2` gives the paper's truthful marginal-value and marginal-cost update forms. The paper claims economic efficiency, individual rationality, incentive compatibility, and budget balance under its modeled functions and update rules. These are KKT- and simulation-backed claims rather than a separately stated general mechanism-design theorem.

DiffRL-DA is a distinct learned allocator. Its state contains consumer-producer path distances, hop counts, and each producer's next-hop distance. A diffusion actor denoises Gaussian noise into the full continuous transaction matrix, while two critics use the lower Q estimate to reduce overestimation. Feasible actions receive social welfare as reward; infeasible actions receive the negative number of violated constraints. Training uses replay, target networks, exploration noise, and soft updates. The authors propose server-side training and execution at a capable UAV cluster head.

IDAA costs `O(I(MN)^3)` over `I` auction iterations because each iteration solves `P2`. DiffRL-DA provides no theorem for global optimality, neural convergence, per-inference feasibility, truthfulness, or the four economic properties claimed for IDAA. It uses [[diffusion-model-as-optimizer]] as an action generator, not distributional value learning.

## Key findings

- In the 3-consumer/3-producer IDAA case, bids, asks, demand, and supply converge after about 10 iterations. Equilibrium demand/supply values are `15.289`, `18.749`, and `13.455` Mbit.
- At that equilibrium, consumer utilities are `29.022`, `39.052`, and `20.818`; producer costs are `3.490`, `3.695`, and `3.383`. Consumer settlement and producer payment coincide at `4.706`, `7.259`, and `3.511` in the paper's table.
- DiffRL-DA's reported allocations are `14.650`, `17.032`, and `9.792` Mbit on both demand and supply sides. Its consumer utilities are `23.134`, `39.497`, and `12.922`, with producer costs `3.555`, `3.659`, and `3.819`.
- The static comparison reports PPO, DDPG, DQN, and DiffRL-DA stabilizing after roughly 200, 300, 400, and 500 epochs, respectively, while DiffRL-DA attains the highest plotted utility. Another subsection says DiffRL-DA stabilizes after about 400 epochs, so convergence timing is internally inconsistent.
- Of tested denoising depths, `T=5` gives the highest reported reward (`55.597`) and utility (`64.520`) with training time `5953.24 s`. `T=3`, `8`, and `10` perform worse on those metrics in the reported table; this is an empirical sweep rather than a general optimum.
- In a dynamic mobility experiment, DiffRL-DA retains the highest plotted utility but fluctuates as distances, path delays, and transmission energy change.

## Limitations

The work is simulation-only, with no NDN testbed, UAV flight trace, cache/Interest workload, radio experiment, or strategic-agent study. The trusted broker is assumed always reachable and becomes a single point of failure; distributed trading is left for future work. The model omits interference, collisions, cache eviction, Pending Interest Table growth and timeout, content authentication overhead, routing loops, producer discovery, malicious bids, collusion, Sybil identities, payment enforcement, and long-term battery or budget evolution.

IDAA depends on hand-designed monotone concave utilities and monotone convex costs. DiffRL-DA's state omits bids, asks, cache state, content popularity, residual energy, and interference, so it does not reproduce IDAA's strategic mechanism. Its count-based infeasibility penalty provides no hard projection or feasibility guarantee. Several equations and the DQN action values are damaged or absent in the parse, and the paper sometimes mistypes IDAA as IDDA. Claims that DiffRL-DA removes strong assumptions should be read as relaxing the analytical solver's function-shape dependence, not as validation for arbitrary real participant preferences.

## Relation to the corpus

This source brings content-name forwarding and caching into the UAV-swarm incentive thread through [[uav-named-data-networking]]. [[li-2026-online-maritime-double-auction]] trades connectivity under deadlines and capacity constraints, [[seid-2026-mafdrl-tn-ntn-incentive]] combines a hierarchical auction with DDPG, and [[dai-2024-multiuav-marine-welfare]] treats UAVs as service buyers rather than content consumers. DiffRL-DA connects the market to [[du-2024-gdm-network-optimization-tutorial]] and [[ye-2025-aigc-diffusion-contract]], but its diffusion policy allocates content under auction constraints rather than generating contracts. Confirmed recurring authors [[zehui-xiong]] and [[dusit-niyato]] connect it to the corpus's generative network-optimization and incentive-design literature.

## Raw artifacts

- Parse: `raw/sources/SkyNDN_Incentivizer_Enhancing_Content_Sharing_in_UAV_Named_Data_Networking/SkyNDN_Incentivizer_Enhancing_Content_Sharing_in_UAV_Named_Data_Networking.md`
- Origin PDF: `raw/sources/SkyNDN_Incentivizer_Enhancing_Content_Sharing_in_UAV_Named_Data_Networking/SkyNDN_Incentivizer_Enhancing_Content_Sharing_in_UAV_Named_Data_Networking.pdf`
- Figures: `raw/sources/SkyNDN_Incentivizer_Enhancing_Content_Sharing_in_UAV_Named_Data_Networking/images/`
