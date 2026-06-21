from google import genai

from app.config import (
    GOOGLE_API_KEY,
    GEMINI_MODEL
)


class GeminiService:

    client = genai.Client(
        api_key=GOOGLE_API_KEY
    )

    @classmethod
    def generate_response(
        cls,
        prompt: str
    ):

        response = cls.client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt,
        )

        return response.text