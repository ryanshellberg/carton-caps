from datetime import datetime, timezone
from uuid import uuid4

from assistant.assistant_orchestrator import AssistantOrchestrator
from request.messages.message import Message


def test_populate_response(mocker):
    latest_response_id = "some-response-id"
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

    expected_response_text = "mock_response"
    expected_response_id = "some-new-id"
    mock_openai_response = mocker.Mock()
    mock_openai_response.output_text = expected_response_text
    mock_openai_response.id = expected_response_id

    mocker.patch(
        "clients.openai_client.OpenAIClient.get_response",
        return_value=mock_openai_response,
    )

    actual_response_text, actual_response_id = AssistantOrchestrator.get_response(
        message, latest_response_id
    )
    assert actual_response_text == expected_response_text
    assert actual_response_id == expected_response_id
