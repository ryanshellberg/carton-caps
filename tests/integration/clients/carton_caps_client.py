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
        if raise_for_status:
            response.raise_for_status()
        return response

    @staticmethod
    def get_current_chat(raise_for_status=True):
        request_url = f"{API_URL}/chats/current"

        _logger.info(f"Calling GET {request_url}")
        response = requests.get(request_url)
        if raise_for_status:
            response.raise_for_status()
        return response
