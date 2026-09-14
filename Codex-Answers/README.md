# Codex Answers — Prototype Builder

This folder contains reusable prompts for asking Codex or another coding assistant to build a prototype. The goal is not hand-copying Arpit's implementation. The assistant should recreate the learning experiment using the conventions of this repository, explain the important choices, and leave behind a runnable revision artifact.

## How to use

1. Open [`build-prototype.md`](build-prototype.md).
2. Replace `<prototype-name>` with a name from [`PROTOTYPE-TODO.md`](../PROTOTYPE-TODO.md).
3. Optionally add a short constraint, such as `keep all retrieval local`.
4. Run the prompt from the root of this repository.
5. Review the plan if the assistant asks for an external service. Never paste a secret into chat or source code; put it only in the ignored `.env` file.

Example request:

```text
Use Codex-Answers/build-prototype.md to build the tool-schema-calibration prototype.
Keep tools local and use OPENAI_API_KEY for model calls.
```

## Session 2 quick prompts

These are ready to append to the master prompt:

| Prototype | Extra instruction |
|---|---|
| `tool-schema-calibration` | Use at least 30 labeled routing queries and report loose-schema versus precise-schema accuracy. |
| `tool-call-error-injection` | Use a deterministic fake weather tool that returns a 503-style error on a known call. |
| `react` | Use local search fixtures and report model calls, input/output tokens, tool calls, and context growth by step. |
| `rrf` | Implement lexical and dense rank inputs plus RRF from first principles; no hosted vector database. |
| `metadata-filtering` | Use documents with deliberately confusing year, quarter, and department metadata. |
| `cross-encoders` | Default to local open-source embedding/reranking models; ask before downloading a large model. |
| `rag-chunking-strategy` | Compare fixed, semantic, and parent-child chunks against the same queries and metrics. |
| `rag-failure-modes` | Create independently reproducible retrieval, ranking/context-placement, and generation failures. |
| `query-rewrite-hyde` | Compare raw query, rewritten query, and HyDE retrieval over the same corpus. |

## Important naming

The credential is an **OpenAI API key**, stored as `OPENAI_API_KEY`. “OpenAPI” is a specification for describing HTTP APIs and is not the credential used here.
