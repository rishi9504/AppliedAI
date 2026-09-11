# 4 — Five-Minute Revision Sheet

## One-sentence model

An application serializes messages into tokens; a Transformer repeatedly predicts next-token probabilities; a decoder selects tokens; the application validates the result and executes any real-world actions.

## Flashcards

**Q: What does an LLM predict?**  
A: A probability distribution over the next token.

**Q: Why can identical prompts diverge?**  
A: Sampling can choose a different early token, changing all later contexts and distributions.

**Q: What does temperature do?**  
A: It sharpens or flattens the next-token distribution before sampling.

**Q: What does temperature not do?**  
A: It does not add knowledge, reasoning capacity, context, or factual verification.

**Q: What is the context window?**  
A: The maximum active token budget for instructions, history, retrieved content, tools, and output—not permanent memory.

**Q: Why do message roles matter?**  
A: They encode conversation structure and instruction priority before serialization.

**Q: Why is “return JSON” weak?**  
A: It is only a natural-language request and does not prevent structurally invalid output.

**Q: What does a schema guarantee?**  
A: Supported structural constraints such as required fields and types—not factual correctness.

**Q: Does the model execute tools?**  
A: No. It proposes a call; the application validates and executes it.

**Q: What is prefill?**  
A: Processing the input tokens to build representations and the Key–Value (KV) cache before output decoding.

**Q: What is autoregressive generation?**  
A: Append one selected token and predict the next, repeatedly.

**Q: What is the first debugging question for Retrieval-Augmented Generation (RAG)?**  
A: Did the correct evidence reach the model?

## Three equations or inequalities to remember

```text
probable text ≠ verified truth
valid JSON ≠ correct answer
model output ≠ authorized application action
```

## 60-second interview answer

“The application sends messages, parameters, and optional tool or schema definitions. The serving layer applies a model-specific chat template, tokenizes the serialized input, and runs a Transformer prefill that builds a KV cache. The model produces logits for the next token, which become probabilities. A decoding strategy—possibly temperature sampling or schema-constrained decoding—selects one token. That token is appended and the process repeats autoregressively. The service detokenizes the output, but the application still owns validation, tool execution, authorization, and error handling. This is why valid formatting, sound reasoning, factual grounding, and successful integration must be evaluated separately.”

## Final recall drill

Without looking back, draw:

1. the full single-call pipeline;
2. the tool-calling sequence;
3. the nine-part failure taxonomy;
4. the boundary between structural validity and factual truth.

