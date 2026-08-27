---
type: source
title: "ReSync: Coordinated Live-Migration for Stateful Containers in Mobile Edge Computing"
authors: ["Reinhard Scheuer", "Yibo Pi", "Xudong Wang"]
year: "not in parse"
url: "not in parse"
venue: "not in parse"
modeling_card: not_applicable
tags: [source, mobile-edge-computing, stateful-migration, container-migration, handover, checkpoint-restore]
related:
  - "[[stateful-edge-microservice-migration]]"
  - "[[service-migration]]"
  - "[[calagna-2024-robust-stateful-migration]]"
  - "[[ma-2019-layered-container-migration]]"
created: 2026-08-27
updated: 2026-08-27
---

# ReSync: Coordinated Live-Migration for Stateful Containers in Mobile Edge Computing

## Citation

Scheuer, R., Pi, Y., & Wang, X. *ReSync: Coordinated Live-Migration for Stateful Containers in Mobile Edge Computing*. Venue and year are not in the parse.

## TL;DR

ReSync augments checkpoint/restore with buffered input replay and coordinates migration timing with a radio handover. A small MEC testbed reports average YOLOv8 downtime of 0.378 seconds and up to 90% lower downtime than the evaluated Pre-copy scheme while retaining comparable total migration time.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Scheuer et al. [x] designed ReSync for stateful container migration across mobile edge hosts during user handover. The source continues serving while inputs are buffered, transferred, and replayed at the restored destination, after which a coordinator aligns the switchover with the predicted handover event. The coordinator uses mobility and radio information together with conservative application migration-time estimates. Small-scale experiments with YOLOv8 and Deepface report average YOLOv8 downtime of 0.378 seconds and up to 90% lower downtime than Pre-copy. These results are prototype and simulation evidence under the tested applications and network conditions, not a universal downtime guarantee.

## Problem and system model

When a user crosses an MEC-area boundary, keeping the application at the original host adds backhaul latency. Moving a stateful service concurrently with the radio handover requires consistent runtime state and a carefully timed switchover.

## Method

ReSync checkpoints the running container, restores it at the target, duplicates post-checkpoint inputs into a FIFO buffer, and replays them until destination state catches up. A coordinator estimates the A3 handover condition from signal strength and time-to-trigger behavior and starts migration early enough to reach a handover-ready state.

## Key findings

- The YOLOv8 experiment reports 0.378 seconds average downtime independent of the tested network condition.
- Total migration time ranges from about 5.2 to 12.3 seconds across the reported network cases.
- Direct comparison reports up to 90% downtime reduction over Pre-copy with comparable total migration time.

## Limitations / future work

The migration prototype uses a small MEC testbed and two inference applications. The coordinator relies on conservative application- and network-specific timing estimates, while large-scale robustness is evaluated by simulation.

## Relation to the corpus

ReSync complements [[calagna-2024-robust-stateful-migration]] by synchronizing post-checkpoint inputs and handover timing rather than analytically selecting migration bandwidth and iteration counts. It also differs from [[ma-2019-layered-container-migration]], which targets redundant file-system transfer.

## Raw artifacts

- Parse: `raw/sources/ReSync_Coordinated_Live-Migration_for_Stateful_Containers_in_Mobile_Edge_Computing/ReSync_Coordinated_Live-Migration_for_Stateful_Containers_in_Mobile_Edge_Computing.md`
- Origin PDF and extracted figures are in the same folder.
