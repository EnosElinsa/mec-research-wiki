---
type: synthesis
title: "Collaborative beamforming across the aerial/space corpus"
tags: [synthesis, collaborative-beamforming, virtual-antenna-array, multi-objective, physical-layer-security]
related:
  - "[[collaborative-beamforming]]"
  - "[[sun-2025-emoppo-vlh-aerial-cb]]"
  - "[[li-2024-emodrl-ground-space-cb]]"
  - "[[li-2024-emssa-uav-swarm-vaa]]"
  - "[[sun-2024-imssa-uav-secure-cb]]"
  - "[[zhang-2024-gdmtd3-aerial-secure-cb]]"
  - "[[multi-objective-reinforcement-learning]]"
  - "[[evolutionary-reinforcement-learning]]"
  - "[[salp-swarm-algorithm]]"
  - "[[physical-layer-security]]"
  - "[[diffusion-model-as-optimizer]]"
  - "[[drl-vs-evolutionary-vs-classical-solvers]]"
created: 2026-06-01
updated: 2026-06-01
---

# Collaborative beamforming across the aerial/space corpus

Five curated sources treat **collaborative beamforming (CB)** — distributed transmitters synchronizing carrier phases and excitation-current weights into a single [[collaborative-beamforming|virtual antenna array]] (VAA) whose received power scales with the square of the element count. All five share one author cluster (the Jilin-University / NTU [[geng-sun]] group) and one core modeling choice — that the array geometry is a *decision variable*, because the elements are mobile UAVs (or selectable ground terminals) whose positions both shape the beam and cost energy. This page maps what each one beamforms toward, what it trades off, and which solver family it reaches for; it is the CB counterpart to the [[isac-sensing-in-aerial-mec]] and [[maritime-mec-architectures]] track maps.

## Roster

| Source | Venue / year | Array → receiver | Objectives (multi-objective) | Solver family |
|---|---|---|---|---|
| [[li-2024-emssa-uav-swarm-vaa]] | IEEE TMC 2024 | GVAA (sensors) **+** AVAA (UAVs) → remote BSs | min completion time / min eavesdropper signal / min UAV energy | Swarm intelligence ([[salp-swarm-algorithm|EMSSA]]) |
| [[sun-2024-imssa-uav-secure-cb]] | IEEE TMC 2024 | UVAA (UAVs) → cluster of BSs | max worst-case secrecy rate / min max sidelobe level / min flight energy | Swarm intelligence ([[salp-swarm-algorithm|IMSSA]]) |
| [[zhang-2024-gdmtd3-aerial-secure-cb]] | IEEE TMC 2024 | UAV swarm → remote BS | max secrecy rate / min flight energy | DRL ([[diffusion-model-as-optimizer\|diffusion]]-enhanced [[td3\|TD3]]) |
| [[sun-2025-emoppo-vlh-aerial-cb]] | IEEE TMC 2025 | UVAA (AAVs) → terrestrial **mobile** user | max total rate / min flight energy | Evolutionary MORL ([[evolutionary-reinforcement-learning\|EMOPPO-VLH]]) |
| [[li-2024-emodrl-ground-space-cb]] | IEEE JSAC 2024 | DCB (ground terminals) → LEO satellite (uplink) | max uplink rate / min terminal energy / min handover frequency | Evolutionary MORL ([[evolutionary-reinforcement-learning\|EMODRL]]) |

## What the CB array points at

Two axes separate the five. The first is **where the array lives and what it serves**:

- **Aerial-to-ground, single receiver.** [[zhang-2024-gdmtd3-aerial-secure-cb]] and [[sun-2025-emoppo-vlh-aerial-cb]] both form a UAV/AAV array beaming to one terrestrial node — a remote base station (secure) and a *mobile* user (reliable), respectively. The mobile-user case is the only one that must track a moving receiver, which is why it pulls in the [[gauss-markov-mobility-model]] and LSTM temporal modeling.
- **Aerial-to-many, with ground arrays too.** [[li-2024-emssa-uav-swarm-vaa]] is the broadest: it puts CB into *both* the IoT sensors (ground VAAs) and the UAVs (aerial VAAs) simultaneously, so data hops cluster → BS without the UAVs flying back and forth. The parse states the authors "introduce collaborative beamforming into IoTs and UAVs simultaneously" — this dual-array framing is unique in the corpus.
- **Ground-to-space.** [[li-2024-emodrl-ground-space-cb]] inverts the geometry: energy-sensitive ground terminals with coarse antennas form a *distributed* CB (DCB) array to reach a LEO satellite on the uplink, where the extra objective is suppressing **ping-pong handovers** as the satellite moves overhead. It is the bridge between the CB thread and the wiki's [[sagin-satellite-offloading-landscape|NTN/LEO]] thread.

## What CB trades against

Every source frames CB as a **multi-objective** problem, and the recurring tension is identical: improving the beam pattern (rate or secrecy) requires repositioning the array, which costs **flight/terminal energy**. Four of five carry an explicit energy objective; the fifth ([[li-2024-emssa-uav-swarm-vaa]]) carries UAV energy as one of three. Beyond the shared rate-vs-energy core, the security-oriented designs add a leakage axis:

- **Secrecy as an objective.** [[zhang-2024-gdmtd3-aerial-secure-cb]] (secrecy rate) and [[sun-2024-imssa-uav-secure-cb]] (worst-case secrecy rate) make CB a [[physical-layer-security|physical-layer-security]] lever — the same high-gain mainlobe that reaches the receiver starves an eavesdropper, so directivity *is* the security mechanism.
- **Sidelobe level as a distinct knob.** [[sun-2024-imssa-uav-secure-cb]] is the only source that optimizes the **maximum sidelobe level (SLL)** as a separate objective, and it is also the only one that models **imperfect / unknown eavesdropper** location information — a harder threat model than the perfect-CSI secrecy in [[zhang-2024-gdmtd3-aerial-secure-cb]].
- **Leakage as a cost term.** [[li-2024-emssa-uav-swarm-vaa]] folds eavesdropper signal strength into the objective set rather than a secrecy rate, alongside time and energy.

## Solver split: swarm intelligence vs evolutionary-RL vs diffusion-DRL

The five sources cleanly partition into the three solver families the corpus tracks in [[drl-vs-evolutionary-vs-classical-solvers]], which makes CB a tidy microcosm of that larger debate:

- **Pure swarm intelligence (no learning).** [[li-2024-emssa-uav-swarm-vaa]] (EMSSA) and [[sun-2024-imssa-uav-secure-cb]] (IMSSA) both build on the [[salp-swarm-algorithm]], adding tailored operators (chaotic/circle-map initialization, discrete-variable update for BS selection, adaptive mutation) to handle mixed-variable, large-scale, NP-hard MOPs and emit a Pareto archive in one run. These are the *earliest* CB entries and the methodological precursors.
- **Evolutionary multi-objective RL.** [[sun-2025-emoppo-vlh-aerial-cb]] (EMOPPO-VLH) and [[li-2024-emodrl-ground-space-cb]] (EMODRL) wrap an evolutionary population mechanism around a (multi-objective) PPO learner to produce a Pareto policy *set* online — the same recipe as the non-CB [[song-2022-emorl-tcto-uav]]. They win when the receiver moves or the cluster scale changes, because offline optimizers cannot react.
- **Diffusion-enhanced DRL.** [[zhang-2024-gdmtd3-aerial-secure-cb]] (GDMTD3) is the only single-policy learner, using a [[diffusion-model-as-optimizer|generative diffusion model]] inside TD3 to represent the high-dimensional action distribution. It ties CB into the wiki's generative-AI thread.

The pattern mirrors the corpus-wide finding that evolutionary/swarm methods are chosen specifically for their **one-run Pareto set** (decision-maker picks a trade-off afterward), while DRL is chosen for **online reactivity** to a non-stationary environment.

## Grounded data points

- **30% fewer handovers.** [[li-2024-emodrl-ground-space-cb]] reports its EMODRL "save[s] 30% handover frequency with a similar uplink achievable rate compared with the rate greedy method" (parse abstract). This is the clearest quantified CB result in the corpus; the rest report qualitative IGD/hypervolume or "outperforms benchmarks" claims whose magnitudes are figure-derived and indicative.
- **Hardware touch.** [[sun-2024-imssa-uav-secure-cb]] reports a Raspberry Pi implementation to demonstrate CB-based secure communication in practice — a rare hardware element in an otherwise simulation-only track (see the corpus-wide hardware-validation note in [[overview]]).

## Gaps

- **No CB source carries a compute/offloading objective.** All five optimize communication (rate/secrecy) and energy, never MEC task latency — CB is a *communication-layer* enabler in this corpus, adjacent to but not fused with the offloading problems that dominate the rest of the wiki. A CB-for-offloading design is an open opportunity, not a curated result.
- **One author cluster.** Every CB source is from the [[geng-sun]] group, so the "consensus" here is really one lab's research line; treat cross-source agreement on method choice accordingly.
- **Threat-model depth is uneven.** Only [[sun-2024-imssa-uav-secure-cb]] handles imperfect/unknown eavesdropper information; the other secure-CB source assumes the eavesdropper is characterized.
