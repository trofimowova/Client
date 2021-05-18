import pickle
import pytest
from socket import socket, AF_INET, SOCK_STREAM
from common.utils import get_configs, send_message, get_message


class Test_Socket:
    CONFIGS = get_configs()

    def __init__(self, test_message):
        self.test_message = test_message
        self.encoded_message = None
        self.received_message = None

    def send(self, message_to_send):
        self.encoded_message = pickle.dumps(self.test_message)
        self.received_message = message_to_send

    def recv(self, max_len):
        pickle_test_message = pickle.dumps(self.test_message)
        return pickle_test_message


CONFIGS = get_configs()


def test_get_config_default_port():
    assert CONFIGS["DEFAULT_PORT"] == 7777


def test_get_config_default_encoding():
    assert CONFIGS["ENCODING"] == "utf-8"


def test_get_config_connections():
    assert CONFIGS["MAX_CONNECTIONS"] == 5


def test_get_config_max_package_length():
    assert CONFIGS["MAX_PACKAGE_LENGTH"] == 1024


def setUp(s):
    s.server_addr = CONFIGS["DEFAULT_IP_ADDRESS"]
    s.server_port = CONFIGS["DEFAULT_PORT"]
    s.socket = socket(AF_INET, SOCK_STREAM)


def tearDown(self):
    self.socket.close()


def test_send_message():
    test_message_from_client = {
        "action": "presence",
        "time": 555555,
        "type": "status",
        "user": {"account_name": "trofimowova", "status": "Hello server!"},
    }

    test_socket = Test_Socket(test_message_from_client)
    send_message(test_socket, test_message_from_client, CONFIGS)
    assert test_socket.encoded_message == test_socket.received_message


def test_get_message():
    test_message = {"response": "200", "alert": "test"}
    test_socket = Test_Socket(test_message)
    assert get_message(test_socket, CONFIGS) == {"response": "200", "alert": "test"}
