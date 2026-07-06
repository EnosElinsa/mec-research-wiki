---
type: concept
title: Task Migration in MEC
tags: [task-offloading, mec, load-balancing]
related:
  - "[[task-offloading]]"
  - "[[vehicular-mec]]"
  - "[[zhang-2025-mcma-task-migration]]"
  - "[[vehicle-twin-migration]]"
  - "[[chen-2026-hc-mappo-vehicle-twin-migration]]"
  - "[[wang-2026-llm-qos-multiuav-resource]]"
created: 2026-05-28
updated: 2026-07-07
---

# Task Migration in MEC

The mechanism of forwarding an in-flight task from one edge server to another, mid-execution or mid-queue. Distinct from:

- **Task offloading** — initial decision *whether* to leave the device. Migration assumes offloading already happened.
- **Service handover** — moving a long-lived service binding (rather than a single task) between cells.

## When migration helps

- **Load balancing** — overloaded server transfers excess to an underloaded peer.
- **Mobility-driven proximity** — the source vehicle has moved closer to a different server; tasks should follow.
- **Failure recovery** — the original server fails or shuts down (e.g. UAV battery depletion).

## When migration hurts

- The migration itself costs network bandwidth and serialization latency. If the saved compute time doesn't exceed this cost, you've made things worse.
- Hysteresis — by the time you decide to migrate, the conditions that motivated the decision may have changed. Trajectory prediction (e.g. [[informer-trajectory-prediction]]) is the standard remedy.

## Decision dimensions

- **Trigger:** load threshold? deadline-imminent threshold? predicted-future cost?
- **Target:** nearest underloaded? predicted-future-cheapest? round-robin?
- **Granularity:** whole task? task fragments? state-only?

[[zhang-2025-mcma-task-migration]] handles all three via a two-stage MA-DRL controller informed by Informer-based trajectory prediction.

[[chen-2026-hc-mappo-vehicle-twin-migration]] specializes migration to [[vehicle-twin-migration]], where the state/service for a vehicle's digital twin follows high-mobility vehicles across RSUs and UAV edge servers.

[[wang-2026-llm-qos-multiuav-resource]] treats task migration as an air-to-air fractional allocation among UAV edge servers, controlled together with access, trajectory, bandwidth, and compute decisions for delay-fairness optimization.
