---
type: concept
title: "Handoff-Aware UAV Trajectory Planning"
tags: [cellular-connected-uav, handoff, trajectory-planning, cargo-uav, connectivity]
related:
  - "[[cellular-connected-uav]]"
  - "[[radio-map-aided-uav-path-planning]]"
  - "[[device-association]]"
  - "[[uav-delivery-pickup-dropoff]]"
  - "[[cherif-2021-disconnectivity-aware-cargo-uav]]"
  - "[[cherif-2024-rl-cargo-uav-cell-association]]"
  - "[[peng-2025-cargo-uav-energy-outage-tradeoff]]"
  - "[[connectivity-aware-cargo-uav-path-planning]]"
created: 2026-11-02
updated: 2026-11-03
---

# Handoff-Aware UAV Trajectory Planning

Trajectory planning for a cellular-connected UAV that treats the number of serving-cell changes as a cost alongside propulsion energy and link reliability. Terrestrial base stations are down-tilted toward ground users, so a UAV at altitude is served by antenna sidelobes, meets coverage holes, and switches cells often. Each handoff adds signaling overhead that can disturb command-and-control links, so the planner may accept a longer path to cross fewer cell boundaries. The usual reliability companion is a disconnectivity rate: the fraction of the mission spent without a usable cell.

## In this wiki

[[cherif-2021-disconnectivity-aware-cargo-uav]] fixes the serving cell from a connectivity heatmap and uses dynamic programming to minimize weighted energy and handoffs under battery and disconnectivity limits. [[cherif-2024-rl-cargo-uav-cell-association]] makes cell association a decision, letting a Q-learning agent pair each motion step with one of the strongest cells and penalize cell changes in the reward. [[peng-2025-cargo-uav-energy-outage-tradeoff]] weighs expected outage time rather than handoff count, and its communication-scheduling variable selects the serving cell along a radio-map trajectory.

The concept differs from [[radio-map-aided-uav-path-planning]], which uses a map mainly as a feasibility layer, by placing the cell-change count in the objective. It also differs from LEO compute-state handover, where a computation rather than a user link is transferred.
