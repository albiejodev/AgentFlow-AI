import os

from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv(
    "OPENAI_API_KEY"
)

GOOGLE_API_KEY = os.getenv(
    "GOOGLE_API_KEY"
)

LLM_PROVIDER = os.getenv(
    "LLM_PROVIDER",
    "gemini"
)

OPENAI_MODEL = os.getenv(
    "OPENAI_MODEL",
    "gpt-4.1-mini"
)

GEMINI_MODEL = os.getenv(
    "GEMINI_MODEL",
    "gemini-2.5-flash"
)