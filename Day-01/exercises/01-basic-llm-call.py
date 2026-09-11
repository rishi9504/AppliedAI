"""Python -> messages -> API -> response -> application output."""

from openai import APIError, OpenAI
from settings import MODEL, key_available, report_api_error


def main():
    if not key_available("01-basic-llm-call.py"):
        return
    client = OpenAI()
    messages = [
        # System: application instructions that guide the model's behavior.
        {"role": "system", "content": "Explain concepts simply in two sentences."},
        # User: the actual request to answer.
        {"role": "user", "content": "What happens during one LLM API call?"},
    ]
    # The SDK sends these messages and parameters to the remote model service.
    response = client.responses.create(model=MODEL, input=messages)
    # The response includes assistant output plus metadata (ID, usage, status).
    # output_text collects the assistant's text; it is not the whole response.
    print("Assistant:", response.output_text or "[No text returned]")
    print("Status:", response.status)
    print("Token usage:", response.usage)


if __name__ == "__main__":
    try:
        main()
    except APIError as error:
        report_api_error(error)
