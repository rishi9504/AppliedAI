"""A natural-language JSON request without API-level format constraints."""

import json
from openai import APIError, OpenAI
from pydantic import ValidationError
from settings import MODEL, key_available, report_api_error
from travel_schema import TRIP_REQUEST, TravelPlan


def parse_and_validate(raw):
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as error:
        print(f"JSON parsing failed: {error.msg}. The model did not return valid JSON.")
        return
    print("JSON syntax parsed successfully.")
    try:
        plan = TravelPlan.model_validate(data)
    except ValidationError as error:
        print("Valid JSON, but wrong schema:", error)
        return
    print("Pydantic validation passed:", plan.model_dump_json(indent=2))


def main():
    if not key_available("04a-prompt-only-json.py"):
        return
    client = OpenAI()
    response = client.responses.create(
        model=MODEL,
        input=[
            {"role": "system", "content": "Return only JSON with destination (string), trip_duration_days (integer), budget_category (string), top_attractions (list of strings), daily_plan (list of objects with day as integer and activities as list of strings)."},
            {"role": "user", "content": TRIP_REQUEST},
        ],
    )  # No JSON mode or schema constraint: success relies on instruction following.
    print("Raw response:", response.output_text)
    parse_and_validate(response.output_text)


if __name__ == "__main__":
    try:
        main()
    except APIError as error:
        report_api_error(error)
