"""Application-level schema constraints plus SDK Pydantic parsing."""

from openai import APIError, OpenAI
from pydantic import ValidationError
from settings import MODEL, key_available, report_api_error
from travel_schema import TRIP_REQUEST, TravelPlan


def main():
    if not key_available("04b-structured-output.py"):
        return
    client = OpenAI()
    # Unlike 'please return JSON', text_format supplies an actual schema to
    # the API. The SDK parses the response into a validated Pydantic object.
    response = client.responses.parse(
        model=MODEL,
        input=[
            {"role": "system", "content": "You are a helpful travel planner."},
            {"role": "user", "content": TRIP_REQUEST},
        ],
        text_format=TravelPlan,
    )
    # Refusals and incomplete responses are not successful schema results.
    if response.status != "completed":
        print("Response did not complete:", response.status)
        return
    for item in response.output:
        for content in getattr(item, "content", []):
            if content.type == "refusal":
                print("Model refused:", content.refusal)
                return
    plan = response.output_parsed
    if plan is None:
        print("No parsed itinerary returned.")
        return
    print(plan.model_dump_json(indent=2))
    # Schema correctness != factual correctness: Pydantic checks shape/types,
    # not whether attractions exist, are open, or fit the claimed budget.
    # Cross-field rules also require separate checks beyond this basic schema.
    if len(plan.daily_plan) != plan.trip_duration_days:
        print("Application check: daily plan length differs from trip duration.")
    print("Schema validated. Independently verify attractions, hours, prices, and feasibility.")


if __name__ == "__main__":
    try:
        main()
    except APIError as error:
        report_api_error(error)
    except ValidationError as error:
        print("Schema validation failed:", error)
