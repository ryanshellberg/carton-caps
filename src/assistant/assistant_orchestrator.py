from typing import Tuple
from assistant.context_manager import ContextManager
from clients.openai_client import OpenAIClient
from request.messages.message import Message

SYSTEM_PROMPT = """Carton Caps is an app that empowers consumers to raise money for the schools they care about while buying the everyday products they love.
Features of the app include assistance finding products that can support the user's local school and a referral program that allows you to invite your friends to join the Carton Caps app. 
You are a helpful chatbot that users will interact with for help in navigating the Carton Caps app. 
Your responses should be narrowly constrained to be relevant to this purpose, and any irrelevant questions can be answered with "I'm here to help with Carton Caps—try asking about referrals or products."
"""


class AssistantOrchestrator:
    @staticmethod
    def get_response(
        message: Message, latest_response_id: str | None
    ) -> Tuple[str, str]:
        context = ContextManager.get_context_for_response(message)

        context_prompt = f"""Provided below is relevant informational content found in the Carton Caps database. 
Limit the scope of your response to this context. If there's no relevant information or the question can't be answered confidently, respond with: I'm not totally sure, please try another question.
{context}
"""

        prompt = f"""{context_prompt}
Response to the following user message: {message.user_text}
"""

        response = OpenAIClient.get_response(
            prompt, system_prompt=SYSTEM_PROMPT, previous_response_id=latest_response_id
        )
        response_text = response.output_text
        response_id = response.id
        return response_text, response_id
