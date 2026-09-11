"""Repeat an identical input; each request starts a fresh conversation."""

from collections import Counter
from openai import APIError, OpenAI
from settings import MODEL, key_available, report_api_error

RUNS = 10
TEMPERATURE = 1.0  # Try 0, 0.5, 1, 1.5. Support depends on the model.


def main():
    if not key_available("02-stochasticity.py"):
        return
    client = OpenAI()
    messages = [
        {"role": "system", "content": "Classify the ticket. Return exactly one label: billing, authentication, account_access, unknown."},
        {"role": "user", "content": "My payment went through but my account is still locked."},
    ]
    outputs = []
    for run in range(RUNS):
        response = client.responses.create(
            model=MODEL, input=messages, temperature=TEMPERATURE,
        )
        label = response.output_text.strip() or "[empty]"
        outputs.append(label)
        print(f"{run + 1:2}: {label!r}")
    print("\nCounts (unexpected outputs remain visible):")
    for label, count in Counter(outputs).most_common():
        print(f"{label}: {count}")
    print("Identical results are possible. A small sample does not prove determinism.")
    print("Temperature changes token sampling; even temperature 0 is not a guarantee of determinism.")


if __name__ == "__main__":
    try:
        main()
    except APIError as error:
        report_api_error(error)
