import json
from integration.clients.carton_caps_client import CartonCapsClient


# Since there is currently no way to end a chat though the API, we're not checking for a missing current chat.
def test_create_chat_and_get_current():
    new_chat = CartonCapsClient.create_chat()
    current_chat = CartonCapsClient.get_current_chat()
    assert new_chat.text == current_chat.text

    chat_json = json.loads(new_chat.text)
    assert chat_json["is_active"]
