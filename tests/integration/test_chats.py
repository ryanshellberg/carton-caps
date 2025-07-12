from integration.clients.carton_caps_client import CartonCapsClient


def test_create_chat_and_get_current():
    new_chat = CartonCapsClient.create_chat()
    current_chat = CartonCapsClient.get_current_chat()
    assert new_chat.text == current_chat.text
