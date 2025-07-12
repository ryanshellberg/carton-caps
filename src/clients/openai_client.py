from typing import List
from openai import OpenAI

from openai.types.embedding import Embedding
from openai.types.responses import Response


from config import settings

_client = OpenAI(api_key=settings.openai_api_key)


class OpenAIClient:
    @staticmethod
    def get_embeddings(text) -> List[Embedding]:
        response = _client.embeddings.create(
            model=settings.openai_embedding_model, input=text
        )

        return response.data

    @staticmethod
    def get_response(
        user_prompt: str,
        system_prompt: str | None = None,
        previous_response_id: str | None = None,
    ) -> Response:
        print(previous_response_id)
        response = _client.responses.create(
            model=settings.openai_chat_model,
            temperature=settings.openai_temperature,
            input=user_prompt,
            instructions=system_prompt,
            previous_response_id=previous_response_id,
        )
        return response
