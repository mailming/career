# System Design Cheat Sheet — AI Infra Track

Quick-reference companion to the 8 full design docs in [../system-design/](../system-design/). Use this **the night before** an onsite to refresh; use the full docs for first-time learning.

For each topic: back-of-envelope numbers you should have memorised, the 3-4 most-likely follow-up questions, the trap an interviewer will set, and the 1-line headline answer.

---

## Universal: numbers to have memorised

| Quantity | Number | Use when |
|----------|--------|----------|
| L1 cache | 1 ns | rare; only if asked about kernel-level |
| L2 cache | 10 ns | rare |
| Main memory | 100 ns | "what's the cost of a memory read?" |
| Read 1 MB sequential from RAM | 250 µs | data-pipeline sizing |
| SSD random read | 100 µs | storage tiering |
| Read 1 MB from SSD | 1 ms | log/index reads |
| Send packet US East → US West | ~70 ms | replication geometry |
| Read 1 MB sequential from disk (HDD) | 20 ms | rare in 2026 |
| Datacenter round-trip | < 1 ms | service-mesh latency |
| Cross-region round-trip | 50-150 ms | multi-region tradeoffs |
| H100 SXM FP16 peak | ~1000 TFLOPS | inference throughput estimation |
| H100 HBM3 bandwidth | ~3 TB/s | "memory-bound" math |
| 1 GPU 70B model FP16 | doesn't fit (140 GB > 80 GB) | needed for "do we shard?" |
| 70B FP16 weights | 140 GB | sharding maths |
| 70B INT8 weights | 70 GB | quantisation tradeoffs |
| 70B INT4 weights | 35 GB | edge deployment |
| KV cache 70B (batch=1, ctx=8k) | ~3-5 GB | inference cost decomposition |
| LLM tokens/sec on H100 (70B FP16, batch=1) | ~30-50 tok/s | latency budgeting |
| LLM tokens/sec on H100 (70B FP16, batch=32, paged) | ~1000-1500 tok/s aggregate | throughput targeting |
| GPT-4-class API cost (in/out per 1M tokens) | $5 / $15 ish | cost-attribution math |
| Open-weights inference cost (70B on H100, amortised) | $0.5-2 per 1M tokens | "buy vs build" |
| H100 cloud price (on-demand) | $2-4 / GPU-hour | capacity planning |
| H100 cloud price (1y reserved) | $1.5-2 / GPU-hour | budget framing |

(Numbers vary; cite a range, not a single number. Interviewers care that you have an *order of magnitude*, not 3 sig figs.)

---

## 1. LLM Inference Serving (multi-tenant)

[Full doc: 01-llm-inference-serving.md](../system-design/01-llm-inference-serving.md)

**Headline:** Continuous batching + paged KV cache on a fleet of GPUs behind a token-budget-aware router, with prefix caching for repeated system prompts.

**5-bullet sketch.**
- Router: token-budget aware, per-tenant rate-limited, routes by model/sla.
- Engine: vLLM / TGI / TensorRT-LLM with continuous batching and paged-attention.
- Cache: shared prefix cache + per-tenant KV reuse.
- Storage: model weights pre-loaded on host SSD, warm-pool of N pods per model.
- Observability: per-request token in/out, TTFT, ITL, queue depth, cache hit rate.

**Back-of-envelope:** 70B FP16 on a single H100 = ~3 GB KV/req; 80 GB total ⇒ ~20 reqs in-flight at 8k ctx ⇒ 1000-1500 tok/s aggregate.

**4 likely follow-ups.**
1. *"How do you handle a 200k-context request?"* → Long-context queue with reserved capacity (or separate GPU pool); evict shorter requests' KV first; possibly chunked prefill.
2. *"What if a tenant burns through their token budget mid-request?"* → Streaming abort with refund metric; budget is enforced at queue admission, not mid-decode (decode is irreversible work).
3. *"Cold-start a new model variant — what's the workflow?"* → Pull weights from object store to local SSD (~30s-2min for 70B FP16 over 10 GbE); preload into GPU memory; warm with synthetic requests until cache is hot; only then accept traffic.
4. *"How do you do canaries?"* → Shadow traffic to the new model variant; compare output distributions on a held-out eval set; promote when within tolerance.

**Trap:** Forgetting that **prefill is compute-bound** and **decode is memory-bound**. You batch prefill aggressively; decode is harder to batch because of variable ITL. Continuous batching + paged-attention is the standard answer.

**1-line for the headline:** "I'd build it as a token-budget-aware admission layer in front of vLLM-style continuous-batching engines, with shared prefix cache and per-tenant KV reuse policies."

---

## 2. Vector DB at Scale

[Full doc: 02-vector-db-at-scale.md](../system-design/02-vector-db-at-scale.md)

**Headline:** HNSW for in-memory, IVF-PQ when the index doesn't fit RAM, DiskANN when even compressed it doesn't fit. Shard by document ID; replicate for QPS.

**Algorithm picks.**
| Index | RAM/vec (768d) | Build cost | Query latency | Use when |
|-------|----------------|------------|---------------|----------|
| Flat (brute force) | ~3 KB | none | O(N) | <1M vectors, ground truth |
| HNSW | ~3-4 KB | medium | < 10 ms | <100M vectors, in-RAM |
| IVF-PQ | ~100 bytes (compressed) | high | 10-50 ms | 100M-10B vectors |
| DiskANN | ~200 bytes (RAM) + on-disk graph | high | 20-100 ms | >10B, disk-resident |

**Back-of-envelope:** 1B vectors × 768d × FP32 = 3 TB raw. HNSW won't fit single-node RAM (> 500 GB). PQ-compressed = ~100 GB → fits one big-mem node, or shard across 4 standard nodes.

**4 likely follow-ups.**
1. *"What's the recall vs latency tradeoff?"* → HNSW: ef_search controls it; IVF: nprobe controls it. Bench at 90 / 95 / 99 recall on your specific dataset.
2. *"How do you do updates?"* → HNSW: in-place inserts, but deletes are tombstones; periodic rebuild. IVF-PQ: re-train the codebook periodically; rolling rebuild per shard.
3. *"Hybrid lexical+vector search?"* → BM25 (Elasticsearch / OpenSearch / tantivy) for sparse; vector index for dense; rerank top-K from each with a cross-encoder.
4. *"Multi-tenant isolation?"* → Per-tenant namespace = collection; either separate indexes (clean, more memory) or single index with metadata filter (cheaper but recall-pre-filter risk).

**Trap:** Filtering *post-ANN* breaks recall — if you ask for 10 results filtered by tenant_id, ANN gives you 10 nearest **globally**, and the post-filter may drop most. Fix: pre-filter (sub-graph per tenant) or over-fetch (K' >> K then filter).

**1-line:** "HNSW in RAM up to ~100M, IVF-PQ for the 100M-10B range, DiskANN beyond — shard by doc-id, replicate by QPS, and pre-filter not post-filter for multi-tenancy."

---

## 3. Agent Orchestration

[Full doc: 03-agent-orchestration.md](../system-design/03-agent-orchestration.md)

**Headline:** Durable workflow runtime (Temporal-style) with typed tool calls, step-level retry/compensation, and replayable state. Agent loop = LangGraph-style state machine, not a free-running while-loop.

**Components.**
- Planner — produces a tool-call graph (sometimes the same LLM that executes).
- Executor — runs tool calls with retry, timeout, cost budget per step.
- State store — durable execution log; one row per step; supports replay.
- Tool registry — typed interfaces (JSON-schema or proto), permissions, cost annotations.
- Eval harness — runs synthetic agent traces nightly.

**Back-of-envelope:** A "research agent" that runs 10 tool calls of 3s each + 5 LLM calls of 5s = ~55s wall-clock. With concurrency on independent branches, 25-30s.

**4 likely follow-ups.**
1. *"What's the failure model?"* → Each step is idempotent or compensable; the runtime persists state before/after each step; on crash, replay from last commit point.
2. *"How do you stop an agent that's looping?"* → Step budget + cost budget + wall-clock budget enforced by the runtime, not the agent (the agent can't trust itself).
3. *"Multi-agent coordination?"* → Two patterns: (a) supervisor-worker (one agent dispatches to specialists), (b) blackboard (shared state, agents subscribe to changes). Pick by problem shape.
4. *"How do users debug?"* → Per-step trace UI (input, output, tool args, cost, latency) — basically a stack-trace for the agent's thinking. Langfuse / AgentOps reference architecture.

**Trap:** Treating the LLM as the controller. The LLM is a *step* in the workflow; the workflow is owned by the runtime. Otherwise you can't enforce budgets, retries, or audit.

**1-line:** "Durable-workflow runtime owns the loop; the LLM is one of many typed tool calls inside it. Budgets and retries are runtime concerns, not LLM concerns."

---

## 4. Eval Pipelines

[Full doc: 04-eval-pipelines.md](../system-design/04-eval-pipelines.md)

**Headline:** Versioned eval datasets → offline replay against versioned models/prompts → versioned judges → regression alerts. Online: per-tenant feedback funnel into the same dataset format.

**Eval types.**
| Type | What it measures | When you trust it |
|------|------------------|-------------------|
| Exact-match / regex | Determinstic format | Code gen, structured output |
| Embedding similarity | Semantic match | Summarisation, open-ended |
| LLM-as-judge | Quality / preference | Subjective, but **drifts** |
| Human eval | Ground truth | Once, for the labelled set |
| Production telemetry | Real distribution | When you've solved consent |

**4 likely follow-ups.**
1. *"How do you avoid judge drift?"* → Pin the judge model version; rerun the calibration set on judge upgrades; alert if judge agreement with humans changes > 2%.
2. *"What's the regression alert threshold?"* → Per-slice, not global. Define "slice" = (task_type, tenant_segment, model_version). Alert on slice-level p95 quality drop > X.
3. *"How do you handle dataset poisoning / overfitting to the eval?"* → Hold out a "gold" set that *never* enters CI; rotate it quarterly.
4. *"Cost of running all evals on every commit?"* → Tier evals: smoke (5 min, every PR), regression (30 min, nightly), full (4 hrs, weekly).

**Trap:** Believing the judge model. LLM-as-judge agrees with itself 95% of the time but with humans only 70-80%. Calibrate.

**1-line:** "Versioned datasets, versioned models, versioned judges, with sliced regression alerts and a held-out gold set you never train against."

---

## 5. Distributed Training Orchestration

[Full doc: 05-distributed-training-orchestration.md](../system-design/05-distributed-training-orchestration.md)

**Headline:** Gang-scheduled jobs on a Slurm-or-K8s cluster, with elastic checkpointing every N minutes, fault-tolerant collective comms (NCCL), and a job-DAG layer (Ray / Flyte / Argo) above.

**Parallelism modes.**
| Mode | Splits | When |
|------|--------|------|
| Data parallel (DDP / FSDP) | batch | model fits 1 GPU; scale by batch |
| Tensor parallel | matrix | model > 1 GPU; same-node only (NVLink) |
| Pipeline parallel | layers | model >> 1 GPU; cross-node |
| Sequence parallel | sequence dim | long-context training |
| 3D = DP × TP × PP | all | frontier-scale (>70B) |

**4 likely follow-ups.**
1. *"Gang scheduling vs. backfill?"* → Training jobs need all-or-nothing (a 64-GPU job needs all 64 to start together). Slurm does this natively; K8s needs Kueue or Volcano.
2. *"Checkpoint strategy?"* → Sharded checkpoints (one file per rank); async write to object store; resume validates checksum + step count.
3. *"What if a node fails mid-epoch?"* → With FSDP elastic: pause, evict failed rank, rebuild group, resume from last checkpoint. Cost: minutes, not hours.
4. *"How do you debug a stuck job?"* → py-spy on each rank; NCCL trace; check for ranks blocked at different collective ops (= mismatched control flow).

**Trap:** Conflating data-parallel scaling with model scaling. DDP scales throughput; you only need TP/PP when the model doesn't fit one GPU.

**1-line:** "Gang-scheduled Slurm or K8s with FSDP/3D parallelism, sharded async checkpointing, NCCL diag, and a DAG layer for hyperparam sweeps."

---

## 6. GPU Autoscaling for Inference

[Full doc: 06-gpu-autoscaling.md](../system-design/06-gpu-autoscaling.md)

**Headline:** Scale on **queue depth + token-rate**, not CPU. Maintain a warm-pool because cold-start a 70B model is 30s-2min. Use spot for tier-2 traffic, on-demand for tier-1.

**Signals to scale on.**
| Signal | Latency to react | When to use |
|--------|------------------|-------------|
| Queue depth | Seconds | The default; reflects real load |
| Token decode rate | Seconds | Catches over-batching that hurts ITL |
| TTFT p95 | 30-60s | Slow but UX-meaningful |
| GPU utilisation | Misleading | Don't use; high util ≠ saturated |
| Predictive (time of day) | Pre-emptive | Layer on top, not as primary |

**Cold-start tactics.**
- Weights on host SSD (not pulled from S3 at start).
- One always-warm pod per model.
- Preheat on rollout: synthetic requests before cutting traffic.
- For occasional models: serverless GPU (Modal-style) with shared model registry.

**4 likely follow-ups.**
1. *"Spot vs. on-demand mix?"* → Spot for batch / async / tier-2 (~70% savings); on-demand for tier-1 latency-SLA traffic. Spot eviction is ~2 min notice; drain gracefully.
2. *"Right-size the warm pool?"* → Pool size = max(P95 demand - autoscale lag × incoming rate). Tune by observed cold-start counts; target zero cold-starts at P95.
3. *"Multi-model on one GPU?"* → Possible with weight-streaming (load-on-demand from SSD) but adds latency. Usually one model per pod, pack pods on the same node.
4. *"How do you handle a model rollout without downtime?"* → Blue-green at the pool level; new pool warms; router shifts traffic 1% → 10% → 100% with eval gates between.

**Trap:** Scaling on GPU utilisation. A GPU can be 99% util on tiny batches that are wasting compute. Queue depth is the right primary signal.

**1-line:** "Queue-depth-driven HPA on a warm-pool of pods, with sharded weight cache and spot/on-demand tiering by SLA."

---

## 7. Multi-Tenant Inference Cost Attribution

[Full doc: 07-multi-tenant-inference-cost.md](../system-design/07-multi-tenant-inference-cost.md)

**Headline:** Per-request cost = (prefill tokens × prefill-rate) + (decode tokens × decode-rate) + (GPU-seconds × GPU rate) + (overhead). Bill on tokens; account on GPU-seconds for the truth.

**Cost decomposition.**
- **Prefill cost** = tokens × $/token at full GPU utilisation (compute-bound).
- **Decode cost** = tokens × $/token at batched-decode utilisation (memory-bound — much more expensive per token at low batch).
- **KV cache cost** = (KV bytes × seconds-in-flight) / (HBM cost).
- **Idle GPU cost** = baseline divided by tenants by some allocation rule (active-share, reserved-share, weighted).

**4 likely follow-ups.**
1. *"How do you bill for cached prefix tokens?"* → Discount; e.g., 10% of normal token price (you save the prefill compute). Tracks how providers like Anthropic / OpenAI bill.
2. *"Per-tenant rate limits — token-based or request-based?"* → **Token-based.** A 100k-token request costs 100× a 1k-token request; request-rate limits are a fairness fiction.
3. *"How do you handle a tenant that bursts and starves others?"* → Token-budget queue with weighted-fair queueing; per-tenant max in-flight; spillover to a slower pool.
4. *"Cost vs. quality vs. latency triangle?"* → Three tiers: small fast (cheap, lower quality), large slow (expensive, best), middle (default). Router picks by request annotation or learned policy.

**Trap:** Reporting cost only at the request level. Tenants compare against each other and against published API prices; you need cost-per-token + utilisation-share + cache-hit-rate per tenant.

**1-line:** "Token-priced billing on top of GPU-second accounting, with weighted-fair queueing, prefix-cache discounts, and per-tenant cost / latency / quality tiers."

---

## 8. Prompt + Eval Registry

[Full doc: 08-prompt-eval-registry.md](../system-design/08-prompt-eval-registry.md)

**Headline:** Versioned, typed prompts + paired eval suites in a registry (think: Hugging Face Hub, but for prompts). Every prompt has a hash, a parent, an eval delta, and a deployment manifest.

**Schema sketch.**
```
PromptRecord:
  id: stable string, e.g. "amp/runbook/diagnose-firewall@v3"
  parent_id: ...@v2
  template: jinja2 string + variable schema
  model_constraints: provider/model/min-version
  eval_suite_ref: "amp/runbook/diagnose-firewall/eval@v3"
  deploy_status: dev | staging | prod | retired
  hash: sha256(template + variable_schema + model_constraints)
```

**4 likely follow-ups.**
1. *"How does a prompt get promoted?"* → Eval delta vs. parent must be non-negative across all slice metrics; manual sign-off + canary rollout.
2. *"What about runtime A/B?"* → The router picks a prompt variant by hash; logs the hash with the request; offline eval rolls up by hash.
3. *"How do you handle prompt secrets / sensitive examples?"* → Variables, not literals. The registry holds the template; runtime injects values; PII never lives in the prompt record.
4. *"Schema migrations when prompts change?"* → Parent ref + variable schema diff. A breaking change forces a new parent line, not a v-bump.

**Trap:** Treating prompts as string literals in code. They drift, no one knows which version is in production, and eval-on-prompt-change is impossible. A registry is non-optional at scale.

**1-line:** "Content-addressed prompt records with paired eval suites, deploy manifests, and a router that logs which prompt-hash served each request."

---

## How to use this in interviews

**Day-before-onsite:** Read this whole file in one 30-min sitting. Mark which numbers you can't recall — write those on a card and revisit.

**During the interview:**
1. Start with the **headline** (the 1-line sentence at top of each section).
2. Draw the 5-bullet sketch.
3. Pause and ask: "What's the part you'd like me to go deepest on?"
4. Use the back-of-envelope numbers for any sizing question.
5. When they ask "what could go wrong?" — go to the **trap** for that topic; you've already thought about it.

**After the interview:**
- Note the question you weren't ready for. Add the answer to this file.
- Note which trap or follow-up they actually asked. The patterns repeat across companies.

---

## What this cheat sheet deliberately doesn't cover

- Generic distributed systems primitives (consensus, replication, sharding) — you have 20 years of this; you don't need a cheat sheet.
- ML / model-internal questions (loss functions, attention mechanics) — out of scope for AI **infra** roles; if asked, frame as "I'd partner with a research engineer on that."
- DSA review for system-design rounds — the system design round is not a coding round; don't get pulled into algorithm details.
