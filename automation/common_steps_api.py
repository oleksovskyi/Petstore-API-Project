import requests
import json
import os
from allure import step


BASE_URL = "https://petstore.swagger.io/v2"


def load_payload(file_name):
    """Load JSON payload from the payloads folder."""
    payload_path = os.path.join(os.path.dirname(__file__), 'payloads', file_name)
    with open(payload_path, 'r') as file:
        return json.load(file)


@step("Send POST request to {endpoint}")
def post_request(endpoint, data=None, files=None):
    """Send a POST request."""
    url = f"{BASE_URL}{endpoint}"
    response = requests.post(url, json=data, files=files)
    return response


@step("Send PUT request to {endpoint}")
def put_request(endpoint, data=None):
    """Send a PUT request."""
    url = f"{BASE_URL}{endpoint}"
    response = requests.put(url, json=data)
    return response


@step("Send GET request to {endpoint}")
def get_request(endpoint, params=None):
    """Send a GET request."""
    url = f"{BASE_URL}{endpoint}"
    response = requests.get(url, params=params)
    return response


@step("Send DELETE request to {endpoint}")
def delete_request(endpoint):
    """Send a DELETE request."""
    url = f"{BASE_URL}{endpoint}"
    response = requests.delete(url)
    return response
