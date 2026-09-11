# 2 — Six Questions That Explain LLM Behaviour

## 1. Why can the same prompt produce different answers?

The model returns a probability distribution over the next token. When decoding samples from that distribution, different valid candidates may be selected.

```text
same prompt
  → similar next-token distribution
  → a different token is sampled
  → the context is now different
  → later distributions differ
  → answers diverge
```

Temperature zero usually means choosing the highest-probability token, not making the model certain or correct. Perfect reproducibility may still be affected by provider infrastructure, batching, numerical behavior, backend changes, or model updates.

## 2. What does temperature influence?

Temperature reshapes the token distribution before selection.

Given logits \(z_i\) and temperature \(T\):

$$
p_i = \frac{e^{z_i/T}}{\sum_j e^{z_j/T}}
$$

- Lower \(T\): sharper distribution; favors top candidates.
- Higher \(T\): flatter distribution; gives weaker candidates more chance.

Temperature does **not** directly change the model’s knowledge, context-window size, parameters, training data, or reasoning capacity. Lower temperature can make an answer more consistent while leaving it consistently wrong.

## 3. What is the context window?

The context window is the maximum number of tokens the model can actively process in one request. It may include:

- system and developer instructions;
- conversation history;
- the current user message;
- retrieved documents;
- memory inserted by the application;
- tool definitions and tool results;
- generated output, depending on the API’s accounting.

It is **working context**, not permanent memory and not the training corpus. If relevant information is absent, truncated, badly retrieved, or buried in noise, a large nominal context window does not solve the problem.

## 4. What do system, user, and assistant roles mean?

| Role | Purpose | Example |
|---|---|---|
| System/developer | Defines behavior, constraints, and operating context | “Never expose secrets.” |
| User | Supplies the current request or data | “Summarize this policy.” |
| Assistant | Represents prior model responses and the next response position | “Here is the summary…” |

The roles establish instruction hierarchy and conversational structure before serialization. They are not equally authoritative. A user message should not override a higher-priority safety or application rule.

## 5. Why is “return JSON” weaker than schema-constrained output?

“Return JSON” is a natural-language instruction. The model may return prose, malformed syntax, missing fields, wrong types, extra keys, or inconsistent field names.

A schema can constrain the allowed **shape**:

```json
{
  "type": "object",
  "properties": {
    "eligible": {"type": "boolean"},
    "reason": {"type": "string"}
  },
  "required": ["eligible", "reason"],
  "additionalProperties": false
}
```

With constrained decoding, invalid structural continuations can be disallowed during generation. This is stronger than hoping an instruction is followed.

Schema constraints provide **syntactic and structural guarantees**, not semantic truth.

## 6. Why can valid output still be factually wrong?

Format correctness and factual correctness are independent dimensions.

```json
{
  "capital": "Sydney"
}
```

This is valid JSON and may perfectly satisfy a schema, yet the fact is wrong.

An LLM optimizes plausible next-token prediction. A schema validates structure. Neither automatically verifies the claim against a trusted source.

For grounded correctness, the application may need:

- authoritative retrieval;
- source citations;
- tool lookups;
- business-rule validation;
- claim verification;
- refusal when evidence is insufficient.

## Compact comparison

| Concern | Mechanism | What it guarantees | What it does not guarantee |
|---|---|---|---|
| Temperature | Reshapes sampling probabilities | Degree of output variation | Truth |
| Context window | Holds active tokens | Maximum active input/output capacity | Relevant recall or permanent memory |
| Message roles | Establish hierarchy and turns | Instruction organization | Perfect obedience |
| JSON instruction | Requests a format in prose | Nothing strict | Parseability or schema compliance |
| Schema constraint | Restricts output structure | Valid shape and types, within supported constraints | Correct facts |
| Grounding | Supplies trusted evidence | Better evidential basis | Perfect reasoning or use of evidence |

## Check yourself

1. Can temperature zero still produce a false answer? Why?
2. Does a 1-million-token context window mean the model remembers previous sessions?
3. If JSON parses successfully, what important dimensions can still fail?
4. What does constrained decoding change during generation?
5. What extra mechanism would you add before trusting a factual field?

