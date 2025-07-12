from typing import List
from openai import OpenAI

from openai.types.chat.chat_completion import ChatCompletion
from openai.types.embedding import Embedding


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
    def invoke_model(
        user_prompt: str, system_prompt: str | None = None
    ) -> ChatCompletion:
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": user_prompt})
        response = _client.chat.completions.create(
            messages=messages,
            model=settings.openai_chat_model,
            temperature=settings.openai_temperature,
        )
        return response
