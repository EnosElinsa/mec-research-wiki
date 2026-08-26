# Model cards for battery-rotation UAV-MEC research

This document records full-text evidence for papers related to battery-aware UAV replacement, persistent aerial service, stateful service migration, and UAV-MEC resource control. Each card is based on the corresponding local Markdown full text, with bibliographic metadata checked against the first page of the local PDF. If a paper does not provide a mathematical model, objective function, decision variables, constraints, algorithm, or experiment, the card states so explicitly rather than reconstructing the missing material.

The relation table in each card uses the same seven dimensions: battery-triggered UAV replacement, stateful running service, replacement selection, finite standby pool and long-term rotation, source continuation during replacement flight, mobile A2A state synchronization, and source-UAV return-energy feasibility.

## Audit scope

- Twenty-eight papers in the current numbered literature table were audited one by one.
- The set includes three additional papers found during the source-corpus scan because they change the boundary assessment: [26]–[28].
- High-level journals support general methodological claims in the manuscript. Conference papers and other non-target venues remain here when they establish prior scenario coverage or a necessary boundary, but they should not be used as the sole support for general methodological claims.

## Cards

## [1] Live Migration of Stateful Microservices in UAV-Assisted Networks for Enhanced Availability

**Bibliographic verification**

- Authors: Sergio Frejo-Martín; Andrés García-López; Juan Manuel Murillo; Jaime Galán-Jiménez.
- Venue: 2025 IEEE Symposium on Computers and Communications $ISCC$.
- Year: 2025.
- DOI: [10.1109/ISCC65549.2025.11325941](https://doi.org/10.1109/ISCC65549.2025.11325941).
- Local artifacts: [PDF](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Live_Migration_of_Stateful_Microservices_in_UAV-Assisted_Networks_for_Enhanced_Availability/Live_Migration_of_Stateful_Microservices_in_UAV-Assisted_Networks_for_Enhanced_Availability.pdf); [Markdown](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Live_Migration_of_Stateful_Microservices_in_UAV-Assisted_Networks_for_Enhanced_Availability/Live_Migration_of_Stateful_Microservices_in_UAV-Assisted_Networks_for_Enhanced_Availability.md).
- Verification note: title, four-author list, venue/year, and DOI were checked against the rendered first page; parsed Markdown accents are partially corrupted, so PDF spelling is used.

**Model/evidence status**

- Mathematical model: **no mathematical model**. The proposal is an architecture and phase-based protocol, without variables, equations, an optimization problem, or analytical constraints.
- Algorithm: **none**. SMF orchestration, pre-copy, and container checkpoint operations are described, but no named algorithm or pseudocode is supplied.
- Evaluation: **use cases only**. Rural streaming, monitoring, and edge-caching examples are illustrative; simulation/testbed measurements are future work.
- Paper type: architecture/framework proposal and use-case conference paper.

**Scenario**

- Topology: a UAV swarm serves an Area of Interest; a ground Base Station contains an Intelligence Center $IC$ and charging infrastructure. The IC maintains a Digital Twin, Swarm Management Function $SMF$, and Central Image Server $CIS$. A replacement UAV flies from base toward the outgoing UAV's role/location.
- Nodes: service-hosting UAVs; one outgoing UAV; one fully charged replacement UAV; end users/IoT devices; IC/SMF/DT/CIS; charging facilities.
- Application: containerized stateful FANET microservices (video streaming, rural monitoring/analytics, edge caching).
- Assumptions: periodic UAV status reporting; low battery/technical failure detection; charged-UAV designation; role position/service specification; immutable/base-layer alignment before deployment; airborne UAV-to-UAV link for final checkpoint/layer transfer; sudden crashes out of scope.
- Multiple-access: **not specified**. No association, spectrum, MAC, or multiple-access scheme.
- Channel model: **not specified**. Rural line-of-sight is discussed, but no A2G/A2A propagation or rate model.

**Problem & objective**

**No optimization problem or objective function.** The qualitative goal is to maximize availability by minimizing handover downtime while preserving runtime state. Image layers are pre-copied; the outgoing container is halted, its checkpoint/layer transferred over an inter-UAV link, and the service restored on the newcomer. No objective equation or optimality criterion is supplied.

**Decision variables**

None. The architecture makes operational choices (for example, SMF designation of a charged UAV), but defines no mathematical decision variable, domain, or decision vector.

**Constraints**

No mathematical constraints. Layer consistency, container halt during final checkpoint, and inter-UAV-link availability are protocol preconditions rather than constraint families.

**Relation to our scenario**

| Element | Yes / No / Partial | Grounded interpretation |
|---|---|---|
| Battery-triggered UAV replacement | Yes | Low battery is an explicit replacement trigger monitored by the Digital Twin/SMF. |
| Stateful running service | Yes | CRIU checkpoints plus Docker layers preserve runtime/container state. |
| Replacement selection | Partial | SMF designates a charged UAV, but no candidate-set model, variable, ranking rule, or objective exists. |
| Finite standby pool and long-term rotation | Partial | Charged UAVs are available and the outgoing UAV returns, but pool size, charger capacity, recharge time, repeated-cycle state, and long-horizon rotation are absent. |
| Source continues during replacement flight | No | Source ceases service, checkpoints, and halts at replacement takeoff; downtime includes flight until A2A contact/restore. |
| Mobile A2A state synchronization | Partial | Final checkpoint/layer transfer uses airborne A2A after contact, but source is halted and no continuous synchronization/rate model is given. |
| Source-UAV return-energy constraint | No | Return is described, but no residual-energy reserve or return-feasibility constraint is formulated. |

**Full-text evidence**

## [2] Microservices migration: A pathway to improved energy efficiency in UAV networks

**Bibliographic verification**

- Authors: Santiago García-Gil; Diego Ramos-Ramos; Javier Berrocal; Juan Manuel Murillo; Jaime Galán-Jiménez.
- Venue: *Internet of Things*, Volume 30, Article 101463.
- Year: 2025 (available online 24 December 2024).
- DOI: [10.1016/j.iot.2024.101463](https://doi.org/10.1016/j.iot.2024.101463).
- Local artifacts: [PDF](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Microservices_Migration_A_Pathway_to_Improved_Energy_Efficiency_in_UAV_Networks/Microservices_Migration_A_Pathway_to_Improved_Energy_Efficiency_in_UAV_Networks.pdf); [Markdown](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Microservices_Migration_A_Pathway_to_Improved_Energy_Efficiency_in_UAV_Networks/Microservices_Migration_A_Pathway_to_Improved_Energy_Efficiency_in_UAV_Networks.md).
- Verification note: title, five-author list, journal/volume/article number, issue year, online date, and DOI were checked against the PDF first page.

**Model/evidence status**

- Mathematical model: **complete optimization**. Workload-dependent Raspberry Pi power/energy model and MILP Eq. (6) optimize per-slot microservice placement.
- Algorithm: **no formally named algorithm**. MILP is solved to optimality in each slot; no numbered pseudocode or distinct heuristic.
- Evaluation: **simulation**. Realistic 36-UAV rural scenario in 10-minute slots with random requests until infeasibility; request/UAV sensitivity and scalability are studied.
- Paper type: mathematical optimization and simulation research article.

**Scenario**

- Topology: UAV swarm graph $\mathcal G=(\mathcal N,\mathcal L)$; WiFi-equipped UAVs mesh with neighbors and use multi-hop forwarding. Ground IoT devices connect to their closest UAV.
- Nodes: UAVs with CPU, RAM, dedicated Raspberry Pi battery, and WiFi; cattle/hog IoT collars/eartags. No replacement UAV, standby pool, charging scheduler, base station, or cloud node is optimized.
- Application: rural intelligent-livestock IoT decomposed into Grazing Zone, Animal Geopositioning/Tracking, Animal Historic Record, and Interest Point microservices.
- Assumptions: undirected graph; LoS; 50 m altitude; 900 m interference-free spacing; closest-UAV association; 10-minute slots; 10,000 baseline requests/slot; threshold $b$ stops service and reserves energy for charging; dedicated Raspberry Pi battery models computing/network rather than propulsion.
- Multiple-access: **not specified**. WiFi traffic is modeled, but no FDMA/OFDMA/TDMA contention, spectrum allocation, or association optimization.
- Channel model: **no propagation/capacity model specified**. LoS and interference-free spacing are assumed; $r^u$ and $r^d$ are workload-generated empirical interface rates, not path-loss/SINR/bandwidth rates.

**Problem & objective**

- Problem: MILP Eq. (6), solved in each time window $t$; binary placement plus continuous slack/epigraph.
- Objective: $\max z$ (Eq. (6a)), where $z$ is no greater than every UAV's post-slot residual battery. This is max-min residual-battery balancing, indirectly maximizing operating epochs rather than minimizing total energy.
- Metric/semantics: least post-slot battery after CPU/WiFi use; migration is inferred when binary placement changes between slots. No migration-size, transfer-time, downtime, checkpoint, consistency, or runtime-state variable.

**Decision variables**

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Microservice placement | $x_{n_i,m_j}$ ($X$) | Binary, $\{0,1\}$ | 1 iff microservice $m_j$ is deployed on UAV $n_i$. |
| Worst residual-battery slack | $z$ | Continuous energy slack | Lower bound on every UAV's residual battery, maximized by Eq. (6a). |

**Constraints**

| ID | Meaning and key expression |
|---|---|
| (6b) | Replica completeness: $\sum_{n_i\in\mathcal N}x_{n_i,m_j}=d_{m_j}$. |
| (6c) | RAM: $\sum_{m_j}x_{n_i,m_j}c_{m_j}\le c_{n_i}$. |
| (6d) | CPU: deployed-service plus request-processing cycles $\le f_{n_i}$. |
| (6e) | Return reserve: $b_{n_i}-E(u_{n_i},r^u_{n_i},r^d_{n_i},t)\ge b$. |
| (6f) | Worst-battery epigraph: $b_{n_i}-E(u_{n_i},r^u_{n_i},r^d_{n_i},t)\ge z$. |

**Relation to our scenario**

| Element | Yes / No / Partial | Grounded interpretation |
|---|---|---|
| Battery-triggered UAV replacement | No | Threshold stops service and reserves return energy, but no replacement UAV is launched or selected. |
| Stateful running service | No | State is binary deployment only; no runtime/session state, checkpoint, consistency, or restore. |
| Replacement selection | No | No replacement candidates or decision. |
| Finite standby pool and long-term rotation | No | Slot re-optimization has no standby inventory, recharge process, or rotation. |
| Source continues during replacement flight | No | No replacement flight or overlap interval. |
| Mobile A2A state synchronization | No | Forwarding/placement changes contain no application-state synchronization or A2A transfer model. |
| Source-UAV return-energy constraint | Partial | Eq. (6e) reserves battery for every UAV to reach charging, but no source/replacement process exists. |

**Full-text evidence**

- Topology/assumptions: [line 72](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Microservices_Migration_A_Pathway_to_Improved_Energy_Efficiency_in_UAV_Networks/Microservices_Migration_A_Pathway_to_Improved_Energy_Efficiency_in_UAV_Networks.md:72), [line 76](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Microservices_Migration_A_Pathway_to_Improved_Energy_Efficiency_in_UAV_Networks/Microservices_Migration_A_Pathway_to_Improved_Energy_Efficiency_in_UAV_Networks.md:76), [line 82](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Microservices_Migration_A_Pathway_to_Improved_Energy_Efficiency_in_UAV_Networks/Microservices_Migration_A_Pathway_to_Improved_Energy_Efficiency_in_UAV_Networks.md:82), [line 92](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Microservices_Migration_A_Pathway_to_Improved_Energy_Efficiency_in_UAV_Networks/Microservices_Migration_A_Pathway_to_Improved_Energy_Efficiency_in_UAV_Networks.md:92).

## [3] Efficient Management of Composite Heterogeneous Applications at the Network Edge

**Bibliographic verification**

- Authors: Madhura Adeppady, Yenchia Yu, Ali Rahmanian, Ahmed Ali-Eldin Hassan, and Carla Fabiana Chiasserini.
- Venue: *IEEE Transactions on Network and Service Management*, vol. 23, 2026.
- Year: 2026 (received 2 October 2025; accepted 28 June 2026; published 2 July 2026; current version 4 August 2026).
- DOI: [10.1109/TNSM.2026.3709656](https://doi.org/10.1109/TNSM.2026.3709656).
- Local artifacts: [PDF](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Efficient_Management_of_Composite_Heterogeneous_Applications_at_the_Network_Edge/Efficient_Management_of_Composite_Heterogeneous_Applications_at_the_Network_Edge.pdf); [Markdown](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Efficient_Management_of_Composite_Heterogeneous_Applications_at_the_Network_Edge/Efficient_Management_of_Composite_Heterogeneous_Applications_at_the_Network_Edge.md).
- The title/authors/venue/dates/DOI were checked against the first page; PDF spelling is used because Markdown drops an “f” in “Efficient”.

**Model/evidence status**

- Mathematical model: **complete optimization**. MAP is NP-hard joint microservice placement, user-instance assignment, CPU allocation, and radio-RB allocation with latency/downtime constraints (13)–(24).
- Algorithm: **STEP (State and Topology-aware Edge-MS Placement)** builds/prunes a dynamic topology graph, expands it for feasibility, applies Dijkstra, and recalibrates CPU; Gurobi obtains exact small-case optima.
- Evaluation: **simulation + testbed**. Small cases compare Gurobi; large cases orchestrate on Kubernetes/Kind with mobility emulation and measured KPIs.
- Paper type: mathematical-optimization and edge-orchestration algorithm paper.

**Scenario**

- Topology: fixed edge servers linked by wired paths and associated with cellular BSs; mobile users (UAVs in experiments) access containerized microservice chains; handover can trigger migration among fixed servers.
- Nodes: mobile users/UAVs, BSs, fixed edge servers, orchestrator, application chains, and stateful/stateless instances. UAVs are clients, not replacements.
- Application: composite latency-sensitive applications; stateful instances retain session/interaction data and may transfer full containers or user state.
- Assumptions: entry microservice co-located with serving BS; changes occur at request/termination/handover; stateful versions remain fixed during migration; moves run in parallel; 50 Mbps reserved per transfer; downtime is maximum component downtime.
- Multiple access: no named MAC; integer radio-RB allocations per user-BS and per-BS capacity are modeled.
- Channel model: testbed bandwidth follows 3GPP TS 38.306 and distance-correlated CQI; SNR/CQI/MCS vary. Inter-server links are fixed wired; no A2A channel.

**Problem & objective**

- Problem: **Multi-microservice Application Placement $MAP$** at application start/stop or handover; mixed binary/integer/continuous nonconvex and NP-hard.
- Cost (1):
$$
C(y,z,\hat\tau,v)=\sum_{n,q,i,s>0}y_{s,i}^{n,q}\left(\frac{\mu_{n,q}}{M_s}+\frac{\hat\tau_{n,q}^{i}}{C_s}+\sum_{u,A_j}z_{u,i}^{n,q}\mathbf 1_{n=A_j[0]}\frac{B_{u,s}}{V_s\mathrm{MCS}_u}\right).
$$
- MAP objective (4a): $\min_{y,z,\hat\tau,v}\;\beta C(y,z,\hat\tau,v)-(1-\beta)Q(z),\;\beta\in[0,1]$, where $Q(z)$ is normalized application quality.
- Metrics: deployment cost/quality, response latency, downtime, request success, orchestration time, migration count, resource use, fairness.

**Decision variables**

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Microservice placement | $y_{s,i}^{n,q}$ | Binary | Instance $i$, microservice $n$, version $q$ on server $s$. |
| User-instance assignment | $z_{u,i}^{n,q}$ | Binary | User $u$ uses that instance/version. |
| CPU allocation | $\hat\tau_{n,q}^{i}$ | Continuous CPU cycles/s | CPU rate allocated to an instance. |
| Radio RB allocation | $v_{u,s}$ | Nonnegative integer | RB count between user $u$ and the BS co-located with server $s$. |

Current placement/assignment, statefulness, sharing, version demands, and latency/downtime limits are parameters.

**Constraints**

| ID | Meaning and key expression |
|---|---|
| (13) | $d_{u,A_j}^{\mathrm{proc}}+d_{u,A_j}^{\mathrm{com}}\le l_{A_j}$. |
| (14) | $D_{u,A_j}^{\mathrm{down}}<D_{A_j}$, using maximum relocation/container/user-state downtime. |
| (15)–(16) | Candidate instances are placed exactly once; unused instances use dummy server $s_0$. |
| (17)–(19) | Shareability and stateful non-shareable identity restrictions. |
| (20)–(21) | One instance/version per required microservice and entry-microservice co-location. |
| (22)–(24) | Per-server memory/CPU and per-BS radio capacity. |

**Relation to our scenario**

| Element | Yes / No / Partial | Grounded interpretation |
|---|---|---|
| Battery-triggered UAV replacement | No | UAVs are mobile users; no battery, low-energy trigger, incoming UAV, or replacement event. |
| Stateful running service | Yes | Stateful microservices preserve session state; container/user-state transfers have explicit downtime. |
| Replacement selection | Partial | MAP selects destination fixed server/instance/version/resources, not a replacement UAV. |
| Finite standby pool and long-term rotation | No | No standby inventory, charging/recovery state, finite fleet, or UAV duty rotation. |
| Source continues during replacement flight | No | No replacement flight; migration is between fixed servers. |
| Mobile A2A state synchronization | No | State moves over fixed wired links; no airborne endpoint or A2A synchronization. |
| Source-UAV return-energy constraint | No | UAV propulsion, reserve, and return energy are absent. |

**Full-text evidence**

- Scenario/migration trigger: [Markdown lines 86-100](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Efficient_Management_of_Composite_Heterogeneous_Applications_at_the_Network_Edge/Efficient_Management_of_Composite_Heterogeneous_Applications_at_the_Network_Edge.md:86).
- Testbed/channel abstraction: [lines 102-109](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Efficient_Management_of_Composite_Heterogeneous_Applications_at_the_Network_Edge/Efficient_Management_of_Composite_Heterogeneous_Applications_at_the_Network_Edge.md:102).
- Stateful semantics/transfer: [lines 198-251](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Efficient_Management_of_Composite_Heterogeneous_Applications_at_the_Network_Edge/Efficient_Management_of_Composite_Heterogeneous_Applications_at_the_Network_Edge.md:198).
- Variables/objective/constraints: [lines 218-293](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Efficient_Management_of_Composite_Heterogeneous_Applications_at_the_Network_Edge/Efficient_Management_of_Composite_Heterogeneous_Applications_at_the_Network_Edge.md:218).

- Exact constraints: [lines 556-618](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Efficient_Management_of_Composite_Heterogeneous_Applications_at_the_Network_Edge/Efficient_Management_of_Composite_Heterogeneous_Applications_at_the_Network_Edge.md:556).
- Evaluation scope: [lines 391-419](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Efficient_Management_of_Composite_Heterogeneous_Applications_at_the_Network_Edge/Efficient_Management_of_Composite_Heterogeneous_Applications_at_the_Network_Edge.md:391).

## [4] Time-Constrained Service Handoff for Mobile Edge Computing in 5G

**Bibliographic verification**

- Authors: Nafiseh Sharghivand, Lena Mashayekhy, Weibin Ma, and Schahram Dustdar.
- Venue: *IEEE Transactions on Services Computing*, vol. 16, no. 3, May/June 2023, pp. 2241-2253.
- Year: 2023 (published 22 September 2022; current version 12 June 2023).
- DOI: [10.1109/TSC.2022.3208783](https://doi.org/10.1109/TSC.2022.3208783).
- Local artifacts: [PDF](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Time-Constrained_Service_Handoff_for_Mobile_Edge_Computing_in_5G/Time-Constrained_Service_Handoff_for_Mobile_Edge_Computing_in_5G.pdf); [Markdown](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Time-Constrained_Service_Handoff_for_Mobile_Edge_Computing_in_5G/Time-Constrained_Service_Handoff_for_Mobile_Edge_Computing_in_5G.md).
- Title, authors, journal/volume/issue/year/pages, dates, and DOI were checked against the PDF first page.

**Model/evidence status**

- Mathematical model: **complete optimization**. SHIP$^3$ is a constrained shortest-path problem with path/link objectives, source/destination flow, handoff-time, and BS-energy constraints.
- Algorithm: **OSHM (Online Service Handoff Mechanism)**, comprising PPA (Pareto-label-correcting path planning) and a marginal-cost payment function; the general link problem is NP-hard.
- Evaluation: **simulation**. Python simulates a 1000 m × 1000 m two-tier 5G network with 10 MBSs, 50 SBSs, Poisson handoff arrivals, and measured MAR/OBJECT VM sizes; no physical testbed.
- Paper type: online constrained path-planning and mechanism-design paper.

**Scenario**

- Topology: two-tier 5G small-cell network; SBSs relay offloading and connect to adjacent SBSs over fronthaul and MBS/cloudlets over backhaul. Fixed BS nodes/links form a directed graph.
- Nodes: mobile users, SBSs, MBSs/cloudlets, Edge Manager, and fixed source/destination cloudlets. VM/container data traverses multi-hop paths; users are not compute servers.
- Application: low-latency VM/container services; handoff transfers a binary base-VM delta or user-specific data when already replicated.
- Assumptions: route/travel time known or predicted; endpoints predetermined; paths cycle-free; handoff must finish within coverage overlap.
- Multiple access: **multi-user OFDMA** with $C_j$ orthogonal RBs per BS, bandwidth $B_j^c$; RBs also model M/M/C servers.
- Channel model: OFDMA Shannon rates with transmit power, channel gain, AWGN, and inter-cell interference. Handoff time includes $d_i/R_l$ and BS queueing; no UAV/A2A channel.

**Problem & objective**

- Problems: SHIP$^3$ $path$, SHIP$^3$-M (constant-free), SHIP$^3$-L (binary link-flow); online constrained shortest path, link form NP-hard.
- Original objective (10): $\max_{p\in\mathcal P}\;v_e+v_m$, maximizing sequential social surplus with $v_m=\lambda_m(\theta_m-\tau_m)$.
- Link objective (13):
$$
\min_x \sum_{i\in\mathcal T}\sum_{l\in\mathcal L}x_l\left[\lambda_i^e(\tau_{j^+}^{\prime q}-\tau_{j^+}^{q})+(\lambda_m^e+\lambda_m)(\tau_m^l+\tau_{j^+}^{q})\right].
$$
- Metrics: link workload, handoff duration, BS energy, unassigned-user ratio, path cost, payment/utility; OSHM reports at least 61% lower workload, 33% lower handoff time, and 29% lower energy than online baselines.

**Decision variables**

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Handoff path | $p$ | Discrete, $p\in\mathcal P$ | Cycle-free sequence of fixed BS nodes/links from source $o$ to destination $d$. |
| Link selection | $x_l$ | Binary | 1 iff fixed link $l$ lies on the selected path. |

Payment $\pi_m$ is computed after path selection; powers, RBs, rates, route, VM size, and energy budgets are parameters.

**Constraints**

| ID | Meaning and key expression |
|---|---|
| (10a)/(12) | Handoff duration deadline $\tau_m\le\theta_m$. |
| (10b)/(12) | Selected path satisfies remaining transmission-energy budget $e_j^{ml}\le\bar\epsilon_j$. |
| (13a)–(13c) | One outgoing source link, one incoming destination link, and flow conservation at intermediate BSs. |
| (13d) | Link transmission plus node-queue time $\le\theta_m$. |
| (13e) | Selected-link energy within each BS's remaining budget. |
| (13f) | $x_l\in\{0,1\}$. |

**Relation to our scenario**

| Element | Yes / No / Partial | Grounded interpretation |
|---|---|---|
| Battery-triggered UAV replacement | No | Trigger is user movement between cloudlet coverages, not UAV low battery. |
| Stateful running service | Partial | VM/container delta or user data is handed off, but evolving runtime state, dirty pages, consistency, and live synchronization are abstracted. |
| Replacement selection | No | Destination cloudlet is fixed; only fixed-network path is optimized. |
| Finite standby pool and long-term rotation | No | No replacement inventory, charging, fleet rotation, or multi-cycle state. |
| Source continues during replacement flight | No | No replacement UAV/flight; handoff window follows coverage overlap. |
| Mobile A2A state synchronization | No | Data traverses fixed SBS/MBS fronthaul/backhaul, not airborne A2A. |
| Source-UAV return-energy constraint | No | BS transmission-energy budgets exist, but UAV propulsion/return energy is absent. |

**Full-text evidence**

- Handoff transfer: [Markdown lines 11-19](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Time-Constrained_Service_Handoff_for_Mobile_Edge_Computing_in_5G/Time-Constrained_Service_Handoff_for_Mobile_Edge_Computing_in_5G.md:11).
- Fixed infrastructure/purpose: [lines 25-37](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Time-Constrained_Service_Handoff_for_Mobile_Edge_Computing_in_5G/Time-Constrained_Service_Handoff_for_Mobile_Edge_Computing_in_5G.md:25).
- Topology/mobility window: [lines 66-100](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Time-Constrained_Service_Handoff_for_Mobile_Edge_Computing_in_5G/Time-Constrained_Service_Handoff_for_Mobile_Edge_Computing_in_5G.md:66).

- OFDMA/channel/objectives/constraints: [lines 102-191](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Time-Constrained_Service_Handoff_for_Mobile_Edge_Computing_in_5G/Time-Constrained_Service_Handoff_for_Mobile_Edge_Computing_in_5G.md:102).
- Simulation/results: [lines 290-339](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Time-Constrained_Service_Handoff_for_Mobile_Edge_Computing_in_5G/Time-Constrained_Service_Handoff_for_Mobile_Edge_Computing_in_5G.md:290).

## [5] ReSync: Coordinated Live-Migration for Stateful Containers in Mobile Edge Computing

**Bibliographic verification**

- Authors: Reinhard Scheuer; Yibo Pi; Xudong Wang.
- Venue: *IEEE Transactions on Mobile Computing*, accepted author version.
- Year: 2026.
- DOI: 10.1109/TMC.2026.3716750.
- Local files: [PDF]$/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/ReSync_Coordinated_Live-Migration_for_Stateful_Containers_in_Mobile_Edge_Computing/ReSync_Coordinated_Live-Migration_for_Stateful_Containers_in_Mobile_Edge_Computing.pdf$; [Markdown]$/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/ReSync_Coordinated_Live-Migration_for_Stateful_Containers_in_Mobile_Edge_Computing/ReSync_Coordinated_Live-Migration_for_Stateful_Containers_in_Mobile_Edge_Computing.md$. Title, authors, venue, copyright, and DOI were checked against the PDF first page.

**Model/evidence status**

- Mathematical model: **partial analysis**. Two concurrent batch-service FIFO queues analyze replay-synchronization stability/convergence; no system-level optimization is formulated.
- Algorithm: **ReSync migration workflow** and **Algorithm 1: ReSync Coordinator's Migration Trigger Procedure based on the A3 Handover Model**. RSSI extrapolation and TTT trigger migration; this is not an optimization solver.
- Evaluation: **testbed + simulation**. A real MEC testbed is combined with high-mobility SUMO/ns-3 simulation.
- Paper type: systems architecture, protocol, implementation, and experiments with partial performance analysis.

**Scenario**

- Topology: urban 5G MEC with BSs attached to two adjacent MEC-area MEHs. Inter-MEH handover migrates a container from source to destination MEH. MEO/ReSync coordinator and migration controllers coordinate both ends; testbed uses two Wi-Fi APs, two edge hosts, and a management node.
- Nodes: UE, serving/target BS or AP, source/destination MEH, MEO, MEPM/MEP, migration and replay controllers.
- Application: CRIU-compatible stateful containers; YOLOv8 object detection and DeepFace recognition write inference results to files/runtime variables as state.
- Assumptions: common base image; source resumes immediately after checkpoint; FIFO buffering/forwarding/replay; replay requires deterministic application behavior (or nondeterministic events that do not affect output state); duration depends on application/network conditions and conservative empirical estimates.
- Multiple-access: **no multi-access model specified**. Testbed uses 2.4 GHz Wi-Fi APs; no OFDMA/TDMA/NOMA allocation.
- Channel model: **no analytical wireless model**. Testbed configures UE–MEH, MEH–MEH, and MEH–MEO bandwidth/RTT; extended simulation uses 3GPP urban-macro path loss with shadowing, noise, L3 filtering, and A3 handover.

**Problem & objective**

- **No optimization problem or objective function**, and no P0/P1 identifiers.
- Engineering goals: shorter service downtime, alignment of handover-ready window with handover, and acceptable total migration time. Metrics include downtime, total migration time, end-to-end delay, migration lead time, and coordination success.
- Eqs. (1)–(15) analyze input arrival, cross-host forwarding, and destination replay queue stability/convergence; they do not form an optimization model.

**Decision variables**

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| None | — | — | No optimization variables. BW, $\lambda_{arr}$, $S_{in}$, $S_{cp}$, $\mu_{rep}$, RSSI, TTT, and threshold are measurements/parameters used by the trigger. |

**Constraints**

Queue-analysis conditions and coordination rules, **not optimization constraint families**:

| ID | Meaning and key expression |
|---|---|
| (2), buffer stability | $\lambda_{arr}<\lambda_{trans}$, with $\lambda_{trans}=BW/S_{in}$. |
| (7)/(8), fast convergence | $N_0^{buf}\le1/\alpha$, equivalently $S_{cp}S_{in}\lambda_{arr}^2/BW^2\le1$. |
| (10), replay stability | $\lambda_{arr}<\mu_{rep}$. |
| Algorithm 1 trigger | $\hat R_{target}>\hat R_{serv}+\Delta_{thresh}$ for one TTT sends migration-start; trigger logic is not feasibility. |

**Relation to our scenario**

| Element | Yes / No / Partial | Grounded interpretation |
|---|---|---|
| Battery-triggered UAV replacement | No | Trigger is UE mobility/A3 handover, not UAV low battery. |
| Stateful running service | Yes | Checkpoint/restore, input buffering, and replay preserve running-container state. |
| Replacement selection | No | Source/target MEHs come from external orchestration; no replacement-node variable or algorithm. |
| Finite standby pool and long-term rotation | No | No standby pool, charging state, or cross-cycle rotation. |
| Source continues during replacement flight | Partial | Source resumes after checkpoint and serves while destination catches up; MEHs are fixed and no UAV flies. |
| Mobile A2A state synchronization | No | State synchronizes over fixed MEH networks, not a mobile UAV-to-UAV link. |
| Source-UAV return-energy constraint | No | No UAV flight or return-energy model. |

**Full-text evidence**

1. [Scenario and fixed MEH topology: line 11]$/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/ReSync_Coordinated_Live-Migration_for_Stateful_Containers_in_Mobile_Edge_Computing/ReSync_Coordinated_Live-Migration_for_Stateful_Containers_in_Mobile_Edge_Computing.md:11$.
2. [Source continuation and synchronization: lines 68–74]$/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/ReSync_Coordinated_Live-Migration_for_Stateful_Containers_in_Mobile_Edge_Computing/ReSync_Coordinated_Live-Migration_for_Stateful_Containers_in_Mobile_Edge_Computing.md:68$.
3. [Coordination algorithm: lines 107–130]$/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/ReSync_Coordinated_Live-Migration_for_Stateful_Containers_in_Mobile_Edge_Computing/ReSync_Coordinated_Live-Migration_for_Stateful_Containers_in_Mobile_Edge_Computing.md:107$.
4. [Variables and buffer conditions: lines 141–175]$/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/ReSync_Coordinated_Live-Migration_for_Stateful_Containers_in_Mobile_Edge_Computing/ReSync_Coordinated_Live-Migration_for_Stateful_Containers_in_Mobile_Edge_Computing.md:141$.
5. [Replay stability/convergence: lines 198–249]$/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/ReSync_Coordinated_Live-Migration_for_Stateful_Containers_in_Mobile_Edge_Computing/ReSync_Coordinated_Live-Migration_for_Stateful_Containers_in_Mobile_Edge_Computing.md:198$.
6. [Testbed/network: lines 269–291]$/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/ReSync_Coordinated_Live-Migration_for_Stateful_Containers_in_Mobile_Edge_Computing/ReSync_Coordinated_Live-Migration_for_Stateful_Containers_in_Mobile_Edge_Computing.md:269$.

7. [Experimental conclusions: lines 326–349]$/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/ReSync_Coordinated_Live-Migration_for_Stateful_Containers_in_Mobile_Edge_Computing/ReSync_Coordinated_Live-Migration_for_Stateful_Containers_in_Mobile_Edge_Computing.md:326$.
8. [Applicability boundary: line 377]$/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/ReSync_Coordinated_Live-Migration_for_Stateful_Containers_in_Mobile_Edge_Computing/ReSync_Coordinated_Live-Migration_for_Stateful_Containers_in_Mobile_Edge_Computing.md:377$.

## [6] CORMO-RAN: Energy Efficiency at the Near-RT RIC via Lossless Migration of O-RAN xApps

**Bibliographic verification**

- Authors: Antonio Calagna, Stefano Maxenti, Leonardo Bonati, Salvatore D'Oro, Tommaso Melodia, and Carla Fabiana Chiasserini.
- Venue: *IEEE Transactions on Mobile Computing*, accepted author version.
- Year: 2026 (accepted manuscript; final volume/issue/pages are not printed in the local PDF).
- DOI: [10.1109/TMC.2026.3715058](https://doi.org/10.1109/TMC.2026.3715058).
- Local artifacts: [PDF](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/CORMO-RAN_Energy_Efficiency_at_the_Near-RT_RIC_via_Lossless_Migration_of_O-RAN_xApps/CORMO-RAN_Energy_Efficiency_at_the_Near-RT_RIC_via_Lossless_Migration_of_O-RAN_xApps.pdf); [Markdown](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/CORMO-RAN_Energy_Efficiency_at_the_Near-RT_RIC_via_Lossless_Migration_of_O-RAN_xApps/CORMO-RAN_Energy_Efficiency_at_the_Near-RT_RIC_via_Lossless_Migration_of_O-RAN_xApps.md).
- Title, six-author list, accepted-journal status, and DOI were checked against the first page; no final volume/issue/pages are inferred.

**Model/evidence status**

- Mathematical model: **complete optimization**. Calibrated temporal/resource models formulate SAL, a joint server-activation and lossless stateful-xApp migration MIQP with allocation, activation, resource, downtime, and SDL consistency constraints.
- Algorithm: **CORMO-RAN** is the rApp framework; SAL uses Gurobi branch-and-bound/cutting planes. No separate named approximation algorithm.
- Evaluation: **testbed + optimization study**. Real O-RAN/OpenShift measurements calibrate models; MATLAB/Gurobi evaluates allocation, feasibility, runtime, and energy savings.
- Paper type: measurement-driven systems and MIQP optimization paper with O-RAN testbed.

**Scenario**

- Topology: fixed near-RT RIC compute cluster on a 10 Gbps SDN switch. A non-RT RIC rApp reallocates xApps across fixed servers and powers dispensable servers down under low RAN load.
- Nodes: near-RT RIC servers, non-RT RIC/CORMO-RAN rApp, stateful xApp containers, RAN nodes/RUs/UEs, and distributed etcd backend for SDL; these are not UAV edge servers.
- Application: stateful O-RAN xApps ingest RAN KPMs and issue control messages (DRL scheduling and KPM-monitoring examples); internal context history must be preserved.
- Assumptions: identical resource-constrained servers; master/fundamental-service servers always on; periodic $\Delta T$ slots (event triggers allowed); measured SM migrates sequentially; each run specifies $\tau\in\{\mathrm{SDL},\mathrm{SM\text{-}MR},\mathrm{SM\text{-}MD}\}$.
- Multiple access: no radio MAC/resource-allocation decision; KPM/control messages are workload inputs while optimization covers compute placement/activation.
- Channel model: no propagation, fading, SINR, or mobile model. Fixed Ethernet/SDN links (10 Gbps) and migration-bandwidth caps; not A2A.

**Problem & objective**

- Problem: **SAL (joint Server Activation and Lossless stateful xApp migration)**.
- Type: MIQP with integer xApp-flow and binary activation variables; stated NP-hard and solved by branch-and-bound when tractable.
- Objective:
  $$
  \min_{\mathbf x,\boldsymbol\mu}\sum_{s\in\mathcal S}E_s,
  $$
  where Eq. (11) includes migration/SDL, migration/instantiation, idle, and xApp execution energy over $\Delta T$.
- Metrics: cluster energy, activation ratio, migration downtime/duration, SDL defragmentation downtime, CPU/memory/disk use, MIP gap, runtime, and strategy feasibility.

**Decision variables**

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Server activation | $\mu_s$ | Binary | 1 if fixed server remains active; 0 if switched off. |
| xApp allocation/migration flow | $x_{k,s,s'}$ | Nonnegative integer | Number of class-k xApps moved from s to s'; equal indices mean retained, unequal means migrated. |

Virtual-server/new-xApp counts, initial activation, switchability $\alpha_s$, strategy $\tau$, and measured coefficients are parameters; $\tau$ is specified rather than optimized.

**Constraints**

| ID | Meaning and key expression |
|---|---|
| (12) | Conservation of initially active/virtual xApp counts. |
| (13)–(14) | No xApp remains on virtual server; each new class-k xApp is assigned to a real server. |
| (15) | Migration originates only from a server active at slot start. |
| (16)–(17) | xApps only on $\mu_s=1$ servers; active server must host xApps with always-on rule. |
| (18) | $R_{\chi_s}^{\tau}\le R_{\chi_s}^{\max}\mu_s$ for CPU, memory, and disk. |
| (19) | Always-on $\mu_s\ge1-\alpha_s$; only switchable servers may shut down. |
| (20)–(22) | Migration/SDL downtime limits and positive active interval $T_{active}=\nu-T_{DF}^{SDL}>0$. |

**Relation to our scenario**

| Element | Yes / No / Partial | Grounded interpretation |
|---|---|---|
| Battery-triggered UAV replacement | No | Workload/traffic switches fixed servers; no UAV battery, depletion, or replacement flight. |
| Stateful running service | Yes | Stateful xApps preserve live state; SM transfers execution/memory/socket state and SDL uses strongly consistent external state. |
| Replacement selection | Partial | $x_{k,s,s'}$ selects destination fixed server and $\mu_s$ active servers, not a replacement UAV. |
| Finite standby pool and long-term rotation | No | Finite servers/repeated slots are not a standby/recharging UAV pool or duty rotation. |
| Source continues during replacement flight | No | No flight; overlap occurs on fixed hosts. |
| Mobile A2A state synchronization | No | State moves/shared within fixed RIC over Ethernet/SDN and etcd, not mobile A2A. |
| Source-UAV return-energy constraint | No | Energy concerns fixed-cluster electricity; UAV propulsion/return reserve is absent. |

**Full-text evidence**

- RIC/xApp scenario: [Markdown lines 21-53](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/CORMO-RAN_Energy_Efficiency_at_the_Near-RT_RIC_via_Lossless_Migration_of_O-RAN_xApps/CORMO-RAN_Energy_Efficiency_at_the_Near-RT_RIC_via_Lossless_Migration_of_O-RAN_xApps.md:21).
- Stateful migration/source continuation: [lines 72-82](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/CORMO-RAN_Energy_Efficiency_at_the_Near-RT_RIC_via_Lossless_Migration_of_O-RAN_xApps/CORMO-RAN_Energy_Efficiency_at_the_Near-RT_RIC_via_Lossless_Migration_of_O-RAN_xApps.md:72).
- SDL overlap/consistency: [lines 84-95](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/CORMO-RAN_Energy_Efficiency_at_the_Near-RT_RIC_via_Lossless_Migration_of_O-RAN_xApps/CORMO-RAN_Energy_Efficiency_at_the_Near-RT_RIC_via_Lossless_Migration_of_O-RAN_xApps.md:84).
- Testbed/fixed links: [lines 97-115](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/CORMO-RAN_Energy_Efficiency_at_the_Near-RT_RIC_via_Lossless_Migration_of_O-RAN_xApps/CORMO-RAN_Energy_Efficiency_at_the_Near-RT_RIC_via_Lossless_Migration_of_O-RAN_xApps.md:97).
- State/variables: [lines 247-292](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/CORMO-RAN_Energy_Efficiency_at_the_Near-RT_RIC_via_Lossless_Migration_of_O-RAN_xApps/CORMO-RAN_Energy_Efficiency_at_the_Near-RT_RIC_via_Lossless_Migration_of_O-RAN_xApps.md:247).
- Temporal/energy models: [lines 294-337](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/CORMO-RAN_Energy_Efficiency_at_the_Near-RT_RIC_via_Lossless_Migration_of_O-RAN_xApps/CORMO-RAN_Energy_Efficiency_at_the_Near-RT_RIC_via_Lossless_Migration_of_O-RAN_xApps.md:294), [lines 361-395](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/CORMO-RAN_Energy_Efficiency_at_the_Near-RT_RIC_via_Lossless_Migration_of_O-RAN_xApps/CORMO-RAN_Energy_Efficiency_at_the_Near-RT_RIC_via_Lossless_Migration_of_O-RAN_xApps.md:361).

- SAL constraints/MIQP: [lines 397-457](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/CORMO-RAN_Energy_Efficiency_at_the_Near-RT_RIC_via_Lossless_Migration_of_O-RAN_xApps/CORMO-RAN_Energy_Efficiency_at_the_Near-RT_RIC_via_Lossless_Migration_of_O-RAN_xApps.md:397).
- Solver/evaluation: [lines 459-482](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/CORMO-RAN_Energy_Efficiency_at_the_Near-RT_RIC_via_Lossless_Migration_of_O-RAN_xApps/CORMO-RAN_Energy_Efficiency_at_the_Near-RT_RIC_via_Lossless_Migration_of_O-RAN_xApps.md:459).

## [7] Context-Aware AIGC Service Migration in Edge Intelligence Networks via Transformer DRL

**Bibliographic verification**

- Authors: Jiaxi Wang, Yixue Hao, Rui Wang, Long Hu, Kaibin Huang, Dusit Niyato, and Min Chen.
- Venue: *IEEE Transactions on Services Computing*, vol. 19, no. 2, March/April 2026, pp. 1020-1033.
- Year: 2026 (published 22 January 2026; current version 10 April 2026).
- DOI: [10.1109/TSC.2026.3656910](https://doi.org/10.1109/TSC.2026.3656910).
- Local artifacts: [PDF](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Context-Aware_AIGC_Service_Migration_in_Edge_Intelligence_Networks_via_Transformer_DRL/Context-Aware_AIGC_Service_Migration_in_Edge_Intelligence_Networks_via_Transformer_DRL.pdf); [Markdown](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Context-Aware_AIGC_Service_Migration_in_Edge_Intelligence_Networks_via_Transformer_DRL/Context-Aware_AIGC_Service_Migration_in_Edge_Intelligence_Networks_via_Transformer_DRL.md).
- Title, seven-author list, journal/volume/issue/year/pages, dates, and DOI were checked against the PDF first page.

**Model/evidence status**

- Mathematical model: **complete optimization**. P1 is a finite-horizon weighted-utility problem with accuracy, context-migration cost, wireless transmission, inter-edge migration, and transformer-computation latency models plus five constraints.
- Algorithm: **TFSCM (TransFormer-based Soft Actor-Critic for Context-aware AIGC service Migration)**, an MDP whose SAC actor is replaced by a Transformer over historical states, with dual critics/targets and replay.
- Evaluation: **simulation** using Telecom Shanghai mobility traces, simulated grid AIGC servers, CogView2 parameters, RTX 3090 training, and six baselines; no deployed migration testbed.
- Paper type: DRL-based mathematical optimization with trace-driven simulation.

**Scenario**

- Topology: one mobile user moves among fixed high-capability edge servers, each hosting the same generalized AIGC model. Nearest server is access; previous or current access server executes requests.
- Nodes: mobile user/device, fixed access/host servers, routers/hops, and predeployed models. No UAV/replacement node.
- Application: continuous AIGC tasks (music/news/video/game-scene generation). Migrated artifact is recent request/generated-content context windows reconstructed by the destination model via in-context learning.
- Assumptions: one customized user; model on every server; each slot routes to previous host or migrates selected recent windows to current access server; no internal semantic filtering; 10-minute-to-one-hour slots; context length limited by model.
- Multiple access: no named MAC or multi-user allocation; single-user uplink/downlink bandwidth and power are fixed.
- Channel model: $B\log_2(1+p/(\sigma^2d^{\iota}))$ wireless rate with Gaussian noise/distance loss; fixed-server migration uses hop count, forwarding rate, geodesic distance, and broadcast speed. No fading/interference/A2A channel.

**Problem & objective**

- Problem: $\mathcal P_1$, joint service/context migration over slots; finite-horizon mixed discrete dynamic optimization, stated NP-hard and reformulated as an MDP.
- Utility/problem:
  $$
  \mathcal F=\mu_1A-\mu_2C-\mu_3D,\qquad \mathcal P_1:\max_{u,b}\mathcal F,
  $$
  where $A$ is average inference accuracy, $C$ context-migration cost, and $D$ total latency.
- DRL objective (19): maximize discounted reward plus SAC entropy; each reward is the same utility.
- Metrics: utility, accuracy, end-to-end latency, migration cost, reward/convergence, training/inference time, and context/trace/edge-density sensitivity.

**Decision variables**

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Service/context mode | $u(t)$ | Binary $\{0,1\}$ (displayed C1 writes $[0,1]$) | 0 routes to previous host; 1 migrates context to current access server. |
| Context-window count | $b(t)$ | Integer $0\le b(t)\le\Omega_t$ | Number of recent windows migrated. |
| Host server | $y_t$ | Induced discrete choice | Restricted to previous host $y_{t-1}$ or current access server $x_t$. |
| MDP action | $a_t$ | Discrete $\{0,1,\ldots,\Omega+1\}$ | $a_t=0$ means no migration; $a_t>0$ gives $b(t)=a_t-1$. |

Access server, trajectory, context availability, data lengths, compute frequency, bandwidth/power, and network constants are state/parameters.

**Constraints**

| ID | Meaning and key expression |
|---|---|
| C1 | Binary strategy $u(t)\in\{0,1\}$; displayed P1 line uses $[0,1]$, an internal inconsistency. |
| C2/(11) | $0\le b(t)\le\Omega_t$. |
| C3/(12) | $\Omega_t\le\Omega$. |
| C4/(13) | $y_t\in\{y_{t-1},x_t\}$. |
| C5/(14) | $D(t)<\tau_{\max}$. |

No server-capacity, contention, battery, flight, or return-energy constraint is included.

**Relation to our scenario**

| Element | Yes / No / Partial | Grounded interpretation |
|---|---|---|
| Battery-triggered UAV replacement | No | Migration follows changing user access/context utility; no serving UAV or battery trigger. |
| Stateful running service | Partial | User contextual memory is preserved, but explicit history—not container/model/checkpoint/live state—is migrated. |
| Replacement selection | No | Destination is previous host or current access server; no replacement-UAV candidate. |
| Finite standby pool and long-term rotation | No | Fixed servers are not a standby/recharge fleet and have no duty-cycle state. |
| Source continues during replacement flight | No | No replacement flight; previous-host routing is an alternative to migration. |
| Mobile A2A state synchronization | No | Context crosses fixed-server hops with no mobile A2A or convergence model. |
| Source-UAV return-energy constraint | No | No UAV battery, propulsion, base return, or reserve. |

**Full-text evidence**

- Motivation/context: [Markdown lines 7-23](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Context-Aware_AIGC_Service_Migration_in_Edge_Intelligence_Networks_via_Transformer_DRL/Context-Aware_AIGC_Service_Migration_in_Edge_Intelligence_Networks_via_Transformer_DRL.md:7).
- Topology/roles and $u(t),b(t)$: [lines 65-77](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Context-Aware_AIGC_Service_Migration_in_Edge_Intelligence_Networks_via_Transformer_DRL/Context-Aware_AIGC_Service_Migration_in_Edge_Intelligence_Networks_via_Transformer_DRL.md:65).
- Context state/bounds: [lines 79-90](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Context-Aware_AIGC_Service_Migration_in_Edge_Intelligence_Networks_via_Transformer_DRL/Context-Aware_AIGC_Service_Migration_in_Edge_Intelligence_Networks_via_Transformer_DRL.md:79).
- Migration cost: [lines 102-118](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Context-Aware_AIGC_Service_Migration_in_Edge_Intelligence_Networks_via_Transformer_DRL/Context-Aware_AIGC_Service_Migration_in_Edge_Intelligence_Networks_via_Transformer_DRL.md:102).
- Channel/latency: [lines 120-158](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Context-Aware_AIGC_Service_Migration_in_Edge_Intelligence_Networks_via_Transformer_DRL/Context-Aware_AIGC_Service_Migration_in_Edge_Intelligence_Networks_via_Transformer_DRL.md:120).
- Objective/constraints/NP-hardness: [lines 160-200](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Context-Aware_AIGC_Service_Migration_in_Edge_Intelligence_Networks_via_Transformer_DRL/Context-Aware_AIGC_Service_Migration_in_Edge_Intelligence_Networks_via_Transformer_DRL.md:160).

- MDP/TFSCM: [lines 202-254](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Context-Aware_AIGC_Service_Migration_in_Edge_Intelligence_Networks_via_Transformer_DRL/Context-Aware_AIGC_Service_Migration_in_Edge_Intelligence_Networks_via_Transformer_DRL.md:202).
- Trace-driven simulation: [lines 289-315](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Context-Aware_AIGC_Service_Migration_in_Edge_Intelligence_Networks_via_Transformer_DRL/Context-Aware_AIGC_Service_Migration_in_Edge_Intelligence_Networks_via_Transformer_DRL.md:289).

## [8] TOM: Joint Trajectory, Offloading and Migration Optimization in Stateful Service-Oriented UAV-Enabled VEC System

**Bibliographic verification**

- Authors: Qijie Qiu, Lingjie Li, Zhijiao Xiao, Qiuzhen Lin, Lijia Ma, and Zhong Ming.
- Venue: *IEEE Transactions on Services Computing*, vol. 18, no. 6, Nov./Dec. 2025.
- Year: 2025 (published 7 August 2025; current version 11 December 2025).
- DOI: [10.1109/TSC.2025.3596889](https://doi.org/10.1109/TSC.2025.3596889).
- Local artifacts: [PDF](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/TOM_Joint_Trajectory_Offloading_and_Migration_Optimization_in_Stateful_Service-Oriented_UAV-Enabled_VEC_System/TOM_Joint_Trajectory_Offloading_and_Migration_Optimization_in_Stateful_Service-Oriented_UAV-Enabled_VEC_System.pdf); [Markdown](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/TOM_Joint_Trajectory_Offloading_and_Migration_Optimization_in_Stateful_Service-Oriented_UAV-Enabled_VEC_System/TOM_Joint_Trajectory_Offloading_and_Migration_Optimization_in_Stateful_Service-Oriented_UAV-Enabled_VEC_System.md).
- Title, author list, venue/year, and DOI were checked against the first page of the local publisher PDF.

**Model/evidence status**

- Mathematical model: **complete optimization**. 3-D UAV/VEC system, offloading, trajectory, and stateful migration equations define dynamic multiobjective P0 with constraints (17)–(22).
- Algorithm: **TOM (joint Trajectory, Offloading, and Migration optimization)**, a dynamic multifactorial evolutionary algorithm with heuristic initialization, three mutations, parallel migration, and environmental adaptation.
- Evaluation: **simulation** with real taxi $TTD$ and electric-vehicle $EVD$ trajectories, six scales, baselines, ablations, and migration-strategy tests.
- Paper type: dynamic multiobjective mathematical-optimization algorithm paper.

**Scenario**

- Topology: 3-D UAV-enabled vehicular edge computing; $J$ mobile UAV nodes serve $I$ moving vehicles in slots. Vehicles offload to nearest UAV and cache the corresponding service there.
- Nodes: UAVs, vehicles, stateful services/VMs, vehicle-UAV and UAV-UAV links. No depot, standby pool, or replacement role.
- Application: stateful vehicular services, motivated by autonomous driving where position, speed, route, and sensor context persist.
- Assumptions: one service per vehicle task; positions update per slot; each UAV migrates at most one service uplink and receives one downlink per slot; groups serialize internally and run in parallel; extra waiting/execution flight is negligible.
- Multiple access: **TDMA** for vehicle-to-nearest-UAV transmission.
- Channel model: A2G path loss/SINR/Shannon rate $H_{i\hat j}(t)=(4\pi\Gamma/c)^2d_{i\hat j}(t)^\alpha$, $\mathrm{SINR}_{i\hat j}=P^tg^2/(N_0H_{i\hat j})$, $R_{i\hat j}=B_{i\hat j}\log_2(1+\mathrm{SINR}_{i\hat j})$. Inter-UAV migration bandwidth $R_{jj'}(t)$ is used, but no separate A2A propagation/fading model.

**Problem & objective**

- Problem P0: joint UAV trajectory, computation offloading, and stateful service migration; dynamic multiobjective optimization.
- Objective: $\mathbb P0=\min_{L_j,\theta_i,PSG}\{FC,EC,AoI,MT\}$, where $FC$ is flight cost, $EC$ local-computing energy, $AoI=\sum_{i,t}Delay_i^{edge}(t)$, and $MT=\sum_t\max_m MT_m(t)$.
- Metrics: HV, Pareto-solution count, pure diversity, normalized four-objective score $F$, and migration time versus FCFS.

**Decision variables**

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV trajectory/location | $L_j(t)=(x_j^{uav},y_j^{uav},z_j^{uav})$ | Continuous 3-D; movement bounded by (21) | UAV $j$'s position in slot $t$. |
| Offloading fraction | $\theta_i(t)$ | Continuous $[0,1]$ | Fraction of vehicle $i$'s task offloaded to nearest UAV. |
| Parallel migration plan | $PSG$ | Discrete grouping/ordering | Serial groups that run in parallel without resource conflicts. |

Fair CPU $f_{i\hat j}$, VM memory $o_k$, bandwidth $B_{i\hat j}$, and inter-UAV bandwidth $R_{jj'}$ are computed or parameters.

**Constraints**

| ID | Meaning and key expression |
|---|---|
| (17) | $\theta_i\in[0,1]$. |
| (18) | $\sum_i f_{i\hat j}\le O_{\hat j}$. |
| (19) | $\sum_{k=1}^{M_j}o_k\le F_j$. |
| (20) | $Delay_i^{local}(t)+Delay_i^{edge}(t)\le\psi_i$. |
| (21) | $\Delta d_j^{uav}(t)\le\Delta t\,\nu^{uav}$. |
| (22) | $d_{i\hat j}(t)\le Range_j$. |
| Migration feasibility | Decoded PSG runs services in parallel only when resources are unlocked/nonconflicting; enforced by Algorithm 3. |

**Relation to our scenario**

| Element | Yes / No / Partial | Grounded interpretation |
|---|---|---|
| Battery-triggered UAV replacement | No | Flight cost is modeled, but no low-battery trigger or source-to-replacement event. |
| Stateful running service | Yes | Stateful services/VMs and live migration are explicit; autonomous-driving context motivates persistent state. |
| Replacement selection | Partial | PSG decodes source/destination UAVs per service, but no replacement candidate set or low-battery selection variable. |
| Finite standby pool and long-term rotation | No | No standby inventory, recharge/return cycle, or long-horizon rotation. |
| Source continues during replacement flight | No | Migration is scheduled between hosting UAVs; no replacement-flight interval or overlap semantics. |
| Mobile A2A state synchronization | Partial | Inter-UAV migration bandwidth/parallel scheduling exist, but no distance-varying channel, generated runtime state, or convergence condition. |
| Source-UAV return-energy constraint | No | No battery or source-return reserve; only flight cost and speed/distance bounds. |

**Full-text evidence**

- Scenario/application: [Markdown lines 75-81](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/TOM_Joint_Trajectory_Offloading_and_Migration_Optimization_in_Stateful_Service-Oriented_UAV-Enabled_VEC_System/TOM_Joint_Trajectory_Offloading_and_Migration_Optimization_in_Stateful_Service-Oriented_UAV-Enabled_VEC_System.md:75)–[81](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/TOM_Joint_Trajectory_Offloading_and_Migration_Optimization_in_Stateful_Service-Oriented_UAV-Enabled_VEC_System/TOM_Joint_Trajectory_Offloading_and_Migration_Optimization_in_Stateful_Service-Oriented_UAV-Enabled_VEC_System.md:81).
- TDMA/A2G channel/rate: [lines 81-84](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/TOM_Joint_Trajectory_Offloading_and_Migration_Optimization_in_Stateful_Service-Oriented_UAV-Enabled_VEC_System/TOM_Joint_Trajectory_Offloading_and_Migration_Optimization_in_Stateful_Service-Oriented_UAV-Enabled_VEC_System.md:81)–[84](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/TOM_Joint_Trajectory_Offloading_and_Migration_Optimization_in_Stateful_Service-Oriented_UAV-Enabled_VEC_System/TOM_Joint_Trajectory_Offloading_and_Migration_Optimization_in_Stateful_Service-Oriented_UAV-Enabled_VEC_System.md:84).
- Stateful migration: [lines 175-194](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/TOM_Joint_Trajectory_Offloading_and_Migration_Optimization_in_Stateful_Service-Oriented_UAV-Enabled_VEC_System/TOM_Joint_Trajectory_Offloading_and_Migration_Optimization_in_Stateful_Service-Oriented_UAV-Enabled_VEC_System.md:175).
- P0/constraints: [lines 200-232](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/TOM_Joint_Trajectory_Offloading_and_Migration_Optimization_in_Stateful_Service-Oriented_UAV-Enabled_VEC_System/TOM_Joint_Trajectory_Offloading_and_Migration_Optimization_in_Stateful_Service-Oriented_UAV-Enabled_VEC_System.md:200).
- TOM encoding/parallel migration: [lines 236-280](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/TOM_Joint_Trajectory_Offloading_and_Migration_Optimization_in_Stateful_Service-Oriented_UAV-Enabled_VEC_System/TOM_Joint_Trajectory_Offloading_and_Migration_Optimization_in_Stateful_Service-Oriented_UAV-Enabled_VEC_System.md:236), [lines 326-362](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/TOM_Joint_Trajectory_Offloading_and_Migration_Optimization_in_Stateful_Service-Oriented_UAV-Enabled_VEC_System/TOM_Joint_Trajectory_Offloading_and_Migration_Optimization_in_Stateful_Service-Oriented_UAV-Enabled_VEC_System.md:326).
- Simulation/conclusions: [lines 403-419](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/TOM_Joint_Trajectory_Offloading_and_Migration_Optimization_in_Stateful_Service-Oriented_UAV-Enabled_VEC_System/TOM_Joint_Trajectory_Offloading_and_Migration_Optimization_in_Stateful_Service-Oriented_UAV-Enabled_VEC_System.md:403), [lines 487-491](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/TOM_Joint_Trajectory_Offloading_and_Migration_Optimization_in_Stateful_Service-Oriented_UAV-Enabled_VEC_System/TOM_Joint_Trajectory_Offloading_and_Migration_Optimization_in_Stateful_Service-Oriented_UAV-Enabled_VEC_System.md:487).

## [9] Energy-Aware Multi-UAV Collaboration for Data Collection and Trajectory Planning With MADDPG

**Bibliographic verification**
- Authors: Jing Mei, Jinglei Xu, Zhao Tong, and Keqin Li.
- Venue: *IEEE Transactions on Network and Service Management*, vol. 23, 2026, pp. 6721-6734.
- Year: 2026.
- DOI: [10.1109/TNSM.2026.3721502](https://doi.org/10.1109/TNSM.2026.3721502).
- Local artifacts: [PDF](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Energy-Aware_Multi-UAV_Collaboration_for_Data_Collection_and_Trajectory_Planning_With_MADDPG/Energy-Aware_Multi-UAV_Collaboration_for_Data_Collection_and_Trajectory_Planning_With_MADDPG.pdf); [Markdown](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Energy-Aware_Multi-UAV_Collaboration_for_Data_Collection_and_Trajectory_Planning_With_MADDPG/Energy-Aware_Multi-UAV_Collaboration_for_Data_Collection_and_Trajectory_Planning_With_MADDPG.md).

**Model/evidence status**
- Mathematical model: **complete optimization**. Slotted multi-UAV data collection, trajectory, propulsion/hover/communication energy, collision avoidance, and RTB form MINLP (32), mapped to a continuous-space MDP.
- Algorithm: **Multi-Agent Deep Deterministic Policy Gradient (MADDPG)** with centralized training/decentralized execution, actor-critics, replay/target networks, and reward terms for data, RTB residual energy, boundary violations, and collisions.
- Evaluation: **simulation**. PyTorch compares MADDPG with MATD3, MASAC, MAPPO, MAAC, and Cluster & Greedy; no testbed.
- Paper type: mathematical optimization plus multi-agent DRL trajectory/data-collection paper.

**Scenario**
- Topology: $K$ mobile UAVs at fixed altitude $H$ serve $M$ static UEs in an $L\times L$ disaster area; each fly-hover-communicates and returns to its initial base.
- Nodes: homogeneous UAVs, static UEs, and common base/safe-return location; no incoming replacement, standby inventory, charging state, or migration endpoint.
- Application: emergency collection of isolated-UE data after terrestrial failure; $D_m(t)$ are data volumes, not services or VM/container state.
- Assumptions: fixed altitude/speed, static UEs, equal slots, fly then hover/collect, one UAV per UE, RTB threshold, point/edge collision checks.
- Multiple access: **time division**; coverage bandwidth is proportional to remaining demand and no association variable is optimized.
- Channel model: LoS A2G, $g_{k,m}(t)=\beta_0\operatorname{dis}_{k,m}^{-2}(t)$, Shannon uplink; peer links provide information only, with no A2A state-transfer rate model.

**Problem & objective**
- Problem: Eq. (32), mixed-integer nonlinear data-collection/trajectory optimization with RTB/collision constraints; mTSP-like NP-hard and approximated by MDP.
- Objective: $\max_{T,\theta_k,T_k^{\mathrm{fly}}}\sum_{t=1}^{T}\sum_{k=1}^{K}\sum_{m=1}^{M}C_{k,m}(t)+\lambda\sum_{k=1}^{K}(E_k^{\mathrm{cons}}-\sum_{t=1}^{T}E_k(t))$, where $\lambda=1$ only after all demand is collected.
- Metrics: cumulative reward, completion/data rate, residual energy, collision/RTB compliance, and coverage.

**Decision variables**
| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Flight heading | $\theta_k(t)$ | Continuous $[0,2\pi]$ | Horizontal UAV direction. |
| Flight duration | $T_k^{\mathrm{fly}}(t)$ | Continuous $[0,\delta]$ | Slot portion spent flying. |
| Mission horizon | $T$ | Discrete/endogenous | Terminal slot when UAVs return to base. |

Access, bandwidth share, data, position, and energy states are induced by actions/dynamics.

**Constraints**
| ID | Meaning and key expression |
|---|---|
| (2)–(4) | Coverage/access only inside footprint and while $D_m(t)>0$. |
| (5), (8)–(9) | Proportional bandwidth; achievable-rate, non-flight-time, and demand limits; $D_m(t+1)=D_m(t)-C_{k,m}(t)$. |
| (19)/(32) | $\sum_tE_k(t)\le E_k^{\mathrm{cons}}$. |
| (20) | $E_k^{\mathrm{rest}}(t)\ge E_k^{\mathrm{rtb}}(t+1)+E_k(t+1)$, otherwise abort and return. |
| (21)–(22), (25)–(31) | Start/end separation and continuous edge-conflict collision checks. |
| (32) | $u_k(0)=u_k(T)$, $0\le x_k(t),y_k(t)\le L$. |

**Relation to our scenario**
| Element | Yes / No / Partial | Grounded interpretation |
|---|---|---|
| Battery-triggered UAV replacement | No | Low energy aborts/returns the same UAV; no incoming replacement. |
| Stateful running service | No | Static-UE data collection has no service, VM/container, checkpoint, session state, or consistency. |
| Replacement selection | No | MADDPG selects heading/duration only for existing UAVs. |
| Finite standby pool and long-term rotation | No | Fixed one-mission fleet; no standby inventory, charging/recovery, or rotation. |
| Source continues during replacement flight | No | No replacement flight or overlap. |
| Mobile A2A state synchronization | No | Peer information only; no state transfer/synchronization/rate model. |
| Source-UAV return-energy constraint | Partial | Eq. (20) reserves RTB energy and forces abort-return, but no source/replacement process. |

**Full-text evidence**
- Motivation/RTB: [Markdown lines 11-21](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Energy-Aware_Multi-UAV_Collaboration_for_Data_Collection_and_Trajectory_Planning_With_MADDPG/Energy-Aware_Multi-UAV_Collaboration_for_Data_Collection_and_Trajectory_Planning_With_MADDPG.md:11).
- Topology/motion: [lines 56-73](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Energy-Aware_Multi-UAV_Collaboration_for_Data_Collection_and_Trajectory_Planning_With_MADDPG/Energy-Aware_Multi-UAV_Collaboration_for_Data_Collection_and_Trajectory_Planning_With_MADDPG.md:56).
- Coverage/rate/energy: [lines 77-143](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Energy-Aware_Multi-UAV_Collaboration_for_Data_Collection_and_Trajectory_Planning_With_MADDPG/Energy-Aware_Multi-UAV_Collaboration_for_Data_Collection_and_Trajectory_Planning_With_MADDPG.md:77), [lines 152-213](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Energy-Aware_Multi-UAV_Collaboration_for_Data_Collection_and_Trajectory_Planning_With_MADDPG/Energy-Aware_Multi-UAV_Collaboration_for_Data_Collection_and_Trajectory_Planning_With_MADDPG.md:152).
- Objective/MDP/simulation: [lines 292-312](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Energy-Aware_Multi-UAV_Collaboration_for_Data_Collection_and_Trajectory_Planning_With_MADDPG/Energy-Aware_Multi-UAV_Collaboration_for_Data_Collection_and_Trajectory_Planning_With_MADDPG.md:292), [lines 318-394](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Energy-Aware_Multi-UAV_Collaboration_for_Data_Collection_and_Trajectory_Planning_With_MADDPG/Energy-Aware_Multi-UAV_Collaboration_for_Data_Collection_and_Trajectory_Planning_With_MADDPG.md:318), [lines 483-571](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Energy-Aware_Multi-UAV_Collaboration_for_Data_Collection_and_Trajectory_Planning_With_MADDPG/Energy-Aware_Multi-UAV_Collaboration_for_Data_Collection_and_Trajectory_Planning_With_MADDPG.md:483).

## [10] Trajectory and Resource Allocation for UAV Replacement to Provide Uninterrupted Service

**Bibliographic verification**
- Authors: Nishant Gupta; Satyam Agarwal; Deepak Mishra; Brijesh Kumbhani.
- Venue: *IEEE Transactions on Communications*, Volume 71, Number 12.
- Year: 2023.
- DOI: [10.1109/TCOMM.2023.3307559](https://doi.org/10.1109/TCOMM.2023.3307559).
- Local artifacts: [PDF](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Trajectory_and_Resource_Allocation_for_UAV_Replacement_to_Provide_Uninterrupted_Service/Trajectory_and_Resource_Allocation_for_UAV_Replacement_to_Provide_Uninterrupted_Service.pdf); [Markdown](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Trajectory_and_Resource_Allocation_for_UAV_Replacement_to_Provide_Uninterrupted_Service/Trajectory_and_Resource_Allocation_for_UAV_Replacement_to_Provide_Uninterrupted_Service.md).

**Model/evidence status**
- Mathematical model: **complete optimization**. Nonconvex NP-hard max-min throughput with joint 3-D two-UAV trajectory/bandwidth, probabilistic LoS/NLoS channel, rotary-wing propulsion energy, mobility, and continuity constraints.
- Algorithm: **Algorithm 2**, alternating bandwidth P2 with **Algorithm 1** trajectory SCA subproblems solved by interior-point methods.
- Evaluation: **simulation** with single-user, two-user, and 12-user/three-cluster cases and four trajectory/bandwidth benchmarks.
- Paper type: mathematical optimization, algorithm, and numerical-evaluation article.

**Scenario**
- Topology: $K$ stationary users; low-energy $U_1$ starts at $\mathbf X_F$ and returns to charging station $\mathbf X_I$; fully charged $U_2$ starts at $\mathbf X_I$ and flies to $\mathbf X_F$. Both serve during overlap; after $U_1$ reaches $\mathbf X_I$ at $N_f$, only $U_2$ serves. Section V-E sketches $M$-UAV replacement.
- Nodes: ground users, outgoing $U_1$, predetermined incoming $U_2$, charging station; no MEC/state-store/A2A node.
- Application: downlink UAV wireless coverage; service means communication rate/coverage, not hosted software.
- Assumptions: known stationary users; slotted motion; fully charged $U_2$; only $U_1$ has explicit energy budget; rotary-wing propulsion dominates and communication energy is ignored; fixed transmit power; both serve during overlap.
- Multiple access: **FDMA**, total bandwidth $B$ allocated as $b_{k,m}[n]$.
- Channel model: probabilistic LoS/NLoS A2G with logistic elevation-angle LoS probability, path loss/attenuation, averaged fading/expected rate. **No A2A channel.**

**Problem & objective**
- Problem: P1 transformed to P1.1, continuous nonconvex NP-hard trajectory/resource allocation.
- Objective: $\max_{\mathbf B,\mathbf T}\min_{k\in\mathcal K}R_k$, $R_k=\sum_{n=1}^{N_f}r_{k,1}[n]+\sum_{n=1}^{N}r_{k,2}[n]$; P1.1 maximizes $\mathcal R$ subject to $R_k\ge\mathcal R$.
- Metrics: minimum cumulative expected throughput and per-slot rate floor $R_{th}$, maintaining communication continuity rather than software-state migration.

**Decision variables**
| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Bandwidth allocation | $b_{k,m}[n]$, $\mathbf B$ | Continuous; total per slot $B$ | Bandwidth from UAV $m$ to user $k$. |
| 3-D trajectories | $\mathbf X_m[n]=[\mathbf q_m[n],z_m[n]]$, $\mathbf T$ | Continuous | UAV position in slot $n$. |
| Max-min epigraph | $\mathcal R$ | Continuous | Lower bound on each user's cumulative throughput. |
| Channel/geometry auxiliaries | $\alpha_{k,m}[n],\Phi_{k,m}[n],y_{k,m}[n],\beta_{k,m}[n]$ | Continuous | SCA auxiliaries. |
| Propulsion auxiliary | $g_1[n]$ | Continuous, $g_1[n]\ge0$ | Convexifies induced power. |

$N_f$ is a given return-slot index ($N_f\le N$), not optimized.

**Constraints**
| ID | Meaning and key expression |
|---|---|
| (10a) | Endpoint exchange: $\mathbf X_1[0]=\mathbf X_F,\mathbf X_1[N_f]=\mathbf X_I,\mathbf X_2[0]=\mathbf X_I,\mathbf X_2[N]=\mathbf X_F$. |
| (10b) | $v_m[n]\le V_{max}$. |
| (10c) | $\|\mathbf X_m[n]-\mathbf X_j[n]\|^2\ge D_{min}^2$. |
| (10d) | $\sum_{n=1}^{N_f}e_1[n]\le E_{left}$. |
| (10e) | $r_{k,1}[n]+r_{k,2}[n]\ge R_{th}$. |
| (10f)/(6) | $\sum_k\sum_{m=1}^{2}b_{k,m}[n]=B$. |
| (11a) | $R_k\ge\mathcal R$. |

**Relation to our scenario**
| Element | Yes / No / Partial | Grounded interpretation |
|---|---|---|
| Battery-triggered UAV replacement | Yes | Low-energy $U_1$ is replaced by fully charged $U_2$; inbound flight and outbound return are explicit. |
| Stateful running service | No | Service is downlink coverage/rate; no application, checkpoint, or state-transition model. |
| Replacement selection | No | $U_2$ is predetermined; no candidate-pool selection. |
| Finite standby pool and long-term rotation | Partial | Repeated/$M$-UAV replacement is discussed, but no inventory, recharge, or multi-cycle state is modeled. |
| Source continues during replacement flight | Yes | $U_1$ rates count until return; both UAVs serve during overlap. |
| Mobile A2A state synchronization | No | No application state or A2A link. |
| Source-UAV return-energy constraint | Yes | Eq. (10d) constrains $U_1$'s propulsion energy to return within $E_{left}$. |

**Full-text evidence**
- Replacement topology/overlap: [line 56](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Trajectory_and_Resource_Allocation_for_UAV_Replacement_to_Provide_Uninterrupted_Service/Trajectory_and_Resource_Allocation_for_UAV_Replacement_to_Provide_Uninterrupted_Service.md:56), [line 62](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Trajectory_and_Resource_Allocation_for_UAV_Replacement_to_Provide_Uninterrupted_Service/Trajectory_and_Resource_Allocation_for_UAV_Replacement_to_Provide_Uninterrupted_Service.md:62).
- Propulsion/budget: [line 84](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Trajectory_and_Resource_Allocation_for_UAV_Replacement_to_Provide_Uninterrupted_Service/Trajectory_and_Resource_Allocation_for_UAV_Replacement_to_Provide_Uninterrupted_Service.md:84), [line 87](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Trajectory_and_Resource_Allocation_for_UAV_Replacement_to_Provide_Uninterrupted_Service/Trajectory_and_Resource_Allocation_for_UAV_Replacement_to_Provide_Uninterrupted_Service.md:87).
- Channel/FDMA/objective/constraints: [line 94](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Trajectory_and_Resource_Allocation_for_UAV_Replacement_to_Provide_Uninterrupted_Service/Trajectory_and_Resource_Allocation_for_UAV_Replacement_to_Provide_Uninterrupted_Service.md:94), [line 110](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Trajectory_and_Resource_Allocation_for_UAV_Replacement_to_Provide_Uninterrupted_Service/Trajectory_and_Resource_Allocation_for_UAV_Replacement_to_Provide_Uninterrupted_Service.md:110), [line 139](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Trajectory_and_Resource_Allocation_for_UAV_Replacement_to_Provide_Uninterrupted_Service/Trajectory_and_Resource_Allocation_for_UAV_Replacement_to_Provide_Uninterrupted_Service.md:139), [line 161](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Trajectory_and_Resource_Allocation_for_UAV_Replacement_to_Provide_Uninterrupted_Service/Trajectory_and_Resource_Allocation_for_UAV_Replacement_to_Provide_Uninterrupted_Service.md:161).
- Algorithms/results: [line 186](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Trajectory_and_Resource_Allocation_for_UAV_Replacement_to_Provide_Uninterrupted_Service/Trajectory_and_Resource_Allocation_for_UAV_Replacement_to_Provide_Uninterrupted_Service.md:186), [line 343](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Trajectory_and_Resource_Allocation_for_UAV_Replacement_to_Provide_Uninterrupted_Service/Trajectory_and_Resource_Allocation_for_UAV_Replacement_to_Provide_Uninterrupted_Service.md:343), [line 450](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Trajectory_and_Resource_Allocation_for_UAV_Replacement_to_Provide_Uninterrupted_Service/Trajectory_and_Resource_Allocation_for_UAV_Replacement_to_Provide_Uninterrupted_Service.md:450), [line 478](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Trajectory_and_Resource_Allocation_for_UAV_Replacement_to_Provide_Uninterrupted_Service/Trajectory_and_Resource_Allocation_for_UAV_Replacement_to_Provide_Uninterrupted_Service.md:478).

- Scenario/IC roles: [line 47](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Live_Migration_of_Stateful_Microservices_in_UAV-Assisted_Networks_for_Enhanced_Availability/Live_Migration_of_Stateful_Microservices_in_UAV-Assisted_Networks_for_Enhanced_Availability.md:47), [line 53](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Live_Migration_of_Stateful_Microservices_in_UAV-Assisted_Networks_for_Enhanced_Availability/Live_Migration_of_Stateful_Microservices_in_UAV-Assisted_Networks_for_Enhanced_Availability.md:53), [line 55](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Live_Migration_of_Stateful_Microservices_in_UAV-Assisted_Networks_for_Enhanced_Availability/Live_Migration_of_Stateful_Microservices_in_UAV-Assisted_Networks_for_Enhanced_Availability.md:55), [line 57](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Live_Migration_of_Stateful_Microservices_in_UAV-Assisted_Networks_for_Enhanced_Availability/Live_Migration_of_Stateful_Microservices_in_UAV-Assisted_Networks_for_Enhanced_Availability.md:57).
- Objective: [line 43](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Live_Migration_of_Stateful_Microservices_in_UAV-Assisted_Networks_for_Enhanced_Availability/Live_Migration_of_Stateful_Microservices_in_UAV-Assisted_Networks_for_Enhanced_Availability.md:43).
- Trigger/phase: [line 59](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Live_Migration_of_Stateful_Microservices_in_UAV-Assisted_Networks_for_Enhanced_Availability/Live_Migration_of_Stateful_Microservices_in_UAV-Assisted_Networks_for_Enhanced_Availability.md:59), [line 72](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Live_Migration_of_Stateful_Microservices_in_UAV-Assisted_Networks_for_Enhanced_Availability/Live_Migration_of_Stateful_Microservices_in_UAV-Assisted_Networks_for_Enhanced_Availability.md:72).
- Designation/image preparation/transfer/restore: [line 74](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Live_Migration_of_Stateful_Microservices_in_UAV-Assisted_Networks_for_Enhanced_Availability/Live_Migration_of_Stateful_Microservices_in_UAV-Assisted_Networks_for_Enhanced_Availability.md:74), [line 76](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Live_Migration_of_Stateful_Microservices_in_UAV-Assisted_Networks_for_Enhanced_Availability/Live_Migration_of_Stateful_Microservices_in_UAV-Assisted_Networks_for_Enhanced_Availability.md:76), [line 78](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Live_Migration_of_Stateful_Microservices_in_UAV-Assisted_Networks_for_Enhanced_Availability/Live_Migration_of_Stateful_Microservices_in_UAV-Assisted_Networks_for_Enhanced_Availability.md:78), [line 80](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Live_Migration_of_Stateful_Microservices_in_UAV-Assisted_Networks_for_Enhanced_Availability/Live_Migration_of_Stateful_Microservices_in_UAV-Assisted_Networks_for_Enhanced_Availability.md:80).
- Use cases/future measurements: [line 86](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Live_Migration_of_Stateful_Microservices_in_UAV-Assisted_Networks_for_Enhanced_Availability/Live_Migration_of_Stateful_Microservices_in_UAV-Assisted_Networks_for_Enhanced_Availability.md:86), [line 88](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Live_Migration_of_Stateful_Microservices_in_UAV-Assisted_Networks_for_Enhanced_Availability/Live_Migration_of_Stateful_Microservices_in_UAV-Assisted_Networks_for_Enhanced_Availability.md:88), [line 121](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Live_Migration_of_Stateful_Microservices_in_UAV-Assisted_Networks_for_Enhanced_Availability/Live_Migration_of_Stateful_Microservices_in_UAV-Assisted_Networks_for_Enhanced_Availability.md:121).

## [11] Prediction-Assisted Multi-UAV Online Service Migration and Trajectory Control for MEC-Empowered Vehicular Networks

**Bibliographic verification**

- Authors: Wei Feng, Wenyang Gao, Jianping Yao, Longyu Zhou, Chenggang Yan, and Tony Q. S. Quek.
- Venue: accepted for publication in *IEEE Transactions on Mobile Computing* (author accepted version; final volume, issue, and pages are not printed in the local PDF).
- Year: 2026 (the accepted-manuscript citation information and DOI are dated 2026).
- DOI: [10.1109/TMC.2026.3700894](https://doi.org/10.1109/TMC.2026.3700894).
- Local artifacts: [PDF](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Prediction-Assisted_Multi-UAV_Online_Service_Migration_and_Trajectory_Control_for_MEC-Empowered_Vehicular_Networks/Prediction-Assisted_Multi-UAV_Online_Service_Migration_and_Trajectory_Control_for_MEC-Empowered_Vehicular_Networks.pdf); [Markdown](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Prediction-Assisted_Multi-UAV_Online_Service_Migration_and_Trajectory_Control_for_MEC-Empowered_Vehicular_Networks/Prediction-Assisted_Multi-UAV_Online_Service_Migration_and_Trajectory_Control_for_MEC-Empowered_Vehicular_Networks.md).
- The title and six-author list were checked on PDF page 1. The accepted venue, 2026 status, and DOI were checked in the publisher footer/citation information; no unprinted final volume, issue, or page range is inferred.

**Model/evidence status**

- Mathematical model: **complete optimization**. Long-term stochastic problem P1 jointly chooses service destinations and continuous UAV movement to minimize average user delay under a time-average migration-cost budget, collision separation, and per-slot movement limits; Lyapunov optimization produces per-slot P2.
- Algorithm: unified **stacked-LSTM + Lyapunov optimization + MADDPG**. A three-layer LSTM predicts vehicle positions; virtual migration queues encode the average-cost constraint; MADDPG with centralized training/decentralized execution, Gumbel-Softmax action reconstruction, and feasibility projection learns mixed discrete-continuous migration/trajectory controls.
- Evaluation: **simulation**. Python 3.9 experiments compare the method with DQN, Greedy Migration, MAPPO, and a no-LSTM ablation over task sizes and 5–30 users. No testbed is reported.
- Paper type: prediction-assisted stochastic optimization and multi-agent DRL paper with simulation evaluation.

**Scenario**

- Topology: $V$ mobile UAVs with onboard MEC servers serve $U$ mobile ground users/vehicles over urban hotspots. Each user has a directly connected local UAV and possibly a different serving UAV; stable multi-hop backhaul links relay tasks and service data among UAVs.
- Nodes: mobile vehicular users, local UAVs, serving UAVs, and an abstract central controller used during centralized training. There are no fixed MEC base stations in the optimized architecture and no standby/replacement UAV class.
- Application: latency-sensitive vehicular computation such as cooperative perception, high-definition video analytics, and high-precision mapping. A user generates one computation task per slot. Migration changes the serving UAV and transfers the task plus its MEC instance/service configuration files.
- Assumptions: users and UAVs move only at slot boundaries and remain stationary within a slot; UAV altitude is constant; user tasks arrive stochastically; inter-UAV backhaul is stable and multi-hop; computing is proportionally shared; future vehicle motion is unknown but short-term positions are predicted from 20 historical slots.
- Multiple access: **OFDMA**, described as interference-free spectrum sharing among users; $B_1$ is the allocated access bandwidth. No inter-user interference term or optimized bandwidth-allocation variable appears.
- Channel model: user-UAV free-space, distance-squared LoS path gain following the cited 3GPP aerial-link principle; rate uses SNR and Shannon capacity. Inter-UAV migration/backhaul delay is abstracted by fixed bandwidths $B_0,B_2$, data size, and hop-count coefficients rather than an A2A propagation/SINR model.

**Problem & objective**

- Problems: long-term stochastic **P1** (14) and Lyapunov per-slot **P2** (21).
- Type: mixed-integer, highly nonconvex, partially observable, long-term stochastic optimization with a time-average constraint.
- P1 objective (14):

  $$
  \min_{\pi_u[n],(x_v[n],y_v[n])}
  \lim_{N\to\infty}\frac{1}{N}\sum_{n=1}^{N}\sum_{u=1}^{U}\ell_u[n],
  $$

  where $\ell_u=\ell_u^{\mathrm{mig}}+\ell_u^{\mathrm{com}}+\ell_u^{\mathrm{cmp}}$, under $\lim_{N\to\infty}N^{-1}\sum_nE[n]\le E_{\mathrm{avg}}$.
- Per-slot P2 (21): $\min_{\pi_u[n],(x_v[n],y_v[n])}\sum_v\sum_{u\in\mathcal U_v[n]}(A_v[n]E_{u,v}[n]+\zeta\ell_u[n])$.
- Metrics: average/system latency, reward and convergence, migration cost/frequency, vehicle-trajectory prediction error, robustness to task size, and scalability with user count.

**Decision variables**

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Serving-UAV/service-migration decision | $\pi_u[n]$ | Discrete, $\pi_u[n]\in\mathcal V$ | UAV to which user $u$'s service is assigned in slot $n$; $v_u^{\mathrm{ser}}[n]=\pi_u[n]$. |
| UAV horizontal position | $(x_v[n],y_v[n])$ | Continuous | Position/trajectory of UAV $v$ at a slot boundary. |
| UAV displacement action | $(\Delta x_v[n],\Delta y_v[n])$ | Continuous | MADDPG action representation that updates UAV position between slots. |

The migration indicator $a_u[n]$, hop counts, latency components, virtual queues $A_v[n]$, predicted user coordinates, and local UAV $v_u^{\mathrm{loc}}[n]$ are derived states/parameters rather than independent optimization variables.

**Constraints**

| ID | Meaning and key expression |
|---|---|
| (13)/(14c) | Long-term migration cost: $\lim_{N\to\infty}N^{-1}\sum_nE[n]\le E_{\mathrm{avg}}$. |
| (14b) | Serving UAV, local UAV, and $\pi_u[n]$ must belong to $\mathcal V$. |
| (14d) | Collision avoidance: $l_{v,v'}[n]\ge l_1$ for every UAV pair. |
| (14e) | Mobility: $0\le l_v[n]\le l_2$, limiting per-slot displacement. |
| (15) | Virtual migration queue: $A_v[n+1]=\max(A_v[n]-E_{\mathrm{avg}},0)+\sum_{u\in\mathcal U_v[n]}E_{u,v}[n]$. |
| (21) | P2 retains UAV-set, collision, and movement feasibility after the average-cost constraint is encoded in the virtual queue. |

**Relation to our scenario**

| Element | Yes / No / Partial | Grounded interpretation |
|---|---|---|
| Battery-triggered UAV replacement | No | Migration is driven by vehicle mobility/channel quality and delay-cost trade-offs. UAV energy is not modeled; energy-aware constraints are listed as future work. |
| Stateful running service | Partial | The paper transfers a task plus an MEC instance/service configuration file and calls this service migration, but does not define mutable runtime/user state, checkpoint/restore, dirty updates, consistency, or downtime beyond a size-and-hop delay. |
| Replacement selection | Partial | $\pi_u[n]$ selects a destination/serving UAV for the user's service, but not an incoming UAV replacing a battery-depleted serving UAV. |
| Finite standby pool and long-term rotation | No | All UAVs are simultaneously available MEC agents; no standby set, charging/recovery state, finite replacement inventory, or duty rotation exists. |
| Source continues during replacement flight | No | There is no battery replacement flight, and the paper does not specify old-instance service overlap during transfer. |
| Mobile A2A state synchronization | Partial | Both endpoints are mobile UAVs and service data crosses a multi-hop A2A backhaul, but only a one-time transfer delay is modeled, not evolving-state synchronization or consistency. |
| Source-UAV return-energy constraint | No | Propulsion, battery reserve, and RTB are absent and explicitly left to future energy-aware extensions. |

**Full-text evidence**

- Motivation, problem boundary, and long-term delay/migration-cost contribution: [Markdown lines 11–31](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Prediction-Assisted_Multi-UAV_Online_Service_Migration_and_Trajectory_Control_for_MEC-Empowered_Vehicular_Networks/Prediction-Assisted_Multi-UAV_Online_Service_Migration_and_Trajectory_Control_for_MEC-Empowered_Vehicular_Networks.md:11).
- Multi-UAV/mobile-user topology, local-versus-serving UAV, and service/MEC-instance transfer semantics: [lines 50–62](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Prediction-Assisted_Multi-UAV_Online_Service_Migration_and_Trajectory_Control_for_MEC-Empowered_Vehicular_Networks/Prediction-Assisted_Multi-UAV_Online_Service_Migration_and_Trajectory_Control_for_MEC-Empowered_Vehicular_Networks.md:50).
- Migration-delay equation and service-instance data abstraction: [lines 70–76](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Prediction-Assisted_Multi-UAV_Online_Service_Migration_and_Trajectory_Control_for_MEC-Empowered_Vehicular_Networks/Prediction-Assisted_Multi-UAV_Online_Service_Migration_and_Trajectory_Control_for_MEC-Empowered_Vehicular_Networks.md:70).
- OFDMA/free-space access channel, task/backhaul communication delay, and compute delay: [lines 78–127](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Prediction-Assisted_Multi-UAV_Online_Service_Migration_and_Trajectory_Control_for_MEC-Empowered_Vehicular_Networks/Prediction-Assisted_Multi-UAV_Online_Service_Migration_and_Trajectory_Control_for_MEC-Empowered_Vehicular_Networks.md:78).
- Migration-cost model and time-average budget: [lines 130–149](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Prediction-Assisted_Multi-UAV_Online_Service_Migration_and_Trajectory_Control_for_MEC-Empowered_Vehicular_Networks/Prediction-Assisted_Multi-UAV_Online_Service_Migration_and_Trajectory_Control_for_MEC-Empowered_Vehicular_Networks.md:130).
- P1 objective, constraints, and mixed-integer/nonconvex classification: [lines 152–186](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Prediction-Assisted_Multi-UAV_Online_Service_Migration_and_Trajectory_Control_for_MEC-Empowered_Vehicular_Networks/Prediction-Assisted_Multi-UAV_Online_Service_Migration_and_Trajectory_Control_for_MEC-Empowered_Vehicular_Networks.md:152).
- Virtual queue, drift-plus-penalty transformation, and P2: [lines 196–243](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Prediction-Assisted_Multi-UAV_Online_Service_Migration_and_Trajectory_Control_for_MEC-Empowered_Vehicular_Networks/Prediction-Assisted_Multi-UAV_Online_Service_Migration_and_Trajectory_Control_for_MEC-Empowered_Vehicular_Networks.md:196).
- LSTM inputs/predictions and MDP observation/action/reward: [lines 246–298](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Prediction-Assisted_Multi-UAV_Online_Service_Migration_and_Trajectory_Control_for_MEC-Empowered_Vehicular_Networks/Prediction-Assisted_Multi-UAV_Online_Service_Migration_and_Trajectory_Control_for_MEC-Empowered_Vehicular_Networks.md:246).
- Simulation setup and absence of an energy model: [lines 401–453](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Prediction-Assisted_Multi-UAV_Online_Service_Migration_and_Trajectory_Control_for_MEC-Empowered_Vehicular_Networks/Prediction-Assisted_Multi-UAV_Online_Service_Migration_and_Trajectory_Control_for_MEC-Empowered_Vehicular_Networks.md:401); [conclusion/future work lines 496–498](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Prediction-Assisted_Multi-UAV_Online_Service_Migration_and_Trajectory_Control_for_MEC-Empowered_Vehicular_Networks/Prediction-Assisted_Multi-UAV_Online_Service_Migration_and_Trajectory_Control_for_MEC-Empowered_Vehicular_Networks.md:496).

## [12] Live Migration of Video Analytics Applications in Edge Computing

**Bibliographic verification**

- Authors: Chenghao Rong, Jessie Hui Wang, Jilong Wang, Yipeng Zhou, and Jun Zhang.
- Venue: *IEEE Transactions on Mobile Computing*, vol. 23, no. 3, pp. 2078–2092.
- Year: 2024 (March 2024 issue; the PDF also notes 2023 online publication/copyright).
- DOI: [10.1109/TMC.2023.3246539](https://doi.org/10.1109/TMC.2023.3246539).
- Local artifacts: [PDF](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Live_Migration_of_Video_Analytics_Applications_in_Edge_Computing/Live_Migration_of_Video_Analytics_Applications_in_Edge_Computing.pdf); [Markdown](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Live_Migration_of_Video_Analytics_Applications_in_Edge_Computing/Live_Migration_of_Video_Analytics_Applications_in_Edge_Computing.md).
- Title, authors, venue, volume/issue/pages, year, and DOI were checked against the first page of the local PDF.

**Model/evidence status**

- Mathematical model: **no mathematical model**. The paper has no numbered problem, objective function, decision vector, or constraint set.
- Algorithm: **warm-up–sync–replay live-migration procedure**. Algorithms 1–2 are integration pseudocode that inserts `stateGET/statePUT` into object-detection/background-subtraction applications; they are not optimization algorithms.
- Evaluation: **testbed**. The implementation runs on a Kubernetes control server and two heterogeneous edge servers.
- Paper type: measurement-driven systems architecture, implementation, and experimental-evaluation paper.

**Scenario**

- Topology: a mobile camera/device offloads a real-time video stream to a nearby edge server. During migration, a Kubernetes control server and migration controller coordinate source and destination edge servers. Each edge server has a local state store; the control server has a global state store; each application pod comprises an application container and sidecar.
- Nodes: mobile camera/client, source/destination edge server, control server/migration controller, local/global state store, sidecar, and video-analytics application container.
- Application: three VA workloads: Vehicle Counter (Faster R-CNN + ResNet101 + Deep Sort, PyTorch), Object Tracking (TensorFlow), and Person Detection (background subtraction + EfficientDet + SURF, TensorFlow).
- Assumptions: every video frame must be analyzed; the application explicitly reports/reads crucial states through a small number of `stateGET/statePUT` calls; permanent state can be warmed up, ephemeral state rebuilt by frame replay, and crucial state synchronized; the deep-learning model is unchanged over the application lifetime or a model-switching window; the scheduler supplies the migration command and destination.
- Multiple access: **not specified**. No wireless access technology or multi-access resource allocation is modeled; video input uses RTMP.
- Channel model: **not specified analytically**. Measurement sets edge-server bandwidth to 50 Mbps and evaluation uses 25–50 Mbps edge-controller bandwidth; edge-cloud latency is explicitly not simulated.

**Problem & objective**

- **No optimization problem or objective function.** The paper distinguishes prior work that decides when/where to migrate from this paper's implementation of how to migrate; scheduling algorithms are external inputs.
- Design objectives are to minimize VA application downtime, preserve analysis latency/accuracy, and analyze every frame. Metrics are total migration time, downtime/frame-analysis latency, GPU/CPU load, sidecar overhead, and state read/write latency.

**Decision variables**

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| None | — | — | There are no optimization decision variables. Frame rate, bandwidth, Deep Sort history $\beta$, and SURF feature cap $\alpha$ are experiment settings; source/destination placement is supplied by an external scheduler. |

**Constraints**

| ID | Meaning and key expression |
|---|---|
| No mathematical constraints | Operational requirements only: every video frame must be analyzed; the destination first warms permanent state, synchronizes crucial state, and identifies/replays the beginning frame. These are not written as a mathematical feasible set. |

**Relation to our scenario**

| Element | Yes / No / Partial | Grounded interpretation |
|---|---|---|
| Battery-triggered UAV replacement | No | Migration is motivated by mobility or resource-efficiency needs, not UAV battery state. |
| Stateful running service | Yes | Permanent, crucial, and ephemeral state jointly represent a running VA application's state; crucial state is explicitly synchronized. |
| Replacement selection | No | The external scheduler supplies when/where and the destination; this paper does not solve node selection. |
| Finite standby pool and long-term rotation | No | No standby UAV pool, charging, recovery, or cross-cycle rotation is modeled. |
| Source continues during replacement flight | Partial | The source application continues while the destination pod is created, warmed, and synchronized, then stops before replay; both endpoints are fixed edge servers, not flying replacements. |
| Mobile A2A state synchronization | No | State is synchronized between fixed edge servers and local/global stores, not through mobile A2A links. |
| Source-UAV return-energy constraint | No | No UAV or energy model exists. |

**Full-text evidence**

- Mobile VA setting, live migration, and per-frame continuity requirement: [lines 31–33](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Live_Migration_of_Video_Analytics_Applications_in_Edge_Computing/Live_Migration_of_Video_Analytics_Applications_in_Edge_Computing.md:31).
- Permanent, crucial, and ephemeral state classes and warm-up/sync/replay handling: [lines 111–125](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Live_Migration_of_Video_Analytics_Applications_in_Edge_Computing/Live_Migration_of_Video_Analytics_Applications_in_Edge_Computing.md:111).
- Migration controller, distributed state store, and sidecar components: [lines 152–158](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Live_Migration_of_Video_Analytics_Applications_in_Edge_Computing/Live_Migration_of_Video_Analytics_Applications_in_Edge_Computing.md:152).
- Source continuation and cutover order: [lines 233–239](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Live_Migration_of_Video_Analytics_Applications_in_Edge_Computing/Live_Migration_of_Video_Analytics_Applications_in_Edge_Computing.md:233).
- Kubernetes control/two-edge-server testbed, 25–50 Mbps links, and latency boundary: [lines 253–257](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Live_Migration_of_Video_Analytics_Applications_in_Edge_Computing/Live_Migration_of_Video_Analytics_Applications_in_Edge_Computing.md:253).
- Downtime and migration-time results: [lines 261–293](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Live_Migration_of_Video_Analytics_Applications_in_Edge_Computing/Live_Migration_of_Video_Analytics_Applications_in_Edge_Computing.md:261).
- Explicit separation of when/where scheduling from this implementation: [line 360](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Live_Migration_of_Video_Analytics_Applications_in_Edge_Computing/Live_Migration_of_Video_Analytics_Applications_in_Edge_Computing.md:360).
- Deep-learning model invariance assumption: [line 346](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Live_Migration_of_Video_Analytics_Applications_in_Edge_Computing/Live_Migration_of_Video_Analytics_Applications_in_Edge_Computing.md:346).

## [13] Optimal Flight Speed Scheduling and Battery Swapping in UAV-Enabled Mobile Edge Computing

**Bibliographic verification**

- Authors: Dongmei Ye, Zhengqing Sun, Weifeng Zhong, Jiawen Kang, Xumin Huang, Dong In Kim, Shengli Xie, and Chau Yuen.
- Venue: *IEEE Transactions on Mobile Computing*, vol. 25, no. 1, January 2026 (metadata also gives publication date 22 August 2025).
- Year: 2026.
- DOI: [10.1109/TMC.2025.3601743](https://doi.org/10.1109/TMC.2025.3601743).
- Local artifacts: [PDF](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Optimal_Flight_Speed_Scheduling_and_Battery_Swapping_in_UAV-Enabled_Mobile_Edge_Computing/Optimal_Flight_Speed_Scheduling_and_Battery_Swapping_in_UAV-Enabled_Mobile_Edge_Computing.pdf); [Markdown](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Optimal_Flight_Speed_Scheduling_and_Battery_Swapping_in_UAV-Enabled_Mobile_Edge_Computing/Optimal_Flight_Speed_Scheduling_and_Battery_Swapping_in_UAV-Enabled_Mobile_Edge_Computing.md).
- The title, eight-author list, venue/volume/year, and DOI were checked against the first page of the local PDF.

**Model/evidence status**

- Mathematical model: **complete optimization**. Original model P1 is a nonconvex MINLP; an extended graph and convex envelopes yield mixed-integer convex P3.
- Algorithm: **ATC-based heuristic (Algorithm 1)** using analytical target cascading. The heuristic decomposes task-node subproblems and coordinates bandwidth, MEC CPU, and time through a master; small P3 instances can also be solved by GUROBI.
- Evaluation: **simulation**. MATLAB/YALMIP/GUROBI experiments compare P3 with constant-speed and fixed-battery-swapping models and evaluate ATC scalability/convergence.
- Paper type: mathematical optimization and heuristic-algorithm paper with numerical simulation.

**Scenario**

- Topology: one quadrotor UAV starts at a base station $BS$, visits geographically distributed task nodes in a prescribed order, may return to the BS for battery swapping, and finally returns to the BS. The BS co-locates an MEC server and battery-swapping station.
- Nodes: one UAV, one BS/MEC/battery station, and $|K|$ task nodes. No second/standby UAV or service-host migration node is modeled.
- Application: UAV patrol inspection of power lines, solar farms, forests, or agriculture, collecting photos/video or anomaly-detection data; each task is processed locally or offloaded to the BS MEC server.
- Assumptions: one-BS coverage; task order is known; the UAV hovers at each task node until collection/processing completes; battery swapping takes fixed time $\tau$; the UAV departs fully charged and resets to a full battery at the swapping station; result data is negligible compared with collected input data.
- Multiple access: **FDMA** between UAV and BS; the UAV purchases bandwidth $b$.
- Channel model: quasi-static LoS free-space path loss; $r_k=b\log_2(1+g_0d_k^{-\alpha}P/N_0)$. No A2A link is present.

**Problem & objective**

- Problem P1 jointly selects path, discrete flight speed, battery swaps, binary local/MEC offloading, and purchased communication/CPU resources.
- Type: nonconvex mixed-integer nonlinear program; P2/P3 are equivalent or reformulated mixed-integer convex problems.
- Objective: $\mathbf P1:\min\;\pi_a b+\pi_b f^{M}+\pi_c(x^{BS}+1)$, subject to (1)–(25), pricing BS bandwidth, MEC computing resource, and battery swaps.
- Metrics: total operational cost and operation time; ATC solver time and total coordination error $\delta_{sum}$ are also reported.

**Decision variables**

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Selected flight leg | $X_{(i,j)}$ | Binary, $\{0,1\}$ | 1 if directed leg $(i,j)$ is selected. |
| Flight speed | $V_{(i,j)}$ | Discrete, $\{V_1,\ldots,V_N\}$ | Speed selected on each actual leg. |
| Task offloading mode | $a_k$ | Binary, $\{0,1\}$ | 0 for local UAV processing; 1 for MEC offloading. |
| Purchased bandwidth | $b$ | Continuous, $B_{min}\le b\le B_{max}$ | BS communication bandwidth purchased by the UAV. |
| Purchased MEC CPU | $f^M$ | Continuous, $F_{min}\le f^M\le F_{max}$ | MEC computing resource purchased by the UAV. |
| Battery-swap count | $x^{BS}$ | Integer induced by selected returns | Number of batteries swapped before the final return. |
| Battery/energy state | $Y_j^{in},Y_j^{out}$ (P1); $Y_j$ (P3) | Continuous, nonnegative at departure | Remaining UAV energy entering/leaving nodes. |
| Convexification auxiliaries | $r^b,r^f,Z^Y_{(i,j)},Z^E_{(i,j)},Z^T_{(i,j)}$ | Continuous | Reciprocal-resource and binary-continuous-product auxiliaries in P2/P3. |

**Constraints**

| ID | Meaning and key expression |
|---|---|
| (1)–(3) | Binary leg selection, visit-each-task-once, and flow continuity. |
| (4) | Battery swaps: $x^{BS}=\sum_{i\in in(BS)}X_{(i,j)}-1$, excluding the final mission return. |
| (5) | Total mission time: flight time + hover time + $x^{BS}\tau\le T^{max}$. |
| (7)–(10) | Binary local/offloaded mode and hover-time definitions for local/MEC execution. |
| (11)–(14) | Discrete speed levels, leg time $T_{(i,j)}=L_{(i,j)}/V_{(i,j)}$, propulsion energy $E_{(i,j)}=T_{(i,j)}P_{(i,j)}$, and rotary-wing power model. |
| (20)–(23) | Battery reset to full at BS, energy-state recursion, and $Y_j^{out}\ge0$ for route energy feasibility. |
| (24)–(25) | Purchased bandwidth and MEC CPU bounds. |
| P1 objective constraints | P1 uses (1)–(25); P3 additionally uses convex envelopes (36) and cone constraints (37). |

**Relation to our scenario**

| Element | Yes / No / Partial | Grounded interpretation |
|---|---|---|
| Battery-triggered UAV replacement | No | Energy shortage makes the same UAV return to the BS and swap a battery; no incoming UAV replaces it in service. |
| Stateful running service | No | Applications are inspection tasks; no persistent runtime state, checkpoint, migration, or service-resume model exists. |
| Replacement selection | No | There is no replacement-UAV candidate or selection variable. |
| Finite standby pool and long-term rotation | No | One UAV makes repeated returns within one tour, but there is no standby inventory, recharge queue, or long-term duty rotation state. |
| Source continues during replacement flight | No | No source/replacement pair or overlapping replacement flight is modeled. |
| Mobile A2A state synchronization | No | Only UAV–BS FDMA communication appears; no A2A synchronization link or state transfer exists. |
| Source-UAV return-energy constraint | Partial | Battery recursion and $Y_j^{out}\ge0$ enforce energy-feasible continuation/returns, but not a designated source UAV reserve during replacement. |

**Full-text evidence**

- Patrol scenario, BS/MEC/swap-station roles, and node set: [lines 33–48](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Optimal_Flight_Speed_Scheduling_and_Battery_Swapping_in_UAV-Enabled_Mobile_Edge_Computing/Optimal_Flight_Speed_Scheduling_and_Battery_Swapping_in_UAV-Enabled_Mobile_Edge_Computing.md:33).
- Path, visit, and swap variables/constraints: [lines 50–80](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Optimal_Flight_Speed_Scheduling_and_Battery_Swapping_in_UAV-Enabled_Mobile_Edge_Computing/Optimal_Flight_Speed_Scheduling_and_Battery_Swapping_in_UAV-Enabled_Mobile_Edge_Computing.md:50).
- FDMA/free-space channel and task offloading: [lines 82–118](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Optimal_Flight_Speed_Scheduling_and_Battery_Swapping_in_UAV-Enabled_Mobile_Edge_Computing/Optimal_Flight_Speed_Scheduling_and_Battery_Swapping_in_UAV-Enabled_Mobile_Edge_Computing.md:82).
- Battery reset, energy recursion, and return feasibility: [lines 198–225](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Optimal_Flight_Speed_Scheduling_and_Battery_Swapping_in_UAV-Enabled_Mobile_Edge_Computing/Optimal_Flight_Speed_Scheduling_and_Battery_Swapping_in_UAV-Enabled_Mobile_Edge_Computing.md:198).
- Objective, model variables, and constraints (1)–(25): [lines 228–246](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Optimal_Flight_Speed_Scheduling_and_Battery_Swapping_in_UAV-Enabled_Mobile_Edge_Computing/Optimal_Flight_Speed_Scheduling_and_Battery_Swapping_in_UAV-Enabled_Mobile_Edge_Computing.md:228).
- P2/P3 reformulation and mixed-integer convex model: [lines 381–431](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Optimal_Flight_Speed_Scheduling_and_Battery_Swapping_in_UAV-Enabled_Mobile_Edge_Computing/Optimal_Flight_Speed_Scheduling_and_Battery_Swapping_in_UAV-Enabled_Mobile_Edge_Computing.md:381).
- ATC decomposition: [lines 433–450](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Optimal_Flight_Speed_Scheduling_and_Battery_Swapping_in_UAV-Enabled_Mobile_Edge_Computing/Optimal_Flight_Speed_Scheduling_and_Battery_Swapping_in_UAV-Enabled_Mobile_Edge_Computing.md:433).
- Simulation setup and findings: [lines 542–562](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Optimal_Flight_Speed_Scheduling_and_Battery_Swapping_in_UAV-Enabled_Mobile_Edge_Computing/Optimal_Flight_Speed_Scheduling_and_Battery_Swapping_in_UAV-Enabled_Mobile_Edge_Computing.md:542).

## [14] Design, Modeling, and Implementation of Robust Migration of Stateful Edge Microservices

**Bibliographic verification**

- Authors: Antonio Calagna, Yenchia Yu, Paolo Giaccone, and Carla Fabiana Chiasserini.
- Venue: *IEEE Transactions on Network and Service Management*, vol. 21, no. 2, pp. 1877–1893.
- Year: 2024 (April 2024 issue; the PDF notes 2023 online publication/copyright).
- DOI: [10.1109/TNSM.2023.3331750](https://doi.org/10.1109/TNSM.2023.3331750).
- Local artifacts: [PDF](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Design_Modeling_and_Implementation_of_Robust_Migration_of_Stateful_Edge_Microservices/Design_Modeling_and_Implementation_of_Robust_Migration_of_Stateful_Edge_Microservices.pdf); [Markdown](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Design_Modeling_and_Implementation_of_Robust_Migration_of_Stateful_Edge_Microservices/Design_Modeling_and_Implementation_of_Robust_Migration_of_Stateful_Edge_Microservices.md).
- Title, authors, venue, volume/issue/pages, year, and DOI were checked against the first page of the local PDF.

**Model/evidence status**

- Mathematical model: **local analysis**, not end-to-end migration/replacement optimization. Processing-Aware Migration $PAM$ fits checkpoint, dump, restore, and transfer components from measurements and gives worst-case upper bounds for traditional/COAT migration duration and downtime. Equations (33)–(34) and (37) invert those bounds to configure bandwidth or iteration count for KPI/safety thresholds.
- Algorithm: **COAT migration procedure + PAM analytical configuration**. COAT (Container OverlAy TCP) uses an OvS/VXLAN overlay, TCP_REPAIR, and CRIU/Podman Iterative PreCopy to preserve existing TCP connections; no named global optimizer is used.
- Evaluation: **testbed + analytical use cases**. A three-VM testbed and DPRGen synthetic microservice, plus real MQTT Broker/Memcached validation, are used. The UAV controller is a PAM-exploitation use case with an analytical stopping-distance safety model, not a UAV-to-UAV experiment.
- Paper type: systems/network mechanism, measurement-derived analytical modeling, implementation, and validation paper.

**Scenario**

- Topology: source host, destination host, and mobile end device are connected by an SDN/OvS overlay. An edge orchestrator triggers migration and an SDN controller configures the overlay. A representative mobile endpoint is a UAV; an edge-hosted controller microservice follows it to a nearby edge server.
- Nodes: mobile client/UAV, source/destination edge host, BS, edge-service orchestrator, SDN controller, and stateful microservice container.
- Application: generic stateful microservices whose state includes CPU context, memory pages, network sockets, and open file descriptors. MQTT Broker and Memcached validate the mechanism; an edge-hosted UAV-autopilot microservice is an analytical use case.
- Assumptions: container Iterative PreCopy is the focus; PostCopy/HybridCopy are not supported for containers; the source microservice runs during dirty-page iterations and stops at final Stop&Copy, then the destination restores it; COAT recreates the namespace/IP exactly and preserves client reachability; the worst-case dirty rate is $\hat R$.
- Multiple access: **not specified**. The UAV–BS wireless link is background connectivity only and has no resource allocation.
- Channel model: **no wireless channel model**. The network model uses source–destination link capacity $L$ and $T_i^{net}=V_i/L$; COAT can operate over different communication technologies.

**Problem & objective**

- **No unified numbered optimization problem or objective function.** PAM predicts KPI values; the paper characterizes/minimizes service disruption by configuring $T_{coat}^{down}\le\theta^{down}$, $T_{coat}^{mig}\le\theta^{mig}$, or UAV stopping distance $D_s(v)\le D_s^*$.
- Key analytical outputs: traditional downtime/migration duration (29)–(30), COAT downtime/migration duration (31)–(32), required bandwidth lower bound (33), admissible dump iterations (34), and UAV safe-control bandwidth (37).
- Metrics: migration duration, microservice downtime/frozen time, checkpoint volume, network transfer time, prediction error, reaction/braking distance, and worst-case stopping distance.

**Decision variables**

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Allocated source–destination bandwidth | `L` | Positive continuous | Configured from the lower bounds in (33) or (37) to satisfy downtime or stopping-distance thresholds. |
| Number of dump/PreCopy iterations | `I` | Nonnegative integer | Inverted from (34) for a target migration duration and controls pre-copy length. |
| Migration procedure | traditional vs. COAT | Categorical design choice | Procedure analyzed by the paper; not jointly optimized in an objective function. |

The remaining quantities $`M`, `R_i`/`R_hat`, `\rho`, `\sigma`, `\alpha_1`–`\alpha_4`, and timing coefficients$ are workload/network measurements or fitted parameters. Source and destination hosts are supplied by the orchestrator; the paper does not select a replacement node.

**Constraints**

| ID | Meaning and key expression |
|---|---|
| (21), memory-processing factor | $0<\eta(R_i)\le1$; domain of the dump memory-work model, not a global resource constraint. |
| (33), target downtime feasibility | $T_{coat}^{down}\le\theta^{down}$ is inverted to a bandwidth lower bound; the denominator must be positive for feasible positive bandwidth. |
| (34), target migration duration | $T_{coat}^{mig}\le\theta^{mig}$, then floor is used for an executable iteration count $I$. |
| (37), UAV stopping safety | $D_s(v)=D_r(v)+D_b(v)\le D_s^*$, with $D_r=v(T_{coat}^{down}+T^v+T^{proc})$, $D_b=v^2m_{UAV}/(2F_b)$; this yields an $L$ lower bound. |
| COAT restoration requirements | Destination recreates the same IP/network namespace and the overlay preserves direct reachability; implementation prerequisites, not numbered mathematical constraints. |

**Relation to our scenario**

| Element | Yes / No / Partial | Grounded interpretation |
|---|---|---|
| Battery-triggered UAV replacement | No | The UAV use case is triggered by mobility/QoE and edge-controller migration, not low battery. |
| Stateful running service | Yes | CPU context, memory, sockets, and file descriptors are explicitly migrated and restored so the service resumes its prior state. |
| Replacement selection | No | Source and destination hosts are specified by the orchestrator; PAM only configures bandwidth and iterations. |
| Finite standby pool and long-term rotation | No | No standby UAV pool, charging, or rotation state is modeled. |
| Source continues during replacement flight | Partial | The source runs during Iterative PreCopy and stops only at final Stop&Copy; there is no replacement UAV flight. |
| Mobile A2A state synchronization | No | State traverses a capacity-$L$ link between fixed edge hosts; the UAV is a client, not the destination compute node. |
| Source-UAV return-energy constraint | No | Only stopping-distance safety is modeled; no flight energy or return reserve exists. |

**Full-text evidence**

- Runtime-state scope: [lines 20–24](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Design_Modeling_and_Implementation_of_Robust_Migration_of_Stateful_Edge_Microservices/Design_Modeling_and_Implementation_of_Robust_Migration_of_Stateful_Edge_Microservices.md:20).
- Source continuation, Stop&Copy, and restoration: [lines 47–57](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Design_Modeling_and_Implementation_of_Robust_Migration_of_Stateful_Edge_Microservices/Design_Modeling_and_Implementation_of_Robust_Migration_of_Stateful_Edge_Microservices.md:47).
- Fixed-host/mobile-client topology and orchestrator scope: [lines 147–170](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Design_Modeling_and_Implementation_of_Robust_Migration_of_Stateful_Edge_Microservices/Design_Modeling_and_Implementation_of_Robust_Migration_of_Stateful_Edge_Microservices.md:147).
- COAT Stop&Copy steps and downtime/migration expressions: [lines 172–205](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Design_Modeling_and_Implementation_of_Robust_Migration_of_Stateful_Edge_Microservices/Design_Modeling_and_Implementation_of_Robust_Migration_of_Stateful_Edge_Microservices.md:172).
- Three-VM testbed and 200-run measurement: [lines 216–236](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Design_Modeling_and_Implementation_of_Robust_Migration_of_Stateful_Edge_Microservices/Design_Modeling_and_Implementation_of_Robust_Migration_of_Stateful_Edge_Microservices.md:216).
- PAM checkpoint/data-volume/link-capacity relations: [lines 324–402](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Design_Modeling_and_Implementation_of_Robust_Migration_of_Stateful_Edge_Microservices/Design_Modeling_and_Implementation_of_Robust_Migration_of_Stateful_Edge_Microservices.md:324).
- PAM downtime and migration-duration upper bounds: [lines 416–452](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Design_Modeling_and_Implementation_of_Robust_Migration_of_Stateful_Edge_Microservices/Design_Modeling_and_Implementation_of_Robust_Migration_of_Stateful_Edge_Microservices.md:416).
- MQTT/Memcached validation and error results: [lines 454–495](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Design_Modeling_and_Implementation_of_Robust_Migration_of_Stateful_Edge_Microservices/Design_Modeling_and_Implementation_of_Robust_Migration_of_Stateful_Edge_Microservices.md:454).
- KPI-based bandwidth/iteration inversion: [lines 499–538](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Design_Modeling_and_Implementation_of_Robust_Migration_of_Stateful_Edge_Microservices/Design_Modeling_and_Implementation_of_Robust_Migration_of_Stateful_Edge_Microservices.md:499).
- UAV stopping-distance and safe-bandwidth model: [lines 540–589](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Design_Modeling_and_Implementation_of_Robust_Migration_of_Stateful_Edge_Microservices/Design_Modeling_and_Implementation_of_Robust_Migration_of_Stateful_Edge_Microservices.md:540).

## [15] MOSE: A Novel Orchestration Framework for Stateful Microservice Migration at the Edge

**Bibliographic verification**

- Authors: Antonio Calagna, Yenchia Yu, Paolo Giaccone, and Carla Fabiana Chiasserini.
- Venue: *IEEE Transactions on Network and Service Management*, vol. 22, no. 5, pp. 4827–4841.
- Year: 2025 (October 2025 issue).
- DOI: [10.1109/TNSM.2025.3579051](https://doi.org/10.1109/TNSM.2025.3579051).
- Local artifacts: [PDF](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/MOSE_A_Novel_Orchestration_Framework_for_Stateful_Microservice_Migration_at_the_Edge/MOSE_A_Novel_Orchestration_Framework_for_Stateful_Microservice_Migration_at_the_Edge.pdf); [Markdown](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/MOSE_A_Novel_Orchestration_Framework_for_Stateful_Microservice_Migration_at_the_Edge/MOSE_A_Novel_Orchestration_Framework_for_Stateful_Microservice_Migration_at_the_Edge.md).
- Title, authors, venue, volume/issue/pages, year, and DOI were checked against the first page of the local PDF.

**Model/evidence status**

- Mathematical model: **local analytical configuration**. MOSE reuses [14]'s PAM migration-KPI upper-bound model and chooses migration strategy, minimum bandwidth, and PreCopy iteration count; it does not restate PAM equations or formulate a new numbered optimization problem, so it is not full system optimization.
- Algorithm: **MOSE Migration Designer configuration algorithm**. Given profiling metrics, target KPI, and vertical objective, it outputs Cold/PreCopy/Iterative PreCopy, allocated bandwidth `L`, and iterations `I`. MOSE-MD minimizes downtime; MOSE-MR minimizes bandwidth/CPU usage. The mechanisms are COAT + CRIU/Podman, coordinated by Zenoh agents/orchestrator.
- Evaluation: **testbed + use cases**. A four-VM OpenStack testbed runs SockPerf/iPerf3 stateful microservices; AAV autopilot and multi-object tracking use PX4/Gazebo and MediaMTX/Ultralytics.
- Paper type: orchestration framework/system implementation and experimental-evaluation paper with model-based configuration.

**Scenario**

- Topology: a mobile device/AAV connects through a 5G gNB to a co-located edge server. After movement, the microservice migrates from source edge host to the destination host co-located with the current gNB. A monitoring edge server hosts the MOSE orchestrator; source, destination, and mobile device each have a MOSE agent; Zenoh coordinates control and protocol, while OvS/COAT preserves end-to-end connectivity.
- Nodes: AAV/mobile client, gNB, source/destination edge host, MOSE edge/client agents, MOSE orchestrator, and external scheduler/network controller.
- Application: generic stateful microservices; SockPerf and iPerf3 provide validation, while AAV autopilot retains tracking state and YOLOv8 + BoT-SORT retains object-tracking state.
- Assumptions: the scheduler triggers migration and supplies container ID, source/destination agent IDs, target KPIs, and objective; scheduler design is out of scope. Profiling measures available bandwidth, state size, dirty-page rate, and PAM parameters; the maximum dirty rate supplies a worst-case upper bound. The source runs during Iterative PreCopy and stops at Stop&Copy.
- Multiple access: **not specified**. Although a 5G gNB is mentioned, wireless MAC/resource allocation is not modeled.
- Channel model: **not specified analytically**. The model uses measured source–destination available bandwidth; experiments use up to 1 Gbps. The AAV/gNB radio link is treated as irrelevant to migration performance except for maintaining application connectivity.

**Problem & objective**

- **No numbered optimization problem or explicit objective function.** Two configuration branches are used:
  - MOSE-MD selects Iterative PreCopy under target migration duration $\theta^{mig}$, uses maximum available bandwidth, and computes the largest feasible $I$ to reduce downtime; if infeasible, it falls back to Cold migration.
  - MOSE-MR selects Cold migration, computes the minimum $L$ satisfying target downtime $\theta^{down}$ to reduce bandwidth/CPU consumption; if infeasible, it uses maximum bandwidth.
- Metrics: $T^{down}$, $T^{mig}$, allocated bandwidth, PreCopy iterations, phase durations, CPU consumption, AAV trajectory error, and MOT frame loss/inference rate.

**Decision variables**

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Migration strategy | `s` | Categorical `{Cold, PreCopy, Iterative PreCopy}` | Workflow selected by the designer according to objective and feasibility. |
| Allocated bandwidth | `L` | Positive continuous, bounded by measured availability | Reserved for source–destination checkpoint transfer; MOSE-MR minimizes it for a downtime target, while MOSE-MD uses maximum available bandwidth. |
| PreCopy iteration count | `I` | Nonnegative integer | Chosen from the target migration duration for Iterative PreCopy. |

Source/destination agent IDs are external task inputs, not MOSE decisions; microservice size, dirty-page rate, PAM coefficients, and KPI targets are measurements/parameters.

**Constraints**

| ID | Meaning and key expression |
|---|---|
| Target migration duration | MOSE-MD uses Iterative PreCopy only when the PAM upper bound satisfies $T^{mig}\le\theta^{mig}$, and selects $I$; otherwise it falls back to Cold migration. |
| Target downtime | MOSE-MR computes minimum $L$ satisfying $T^{down}\le\theta^{down}$; if required $L$ exceeds available bandwidth, maximum bandwidth is used and the target may remain infeasible. |
| Bandwidth availability | $L$ cannot exceed profiled source–destination available bandwidth. |
| Worst-case robustness | PAM sets dirty-page rate to its maximum so the prediction is an upper bound on downtime/migration duration. |
| Task specification | The migration task must include container ID, source/destination IDs, target KPI, and vertical objective; destination selection is outside MOSE. |

**Relation to our scenario**

| Element | Yes / No / Partial | Grounded interpretation |
|---|---|---|
| Battery-triggered UAV replacement | No | Migration is triggered by an external scheduler, mobility, or latency—not battery state. |
| Stateful running service | Yes | CRIU/COAT preserves container state and established connections; AAV autopilot and MOT retain tracking state. |
| Replacement selection | No | The task already specifies source/destination agent IDs; MOSE selects technique and resources only. |
| Finite standby pool and long-term rotation | No | No standby UAV pool, charging/reuse state, finite replacement inventory, or duty rotation exists. |
| Source continues during replacement flight | Partial | Iterative PreCopy transfers dirty pages while the source runs and Stop&Copy creates downtime; there is no replacement UAV flight. |
| Mobile A2A state synchronization | No | Checkpoint moves between fixed edge hosts; the AAV is a client/data source rather than a destination compute UAV. |
| Source-UAV return-energy constraint | No | No UAV propulsion or return-energy model; the autopilot use case measures trajectory error only. |

**Full-text evidence**

- Stateful migration, CRIU contents, and Cold/Iterative PreCopy flow: [lines 49–69](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/MOSE_A_Novel_Orchestration_Framework_for_Stateful_Microservice_Migration_at_the_Edge/MOSE_A_Novel_Orchestration_Framework_for_Stateful_Microservice_Migration_at_the_Edge.md:49).
- AAV–gNB–edge topology and three-component framework: [lines 74–92](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/MOSE_A_Novel_Orchestration_Framework_for_Stateful_Microservice_Migration_at_the_Edge/MOSE_A_Novel_Orchestration_Framework_for_Stateful_Microservice_Migration_at_the_Edge.md:74).
- State-size/dirty-rate/bandwidth profiling and worst-case quantities: [lines 96–105](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/MOSE_A_Novel_Orchestration_Framework_for_Stateful_Microservice_Migration_at_the_Edge/MOSE_A_Novel_Orchestration_Framework_for_Stateful_Microservice_Migration_at_the_Edge.md:96).
- External task inputs, strategy/bandwidth/iteration outputs, and objective branches: [lines 107–125](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/MOSE_A_Novel_Orchestration_Framework_for_Stateful_Microservice_Migration_at_the_Edge/MOSE_A_Novel_Orchestration_Framework_for_Stateful_Microservice_Migration_at_the_Edge.md:107).
- Zenoh checkpoint, namespace, flow, and restore protocol: [lines 127–135](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/MOSE_A_Novel_Orchestration_Framework_for_Stateful_Microservice_Migration_at_the_Edge/MOSE_A_Novel_Orchestration_Framework_for_Stateful_Microservice_Migration_at_the_Edge.md:127).
- Four-VM testbed and SockPerf/iPerf3 workloads: [lines 137–156](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/MOSE_A_Novel_Orchestration_Framework_for_Stateful_Microservice_Migration_at_the_Edge/MOSE_A_Novel_Orchestration_Framework_for_Stateful_Microservice_Migration_at_the_Edge.md:137).
- MOSE-MD/MR KPI-target validation: [lines 195–201](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/MOSE_A_Novel_Orchestration_Framework_for_Stateful_Microservice_Migration_at_the_Edge/MOSE_A_Novel_Orchestration_Framework_for_Stateful_Microservice_Migration_at_the_Edge.md:195).
- AAV autopilot, PX4/Gazebo, and state-size/dirty-rate results: [lines 208–220](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/MOSE_A_Novel_Orchestration_Framework_for_Stateful_Microservice_Migration_at_the_Edge/MOSE_A_Novel_Orchestration_Framework_for_Stateful_Microservice_Migration_at_the_Edge.md:208).

## [16] Efficient Live Migration of Edge Services Leveraging Container Layered Storage

**Bibliographic verification**

- Authors: Lele Ma, Shanhe Yi, Nancy Carter, and Qun Li.
- Venue: *IEEE Transactions on Mobile Computing*, vol. 18, no. 9, pp. 2020–2033.
- Year: 2019 (September 2019 issue; the PDF notes 2018 online publication/copyright).
- DOI: [10.1109/TMC.2018.2871842](https://doi.org/10.1109/TMC.2018.2871842).
- Local artifacts: [PDF](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Efficient_Live_Migration_of_Edge_Services_Leveraging_Container_Layered_Storage/Efficient_Live_Migration_of_Edge_Services_Leveraging_Container_Layered_Storage.pdf); [Markdown](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Efficient_Live_Migration_of_Edge_Services_Leveraging_Container_Layered_Storage/Efficient_Live_Migration_of_Edge_Services_Leveraging_Container_Layered_Storage.md).
- Title, authors, venue, volume/issue/pages, year, and DOI were checked against the first page of the local PDF.

**Model/evidence status**

- Mathematical model: **no mathematical model**. The paper gives qualitative trade-offs, system parameters, and experimental statistics, but no objective, decision vector, or constraint set.
- Algorithm: **no formal optimization algorithm**. The contribution is a container layered-storage live-migration workflow with layer-ID remapping, base-memory pre-dump, dirty-memory synchronization, compression, and parallel/pipelined processing.
- Evaluation: **testbed**. Two VMs run Docker and network emulation tests use Busybox/OpenFace.
- Paper type: system architecture, storage mechanism, prototype implementation, and experimental-evaluation paper.

**Scenario**

- Topology: three-level edge platform with a centralized edge controller/cloud, distributed edge nodes over a WAN, and mobile clients. An offloading container migrates from a source edge server/VM to a target edge server/VM; the controller provides scheduling, monitoring, image service, and authentication.
- Nodes: mobile user/client, source/target edge server or cluster, Docker-host VM, offloading container, central edge controller, and container/VM image service.
- Application: generic computation-offloading service; Busybox and OpenFace face recognition are evaluated while a mobile client continuously sends camera images and receives recognition results.
- Assumptions: source and target download common base-image layers before handoff; base-memory image transfer finishes before handoff; potential target servers are known and pre-provisioned; source runs during pre-transfer and stops only when dirty memory/files are small enough; containers run inside VMs.
- Multiple access: mobile devices may use Wi-Fi or LTE to reach edge nodes, but **no multi-access or resource-allocation model is specified**.
- Channel model: **no analytical channel model**. Linux `tc` emulates WAN 5–45 Mbps/50 ms and LAN 50–500 Mbps/6 ms, with varied compression and iteration settings.

**Problem & objective**

- **No optimization problem or objective function.** End-user QoS is called the ultimate optimization goal, but the paper explicitly provides no concrete optimization target; it exposes configurable strategies and metrics.
- Interruption time, service downtime, and total migration time are evaluation metrics, not a formal single- or multi-objective function.
- Cloud go/no-go, migration timing, and target-server selection are outside scope; the paper implements migration mechanisms and collects edge-node measurements.

**Decision variables**

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| None | — | — | No optimization decisions. Compression option, iteration count, bandwidth, and latency are configurable/measured parameters varied in experiments, not solved optima. |

**Constraints**

| ID | Meaning and key expression |
|---|---|
| No mathematical constraints | Operational conditions only: final dirty memory/files must be “small enough” before source stop, and base-memory transfer is assumed complete before handoff; no threshold formula or feasible set is given. |

**Relation to our scenario**

| Element | Yes / No / Partial | Grounded interpretation |
|---|---|---|
| Battery-triggered UAV replacement | No | Trigger is a mobile-user service handoff request, not UAV battery state. |
| Stateful running service | Yes | Runtime memory, dirty memory, writable container layer, and metadata are migrated. |
| Replacement selection | Partial | A central scheduler may select a target using location/load/bandwidth/latency, but this paper does not implement or solve that choice. |
| Finite standby pool and long-term rotation | No | Potential target servers are pre-provisioned, but no finite standby pool, charging, or rotation state exists. |
| Source continues during replacement flight | Partial | Source runs during base-memory/dirty-memory pre-transfer and stops in the final round; there is no UAV flight. |
| Mobile A2A state synchronization | No | Fixed edge servers synchronize over a WAN; no mobile A2A channel is modeled. |
| Source-UAV return-energy constraint | No | No UAV flight, propulsion energy, or return constraint exists. |

**Full-text evidence**

- Mobile-user service handoff: [lines 57–70](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Efficient_Live_Migration_of_Edge_Services_Leveraging_Container_Layered_Storage/Efficient_Live_Migration_of_Edge_Services_Leveraging_Container_Layered_Storage.md:57).
- Three-level topology, nodes, and Wi-Fi/LTE access: [lines 176–215](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Efficient_Live_Migration_of_Edge_Services_Leveraging_Container_Layered_Storage/Efficient_Live_Migration_of_Edge_Services_Leveraging_Container_Layered_Storage.md:176).
- Complete migration workflow and source-stop point: [lines 217–246](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Efficient_Live_Migration_of_Edge_Services_Leveraging_Container_Layered_Storage/Efficient_Live_Migration_of_Edge_Services_Leveraging_Container_Layered_Storage.md:217).
- Base-memory pre-transfer assumption: [lines 273–277](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Efficient_Live_Migration_of_Edge_Services_Leveraging_Container_Layered_Storage/Efficient_Live_Migration_of_Edge_Services_Leveraging_Container_Layered_Storage.md:273).
- Metrics and explicit absence of a concrete optimization target: [lines 301–323](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Efficient_Live_Migration_of_Edge_Services_Leveraging_Container_Layered_Storage/Efficient_Live_Migration_of_Edge_Services_Leveraging_Container_Layered_Storage.md:301).
- Target-selection decision outside scope: [lines 341–345](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Efficient_Live_Migration_of_Edge_Services_Leveraging_Container_Layered_Storage/Efficient_Live_Migration_of_Edge_Services_Leveraging_Container_Layered_Storage.md:341).
- Testbed and WAN/LAN parameters: [lines 347–369](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Efficient_Live_Migration_of_Edge_Services_Leveraging_Container_Layered_Storage/Efficient_Live_Migration_of_Edge_Services_Leveraging_Container_Layered_Storage.md:347).

## [17] KubeSPT: Stateful Pod Teleportation for Service Resilience With Live Migration

**Bibliographic verification**

- Authors: Hansheng Zhang, Song Wu, Hao Fan, Zhuo Huang, Weibin Xue, Chen Yu, Shadi Ibrahim, and Hai Jin.
- Venue: *IEEE Transactions on Services Computing*, vol. 18, no. 3, pp. 1500–1514.
- Year: 2025 (May/June 2025 issue).
- DOI: [10.1109/TSC.2025.3564888](https://doi.org/10.1109/TSC.2025.3564888).
- Local artifacts: [PDF](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/sources/KubeSPT_Stateful_Pod_Teleportation_for_Service_Resilience_With_Live_Migration/KubeSPT_Stateful_Pod_Teleportation_for_Service_Resilience_With_Live_Migration.pdf); [Markdown](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/sources/KubeSPT_Stateful_Pod_Teleportation_for_Service_Resilience_With_Live_Migration/KubeSPT_Stateful_Pod_Teleportation_for_Service_Resilience_With_Live_Migration.md).
- Title, authors, venue, volume/issue/pages, year, and DOI were checked against the first page of the local PDF.

**Model/evidence status**

- Mathematical model: **local analysis**. The paper gives downtime decompositions (1) and (2), but no objective function, decision vector, or feasible-domain constraints; it is not a complete optimization problem.
- Algorithm: **KubeSPT workflow/system mechanisms**: CRD/Controller plus per-node Migration Daemon; T-Checkpointer iterative checkpoint/hot-page tracking; T-Proxy network freeze/cache/redirect; T-Restorer Hot Data and Lazy-Restore; migration-aware pod recreation and Kubernetes-controller alignment. No node-selection or resource-optimization solver is used.
- Evaluation: **testbed**. A three-node Kubernetes cluster runs Redis and FFmpeg workloads and measures downtime, application performance, total migration time, and controller reliability.
- Paper type: cloud/container systems design, kernel/runtime modification, implementation, and experimental-evaluation paper.

**Scenario**

- Topology: one Kubernetes data-center cluster with leader/control plane and worker nodes. A stateful pod live-migrates from a source worker to a destination worker. The controller invokes the scheduler to select a target and reserve resources; each node runs a Migration Daemon; external clients retain TCP connections.
- Nodes: Kubernetes Controller/Scheduler/Kubelet/CNI, source/destination worker node, migrated pod (stateful primary and auxiliary containers), external clients, and T-Checkpointer/T-Proxy/T-Restorer.
- Application: stateful long-running applications with network and memory state; experiments use Redis (memory/cache/database) and concurrent FFmpeg video decode/transcode.
- Assumptions: live migration preserves pod name/IP and TCP state; service continues during iterative checkpoint; final checkpoint/delete/recreate/restore causes downtime; Hot Data + Lazy-Restore targets skewed memory footprints with stable short-term hotspots and requires prior memory-access knowledge; the core scope focuses on remote PVC/RWX, not local/emptyDir storage.
- Multiple access: **none**. This is a data-center/Kubernetes cluster with no wireless access.
- Channel model: **none**. Worker bandwidth is fixed at 3 Gbps in experiments; network transfer is measured, not modeled with a channel or MAC equation.

**Problem & objective**

- **No optimization problem, problem ID, or objective function.** The design objective is to minimize stateful-pod rescheduling downtime while maintaining TCP continuity, restoring runtime memory state, and remaining compatible with Kubernetes reconciliation.
- Local analysis: baseline downtime (1) $T_D=G_D(M_{FD})+G_T(M_{FD})+G_R(M_W)+T_{Restart}+T_{Reconnect}+T_{Others}$; KubeSPT downtime (2) $T_D=\max(T_{Restart},G_{FT}(M_{FD}))+G_{HL}(M_H)+T_{Others}$.
- Metrics: downtime/components, checkpoint sizes, network redirection time, Redis throughput/latency, FFmpeg transcoding time/speed, total migration time, and controller reliability.

**Decision variables**

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| None | — | — | The target node is selected by the existing Kubernetes Scheduler/placement strategy; KubeSPT does not optimize the destination. Hot-page set, checkpoint iteration/termination, and 16-page fetch batch are mechanism states or heuristic settings, not a joint objective-vector decision. |

**Constraints**

| ID | Meaning and key expression |
|---|---|
| Same identity/connectivity | Preserve pod name/IP; freeze the destination namespace, cache packets, and release them after restore to avoid TCP disconnect. |
| Iteration termination | From the second checkpoint, continue only when dirty pages decrease sufficiently relative to the prior round; stop early after several rounds without material decrease. No numeric ratio is given. |
| Hot-data applicability | The method assumes skewed, stable memory footprints and prior memory-access-pattern knowledge. |
| Volume scope | Core design targets remote persistent storage/RWX PVC; RWO/local/emptyDir require another iterative data-migration method. |
| Failure boundary | Stage 1 failure can terminate while the source continues; Stage 2 communication failure during final-checkpoint transfer can lose pod state; after Stage 3 data reaches the destination, communication failure does not prevent restore. |

**Relation to our scenario**

| Element | Yes / No / Partial | Grounded interpretation |
|---|---|---|
| Battery-triggered UAV replacement | No | Rescheduling is triggered by upgrade, failure, or load balancing, not UAV battery state. |
| Stateful running service | Yes | Network connections, process memory, and context are preserved/restored; Redis and FFmpeg resume from an intermediate running state. |
| Replacement selection | No | The target worker is selected by the existing scheduler; KubeSPT reuses the placement strategy. |
| Finite standby pool and long-term rotation | No | No standby pool, charging/recovery, or long-term worker-duty rotation is optimized. |
| Source continues during replacement flight | Partial | Iterative checkpoint does not interrupt the source; final checkpoint enters downtime, but there is no replacement flight. |
| Mobile A2A state synchronization | No | Checkpoint transfer is between fixed data-center workers, with no mobile nodes or A2A link. |
| Source-UAV return-energy constraint | No | No UAV, flight, or energy model exists. |

**Full-text evidence**

- Stateful-pod rescheduling network/memory/context challenges: [lines 11–25](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/sources/KubeSPT_Stateful_Pod_Teleportation_for_Service_Resilience_With_Live_Migration/KubeSPT_Stateful_Pod_Teleportation_for_Service_Resilience_With_Live_Migration.md:11).
- Baseline downtime decomposition and local challenges: [lines 82–107](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/sources/KubeSPT_Stateful_Pod_Teleportation_for_Service_Resilience_With_Live_Migration/KubeSPT_Stateful_Pod_Teleportation_for_Service_Resilience_With_Live_Migration.md:82).
- KubeSPT mechanisms, three-stage workflow, and optimized downtime: [lines 109–129](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/sources/KubeSPT_Stateful_Pod_Teleportation_for_Service_Resilience_With_Live_Migration/KubeSPT_Stateful_Pod_Teleportation_for_Service_Resilience_With_Live_Migration.md:109).
- T-Proxy freeze/cache/redirect and TCP continuity: [lines 131–153](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/sources/KubeSPT_Stateful_Pod_Teleportation_for_Service_Resilience_With_Live_Migration/KubeSPT_Stateful_Pod_Teleportation_for_Service_Resilience_With_Live_Migration.md:131).
- Source-running iterative checkpoint and final transfer: [lines 155–166](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/sources/KubeSPT_Stateful_Pod_Teleportation_for_Service_Resilience_With_Live_Migration/KubeSPT_Stateful_Pod_Teleportation_for_Service_Resilience_With_Live_Migration.md:155).
- Lazy-Restore/userfaultfd and batched restore: [lines 166–172](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/sources/KubeSPT_Stateful_Pod_Teleportation_for_Service_Resilience_With_Live_Migration/KubeSPT_Stateful_Pod_Teleportation_for_Service_Resilience_With_Live_Migration.md:166).
- Parallel pod recreation, Kubernetes alignment, and volume scope: [lines 174–192](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/sources/KubeSPT_Stateful_Pod_Teleportation_for_Service_Resilience_With_Live_Migration/KubeSPT_Stateful_Pod_Teleportation_for_Service_Resilience_With_Live_Migration.md:174).
- Three-node testbed and 3 Gbps link: [lines 194–212](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/sources/KubeSPT_Stateful_Pod_Teleportation_for_Service_Resilience_With_Live_Migration/KubeSPT_Stateful_Pod_Teleportation_for_Service_Resilience_With_Live_Migration.md:194).
- Redis/FFmpeg workloads, metrics, and ten-run method: [lines 221–246](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/sources/KubeSPT_Stateful_Pod_Teleportation_for_Service_Resilience_With_Live_Migration/KubeSPT_Stateful_Pod_Teleportation_for_Service_Resilience_With_Live_Migration.md:221).

## [18] Multi-Cell Mobile Edge Computing: Joint Service Migration and Resource Allocation

**Bibliographic verification**

- Authors: Zezu Liang, Yuan Liu, Tat-Ming Lok, and Kaibin Huang.
- Venue: *IEEE Transactions on Wireless Communications*, vol. 20, no. 9, September 2021, pp. 5898–5912.
- Year: 2021 (first page: received 20 September 2020; accepted 22 March 2021; published 12 April 2021; current version 10 September 2021).
- DOI: [10.1109/TWC.2021.3070974](https://doi.org/10.1109/TWC.2021.3070974).
- Local artifacts: [PDF](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Multi-Cell_Mobile_Edge_Computing_Joint_Service_Migration_and_Resource_Allocation/Multi-Cell_Mobile_Edge_Computing_Joint_Service_Migration_and_Resource_Allocation.pdf); [Markdown](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Multi-Cell_Mobile_Edge_Computing_Joint_Service_Migration_and_Resource_Allocation/Multi-Cell_Mobile_Edge_Computing_Joint_Service_Migration_and_Resource_Allocation.md).
- Title, authors, journal/volume/issue/pages, dates, and DOI were checked against the first page of the local publisher PDF.

**Model/evidence status**

- Mathematical model: **complete optimization**. P1 is an integer nonlinear program for joint service migration/BS handover, computation-load balancing, and radio/computation-aware placement with explicit assignment and VM-capacity constraints. A radio-RB extension and hotspot-mitigation special case are also derived.
- Algorithm: two-stage relaxation-and-rounding (Algorithm 2). Integer relaxation and a sum-of-ratios fractional-programming transform are solved by Algorithm 1 with a modified Newton update; BS loads are rounded and a Hungarian Linear Assignment Problem recovers binary JMH decisions. The hotspot special case has an optimal rounding result under its stated regime.
- Evaluation: **simulation**. A seven-BS, 1 km$^2$ simulation with Random Waypoint users and 500 Monte Carlo runs compares exhaustive search/upper bounds, no migration, and radio-oriented migration; no testbed is reported.
- Paper type: joint cellular-MEC service-placement/resource-management optimization and simulation paper.

**Scenario**

- Topology: $N$ fixed cellular BSs, each co-located with an MEC server, serve $K$ mobile users. A user's wireless handover and VM/service migration between fixed BS/server sites are coupled; the hotspot case adds helper BSs around an overloaded macro BS.
- Nodes: mobile users, fixed BSs/MEC servers, and one dedicated VM per user. No UAV nodes exist.
- Application: computation-intensive/latency-critical mobile applications offloaded into per-user VMs. Each VM is a software clone of the user's service environment containing profiles/applications for offloaded tasks and can migrate as the user moves.
- Assumptions: slotted system; user association and channel gains are constant within a slot but vary between slots; one dedicated VM and one BS association per user; migration/handover time is negligible relative to a slot; download results are ignored; VM co-location causes I/O interference.
- Multiple access: baseline P1 uses same-band uplink with reuse factor 1, fixed transmit powers, and multi-user interference in SINR. Section III-E extends it with per-BS radio-resource blocks $b_{k,n}$.
- Channel model: abstract gain $g_{k,n}$ includes path loss and shadowing; small-scale fading is neglected/averaged. Rate is Shannon bandwidth times $\log_2(1+\mathrm{SINR})$; simulations use path loss $128.1+37.6\log_{10}l[\mathrm{km}]$ dB.

**Problem & objective**

- Problem **P1** computes optimal JMH decisions from a current placement.
- Type: binary integer nonlinear program, nonconvex through load-dependent computation rates; brute-force complexity is $O(N^K)$.
- Objective (5):

  $$
  \max_{\mathbf X}\;\sum_{k\in\mathcal K}\omega_k\sum_{n\in\mathcal N}x_{k,n}R_{k,n}-\lambda\sum_{k\in\mathcal K}\sum_{n,j\in\mathcal N}x_{k,j}^{0}x_{k,n}c_{k,j,n}.
  $$

  It maximizes weighted offloading throughput while penalizing VM-migration plus handover cost.
- Metrics: objective/sum utility, weighted/sum offloading rate, total JMH cost, migrated-user percentage, I/O-degradation resistance, mobility sensitivity, load distribution, and running complexity.

**Decision variables**

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| JMH/service placement | $x_{k,n}$ | Binary, $\{0,1\}$ | 1 iff user $k$'s VM/service and radio association are placed at BS $n$ for the next slot. |
| Relaxed BS load | $y_n$ | Continuous in relaxation; recovered integer | Auxiliary number of VMs/users hosted at BS $n$, equal to $\sum_kx_{k,n}$ at optimum. |
| RB allocation (extension) | $b_{k,n}$ | Nonnegative integer | Number of resource blocks allocated to user $k$ at BS $n$ in the radio-resource extension. |

Current placement $x_{k,j}^{0}$, migration/handover cost $c_{k,j,n}$, weights, channel gains, powers, isolated VM rates, I/O degradation, and capacities are parameters.

**Constraints**

| ID | Meaning and key expression |
|---|---|
| (6) | Exactly one BS/VM location per user: $\sum_nx_{k,n}=1$. |
| (7) | Per-BS VM capacity: $\sum_kx_{k,n}\le M_n$. |
| (8) | Binary JMH placement: $x_{k,n}\in\{0,1\}$. |
| (10)–(13) | Relaxed P1*: assignment equality, $y_n\ge\sum_kx_{k,n}$, $0\le x_{k,n}\le1$, and $0\le y_n\le M_n$. |
| Radio extension | Allocation is tied to association and total RBs at a BS cannot exceed its RB budget; $b_{k,n}$ is derived in the extended problem. |
| Hotspot special case | Recovered integer loads sum to the number of users and respect helper/macro capacities; the assignment is solved as a LAP. |

**Relation to our scenario**

| Element | Yes / No / Partial | Grounded interpretation |
|---|---|---|
| Battery-triggered UAV replacement | No | Infrastructure is fixed BS/MEC servers. Migration responds to handover, radio quality, server load, and cost, not UAV battery. |
| Stateful running service | Partial | A per-user VM contains the service environment and is migrated, but migration time is negligible and runtime-state evolution, checkpointing, dirty state, and consistency are absent. |
| Replacement selection | Partial | $x_{k,n}$ selects a destination fixed BS/server for the VM/service, not an airborne replacement UAV. |
| Finite standby pool and long-term rotation | No | BS/server capacities are finite, but no standby UAV pool, recharge/recovery, repeated flight duty, or rotation is modeled. |
| Source continues during replacement flight | No | No UAV or replacement flight exists; migration/handover time is assumed negligible. |
| Mobile A2A state synchronization | No | Migration uses fixed-server backhaul, with no mobile A2A or application-state synchronization process. |
| Source-UAV return-energy constraint | No | No UAV propulsion, battery, base-return, or reserve-energy constraint exists. |

**Full-text evidence**

- Fixed multi-cell MEC motivation, JMH boundary, objective, and algorithm: [lines 15–35](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Multi-Cell_Mobile_Edge_Computing_Joint_Service_Migration_and_Resource_Allocation/Multi-Cell_Mobile_Edge_Computing_Joint_Service_Migration_and_Resource_Allocation.md:15).
- Fixed BS/server topology, VM semantics, slot assumptions, JMH variable, cost, and negligible migration time: [lines 43–54](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Multi-Cell_Mobile_Edge_Computing_Joint_Service_Migration_and_Resource_Allocation/Multi-Cell_Mobile_Edge_Computing_Joint_Service_Migration_and_Resource_Allocation.md:43).
- Same-band reuse-1 uplink and SINR model: [lines 56–62](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Multi-Cell_Mobile_Edge_Computing_Joint_Service_Migration_and_Resource_Allocation/Multi-Cell_Mobile_Edge_Computing_Joint_Service_Migration_and_Resource_Allocation.md:56).
- VM computation/I/O interference, capacity, and offloading-rate model: [lines 64–78](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Multi-Cell_Mobile_Edge_Computing_Joint_Service_Migration_and_Resource_Allocation/Multi-Cell_Mobile_Edge_Computing_Joint_Service_Migration_and_Resource_Allocation.md:64).
- P1 objective, assignment/capacity constraints, and complexity: [lines 80–106](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Multi-Cell_Mobile_Edge_Computing_Joint_Service_Migration_and_Resource_Allocation/Multi-Cell_Mobile_Edge_Computing_Joint_Service_Migration_and_Resource_Allocation.md:80).
- Relaxation/rounding and Hungarian recovery: [lines 108–138](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Multi-Cell_Mobile_Edge_Computing_Joint_Service_Migration_and_Resource_Allocation/Multi-Cell_Mobile_Edge_Computing_Joint_Service_Migration_and_Resource_Allocation.md:108).
- Hungarian recovery and Algorithm 2: [lines 306–367](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Multi-Cell_Mobile_Edge_Computing_Joint_Service_Migration_and_Resource_Allocation/Multi-Cell_Mobile_Edge_Computing_Joint_Service_Migration_and_Resource_Allocation.md:306).
- Simulation topology, mobility, and exact/upper-bound comparisons: [lines 581–604](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Multi-Cell_Mobile_Edge_Computing_Joint_Service_Migration_and_Resource_Allocation/Multi-Cell_Mobile_Edge_Computing_Joint_Service_Migration_and_Resource_Allocation.md:581).
- Mobility, migration-rate, and cost-throughput results: [lines 611–627](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Multi-Cell_Mobile_Edge_Computing_Joint_Service_Migration_and_Resource_Allocation/Multi-Cell_Mobile_Edge_Computing_Joint_Service_Migration_and_Resource_Allocation.md:611).

## [19] Mobility-Aware Seamless Service Migration and Resource Allocation in Multi-Edge IoV Systems

**Bibliographic verification**

- Authors: Zheyi Chen, Sijin Huang, Geyong Min, Zhaolong Ning, Jie Li, and Yan Zhang.
- Venue: *IEEE Transactions on Mobile Computing*, vol. 24, no. 7, July 2025, pp. 6315–6332.
- Year: 2025 (first page: received 29 November 2024; accepted 6 February 2025; published 11 February 2025; current version 5 June 2025).
- DOI: [10.1109/TMC.2025.3540407](https://doi.org/10.1109/TMC.2025.3540407).
- Local artifacts: [PDF](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Mobility-Aware_Seamless_Service_Migration_and_Resource_Allocation_in_Multi-Edge_IoV_Systems/Mobility-Aware_Seamless_Service_Migration_and_Resource_Allocation_in_Multi-Edge_IoV_Systems.pdf); [Markdown](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Mobility-Aware_Seamless_Service_Migration_and_Resource_Allocation_in_Multi-Edge_IoV_Systems/Mobility-Aware_Seamless_Service_Migration_and_Resource_Allocation_in_Multi-Edge_IoV_Systems.md).
- Title, authors, journal/volume/issue/pages, dates, and DOI were checked against the first page of the local publisher PDF.

**Model/evidence status**

- Mathematical model: **complete optimization**. MINLP P1 jointly minimizes long-term migration, communication, and computation delay through discrete service destinations and continuous CPU shares. It is decoupled into service-migration P2 and resource-allocation P3/P4.
- Algorithm: **SR-CL** (mobility-aware seamless Service migration and Resource allocation via Convex-optimization-enabled deep Reinforcement Learning). A delayed-update actor/one-step-update critic selects migrations; convex/KKT analysis gives optimal per-server CPU share $e_{z,t}\propto\sqrt{K_{z,t}}$.
- Evaluation: **simulation + Simu5G-based emulation**. Simulations use 320 Rome taxi trajectories and 16-/25-edge-node topologies, comparing DDPG, JSR, IDQN, GA, Never Migrate, and Always Migrate. OMNeT++/INET/Simu5G emulates 5G RAN/core/MEC with 10 moving UEs and two gNBs/MEC hosts.
- Paper type: sequential service-migration/resource-allocation optimization with DRL/convex algorithm, trace-driven simulation, and network-emulation validation.

**Scenario**

- Topology: a central MEC controller manages $M$ fixed BS/MEC edge nodes connected by stable multi-hop backhaul; $U$ intelligent vehicles connect to their nearest BS. A task may traverse backhaul to the server holding its service instance, or the instance may migrate to another fixed node.
- Nodes: intelligent vehicles, fixed BSs/co-located MEC servers, switches/backhaul, and central MEC controller/DRL agent. No UAVs exist.
- Application: per-vehicle intelligent applications (automatic driving, image recognition, path planning). Virtualized service instances encapsulate runtime data and user context and process one computation-intensive task per slot.
- Assumptions: discrete slots; vehicles change location at boundaries; each vehicle initially creates one instance at its nearest edge node; tasks use that instance; instances run in parallel; edge nodes have stable backhaul but finite CPU; service interruption contributes to migration delay; result-download delay is neglected.
- Multiple access: **OFDM** equally divides each BS's bandwidth among connected vehicles; radio shares are not optimized.
- Channel model: distance-based SNR $P_u\alpha/(\sigma^2|Len_{u,i}|^2)$ with unit-distance gain and Gaussian noise; uplink delay uses Shannon rate. Backhaul transfers use fixed bandwidth $\chi$, data size, hop count, and per-hop delay coefficients.

**Problem & objective**

- Problems: joint MINLP **P1** (9), migration **P2** (13), joint resource subproblem **P3** (14), and per-server convex allocation **P4** (23).
- Type: mixed-integer nonlinear, long-term sequential problem; P1 is NP-hard by reduction to knapsack; P4 is convex.
- Objective (8)–(9): $\min_{\mathcal X_t,\mathcal E_t}\sum_{t=0}^{T}\mathcal G(\mathcal X_t,\mathcal E_t)$, where $\mathcal G=\sum_u(MT_{u,t}+HT_{u,t}+CT_{u,t})$. P2 minimizes total delay over migration destinations; P4 minimizes $\sum_{u\in\mathcal{IV}_m}K_{u,t}/(e_{u,t}F)$ at one server.
- Metrics: reward/convergence, migration frequency, migration/communication/computation/total delay, task-response delay, decision time, and sensitivity to CPU, traffic, hop cost, topology, bandwidth, speed, and uplink time.

**Decision variables**

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Service-migration destination | $x_{u,t}$ | Discrete integer, $\{1,\ldots,M\}$ | Edge node hosting vehicle $u$'s service instance in slot $t$. |
| CPU allocation share | $e_{u,t}$ | Continuous, $[0,1]$ | Fraction of destination MEC CPU allocated to vehicle $u$'s instance. |

Current service node, vehicle location, task/service sizes, computational density, hop distances, connected edge node, and hosted-instance sets are state/parameters.

**Constraints**

| ID | Meaning and key expression |
|---|---|
| C1/(9) | Destination: $x_{u,t}\in\{1,2,\ldots,M\}$; each instance runs on one edge node per slot. |
| C2/(9) | Per-instance CPU share: $e_{u,t}\in[0,1]$. |
| C3/(9) | Per-server CPU budget: $\sum_{u\in\mathcal{IV}_m}e_{u,t}\le1$. |
| (13) | P2 retains C1 while minimizing total delay over service migration. |
| (14)/(23) | P3/P4 retain C2–C3 and minimize compute delay for a fixed migration decision. |
| (24) | Convex restatement: $\sum_ze_{z,t}-1\le0$, $-e_{z,t}\le0$, and $e_{z,t}-1\le0$. |
| (28)–(29) | KKT feasibility gives globally optimal CPU share $e_{z,t}=\sqrt{K_{z,t}}/\sum_z\sqrt{K_{z,t}}$. |

**Relation to our scenario**

| Element | Yes / No / Partial | Grounded interpretation |
|---|---|---|
| Battery-triggered UAV replacement | No | Mobility and changing fixed-edge access trigger relocation; no UAV or battery variable exists. |
| Stateful running service | Yes | Virtualized instances encapsulate runtime data and user context and are continuously used; transferred service-data amount is $S_{u,t}$, but checkpoint consistency is abstracted. |
| Replacement selection | Partial | $x_{u,t}$ selects a destination fixed edge server, not a replacement UAV. |
| Finite standby pool and long-term rotation | No | Finite edge CPU is modeled, but not standby fleet, charge/recovery, replacement inventory, or long-term UAV rotation. |
| Source continues during replacement flight | No | No UAV flight; service interruption contributes to migration delay and source-serving overlap is not modeled. |
| Mobile A2A state synchronization | No | State moves among fixed MEC servers over stable backhaul; no live mobile synchronization model appears. |
| Source-UAV return-energy constraint | No | No UAV propulsion/return model; energy integration is future work. |

**Full-text evidence**

- Runtime-data/user-context definition and mobility-driven migration: [lines 13–17](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Mobility-Aware_Seamless_Service_Migration_and_Resource_Allocation_in_Multi-Edge_IoV_Systems/Mobility-Aware_Seamless_Service_Migration_and_Resource_Allocation_in_Multi-Edge_IoV_Systems.md:13).
- Fixed BS/MEC/controller topology and task lifecycle: [lines 49–58](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Mobility-Aware_Seamless_Service_Migration_and_Resource_Allocation_in_Multi-Edge_IoV_Systems/Mobility-Aware_Seamless_Service_Migration_and_Resource_Allocation_in_Multi-Edge_IoV_Systems.md:49).
- Migration destination, service-data amount, interruption/hop delay, and fixed backhaul: [lines 60–68](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Mobility-Aware_Seamless_Service_Migration_and_Resource_Allocation_in_Multi-Edge_IoV_Systems/Mobility-Aware_Seamless_Service_Migration_and_Resource_Allocation_in_Multi-Edge_IoV_Systems.md:60).
- Distance-SNR, OFDM access, communication delay, and compute model: [lines 70–115](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Mobility-Aware_Seamless_Service_Migration_and_Resource_Allocation_in_Multi-Edge_IoV_Systems/Mobility-Aware_Seamless_Service_Migration_and_Resource_Allocation_in_Multi-Edge_IoV_Systems.md:70).
- P1 objective, variables, constraints, and NP-hardness: [lines 118–150](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Mobility-Aware_Seamless_Service_Migration_and_Resource_Allocation_in_Multi-Edge_IoV_Systems/Mobility-Aware_Seamless_Service_Migration_and_Resource_Allocation_in_Multi-Edge_IoV_Systems.md:118).
- P2/P3 decomposition: [lines 152–177](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Mobility-Aware_Seamless_Service_Migration_and_Resource_Allocation_in_Multi-Edge_IoV_Systems/Mobility-Aware_Seamless_Service_Migration_and_Resource_Allocation_in_Multi-Edge_IoV_Systems.md:152).
- MDP state/action/reward and actor-critic algorithm: [lines 209–299](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Mobility-Aware_Seamless_Service_Migration_and_Resource_Allocation_in_Multi-Edge_IoV_Systems/Mobility-Aware_Seamless_Service_Migration_and_Resource_Allocation_in_Multi-Edge_IoV_Systems.md:209).
- Convex P4, KKT conditions, and CPU allocation: [lines 303–363](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Mobility-Aware_Seamless_Service_Migration_and_Resource_Allocation_in_Multi-Edge_IoV_Systems/Mobility-Aware_Seamless_Service_Migration_and_Resource_Allocation_in_Multi-Edge_IoV_Systems.md:303).
- Rome trajectory simulation: [lines 409–444](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Mobility-Aware_Seamless_Service_Migration_and_Resource_Allocation_in_Multi-Edge_IoV_Systems/Mobility-Aware_Seamless_Service_Migration_and_Resource_Allocation_in_Multi-Edge_IoV_Systems.md:409).
- Simu5G testbed and energy-boundary statement: [lines 544–562](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Mobility-Aware_Seamless_Service_Migration_and_Resource_Allocation_in_Multi-Edge_IoV_Systems/Mobility-Aware_Seamless_Service_Migration_and_Resource_Allocation_in_Multi-Edge_IoV_Systems.md:544).

## [20] Service Migration Strategies Based on Partially Observable and Multi-Objective Optimization

**Bibliographic verification**

- Authors: Yingzhen Hou, Lei Yang, and Yu Dai.
- Venue: *IEEE Transactions on Mobile Computing*, vol. 25, no. 3, pp. 3540–3554.
- Year: 2026 (March 2026 issue; the PDF also notes 2025 IEEE copyright and 2025-10-06 online publication).
- DOI: [10.1109/TMC.2025.3618278](https://doi.org/10.1109/TMC.2025.3618278).
- Local artifacts: [PDF](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Service_Migration_Strategies_Based_on_Partially_Observable_and_Multi-Objective_Optimization/Service_Migration_Strategies_Based_on_Partially_Observable_and_Multi-Objective_Optimization.pdf); [Markdown](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Service_Migration_Strategies_Based_on_Partially_Observable_and_Multi-Objective_Optimization/Service_Migration_Strategies_Based_on_Partially_Observable_and_Multi-Objective_Optimization.md).
- Title, authors, venue, volume/issue/pages, year, and DOI were checked against the first page of the local PDF.

**Model/evidence status**

- Mathematical model: **complete optimization**. A finite-horizon, slotted service-server selection problem (11) is followed by a POMDP observation/action/reward definition. The physical objective trades total perception delay against total energy/migration cost; training uses separate delay/energy critics and dynamic weights. Equation (11) uses the compact $r(T_{total},E_{total})$ notation, while (14) writes their negative sum; Pareto/multi-policy semantics are implemented mainly by MEMPO rather than an explicitly displayed vector objective.
- Algorithm: **AVSI-MEMPO** (Adversarial Variational State Inference with Maximum Entropy Multi-Objective Policy Optimization). AVSI combines VAE, adversarial learning, and LSTM hidden-state inference; MEMPO combines multi-critic SAC, maximum entropy, and dynamic objective weights. An oracle policy with full future information converts node choice into a shortest-path problem solved by Dijkstra.
- Evaluation: **simulation + use cases** (no real migration testbed). Rome and San Francisco taxi traces drive MEC simulation; Apple M3 “edge-terminal simulation environment” measures inference overhead. OTA industrial-update recommendations are discussed but not deployed on a real vehicle/MEC migration platform.
- Paper type: POMDP/multi-objective DRL algorithm paper with trace-driven simulation.

**Scenario**

- Topology: $N$ mobile vehicles move through an area covered by $M$ MEC server/BS pairs. Each user accesses a local server; if the selected target/service server differs, tasks traverse wired multi-hop links; service data moves from the previous source server to the target.
- Nodes: mobile user/vehicle, co-located BS–MEC server, local/source/target service server, and a user-centric lightweight agent on the terminal.
- Application: assisted driving (LiDAR/camera processing), AR navigation, and other computation-intensive low-latency IoV applications. Each slot generates a task triplet $(d_t^{task}(n),\rho_t(n),c_t(n))$ and migration data $d_t^{migration}(n)$.
- Assumptions: user position changes at slot start; migration-node selection precedes offloading and processing; each slot's task finishes in the same slot; result data is small and return transfer is ignored; users observe only local/source IDs, wireless rate, and task load/size; nonlocal server load is hidden; any MEC server in coverage can be selected.
- Multiple access: **not specified**. No OFDMA/TDMA/NOMA, user-association capacity, or bandwidth-allocation decision appears; wireless rate $\omega_t(n)$ is an observation/derived input.
- Channel model: no physical channel or MAC model. Wireless rate is an empirical distance-segment function $\omega_t(n)=12\,\mathrm{round}(R/d_t(n))$; inter-server bandwidth is fixed at 500 MB/s and wired multi-hop delay uses propagation/migration coefficients.

**Problem & objective**

- Problem (11): finite-horizon, discrete-node, time-varying, partially observable sequential multi-objective problem, subsequently modeled as a POMDP; the paper does not name it P0/P1.
- Objective display: $\min_{\{a_t(n)\}}\sum_{t=1}^{T}r(T_t^{total}(n),E_t^{total}(n))$. Here $T_t^{total}=T_t^m+T_t^w+T_t^p+T_t^c$ (9), $E_t^{total}=E_t^m+E_t^w+E_t^p+E_t^c$ (10), and POMDP reward is $r_t(n)=-(T_t^{total}(n)+E_t^{total}(n))$ (14). MEMPO maximizes cumulative reward plus entropy (22) with separate delay and energy critics.
- Metrics: migration/transmission/propagation/computation latency, migration/wireless/propagation/computation energy, total delay, total energy (also called migration cost), cumulative/average reward, and inference time.

**Decision variables**

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Target/service MEC server | `$a_t(n)$` / `$a_t^object(n)$` | Discrete categorical, in $\mathcal M=\{1,\ldots,M\}$ | Migration destination selected by user $n$ in slot $t$; the sole physical optimization decision. |
| Causal migration policy | $\pi_\beta(a_t\mid d_t,o_t)$ | Stochastic policy over $\mathcal M$ | Solver representation mapping inferred hidden state $d_t$ and local observation $o_t$ to node choice. |
| Dynamic objective weights | $\delta^t,\eta^t$ | Positive continuous, sum to 1 | MEMPO training weights adapted from delay/energy critic gaps; internal algorithm variables, not system-level migration resources. |

**Constraints**

| ID | Meaning and key expression |
|---|---|
| (11a), action domain | $a_t(n)\in\mathcal M$ for every $t,n$; destination must be an MEC server. |
| (11b), compute capacity | $\sum_{n\in\mathcal N}(c_t(n)+\eta_t(n))\le f_{max}$; task load plus real-time server load cannot exceed maximum processing capacity. The paper does not group this expression by target server. |
| Same-slot completion assumption | Slot $t$'s task completes within slot $t$; stated in prose, not a deadline inequality. |
| Partial-observation boundary | Observation contains local/source ID, wireless rate, and task load/size; nonlocal load is unavailable in real time. This is POMDP information structure, not a feasible-domain constraint. |

**Relation to our scenario**

| Element | Yes / No / Partial | Grounded interpretation |
|---|---|---|
| Battery-triggered UAV replacement | No | Vehicle mobility and QoS trigger migration; no UAV battery state or threshold exists. |
| Stateful running service | Partial | The model migrates “service data” and evolves source/target servers by slot, but defines no checkpoint, memory/socket/runtime-state semantics, source continuation, synchronization, or consistency; $d_t^{migration}$ is only a data volume. |
| Replacement selection | Partial | $a_t(n)$ explicitly selects a target MEC server and can motivate a POMDP candidate policy, but candidates are fixed MEC servers rather than replacement UAVs. |
| Finite standby pool and long-term rotation | No | A finite server set and finite horizon exist, but no standby/active/charging pool, reusable rotation, or cross-cycle energy state is modeled. |
| Source continues during replacement flight | No | No replacement flight or event ordering for source/target parallel service and synchronization is modeled. |
| Mobile A2A state synchronization | No | Service data moves through wired links between fixed MEC servers, not mobile UAV-to-UAV channels. |
| Source-UAV return-energy constraint | No | Energy includes communication and computation only; no flight or return energy is modeled. |

**Full-text evidence**

- Fixed MEC/BS topology and local/source/service servers: [line 34](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Service_Migration_Strategies_Based_on_Partially_Observable_and_Multi-Objective_Optimization/Service_Migration_Strategies_Based_on_Partially_Observable_and_Multi-Objective_Optimization.md:34).
- Slot event order, task triplet, and node-choice variable: [lines 36–38](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Service_Migration_Strategies_Based_on_Partially_Observable_and_Multi-Objective_Optimization/Service_Migration_Strategies_Based_on_Partially_Observable_and_Multi-Objective_Optimization.md:36).
- Task forwarding, service-data migration, same-slot completion, and ignored result return: [line 40](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Service_Migration_Strategies_Based_on_Partially_Observable_and_Multi-Objective_Optimization/Service_Migration_Strategies_Based_on_Partially_Observable_and_Multi-Objective_Optimization.md:40).
- Migration latency/energy and destination-dependent branches: [lines 42–52](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Service_Migration_Strategies_Based_on_Partially_Observable_and_Multi-Objective_Optimization/Service_Migration_Strategies_Based_on_Partially_Observable_and_Multi-Objective_Optimization.md:42).
- Wireless transmission and wired multi-hop propagation model: [lines 54–76](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Service_Migration_Strategies_Based_on_Partially_Observable_and_Multi-Objective_Optimization/Service_Migration_Strategies_Based_on_Partially_Observable_and_Multi-Objective_Optimization.md:54).
- Total delay/energy, objective (11), and constraints: [lines 94–112](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Service_Migration_Strategies_Based_on_Partially_Observable_and_Multi-Objective_Optimization/Service_Migration_Strategies_Based_on_Partially_Observable_and_Multi-Objective_Optimization.md:94).
- POMDP observation/action/reward: [lines 144–160](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Service_Migration_Strategies_Based_on_Partially_Observable_and_Multi-Objective_Optimization/Service_Migration_Strategies_Based_on_Partially_Observable_and_Multi-Objective_Optimization.md:144).
- MEMPO dual critics, entropy, and dynamic weights: [lines 219–270](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Service_Migration_Strategies_Based_on_Partially_Observable_and_Multi-Objective_Optimization/Service_Migration_Strategies_Based_on_Partially_Observable_and_Multi-Objective_Optimization.md:219).
- Trace-driven simulation, empirical rate function, and random parameters: [lines 333–345](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Service_Migration_Strategies_Based_on_Partially_Observable_and_Multi-Objective_Optimization/Service_Migration_Strategies_Based_on_Partially_Observable_and_Multi-Objective_Optimization.md:333).
- Apple M3 edge-terminal simulation environment: [lines 410–425](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Service_Migration_Strategies_Based_on_Partially_Observable_and_Multi-Objective_Optimization/Service_Migration_Strategies_Based_on_Partially_Observable_and_Multi-Objective_Optimization.md:410).

## [21] Service Migration or Task Rerouting: A Two-Timescale Online Resource Optimization for MEC

**Bibliographic verification**

- Authors: You Shi, Changyan Yi, Ran Wang, Qiang Wu, Bing Chen, and Jun Cai.
- Venue: *IEEE Transactions on Wireless Communications*, vol. 23, no. 2, February 2024 (published 5 July 2023).
- Year: 2024.
- DOI: [10.1109/TWC.2023.3290005](https://doi.org/10.1109/TWC.2023.3290005).
- Local artifacts: [PDF](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Service_Migration_or_Task_Rerouting_A_Two-Timescale_Online_Resource_Optimization_for_MEC/Service_Migration_or_Task_Rerouting_A_Two-Timescale_Online_Resource_Optimization_for_MEC.pdf); [Markdown](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Service_Migration_or_Task_Rerouting_A_Two-Timescale_Online_Resource_Optimization_for_MEC/Service_Migration_or_Task_Rerouting_A_Two-Timescale_Online_Resource_Optimization_for_MEC.md).
- The title, six-author list, venue/volume/year, and DOI were checked against the first page of the local PDF.

**Model/evidence status**

- Mathematical model: **complete optimization**. The paper formulates a two-timescale stochastic MINLP (P1/P2) with queues, service migration/task rerouting, caching, energy, and resource constraints, then derives deterministic per-frame/per-slot subproblems.
- Algorithm: **OASTR (two-timescale online optimization for joint Access control, Service migration, Task Rerouting, and Resource management)**, using an improved Lyapunov method, JASTO randomized rounding for large-timescale decisions, and Lagrange-dual/KKT resource allocation at the small timescale.
- Evaluation: **simulation plus theoretical analysis**. Simulations evaluate convergence, queue stability, bandwidth/edge-server-count/service-size sensitivity, and comparisons with JMH/O2TL.
- Paper type: stochastic online optimization with queueing/Lyapunov theory and simulation evaluation.

**Scenario**

- Topology: $M$ geographically distributed fixed edge servers $ESs$, each deployed at a base station, serve $I$ mobile devices $MDs$. MDs hand over between ESs as random mobility changes their access connections.
- Nodes: mobile devices, fixed ESs, application/service copies, and wired ES-to-ES migration links. There are no UAVs, airborne nodes, battery stations, or standby inventory.
- Application: heterogeneous computation-intensive and delay-sensitive MD services, including V2X, immersive XR, online gaming/live video, and human digital-twin health monitoring.
- Assumptions: one ES is selected per MD per large frame; only one ES stores a copy of an MD's required application in each frame; service migration moves the application once at frame start, whereas task rerouting sends each generated task back to the previously hosting ES; access/migration/rerouting use a coarse timescale and offloading/resource allocation use fine slots.
- Multiple access: **not named**. The model allocates bandwidth ratios $\alpha_i(\tau)$ subject to per-ES sum constraints but does not call the mechanism TDMA, FDMA, or OFDMA.
- Channel model: uncorrelated stationary Rayleigh flat fading with distance path loss, $\mathrm{SNR}_{i,m}=p_i|h_{i,m}|^2/(L_{i,m}^{\theta}N_0W_m)$, and $r_{i,m}=x_i^m\alpha_iW_m\log_2(1+\mathrm{SNR}/\alpha_i)$. The ES-to-ES migration rate $r_{m',m}(t)$ is a wired-link parameter assumed invariant within a frame.

**Problem & objective**

- Problem P1: two-timescale joint access selection, service migration versus task rerouting, task offloading, and communication/computing resource allocation under dynamic tasks and channels.
- Type: long-term stochastic mixed-integer nonlinear optimization with queue-stability, caching-capacity, and average-energy constraints.
- Objective formula:
$$
\mathcal F=\frac1T\sum_{t=0}^{T-1}\sum_{i=1}^{I}D_i^{tol}(t),\qquad \mathscr P_1:\min\lim_{T\to\infty}\mathcal F,
$$
  where $D_i^{tol}(t)$ includes local/edge execution, one-time migration delay, or per-slot rerouting delay.
- Metrics: long-term average service delay, average energy consumption, energy-deficit/local-task queue backlogs, convergence versus $V$ and $K$, and comparison against JMH/O2TL.

**Decision variables**

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| ES access selection | $x_i^m(t)$ | Binary, $\{0,1\}$ | MD $i$ accesses ES $m$ in large frame $t$. |
| Service migration mode | $\varpi_i(t)$ | Binary, $\{0,1\}$ | 1 when the required service application migrates from the old ES to the newly accessed ES. |
| Task-rerouting mode | $\vartheta_i(t)$ | Binary, $\{0,1\}$ | 1 when tasks are rerouted from the new ES back to the previously hosting ES; $\varpi_i+\vartheta_i=1$. |
| Mode indicator (auxiliary) | $y_i(t)$ | Binary, $\{0,1\}$ | Equivalent migration/rerouting mode used in JASTO $1 = migration, 0 = rerouting$. |
| Task offloading | $z_i(\tau)$ | Binary, $\{0,1\}$ | 1 for edge offloading and 0 for local execution in fine slot $\tau$. |
| CPU allocation ratio | $\rho_i(\tau)$ | Continuous, $[0,1]$ | Fraction of accessed ES CPU allocated to MD $i$. |
| Bandwidth allocation ratio | $\alpha_i(\tau)$ | Continuous, $(0,1]$ | Fraction of ES bandwidth allocated to MD $i$. |
| Service-placement state (state, not control) | $A_i^m(t)$ | Binary, $\{0,1\}$ | Indicates which ES currently stores MD $i$'s application; recursively determined from prior decisions. |

**Constraints**

| ID | Meaning and key expression |
|---|---|
| (2) | Access/bandwidth sharing: $\sum_mx_i^m(t)\le1$, $\sum_ix_i^m(t)\alpha_i(\tau)\le1$. |
| (6) | Long-term stability of each MD's local task-buffer queue. |
| (20) | ES caching capacity: $C_m^A(t)+C_m^B(t)\le C_m^{max}$, covering migrated and reserved rerouting applications. |
| (22) | Long-term per-MD energy budget: $\lim_{T\to\infty}T^{-1}\sum_te_i^{tol}(t)\le e_i^{th}$. |
| (23) | Per-slot edge CPU allocation: the sum of CPU fractions for migration and rerouting users is at most one. |
| (24) | Binary migration/rerouting modes and exclusivity: $\varpi_i,\vartheta_i\in\{0,1\}$, $\varpi_i+\vartheta_i=1$. |
| (25) | Binary offloading: $z_i(\tau)\in\{0,1\}$. |
| Service-state recursion | $A_i^m(t)$ is updated from previous-frame $(x,\varpi,\vartheta)$, with $\sum_mA_i^m(t)=1$; this is a state-transition constraint rather than a UAV-replacement model. |

**Relation to our scenario**

| Element | Yes / No / Partial | Grounded interpretation |
|---|---|---|
| Battery-triggered UAV replacement | No | The system consists of fixed ESs and mobile devices; no UAV battery or replacement event exists. |
| Stateful running service | No | Services are persistent application copies, but migration is represented by application size $b_i$ and delay $b_i/r_{m',m}$; runtime state, checkpoint, and dirty-state synchronization are not modeled. |
| Replacement selection | No | $x_i^m(t)$ selects a fixed ES access point, not a replacement UAV. |
| Finite standby pool and long-term rotation | No | ES cache capacity is finite, but there is no standby UAV inventory, recharge, or rotation process. |
| Source continues during replacement flight | No | There is no replacement flight; migration occurs over a wired ES-to-ES link and is represented as one-time delay. |
| Mobile A2A state synchronization | No | The inter-ES migration rate is a wired-link parameter; no mobile A2A channel or running-state synchronization is defined. |
| Source-UAV return-energy constraint | No | Energy constraints apply to MD/service execution and migration/rerouting, not UAV propulsion or source return. |

**Full-text evidence**

- Topology and service semantics: [lines 48-57](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Service_Migration_or_Task_Rerouting_A_Two-Timescale_Online_Resource_Optimization_for_MEC/Service_Migration_or_Task_Rerouting_A_Two-Timescale_Online_Resource_Optimization_for_MEC.md:48)–[57](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Service_Migration_or_Task_Rerouting_A_Two-Timescale_Online_Resource_Optimization_for_MEC/Service_Migration_or_Task_Rerouting_A_Two-Timescale_Online_Resource_Optimization_for_MEC.md:57) define fixed ESs, mobile MDs, handover, application migration, and task-rerouting examples.
- Timescales and channel model: [lines 67-85](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Service_Migration_or_Task_Rerouting_A_Two-Timescale_Online_Resource_Optimization_for_MEC/Service_Migration_or_Task_Rerouting_A_Two-Timescale_Online_Resource_Optimization_for_MEC.md:67)–[85](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Service_Migration_or_Task_Rerouting_A_Two-Timescale_Online_Resource_Optimization_for_MEC/Service_Migration_or_Task_Rerouting_A_Two-Timescale_Online_Resource_Optimization_for_MEC.md:85) define coarse/fine frames, bandwidth allocation, Rayleigh fading, path loss, and Shannon rate.
- Computation/offloading variables and queue: [lines 87-117](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Service_Migration_or_Task_Rerouting_A_Two-Timescale_Online_Resource_Optimization_for_MEC/Service_Migration_or_Task_Rerouting_A_Two-Timescale_Online_Resource_Optimization_for_MEC.md:87)–[117](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Service_Migration_or_Task_Rerouting_A_Two-Timescale_Online_Resource_Optimization_for_MEC/Service_Migration_or_Task_Rerouting_A_Two-Timescale_Online_Resource_Optimization_for_MEC.md:117) introduce $z_i,\rho_i,\alpha_i$, local/edge delay and energy, and task-buffer stability.
- Migration/rerouting semantics and migration-size formula: [lines 149-176](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Service_Migration_or_Task_Rerouting_A_Two-Timescale_Online_Resource_Optimization_for_MEC/Service_Migration_or_Task_Rerouting_A_Two-Timescale_Online_Resource_Optimization_for_MEC.md:149)–[176](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Service_Migration_or_Task_Rerouting_A_Two-Timescale_Online_Resource_Optimization_for_MEC/Service_Migration_or_Task_Rerouting_A_Two-Timescale_Online_Resource_Optimization_for_MEC.md:176) define binary $(\varpi,\vartheta)$, state $A_i^m$, one-copy caching, and $D_i^{mig}=b_i/r_{m',m}$.
- Caching, objective, and constraints: [lines 207-258](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Service_Migration_or_Task_Rerouting_A_Two-Timescale_Online_Resource_Optimization_for_MEC/Service_Migration_or_Task_Rerouting_A_Two-Timescale_Online_Resource_Optimization_for_MEC.md:207)–[258](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Service_Migration_or_Task_Rerouting_A_Two-Timescale_Online_Resource_Optimization_for_MEC/Service_Migration_or_Task_Rerouting_A_Two-Timescale_Online_Resource_Optimization_for_MEC.md:258) give cache equations (18)-(20), the average-delay objective (21), and P1 constraints (22)-(25).
- Algorithm identity and hierarchy: [lines 269-303](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Service_Migration_or_Task_Rerouting_A_Two-Timescale_Online_Resource_Optimization_for_MEC/Service_Migration_or_Task_Rerouting_A_Two-Timescale_Online_Resource_Optimization_for_MEC.md:269)–[303](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Service_Migration_or_Task_Rerouting_A_Two-Timescale_Online_Resource_Optimization_for_MEC/Service_Migration_or_Task_Rerouting_A_Two-Timescale_Online_Resource_Optimization_for_MEC.md:303) show OASTR's improved Lyapunov reformulation and JASTO randomized rounding.
- Small-timescale solver and theory: [lines 424-503](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Service_Migration_or_Task_Rerouting_A_Two-Timescale_Online_Resource_Optimization_for_MEC/Service_Migration_or_Task_Rerouting_A_Two-Timescale_Online_Resource_Optimization_for_MEC.md:424)–[503](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Service_Migration_or_Task_Rerouting_A_Two-Timescale_Online_Resource_Optimization_for_MEC/Service_Migration_or_Task_Rerouting_A_Two-Timescale_Online_Resource_Optimization_for_MEC.md:503) specify Lagrange/KKT resource allocation and offloading choice.
- Simulation conclusions: [lines 587-636](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Service_Migration_or_Task_Rerouting_A_Two-Timescale_Online_Resource_Optimization_for_MEC/Service_Migration_or_Task_Rerouting_A_Two-Timescale_Online_Resource_Optimization_for_MEC.md:587)–[636](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Service_Migration_or_Task_Rerouting_A_Two-Timescale_Online_Resource_Optimization_for_MEC/Service_Migration_or_Task_Rerouting_A_Two-Timescale_Online_Resource_Optimization_for_MEC.md:636) report convergence, queue behavior, sensitivity, and comparison with JMH/O2TL.

## [22] Joint Optimization of Trajectory, Offloading, Caching, and Migration for UAV-Assisted MEC

**Bibliographic verification**

- Authors: Mingxiong Zhao, Rongqian Zhang, Zhenli He, and Keqin Li.
- Venue: *IEEE Transactions on Mobile Computing*, vol. 24, no. 3, March 2025, pp. 1981-1998.
- Year: 2025 (received 16 March 2024; revised 30 September 2024; accepted 23 October 2024; published 28 October 2024; current version 5 February 2025).
- DOI: [10.1109/TMC.2024.3486995](https://doi.org/10.1109/TMC.2024.3486995).
- Local artifacts: [PDF](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Optimization_of_Trajectory_Offloading_Caching_and_Migration_for_UAV-Assisted_MEC/Joint_Optimization_of_Trajectory_Offloading_Caching_and_Migration_for_UAV-Assisted_MEC.pdf); [Markdown](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Optimization_of_Trajectory_Offloading_Caching_and_Migration_for_UAV-Assisted_MEC/Joint_Optimization_of_Trajectory_Offloading_Caching_and_Migration_for_UAV-Assisted_MEC.md).
- Bibliographic fields were checked against the first page of the local publisher PDF.

**Model/evidence status**

- Mathematical model: **complete optimization**. Long-term problem P jointly chooses UAV deployment/trajectory, user association, task offloading, compute/migrate/cache scheduling, and A2A migration bandwidth to maximize admitted-task throughput under time, compute, bandwidth, cache-stability, and scheduling-cost constraints.
- Algorithm: **Lyapunov online optimization plus Block Coordinate Descent $BCD$**. The per-slot method combines Task-Scheduling-Oriented UAV Deployment (TSOUD), Distance Probability Rounding Method $DPRM$, task-offloading Algorithm 4, QCQP-to-SDR plus probabilistic mapping for binary scheduling, and bisection/auxiliary-variable/dual updates for migration bandwidth. Algorithm 7 is the complete procedure.
- Evaluation: **simulation**. MATLAB/CVX/YALMIP and PyTorch simulate three UAVs and 100 mobile users in a $500\,\mathrm{m}\times500\,\mathrm{m}$ area for 200 slots; comparisons include K-means++/random deployment and DDPG/A2C/PPO Lyapunov alternatives. No testbed is reported.
- Paper type: stochastic mixed-integer task-scheduling/trajectory optimization and algorithm paper with simulation evaluation.

**Scenario**

- Topology: multiple mobile UAV MEC servers at fixed altitudes cover overlapping regions containing mobile ground users. Users offload newly generated computational tasks to associated UAVs; overloaded UAVs may compute, cache for a later slot, or migrate a task to another mobile UAV over an A2A link.
- Nodes: mobile users and mobile UAVs with onboard compute, cache, and radios. There is no fixed ground MEC server in the modeled scheduling system, replacement UAV role, standby pool, charger, or base-return process.
- Application: generic computational tasks described by input data $e_i(t)$ and required compute $w_i(t)$. A cached task is processed in a later slot; a migrated object is the **task**, not a running service instance, VM/container, or runtime state.
- Assumptions: slotted horizon with unpredictable mobile users; users and UAVs have positions per slot; UAV altitude is constant; each admitted task is associated/offloaded to one covering UAV; each offloaded task chooses exactly one of compute, migrate, or cache; cached work consumes next-slot capacity; task-result download is not modeled; next-slot trajectory/deployment is heuristically informed by prior migration/cache decisions.
- Multiple access: **FDMA** for users; each user has fixed offloading bandwidth $B_i(t)$. Inter-UAV migration shares total A2A bandwidth $B$ through optimized fractions $b_{i,uu'}(t)$.
- Channel model: air-to-ground uses probabilistic LoS/NLoS path loss with elevation-angle-dependent LoS probability and NLoS attenuation; A2A assumes LoS distance/path-loss gain. Both access and A2A rates use Shannon formulas. No dynamic application-state synchronization channel is modeled.

**Problem & objective**

- Problems: long-term **P** (9), Lyapunov per-slot **P'** (17), deployment $(P_q)$, offloading $(P_z)$, scheduling $(P_k)$, and bandwidth $(P_b)$ subproblems.
- Type: long-term stochastic mixed-binary nonlinear optimization with time-average cache/cost constraints; scheduling is NP-hard, transformed into a nonconvex separable QCQP and then an SDR/SDP relaxation.
- Main objective (9a):

  $$
  \max_{Q,S,Z,A,M,O,B}\lim_{\tau\to\infty}\frac1\tau
  \sum_{t\in\mathcal T}\mathbb E\{Y(z_{i,u}(t))\},
  \qquad Y=\sum_u\sum_{i\in\mathcal T_s}z_{i,u}(t).
  $$

- Per-slot Lyapunov objective (17a): minimize $\Gamma+\sum_uG_u(t)C_u(t)+\Omega_u(t)O_u(t)-VY(z_{i,u}(t))$, balancing admitted-task throughput against scheduling cost and cache backlogs.
- Metrics: long-term throughput/admission frequency, scheduling cost (weighted task delay plus scheduling energy), cache/cost queue backlog and stability, task completion, runtime, and sensitivity to UAV placement and Lyapunov $V$.

**Decision variables**

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV deployment/trajectory | $Q=\{q_u(t)\}$ | Continuous 3-D positions (fixed altitude) | UAV position in each slot; the position sequence is the trajectory. |
| User-UAV association | $s_{i,u}(t)$ | Binary | 1 iff user $i$ is associated with/covered by UAV $u$. |
| Task offloading | $z_{i,u}(t)$ | Binary | 1 iff user $i$'s task is admitted/offloaded to UAV $u$. |
| Task computation | $a_{i,u}(t)$ | Binary | 1 iff UAV $u$ computes the task. |
| Task migration | $m_{i,uu'}(t)$ | Binary | 1 iff UAV $u$ sends the task to UAV (u'). |
| Task caching | $o_{i,u}(t)$ | Binary | 1 iff UAV $u$ caches the task for later processing. |
| A2A migration bandwidth | $b_{i,uu'}(t)$ | Continuous proportion | Fraction of total A2A bandwidth assigned to migrating task $i$ from $u$ to (u'). |
| Relaxation/auxiliary variables | $z_{i,u,2},\phi_i,\kappa_i,K_i,\varphi_{i,uu'}$ | Continuous/vector/matrix | Variables used by offloading relaxation, QCQP/SDR, and bandwidth optimization; not new physical actions. |

**Constraints**

| ID | Meaning and key expression |
|---|---|
| (9b)-(9f) | $s,z,a,m,o$ are binary decisions. |
| (9g) | A task is offloaded to at most one UAV: $\sum_uz_{i,u}(t)\le1$. |
| (9h) | Each offloaded task chooses exactly one scheduling action: $\sum_{u'\ne u}m_{i,uu'}+a_{i,u}+o_{i,u}=1$. |
| (9i) | A task can be offloaded only to its associated UAV: $z_{i,u}\le s_{i,u}$. |
| (9j) | Offloading, migration, computation, and transmission time must fit within one slot (cache writing time is treated as negligible/exempt). |
| (9k) | Per-A2A-link bandwidth: $\sum_{i\in\mathcal T_m^u}b_{i,uu'}(t)\le1$. |
| (9l) | UAV compute capacity: $\sum_i a_{i,u}(t)w_{i,u}(t)\le W_u^a(t)$, with prior cached tasks reducing current available capacity. |
| (9m) | Long-term cache queue/space stability. |
| (9n) | Long-term average scheduling cost per UAV cannot exceed $\tilde C$. |
| (10)-(11) | Virtual scheduling-cost queue $G_u$ and actual cache queue $\Omega_u$ dynamics. |
| (43)-(45) | Scheduling QCQP/SDR enforces binary-equivalent, one-action, slot-delay, compute-capacity, PSD, and rank-one conditions before rank relaxation/mapping. |

**Relation to our scenario**

| Element | Yes / No / Partial | Grounded interpretation |
|---|---|---|
| Battery-triggered UAV replacement | No | Scheduling energy covers task migration, computation, and caching, not propulsion battery. Low-battery/mechanical-failure UAV exit is explicitly future work. |
| Stateful running service | No | The migrated/cached object is a newly generated computational task with data and cycle demand. No VM/container, session, runtime memory, checkpoint, dirty state, or consistency mechanism exists. |
| Replacement selection | No | The algorithm selects a destination UAV for a task and future UAV positions, but never selects an incoming UAV to assume another UAV's service role. |
| Finite standby pool and long-term rotation | No | The active UAV set is fixed; no standby inventory, recharge, recovery, availability cycle, or repeated replacement rotation is modeled. |
| Source continues during replacement flight | No | No replacement flight exists. A source UAV may schedule different tasks, but that is not continued service during replacement arrival. |
| Mobile A2A state synchronization | No | Mobile A2A **task transmission** and bandwidth are explicit, but there is no running application state or synchronization process. This is task migration, not state synchronization. |
| Source-UAV return-energy constraint | No | No propulsion, battery reserve, return-to-base, or source-UAV exit constraint is present; low-battery exit is future work. |

**Full-text evidence**

- Scope and explicit focus on computational task caching/migration rather than content/service-state migration: [lines 13-29](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Optimization_of_Trajectory_Offloading_Caching_and_Migration_for_UAV-Assisted_MEC/Joint_Optimization_of_Trajectory_Offloading_Caching_and_Migration_for_UAV-Assisted_MEC.md:13).
- Mobile-UAV/mobile-user topology, task descriptors, and offload/compute/cache/migrate lifecycle: [lines 75-90](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Optimization_of_Trajectory_Offloading_Caching_and_Migration_for_UAV-Assisted_MEC/Joint_Optimization_of_Trajectory_Offloading_Caching_and_Migration_for_UAV-Assisted_MEC.md:75).
- Air-to-ground LoS/NLoS and A2A LoS channel/rate models: [lines 92-104](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Optimization_of_Trajectory_Offloading_Caching_and_Migration_for_UAV-Assisted_MEC/Joint_Optimization_of_Trajectory_Offloading_Caching_and_Migration_for_UAV-Assisted_MEC.md:92).
- Explicit task migration/cache decisions, scheduling delay/energy, and cache/cost budgets: [lines 106-163](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Optimization_of_Trajectory_Offloading_Caching_and_Migration_for_UAV-Assisted_MEC/Joint_Optimization_of_Trajectory_Offloading_Caching_and_Migration_for_UAV-Assisted_MEC.md:106).
- Long-term objective and complete constraints (9a)-(9n): [lines 166-230](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Optimization_of_Trajectory_Offloading_Caching_and_Migration_for_UAV-Assisted_MEC/Joint_Optimization_of_Trajectory_Offloading_Caching_and_Migration_for_UAV-Assisted_MEC.md:166).
- Lyapunov queues and per-slot objective: [lines 238-325](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Optimization_of_Trajectory_Offloading_Caching_and_Migration_for_UAV-Assisted_MEC/Joint_Optimization_of_Trajectory_Offloading_Caching_and_Migration_for_UAV-Assisted_MEC.md:238).
- BCD decomposition and migration/cache-informed UAV deployment: [lines 327-355](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Optimization_of_Trajectory_Offloading_Caching_and_Migration_for_UAV-Assisted_MEC/Joint_Optimization_of_Trajectory_Offloading_Caching_and_Migration_for_UAV-Assisted_MEC.md:327).
- Scheduling QCQP/SDR transformation: [lines 491-507](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Optimization_of_Trajectory_Offloading_Caching_and_Migration_for_UAV-Assisted_MEC/Joint_Optimization_of_Trajectory_Offloading_Caching_and_Migration_for_UAV-Assisted_MEC.md:491).
- Simulation settings and Algorithm 7: [lines 901-917](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Optimization_of_Trajectory_Offloading_Caching_and_Migration_for_UAV-Assisted_MEC/Joint_Optimization_of_Trajectory_Offloading_Caching_and_Migration_for_UAV-Assisted_MEC.md:901) and [lines 938-974](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Optimization_of_Trajectory_Offloading_Caching_and_Migration_for_UAV-Assisted_MEC/Joint_Optimization_of_Trajectory_Offloading_Caching_and_Migration_for_UAV-Assisted_MEC.md:938).
- Low-battery/replacement modeling is explicitly future work: [lines 1012-1016](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Optimization_of_Trajectory_Offloading_Caching_and_Migration_for_UAV-Assisted_MEC/Joint_Optimization_of_Trajectory_Offloading_Caching_and_Migration_for_UAV-Assisted_MEC.md:1012).

## [23] Joint Task Offloading and Migration Optimization in UAV-Enabled Dynamic MEC Networks

**Bibliographic verification**

- Authors: Liang Wang, Bingnan Shen, Lianbo Ma, Yao Zhang, Yingnan Zhao, Hongzhi Guo, Zhiwen Yu, and Bin Guo.
- Venue: *IEEE Transactions on Services Computing*, vol. 18, no. 4, July/August 2025.
- Year: 2025 (received 8 January 2025; accepted 27 May 2025; published 4 June 2025; current version 8 August 2025).
- DOI: [10.1109/TSC.2025.3576644](https://doi.org/10.1109/TSC.2025.3576644).
- Local artifacts: [PDF](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Task_Offloading_and_Migration_Optimization_in_UAV-Enabled_Dynamic_MEC_Networks/Joint_Task_Offloading_and_Migration_Optimization_in_UAV-Enabled_Dynamic_MEC_Networks.pdf); [Markdown](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Task_Offloading_and_Migration_Optimization_in_UAV-Enabled_Dynamic_MEC_Networks/Joint_Task_Offloading_and_Migration_Optimization_in_UAV-Enabled_Dynamic_MEC_Networks.md).
- The title, eight-author list, journal/volume/issue/date, publication history, and DOI were checked visually against the first page of the local IEEE publisher PDF.

**Model/evidence status**

- Mathematical model: **complete optimization**. The paper models slotted task upload, execution, intra-UAV migration, and result download; formulates online CTMiG assignment problem P1 in (17); and maps it to a continuous-time/slot-operated MDP. UAV positions are fixed, while trajectory, propulsion energy, replacement, and return-to-base behavior are outside the formulation.
- Algorithm: **ILCTS (Imitation Learning-based Computation Task Serving)**, a GAIL-style online imitation-learning method. An improved PPO (**IPPO**) policy with hybrid GCN-GMM/MLP networks and a sliding-window trajectory filter first generates expert state-action trajectories; policy/value networks and a discriminator then learn offloading/migration actions adversarially.
- Evaluation: **simulation**. Python/PyTorch experiments use 25–50 UAVs, 1,000 BonnMotion traces plus GeoLife/HMM mobility, and compare ILCTS with IPPO, DDQN, OLSA, GBLM, and SR-CL. No testbed or real UAV deployment is reported.
- Paper type: mathematical optimization plus imitation-learning/RL paper for dynamic computation-task offloading and migration, evaluated by simulation.

**Scenario**

- Topology: a centralized SDN-controlled multi-UAV MEC network with $U$ UAV-mounted MEC servers and continuously moving ground mobile users $MUs$ over a finite slotted horizon. UAVs remain stationary at predefined horizontal positions and fixed altitude; inter-UAV multi-hop paths can relay uploads, migrated task data, and results.
- Nodes: mobile MUs, stationary UAV/MEC servers, and a logical SDN controller with global location, resource, workload, topology, and channel information. No incoming/standby/charging UAV class or depot/base is modeled.
- Application: independently arriving hard- or soft-deadline computation tasks such as high-definition 3D road-map processing. A task is described by input size, computational demand, result size, and delay class. The migration object is one task's remaining unprocessed input plus an assumed fraction of its partial result, not a VM/container/application service.
- Assumptions: Poisson task arrivals; MUs are static within a slot; UAVs are fixed; each task is served by one UAV at a time; FCFS and no preemption; migration finishes within one slot; multiple migrations of a task are allowed; SDN information-collection overhead is ignored.
- Multiple access: WiFi/CSMA-CA is named, but the analytical model idealizes the MAC and omits contention, backoff, retransmission, and detailed interference dynamics. The nearest covered UAV supplies MU association; the controller may redirect a task to another serving UAV.
- Channel model: time-varying quasi-static-per-slot A2G/G2A and A2A links. A2G combines free-space loss with probabilistic LoS/NLoS excess loss; A2A uses free-space LoS path loss. Rate is $B(t)\log_2(1+E_i10^{-PL/10}/(B(t)\sigma^2))$; shortest/condition-aware multi-hop routes are assumed available rather than jointly optimized in P1.

**Problem & objective**

- Problem: **P1 / Eq. (17), CTMiG**. At each decision time the controller assigns each newly arrived task to a serving UAV or keeps/migrates an ongoing task, minimizing realized mean service latency while satisfying one-server, UAV-compute-capacity, and task-deadline requirements.
- Type: online binary combinatorial assignment/control problem, argued NP-hard by analogy to the College Admission Problem, then represented as an MDP.
- Objective:

  $$
  \min_{\{y_{i,j}^{t}\in\mathbf Y^t\}}\frac{1}{M}\sum_{i=1}^{M}\mathcal L_i,
  $$

  where $\mathcal L_i$ is actual end-to-end task latency at the horizon. Its estimate in (14) is upload + computation + cumulative migration + result-download latency.
- Trigger semantics: for hard tasks, estimated end-to-end latency is checked against $dl_i$; for soft tasks, the controller also uses allowed extension $\Delta t_i$ and completion-progress threshold $\varsigma$. This is a deadline/QoS trigger, not a battery trigger.
- MDP objective: maximize discounted cumulative shaped reward; terminal reward is negative average realized latency, intermediate reward is based on $(\chi_i-\hat{\mathcal L}_{i,t})/\chi_i$, and no-action reward is zero.
- Metrics: normalized cumulative training reward, per-slot decision runtime, average task latency, migration frequency, upload/computation/migration/download latency components, hard/soft task latency, and robustness to bandwidth, arrival-rate, and mobility variations.

**Decision variables**

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Task-serving assignment | $y_{i,j}^{t}$ | Binary | UAV $j$ serves MU $i$'s newly offloaded or ongoing task in slot $t$; changing UAV implements migration. |
| Controller action | $a_t^i$ | Discrete, $\{0,1,\ldots,U\}$ | MDP implementation: 0 keeps the current serving UAV; a UAV index selects the offloading/migration target. |

Nearest-UAV association $x_{i,j}^{t}$, routes $Path^t$, task-progress state $ds_i^t$, channel rates, and latency terms are derived/exogenous states or assumed routing outputs, not additional P1 decision variables. UAV position/trajectory, battery replacement, charging, and return flight are not optimized.

**Constraints**

| ID | Meaning and key expression |
|---|---|
| (1) | Hard/soft deadline definition: $\chi_i=dl_i$ for hard tasks and $dl_i+\Delta t_i$ for soft tasks. |
| (2) | Proximity association: each MU connects to exactly one nearest covered UAV in a slot. |
| (3)/(17) | UAV computation capacity: $\sum_i y_{i,j}^{t}\mu_i\leq\varpi_j$. |
| Serving uniqueness in (17) | $y_{i,j}^{t}\in\{0,1\}$ and each task has exactly one serving UAV at a decision time. |
| (8)-(13) | Upload, execution, cumulative migration, and result-download latency definitions over the selected serving UAV and multi-hop paths. |
| (12) | A migration transfers $ds_i^t+\zeta_t res_i$, is assumed to finish within one slot, and adds to prior cumulative migration latency. |
| (14)-(16) | Migration/QoS condition uses estimated end-to-end latency; a soft task may remain when sufficiently complete and within $dl_i+\Delta t_i$. |
| Deadline constraints in (17) | Hard tasks must meet $dl_i$; soft tasks may use the stated $\Delta t_i$ allowance. |

**Relation to our scenario**

| Element | Yes / No / Partial | Grounded interpretation |
|---|---|---|
| Battery-triggered UAV replacement | No | Migration is triggered by predicted deadline violation and execution progress. Residual energy appears only in narrative scheduling guidance; P1 has no battery state, low-energy threshold, departing UAV, or incoming replacement. |
| Stateful running service | Partial | An ongoing **single computation task** can move with remaining input and an assumed partial-result payload, preserving limited task-execution progress. The paper distinguishes this from service-oriented live/stateful migration and models no VM/container, session, service replica, memory dirtying, or consistency semantics. |
| Replacement selection | No | The controller selects a task-serving/migration-target UAV, not a UAV that replaces a depleted serving aircraft. |
| Finite standby pool and long-term rotation | No | The same fixed set of airborne UAV/MEC servers is available over one horizon; no standby inventory, charging turnaround, return/relaunch, or repeated duty rotation is modeled. |
| Source continues during replacement flight | No | There is no replacement flight. The source task server transfers remaining task state at a decision slot, and transfer is assumed to complete within one slot; overlap during an incoming UAV's travel is absent. |
| Mobile A2A state synchronization | Partial | Eq. (12) models multi-hop A2A transfer of remaining task data plus a partial result between **stationary** UAVs. It is one-shot task relocation, not continuous synchronization between moving source/replacement UAVs, and has no dirty-state/consistency model. |
| Source-UAV return-energy constraint | No | No UAV trajectory, propulsion battery, depot, or return-to-base reserve is formulated; energy efficiency is left to future work. |

**Full-text evidence**

- Task migration is distinguished from service-oriented migration and defined around computation execution/delivery: [line 28](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Task_Offloading_and_Migration_Optimization_in_UAV-Enabled_Dynamic_MEC_Networks/Joint_Task_Offloading_and_Migration_Optimization_in_UAV-Enabled_Dynamic_MEC_Networks.md:28).
- Fixed UAVs, mobile MUs, slots, quasi-static channels, and centralized SDN state collection: [line 58](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Task_Offloading_and_Migration_Optimization_in_UAV-Enabled_Dynamic_MEC_Networks/Joint_Task_Offloading_and_Migration_Optimization_in_UAV-Enabled_Dynamic_MEC_Networks.md:58).
- Fixed UAV positions, Poisson task arrivals, task tuple, and hard/soft deadlines: [line 66](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Task_Offloading_and_Migration_Optimization_in_UAV-Enabled_Dynamic_MEC_Networks/Joint_Task_Offloading_and_Migration_Optimization_in_UAV-Enabled_Dynamic_MEC_Networks.md:66).
- FCFS serving, resource/proximity/energy-status narrative, and SDN routing: [line 82](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Task_Offloading_and_Migration_Optimization_in_UAV-Enabled_Dynamic_MEC_Networks/Joint_Task_Offloading_and_Migration_Optimization_in_UAV-Enabled_Dynamic_MEC_Networks.md:82).
- Task-serving variable, one-server semantics, and UAV compute-capacity constraint: [line 84](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Task_Offloading_and_Migration_Optimization_in_UAV-Enabled_Dynamic_MEC_Networks/Joint_Task_Offloading_and_Migration_Optimization_in_UAV-Enabled_Dynamic_MEC_Networks.md:84).
- WiFi/CSMA-CA statement and explicit ideal-MAC limitation: [line 92](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Task_Offloading_and_Migration_Optimization_in_UAV-Enabled_Dynamic_MEC_Networks/Joint_Task_Offloading_and_Migration_Optimization_in_UAV-Enabled_Dynamic_MEC_Networks.md:92).
- A2A free-space path loss and unified A2A/A2G rate formula: [line 108](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Task_Offloading_and_Migration_Optimization_in_UAV-Enabled_Dynamic_MEC_Networks/Joint_Task_Offloading_and_Migration_Optimization_in_UAV-Enabled_Dynamic_MEC_Networks.md:108).
- Exact migrated payload, one-slot assumption, and cumulative migration latency: [line 158](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Task_Offloading_and_Migration_Optimization_in_UAV-Enabled_Dynamic_MEC_Networks/Joint_Task_Offloading_and_Migration_Optimization_in_UAV-Enabled_Dynamic_MEC_Networks.md:158).
- Deadline/progress migration trigger and four-part expected latency: [line 176](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Task_Offloading_and_Migration_Optimization_in_UAV-Enabled_Dynamic_MEC_Networks/Joint_Task_Offloading_and_Migration_Optimization_in_UAV-Enabled_Dynamic_MEC_Networks.md:176).
- P1, mean-latency objective, online nature, and NP-hardness argument: [line 194](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Task_Offloading_and_Migration_Optimization_in_UAV-Enabled_Dynamic_MEC_Networks/Joint_Task_Offloading_and_Migration_Optimization_in_UAV-Enabled_Dynamic_MEC_Networks.md:194).
- MDP state/action/reward and action 0 meaning keep-current-server: [line 223](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Task_Offloading_and_Migration_Optimization_in_UAV-Enabled_Dynamic_MEC_Networks/Joint_Task_Offloading_and_Migration_Optimization_in_UAV-Enabled_Dynamic_MEC_Networks.md:223).
- Simulation environment, mobility traces, baselines, and reported metrics: [line 388](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Task_Offloading_and_Migration_Optimization_in_UAV-Enabled_Dynamic_MEC_Networks/Joint_Task_Offloading_and_Migration_Optimization_in_UAV-Enabled_Dynamic_MEC_Networks.md:388).
- Trajectory and energy-efficiency modeling are explicitly future work: [line 506](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Task_Offloading_and_Migration_Optimization_in_UAV-Enabled_Dynamic_MEC_Networks/Joint_Task_Offloading_and_Migration_Optimization_in_UAV-Enabled_Dynamic_MEC_Networks.md:506).

## [24] Joint Content Caching, Service Placement, and Task Offloading in UAV-Enabled Mobile Edge Computing Networks

**Bibliographic verification**

- Authors: Youhan Zhao, Chenxi Liu, Xiaoling Hu, Jianhua He, Mugen Peng, Derrick Wing Kwan Ng, and Tony Q. S. Quek.
- Venue: *IEEE Journal on Selected Areas in Communications*, vol. 43, no. 1, January 2025.
- Year: 2025 (received 7 March 2024; accepted 5 August 2024; published 13 September 2024; current version 18 December 2024).
- DOI: [10.1109/JSAC.2024.3460049](https://doi.org/10.1109/JSAC.2024.3460049).
- Local artifacts: [PDF](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Content_Caching_Service_Placement_and_Task_Offloading_in_UAV-Enabled_Mobile_Edge_Computing_Networks/Joint_Content_Caching_Service_Placement_and_Task_Offloading_in_UAV-Enabled_Mobile_Edge_Computing_Networks.pdf); [Markdown](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Content_Caching_Service_Placement_and_Task_Offloading_in_UAV-Enabled_Mobile_Edge_Computing_Networks/Joint_Content_Caching_Service_Placement_and_Task_Offloading_in_UAV-Enabled_Mobile_Edge_Computing_Networks.md).
- The title, seven-author list, journal/volume/issue/date, publication history, and DOI were checked visually against the first page of the local IEEE publisher PDF.

**Model/evidence status**

- Mathematical model: **complete optimization**. P1 jointly optimizes binary content caching, static/a-priori service placement, and per-task local/offloaded execution to maximize composite QoE under storage, CPU-core, and computation-energy limits.
- Algorithm: alternating two-subproblem design. **Gibbs sampling** updates each UAV's content/service cache configuration; a **many-to-one matching game**, initialized with the Hungarian algorithm and followed by deferred acceptance and swap matching, determines task offloading. Algorithm 2 iterates both stages to convergence.
- Evaluation: **simulation/numerical experiments**. Results average 1,000 randomized simulations with 13 UAVs and 63 UEs, comparing exhaustive-search upper bound, greedy offloading, non-cooperative, content-first, and service-first schemes. No testbed is reported.
- Paper type: joint caching/service-placement/task-offloading mixed-binary optimization with algorithmic decomposition and numerical simulation.

**Scenario**

- Topology: multiple spatially deployed UAVs serve as aerial BS/MEC nodes for ground UEs in a fixed-area snapshot. A UE fetches requested content from one feasible UAV, while independent tasks in a service request may be split across feasible UAVs or run locally.
- Nodes: UAVs with finite storage, CPU cores/frequency, and computation-energy budgets; ground UEs with local CPUs. No cloud, depot, standby/charging fleet, replacement UAV, or moving serving-UAV process is modeled.
- Application: heterogeneous UE requests. A content request asks for a file. A service request (for example, VR/AR or mobile gaming) requires several independent tasks and a corresponding application plus libraries/databases deployed **a priori** at a selected UAV. This is static asset placement, not migration of a running stateful service.
- Assumptions: request type/content/service demand and binary coverage matrix are known; every content/service has a size; service tasks are independent; a service completes when all tasks complete; downlink result delay is ignored because results are much smaller than inputs; UAV/UE positions and trajectories are not decision variables.
- Multiple access/MAC: each UAV-UE pair receives a distinct uplink/downlink subchannel, eliminating co-channel interference; channel allocation is outside scope.
- Channel model: UE-UAV uplink rate $r_{m,u}=W\log_2(1+\gamma_{m,u})$, with SNR from UE transmit power, distance-dependent path loss $d_{m,u}^{-\eta}$, and thermal noise. No A2A channel, UAV mobility channel, or inter-UAV state-transfer rate is modeled.

**Problem & objective**

- Problem: **P1 / Eq. (16)**, joint content caching, service placement, and task offloading. Cache/placement decisions specify files and application packages resident at each UAV; $y$ assigns each independent task to at most one UAV, with all-zero $y$ meaning local execution.
- Type: coupled non-convex binary combinatorial optimization, described as NP-hard/intractable and decomposed into cache-placement P2 and task-offloading P3.
- Objective:

  $$
  \max_{\mathbf X_{\mathcal F},\mathbf X_{\mathcal K},\mathbf Y}Q=\alpha Pr_h(\mathbf X_{\mathcal F})+(1-\alpha)Pr_s(\mathbf X_{\mathcal F},\mathbf X_{\mathcal K},\mathbf Y),
  $$

  where $Pr_h$ is content-cache hit ratio and $Pr_s=\frac1M\sum_m(1-T_m/T_{m,L})$ is service-delay shrinkage relative to all-local execution.
- Delay model: service completion delay is the maximum completion delay among independent tasks. Each task delay is uplink plus processing delay; downlink delay is explicitly omitted.
- Metrics: average QoE $Q$, cache-hit ratio, service-delay shrinkage, convergence versus Gibbs temperature/iterations, and sensitivity to UAV CPU cores, storage, computation-energy limit, and UE/UAV counts.

**Decision variables**

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Content caching | $x_{u,f}$ | Binary | Content file $f$ is cached at UAV $u$ before service. |
| Service placement | $x_{u,k}$ | Binary | Application/service $k$, including related libraries/databases, is deployed at UAV $u$ a priori. |
| Task offloading | $y_{m,n,u}^{k}$ | Binary | Independent task $n$ of UE $m$'s service-$k$ request is assigned to UAV $u$; all-zero values mean local execution. |

Request indicators, coverage, task sizes/cycles, positions, CPU specifications, and energy limits are exogenous parameters. No migration time, running-state transfer, UAV flight, battery replacement, or return decision appears.

**Constraints**

| ID | Meaning and key expression |
|---|---|
| (1)/(16c) | Per-UAV joint storage: $\sum_fx_{u,f}c_f+\sum_kx_{u,k}c_k\le St_u$. |
| (2)/(16a)-(16b) | Binary request type and at most one content or service request per UE in the snapshot. |
| Request feasibility | Content is served only when $\mu_{m,u}x_{u,f}=1$; an offloaded service task requires coverage and $x_{u,k}=1$. |
| (3)/(16d) | Each independent task is offloaded to at most one UAV; no offload represents local computation. |
| (4)/(16e) | Simultaneous tasks assigned to UAV $u$ cannot exceed $Core_u$. |
| (6)-(12) | Service completion is the maximum task delay; task delay comprises uplink and processing; $Pr_s$ is normalized against local completion time. |
| (13)-(14)/(16f) | Per-UAV **computation** energy: $E_u^{pr}=\kappa_u\sum_{m,n}y_{m,n,u}\zeta_{m,n}^{k}\le E_{max}$; this is not a propulsion/return constraint. |
| (16) | Binary cache/service/offload domains are enforced by feasible configuration and matching sets. |

**Relation to our scenario**

| Element | Yes / No / Partial | Grounded interpretation |
|---|---|---|
| Battery-triggered UAV replacement | No | $E_{max}$ limits CPU energy consumed by assigned tasks. There is no residual flight battery, low-energy trigger, departing source UAV, or incoming replacement. |
| Stateful running service | No | “Service placement” caches an application and libraries/databases **before** task execution. Independent tasks have no running instance, memory/session, checkpoint, dirty pages, or continuity protocol. |
| Replacement selection | No | The algorithm chooses cache/placement configurations and task execution nodes, not a replacement UAV. |
| Finite standby pool and long-term rotation | No | A fixed deployed UAV set is optimized for a static request snapshot; no standby pool, charging recovery, fleet rotation, or multi-cycle horizon appears. |
| Source continues during replacement flight | No | UAV flight and replacement do not exist in the model. Parallel independent-task execution is not source/replacement overlap. |
| Mobile A2A state synchronization | No | Algorithmic collaboration updates placement decisions, but the physical model has no A2A rate and transfers neither running state nor replicas between UAVs. |
| Source-UAV return-energy constraint | No | The only UAV energy constraint is computation energy (13)-(14); there is no propulsion, travel-to-base, or reserved return energy. |

**Full-text evidence**

- Service placement is an application plus libraries/databases placed a priori: [line 15](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Content_Caching_Service_Placement_and_Task_Offloading_in_UAV-Enabled_Mobile_Edge_Computing_Networks/Joint_Content_Caching_Service_Placement_and_Task_Offloading_in_UAV-Enabled_Mobile_Edge_Computing_Networks.md:15).
- Framework with a-priori content/service caching and local-or-offloaded execution: [line 23](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Content_Caching_Service_Placement_and_Task_Offloading_in_UAV-Enabled_Mobile_Edge_Computing_Networks/Joint_Content_Caching_Service_Placement_and_Task_Offloading_in_UAV-Enabled_Mobile_Edge_Computing_Networks.md:23).
- Network roles, heterogeneous requests, multi-UAV task splitting, orthogonal subchannels, and known coverage: [line 39](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Content_Caching_Service_Placement_and_Task_Offloading_in_UAV-Enabled_Mobile_Edge_Computing_Networks/Joint_Content_Caching_Service_Placement_and_Task_Offloading_in_UAV-Enabled_Mobile_Edge_Computing_Networks.md:39).
- Static content/service objects, examples, binary placement, and shared storage constraint: [line 46](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Content_Caching_Service_Placement_and_Task_Offloading_in_UAV-Enabled_Mobile_Edge_Computing_Networks/Joint_Content_Caching_Service_Placement_and_Task_Offloading_in_UAV-Enabled_Mobile_Edge_Computing_Networks.md:46).
- Service request consists of multiple independent tasks: [line 69](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Content_Caching_Service_Placement_and_Task_Offloading_in_UAV-Enabled_Mobile_Edge_Computing_Networks/Joint_Content_Caching_Service_Placement_and_Task_Offloading_in_UAV-Enabled_Mobile_Edge_Computing_Networks.md:69).
- Offloading variable, service/coverage condition, and local execution semantics: [line 71](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Content_Caching_Service_Placement_and_Task_Offloading_in_UAV-Enabled_Mobile_Edge_Computing_Networks/Joint_Content_Caching_Service_Placement_and_Task_Offloading_in_UAV-Enabled_Mobile_Edge_Computing_Networks.md:71).
- Service/task delay decomposition and omitted result-downlink delay: [line 97](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Content_Caching_Service_Placement_and_Task_Offloading_in_UAV-Enabled_Mobile_Edge_Computing_Networks/Joint_Content_Caching_Service_Placement_and_Task_Offloading_in_UAV-Enabled_Mobile_Edge_Computing_Networks.md:97).
- UE-UAV SNR/rate model with distance loss and orthogonal bandwidth: [line 121](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Content_Caching_Service_Placement_and_Task_Offloading_in_UAV-Enabled_Mobile_Edge_Computing_Networks/Joint_Content_Caching_Service_Placement_and_Task_Offloading_in_UAV-Enabled_Mobile_Edge_Computing_Networks.md:121).
- Energy is CPU computation energy, not flight energy: [line 147](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Content_Caching_Service_Placement_and_Task_Offloading_in_UAV-Enabled_Mobile_Edge_Computing_Networks/Joint_Content_Caching_Service_Placement_and_Task_Offloading_in_UAV-Enabled_Mobile_Edge_Computing_Networks.md:147).
- Composite QoE definition and interpretation: [line 161](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Content_Caching_Service_Placement_and_Task_Offloading_in_UAV-Enabled_Mobile_Edge_Computing_Networks/Joint_Content_Caching_Service_Placement_and_Task_Offloading_in_UAV-Enabled_Mobile_Edge_Computing_Networks.md:161).
- P1 objective and storage/CPU/energy constraints: [line 169](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Content_Caching_Service_Placement_and_Task_Offloading_in_UAV-Enabled_Mobile_Edge_Computing_Networks/Joint_Content_Caching_Service_Placement_and_Task_Offloading_in_UAV-Enabled_Mobile_Edge_Computing_Networks.md:169).
- Gibbs sampling and matching-game decomposition: [line 211](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Content_Caching_Service_Placement_and_Task_Offloading_in_UAV-Enabled_Mobile_Edge_Computing_Networks/Joint_Content_Caching_Service_Placement_and_Task_Offloading_in_UAV-Enabled_Mobile_Edge_Computing_Networks.md:211).
- Randomized simulation scale, parameters, and repeated-run count: [line 324](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Content_Caching_Service_Placement_and_Task_Offloading_in_UAV-Enabled_Mobile_Edge_Computing_Networks/Joint_Content_Caching_Service_Placement_and_Task_Offloading_in_UAV-Enabled_Mobile_Edge_Computing_Networks.md:324).

## [25] Serv-HU: Service Hand-off for UAV-as-a-Service

**Bibliographic verification**

- Authors: Arijit Roy, Veera Manikantha Rayudu Tummala, and Vinay Yadam.
- Venue: *IEEE Transactions on Services Computing*, vol. 18, no. 1, January/February 2025.
- Year: 2025 (received 30 October 2023; accepted 14 December 2024; published 24 December 2024; current version 6 February 2025).
- DOI: [10.1109/TSC.2024.3521684](https://doi.org/10.1109/TSC.2024.3521684).
- Local artifacts: [PDF](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Serv-HU_Service_Hand-off_for_UAV-as-a-Service/Serv-HU_Service_Hand-off_for_UAV-as-a-Service.pdf); [Markdown](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Serv-HU_Service_Hand-off_for_UAV-as-a-Service/Serv-HU_Service_Hand-off_for_UAV-as-a-Service.md).
- The title, three-author list, journal/volume/issue/date, publication history, and DOI were checked against the first page of the local IEEE publisher PDF.

**Model/evidence status**

- Mathematical model: **local analysis**. The paper analyzes service-provider eligibility, reviews, coverage, and price; uses KKT for a provider-area selection-factor problem (13)-(18), derives a fallback provider rule (19), itemizes rental/energy/damage/data costs, and uses KKT for a scalar PSP price problem (40)-(46). It does not formulate an end-to-end UAV assignment, flight, radio, state-transfer, or replacement optimization model.
- Algorithm: **Serv-HU** has three procedures: recursive exponential-moving-average review computation; greedy iterative **Optimal SSP Selection** by maximum selection factor $SF_i$ until residual secondary area is covered; and **Optimal Pricing** from the cost model and bound (46). KKT/Lagrangian derivations support area and charged-price subproblems. A failed SSP can be replaced by another eligible SSP using rule (19), but this is provider-level failure fallback, not aircraft replacement.
- Evaluation: **simulation**. A synthetic $10\times10$ area with one PSP, 2–10 SSPs, provider UAV/sensor/cost parameters, and regional coverage partitions compares optimal versus random SSP choice, traditional UaaS versus Serv-HU, and direct versus multi-hop communication. No testbed, UAV experiment, or case-study deployment is reported.
- Paper type: UaaS service-provider responsibility hand-off, provider selection, and economic/pricing analysis with synthetic simulation.

**Scenario**

- Topology: a UAV-as-a-Service platform links one end user, UAV/sensor owners, a Primary Service Provider $PSP$, and candidate Secondary Service Providers $SSPs$. Requested application area $A$ is partitioned into PSP-covered $A_p$ and uncovered secondary area $A_s$; selected SSPs serve $A_s$.
- Nodes/actors: end user, PSP, SSPs, UAV owners, sensor owners, and each provider's heterogeneous sensor-equipped UAV fleet. The end user remains registered with the PSP and is unaware of backend provider collaboration.
- Application: generic IoT/UaaS sensing over a geographic area. “Service hand-off” means contractual/operational responsibility for an **unserved region** moves from PSP to one or more SSPs. It is neither a running MEC application instance nor session/memory state moving between UAVs.
- Assumptions: a provider is eligible if its UAV/sensor set supplies required sensors and can hover over $A_s$; prior reviews are available; providers quote area-based prices; PSP may serve $A_p$ while SSPs serve other portions; costs include UAV/sensor rent, energy, damage, storage, communication, transmission, and upload.
- MAC: no MAC/access-control model, spectrum allocation, contention, or interference equation is given.
- Channel/communication: no propagation, rate, latency, or mobility channel model is formulated. After SSP selection, the paper assumes Internet/cloud coordination or UAV multi-hop relay and names Max-Min Residual Energy AOMDV for routing; simulation compares aggregate communication cost rather than optimizing channel, routing, or state synchronization.

**Problem & objective**

- SSP selection subproblem: Eqs. (13)-(18) maximize provider $i$'s selection factor over serviceable area $A^i$:

  $$
  \arg\max_{A^i}SF_i,\qquad SF_i=e(SP_i)\,\phi(SP_i)\,\frac{S_p^{\max}A^i(1-\log A_{eff}^i)}{C_{in}^{i}},
  $$

  subject to $A^i\le A_{res}^i$ and $\phi(SP_i)\le100$. Algorithm 2 adds maximum-$SF_i$ providers until residual area is covered.
- Failure fallback: Eq. (19) chooses an eligible, well-reviewed, lower-price **service provider** after an SSP fails; it contains no UAV battery or UAV-level replacement decision.
- Pricing subproblem: Eqs. (40)-(46) maximize PSP utility $UF_{PSP}=R_E-\ln(\Gamma(R_E))$ over charged price $C_{in}^{PSP}$, subject to relative cash outflow $R_E=C_{out}^{PSP}/C_{in}^{PSP}\le1$, yielding price/bounds in (45)-(46).
- Type: two local continuous analytical/KKT subproblems embedded in greedy provider selection and cost accounting; not one complete network optimization.
- Metrics: PSP-to-SSP payment, end-user charged price, PSP cash inflow/outflow/service payoff, sensitivity to SSP/UAV/task/end-user counts, and communication cost for multi-hop versus direct transmission.

**Decision variables**

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Provider service area | $A^i$ / $A^{i*}$ | Continuous area, $0\le A^i\le A_{res}^i$ | Portion of residual secondary area assigned to provider $SP_i$ in local selection-factor optimization. |
| Selected SSP set | `SSPs` | Algorithmic subset | Greedily accumulated providers with maximum $SF_i$ until $A_s$ is covered; no explicit binary set-cover formulation. |
| PSP charged price | $C_{in}^{PSP}$ | Positive continuous monetary quantity | Price charged by PSP to the end user, optimized through (40)-(46). |

Eligibility, reviews, provider price, fleet/sensor sets, energy/cost quantities, and communication mode are inputs or derived accounting terms. No individual-UAV selection/dispatch, route, trajectory, battery threshold, replacement time, task/service state, or synchronization variable is defined.

**Constraints**

| ID | Meaning and key expression |
|---|---|
| (2) | Provider eligibility is 1 only when required UAV/sensor capability is contained in provider $i$'s fleet and can serve $A_s$. |
| (3)-(4) | Prior-provider review is an exponential moving average and $\phi(SP_i)$ is the cross-provider average review. |
| (5)-(12) | Effective-area, price, eligibility, and review terms define selectivity and $SF_i$; these are score construction rather than physical continuity constraints. |
| (14a) | Assigned/serviceable area $A^i\le A_{res}^i$. |
| (14b) | Review score $\phi(SP_i)\le100$. |
| Algorithm 2 termination | Providers are added until effective/residual secondary area is covered; individual UAV assignments are not optimized. |
| (19) | Provider-level fallback maximizes $e(SP_i)\phi(SP_i)/C_{in}^i$ after selected-SSP failure. |
| (20)-(38) | Rental, flight/hover/heat energy, damage, data-management, provider-payment, and PSP-payoff accounting definitions, not battery-feasibility/return constraints. |
| (41) | Relative cash outflow $R_E=C_{out}^{PSP}/C_{in}^{PSP}\le1$ in price optimization. |
| (15)-(18), (42)-(46) | Lagrangian/KKT stationarity, dual feasibility, and complementary slackness for area and pricing subproblems. |

**Relation to our scenario**

| Element | Yes / No / Partial | Grounded interpretation |
|---|---|---|
| Battery-triggered UAV replacement | No | UAV energy contributes to maintenance/price accounting and repair/replacement cost is mentioned for damage, but no low-battery trigger or handover from a depleted UAV to an incoming UAV is modeled. |
| Stateful running service | No | The handed-off object is responsibility for an uncovered geographic area. No running software/service instance, session, checkpoint, memory state, or consistency semantics is defined. |
| Replacement selection | No | Serv-HU selects SSP organizations; Eq. (19) replaces a failed **provider** with another provider, never an aircraft replacing a serving UAV. |
| Finite standby pool and long-term rotation | No | Candidate SSP/deployed-UAV counts are finite simulation inputs, but there is no standby/active aircraft state, recharge recovery, or repeated rotation schedule. |
| Source continues during replacement flight | No | PSP may continue serving $A_p$ while SSPs cover $A_s$, but this is simultaneous regional responsibility, not an incoming replacement flight. |
| Mobile A2A state synchronization | No | UAV multi-hop relays sensor/task data and uses residual-energy-aware routing; it does not synchronize running application state and supplies no mobile A2A rate/consistency model. |
| Source-UAV return-energy constraint | No | Flight/hover energy is monetized as cost, but there is no battery-capacity feasibility, reserve threshold, source UAV, depot, or return-to-base energy constraint. |

**Full-text evidence**

- Abstract defines PSP-to-SSP hand-off of uncovered application area and two-stage provider selection/pricing: [line 5](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Serv-HU_Service_Hand-off_for_UAV-as-a-Service/Serv-HU_Service_Hand-off_for_UAV-as-a-Service.md:5).
- UaaS actors and owner-provider rental/business relationships: [line 13](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Serv-HU_Service_Hand-off_for_UAV-as-a-Service/Serv-HU_Service_Hand-off_for_UAV-as-a-Service.md:13).
- PSP and SSP are provider roles defined by requested/unserved application area: [line 15](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Serv-HU_Service_Hand-off_for_UAV-as-a-Service/Serv-HU_Service_Hand-off_for_UAV-as-a-Service.md:15).
- Motivation is collaborative geographic coverage through multiple providers: [line 25](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Serv-HU_Service_Hand-off_for_UAV-as-a-Service/Serv-HU_Service_Hand-off_for_UAV-as-a-Service.md:25).
- Scenario partitions $A$ into PSP-covered $A_p$ and SSP-covered $A_s$, hidden from end user: [line 51](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Serv-HU_Service_Hand-off_for_UAV-as-a-Service/Serv-HU_Service_Hand-off_for_UAV-as-a-Service.md:51).
- Fleet/sensor ownership model and one-PSP-to-many-SSP relationship: [line 58](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Serv-HU_Service_Hand-off_for_UAV-as-a-Service/Serv-HU_Service_Hand-off_for_UAV-as-a-Service.md:58).
- Eligibility depends on provider sensor/UAV capability and ability to hover over secondary area: [line 84](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Serv-HU_Service_Hand-off_for_UAV-as-a-Service/Serv-HU_Service_Hand-off_for_UAV-as-a-Service.md:84).
- Selection-factor objective, area/review constraints, and KKT solution: [line 195](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Serv-HU_Service_Hand-off_for_UAV-as-a-Service/Serv-HU_Service_Hand-off_for_UAV-as-a-Service.md:195).
- Failed-SSP fallback is provider selection followed by Internet or UAV multi-hop data communication: [line 241](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Serv-HU_Service_Hand-off_for_UAV-as-a-Service/Serv-HU_Service_Hand-off_for_UAV-as-a-Service.md:241).
- Residual-energy AOMDV is assumed for multi-hop routing rather than derived as a state-transfer model: [line 257](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Serv-HU_Service_Hand-off_for_UAV-as-a-Service/Serv-HU_Service_Hand-off_for_UAV-as-a-Service.md:257).
- Energy/repair/replacement appear as maintenance-price components: [line 291](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Serv-HU_Service_Hand-off_for_UAV-as-a-Service/Serv-HU_Service_Hand-off_for_UAV-as-a-Service.md:291).
- UAV flight/hover energy is cost accounting without battery feasibility or return-to-base: [line 297](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Serv-HU_Service_Hand-off_for_UAV-as-a-Service/Serv-HU_Service_Hand-off_for_UAV-as-a-Service.md:297).
- PSP price objective and relative-outflow constraint: [line 451](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Serv-HU_Service_Hand-off_for_UAV-as-a-Service/Serv-HU_Service_Hand-off_for_UAV-as-a-Service.md:451).
- Simulation design, synthetic area, PSP/SSP counts, and unit prices: [line 551](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Serv-HU_Service_Hand-off_for_UAV-as-a-Service/Serv-HU_Service_Hand-off_for_UAV-as-a-Service.md:551).
- Multi-hop versus direct transmission evaluation concerns communication cost and sensor-data relay: [line 666](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Serv-HU_Service_Hand-off_for_UAV-as-a-Service/Serv-HU_Service_Hand-off_for_UAV-as-a-Service.md:666).

## [26] Optimizing UAV Resupply Scheduling for Heterogeneous and Persistent Aerial Service

**Bibliographic verification**

- Authors: Edgar Arribas, Vicent Cholvi, and Vincenzo Mancuso.
- Venue: *IEEE Transactions on Robotics*, vol. 39, no. 4, pp. 2639-2653, August 2023.
- Year: 2023 (publication date 19 April 2023 on the PDF first page).
- DOI: [10.1109/TRO.2023.3263077](https://doi.org/10.1109/TRO.2023.3263077).
- Local artifacts: [PDF](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Optimizing_UAV_Resupply_Scheduling_for_Heterogeneous_and_Persistent_Aerial_Service/Optimizing_UAV_Resupply_Scheduling_for_Heterogeneous_and_Persistent_Aerial_Service.pdf); [Markdown](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Optimizing_UAV_Resupply_Scheduling_for_Heterogeneous_and_Persistent_Aerial_Service/Optimizing_UAV_Resupply_Scheduling_for_Heterogeneous_and_Persistent_Aerial_Service.md).
- Title, authors, journal, volume/issue, pages, year, and DOI were checked against the local publisher PDF first page; the last page is 2653.

**Model/evidence status**

- Mathematical model: **complete analytical/combinatorial scheduling, but not slot-level energy optimization**. The UAV persistent service $UPS$ problem gives exact HORR scheduling and minimum fleet-size theorems for homogeneous distances; heterogeneous distances are NP-hard, with lower bounds, HERR sufficient fleet size, and PHERR near-exact heuristic. Energy is abstracted by maximum flight time $f$, round-trip displacement $2g_i$, and resupply time $c$; no battery recursion, propulsion-power, or communication-energy equation is given.
- Algorithm: **HORR / HERR / PHERR**. HORR rotates homogeneous targets at a fixed interval and is exact; HERR uses nonuniform intervals for heterogeneous distances; PHERR partitions target locations into as-homogeneous-as-possible subsets and runs HERR per subset.
- Evaluation: **analytical proofs plus MATLAB numerical simulation**. Each heterogeneity/cost setting uses 1,000 random realizations; SUFF, HERR, PHERR, HORR, and GREEDY are compared by fleet size, extra-energy ratio, and approximation factor to the lower bound.
- Paper type: long-term persistent-service analytical scheduling and combinatorial optimization. Its core objective is minimum fleet size under continuous coverage, not one-time handover downtime or UAV-energy minimization.

**Scenario**

- Topology: one energy supply station $ESS$ at a given location and $N$ fixed aerial target locations; $M\ge N$ homogeneous UAVs shuttle between ESS and targets. Exactly one UAV must serve each target at every instant.
- Nodes: one ESS, active homogeneous UAVs, resupplied/backup UAVs, and aerial target locations. ESS can resupply any number of UAVs simultaneously, so charging positions and queues are not finite.
- Application: service type is deliberately unspecified; only persistent coverage is required. Communication, computing, monitoring, and security are possible examples, not a concrete workload model.
- Assumptions: fixed ESS/target topology; all UAVs have maximum flight time $f$; one-way ESS-to-target displacement time $g_i$ with $2g_i<f$; resupply (battery swap, charging, or refueling) takes $c\ge0$; each UAV serves one location per trip, returns directly to ESS, and re-enters the backup set after resupply.
- Multiple access: **none**. No user access, spectrum allocation, or MAC model is given.
- Channel model: **none**. No path loss, SINR, rate, or communication reliability equation appears; $g_i$ is flight displacement time.

**Problem & objective**

- Problem: the “UAV persistent service problem,” seeking an indefinite coordinated schedule $\{(t_k,u_k,i_k)\}_{k\ge0}$ that keeps every target covered and uses as few UAVs as possible.
- Type: exact periodic scheduling for homogeneous distances and NP-hard combinatorial scheduling/partitioning for heterogeneous distances; PHERR partition search is heuristic, not an unstated MILP/MINLP.
- Objective (compact restatement of the text, not a numbered source equation):

  $$
  \min M\quad\text{subject to continuous target coverage and return-feasible UAV schedules}.
  $$

  Homogeneous optimum (Theorem 2): $M=N+\left\lceil\frac{c+2g}{f-2g}N\right\rceil$. Heterogeneous lower bound (Theorem 4): $M_{LB}=N+\left\lceil\sum_{i=1}^{N}\frac{c+2g_i}{f-2g_i}\right\rceil$.
- Metrics: total fleet $M$, backup count, PHERR approximation factor relative to $M_{LB}$, extra-energy ratio $\sigma/(NT)$, heterogeneity $\Delta$, and average flight cost $\omega=2\bar g/f$. No downtime, task latency, throughput, or computing-energy metric is used.

**Decision variables**

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Indefinite rotation schedule | $\{(t_k,u_k,i_k)\}_{k\ge0}$ | Discrete UAV/target choices plus continuous times | Specifies which UAV departs ESS when to replace the active UAV at target $i_k$; direct output of HORR/HERR. |
| Fleet size | $M$ | Integer, $M\ge N$ | Resource quantity to minimize; closed form in homogeneous case and algorithmically evaluated for heterogeneous case. |
| Homogeneous rotation interval | $x=(f-2g)/N$ | Positive continuous, derived | HORR fixed replacement interval derived from inputs, not an independent search variable. |
| Heterogeneous rotation intervals | $x_{i_j}$ | Positive continuous, derived | HERR nonuniform intervals based on subset distances and farthest target. |
| Target partition | $\mathcal P_N={\mathcal I_1,\ldots}$ | Set partition | PHERR partition of heterogeneous targets; each subset runs HERR. |

$f,c,g_i,N$ are inputs. The paper does not optimize speed, continuous trajectory, power, bandwidth, transfer volume, or service state.

**Constraints**

| ID | Meaning and key expression |
|---|---|
| Persistent coverage | Every $i\in\mathcal N$ has exactly one serving UAV at all times; replacement arrives as the active UAV leaves, with no coverage gap. |
| One UAV per location | Each target has one UAV at a time; initial deployment uses $N$ UAVs. |
| Return feasibility | $2g_i<f$ for all $i\in\mathcal N$, ensuring ESS-to-target-and-back time feasibility, not battery recursion. |
| Resupply turnaround | After leaving a target, UAV returns $g_i$, resupplies for $c$, then flies back; only after resupply does it re-enter backup pool. |
| HORR interval | $x=(f-2g)/N$; an active UAV serves $Nx=f-2g$ before rotation and its replacement departs $g$ early. |
| Backup availability | HORR assumes a fully charged backup at each replacement; Theorems 1-2 derive required backup count rather than tracking inventory state. |
| HERR/PHERR feasibility | HERR dispatches backups $g_{i_j}$ early using heterogeneous intervals; PHERR applies HERR to each partition and chooses minimum total $M$. |

**Relation to our scenario**

| Element | Yes / No / Partial | Grounded interpretation |
|---|---|---|
| Battery-triggered UAV replacement | Partial | Replacement is driven by finite endurance and periodic resupply, but HORR rotates on a preset interval and notes an active UAV need not be near depletion; no event-level energy threshold is used. |
| Stateful running service | No | Service type is unspecified and only location coverage is required; no process, VM/container, checkpoint, session, or application state exists. |
| Replacement selection | Partial | Schedule specifies $u_k$ replacing target $i_k$, but replacement is an already-ready backup and no compute/state compatibility utility is optimized. |
| Finite standby pool and long-term rotation | Partial | Long-term minimum total fleet and backup count are optimized and resupplied UAVs are reused; ESS has unlimited simultaneous resupply with no finite charging queue or inventory recursion. |
| Source continues during replacement flight | Yes (coverage semantics) | Backup departs $g_i$ early; source remains until replacement arrives, preserving target coverage, but no service-state synchronization is involved. |
| Mobile A2A state synchronization | No | No A2A data link, state, synchronization rate, consistency, or catch-up condition is modeled; replacement is positional duty handover. |
| Source-UAV return-energy constraint | Partial | $2g_i<f$ and service interval $f-2g_i$ ensure return feasibility, but no residual-energy state, propulsion integral, or reserve margin is tracked. |

**Full-text evidence**

- Persistent service, minimum fleet size, HORR exactness, and PHERR near-exactness: [lines 1-7](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Optimizing_UAV_Resupply_Scheduling_for_Heterogeneous_and_Persistent_Aerial_Service/Optimizing_UAV_Resupply_Scheduling_for_Heterogeneous_and_Persistent_Aerial_Service.md:1).
- Service type is unspecified and persistence means one UAV covers every location at every instant: [lines 17-19](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Optimizing_UAV_Resupply_Scheduling_for_Heterogeneous_and_Persistent_Aerial_Service/Optimizing_UAV_Resupply_Scheduling_for_Heterogeneous_and_Persistent_Aerial_Service.md:17).
- Routing boundary requiring each UAV to return directly to ESS after service: [lines 21-25](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Optimizing_UAV_Resupply_Scheduling_for_Heterogeneous_and_Persistent_Aerial_Service/Optimizing_UAV_Resupply_Scheduling_for_Heterogeneous_and_Persistent_Aerial_Service.md:21).
- One ESS, $N$ targets, $M\ge N$, resupply time, and $2g_i<f$: [lines 45-58](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Optimizing_UAV_Resupply_Scheduling_for_Heterogeneous_and_Persistent_Aerial_Service/Optimizing_UAV_Resupply_Scheduling_for_Heterogeneous_and_Persistent_Aerial_Service.md:45).
- UPS objective of always covering targets while using minimum UAVs: [line 60](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Optimizing_UAV_Resupply_Scheduling_for_Heterogeneous_and_Persistent_Aerial_Service/Optimizing_UAV_Resupply_Scheduling_for_Heterogeneous_and_Persistent_Aerial_Service.md:60).
- HORR inputs, intervals, early backup departure, and replacement schedule: [lines 68-92](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Optimizing_UAV_Resupply_Scheduling_for_Heterogeneous_and_Persistent_Aerial_Service/Optimizing_UAV_Resupply_Scheduling_for_Heterogeneous_and_Persistent_Aerial_Service.md:68).
- Homogeneous backup and minimum fleet closed forms: [lines 94-106](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Optimizing_UAV_Resupply_Scheduling_for_Heterogeneous_and_Persistent_Aerial_Service/Optimizing_UAV_Resupply_Scheduling_for_Heterogeneous_and_Persistent_Aerial_Service.md:94).
- Heterogeneous NP-hardness and fleet-size lower bound: [lines 204-222](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Optimizing_UAV_Resupply_Scheduling_for_Heterogeneous_and_Persistent_Aerial_Service/Optimizing_UAV_Resupply_Scheduling_for_Heterogeneous_and_Persistent_Aerial_Service.md:204).
- PHERR partition objective and separate HERR runs: [lines 334-386](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Optimizing_UAV_Resupply_Scheduling_for_Heterogeneous_and_Persistent_Aerial_Service/Optimizing_UAV_Resupply_Scheduling_for_Heterogeneous_and_Persistent_Aerial_Service.md:334).
- MATLAB simulation with 1,000 random realizations per setting: [lines 390-402](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Optimizing_UAV_Resupply_Scheduling_for_Heterogeneous_and_Persistent_Aerial_Service/Optimizing_UAV_Resupply_Scheduling_for_Heterogeneous_and_Persistent_Aerial_Service.md:390).

## [27] Seamless Service Handover in UAV-based Mobile Edge Computing

**Bibliographic verification**

- Authors: Zilong Ye, Philip N. Ji, and Ting Wang.
- Venue: *2023 IEEE Global Communications Conference (GLOBECOM 2023)*, pp. 1113-1118.
- Year: 2023.
- DOI: [10.1109/GLOBECOM54140.2023.10437843](https://doi.org/10.1109/GLOBECOM54140.2023.10437843).
- Local artifacts: [PDF](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/sources/Seamless_Service_Handover_in_UAV-Based_Mobile_Edge_Computing/Seamless_Service_Handover_in_UAV-Based_Mobile_Edge_Computing.pdf); [Markdown](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/sources/Seamless_Service_Handover_in_UAV-Based_Mobile_Edge_Computing/Seamless_Service_Handover_in_UAV-Based_Mobile_Edge_Computing.md).
- The title, three authors, GLOBECOM 2023, DOI, and continuous PDF page numbers 1113-1118 were checked from the first page. This conference paper is an early boundary-setting study: it supports the battery-triggered UAV-MEC scenario and system concept, but not a mature stateful-migration mechanism, complete optimization model, or general high-level claim by itself.

**Model/evidence status**

- Mathematical model: **no complete mathematical model or numbered optimization problem**. The paper has no equations for service state, migration data, transfer time, residual energy, downtime, or response time, and no unified decision-vector/constraint set.
- Algorithm: **rule-based UAV dispatch scheme (Algorithm 1)**. It processes low-battery requests in ascending remaining-energy order; selects the nearest reachable retrieval station with a charging spot; prefers dispatch from that same station when a fully charged UAV is available, otherwise from the nearest station with a fully charged UAV; then computes launch time $T$. The pseudocode does not provide a formula for $T$.
- Evaluation: **time-series event-driven simulation**. A 12-hour city simulation compares handover/no-handover average response time, UAV count, average UAV service time, and users served per minute with good service. No testbed or real migration implementation is reported.
- Paper type: UAV-MEC service-handover concept, greedy dispatch heuristic, and simulation conference paper.
- Statefulness audit: “current states of their computing tasks/computations” appears only as a conceptual transfer object, station-reachability check, and result explanation. There is no VM/container/process, memory/socket/session, checkpoint/restore, dirty-state generation, pre-copy/stop-and-copy, consistency, or destination-resume recursion. The evidence supports conceptual task-state handover, not a formal stateful running-service/live-migration model.

**Scenario**

- Topology: multiple UAV stations are distributed across a city; each station stores/charges UAVs. Serving UAV edge servers cover hotspots, while a central controller uses multi-station resource views to dispatch an incoming fully charged UAV and retrieve an outgoing low-battery UAV.
- Nodes: ground users/computing jobs, serving low-battery UAV edge server, incoming fully charged UAV edge server, UAV stations/charging spots, and a controller with battery monitor, station monitor, and dispatch module.
- Application: generic mobile edge computing and data processing for hotspot users; simulation jobs last 9-12 minutes. The paper mentions handover of users, data, computing models, tasks, and their current states, but does not define a concrete stateful runtime.
- Assumptions: a serving UAV detects/reports low energy; replacement departs early and arrives before source return; controller knows UAV locations/remaining energy, station coordinates, fully charged UAV counts, and available charging spots; retrieval station remains reachable after accounting for handover time; station resources are maintained by heartbeat/proactive updates.
- Multiple access: **no analytical MAC/resource-allocation model**. WiFi/LTE are examples of commercial wireless connections between UAVs, controller, and stations.
- Channel model: **none**. “Available network bandwidth” is an exogenous transfer-time check; there is no path loss, SINR, rate, or bandwidth-allocation equation.

**Problem & objective**

- Problem: no problem ID or compact optimization expression. The system-level goal is minimum downtime/average response time, while the dispatch algorithm is designed to maximize UAV service time.
- Type: greedy procedural heuristic for prioritized requests and multi-station dispatch/retrieval, not mathematical optimization over an explicit feasible set.
- Objective formula: **none**. The text must not be converted into a weighted sum or an unstated integer program.
- Metrics: average service response time; service-downtime spike width; UAV count over 12 hours; average service time per UAV; users per minute with response time below 60 ms. Table I reports no-handover/handover values of 24/28 UAVs, 98.3/102 service-time units, and 180.5/197.6 users served.

**Decision variables**

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Dispatch station | $D$ (pseudocode label) | Categorical over stations | Station launching the fully charged UAV; retrieval station is preferred, otherwise nearest station with an available full-charge UAV. |
| Retrieval station | $H$ (pseudocode label) | Categorical over stations | Station receiving the low-battery UAV after handover; must have a charging spot, be reachable, and be nearest among candidates. |
| Launch time | $T$ | Continuous time, formula not given | Incoming UAV dispatch time, described as a function of source remaining energy and dispatch-station/source distance. |
| Low-battery request order | No unified symbol | Permutation induced by remaining battery | Ascending remaining-energy order processes the most urgent UAV first. |

Replacement-UAV identity is not a decision variable; the algorithm only checks whether the selected dispatch station has a fully charged UAV. Handover strategy, state representation, bandwidth allocation, and charging schedule are also not decision variables.

**Constraints**

| ID | Meaning and key expression |
|---|---|
| Low-battery priority | Multiple requests are sorted by ascending remaining battery. |
| Retrieval reachability | Low-battery UAV must still reach candidate station after accounting for handover transfer time; transfer time depends on data/model/current-task-state and available bandwidth, but no formula is given. |
| Charging-spot availability | Retrieval station must have enough available charging spots. |
| Retrieval proximity | Among reachable candidates with charging spots, choose the station nearest to the low-battery UAV. |
| Fully charged availability | Dispatch station must have a fully charged UAV; prefer the retrieval station, otherwise nearest station with one. |
| Plan-ahead overlap | Incoming UAV departs early and arrives before source returns, reserving duty/data/task/current-state handover time. |
| Launch timing | $T$ is computed, but neither pseudocode nor text gives an explicit equality, deadline, or feasible domain. |

**Relation to our scenario**

| Element | Yes / No / Partial | Grounded interpretation |
|---|---|---|
| Battery-triggered UAV replacement | Yes | A low-battery request from the serving UAV triggers controller dispatch; a fully charged UAV arrives to take over, after which the source returns for charging. |
| Stateful running service | Partial (conceptual only) | The paper says current states of computing tasks are transferred and contrasts this with reboot/recompute, but provides no runtime/container/checkpoint/restore, dirty-state, or consistency model. |
| Replacement selection | Partial | Controller selects a dispatch station with a fully charged UAV; it does not select a specific replacement UAV or optimize compute/state compatibility or candidate utility. |
| Finite standby pool and long-term rotation | Partial | Station monitor tracks finite fully charged UAVs and charging spots; simulation uses 20 UAVs and 20 spots per station, but omits charging time, inventory transitions, queues, cross-event rotation, and long-term fleet optimization. |
| Source continues during replacement flight | Partial | Incoming UAV flies ahead while source remains in the hotspot until arrival and handover, but request processing, cutover, and downtime during overlap are not formalized. |
| Mobile A2A state synchronization | Partial (conceptual) | WiFi/LTE may carry current-computation-state transfer using available bandwidth; no A2A channel/rate, state generation, iterative synchronization, catch-up, or consistency condition is defined. |
| Source-UAV return-energy constraint | Partial | Retrieval station must remain reachable after accounting for source battery and handover time, but there is no remaining-energy/return-cost equation or explicit reserve. |

**Full-text evidence**

- Low-battery UAV to fully charged UAV job shift, minimum downtime, dispatch goal, and event-driven simulation: [lines 1-9](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/sources/Seamless_Service_Handover_in_UAV-Based_Mobile_Edge_Computing/Seamless_Service_Handover_in_UAV-Based_Mobile_Edge_Computing.md:1).
- Low-battery source return and new full-charge UAV taking over users/tasks: [lines 18-20](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/sources/Seamless_Service_Handover_in_UAV-Based_Mobile_Edge_Computing/Seamless_Service_Handover_in_UAV-Based_Mobile_Edge_Computing.md:18).
- Handover scope is users/computing tasks rather than fixed-edge migration: [lines 24-28](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/sources/Seamless_Service_Handover_in_UAV-Based_Mobile_Edge_Computing/Seamless_Service_Handover_in_UAV-Based_Mobile_Edge_Computing.md:24).
- Open decisions and downtime/response-time text objective: [lines 34-36](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/sources/Seamless_Service_Handover_in_UAV-Based_Mobile_Edge_Computing/Seamless_Service_Handover_in_UAV-Based_Mobile_Edge_Computing.md:34).
- Reboot baseline and plan-ahead handover, including the only “current states of computing tasks” wording: [lines 41-43](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/sources/Seamless_Service_Handover_in_UAV-Based_Mobile_Edge_Computing/Seamless_Service_Handover_in_UAV-Based_Mobile_Edge_Computing.md:41).
- Multi-station/edge-UAV/controller architecture and WiFi/LTE examples: [lines 45-49](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/sources/Seamless_Service_Handover_in_UAV-Based_Mobile_Edge_Computing/Seamless_Service_Handover_in_UAV-Based_Mobile_Edge_Computing.md:45).
- Station monitor tracks fully charged UAVs and available charging spots: [lines 51-55](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/sources/Seamless_Service_Handover_in_UAV-Based_Mobile_Edge_Computing/Seamless_Service_Handover_in_UAV-Based_Mobile_Edge_Computing.md:51).
- Dispatch service-time objective, state-transfer-aware reachability, and charging-spot gate: [lines 62-68](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/sources/Seamless_Service_Handover_in_UAV-Based_Mobile_Edge_Computing/Seamless_Service_Handover_in_UAV-Based_Mobile_Edge_Computing.md:62).
- Dispatch/retrieval station, launch-time rules, and complete pseudocode: [lines 70-97](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/sources/Seamless_Service_Handover_in_UAV-Based_Mobile_Edge_Computing/Seamless_Service_Handover_in_UAV-Based_Mobile_Edge_Computing.md:70).
- Four stations, 20 UAVs/20 spots per station, job/response-time settings, and 12-hour simulation: [lines 99-101](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/sources/Seamless_Service_Handover_in_UAV-Based_Mobile_Edge_Computing/Seamless_Service_Handover_in_UAV-Based_Mobile_Edge_Computing.md:99).
- Downtime-UAV-count tradeoff and Table I metrics: [lines 106-114](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/sources/Seamless_Service_Handover_in_UAV-Based_Mobile_Edge_Computing/Seamless_Service_Handover_in_UAV-Based_Mobile_Edge_Computing.md:106).

## [28] Cost Optimization of UAV Swarm Network for Persistent Emergency Communication

**Bibliographic verification**

- Authors: Changtong Liu, Xin Xin, Yueyue Dai, and Du Xu.
- Venue: *IEEE Transactions on Green Communications and Networking*, vol. 10, pp. 1734-1748, 2026 (the PDF first page does not print an issue number).
- Year: 2026 issue; PDF first page shows publication date 29 December 2025.
- DOI: [10.1109/TGCN.2025.3649278](https://doi.org/10.1109/TGCN.2025.3649278).
- Local artifacts: [PDF](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/sources/Cost_Optimization_of_UAV_Swarm_Network_for_Persistent_Emergency_Communication/Cost_Optimization_of_UAV_Swarm_Network_for_Persistent_Emergency_Communication.pdf); [Markdown](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/sources/Cost_Optimization_of_UAV_Swarm_Network_for_Persistent_Emergency_Communication/Cost_Optimization_of_UAV_Swarm_Network_for_Persistent_Emergency_Communication.md).
- Title, four authors, journal/volume/year/start page, and DOI were checked against the local publisher PDF first page; the last page is 1748.

**Model/evidence status**

- Mathematical model: **complete joint optimization**. In continuous time, the paper jointly optimizes UAV-target association $\mathbf A$, trajectories $\mathbf Q$, and tree topology $\mathbf U$ to minimize fleet size $|\mathcal M|$, subject to persistent coverage, tree connectivity, and return-energy constraints. It is a strongly coupled, continuous-time, combinatorial MINLP with energy-trajectory coupling.
- Algorithm: **USP-NFRP**, comprising periodic rotation path $PRP$, dynamic tree backhaul link $DTBL$, and max-min ant system rotation path planning (MMAS-PP). PRP forms cyclic paths through access/fixed-relay/non-fixed-relay task points; DTBL switches relay roles and reconstructs backhaul while relays move; MMAS-PP searches paths and task order.
- Evaluation: **simulation**. A $20\,\mathrm{km}\times20\,\mathrm{km}$ area with seven access points and a remote station is compared with GA-VRP, TLB-DRM, and PHRR on required UAV count and spanning-tree connectivity. No testbed is reported.
- Paper type: persistent emergency-communication network-topology, path-planning, and fleet-size optimization.
- Service-semantics boundary: a “task” is a ground-access or multi-hop-relay task, and “replacement” is a UAV taking over an access/relay point on a periodic path. The paper preserves communication coverage and relay connectivity; it has no MEC workload, running service state, checkpoint, or state migration.

**Scenario**

- Topology: after a disaster in mountainous/rural areas, $K$ distant population clusters are far from one ground base station. $M$ homogeneous UAVs at fixed altitude form a multi-hop tree backhaul from target areas to a remote station; base and charging station are co-located.
- Nodes: population clusters/target areas, access UAVs, fixed and non-fixed relay UAVs, and base/charging station. UAV task points include access and relay points.
- Application: persistent emergency communication when terrestrial infrastructure fails; UAVs act as aerial base stations/relays and forward isolated-area traffic to the remote station over multiple hops. No MEC computation/service is modeled.
- Assumptions: homogeneous fixed-wing UAVs, fixed altitude, constant speed $V$, small-circle constant-speed flight as the hover abstraction; active state consumes constant $P_c+P_f$; battery swap at the station is instantaneous and restores $E_{max}$; one UAV serves each target and each UAV serves at most one target; stable bidirectional relay links exist within distance $D$; periodic paths return to station and exhaust energy under the stated abstraction.
- Multiple access: **none**. No ground-user scheduling, spectrum partition, interference, or MAC equation is given.
- Channel model: **distance-threshold connectivity graph only**, without physical-layer channel or rate model. $z_{p,q}(t)=1$ when node distance is at most maximum relay distance $D$; no path loss, SINR, capacity, or traffic-flow constraint appears.

**Problem & objective**

- Problem (10): joint fleet-size, association, trajectory, and tree-topology optimization.
- Type: continuous-time mixed-binary/continuous MINLP with combinatorial tree/VRP structure; tree topology and energy-trajectory coupling make global solution difficult.
- Original objective:

  $$
  \min_{\mathbf A,\mathbf Q,\mathbf U}|\mathcal M|\tag{10}
  $$

  subject to Eqs. (11)-(20).
- PRP fleet relation and reformulation: $M_r=\left\lceil\mathcal T_r/\Delta t_r\right\rceil$, $|\mathcal M|=\sum_{r\in R}M_r$, and $\mathcal T_r=T_{max}=E_{max}/(P_c+P_f)$. Eq. (24) minimizes the sum of scheduling-interval reciprocals; Eq. (26) maximizes each $\Delta t_r$ subject to path-period decomposition, minimum replacement interval, and non-fixed-relay waiting constraints. These equations are not state-migration objectives.
- Metrics: required fleet size, relative UAV reduction, fleet size under different $D$ and $T_{max}$, path/task schedules, and UAV-to-station spanning-tree continuity. The paper reports up to 30.9% and average 21.6% reduction versus baselines.

**Decision variables**

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV-target association | $\mathbf A=\{\alpha_{k,m}(t)\}$ | Binary | Whether UAV $m$ serves target area $k$ at time $t$. |
| UAV trajectories/positions | $\mathbf Q=\{L_m(t)\}$ | Continuous 2-D trajectories at fixed altitude | Positions, paths, and access/relay role handovers over time. |
| Tree topology selection | $\mathbf U=\{\mu_{p,q}(t)\}$ | Binary | Whether available link ($p,q$) is selected in the backhaul tree. |
| Link existence | $z_{p,q}(t)$ | Binary, induced by distance | Stable bidirectional link exists when distance is at most $D$; geometric auxiliary variable, not an independent physical-layer decision. |
| Rotation-path configuration | $R$, path/task ordering | Discrete routes and relay roles | PRP/MMAS-PP cyclic paths and execution order through access/relay points. |
| Scheduling interval | $\Delta t_r$ | Continuous, $\Delta t_r\ge T_{interval}$ | Departure/role-handover interval for adjacent UAVs on a path; maximized in Eq. (26). |
| Non-fixed waiting time | $t_r^{nonfix}$ | Nonnegative continuous | Waiting needed by non-fixed relay to keep distance to adjacent UAV within $D$. |

Active/charging state $S_m(t)$, energy $E_m(t)$, and fleet count $M_r$ are derived from positions, paths, and time. No application-state, migration-data, or synchronization control variable is introduced.

**Constraints**

| ID | Meaning and key expression |
|---|---|
| (11) | Each UAV serves at most one target: $\sum_k\alpha_{k,m}(t)\le1$. |
| (12) | Each target has exactly one serving UAV: $\sum_m\alpha_{k,m}(t)=1$. |
| (13) | Only geometric links that exist can enter the tree: $\mu_{p,q}(t)\le z_{p,q}(t)$. |
| (14)-(15) | Tree always includes station and connects every target-serving UAV to station backhaul. |
| (16) | Current tree-node set $\mathcal T'(t)$ has enough edges to maintain connectivity. |
| (17) | For all subsets $S\subseteq\mathcal T'(t)$, the stated edge bound ensures acyclicity; no unstated reformulation is made. |
| (18) | Return energy: $E_m(t)\ge\frac{\|L_m(t)-B\|}{V}(P_c+P_f)$. |
| (19)-(20) | $\alpha_{k,m}(t),\mu_{p,q}(t),z_{p,q}(t)\in\{0,1\}$. |
| (26) | Path-period decomposition, $\Delta t_r\ge T_{interval}$, $t_r^{nonfix}\ge0$, and $t_r^{nonfix}\ge\Delta t_r-D/V$. |
| DTBL feasibility | If relay movement would disconnect another task point, the relay must retain stable backhaul or an alternate relay; otherwise that point is fixed rather than non-fixed. Algorithms 1-2 check this condition. |

**Relation to our scenario**

| Element | Yes / No / Partial | Grounded interpretation |
|---|---|---|
| Battery-triggered UAV replacement | No (periodic endurance driven) | UAVs rotate at fixed PRP intervals and return after each path; no low-battery request/threshold triggers a source-replacement event. |
| Stateful running service | No | Persistent objects are ground access and multi-hop relay connectivity; no MEC process, VM/container, user-session state, checkpoint, or restore exists. |
| Replacement selection | Partial | Path/order/association decide which UAV takes the next access/relay role, but no standby candidate is selected by battery, compute, or synchronization compatibility. |
| Finite standby pool and long-term rotation | Partial | Total fleet $|\mathcal M|$ is optimized and periodic return paths repeat; station energy recovery is instantaneous and there is no finite charging position, queue, or distributed inventory. |
| Source continues during replacement flight | Partial (communication role) | Synchronized forward shifting preserves relay/coverage and spanning-tree continuity while a successor approaches, but this is communication-task continuity, not a running service continuing during replacement flight. |
| Mobile A2A state synchronization | No | UAV-UAV links carry multi-hop backhaul connectivity only; no service-state data, synchronization rate, dirty state, catch-up, or cutover condition is defined. |
| Source-UAV return-energy constraint | Yes (generic UAV) | Eq. (18) requires active UAV residual energy to suffice for return to station at constant speed, but is not coupled to state-transfer completion or a source-return reserve. |

**Full-text evidence**

- Persistent multi-hop connectivity, fleet-size objective, PRP/DTBL/MMAS-PP, and up to 30.9% reduction: [lines 1-7](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/sources/Cost_Optimization_of_UAV_Swarm_Network_for_Persistent_Emergency_Communication/Cost_Optimization_of_UAV_Swarm_Network_for_Persistent_Emergency_Communication.md:1).
- Disaster-area context, remote base station, and multi-hop emergency communication: [lines 55-61](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/sources/Cost_Optimization_of_UAV_Swarm_Network_for_Persistent_Emergency_Communication/Cost_Optimization_of_UAV_Swarm_Network_for_Persistent_Emergency_Communication.md:55).
- Fixed altitude/station, association definition, and persistent one-to-one target coverage: [lines 61-78](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/sources/Cost_Optimization_of_UAV_Swarm_Network_for_Persistent_Emergency_Communication/Cost_Optimization_of_UAV_Swarm_Network_for_Persistent_Emergency_Communication.md:61).
- Distance-threshold link existence and tree-to-station semantics: [lines 81-87](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/sources/Cost_Optimization_of_UAV_Swarm_Network_for_Persistent_Emergency_Communication/Cost_Optimization_of_UAV_Swarm_Network_for_Persistent_Emergency_Communication.md:81).
- Active/charging states, instantaneous resupply, and constant-power fixed-wing abstraction: [lines 103-120](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/sources/Cost_Optimization_of_UAV_Swarm_Network_for_Persistent_Emergency_Communication/Cost_Optimization_of_UAV_Swarm_Network_for_Persistent_Emergency_Communication.md:103).
- Explicit return-energy constraint (9): [lines 123-126](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/sources/Cost_Optimization_of_UAV_Swarm_Network_for_Persistent_Emergency_Communication/Cost_Optimization_of_UAV_Swarm_Network_for_Persistent_Emergency_Communication.md:123).
- Original association/trajectory/topology decisions, objective (10), and constraints (11)-(20): [lines 129-184](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/sources/Cost_Optimization_of_UAV_Swarm_Network_for_Persistent_Emergency_Communication/Cost_Optimization_of_UAV_Swarm_Network_for_Persistent_Emergency_Communication.md:129).
- Continuous-time coupled MINLP classification and USP-NFRP modules: [lines 188-192](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/sources/Cost_Optimization_of_UAV_Swarm_Network_for_Persistent_Emergency_Communication/Cost_Optimization_of_UAV_Swarm_Network_for_Persistent_Emergency_Communication.md:188).
- PRP access/relay points, cyclic role handover, and forward-shift connectivity: [lines 194-202](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/sources/Cost_Optimization_of_UAV_Swarm_Network_for_Persistent_Emergency_Communication/Cost_Optimization_of_UAV_Swarm_Network_for_Persistent_Emergency_Communication.md:194).
- Path period, fleet count, constant-power endurance, and Eq. (24) reformulation: [lines 207-228](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/sources/Cost_Optimization_of_UAV_Swarm_Network_for_Persistent_Emergency_Communication/Cost_Optimization_of_UAV_Swarm_Network_for_Persistent_Emergency_Communication.md:207).
- Fixed/non-fixed task hovering and scheduling-interval LP (26): [lines 231-243](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/sources/Cost_Optimization_of_UAV_Swarm_Network_for_Persistent_Emergency_Communication/Cost_Optimization_of_UAV_Swarm_Network_for_Persistent_Emergency_Communication.md:231).
- DTBL relay-role/backhaul adjustment without running-state migration: [lines 343-357](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/sources/Cost_Optimization_of_UAV_Swarm_Network_for_Persistent_Emergency_Communication/Cost_Optimization_of_UAV_Swarm_Network_for_Persistent_Emergency_Communication.md:343).
- Simulation settings, baselines, fairness, and fleet-size reductions: [lines 507-532](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/sources/Cost_Optimization_of_UAV_Swarm_Network_for_Persistent_Emergency_Communication/Cost_Optimization_of_UAV_Swarm_Network_for_Persistent_Emergency_Communication.md:507).
- Periodic path access coverage and spanning-tree continuity: [lines 539-547](C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/sources/Cost_Optimization_of_UAV_Swarm_Network_for_Persistent_Emergency_Communication/Cost_Optimization_of_UAV_Swarm_Network_for_Persistent_Emergency_Communication.md:539).
