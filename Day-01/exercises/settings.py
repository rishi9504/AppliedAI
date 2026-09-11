"""Shared setup only: API calls stay visible in each exercise."""

import os
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[2]
load_dotenv(ROOT / ".env")  # Existing shell variables take precedence.
MODEL = "gpt-4.1-mini"


def key_available(script):
    key = os.getenv("OPENAI_API_KEY", "").strip()
    if not key or key == "your_key_here":
        print(f"Add your OpenAI API key to `.env`, then run: python Day-01/exercises/{script}")
        return False
    return True


def report_api_error(error):
    # Avoid printing server error bodies, which can contain credential fragments.
    print(f"API request failed ({type(error).__name__}). Check your key, model access, quota, and connection.")
