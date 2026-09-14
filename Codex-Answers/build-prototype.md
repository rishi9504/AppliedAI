# Prompt: Build `<prototype-name>`

You are working inside the `rishi9504/AppliedAI` repository. Build the prototype named `<prototype-name>` from the tracker in `PROTOTYPE-TODO.md`.

Use `https://github.com/arpitbbhayani/prototypes-ai/tree/master/<prototype-name>` only to understand the experiment and learning objective. Do not mechanically copy its implementation. Recreate it in the style of this repository, using OpenAI where a language model is actually necessary.

## Required workflow

1. Read the repository root README, `.gitignore`, `.env.example`, `PROTOTYPE-TODO.md`, and relevant existing Day folders before editing.
2. Inspect the named reference prototype's README and source. State its hypothesis, independent variable, dependent metrics, and expected observation.
3. Propose a compact implementation plan. Continue autonomously when only local Python packages and `OPENAI_API_KEY` are required.
4. If the design genuinely needs any other credential, hosted database, cloud account, paid API, downloadable large model, Docker daemon, or system service, stop before adding that dependency. Ask me whether to use it and offer a local/fake alternative with the trade-off. Do not silently substitute a service.
5. Create `prototypes/<prototype-name>/` with:
   - `README.md` — intuition, experiment design, architecture, setup, commands, expected output, production lessons, limitations;
   - typed, modular Python source rather than one giant script;
   - `tests/` with unit tests and deterministic fakes;
   - `requirements.txt` only when prototype-specific dependencies are necessary;
   - `RESULTS.md` with the verified local result and placeholders for API-backed observations that were not run.
6. Use Python 3.10+ and the official OpenAI Python SDK. Prefer the Responses API and current structured-output/tool-calling interfaces. Load `OPENAI_API_KEY` from the root `.env` via `python-dotenv`. Never print the key, hard-code it, add a real `.env`, or commit secrets.
7. Make the default test suite free: mock model responses or isolate pure functions so tests do not call an API. Put live API execution behind an explicit command or flag, show the estimated number of calls, and fail with a clear setup message when `OPENAI_API_KEY` is absent.
8. Prefer local deterministic fixtures for tools, search corpora, errors, and evaluation labels. Add retries only for transient failures, with bounded attempts, timeouts, and visible errors. Validate tool arguments and model outputs at application boundaries.
9. Capture relevant experiment measurements: correctness, latency, token usage, approximate cost when pricing is explicitly configured, tool-call count, failure count, and the prototype-specific metric. Do not invent results.
10. Update `PROTOTYPE-TODO.md` only after verification. Mark `[x]` when the definition of done is met; otherwise leave `[~]` and list the remaining gap. Update the root README only if a new navigation link is needed.
11. Run formatting/linting if already configured, then run the prototype's tests and at least one safe local execution. Report exact commands, results, changed files, assumptions, and anything not executed.

## Engineering constraints

- Keep the prototype small enough to revise in roughly 30 minutes.
- Explain abbreviations in full on first use.
- Separate orchestration, tools/retrieval, schemas, and evaluation when the prototype has those concerns.
- Avoid framework abstraction unless it teaches something essential; start with the OpenAI SDK and plain Python.
- Keep unsafe security demonstrations benign and sandboxed. Do not implement real credential theft, destructive execution, or bypass instructions aimed at third-party systems.
- Preserve unrelated user changes and never overwrite completed work.

Start by telling me the experiment you are about to build and whether it requires anything beyond local Python packages and `OPENAI_API_KEY`.
