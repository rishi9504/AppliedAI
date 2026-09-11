# Exercise 5: Locate the failure

| Failure | Simple example | Failed layer | One mitigation |
|---|---|---|---|
| Instruction | Asked for one label; returns a paragraph | Model instruction following | Give explicit output rules and evaluate adherence |
| Reasoning | Given 3 days at 100 per day; computes 200 | Model reasoning over available facts | Calculate totals in Python |
| Knowledge | Uses outdated museum opening hours | Model knowledge / supplied context | Supply current authoritative opening hours |
| Format/schema | Returns valid JSON without `daily_plan` | Output contract | Use structured output and Pydantic validation |
| Hallucination | Invents a museum and presents it as real | Unsupported generated claims | Verify attractions against trusted sources |
| Application/integration | Python reads `days` instead of `daily_plan` | Application consuming the response | Use the validated object's defined field names |

These categories can overlap. An API timeout or missing key is also an integration
issue, not evidence of bad reasoning. Valid JSON can have the wrong fields;
a valid schema can contain false facts. The simple travel schema does not enforce
positive durations, unique sequential days, or matching duration and plan length.
Those need application checks or additional validation.

Read the existing [failure notes](../03-llm-system-failures.md) for the broader taxonomy.

Think about:

1. Which failure could Python prevent without another model call?
2. Which failures could remain after a successful Pydantic validation?
3. Could one bad itinerary involve several layers at once?
