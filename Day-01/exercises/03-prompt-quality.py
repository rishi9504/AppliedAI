"""Compare four prompts against the same small, inspectable evaluation set."""

from openai import APIError, OpenAI
from settings import MODEL, key_available, report_api_error

INSTRUCTION = "Classify the ticket. Return exactly one label: billing, authentication, account_access, unknown."
DEFINITIONS = """
billing: charges, refunds, invoices, or payment-method problems.
authentication: identity verification, passwords, sign-in codes, or MFA.
account_access: locked/suspended accounts or missing permissions/entitlements.
unknown: insufficient information or none of the above.
"""
EXAMPLES = [
    ("Please send a receipt for last month.", "billing"),
    ("My password reset link is invalid.", "authentication"),
    ("My profile was suspended by an administrator.", "account_access"),
    ("I need some help.", "unknown"),
]
RULES = """
Use the explicitly described blocker, not just a keyword.
If payment succeeded but access is blocked, choose account_access.
If payment failed (including an expired card), choose billing even if access is affected.
An explicit password/MFA/verification failure takes priority over a generic access complaint.
If no cause is given but the account is explicitly locked, choose account_access.
If separate issues remain tied, prioritize authentication, then billing, then account_access.
If no specific issue is described, choose unknown. Do not invent a cause.
"""
# Expected labels express this exercise's routing policy, not universal truth.
# These cases are separate from the few-shot examples, but are a tiny teaching set.
CASES = [
    ("I was charged twice for my subscription.", "billing"),
    ("My password is rejected when I sign in.", "authentication"),
    ("I can sign in but do not have permission to open my workspace.", "account_access"),
    ("My payment went through but my account is still locked.", "account_access"),
    ("The MFA code never arrives.", "authentication"),
    ("My card expired and renewal failed.", "billing"),
    ("Nothing works. Fix it.", "unknown"),
    ("My account is locked and my MFA code is rejected.", "authentication"),
    ("My payment failed and now I cannot access premium features.", "billing"),
    ("I can log in, but my paid plan features are missing.", "account_access"),
    ("I need a refund and my password is also rejected.", "authentication"),
    ("My account is locked. I do not know why.", "account_access"),
]


def prompt_messages(version, ticket):
    system = INSTRUCTION
    if version >= 2:
        system += DEFINITIONS
    if version == 4:
        system += RULES
    messages = [{"role": "system", "content": system}]
    if version >= 3:
        for example, label in EXAMPLES:
            messages.extend([
                {"role": "user", "content": example},
                # Assistant messages demonstrate desired answers, not new instructions.
                {"role": "assistant", "content": label},
            ])
    messages.append({"role": "user", "content": ticket})
    return messages


def main():
    if not key_available("03-prompt-quality.py"):
        return
    client = OpenAI()
    correct = [0] * 4
    print("Input | Expected | V1 | V2 | V3 | V4", flush=True)
    for ticket, expected in CASES:
        outputs = []
        for version in range(1, 5):
            response = client.responses.create(
                model=MODEL, input=prompt_messages(version, ticket), temperature=0,
            )
            label = response.output_text.strip()
            outputs.append(label)
            correct[version - 1] += label == expected
        print(" | ".join([ticket, expected] + [repr(x) for x in outputs]), flush=True)
    for version, count in enumerate(correct, 1):
        print(f"V{version}: {count}/{len(CASES)} = {count / len(CASES):.1%}")
    print("Exact-label scoring: extra prose counts as wrong. V4 need not win.")
    print("Small policy-specific dataset: repeat runs and evaluate new cases before generalizing.")


if __name__ == "__main__":
    try:
        main()
    except APIError as error:
        report_api_error(error)
