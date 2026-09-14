# Applied AI Prototype TODO

Reference: [Arpit Bhayani's `prototypes-ai`](https://github.com/arpitbbhayani/prototypes-ai)

Last compared: 14 September 2026. Arpit's root README says 24 prototypes, but the repository currently contains **37 prototype directories**. This tracker follows the repository, not the stale headline count.

## Current score

| Measure | Count |
|---|---:|
| Reference prototype directories | 37 |
| Complete equivalents in this repository | 0 |
| Partial equivalents | 2 |
| Runnable Day 01 learning exercises | 4 |
| Reference prototypes remaining | 35 complete + 2 to finish |

`Day-01/exercises/02-stochasticity.py` plus the two JSON exercises partially cover `non-deterministic`. `Day-01/exercises/03-prompt-quality.py` partially covers the experiment shape behind `prompt-regression`, but neither is yet a faithful, tested equivalent of Arpit's prototype. Notes do not count as completed prototypes.

## Status legend

- `[ ]` Not started
- `[~]` Partially implemented in this repository
- `[x]` Complete, runnable, documented, and tested

## 1. Model behaviour and prompting

- [~] `non-deterministic` — variance and constrained output; finish with repeatable metrics and a comparison report
- [ ] `cot-vs-direct` — direct answer versus explicit reasoning benchmark
- [ ] `cot-vs-few-vs-direct` — direct, zero-shot reasoning, and few-shot reasoning trade-offs
- [ ] `sycophancy` — measure agreement with a planted incorrect assertion
- [ ] `critic-refiner` — compare iterative refinement with and without a rubric
- [~] `prompt-regression` — turn the Day 01 classification experiment into a regression suite
- [ ] `prompt-caching` — demonstrate latency and token-cost effects of cached prefixes

## 2. Tool use and agent loops

- [ ] `tool-schema-calibration` — measure tool-selection accuracy for vague versus precise schemas
- [ ] `tool-call-error-injection` — surface a simulated downstream tool failure instead of hiding or hallucinating
- [ ] `react` — Reasoning and Acting loop plus token-growth measurement
- [ ] `observe-think-act-loop` — observe an error, propose an action, execute, and repeat
- [ ] `hitl` — Human in the Loop approval before a sensitive action
- [ ] `checkpoint-replay` — persist and resume an interrupted agent session
- [ ] `code-patcher` — generate and safely apply a code patch
- [ ] `self-evolving-agent` — one-time code execution versus reusable tool registration
- [ ] `skill-executor` — typed multi-step skill with validation and correction at each boundary
- [ ] `grep_search` — codebase search tool behaviour

## 3. Retrieval-Augmented Generation and search

- [ ] `metadata-filtering` — extract hard filters before semantic retrieval
- [ ] `rrf` — Reciprocal Rank Fusion (RRF) over lexical and semantic rankings
- [ ] `rrf-viz` — interactive visualization of RRF ranks and the smoothing constant
- [ ] `cross-encoders` — bi-encoder retrieval followed by cross-encoder reranking
- [ ] `query-rewrite-hyde` — query rewriting and Hypothetical Document Embeddings (HyDE)
- [ ] `rag-chunking-strategy` — fixed, semantic, and parent-child chunking with evaluation
- [ ] `rag-failure-modes` — retrieval miss, lost-in-the-middle, and faithfulness failures

## 4. Memory

- [ ] `working-memory` — eviction versus summarization versus external retrieval
- [ ] `memory-persistent` — explicit memory write and retrieval across sessions
- [ ] `evolving-memory` — update and consolidate stored knowledge over time

## 5. Multi-agent systems

- [ ] `orchestrator-vs-specialist` — routing to specialist agents versus a generalist
- [ ] `deadlock` — detect and stop circular hand-offs
- [ ] `deep-research` — plan, parallel research, synthesize, and quality-check
- [ ] `agent-paper-to-code-2` — paper ingestion, implementation, execution, and repair
- [ ] `agent-paper-to-code-3` — later paper-to-code iteration; compare its design delta with version 2

## 6. Evaluation and observability

- [ ] `evals` — dataset-driven output evaluation
- [ ] `observability` — traces, spans, token usage, latency, cost attribution, and budgets

## 7. Security and resilience

- [ ] `prompt-injection` — distinguish instructions from untrusted retrieved content
- [ ] `system-prompt-leak` — demonstrate leakage risk and defenses safely
- [ ] `token-smuggling` — show why keyword-only filters are insufficient using benign fixtures

## Definition of done

A checkbox becomes `[x]` only when the prototype has:

1. its own folder under `prototypes/<name>/`;
2. a README explaining the intuition, architecture, trade-offs, and expected observations;
3. runnable Python using `OPENAI_API_KEY` through the official OpenAI SDK when an LLM is needed;
4. deterministic local fixtures or a clearly labeled external dependency;
5. automated tests that do not require paid API calls by default;
6. `.env.example` updates without committed secrets;
7. commands that were actually run and verified;
8. a short `RESULTS.md` recording what the experiment demonstrated.

## Recommended build order

For Session 2, build in this order:

1. `tool-schema-calibration`
2. `tool-call-error-injection`
3. `react`
4. `rrf`
5. `metadata-filtering`
6. `cross-encoders`
7. `rag-chunking-strategy`
8. `rag-failure-modes`
9. `query-rewrite-hyde`

Then return to the remaining prompting prototypes before memory and multi-agent systems.
