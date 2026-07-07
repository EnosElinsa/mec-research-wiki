---
type: source
title: "HybridRAG-Based LLM Agents for Low-Carbon Optimization in Low-Altitude Economy Networks"
authors: ["Jinbo Wen", "Cheng Su", "Jiawen Kang", "Jiangtian Nie", "Yang Zhang", "Jianhang Tang", "Dusit Niyato", "Chau Yuen"]
year: 2026
url: "https://doi.org/10.1109/TMC.2025.3637120"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, low-altitude-economy, hybridrag, generative-ai, diffusion-model, soft-actor-critic, low-carbon-mec]
related:
  - "[[hybridrag-network-optimization]]"
  - "[[llm-assisted-mec-optimization-control-plane]]"
  - "[[low-altitude-intelligent-network]]"
  - "[[task-offloading]]"
  - "[[rotary-wing-propulsion-energy-model]]"
  - "[[diffusion-model-as-optimizer]]"
  - "[[soft-actor-critic]]"
  - "[[generative-ai-for-mec]]"
created: 2026-07-07
updated: 2026-07-07
---

# HybridRAG-Based LLM Agents for Low-Carbon Optimization in Low-Altitude Economy Networks

## Citation

Wen, J., Su, C., Kang, J., Nie, J., Zhang, Y., Tang, J., Niyato, D., & Yuen, C. (2026). *HybridRAG-Based LLM Agents for Low-Carbon Optimization in Low-Altitude Economy Networks*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2025.3637120.

## TL;DR

Uses HybridRAG to help LLM agents formulate a low-carbon multi-UAV MEC optimization problem for LAE networks, then solves the generated problem with R^2DSAC, a double-regularized diffusion-enhanced SAC algorithm. The retrieval stack combines KeywordRAG, VectorRAG, and GraphRAG so model-formulation prompts can retrieve both textual domain knowledge and relational UAV/MEC structure. The DRL solver uses diffusion-policy regularization and dynamic pruning to improve reward while tracking training/inference carbon emissions.

## Problem framing

Low-carbon LAE MEC design is hard because UAV mobility, communication, computation, propulsion energy, task offloading, and resource allocation interact in one coupled optimization problem. Manual formulation can omit important terms such as propulsion energy or Wh/J conversion. Traditional vector RAG can miss relational structure, while DRL solvers can fall into suboptimal exploration in high-dimensional action spaces.

## System model

The expert model is a multi-UAV-assisted MEC network with rotary-wing UAVs and users over slotted time. Users generate indivisible tasks with data size and CPU-cycle demand, and offload to UAV MEC servers. UAV states include 3D position at fixed height, flight speed/direction, collision and boundary constraints, coverage constraints, communication links, computation allocation, task offloading, and rotary-wing propulsion energy. The objective minimizes carbon emissions, with total energy converted through a carbon-emission coefficient and a Wh/J conversion factor.

## Method

HybridRAG merges three retrieval channels:

- KeywordRAG indexes hierarchical headings and domain-specific terms for precise engineering terminology.
- GraphRAG builds a Neo4j knowledge graph from expert IEEE papers so the LLM can retrieve relationships among UAVs, MEC servers, user devices, tasks, and network resources.
- VectorRAG retrieves semantically similar passages from a Qdrant vector store.

The merged retrieval results feed an LLM agent that formulates the carbon-emission optimization problem. The solver, R^2DSAC, models the formulated problem as an MDP and uses a diffusion policy inside SAC, adding diffusion entropy regularization, action entropy regularization, Q-learning guidance, policy improvement, and dynamic pruning of low-importance actor neurons.

## Key findings

- HybridRAG reports precision 46.2, recall 76.5, and F1 53.2, compared with 44.6, 74.4, and 49.9 for VectorRAG plus KeywordRAG.
- HybridRAG improves claim recall (83.1 vs 82.7), context precision (33.4 vs 32.4), context utilization (80.2 vs 75.8), and relevant-noise sensitivity (28.6 vs 30.5), while hallucination (7.2 vs 6.7) and faithfulness (92.4 vs 92.8) are slightly worse than the non-GraphRAG baseline.
- R^2DSAC reports the highest test rewards and converges faster than PPO and SAC, with 64% improvement over SAC and 19.9% over PPO in the result discussion; the conclusion states 64.17% over SAC.
- CodeCarbon estimates about 70.3 g carbon emissions for model training and 0.025 g per inference.
- The reported best hyperparameter setting includes pruning rate 0.1 and diffusion steps T=3; excessive behavior-cloning weight reduces exploration.

## Limitations / future work

The paper notes that HybridRAG's hallucination and faithfulness metrics are not better than the VectorRAG+KeywordRAG baseline and suggests prompt engineering for improving designer-agent interaction. It also leaves multi-agent diffusion-model-based DRL algorithms for carbon optimization in LAENets as future work. The system results are simulation-based.

## Relation to the corpus

This source extends [[generative-ai-for-mec]] from AIGC service provisioning and diffusion optimizers into LLM-agent-assisted optimization formulation. It gives the corpus a [[hybridrag-network-optimization]] concept and links low-carbon LAE design to [[diffusion-model-as-optimizer]], [[soft-actor-critic]], [[rotary-wing-propulsion-energy-model]], and [[task-offloading]]. In [[llm-assisted-mec-optimization-control-plane]], it is the formulation-side counterpart to LLM-assisted DRL state/reward design, teacher-policy generation, and long-tail resource repair.

## Raw artifacts

- `raw/sources/HybridRAG-Based LLM Agents for Low-Carbon Optimization in Low-Altitude Economy Networks/HybridRAG-Based LLM Agents for Low-Carbon Optimization in Low-Altitude Economy Networks.md`
- Original PDF and extracted figures (`images/`) in the same folder.
