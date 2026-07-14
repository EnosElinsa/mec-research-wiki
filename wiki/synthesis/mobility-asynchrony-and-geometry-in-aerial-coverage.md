---
type: synthesis
title: "Mobility, asynchrony, and geometry in aerial coverage"
tags: [synthesis, aerial-networking, coverage, mobility, asynchrony, geometry]
related:
  - "[[hong-2026-beam-delay-alignment]]"
  - "[[fang-2026-cellfree-uav-predictive-beamforming]]"
  - "[[chen-2026-traffic-aware-asynchronous-control]]"
  - "[[shi-2026-vhetnet-comp-coverage]]"
  - "[[ren-2026-distributed-uav-los]]"
  - "[[wang-2026-6dara-cellfree]]"
  - "[[jiang-2026-ray-antenna-array]]"
  - "[[chai-2026-random-position-relay-deployment]]"
  - "[[beam-delay-alignment-transmission]]"
  - "[[wideband-asynchronous-cell-free-massive-mimo]]"
  - "[[cell-free-uav-predictive-beamforming]]"
  - "[[traffic-aware-asynchronous-uav-control]]"
  - "[[coordinated-multipoint-transmission]]"
  - "[[poisson-delaunay-comp-clustering]]"
  - "[[same-tier-three-site-comp]]"
  - "[[two-regime-aerial-user-association]]"
  - "[[air-to-ground-channel-model]]"
  - "[[blockage-aware-channel-model]]"
  - "[[six-dimensional-aerial-rotatable-antenna-array]]"
  - "[[team-mmse-receive-combining]]"
  - "[[ray-antenna-array]]"
  - "[[statistical-user-position-uav-deployment]]"
  - "[[collaborative-beamforming-in-aerial-mec]]"
  - "[[isac-sensing-in-aerial-mec]]"
created: 2026-07-14
updated: 2026-07-14
---

# Mobility, asynchrony, and geometry in aerial coverage

## Scope: what coverage means across these sources

“Coverage” is not one interchangeable outcome in this source set. It ranges from reliable radio access for a moving UAV to spatially uniform sensing of a UAV swarm, and each paper evaluates a different link direction, service role, and metric.

| Source | Direction and aerial role | What is being made available | Primary reported criterion |
|---|---|---|---|
| [[hong-2026-beam-delay-alignment]] | Distributed ground APs transmit to UAV users | A wideband cell-free downlink despite propagation and multipath delay mismatch | Max-min received quality and spectral-efficiency distributions |
| [[fang-2026-cellfree-uav-predictive-beamforming]] | Distributed ground APs transmit to high-mobility UAV users | Beam alignment across a frame with only first-slot pilots | Effective sum spectral efficiency after training overhead |
| [[chen-2026-traffic-aware-asynchronous-control]] | UAV relays carry directional flows between ground devices | Collection, inter-UAV handoff, and delivery of heterogeneous traffic | Minimum delivered-flow throughput |
| [[shi-2026-vhetnet-comp-coverage]] | Terrestrial and UAV-mounted base stations transmit to aerial users | SIR-threshold service from same-tier three-site clusters | Coverage probability |
| [[ren-2026-distributed-uav-los]] | Distributed ground base stations serve UAVs | Urban mmWave access under height-, distance-, and deployment-dependent LoS | Outage probability, ergodic capacity, and throughput |
| [[wang-2026-6dara-cellfree]] | Mobile ground users transmit to UAV-mounted access points | Cell-free uplink reception under moving users and reconfigurable aerial arrays | Sum rate and Jain’s fairness index |
| [[jiang-2026-ray-antenna-array]] | A UAV-swarm ISAC transmitter/target scene is observed by an ISAC receiver | Directionally uniform angle discrimination plus communication | Angular resolution, estimation error/missed targets, and communication rate |
| [[chai-2026-random-position-relay-deployment]] | Ground users send through aerial relays to a satellite | Two-hop delivery under statistical user positions and a first-hop eavesdropper | Expected/summed transmission time |

The table is a taxonomy, not a leaderboard. Coverage probability, outage, spectral efficiency, sum rate, delivered-flow throughput, transmission time, and angular coverage have different denominators and physical events. Likewise, ground-AP-to-UAV downlink, aerial-AP-to-ground uplink, aerial relay service, and UAV-swarm ISAC cannot be ranked by placing their reported numbers side by side.

## Mobility and state prediction

[[cell-free-uav-predictive-beamforming]] treats mobility as a channel-acquisition problem. In [[fang-2026-cellfree-uav-predictive-beamforming]], ground APs estimate delay, Doppler, azimuth, and elevation from the first slot’s pilots, update local kinematic states with EKFs, fuse state and covariance information at the CPU, and reconstruct LoS channels for later predictive zero-forcing beams. The predicted uncertainty also controls pilot length, AP association, and downlink power. Mobility therefore changes both the beam direction and the amount of training considered worthwhile.

[[wang-2026-6dara-cellfree]] uses a different moving object and control surface. Ground users move continuously while UAV-mounted access points change [[six-dimensional-aerial-rotatable-antenna-array|3-D position and 3-D array orientation]] at frame scale; [[team-mmse-receive-combining]] adapts at slot scale. This is physical infrastructure reconfiguration for an uplink, not extrapolation of a UAV user’s downlink channel.

[[traffic-aware-asynchronous-uav-control]] also moves aircraft, but its state is dominated by traffic buffers, cluster relationships, relay opportunities, and service-stage durations. It does not predict the radio channel in Fang’s sense. Conversely, [[statistical-user-position-uav-deployment]] plans from a user-position density before exact locations are available, while the association routine in [[chai-2026-random-position-relay-deployment]] later consumes realized coordinates. These are three distinct uncertainty treatments: frame-ahead state prediction, traffic-conditioned control, and distribution-level placement.

Cross-source inference: a complete mobile coverage controller would need an explicit handoff among those uncertainty representations. None of the eight papers supplies that integrated controller, and static altitude/association analyses in [[shi-2026-vhetnet-comp-coverage]] and [[ren-2026-distributed-uav-los]] should not be described as mobility solutions.

## Two distinct forms of asynchrony

[[hong-2026-beam-delay-alignment]] uses **waveform/path asynchrony**. Signals from geographically separated ground APs and different propagation paths arrive with unequal delays; when residual delay exceeds the cyclic prefix, the model includes phase rotation, inter-carrier interference, and inter-symbol interference. [[beam-delay-alignment-transmission]] compensates a selected path by the gap between that path’s delay and the user’s maximum path delay, while a delay-compatible path set excludes combinations that cannot share the residual-delay tolerance.

[[chen-2026-traffic-aware-asynchronous-control]] uses **scheduling asynchrony**. Every UAV independently divides a common slot among flight, uplink collection, inter-UAV relay, and downlink delivery. Different UAVs can therefore occupy different service stages within the same slot according to their local traffic conditions.

The two meanings are not substitutes. Scheduling UAVs independently does not align multipath arrivals, and adding true-time-delay hardware does not decide how long a relay should collect or forward traffic. Fang’s prediction frame and Wang’s two-timescale controller introduce still other temporal decompositions: they specify how frequently state, geometry, or combining is refreshed, but neither is the same mechanism as Chen’s per-UAV mode allocation or Hong’s symbol/path alignment.

## Deployment, channel, association, and CoMP geometry

The geometry-oriented sources expose four different decisions that are often compressed into “coverage optimization”:

1. **Deployment prior.** [[chai-2026-random-position-relay-deployment]] integrates its relay-placement objective over a truncated-Gaussian user density and places fixed-altitude relays on a horizontal grid. Exact user coordinates reappear in the subsequent shortest-time association and load-repair procedure, so statistical planning and online assignment remain separate.
2. **Channel law.** [[ren-2026-distributed-uav-los]] combines a finite [[matern-hard-core-bs-deployment|Matérn hard-core]] ground-BS process with a piecewise 3GPP UAV LoS model. Its [[air-to-ground-channel-model]] conditions serving distance, outage, and capacity on height, horizontal distance, and urban deployment type. This is a statistical member of the broader [[blockage-aware-channel-model]] family rather than a building-by-building geometric map.
3. **Tier and cluster association.** [[shi-2026-vhetnet-comp-coverage]] constructs [[poisson-delaunay-comp-clustering|Delaunay]] three-site candidates separately in aerial and terrestrial tiers. [[two-regime-aerial-user-association]] then compares long-term aggregate power from the two candidate clusters. The low-altitude regime is shaped by terrestrial blockage/LoS improvement; closer to the aerial tier, geometric proximity favors aerial sites. The reported boundary and U-shaped behavior are conditional on the evaluated model.
4. **Cooperation scope.** [[same-tier-three-site-comp]] fixes each serving group to three ABSs or three TBSs. [[coordinated-multipoint-transmission]] then aggregates their desired signal while nonserving sites remain interferers. Mixed-tier serving triads are excluded after one simulated setup finds them uncommon; this is a modeling restriction, not a general law.

Cross-source inference: these decisions form a useful reasoning order—choose what spatial information is available, choose a propagation model, form candidate sites, associate the user, then coordinate the selected sites—but the papers do not implement a single sequential pipeline. Chai’s relay-to-satellite delay objective, Shi’s SIR coverage objective, and Ren’s ground-BS outage/capacity analysis remain non-comparable.

## Antenna and array geometry

[[six-dimensional-aerial-rotatable-antenna-array]] changes where an aerial access point is and how its rigid planar array is oriented. Translation changes distance and service geometry; rotation changes local arrival angles and steering. In [[wang-2026-6dara-cellfree]], those mechanical variables and user association are held over a frame, while [[team-mmse-receive-combining]] uses local instantaneous CSI plus cross-node statistics for slot-level uplink reception. The team-optimality statement is conditioned on fixed association and geometry.

[[ray-antenna-array]] changes the internal layout of an ISAC receiver. Radially oriented simple linear subarrays directly combine their elements, a switch network selects a small number of ray outputs, and the full-coverage construction gives direction-independent first-null resolution under the paper’s element-pattern assumptions. [[jiang-2026-ray-antenna-array]] then estimates angle, delay, and Doppler for a UAV swarm. This is array-topology geometry, not UAV deployment or CoMP cluster geometry, and the published result is one-dimensional; adjacent-ray blockage and full 3-D coverage remain open.

Hong’s delay network is a third hardware axis. It corrects frequency-dependent beam split and path timing at ground transmitters, whereas Wang rotates an aerial receive array and Jiang selects fixed radial subarrays. The shared word “beam” does not make these architectures interchangeable.

## Cross-source design map

The following direct relationships are accepted because each pair answers a specific interface or boundary question. Rows marked “cross-source inference” are editorial connections grounded in both parses; they are not claims that either paper implemented the combined design.

| ID | Direct pair | Why the direct relationship is useful | Boundary that must remain explicit |
|---:|---|---|---|
| 1 | [[coordinated-multipoint-transmission]] ↔ [[poisson-delaunay-comp-clustering]] | Delaunay triangles instantiate the three-site coordination set used by Shi’s CoMP analysis. | The tractability and point-process assumptions belong to that model, not to CoMP generally. |
| 2 | [[coordinated-multipoint-transmission]] ↔ [[two-regime-aerial-user-association]] | Association chooses which tier’s three-site CoMP candidate supplies the serving signal. | The altitude pattern is scenario-dependent and does not establish a universal handover height. |
| 3 | [[poisson-delaunay-comp-clustering]] ↔ [[two-regime-aerial-user-association]] | Per-tier Delaunay candidates provide the aggregate-power objects compared by the association rule. | Candidate construction and tier selection are separate decisions. |
| 4 | [[same-tier-three-site-comp]] ↔ [[two-regime-aerial-user-association]] | The association probability is defined over all-ABS versus all-TBS triads. | Mixed-tier serving triads are omitted by assumption. |
| 5 | [[beam-delay-alignment-transmission]] ↔ [[cell-free-uav-predictive-beamforming]] | Cross-source inference: one protects a ground-AP/UAV downlink against path-delay mismatch; the other predicts motion-driven channel state and reduces repeated training. | Neither paper jointly tracks moving multipath delays and aligns them. |
| 6 | [[wideband-asynchronous-cell-free-massive-mimo]] ↔ [[six-dimensional-aerial-rotatable-antenna-array]] | Cross-source inference: they expose timing hardware versus mechanical geometry as different adaptation surfaces in cell-free systems. | Hong is ground-AP-to-UAV downlink; Wang is ground-user-to-aerial-AP uplink. |
| 7 | [[wideband-asynchronous-cell-free-massive-mimo]] ↔ [[team-mmse-receive-combining]] | Cross-source inference: both distribute physical-layer work under limited information, but one configures transmit beams/delays and the other computes receive combiners. | Team-MMSE does not resolve excess path delay, and BDAT does not provide Wang’s uplink decoder. |
| 8 | [[cell-free-uav-predictive-beamforming]] ↔ [[six-dimensional-aerial-rotatable-antenna-array]] | Cross-source inference: prediction adapts beams to a moving UAV user, while 6D control adapts aerial infrastructure to moving ground users. | User motion and access-point motion occur on opposite sides of the link. |
| 9 | [[cell-free-uav-predictive-beamforming]] ↔ [[team-mmse-receive-combining]] | Cross-source inference: both are fast cell-free physical-layer blocks using distributed observations and statistical coordination. | Fang uses predictive downlink zero forcing; Wang uses uplink team-MMSE under a different information structure. |
| 10 | [[hong-2026-beam-delay-alignment]] ↔ [[wang-2026-6dara-cellfree]] | Cross-source inference: source-level comparison separates ground-transmitter delay control from aerial-receiver position/orientation control. | Their directions, objectives, channel models, and metrics differ. |
| 11 | [[fang-2026-cellfree-uav-predictive-beamforming]] ↔ [[wang-2026-6dara-cellfree]] | Cross-source inference: both split slow configuration from faster radio adaptation in dynamic cell-free networks. | Fang predicts UAV state for a downlink; Wang moves/rotates aerial APs for an uplink. |
| 12 | [[wang-2026-6dara-cellfree]] ↔ [[wideband-asynchronous-cell-free-massive-mimo]] | Cross-source inference: Wang supplies the aerial-AP geometry counterpart to Hong’s ground-AP timing architecture. | A role reversal is required before their mechanisms could share a system model. |
| 13 | [[fang-2026-cellfree-uav-predictive-beamforming]] ↔ [[beam-delay-alignment-transmission]] | Cross-source inference: Fang’s state prediction addresses where the dominant path will point; BDAT addresses when selected paths arrive. | Fang’s multipath extension tracks only deterministic LoS and does not perform BDAT. |
| 14 | [[hong-2026-beam-delay-alignment]] ↔ [[team-mmse-receive-combining]] | Cross-source inference: the pair contrasts distributed transmit-side delay/beam construction with distributed receive-side interference combining. | Fixed-geometry team optimality cannot be transferred to Hong’s path-selection problem. |
| 15 | [[shi-2026-vhetnet-comp-coverage]] ↔ [[hong-2026-beam-delay-alignment]] | Cross-source inference: both study cooperative aerial-user coverage, with bounded three-site CoMP versus user-centric wideband cell-free transmission. | Shi reports SIR coverage probability; Hong reports received-quality/SE behavior under path asynchrony. |
| 16 | [[shi-2026-vhetnet-comp-coverage]] ↔ [[fang-2026-cellfree-uav-predictive-beamforming]] | Cross-source inference: static altitude/tier association and dynamic state-predictive AP association are two different coverage-control layers. | Shi uses aerial snapshots and coherent same-tier triads; Fang uses moving UAVs and noncoherent AP downlink. |
| 17 | [[coordinated-multipoint-transmission]] ↔ [[wideband-asynchronous-cell-free-massive-mimo]] | Cross-source inference: both coordinate geographically separated sites, making synchronization and cooperation scope explicit design variables. | Shi assumes coherent same-tier CoMP; Hong models and compensates propagation/multipath delay. |
| 18 | [[same-tier-three-site-comp]] ↔ [[wideband-asynchronous-cell-free-massive-mimo]] | Cross-source inference: the pair contrasts a fixed three-site same-tier cluster with user-centric distributed AP/path selection. | Site-tier restriction and path-delay compatibility are different selection criteria. |
| 19 | [[statistical-user-position-uav-deployment]] ↔ [[two-regime-aerial-user-association]] | Cross-source inference: density-level placement and altitude-dependent tier choice are complementary planning and association stages. | Chai fixes relay altitude and minimizes transmission time; Shi studies aerial-user SIR coverage across altitude. |
| 20 | [[chai-2026-random-position-relay-deployment]] ↔ [[shi-2026-vhetnet-comp-coverage]] | Cross-source inference: both connect spatial user information to aerial placement and association, but expose different information assumptions. | Relay-satellite delay under a user density cannot be compared numerically with CoMP coverage probability at sample locations. |
| 21 | [[statistical-user-position-uav-deployment]] ↔ [[cell-free-uav-predictive-beamforming]] | Cross-source inference: the pair separates pre-deployment location uncertainty from frame-level kinematic state uncertainty. | A population density is not a UAV state estimate; neither source converts one representation into the other. |

## Non-comparability and evidence limits

- **Link direction and platform role:** Hong and Fang use ground APs to serve UAV users; Ren uses ground BSs to serve UAVs; Shi combines aerial and terrestrial BS tiers for aerial users; Wang uses UAVs as receive APs for ground users; Chen and Chai use UAVs as relays; Jiang studies a UAV-swarm ISAC scene.
- **Temporal semantics:** Chen’s independent service-stage durations, Hong’s propagation/multipath delay, Fang’s prediction frame, and Wang’s frame/slot split are four different timing constructs.
- **Geometry semantics:** Chai and Shi place infrastructure, Ren models serving distance and LoS, Shi forms CoMP triangles, Wang moves and rotates an aerial array, and Jiang changes the array topology itself.
- **Metrics:** Shi’s coverage probability, Ren’s outage/capacity, Hong and Fang’s spectral-efficiency quantities, Wang’s sum rate/fairness, Chen’s delivered-flow throughput, Chai’s transmission time, and Jiang’s angular/sensing measures are not normalized to a common event.
- **Evidence scope:** all eight evaluations are analytical and/or simulation based. The source set does not provide a joint flight/radio prototype, common channel trace, common traffic model, or shared evaluation protocol.

Direct links in the design map indicate a specific conceptual interface or contrast. They do not imply metric superiority, plug-compatible algorithms, or a combined theorem.

## Design implications and open gaps

1. **Declare the aerial role before selecting a method.** A predictive downlink beam for a UAV user cannot be moved unchanged into an aerial-AP uplink or relay-to-satellite system.
2. **Keep a timing contract between layers.** Path-delay alignment, pilot refresh, mechanical reconfiguration, receive combining, and relay-mode scheduling need separate clocks and state variables.
3. **Make uncertainty conversion explicit.** Statistical user density, kinematic covariance, traffic history, LoS probability, and instantaneous/local CSI are not interchangeable inputs. An integrated design needs a documented estimator or aggregation step between them.
4. **Separate candidate formation from service optimization.** Delaunay triads, delay-compatible path cliques, AP association, and relay load repair select different objects for different reasons. A common “clustering” label hides those constraints.
5. **Test metric translation rather than assume it.** Better angular resolution need not improve network coverage probability; lower outage need not maximize ergodic capacity; higher sum rate need not minimize end-to-end relay time.
6. **Close the hardware loop.** Hong leaves delay/angle acquisition and calibration open, Wang lacks gimbal/flight actuation validation, and Jiang lacks a fabricated RAA and full 3-D blockage study. A useful next experiment would co-measure motion, synchronization, array orientation, and end-to-end service quality on one aerial platform.
7. **Unify static geometry with mobility cautiously.** Shi and Ren provide interpretable altitude/association/channel structure, while Fang, Chen, and Wang provide dynamic controllers. Combining them requires checking whether the static stochastic assumptions remain valid over the controller’s update horizon.
