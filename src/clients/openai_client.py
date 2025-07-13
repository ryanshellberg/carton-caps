from typing import List
from openai import OpenAI

from openai.types.embedding import Embedding
from openai.types.responses import Response


from config import settings

_client = OpenAI(api_key=settings.openai_api_key)


class OpenAIClient:
    @staticmethod
    def get_embeddings(text: str) -> List[Embedding]:
        """Generates embeddings for text.

        Args:
            text: The string to get embeddings for.

        Returns:
            A list of Embedding objects.
        """
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
        """Call's the set OpenAI model using the Responses API.

        Args:
            user_prompt: The message to send to the model.
            system_prompt: Additional instructions for the model to follow.
            previous_response_id: The ID of the most recent Response in this chat session.

        Returns:
            The Response object from the OpenAI SDK.
        """
        response = _client.responses.create(
            model=settings.openai_chat_model,
            temperature=settings.openai_temperature,
            input=user_prompt,
            instructions=system_prompt,
            previous_response_id=previous_response_id,
        )
        return response
