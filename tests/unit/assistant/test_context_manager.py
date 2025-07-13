from datetime import datetime, timezone
from uuid import uuid4
from assistant.context_manager import ContextManager
from request.messages.message import Message


def test_get_context_for_response(mocker):
    message = Message(
        id=uuid4(),
        chat_id=uuid4(),
        user_text="Some message.",
        created_at=datetime.now(timezone.utc),
        is_terminal=False,
    )

    mock_embeddings = [mocker.Mock()]
    mock_documents = ["mock document content"]

    mocker.patch(
        "clients.openai_client.OpenAIClient.get_embeddings",
        return_value=mock_embeddings,
    )
    mocker.patch(
        "services.knowledge_base_service.KnowledgeBaseService.get_matching_documents",
        return_value=mock_documents,
    )

    context = ContextManager.get_context_for_response(message)

    assert mock_documents[0] in context
    assert "5 eggs" in context
