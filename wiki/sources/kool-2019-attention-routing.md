---
type: source
title: "Attention, Learn to Solve Routing Problems!"
authors: ["Wouter Kool", "Herke van Hoof", "Max Welling"]
year: 2019
url: "https://arxiv.org/abs/1803.08475"
venue: "ICLR 2019 (International Conference on Learning Representations)"
modeling_card: not_applicable
tags: [source, attention-model, combinatorial-optimization, routing, reinforce, learned-heuristics, foundational-method]
related:
  - "[[transformer-encoder]]"
  - "[[generalized-traveling-salesman-problem]]"
  - "[[transformer-weighted-a-star-trajectory-planning]]"
created: 2026-11-02
updated: 2026-11-02
---

# Attention, Learn to Solve Routing Problems!

## Citation

Kool, W., van Hoof, H., & Welling, M. (2019). *Attention, Learn to Solve Routing Problems!* **ICLR 2019**. arXiv:1803.08475.

## TL;DR

An attention-based encoder-decoder, trained with REINFORCE and a greedy-rollout baseline, learns construction heuristics for routing problems. With one set of hyperparameters it approaches optimal TSP tours up to 100 nodes and produces strong heuristics for two VRP variants, the orienteering problem, and a stochastic prize-collecting TSP.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Kool et al. [x] studied learning heuristics for combinatorial optimization problems to reduce costly hand-crafted algorithm development. They proposed a model based on attention layers with benefits over the Pointer Network and trained it using REINFORCE with a simple baseline based on a deterministic greedy rollout, which they found more efficient than a value function baseline. The approach significantly improves over earlier learned heuristics for the Travelling Salesman Problem and comes close to optimal results for problems up to 100 nodes. With the same hyperparameters, it learns strong heuristics for two variants of the Vehicle Routing Problem, the Orienteering Problem, and a stochastic variant of the Prize Collecting TSP, outperforming a range of baselines and approaching highly optimized specialized algorithms.

## Scope and method

The encoder applies multi-head attention over node embeddings; the decoder builds a solution one node at a time using a context embedding and masks infeasible nodes. The baseline is the cost of a greedy rollout of the best model so far, frozen each epoch. This is a foundational learning method for combinatorial problems, not an application-specific network decision model.

## Key findings

- With greedy decoding, the attention model's TSP optimality gaps are 0.34%, 1.76%, and 4.53% for 20, 50, and 100 nodes.
- Sampling solutions reduces the gap further, for example to 2.26% at 100 nodes.
- The rollout baseline trains more efficiently than a learned value baseline.

## Limitations / future work

Results are for problem sizes up to 100 nodes, and the method builds solutions without search-based improvement.

## Relation to the corpus

A widely reused attention model for routing and visiting-order decisions, related to [[transformer-encoder]] state processing and to UAV routing formulations such as [[generalized-traveling-salesman-problem]] and [[transformer-weighted-a-star-trajectory-planning]].

## Raw artifacts

- Parse: `raw/sources/Attention Learn to Solve Routing Problems/kool2019iclr.md`
- Origin PDF is in the same folder.
