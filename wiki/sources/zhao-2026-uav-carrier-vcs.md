---
type: source
title: "UAV Carrier Enabled Vehicular Crowdsensing by Multi-Agent Reinforcement Learning with Mutual Policy Divergence and Attentive Memory Update"
authors: ["Qiran Zhao", "Chi Harold Liu", "Jianxin Zhao", "Guozheng Li", "Guangpeng Qi", "Xu Ji", "Duo Xu", "Jon Crowcroft"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3693470"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), 1-18"
tags: [source, vehicular-crowdsensing, uav-carrier, heterogeneous-agent-rl, multi-agent-drl, attentive-memory, policy-divergence]
related:
  - "[[uav-assisted-mobile-crowd-sensing]]"
  - "[[attentive-memory-integrated-information-exchange]]"
  - "[[mutual-policy-divergence-exploration]]"
  - "[[ma-pomdp]]"
  - "[[heterogeneous-agent-rl]]"
  - "[[hidden-state-sharing-marl]]"
  - "[[sequential-multi-agent-policy-generation]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[ppo]]"
  - "[[gae]]"
  - "[[jains-fairness-index]]"
  - "[[zhou-2026-a2g-madrl-air-ground-vcs]]"
  - "[[liu-2021-edivert-mobile-crowdsensing]]"
  - "[[chi-harold-liu]]"
created: 2026-07-14
updated: 2026-07-14
---

# UAV Carrier Enabled Vehicular Crowdsensing by Multi-Agent Reinforcement Learning with Mutual Policy Divergence and Attentive Memory Update

## Citation

Zhao, Q., Liu, C. H., Zhao, J., Li, G., Qi, G., Ji, X., Xu, D., & Crowcroft, J. (2026). *UAV Carrier Enabled Vehicular Crowdsensing by Multi-Agent Reinforcement Learning with Mutual Policy Divergence and Attentive Memory Update*. **IEEE Transactions on Mobile Computing**, 1-18. DOI: 10.1109/TMC.2026.3693470.

## TL;DR

HADRL-VCS coordinates road-constrained UGV carriers with UAV scouts for urban vehicular crowdsensing. Attentive memory-integrated information exchange fuses link-qualified neighbor representations, prior memory, and sequentially announced actions, while mutual policy divergence-driven exploration encourages differentiated vehicle roles and continued per-agent exploration.

## Problem

UGVs can carry, recover, and recharge UAVs but are confined to roads and have limited sensing reach. UAVs can explore beyond that range, yet UAVs and UGVs differ in mobility, sensing responsibility, action spaces, observation spaces, and decision duration. The controller must coordinate these heterogeneous vehicles while balancing data collection, geographic fairness, UAV-enabled sensing expansion, overlap, and energy use.

## System model

- UGVs move between predefined road stops over multiple timeslots. Fixed-altitude UAVs move in a planar control space, avoid buildings above flight altitude, and may return to a UGV for recovery and charging.
- UAVs discover PoI locations and data information beyond UGV sensing range; UGVs subsequently move to PoIs and perform payload collection. The operational role split should not be summarized as UAV payload collection.
- Local observations include vehicle and PoI state only when sensing range and a reliable link permit it; unavailable components are zero-masked.
- The Dec-POMDP uses hybrid UAV flight/return actions and discrete UGV destination-stop actions. Active vehicles choose new actions, while inactive vehicles continue actions whose durations span multiple global timeslots.
- The episode metric multiplies data collection ratio, [[jains-fairness-index|Jain geographic fairness]], UAV-enabled sensing expansion, and an initial-to-consumed-energy factor. Overlap is evaluated separately. The displayed optimization constrains only nonnegative remaining energy; several feasibility and safety mechanisms instead reside in actions, the environment, or reward penalties.

## Method

[[attentive-memory-integrated-information-exchange|AMIE]] encodes local observations, exchanges hidden representations over link-qualified neighborhoods, attends to current environment/action messages, and combines them with persistent per-vehicle memory. Inactive vehicles announce continuing actions first; active vehicles then act in generated sequence and immediately share selected actions so later vehicles can condition on them.

[[mutual-policy-divergence-exploration|MPDE]] adds conditional Cauchy-Schwarz divergence terms between the current vehicle policy and both the previously updated vehicle's current policy and the same vehicle's previous-episode policy. Kernel-density estimates over representation-action trajectories approximate these terms, with a tunable coefficient balancing role differentiation against temporal policy diversity.

Training uses a global value network, [[gae|GAE]], randomized sequential actor updates, a clipped [[ppo|PPO]] objective, propagated modified advantages, and a clipped critic loss. This corresponds at the architecture level to [[centralized-training-decentralized-execution|CTDE]], although the method section does not explicitly label HADRL-VCS that way.

## Key findings

- On OpenStreetMap-derived Guangzhou and Madrid layouts, removing AMIE lowers Guangzhou efficiency from 10.6163 to 9.0027, a reported 15.19% drop; removing MPDE lowers Madrid efficiency from 10.5494 to 9.662, a reported 8.45% drop.
- Among six tested action-order configurations, dynamic-random ordering performs best on the listed metrics under the reported 12-UAV/6-UGV setting. This does not establish universal superiority for random ordering.
- The best tested MPDE balance coefficient differs by environment: 0.45 in Guangzhou and 0.4 in Madrid.
- HADRL-VCS is reported strongest against MASIA, RoMAT, HAPPO, LUDC, and Random across the plotted vehicle-count and sensing-range sweeps under a common active/inactive execution setting.
- In Guangzhou, raising message-loss probability from 0 to 0.4 lowers the composite efficiency from 10.6163 to 9.4199, and increasing imposed delay from 0 to four timeslots lowers it to 9.0795. These are empirical degradation measurements, not formal communication-robustness bounds.
- One sudden-PoI simulation reports all new PoIs discovered within 30 timeslots; the hotspot-aware experiments also favor HADRL-VCS on the two tested maps. Both use generated PoIs and demands rather than field sensor deployments.

## Limitations / guarantee scope

The study is simulation-only. Real map geometry is combined with synthetic PoI placement and 0.8-1.2 GB demands; UAV altitude is fixed, UGV routes use predefined stops, communication and onboard-compute energy are folded into baseline terms, and charging duration, charger capacity, docking uncertainty, and carrier assignment are not developed in detail. AMIE requires message exchange and an active-vehicle ordering, while MPDE adds quadratic-in-trajectory-length training cost.

No theorem, proof, global-optimality result, approximation ratio, monotonic-improvement result, safety guarantee, general asynchronous-network guarantee, or sim-to-real guarantee is established for HADRL-VCS. The reported “convergence analysis” consists of empirical training curves. The boundedness of conditional Cauchy-Schwarz divergence is invoked from prior work, and HAPPO/HATRPO guarantees discussed as related work do not transfer to this method. The controller uses current link-qualified messages; packet-loss/delay stress tests do not make AMIE a derived delay-aware protocol.

## Relation to the corpus

This source extends [[uav-assisted-mobile-crowd-sensing]] with a carrier-enabled UAV-UGV division of labor and heterogeneous action durations. It is closest to [[zhou-2026-a2g-madrl-air-ground-vcs]], which also coordinates UAVs and UGVs with sequential actions but targets AoI/latency and NOMA resource assignment. It also follows the energy/fairness-aware crowdsensing lineage of [[liu-2021-edivert-mobile-crowdsensing]]. AMIE specializes [[hidden-state-sharing-marl]] with attention, persistent memory, link qualification, and ordered action propagation, while MPDE adds a distinct policy-divergence exploration objective.

## Raw artifacts

- Parse: `raw/sources/UAV_Carrier_Enabled_Vehicular_Crowdsensing_by_Multi-Agent_Reinforcement_Learning_with_Mutual_Policy_Divergence_and_Attentive_Memory_Update/UAV_Carrier_Enabled_Vehicular_Crowdsensing_by_Multi-Agent_Reinforcement_Learning_with_Mutual_Policy_Divergence_and_Attentive_Memory_Update.md`
- Origin PDF: `raw/sources/UAV_Carrier_Enabled_Vehicular_Crowdsensing_by_Multi-Agent_Reinforcement_Learning_with_Mutual_Policy_Divergence_and_Attentive_Memory_Update/UAV_Carrier_Enabled_Vehicular_Crowdsensing_by_Multi-Agent_Reinforcement_Learning_with_Mutual_Policy_Divergence_and_Attentive_Memory_Update.pdf`
- Figures: `raw/sources/UAV_Carrier_Enabled_Vehicular_Crowdsensing_by_Multi-Agent_Reinforcement_Learning_with_Mutual_Policy_Divergence_and_Attentive_Memory_Update/images/`
