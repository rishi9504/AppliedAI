# Day 02 — Tool Use and RAG in Production

This day connects two production loops:

```text
Tool use: user request → model chooses a tool → application validates and executes → model interprets the result
RAG: query → retrieve candidates → fuse/filter/rerank → assemble context → generate → evaluate
```

The goal is not another “chat with five PDFs” demo. By the end, you should be able to defend each retrieval and tool-execution decision, identify its failure mode, and say how you would measure it.

## Learning objectives

You should be able to explain:

- why a tool call is a model-generated proposal, not an executed function;
- how tool names, descriptions, schemas, validation, timeouts, retries, idempotency, and permissions affect reliability;
- lexical retrieval with Best Matching 25 (BM25), dense retrieval with embeddings, and Approximate Nearest Neighbor (ANN) search;
- how Hierarchical Navigable Small World (HNSW) search trades recall, memory, build time, and query latency;
- hybrid retrieval using Reciprocal Rank Fusion (RRF), followed by reranking;
- metadata filtering, chunking, deduplication with MinHash, and evaluation of each RAG stage;
- how Server-Sent Events (SSE), Amazon Simple Storage Service (S3) events, AWS Lambda, and Apache Kafka fit an asynchronous ingestion pipeline.

## Recommended sequence

### Block 1 — Production RAG mental model (60–75 minutes)

1. **Required:** [What Matters in Production RAG — Arpit Bhayani](https://arpitbhayani.me/blogs/rag-production)
2. Draw the offline ingestion path and online query path separately.
3. For every stage, write one failure and one metric.

Focus on corpus quality, parsing, chunking, metadata, indexing, retrieval, reranking, context construction, answer generation, evaluation, observability, access control, freshness, and cost. The vector database is one component, not the architecture.

### Block 2 — Retrieval foundations (90 minutes)

Read in this dependency order:

1. **Required:** [What is BM25? — Arpit Bhayani](https://arpitbhayani.me/blogs/bm25)
2. **Required:** [HNSW and vector search — Pinecone](https://www.pinecone.io/learn/series/faiss/hnsw/)
3. **Required:** [MinHash: Fast Jaccard Similarity at Scale — Arpit Bhayani](https://arpitbhayani.me/blogs/jaccard-minhash)
4. **Recommended video:** On [Arpit Bhayani's YouTube channel](https://youtube.com/c/ArpitBhayani), watch **“BM25, Embeddings, and the Power of Agentic Search.”**
5. **Reference while building:** [Sentence Transformers retrieve and rerank](https://www.sbert.net/examples/sentence_transformer/applications/retrieve_rerank/README.html)

Questions to answer:

- When will exact lexical terms beat semantic similarity?
- Which HNSW parameters affect index construction versus query-time exploration?
- Why should hybrid systems fuse ranks rather than blindly add incompatible raw scores?
- Why is a cross-encoder suitable for tens or hundreds of candidates, but not millions?
- Why is MinHash for approximate set overlap/deduplication rather than semantic retrieval?

### Block 3 — Tool calling as an application protocol (60 minutes)

1. [OpenAI function calling guide](https://developers.openai.com/api/docs/guides/function-calling)
2. [OpenAI tools guide](https://developers.openai.com/api/docs/guides/tools)
3. Revisit the Day 01 distinction between JSON-looking text and schema-constrained output.

Use this loop during revision:

1. The application declares tools and JSON schemas.
2. The model emits a tool-call request with arguments.
3. The application validates authorization, arguments, and policy.
4. The application executes the tool with timeout/error handling.
5. The application returns a structured result tied to the call identifier.
6. The model produces another tool call or the final response.

Production questions: Can the call be retried safely? Is the operation idempotent? Who is authorized? How is user confirmation obtained for a side effect? What does the model see when the tool fails? What is logged without leaking secrets?

### Block 4 — Streaming and asynchronous ingestion (60–75 minutes)

1. [Server-Sent Events — MDN](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)
2. [Amazon S3 event notifications](https://docs.aws.amazon.com/AmazonS3/latest/userguide/EventNotifications.html)
3. [Tutorial: use S3 with AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/with-s3-example.html)
4. [Apache Kafka introduction](https://kafka.apache.org/intro/)

Keep the roles separate:

- SSE streams one-way server updates to a browser; it is not the ingestion queue.
- S3 events notify downstream systems that an object changed; delivery and duplicate handling must be designed explicitly.
- Lambda can perform short event-driven work or enqueue a durable job.
- Kafka is a durable distributed event log useful when multiple consumers, replay, ordering, or sustained throughput matter.

### Block 5 — Build and measure (90–120 minutes)

Build these first using [`Codex-Answers/build-prototype.md`](../Codex-Answers/build-prototype.md):

1. `tool-schema-calibration`
2. `tool-call-error-injection`
3. `rrf`

If time remains, build `metadata-filtering`. This gives one tool-selection experiment, one execution-failure experiment, and one retrieval-quality experiment rather than a large but shallow application.

## Day 02 deliverables

- [ ] Explain tool calling end to end without saying “the model executes the function.”
- [ ] Compare BM25, dense retrieval, hybrid fusion, and cross-encoder reranking.
- [ ] Explain HNSW construction/search trade-offs and MinHash's correct scope.
- [ ] Draw the S3 → event → worker → parse/chunk/embed/index ingestion path.
- [ ] Build and test `tool-schema-calibration`.
- [ ] Build and test `tool-call-error-injection`.
- [ ] Build and test `rrf`.
- [ ] Record observations in each prototype's `RESULTS.md`.

## Optional deeper reads

- [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172)
- [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401)
- [Precise Zero-Shot Dense Retrieval without Relevance Labels (HyDE)](https://arxiv.org/abs/2212.10496)
- [OpenAI Cookbook](https://cookbook.openai.com/) — search for current embeddings, tool-calling, and evaluation examples as needed

## Five-minute revision questions

1. Why can good generation not repair a retrieval miss?
2. What does BM25 capture that embeddings may miss?
3. What does HNSW approximate, and what is sacrificed for speed?
4. Why does RRF avoid score calibration?
5. Where does a cross-encoder sit in the pipeline?
6. What does MinHash estimate?
7. Who validates and executes a tool call?
8. What should happen after a tool timeout or malformed arguments?
9. When is SSE appropriate, and when is Kafka appropriate?
10. Which metric tells you whether the answer is supported by retrieved context?
