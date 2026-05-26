# Reading List — AI Infra (Curated, Week-Aligned)

The 5-month plan calls for 1 hour/week of reading minimum. This file is your reading queue: papers, blog posts, and docs, **aligned to the week** of [STUDY-PLAN-5MONTHS.md](../STUDY-PLAN-5MONTHS.md) when each is most relevant.

Rules:
- **Pick 1-2 per week**, not all. Reading without internalising is wasted time.
- **Take notes** in a single file (suggested: `notes/<week>.md` — gitignored). 5 bullets per paper is the right unit.
- **Cite what you read** when interviewers go deep on a topic. "I was reading the vLLM paper last week and they make the point that..." instantly establishes seniority.
- If a link rots, search the title — most of these are stable enough to find.

---

## Month 1, Week 1 — LLM inference (paired with design doc 01)

**Must read this week (pick 1):**

1. **Efficient Memory Management for Large Language Model Serving with PagedAttention** — Kwon et al, 2023 (the vLLM paper). https://arxiv.org/abs/2309.06180
   - **Why:** Foundational. Anyone who interviews you on inference will have read this.
   - **Take-away:** Why fixed-size blocks for KV cache + how that enables continuous batching and prefix sharing.

2. **vLLM docs — engine internals.** https://docs.vllm.ai/
   - **Why:** Concrete; you can run code; turns the paper into intuition.

**Optional supplementary:**
- **FlashAttention** (Dao et al, 2022). https://arxiv.org/abs/2205.14135 — why I/O-aware attention is so much faster.
- **Anthropic prompt caching docs.** https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching — production-relevant; cite in cost/inference discussions.

---

## Month 1, Week 2 — Retrieval & vector DBs (paired with design doc 02)

**Must read (pick 1):**

3. **Efficient and robust approximate nearest neighbor search using HNSW** — Malkov & Yashunin, 2018. https://arxiv.org/abs/1603.09320
   - **Why:** HNSW is the default in production vector DBs. Know how the layers work.

4. **DiskANN: Fast Accurate Billion-point Nearest Neighbor Search on a Single Node** — Subramanya et al, 2019. https://suhasjs.github.io/files/diskann_neurips19.pdf
   - **Why:** When indexes don't fit RAM, this is the answer.

**Optional:**
- **Pinecone or Weaviate engineering blog** — pick any one production write-up to ground theory in reality.
- **Lucene Vector Search** — for hybrid lexical+dense systems.

---

## Month 1, Week 3 — Agent orchestration (paired with design doc 03)

**Must read (pick 1):**

5. **ReAct: Synergizing Reasoning and Acting in Language Models** — Yao et al, 2022. https://arxiv.org/abs/2210.03629
   - **Why:** The thinking-loop paradigm everyone references; older but foundational.

6. **LangGraph documentation — concepts + glossary.** https://langchain-ai.github.io/langgraph/
   - **Why:** You already use this in SmartTuna; deepen by reading the orchestration concepts page.

**Optional:**
- **Anthropic — Building Effective Agents.** https://www.anthropic.com/research/building-effective-agents — Anthropic's own opinion; if you interview there, *cite it*.
- **Claude Code internals blog posts** (Anthropic's engineering blog) — useful surface for the Cursor/Anthropic developer-productivity roles.

---

## Month 1, Week 4 — Eval (paired with design doc 04)

**Must read (pick 1):**

7. **Holistic Evaluation of Language Models (HELM)** — Stanford CRFM, 2022 (paper + ongoing benchmark). https://crfm.stanford.edu/helm/
   - **Why:** The blueprint for taxonomy of evaluation. Even if you don't run HELM, you should know the categories.

8. **Anthropic — How we evaluate models** (multiple blog posts on their alignment + Constitutional AI work).
   - **Why:** Anthropic-specific values + practical setup.

**Optional:**
- **Langfuse / AgentOps docs** — production eval observability; the runtime side of evaluation (you already use these in OpenClaw, deepen).
- **LLM-as-a-Judge papers** (e.g., "Judging LLM-as-a-Judge with MT-Bench" — Zheng et al). https://arxiv.org/abs/2306.05685 — calibration and limitations.

---

## Month 2, Week 5 — Distributed training (paired with design doc 05)

**Must read (pick 1):**

9. **Megatron-LM: Training Multi-Billion Parameter Language Models** — Shoeybi et al, 2019. https://arxiv.org/abs/1909.08053
   - **Why:** Tensor parallelism foundational; understand the layer-split.

10. **PyTorch FSDP: Experiences on Scaling Fully Sharded Data Parallel** — Zhao et al, 2023. https://arxiv.org/abs/2304.11277
    - **Why:** This is what real shops use today; understand sharded params vs. ZeRO stages.

**Optional:**
- **DeepSpeed ZeRO** docs / paper — historical context.
- **Pathways / TPU world** — Google's approach to distributed; useful contrast.

---

## Month 2, Week 6 — GPU autoscaling, serving infra (paired with design doc 06)

**Must read (pick 1):**

11. **AlpaServe: Statistical Multiplexing with Model Parallelism for Deep Learning Serving** — Li et al, 2023. https://arxiv.org/abs/2302.11665
    - **Why:** Best academic treatment of how to multiplex large models across requests.

12. **Modal engineering blog posts** — Erik Bernhardsson and team write very well about serverless GPU compute. Start with their "How Modal works" and "GPU autoscaling" posts.
    - **Why:** If you interview at Modal, this is required reading.

**Optional:**
- **Anyscale / Ray Serve** docs on autoscaling LLM endpoints.
- **NVIDIA Triton Inference Server** docs — what the older world looks like.

---

## Month 2, Week 7 — Cost attribution + multi-tenancy (paired with design doc 07)

**Must read (pick 1):**

13. **Anthropic — token pricing & prompt caching documentation.** Already read in W1 but **re-read with cost-attribution lens**.

14. **vLLM blog: prefix caching + how billing typically works.**
    - **Why:** Translate the engineering into the dollars.

**Optional:**
- **OpenAI cookbook — managing tokens and costs.** Practical.
- **Snowflake / Databricks documentation on FinOps for AI workloads** — enterprise framing.

---

## Month 2, Week 8 — Prompt/eval registry (paired with design doc 08)

**Must read (pick 1):**

15. **MLflow Prompts documentation.** https://mlflow.org/docs/latest/prompts/
    - **Why:** Closest production-grade pattern to a registry today.

16. **Anthropic — Versioning prompts in production** (their blog or applied AI talks).
    - **Why:** Real-world failure modes when prompts drift.

**Optional:**
- **LangSmith prompt management** docs.
- **Promptfoo or BrainTrust** docs — open evaluation tooling.

---

## Month 3 — Portfolio support (Weeks 9-12)

Reading shifts from breadth to *depth on whatever you're shipping*.

**If shipping the OpenClaw blog (Option A):**
- Re-read your own OpenClaw IEEE-style report; pull the strongest 2 graphs.
- **WebArena / VisualWebArena** papers — for benchmark grounding. https://webarena.dev/
- **Operator / Computer Use** papers from OpenAI and Anthropic — for context on what others have shipped.

**If shipping an MCP server (Option B):**
- **Anthropic MCP specification** (latest). https://modelcontextprotocol.io/specification
- **Anthropic registry submission guide** (currently called "Verified MCP servers").
- Read 2-3 existing high-quality servers in the [official servers repo](https://github.com/modelcontextprotocol/servers).

**If contributing to OSS (Option C):**
- The project's architecture doc (e.g., vLLM's `docs/source/design/`).
- The project's "good first issue" + "help wanted" labels — pick one with ≥ 10 days of recent maintainer engagement.

---

## Month 4 — Deep dive support (Weeks 13-16)

Reading targets specific gaps from your real onsites.

- **After each onsite,** identify the 1-2 topics where you wished you had more depth, and add a paper or post here.
- Re-read the most-cited paper for whatever your **next** onsite is likely to surface.
- Read each target company's **engineering blog** in full the week before their onsite. Anthropic, Cursor, Modal, OpenAI, Databricks, Sierra, Perplexity, Browserbase — most have well-curated engineering posts.

---

## Month 5 — No new reading

Stop adding new sources in Months 5. Re-read your notes from Months 1-4. Compounding > novelty.

---

## Always-on (read whenever):

These accumulate over the 5 months; check feeds weekly.

**Newsletters / feeds:**
- **Latent Space podcast/newsletter** (Swyx & Alessio) — surveys the AI eng ecosystem weekly.
- **The Pragmatic Engineer** (Gergely Orosz) — esp. AI engineering issues; some are paywalled but worth it during the search.
- **Import AI** (Jack Clark, Anthropic) — weekly digest of AI research with policy context.
- **Anthropic, OpenAI, Cursor, Modal engineering blogs** — set up RSS or check biweekly.

**Books (one is enough over 5 months):**
- **Designing Machine Learning Systems** — Chip Huyen (2022). The single best book on the operational side of ML.
- **Building LLMs for Production** — Louis-François Bouchard / Activeloop. Practical, lighter.
- **The Pragmatic Engineer's Guide to Engineering Senior+ Interviews** — Gergely Orosz. Worth it if interviewing at FAANG-tier; less relevant for AI-native shops.

**One newsletter to subscribe to:**
- Pick **one** AI-eng newsletter and read it religiously. More than one and you get noise. Latent Space is the best balance for AI-infra audience.

---

## What's deliberately not on this list

- **Generic distributed-systems papers** (Raft, Paxos, Spanner, Dynamo). You already have these in your bones from 20 years of platform work.
- **Foundational ML textbooks** (Bishop, Goodfellow). Out of scope for the AI **infra** track; if you find yourself wanting them, you've drifted from infra into research.
- **Generic interview-prep books** (Cracking the Coding Interview, Designing Data-Intensive Applications standalone read). Use the coding patterns cheat sheet and the system-design docs instead — those are tailored to your track.

---

## How to actually retain this stuff

**Per paper / post (15-30 min):**
1. Read the abstract / TL;DR. Stop if it's not aligned with what you're trying to learn.
2. Skim the figures. Most ideas are in the figures, not the prose.
3. Read sections that answer **a specific question** you had going in.
4. Write 5 bullets in your notes file:
   - What problem does it solve?
   - What's the 1-sentence approach?
   - What's the most interesting trade-off?
   - What did you not understand?
   - What would you cite this for in an interview?
5. If reading a paper deeply, write 1 paragraph of your own explanation. **If you can't, you didn't understand it.**

**Anti-pattern:** Reading the full paper linearly without a question in mind. You'll forget it in a week.
