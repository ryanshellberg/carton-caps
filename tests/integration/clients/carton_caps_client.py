import logging
import requests

API_URL = "http://web:8000/v1"

_logger = logging.getLogger(__name__)


class CartonCapsClient:
    @staticmethod
    def create_chat(raise_for_status=True):
        request_url = f"{API_URL}/chats"

        _logger.info(f"Calling POST {request_url}")
        response = requests.post(request_url)
        _logger.info(f"Response code: {response.status_code}")
        _logger.info(f"Response text: {response.text}")
        if raise_for_status:
            response.raise_for_status()
        return response

    @staticmethod
    def get_current_chat(raise_for_status=True):
        request_url = f"{API_URL}/chats/current"

        _logger.info(f"Calling GET {request_url}")
        response = requests.get(request_url)
        _logger.info(f"Response code: {response.status_code}")
        _logger.info(f"Response text: {response.text}")
        if raise_for_status:
            response.raise_for_status()
        return response

    @staticmethod
    def create_message(chat_id, text, raise_for_status=True):
        request_url = f"{API_URL}/chats/{chat_id}/messages"
        body = {"text": text}
        _logger.info(f"Calling POST {request_url} with {body}")
        response = requests.post(request_url, json=body)
        _logger.info(f"Response code: {response.status_code}")
        _logger.info(f"Response text: {response.text}")
        if raise_for_status:
            response.raise_for_status()
        return response

    @staticmethod
    def list_messages(chat_id, raise_for_status=True):
        request_url = f"{API_URL}/chats/{chat_id}/messages"

        _logger.info(f"Calling GET {request_url}")
        response = requests.get(request_url)
        _logger.info(f"Response code: {response.status_code}")
        _logger.info(f"Response text: {response.text}")

        if raise_for_status:
            response.raise_for_status()
        return response
