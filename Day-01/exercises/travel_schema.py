"""Shared itinerary contract for the two parts of exercise 4."""

from pydantic import BaseModel, ConfigDict


class DayPlan(BaseModel):
    model_config = ConfigDict(extra="forbid")
    day: int
    activities: list[str]


class TravelPlan(BaseModel):
    model_config = ConfigDict(extra="forbid")
    destination: str
    trip_duration_days: int
    budget_category: str
    top_attractions: list[str]
    daily_plan: list[DayPlan]


TRIP_REQUEST = "Plan a three-day budget trip to Jaipur, India."
