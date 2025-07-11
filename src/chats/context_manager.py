from services.knowledge_base_service import KnowledgeBaseService
from clients.openai_client import OpenAIClient
from request.messages.message import Message


class ContextManager:
    @staticmethod
    def get_context_for_response(message: Message) -> str:
        # Get relevant information from the knowledge base.
        # Get relevant user information.
        user_text_embedding = OpenAIClient.get_embeddings(message.user_text)
        relevant_document_texts = KnowledgeBaseService.get_matching_documents(
            user_text_embedding
        )
        all_document_text = "\n".join(relevant_document_texts)

        user_context = "Purchase history: 5 eggs."

        all_context = f"""USER_CONTEXT:
```
{user_context}
```

RELEVANT_DOCUMENT_CONTEXT:
```
{all_document_text}
```
"""

        return all_context
