import pytest
from common.utils import get_configs
from server import check_message


CONFIGS = get_configs()

test_error_message = {CONFIGS.get("RESPONSE"): 400, CONFIGS.get("ERROR"): "Bad request"}

test_correct_message = {
    CONFIGS.get("RESPONSE"): 200,
    CONFIGS.get("ALERT"): "Привет, клиент!",
}


def test_check_not_full_message():
    assert check_message({"action": "presence", "type": "status"}) == test_error_message


def test_check_correct_message():
    test_message = {
        "action": "presence",
        "time": "Sat Feb 13 02:17:51 2021",
        "type": "status",
        "user": {"account_name": "Trofimowova", "status": "Hello, server!"},
    }
    assert check_message(test_message) == test_correct_message


def test_check_message_wrong_user():
    test_message = {
        "action": "presence",
        "time": "Sat Feb 13 02:17:51 2021",
        "type": "status",
        "user": {"account_name": "Nolan Grayson", "status": "Think , Mark! Think!"},
    }
    assert check_message(test_message) == test_error_message



