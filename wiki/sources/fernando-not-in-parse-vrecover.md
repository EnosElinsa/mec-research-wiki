---
type: source
title: "V-Recover: Virtual Machine Recovery When Live Migration Fails"
authors: ["Dinuni Fernando", "Jonathan Terner", "Ping Yang", "Kartik Gopalan"]
year: "not in parse"
url: "not in parse"
venue: "not in parse"
modeling_card: not_applicable
tags: [source, virtual-machine, live-migration, fault-tolerance, checkpointing, recovery]
related:
  - "[[service-migration]]"
  - "[[stateful-edge-microservice-migration]]"
  - "[[calagna-2024-robust-stateful-migration]]"
created: 2026-08-27
updated: 2026-08-27
---

# V-Recover: Virtual Machine Recovery When Live Migration Fails

## Citation

Fernando, D., Terner, J., Yang, P., & Gopalan, K. *V-Recover: Virtual Machine Recovery When Live Migration Fails*. Venue and year are not in the parse.

## TL;DR

V-Recover protects running VMs during live migration failures. Forward incremental checkpoints recover source failures during pre-copy and post-copy, while reverse incremental checkpoints recover destination or network failures during post-copy; a KVM/QEMU implementation measures the resulting overhead.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Fernando et al. [x] addressed VM loss when a source, destination, or network fails during live migration. V-Recover uses forward incremental checkpointing before and during migration to reconstruct state after source failure, and reverse incremental checkpointing after post-copy resumes to recover from destination or network failure. The techniques are integrated into KVM/QEMU and evaluated for migration and application-performance overhead. Results show effective recovery with acceptable overhead on the reported workloads. The design targets VM fault tolerance and does not optimize edge-service placement or migration scheduling.

## Problem and system model

Pre-copy and post-copy split the current VM state across machines during migration. Source failure can lose the latest state in either method, while destination or network failure is additionally catastrophic for post-copy.

## Method

Forward incremental checkpoints are stored away from the source and combined with state already at the destination. During post-copy, reverse checkpoints are sent from destination to an external in-memory store, allowing source recovery after destination or network failure.

## Key findings

- V-Recover handles source failure for both pre-copy and post-copy.
- Reverse checkpointing extends recovery to destination and network failure during post-copy.
- KVM/QEMU experiments report effective recovery with acceptable migration and application overhead.

## Limitations / future work

The evaluation is confined to KVM/QEMU and the tested VM workloads. Checkpoint storage, bandwidth monitoring, and failure timing affect overhead.

## Relation to the corpus

V-Recover adds a fault-tolerance layer to [[service-migration]] and complements stateful connection continuity in [[calagna-2024-robust-stateful-migration]].

## Raw artifacts

- Parse: `raw/sources/V-Recover_Virtual_Machine_Recovery_When_Live_Migration_Fails/V-Recover_Virtual_Machine_Recovery_When_Live_Migration_Fails.md`
- Origin PDF and figures are in the same folder.
