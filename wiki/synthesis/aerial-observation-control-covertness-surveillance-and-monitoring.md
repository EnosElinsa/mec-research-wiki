---
type: synthesis
title: "Aerial observation control: covertness, surveillance, and monitoring"
tags: [synthesis, covertness, surveillance, monitoring, isac, physical-layer-security]
related:
  - "[[wang-2026-covert-cognitive-radio]]"
  - "[[lin-2026-fc-ris-surveillance]]"
  - "[[guo-2024-multiuav-proactive-eavesdropping]]"
  - "[[zhan-2026-star-ris-aerial-monitoring]]"
  - "[[wang-2026-fd-covert-isac]]"
  - "[[deng-2025-covert-isac-trajectory]]"
  - "[[zhang-2026-irs-uav-covert-fbl]]"
  - "[[primary-signal-assisted-covertness]]"
  - "[[sensing-signal-assisted-covertness]]"
  - "[[wireless-information-surveillance]]"
  - "[[monitoring-success-probability]]"
  - "[[proactive-eavesdropping]]"
  - "[[full-duplex-receiver-jamming]]"
  - "[[isac-sensing-in-aerial-mec]]"
created: 2026-07-14
updated: 2026-07-14
---

# Aerial observation control: covertness, surveillance, and monitoring

The word *monitoring* hides several incompatible control problems. A covert transmitter wants an unauthorized observer to miss the existence of a communication. An authorized wireless monitor wants to decode a suspicious link. A camera UAV wants to remain close enough to physical targets and deliver the captured video. An ISAC base station wants to associate echo-derived observations with trajectories. These tasks can share UAV motion, beamforming, interference, and surface control without sharing an observer, an outcome, or a metric.

## Observer, observed party, and controller

| Source | Observer | Observed party or object | Controller | Desired observation outcome |
|---|---|---|---|---|
| [[wang-2026-covert-cognitive-radio]] | Multiple wardens using received-power tests | Whether the relaying UAV superposes a secondary covert signal | UAV relay power and horizontal trajectory | Wardens should remain uncertain while the primary and secondary receivers are served. |
| [[lin-2026-fc-ris-surveillance]] | Passive legitimate monitoring station | Suspicious source-to-destination information | Receive-antenna rule, [[fully-connected-ris]], and long-term aerial surface placement | The authorized monitor should decode the suspicious signal. |
| [[guo-2024-multiuav-proactive-eavesdropping]] | Cooperative monitoring UAVs and their central console | Multiple mobile suspicious UAV links | Monitoring-UAV jamming powers and trajectories | The authorized party should decode more links by degrading suspicious destinations and improving monitoring channels. |
| [[zhan-2026-star-ris-aerial-monitoring]] | Camera-equipped monitoring UAV, with indoor and outdoor users consuming its video | Moving physical targets and the resulting VR stream | UAV trajectory, active beamforming, and [[star-ris]] coefficients | Targets should remain within the modeled observation distance while captured content is delivered with high long-term throughput. |
| [[wang-2026-fd-covert-isac]] | Willie observes communication activity; the base station senses a separate aerial target | Alice-to-Bob covert activity and target echo | Base-station sensing/communication beams, Bob's trajectory, and randomized receiver jamming | Willie should be confused while Bob is served and the echo-SINR constraint is met. |
| [[deng-2025-covert-isac-trajectory]] | Multiple passive wardens; the UAV also illuminates sensing targets | Presence of the UAV's information stream beside its sensing waveform | UAV trajectory and communication/sensing covariance matrices | Information activity should be hidden while target-directed sensing gain is preserved. |
| [[zhang-2026-irs-uav-covert-fbl]] | Willie | Whether the UAV transmits a finite-blocklength packet to Bob | UAV trajectory and active/passive IRS beamforming | Willie should have high detection error while Bob's finite-blocklength covert rate is maximized. |
| [[yan-2026-uav-trajectory-monitoring]] | One three-array ISAC base station and its data-center pipeline | Non-cooperative UAV motion states and track identities | Sensing-cycle beam management, estimation, association, and filtering | New targets should be discovered and existing trajectories associated, estimated, and predicted for the next cycle. |
| [[huang-2026-intelligent-jamming-maritime]] | Eve attempts to decode Alice; the legitimate controller observes or predicts Eve | Alice's maritime data and Eve's time-varying position | Alice/Bob trajectories and powers under a POMDP policy | Eve's rate should be suppressed while secrecy and propulsion-energy objectives are balanced. |

Authorization and intent therefore belong in the system model, not in the radio label. A *warden*, *legitimate monitor*, *camera platform*, and *ISAC tracker* are not interchangeable observers.

## Role inversion: hiding, intercepting, and monitoring

The covertness papers treat received-power observation as the threat. [[wang-2026-covert-cognitive-radio]] places a useful primary waveform under both hypotheses; [[deng-2025-covert-isac-trajectory]] and [[wang-2026-fd-covert-isac]] place a sensing waveform under both hypotheses; [[zhang-2026-irs-uav-covert-fbl]] shapes active and passive beams so Willie has difficulty distinguishing transmission from silence. Their controller tries to reduce the information that reaches an unauthorized activity detector.

[[wireless-information-surveillance]] reverses that goal. In [[lin-2026-fc-ris-surveillance]], the authorized observer passively improves its cascaded reception path. In [[guo-2024-multiuav-proactive-eavesdropping]], [[proactive-eavesdropping]] intentionally reduces suspicious-destination capacity with cognitive jamming so the central monitor can decode. A jamming waveform can therefore hide a legitimate transmission from a warden or help an authorized monitor intercept a suspicious link; its meaning follows the observer roles and decoding inequality.

Physical and kinematic monitoring form two more roles. [[zhan-2026-star-ris-aerial-monitoring]] uses panoramic cameras and a distance constraint to keep moving targets in an observation region before broadcasting video. [[yan-2026-uav-trajectory-monitoring]] instead converts radio echoes into position/velocity observations, track identities, and next-cycle predictions. Neither task asks whether a wireless payload is covert or decodable by a suspicious-link monitor.

## Covertness mechanisms

- [[primary-signal-assisted-covertness]] reuses relayed primary data as beneficial interference. The signal still satisfies a [[cooperative-cognitive-radio]] service obligation, so it is not a dedicated jammer.
- [[sensing-signal-assisted-covertness]] makes a legitimate sensing waveform the power baseline under both warden hypotheses. In the two ISAC designs, beamforming and UAV geometry jointly set the information-to-sensing power ratio.
- [[full-duplex-receiver-jamming]] lets Bob receive the covert payload while emitting randomized artificial noise. This adds a controllable mask but also residual self-interference and interference to the sensing function.
- [[zhang-2026-irs-uav-covert-fbl]] uses an IRS plus active beamforming and trajectory control under a [[finite-blocklength-urllc|finite-blocklength]] detector model. More channel uses help coding until the additional Willie observations tighten covertness.
- [[ambient-interference-aided-covertness]] relies on an environmental interference distribution rather than a cooperating controller. It is a useful boundary case: density and power are stochastic context, not a beam or trajectory selected by the covert pair.

All of these mechanisms remain detector- and model-scoped. A KL/Pinsker sufficient condition, an optimal threshold under a specified likelihood model, and an infinite-sample radiometer result do not establish detector-independent invisibility.

## Surveillance mechanisms

The passive design in [[lin-2026-fc-ris-surveillance]] first applies [[threshold-based-antenna-selection]] or another one-antenna rule using the FC-RIS-to-monitor sub-link, then configures the ideal symmetric-unitary surface once for the selected antenna. Its long-timescale placement uses statistical or large-scale channel information. The desired event is summarized by [[monitoring-success-probability]]: the monitor's rate exceeds the suspicious destination's rate.

The proactive design in [[guo-2024-multiuav-proactive-eavesdropping]] uses monitoring UAVs to receive suspicious information and send jamming simultaneously. Per-state jamming power is solved outside the learned motion policy; decentralized trajectories improve monitoring channels over a long-run average-reward horizon. The intervention is successful only if the resulting joint-decoding rate supports authorized interception. Its jamming is distinct from [[cooperative-jamming]] that protects a friendly link against an eavesdropper.

## Aerial monitoring as stochastic service control

In [[zhan-2026-star-ris-aerial-monitoring]], the observation sensor is a panoramic camera. Target motion changes a geometric-center constraint, the UAV path, propagation, and propulsion energy. A virtual queue turns the long-term energy budget into per-slot pressure, while active beamforming and STAR-RIS transmission/reflection coefficients deliver the already processed monitoring video to users on both sides of the surface.

The optimization objective is long-term average communication throughput, not a target-state error. Remaining within the prescribed distance is a proxy for physical observation coverage; the parse does not report recognition accuracy, missed-target probability, or trajectory RMSE. This keeps the result separate from radio surveillance and from the estimation/association metrics in ISAC tracking.

## Metrics and detector assumptions

| Task | Main metric or constraint | Observer model | Evidence boundary |
|---|---|---|---|
| Covert cooperative CR | Average finite-blocklength effective throughput subject to per-warden detection-error/KL constraints | Neyman-Pearson likelihood test on finite received-power samples under stated Gaussian/Rayleigh channels | Conservative Pinsker/KL sufficiency and numerical evaluation; no alternate-detector result. |
| Passive wireless surveillance | [[monitoring-success-probability]] and monitoring rate | Authorized receiver succeeds when its achievable rate exceeds the suspicious destination's rate | Nakagami/order-statistic model, exponential approximation, and ideal FC-RIS assumptions. |
| Proactive surveillance | Eavesdropping rate and eavesdropping success rate | Authorized UAV/console joint decoder; suspicious destination is deliberately jammed | MDP/SCA/MAPPO analysis and Monte Carlo simulation, not a detection-error metric. |
| STAR-RIS physical monitoring | Long-term sum throughput, target-center distance, and average propulsion energy | Panoramic camera capture is assumed; users receive the processed stream | Synthetic target motion and communication simulation; no perception-quality metric. |
| Full-duplex covert ISAC | Covert rate, Willie MDEP, echo SINR, and Bob outage | Infinite-channel-use radiometer with uniform jamming power and bounded Willie-location uncertainty | Model-specific threshold/MDEP and simulation; finite-sample and alternate-detector behavior are open. |
| Sensing-signal covert ISAC | Average covert rate, equal-prior wardens' detection error, and sensing beam gain | Received-power binary test under known locations and LoS channels | Local SDR/SCA solution and simulation. |
| IRS finite-blocklength covertness | Finite-blocklength covert rate and KL/DEP constraint | Willie observes the same finite set of channel uses used by Bob's codeword | Pinsker/KL sufficiency and numerical comparison; no global optimizer or field detector. |
| ISAC trajectory monitoring | Parameter/position/velocity RMSE, association outcome, and complete simulated tracks | Echo processing, [[phase-rotated-dft-motion-parameter-estimation]], [[position-gated-velocity-nearest-neighbor-association]], and IMM-UKF | Simulation evidence for selected SNR, motion, and crossing cases; no universal association guarantee. |
| Maritime intelligent jamming | Total secrecy rate and Alice/Bob propulsion energy; predicted Eve position is a controller input | Eve decodes a protected link, while an LSTM supplies observed or predicted Eve position | Simulation under a memory-based Gauss-Markov Eve; the supplied parse omits the cited prediction-error appendix. |

## Mobility, horizon, and control surfaces

The horizon determines what the controller can claim. [[wang-2026-covert-cognitive-radio]], [[deng-2025-covert-isac-trajectory]], [[wang-2026-fd-covert-isac]], and [[zhang-2026-irs-uav-covert-fbl]] discretize a prescribed flight mission and enforce covertness slot by slot while maximizing an average rate. [[lin-2026-fc-ris-surveillance]] separates short-term antenna/surface configuration from long-term placement. [[guo-2024-multiuav-proactive-eavesdropping]] and [[huang-2026-intelligent-jamming-maritime]] learn sequential trajectory/power policies. [[zhan-2026-star-ris-aerial-monitoring]] couples per-slot control to a long-term energy queue. [[yan-2026-uav-trajectory-monitoring]] uses a fixed sensing cycle and predicts one cycle ahead to steer the next beam.

Mobility also belongs to different actors. A covert transmitter may move away from a warden; a legitimate monitor may move toward a suspicious source; a camera UAV follows a target group; an ISAC base station is fixed and estimates target motion; a friendly jammer moves relative to an unobserved Eve. A generic `trajectory optimization` label does not preserve these control semantics.

## Explicit non-comparability

- Covert detection error or KL divergence measures uncertainty about *whether a transmission exists*. It is not secrecy rate and does not say whether an intercepted payload can be decoded.
- [[monitoring-success-probability]] measures an authorized decoder beating a suspicious destination. It is not a warden's false-alarm-plus-miss probability.
- Proactive eavesdropping rate/success measure legitimate interception after intervention. They are not the physical-camera service throughput in STAR-RIS aerial monitoring.
- The STAR-RIS monitoring throughput measures delivery of captured content. Its target-distance constraint is not a tracking-error distribution.
- PRDFT estimation error, association correctness, and filtered trajectory RMSE describe kinematic tracking stages. They do not establish covertness, secrecy, or monitoring-success probability.
- Maritime secrecy rate compares legitimate and Eve rates. [[lstm-eavesdropper-trajectory-prediction]] supplies a controller state, but the supplied parse does not provide the prediction-error evidence needed to compare it numerically with ISAC tracking.

## Gaps

- No source jointly chooses among hiding, authorized interception, physical observation, and trajectory tracking after verifying observer authorization; each role is fixed before optimization.
- The covert designs remain tied to a particular detector, channel prior, or uncertainty set. Cross-detector robustness and over-the-air field evidence are absent.
- Physical aerial monitoring uses target distance as its observation proxy, leaving camera perception quality and target-identity continuity outside the optimization.
- The ISAC tracking pipeline estimates and associates current echoes before model-based prediction, while the maritime controller imputes an unobserved eavesdropper from position history. A measured sensing-to-prediction pipeline for adversarial aerial observers is not evaluated.
- Surface-assisted observation is split across ideal [[fully-connected-ris]] surveillance and diagonal [[star-ris]] video delivery. Hardware loss, acquisition overhead, and observation quality have not been validated together.

For the broader sensing-function and solver cross-section, see [[isac-sensing-in-aerial-mec]].
