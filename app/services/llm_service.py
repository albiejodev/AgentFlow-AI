from app.config import (
    LLM_PROVIDER
)

from app.services.openai_service import (
    OpenAIService
)

from app.services.gemini_service import (
    GeminiService
)


class LLMService:

    @staticmethod
    def generate(
        prompt: str
    ):

        if LLM_PROVIDER == "openai":
            return OpenAIService.generate_response(
                prompt
            )

        if LLM_PROVIDER == "gemini":
            return GeminiService.generate_response(
                prompt
            )

        raise ValueError(
            f"Unsupported provider: {LLM_PROVIDER}"
        )