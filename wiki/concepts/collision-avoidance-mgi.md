---
type: concept
title: Markov Game of Intervention (MGI) for Collision Avoidance
tags: [game-theory, safe-rl, multi-agent, uav]
related:
  - "[[safe-reinforcement-learning]]"
  - "[[zhang-2025-ssac-mgi-heterogeneous-uav]]"
created: 2026-05-28
updated: 2026-05-28
---

# Markov Game of Intervention (MGI) for Collision Avoidance

A two-agent sub-game introduced in [[zhang-2025-ssac-mgi-heterogeneous-uav]] for collision avoidance between paired UAVs on near-collision trajectories.

The trick: instead of a symmetric cooperative game where both UAVs share the same avoidance objective (which can lead to symmetric-swerve collisions where both UAVs deflect identically and still hit), MGI **asymmetrically** assigns roles:

- **Intervention agent.** Constrained to actively deflect to maintain separation.
- **Non-intervention agent.** Free to pursue its primary task; treats the intervention agent's deflection as a known constraint.

The Nash equilibrium of this asymmetric game is a stable separation maneuver where neither UAV's primary task is disrupted more than necessary.

## Why this beats symmetric cooperative deflection

- **Symmetric:** both UAVs see the same approach geometry, both compute "swerve right". They still collide.
- **Asymmetric (MGI):** roles are determined by some deterministic rule (UAV ID, current speed, heading). One UAV swerves, the other holds course. The lateral separation grows monotonically.

## Trade-offs

- The role-assignment rule must be deterministic and globally consistent across the fleet — needs either a deterministic ID-ordering or a higher-level coordinator.
- Doesn't scale directly to 3-way+ collisions; pairwise decomposition is a reasonable first approximation.
- Assumes both UAVs have low-latency awareness of each other's positions.
