from datetime import datetime, timezone
from uuid import uuid4

from assistant.assistant_orchestrator import AssistantOrchestrator
from request.messages.message import Message


def test_populate_response(mocker):
    message = Message(
        id=uuid4(),
        chat_id=uuid4(),
        user_text="Some message.",
        created_at=datetime.now(timezone.utc),
        is_terminal=False,
    )

    mock_context = "some context"
    mocker.patch(
        "assistant.context_manager.ContextManager.get_context_for_response",
        return_value=mock_context,
    )

    response_text = "mock_response"
    # Create a mock OpenAI response structure
    mock_openai_response = mocker.Mock()
    mock_choice = mocker.Mock()
    mock_message = mocker.Mock()
    mock_message.content = response_text
    mock_choice.message = mock_message
    mock_openai_response.choices = [mock_choice]

    mocker.patch(
        "clients.openai_client.OpenAIClient.invoke_model",
        return_value=mock_openai_response,
    )

    assert message.response_text is None
    AssistantOrchestrator.populate_response(message)
    assert message.response_text == response_text
