import json
from integration.clients.carton_caps_client import CartonCapsClient


def test_send_relevant_message():
    current_chat_response = CartonCapsClient.get_current_chat()
    current_chat_json = json.loads(current_chat_response.text)
    chat_id = current_chat_json["id"]

    message_text = "How do I refer a friend?"
    message_response = CartonCapsClient.create_message(chat_id, message_text)
    message_response_json = json.loads(message_response.text)

    assert message_response_json["chat_id"] == chat_id
    assert message_response_json["user_text"] == message_text
    assert message_response_json["moderation_code"] is None
    assert not message_response_json["is_terminal"]

    response_text = message_response_json["response_text"]
    assert "try asking about" not in response_text
    assert "refer a friend" in response_text


def test_message_context():
    current_chat_response = CartonCapsClient.get_current_chat()
    current_chat_json = json.loads(current_chat_response.text)
    chat_id = current_chat_json["id"]

    first_message_text = "How do I refer a friend? Only give me the first step."
    message_response = CartonCapsClient.create_message(chat_id, first_message_text)
    message_response_json = json.loads(message_response.text)
    response_text = message_response_json["response_text"]

    assert "account icon" in response_text

    # Now send a second message ensuring that we have maintained context from the last one.
    second_message_text = "Now give me the next step."
    message_response = CartonCapsClient.create_message(chat_id, second_message_text)
    message_response_json = json.loads(message_response.text)

    response_text = message_response_json["response_text"]
    assert "invite friends" in response_text.lower()


def test_send_irrelevant_message():
    current_chat_response = CartonCapsClient.get_current_chat()
    current_chat_json = json.loads(current_chat_response.text)
    chat_id = current_chat_json["id"]

    message_text = "What's your favorite kind of tree?"
    message_response = CartonCapsClient.create_message(chat_id, message_text)
    message_response_json = json.loads(message_response.text)

    assert message_response_json["chat_id"] == chat_id
    assert message_response_json["user_text"] == message_text
    assert message_response_json["moderation_code"] is None
    assert not message_response_json["is_terminal"]

    response_text = message_response_json["response_text"]
    assert "try asking about" in response_text


def test_list_messages():
    current_chat_response = CartonCapsClient.get_current_chat()
    current_chat_json = json.loads(current_chat_response.text)
    chat_id = current_chat_json["id"]

    messages_response = CartonCapsClient.list_messages(chat_id)
    messages_response_json = json.loads(messages_response.text)
    initial_message_count = len(messages_response_json)

    message_text = "What's your favorite kind of tree?"
    new_message_response = CartonCapsClient.create_message(chat_id, message_text)
    new_message_json = json.loads(new_message_response.text)

    messages_response = CartonCapsClient.list_messages(chat_id)
    messages_response_json = json.loads(messages_response.text)
    final_message_count = len(messages_response_json)

    assert final_message_count == initial_message_count + 1
    assert new_message_json == messages_response_json[0]
