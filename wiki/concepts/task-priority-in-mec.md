---
type: concept
title: Task Priority in MEC
tags: [mec, scheduling, qos]
related:
  - "[[task-offloading]]"
  - "[[hao-2025-priority-aware-task-driven-co]]"
  - "[[peng-2025-drudm-cfg]]"
created: 2026-05-28
updated: 2026-05-28
---

# Task Priority in MEC

Not all tasks are equally important. The cost of missing a deadline varies by orders of magnitude across workload classes:

| Class | Example | Failure cost |
|---|---|---|
| **Safety-critical** | Autonomous driving control loop, navigation | Catastrophic (collision) |
| **Mission-critical** | Industrial control, medical telemetry | High (process failure) |
| **Real-time UX** | AR/VR rendering, interactive gaming | Moderate (broken experience) |
| **Streaming** | Live video, audio | Mild (degraded quality) |
| **Background** | Telemetry upload, batch analytics | Negligible |

A scheduler that treats all tasks equally — common in baseline MEC papers — implicitly trades safety-critical reliability for streaming throughput.

## Common formulations

- **Static priority levels.** Each task carries an integer / categorical priority on arrival.
- **Priority utility function.** Reward function multiplies by a priority-conditional weight: $u(p, T, E) = w(p) \cdot f(T, E)$ where $w$ scales rapidly with priority.
- **Deadline-aware urgency.** Priority interpreted as remaining-deadline / required-compute. Used in [[peng-2025-drudm-cfg]]'s DRUDM and elsewhere.
- **Preemptive scheduling.** High-priority tasks displace queued low-priority tasks. Risk: low-priority starvation.

## In this wiki

- [[hao-2025-priority-aware-task-driven-co]] uses the priority-utility-function formulation.
- [[peng-2025-drudm-cfg]] uses a distance/resource/urgency weighted score (DRUDM) — urgency proxies for priority.
- Most other curated sources implicitly assume uniform priority.

## Open question

How should priority be **assigned** in real deployments? Static labels are brittle; learning priority from task content is a research direction not yet covered in the wiki.
